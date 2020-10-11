from django.forms import ModelForm
from .models import Offer, Profile
from django import forms
from django.contrib.auth.models import User

class OfferForm(ModelForm):
  class Meta:
    model = Offer
    # fields = ['title', 'bgg_slug', 'year_published', 'image', 'thumbnail', 'condition', 'comment']
    # exclude = ['title', 'bgg_slug', 'year_published', 'image', 'thumbnail', 'user']
    fields = '__all__'
    widgets = {
      'user': forms.HiddenInput(),
      'title': forms.HiddenInput(),
      'bgg_slug': forms.HiddenInput(),
      'image': forms.HiddenInput(),
      'thumbnail': forms.HiddenInput(),
      'year_published': forms.HiddenInput(),
    }

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ('icon',)