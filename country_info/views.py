from django.shortcuts import render
from .models import Country

# Create your views here.

def country_list(request):
    country = Country.objects.order_by("title")
    return render(request, 'country_info/country.html', {'country': country})
