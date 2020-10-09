from django.shortcuts import render
from django.http import HttpResponse

# home page

def home(request):
  return HttpResponse('Home test test')

# about page

def about(request):
  return render(request, 'about.html')
