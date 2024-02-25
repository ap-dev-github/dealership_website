from django.contrib import admin
from .models import CarModel, CarMake

admin.site.register(CarMake)
admin.site.register(CarModel)