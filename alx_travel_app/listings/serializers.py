from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Booking, Listing, Review, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", "guest"),
        )
        return user


class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)

    class meta:
        model = Listing
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class BookingSerializer(serializers.Serializer):
    property = ListingSerializer(read_only=True)
    customer = UserSerializer(read_only=True)

    class meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        field = "__all__"
        extra_kwargs = {
            "property": {"write_only": True},
            "id": {"read_only": True},
        }


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        extra_kwargs = {
            "booking": {"write_only": True},
            "id": {"read_only": True},
        }




# from rest_framework import serializers
# from .models import Listing, Booking

# class ListingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Listing
#         fields = [
#             'id',
#             'title',
#             'description',
#             'price_per_night',
#             'location',
#             'availability',
#             'created_at',
#             'updated_at'
#         ]


# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = [
#             'id',
#             'listing',
#             'user',
#             'start_date',
#             'end_date',
#             'num_guests',
#             'created_at',
#             'updated_at'
#         ]
