from django.shortcuts import render
from .forms import CommentForm, MenuForm, BookingForm
from .models import UserComments, Menu, Booking
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
import json
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView 
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from .serializers import MenuSerializer, BookingSerializer, UserCommentsSerializer, UserSerializer, StaffUserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# added to the views that need auth, work for Class Based Views only CBV:
# @api_view()
# @permission_classes([IsAuthenticated])


# functino based view FBV
def home(request):
	return render(request, 'index.html')

def form_view(request):
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			# can skip?
			# cldt = form.cleaned_data
			# uc = UserComments(
			# 	first_name = cldt['first_name'],
			# 	last_name = cldt['last_name'],
			# 	comment = cldt['comment']
			# )
			form.save()
			return JsonResponse({'message': 'success'})
	return render(request, 'blog.html', {'form': form})

def menu_view(request):
	form = MenuForm()
	if request.method == "POST":
		form = MenuForm(request.POST)
		if form.is_valid():
			# cleanD = form.cleaned_data
			# mf = Menu(
			# 	item_name = cleanD['item_name'],
			# 	category = cleanD['category'],
			# 	description = cleanD['description']
			# )
			form.save()
			return JsonResponse({'message': 'success'})
	return render(request, 'menu_items.html', {'form': form})

def book(request):
	form = BookingForm()
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'message': 'success'})
	return render(request, 'book.html', {'form': form})

# @login_required
@csrf_exempt	
def bookings(request):
	# this version from prev lab:
	# show map and  a header All Reservations
	# date = request.GET.get('date', datetime.today().date())
	# bookings = Booking.objects.all()
	# booking_json = serializers.serialize('json', bookings)
	# return render(request, 'bookings.html', {'bookings': booking_json})
	if request.method == 'POST':
		data = json.load(request)
		exist = Booking.objects.filter(
			reservation_date=data['reservation_date']
			).filter(
				reservation_slot= data['reservation_slot']
				).exists()
		if exist == False:
			booking = Booking(
				first_name=data['first_name'],
				reservation_date=data['reservation_date'],
				reservation_slot=data['reservation_slot'],
				occasion = data.get('occasion', '')
				)
			booking.save()
		else:
			return HttpResponse("{'error': 1}", content_type='application/json')
				
	date = request.GET.get('date', datetime.today().date())
	if date == '':
		date = datetime.today().date()
	bookings = Booking.objects.all().filter(reservation_date=date)
	booking_json = serializers.serialize('json', bookings)
	return HttpResponse(booking_json, content_type='application/json') 

@api_view()
@permission_classes([IsAuthenticated])
def all_bookings(request):
	# to show the bookings just for today:
	# date = request.GET.get('date', datetime.today().date())
	# if date == '':
	# 	date = datetime.today().date()
	# bookings = Booking.objects.all().filter(reservation_date=date)
	bookings = Booking.objects.all()
	booking_json = serializers.serialize('json', bookings)
	return render(request, 'bookings.html', {'bookings': booking_json})



# adding new views, due to addition of serializers (to convert Model data to JSON)
class MenuListCreateView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticated]

class BookingListCreateView(generics.ListCreateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]

class UserCommentListCreateView(generics.ListCreateAPIView):
	queryset = UserComments.objects.all()
	serializer_class = UserCommentsSerializer
	permission_classes = [IsAuthenticated]


# different type of view - APIView:
class BookingAPIView(APIView):
	def get(self, request):
		items = Booking.objects.all()
		serializer = BookingSerializer(items, many = True)
		return Response(serializer.data)
	# def post()
	permission_classes = [IsAuthenticated]

#the most automatic combo view version that does everything w viewsets:
class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAdminUser]

# admin only view: registration, edit, roles etc
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAdminUser]

# any new staff registration:
class StaffUserView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = StaffUserSerializer
	permission_classes = [permissions.AllowAny]


# for testing the auth:
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
	return Response({"message":"This view is protected"})