from django.contrib import admin
from .models import UserComments, Menu, Booking

# Register your models here.
admin.site.register(UserComments)
admin.site.register(Menu)
admin.site.register(Booking)
