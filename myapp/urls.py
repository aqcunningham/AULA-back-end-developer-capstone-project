from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import reservation_page_view, reservation_api, ReservationViewSet, reservation_staff_view, ReviewsView, about
# MenuListCreateView, BookingListCreateView, Reviews, BookingAPIView, BookingViewSet,SingleMenuItemView, UserViewSet, StaffUserView, add_menu_view, menu_items_view
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

# plain Django views: render HTML
# cant use automatic router method
urlpatterns = [
	path('', views.home, name='home'),
	path('staff/', views.staff_dashboard, name='staff_dashboard'),
	path('staff/register/drf/', views.StaffUserView.as_view(), name='staff_register_drf'),
	path('staff/register/', views.staff_register_page, name='staff_register'),
	path('staff/login/', auth_views.LoginView.as_view(template_name='staff_login.html'), name='staff_login'),
	path('staff/logout/', auth_views.LogoutView.as_view(next_page='home'), name='staff_logout'),
	path('make_reservation/', views.reservation_page_view, name='reservation_page'),
	# an adjacent path to the reservation page, but this one is for the API, not the HTML page
	path('api/make_reservation/', views.reservation_api, name='reservation_api'),
	path('make_reservation/staff/', views.reservation_staff_view, name='reservation_staff'),
	path('menu/', views.menu_items_view, name='menu'),
	path('reviews/', views.ReviewsView, name='reviews'),
	path('about/', views.about, name='about'),

	# # editable menu items:
	# path('add_menu_items/', views.add_menu_view, name='add_menu_view'),
	
	
	# # need to protect, identical to api/bookingscombo:
	# path('bookings/', views.bookings, name='bookings'),
	# # protected:
	# path('all-bookings/', views.all_bookings, name='all_bookings'),
	# path('newuserregistration/', StaffUserView.as_view())
]
# DRF generic / API views: manual path generation
# urlpatterns+=[
# 	path('api/menu/', MenuListCreateView.as_view(), name='api-menu'),
# 	path('api/menu/<int:pk>/', SingleMenuItemView.as_view(), name='api-menu-item'),
# 	path('api/bookings/', ReservationListCreateView.as_view(), name='api-bookings'),
# 	path('api/usercomments/', Reviews.as_view(), name='api-usercomments'),
# 	# only views, no edits:
# 	path('api/bookingsapiview/', BookingAPIView.as_view(), name='api-bookings-apiview'),
# 	# path('api/bookingsviewset/', BookingViewSet.as_view(), name='api-bookings-asviewset'),
# 	# path('api/usersviewset/', UserViewSet.as_view(), name='api-users-viewsetset'),
# ]

# # DRF ViewSets (auto-routed via router)
# # to enable the viewsets/ModelViewSet:
router = DefaultRouter()

router.register('make_reservation/drf', views.ReservationViewSet)
router.register('api/users', views.UserViewSet)

urlpatterns +=router.urls

# # add the login/logout options
urlpatterns +=[
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('api-token-auth/', obtain_auth_token),
]

