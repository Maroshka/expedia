from django import forms
from deals.models import Deals
import datetime
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator
class SubmitDeal(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'
    regionIds = forms.IntegerField(required=False, label=mark_safe('</br></br>Region ID'))
    minTripStartDate = forms.DateField(initial=datetime.date.today, required=False, label=mark_safe('</br></br>Min Trip Start Date'))
    maxTripStartDate = forms.DateField(initial=datetime.date.today, required=False, label=mark_safe('</br></br>Max Trip Start Date'))
    lengthOfStay = forms.IntegerField(required=False, label=mark_safe('</br></br>Length Of Stay'))
    maxStarRating = forms.DecimalField(required=False, label=mark_safe('</br></br>Max Star Rating'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minStarRating = forms.DecimalField(required=False, label=mark_safe('</br></br>Min Star RatingD'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    maxTotalRate = forms.DecimalField(required=False, label=mark_safe('</br></br>Max Total Rate'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minTotalRate = forms.DecimalField(required=False, label=mark_safe('</br></br>Min Total Rate'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    maxGuestRating = forms.DecimalField(required=False, label=mark_safe('</br></br>Max Guest Rating'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
    minGuestRating = forms.DecimalField(required=False, label=mark_safe('</br></br>Min Guest Rating'), max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])
