from django.shortcuts import render
from .models import UserProfile
from django.views import generic
from privileges.models import Prvs

class ProfileView(generic.ListView):
    template_name = 'profile/profileMain.html'
    model = UserProfile

    def my_prvs(request, *args, **kwargs):
        obj = Prvs.objects.get(id=1)
        context = {
            'object': obj
        }

        contextText = {
            "texxt": 123,
        }
        return render(request, "profile/profileMain.html", contextText)

