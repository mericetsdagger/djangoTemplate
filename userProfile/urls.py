from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profil/$', views.ProfileView.as_view(), name='profil')
]