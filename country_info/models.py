from django.db import models
import uuid


class Country(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return self.title    
    
    class Meta:
        ordering = ['title']



class City(models.Model):
    country_id = models.ForeignKey('country_info.Country', on_delete=models.CASCADE, null=True , related_name='cities')
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.title    

    class Meta:
        ordering = ['title']



