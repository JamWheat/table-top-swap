from django.urls import path
from . import views

urlpatterns = [
  # accounts
  path('accounts/signup/', views.signup, name='signup'),
  # basic views
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # game views/actions
  path('games/search/', views.games_search, name='games_search'),
  path('games/bgg_search/', views.bgg_search, name='bgg_search')
]
