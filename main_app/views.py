from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .games_search import search, find
from .forms import OfferForm, UserForm, ProfileForm
from .models import Offer


# to protect view functions: decorate with @login_required
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
  return render(request, 'home.html')

# about page

def about(request):
  return render(request, 'about.html')

# games views/actions

def games_search(request):
  return render(request, 'games_search.html')

def bgg_search(request):
  results = search(request.POST['query'])
  return render(request, 'games_search.html', { 'results': results })

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

def add_offer(request):
  form = OfferForm(request.POST)
  if form.is_valid():
    new_offer = form.save(commit=False)
    # new_offer.list_type = 'offer'
    new_offer.save()
  return redirect('/users/profile/')

# offer views/actions

def offer_details(request, offer_id):
  offer = Offer.objects.get(id=offer_id)
  return render(request, 'offers/details.html', { 'offer': offer })

class OfferUpdate(UpdateView):
  model = Offer
  fields = ['condition', 'comment']

class OfferDelete(DeleteView):
  model = Offer
  success_url = '/users/profile/'


# user views/actions

def profile(request):
  offers = Offer.objects.filter(user=request.user, list_type='O')
  wishes = Offer.objects.filter(user=request.user, list_type='W')
  user = request.user
  return render(request, 'profile.html', { 'offers': offers, 'wishes': wishes, 'user': user})

