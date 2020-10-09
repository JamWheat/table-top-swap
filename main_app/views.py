from django.shortcuts import render

# home page

def home(request):
  return render(request, 'home.html')

# about page

def about(request):
  return render(request, 'about.html')
