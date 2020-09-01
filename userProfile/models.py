from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    profileType = models.IntegerField()
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'userprofile'

