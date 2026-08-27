from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import reservation_page_view, reservation_api
# MenuListCreateView, BookingListCreateView, Reviews, BookingAPIView, BookingViewSet,SingleMenuItemView, UserViewSet, StaffUserView, add_menu_view, menu_items_view
from rest_framework.authtoken.views import obtain_auth_token

# plain Django views: render HTML
# cant use automatic router method
urlpatterns = [
	path('', views.home, name='home'),
	path('reservation/', views.reservation_page_view, name='reservation_page'),
	path('api/reservation/', views.reservation_api, name='reservation_api'),
	path('menu/', views.menu_items_view, name='menu'),
	path('reviews/', views.form_view, name='reviews'),

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
# router.register('api/bookingscombo', BookingViewSet)
router.register('api/users', views.UserViewSet)

urlpatterns +=router.urls

# # add the login/logout options
urlpatterns +=[
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('api-token-auth/', obtain_auth_token),
]

