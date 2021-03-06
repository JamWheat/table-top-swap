from django.urls import path
from . import views

urlpatterns = [
  # accounts
  path('accounts/signup/', views.signup, name='signup'),
  path('update_profile/', views.update_profile, name='update_profile'),
  # basic views
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # game views/actions
  path('games/search/', views.games_search, name='games_search'),
  path('games/lookup/', views.game_lookup, name='game_lookup'),
  path('games/bgg_find/', views.bgg_find, name='bgg_find'),
  path('games/add_offer/', views.add_offer, name='add_offer'),
  # offer views/actions
  path('offers/<int:offer_id>/', views.offer_details, name='offer_details'),
  path('offers/<int:pk>/update/', views.OfferUpdate.as_view(), name='offer_update'),
  path('offers/<int:pk>/delete/', views.OfferDelete.as_view(), name='offer_delete'),
  path('offer/search/', views.offer_search, name="offer_search"),
  # user views
  path('users/profile/', views.profile, name='profile'),
  path('users/<int:user_id>/', views.user_page, name='user_page'),
  # messages views/actions
  path('messages/create/', views.message_create, name='message_create'),
  path('messages/send/', views.message_send, name='message_send'),
  path('messages/view/', views.messages_view, name='messages_view'),
  path('messages/<int:pk>/update/', views.MessageUpdate.as_view(), name='message_update'),
  path('messages/<int:pk>/delete/', views.MessageDelete.as_view(), name='message_delete'),
  # reply views/actions
  # path('reply/new', views.reply_new, name='reply_new'),
  path('reply/create', views.reply_create, name='reply_create'),
  path('reply/<int:pk>/update/', views.ReplyUpdate.as_view(), name='reply_update'),
  # path('reply/<int:pk>/delete/', views.ReplyDelete.as_view(), name='reply_delete'),
  path('reply/<int:reply_id>/delete/', views.reply_delete, name='reply_delete'),
]
