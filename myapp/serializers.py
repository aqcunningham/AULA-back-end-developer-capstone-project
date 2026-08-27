from rest_framework import serializers
from .models import Menu, Reservation, Reviews
from django.contrib.auth.models import User
from djoser.serializers import TokenCreateSerializer

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'



class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'


class UserCommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reviews
		fields = '__all__'

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

class CustomTokenCreateSerializer(TokenCreateSerializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})