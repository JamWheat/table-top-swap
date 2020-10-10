from django.forms import ModelForm
from .models import Offer

class OfferForm(ModelForm):
  class Meta:
    model = Offer
    fields = ['title', 'bgg_slug', 'year_published', 'image', 'thumbnail', 'condition', 'comment', 'designer']