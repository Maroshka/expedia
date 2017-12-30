from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Deals(models.Model):
    regionIds = models.PositiveIntegerField(blank=True, null=True)
    minTripStartDate = models.DateField(blank=True, null=True)
    maxTripStartDate = models.DateField(blank=True, null=True)
    lengthOfStay = models.PositiveIntegerField(blank=True, null=True)
    maxStarRating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minStarRating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    maxTotalRate = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minTotalRate = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    maxGuestRating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minGuestRating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])