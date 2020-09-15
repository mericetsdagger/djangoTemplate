from django.db import models

class PrvType(models.Model):
    fishingDistrictId = models.ForeignKey('FishDist', on_delete=models.DO_NOTHING)
    #szczegóły dograć z Jarkiem
    class Meta:
        db_table = 'prv_type'

class FishAsso(models.Model):
    associationName = models.CharField(max_length=200)
    fishingDistrictId = models.ForeignKey('FishDist', on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'fish_asso'

class FishDist(models.Model):
    districtName = models.CharField(max_length=250)
    localization = models.CharField(max_length=100)
    class Meta:
        db_table = 'fish_dist'

class Prvs(models.Model):
    profileId = models.ForeignKey('userProfile.UserProfile', on_delete=models.CASCADE)
    prvTypeId = models.ForeignKey('PrvType', on_delete=models.DO_NOTHING)
    #szczegoly dogadac z Jarkiem
    class Meta:
        db_table = 'prvs'