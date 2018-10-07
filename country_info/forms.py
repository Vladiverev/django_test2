from django import forms

from .models import Country, City

class CityForm(forms.ModelForm):

   class Meta:
       model = City
       fields = ('title', 'desc',)

