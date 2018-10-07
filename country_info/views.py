from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Country, City
from .forms import CityForm

# Create your views here.

def country_list(request):
    countrys = Country.objects.order_by("title")
    return render(request, 'country_info/country.html', {'countrys': countrys})

def c_city(request, pk):
    countrys = Country.objects.order_by("title")
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'country_info/c_city.html', {'country': country, 'countrys': countrys})

@login_required
def city_add(request, pk):
    countrys = Country.objects.order_by("title")
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.country_id = country
            city.save()
            return redirect('c_city', pk=country.pk)
    else:
        form = CityForm()
    return render(request, 'country_info/city_add.html', {'form': form, 'country': country, 'countrys': countrys})

@login_required
def city_edit(request, pk_count, pk_city):
    countrys = Country.objects.order_by("title")
    country = get_object_or_404(Country, pk=pk_count)
    city = get_object_or_404(City, pk=pk_city)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('c_city', pk=pk_count)
    else:
        form = CityForm(instance=city)
    return render(request, 'country_info/city_edit.html', {'form': form, 'country': country, 'countrys': countrys})

@login_required
def city_remove(request, pk_count, pk_city):
    countrys = Country.objects.order_by("title")
    country = get_object_or_404(Country, pk=pk_count)
    city = get_object_or_404(City, pk=pk_city)
    city.delete()
    return render(request, 'country_info/c_city.html', {'country': country, 'countrys': countrys})