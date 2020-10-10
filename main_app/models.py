from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.

CONDITIONS =(
  ('1', 'New'),
  ('2', 'Like New'),
  ('3', 'Good'),
  ('4', 'Fair'),
  ('5', 'Poor'),
)

class Offer(models.Model):
  title = models.CharField(max_length=200)
  bgg_slug = models.IntegerField()
  year_published = models.IntegerField()
  image = models.CharField(max_length=200)
  thumbnail = models.CharField(max_length=200)
  condition = models.CharField(
    max_length=1,
    choices = CONDITIONS,
    default = CONDITIONS[2][0]
  )
  comment = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse('offer_details', kwargs={'offer_id': self.id})

class Wish(models.Model):
  title = models.CharField(max_length=200)
  bgg_slug = models.IntegerField()
  year_published = models.IntegerField()
  comment = models.TextField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
