from django.contrib import admin
from .models import Offer, Profile, Message, Reply
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInline,)

# Register your models here.
admin.site.register(Offer)
admin.site.register(Message)
admin.site.register(Reply)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)