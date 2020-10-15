from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .games_search import search, find
from .forms import OfferForm, UserForm, ProfileForm, MessageForm, ReplyForm
from .models import Offer, Message, Reply

# to protect view classes: put LoginRequiredMixin, into the class inheritance

# accounts

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def update_profile(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      #messages.success(request, _('Your profile was successfully updated!'))
      return redirect('/users/profile/')
    #else:
      #messages.error(request, _('Please correct the error below.'))
  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return render(request, 'edit_profile.html', {
    'user_form': user_form,
    'profile_form': profile_form
  })

# home page

def home(request):
  recent = Offer.objects.order_by('-id')[:10]
  return render(request, 'home.html', {'recent': recent})

# about page

def about(request):
  return render(request, 'about.html')

# games views/actions

def games_search(request):
  return render(request, 'games_search.html')

def game_lookup(request):
  results = search(request.POST['query'])
  return render(request, 'games_search.html', { 'results': results })

@login_required
def bgg_find(request):
  result = find(request.POST['objectid'])
  result['title'] = request.POST['title']
  offer_form = OfferForm(initial={ 
    'title': result['title'],
    'bgg_slug': result['bgg_slug'],
    'year_published': result['year_published'],
    'thumbnail': result['thumbnail'],
    'image': result['image'],
    'user': request.user
   })
  return render(request, 'amend_game.html', {'result': result, 'offer_form': offer_form })

@login_required
def add_offer(request):
  form = OfferForm(request.POST)
  if form.is_valid():
    new_offer = form.save(commit=False)
    # new_offer.list_type = 'offer'
    new_offer.save()
  return redirect('/users/profile/')

# offer views/actions

@login_required
def offer_details(request, offer_id):
  offer = Offer.objects.get(id=offer_id)
  return render(request, 'offers/details.html', { 'offer': offer })

class OfferUpdate(LoginRequiredMixin, UpdateView):
  model = Offer
  fields = ['condition', 'comment']

class OfferDelete(LoginRequiredMixin, DeleteView):
  model = Offer
  success_url = '/users/profile/'

@login_required
def offer_search(request):
  offers = Offer.objects.filter(title__icontains=request.POST['query']).exclude(user=request.user)
  return render(request, 'home.html', {'offers':offers})


# user views/actions

@login_required
def profile(request):
  offers = Offer.objects.filter(user=request.user, list_type='O')
  wishes = Offer.objects.filter(user=request.user, list_type='W')
  user = request.user
  return render(request, 'profile.html', { 'offers': offers, 'wishes': wishes, 'user': user})

def user_page(request, user_id):
  user_focus = User.objects.get(id=user_id)
  user_offers = Offer.objects.filter(user=user_id, list_type='O')
  user_wishes = Offer.objects.filter(user=user_id, list_type='W')
  return render(request, 'users/details.html', {
    'user_focus': user_focus,
    'user_offers': user_offers,
    'user_wishes': user_wishes
  })

# messages views and actions

@login_required
def message_create(request):
  message_form = MessageForm(initial={ 
    'sender': request.user.id,
    'receiver': request.POST['receiver']
  })
  return render(request, 'messages/create_message.html', { 'message_form': message_form })

@login_required
def message_send(request):
  form = MessageForm(request.POST)
  if form.is_valid():
    new_message = form.save(commit=False)
    new_message.save()
  return redirect('/messages/view/')

@login_required
def messages_view(request):
  sent_messages = Message.objects.filter(sender=request.user)
  received_messages = Message.objects.filter(receiver=request.user)
  return render(request, 'messages/view_messages.html', { 
    'sent_messages': sent_messages,
    'received_messages': received_messages
  })

class MessageUpdate(LoginRequiredMixin, UpdateView):
  model = Message
  fields = ['message']

class MessageDelete(LoginRequiredMixin, DeleteView):
  model = Message
  success_url = '/messages/view/'

# reply views/actions

# def reply_new(request):
#   message = Message.objects.get(id=request.POST['message'])
#   reply_form = ReplyForm(initial={ 
#     'sender': request.user.id,
#     'message': request.POST['message']
#   })
#   return render(request, 'replies/reply_new.html', { 
#     'reply_form': reply_form ,
#     'message': message
#   })

@login_required
def reply_create(request):
  form = ReplyForm(request.POST)
  if form.is_valid():
    new_message = form.save(commit=False)
    new_message.save()
  return redirect('/messages/view/')

class ReplyUpdate(LoginRequiredMixin, UpdateView):
  model = Reply
  fields = ['reply']

# class ReplyDelete(LoginRequiredMixin, DeleteView):
#   model = Reply
#   success_url = '/messages/view/'

@login_required
def reply_delete(request, reply_id):
  Reply.objects.get(id=reply_id).delete()
  return redirect('/messages/view/')