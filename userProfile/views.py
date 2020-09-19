from django.shortcuts import render
from .models import UserProfile
from django.views import generic
from privileges.models import Prvs

class ProfileView(generic.ListView):
    template_name = 'profile/profileMain.html'
    model = UserProfile

    def my_prvs(request):
        obj = Prvs.objects.get(id=user_id)
        context = {
            'object': obj
        }
        return render(request, template_name, context)

