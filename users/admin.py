from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):# setting the admin display of the profile model
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')
