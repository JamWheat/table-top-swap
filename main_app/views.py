from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .games_search import search


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

# home page

def home(request):
  return render(request, 'home.html')

# about page

def about(request):
  return render(request, 'about.html')

# games views

def games_search(request):
  return render(request, 'games_search.html')

def bgg_search(request):
  results = search(request.POST['query'])
  return render(request, 'games_search.html', { 'results': results })

