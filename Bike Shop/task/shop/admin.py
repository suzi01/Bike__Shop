from django.contrib import admin
from .models import Frame, Tire, Bike, Basket, Order, Seat

# Register your models here.

admin.site.register(Frame)
admin.site.register(Tire)
admin.site.register(Seat)
admin.site.register(Basket)
admin.site.register(Bike)
admin.site.register(Order)
