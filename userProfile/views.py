from django.shortcuts import render
from .models import UserProfile
from django.views import generic
from privileges.models import Prvs
from .forms import UserDataForm

class ProfileView(generic.ListView):
    template_name = 'profile/profileMain.html'
    model = UserProfile

def user_data_view(request):
    form = UserDataForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "profile/userData.html", context)