from rest_framework import serializers
from .models import Menu, Reservation, Reviews
from django.contrib.auth.models import User
from djoser.serializers import TokenCreateSerializer

from myapp import models

# admin only:
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'groups']

# for new staff:
class StaffUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user
	
class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'

# full menu details, for admin and staff:
class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'

class PublicMenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ['id', 'item_name', 'description', 'price', 'image']

class ReviewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reviews
		fields = '__all__'

class CustomTokenCreateSerializer(TokenCreateSerializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})