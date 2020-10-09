from django.urls import path
from . import views

urlpatterns = [
  # accounts
  path('accounts/signup/', views.signup, name='signup'),
  # basic views
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # game views
  path('games/search/', views.games_search, name='games_search')
]
