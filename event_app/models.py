from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    mail = models.EmailField()
    counrty = models.CharField(max_length=100,blank=True, null=True)
    phone = models.IntegerField()
    message = models.TextField(blank=True, null=True)
