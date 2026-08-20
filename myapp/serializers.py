from rest_framework import serializers
from .models import Menu, Booking, UserComments
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'

class UserCommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserComments
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'groups']