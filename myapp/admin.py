from django.contrib import admin
from .models import Reviews, Menu, Reservation

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Reviews)
admin.site.register(Menu)

