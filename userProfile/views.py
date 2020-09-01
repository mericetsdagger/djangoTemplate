from django.shortcuts import render
from .models import UserProfile
from django.views import generic

class ProfileView(generic.ListView):
    template_name = 'profile/profileMain.html'
    model = UserProfile