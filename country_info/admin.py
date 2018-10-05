from django.contrib import admin
from .models import Country
from .models import City

admin.site.register(Country)
admin.site.register(City)