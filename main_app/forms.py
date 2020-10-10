from django.forms import ModelForm
from .models import Offer
from django import forms

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