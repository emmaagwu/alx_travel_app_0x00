from rest_framework import serializers
from .models import Listing, Booking

class Listing(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'price_per_night',
            'location',
            'availability',
            'created_at',
            'updated_at'
        ]


class Booking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'user',
            'start_date',
            'end_date',
            'num_guests',
            'created_at',
            'updated_at'
        ]
