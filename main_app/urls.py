from django.urls import path
from . import views

urlpatterns = [
  # accounts
  path('accounts/signup/', views.signup, name='signup'),
  # basic views
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
]
