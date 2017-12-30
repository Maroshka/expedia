from django import forms
from deals.models import Deals
import datetime
from django.utils.safestring import mark_safe

class SubmitDeal(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'
    regionIds = forms.IntegerField(required=False, label=mark_safe('</br></br>Region ID'))
    minTripStartDate = forms.DateField(initial=datetime.date.today, required=False, label=mark_safe('</br></br>Min Trip Start Date'))
    maxTripStartDate = forms.DateField(initial=datetime.date.today, required=False, label=mark_safe('</br></br>Max Trip Start Date'))
    lengthOfStay = forms.IntegerField(required=False, label=mark_safe('</br></br>Length Of Stay'))
    maxStarRating = forms.IntegerField(required=False, label=mark_safe('</br></br>Max Star Rating'))
    minStarRating = forms.IntegerField(required=False, label=mark_safe('</br></br>Min Star RatingD'))
    maxTotalRate = forms.IntegerField(required=False, label=mark_safe('</br></br>Max Total Rate'))
    minTotalRate = forms.IntegerField(required=False, label=mark_safe('</br></br>Min Total Rate'))
    maxGuestRating = forms.IntegerField(required=False, label=mark_safe('</br></br>Max Guest Rating'))
    minGuestRating = forms.IntegerField(required=False, label=mark_safe('</br></br>Min Guest Rating'))
