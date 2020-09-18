from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from privileges.models import Prvs, PrvType, FishAsso, FishDist

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+', unique=True)
    profileType = models.IntegerField(default=1)
    fish_asso = models.ForeignKey('privileges.FishAsso', on_delete=models.DO_NOTHING, null=True)

    def __str__(selfself):
        return self.user.username

    class Meta:
        db_table = 'userprofile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


