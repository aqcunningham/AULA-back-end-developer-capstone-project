from django.shortcuts import render
# from .forms import Reviews, MenuForm, ReservationForm
from .models import Reviews, Menu, Reservation
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
import json
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView 
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from .serializers import MenuSerializer, ReservationSerializer, ReviewsSerializer, UserSerializer, StaffUserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

# added to the views that need auth, work for Class Based Views only CBV:
# @api_view()
# @permission_classes([IsAuthenticated])

# functino based view FBV
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

# for customer to make a reservation
def reservation_page_view(request):
	return render(request, 'reservation.html')

# api logic for reservation page, to get the bookings for a given date, and to make a new booking
# not visible to the user, but used by the reservation.html page via fetch() in JS
# cusotmer-facing endpoint
def reservation_api(request):
	if request.method == 'POST':
		data = json.load(request)
		exists = Reservation.objects.filter(
			reservation_date=data['reservation_date'],
			).filter(
				reservation_slot=data['reservation_slot']
				).exists()
		if exists == False:
			booking = Reservation(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
                occasion=data.get('occasion', '')
            )
			booking.save()
		else:
			return JsonResponse("{'error': 1}", content_type='application/json', status=400)
			# return JsonResponse({'message': 'Booking already exists for this date and time slot.'}, status=400)
		# return HttpResponse(booking_json, content_type='application/json')
	date = request.GET.get('date', datetime.today().date())
	if date == '':
		date = datetime.today().date()
	bookings = Reservation.objects.all().filter(reservation_date=date)
	booking_json = serializers.serialize('json', bookings)
	return HttpResponse(booking_json, content_type='application/json')

# grants access to Reservation API views if the user is in the 'managers' or 'waiters' group or is a superuser
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            # Only managers/admin can delete
            return [IsManagerGroup()]
        # list, retrieve, create, update, partial_update — waiters and managers both allowed
        return [IsWaiterOrManager()]

# grants access to api views if the user is in the 'managers' group or is a superuser
class IsManagerGroup(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name='managers').exists()

# grants access to api views if the user is in the 'managers' or 'waiters' group or is a superuser
class IsWaiterOrManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name__in=['managers', 'waiters']).exists()

# staff dashboard view, only accessible to logged-in users
@login_required
def reservation_staff_view(request):
    return render(request, 'reservation_staff.html')



# def form_view(request):
# 	form = Reviews()
# 	if request.method == "POST":
# 		form = Reviews(request.POST)
# 		if form.is_valid():
# 			# can skip?
# 			# cldt = form.cleaned_data
# 			# uc = UserComments(
# 			# 	first_name = cldt['first_name'],
# 			# 	last_name = cldt['last_name'],
# 			# 	comment = cldt['comment']
# 			# )
# 			form.save()
# 			return JsonResponse({'message': 'success'})
# 	return render(request, 'reviews.html', {'form': form})

# menu realted views:
# def add_menu_view(request):
# 	form = MenuForm()
# 	if request.method == "POST":
# 		form = MenuForm(request.POST)
# 		if form.is_valid():
# 			# cleanD = form.cleaned_data
# 			# mf = Menu(
# 			# 	item_name = cleanD['item_name'],
# 			# 	category = cleanD['category'],
# 			# 	description = cleanD['description']
# 			# )
# 			form.save()
# 			return JsonResponse({'message': 'success'})
# 	return render(request, 'add_menu_items.html', {'form': form})

def menu_items_view(request):
	menu = Menu.objects.all()
	menu_json = serializers.serialize('json', menu)
	return render(request, 'menu_items.html', {'menu': menu_json})

# adding new views, due to addition of serializers (to convert Model data to JSON)
class MenuListCreateView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticated]

# class Reviews(generics.ListCreateAPIView):
# 	queryset = Reviews.objects.all()
# 	serializer_class = ReviewsSerializer
# 	permission_classes = [IsAuthenticated]

def ReviewsView(request):
	reviews = Reviews.objects.all()
	reviews_json = serializers.serialize('json', reviews)
	return render(request, 'reviews.html', {'reviews': reviews_json})  




# auladmin only view: registration, edit, roles etc
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsManagerGroup]

# any new staff registration:
class StaffUserView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = StaffUserSerializer
	permission_classes = [permissions.AllowAny]

def staff_register_page(request):
	return render(request, 'staff_register.html')
