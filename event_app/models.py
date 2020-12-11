from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    mail = models.EmailField()
    counrty = models.CharField(max_length=100,blank=True, null=True)
    phone = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    
class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=True, null=True)
    cost = models.IntegerField()
    location = models.CharField(max_length=100,blank=True, null=True)
    avaliblity = models.CharField(max_length=100,blank=True, null=True)
    note = models.CharField(max_length=100,blank=True, null=True)
    points = models.TextField(blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=100,blank=True, null=True)
    dispatched = models.IntegerField()
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})