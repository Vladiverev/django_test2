from django.db import models
from django.utils import timezone
import uuid


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return self.title

