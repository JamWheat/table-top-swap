from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

CONDITIONS =(
  ('1', 'New'),
  ('2', 'Like New'),
  ('3', 'Good'),
  ('4', 'Fair'),
  ('5', 'Poor'),
)

LISTS =(
  ('O', 'Offer List'),
  ('W', 'Wish List')
)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  icon = models.URLField(max_length=300, blank=True)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()



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
  list_type = models.CharField(
    ('Which list?'),
    max_length=1,
    choices = LISTS
  )

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
  
