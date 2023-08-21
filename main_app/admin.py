from django.contrib import admin
from .models import Property, Renting, Amenity

# Register your models here.
admin.site.register(Property)
admin.site.register(Renting)
admin.site.register(Amenity)