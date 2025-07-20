# listings/serializers.py

from rest_framework import serializers
from .models import Listing, Booking
# from django.contrib.auth import authenticate, get_user_model


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# User = get_user_model()
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'password']
#         extra_kwargs = {"password": {"write_only": True}}


# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'password']
#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


# class LoginUserSerializer(serializers.Serializer):
#     """
#     Serializer class to authenticate users with email and password.
#     """
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")
    

# class ListingSerializer(serializers.ModelSerializer):
#     host = serializers.StringRelatedField(read_only=True)  # or use nested if needed

#     class Meta:
#         model = Listing
#         fields = [
#             'id',
#             'host',
#             'name',
#             'description',
#             'location',
#             'price_per_night',
#             'created_at',
#             'updated_at'
#         ]
#         read_only_fields = ['id', 'host', 'created_at', 'updated_at']


# class BookingSerializer(serializers.ModelSerializer):
#     guest = serializers.StringRelatedField(read_only=True)
#     property = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Booking
#         fields = [
#             'id',
#             'property',
#             'guest',
#             'start_date',
#             'end_date',
#             'total_price',
#             'status',
#             'created_at',
#         ]
#         read_only_fields = ['id', 'guest', 'status', 'created_at']



# class ReviewSerializer(serializers.ModelSerializer):
#     reviewer = serializers.StringRelatedField(read_only=True)
#     property = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Review
#         fields = [
#             'id',
#             'property',
#             'reviewer',
#             'rating',
#             'comment',
#             'created_at'
#         ]
#         read_only_fields = ['id', 'reviewer', 'created_at']

# class PaymentSerializer(serializers.ModelSerializer):
#     booking = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Payment
#         fields = [
#             'id',
#             'booking',
#             'amount',
#             'payment_date',
#             'payment_method'
#         ]
#         read_only_fields = ['id', 'payment_date']