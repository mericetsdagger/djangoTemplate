"""djangoTemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from home.views import home_view
from userProfile.views import user_data_view, profile_data_view, buy_licence_view, my_licences_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('userProfile.urls')),
    url('accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    path('', home_view, name='home'),
    path('userData', user_data_view),
    path('profileData', profile_data_view),
    path('buyLicence', buy_licence_view),
    path('myLicences', my_licences_view),
]
