from django.shortcuts import render
from .models import UserProfile
from django.views import generic
from privileges.models import Prvs
from .forms import UserDataForm, UserProfileForm

class ProfileView(generic.ListView):
    template_name = 'profile/profileMain.html'
    model = UserProfile

def user_data_view(request):
    if request.method=='POST':
        form = UserDataForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserDataForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, "profile/userData.html", context)

def profile_data_view(request):
    if request.method=='POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, "profile/profileData.html", context)

def buy_licence_view(request):
    context = {}
    return render(request, "profile/buyLicence.html", context)

def my_licences_view(request):
    context = {}
    return render(request, "profile/myLicences.html", context)