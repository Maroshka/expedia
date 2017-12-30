from rest_framework import serializers
from .models import Deals

class EmbedSerializer(serializers.ModelSerializer):


    regionIds = serializers.IntegerField(required=False)
    minTripStartDate = serializers.DateField(required=False)
    maxTripStartDate = serializers.DateField(required=False)
    lengthOfStay = serializers.IntegerField(required=False)
    maxStarRating = serializers.IntegerField(required=False)
    minStarRating = serializers.IntegerField(required=False)
    maxTotalRate = serializers.IntegerField(required=False)
    minTotalRate = serializers.IntegerField(required=False)
    maxGuestRating = serializers.IntegerField(required=False)
    minGuestRating = serializers.IntegerField(required=False)