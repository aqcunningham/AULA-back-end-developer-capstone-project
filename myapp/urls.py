from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MenuListCreateView, BookingListCreateView, UserCommentListCreateView, BookingAPIView, BookingViewSet,SingleMenuItemView

# plain Django views: render HTML
urlpatterns = [
	path('', views.home, name='home'),
	path('blog/', views.form_view, name='form_view'),
	path('menu_items/', views.menu_view, name='menu_view'),
	path('book/', views.book, name="book"),
	path('bookings/', views.bookings, name='bookings'),
	path('all-bookings/', views.all_bookings, name='all_bookings'),
]
# DRF generic / API views: manual path generation
urlpatterns+=[
	path('api/menu/', MenuListCreateView.as_view(), name='api-menu'),
	path('api/menu/<int:pk>', SingleMenuItemView.as_view(), name='api-menu-item'),
	path('api/bookings/', BookingListCreateView.as_view(), name='api-bookings'),
	path('api/usercomments/', UserCommentListCreateView.as_view(), name='api-usercomments'),
	path('api/bookingsapiview/', BookingAPIView.as_view()),
]

# DRF ViewSets (auto-routed via router)
# to enable the viewsets/ModelViewSet:
router = DefaultRouter()
router.register('api/bookingscombo', BookingViewSet)
router.register('api/users', views.UserViewSet)

urlpatterns +=router.urls

# add the login/logout options
urlpatterns +=[
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

