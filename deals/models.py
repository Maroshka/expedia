from django.db import models

# Create your models here.

class Deals(models.Model):
    regionIds = models.IntegerField(blank=True, null=True)
    minTripStartDate = models.DateField(blank=True, null=True)
    maxTripStartDate = models.DateField(blank=True, null=True)
    lengthOfStay = models.IntegerField(blank=True, null=True)
    maxStarRating = models.IntegerField(blank=True, null=True)
    minStarRating = models.IntegerField(blank=True, null=True)
    maxTotalRate = models.IntegerField(blank=True, null=True)
    minTotalRate = models.IntegerField(blank=True, null=True)
    maxGuestRating = models.IntegerField(blank=True, null=True)
    minGuestRating = models.IntegerField(blank=True, null=True)