from django.db import models
from django.conf import settings
from privileges.models import Prvs, PrvType, FishAsso, FishDist

class UserProfile(models.Model):
    profileType = models.IntegerField()
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assoRelated = models.ForeignKey('privileges.FishAsso', on_delete=models.DO_NOTHING, default = 1)

    class Meta:
        db_table = 'userprofile'

