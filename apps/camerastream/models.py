from django.db import models

# Create your models here.
class Camers(models.Model):
    location = models.CharField(max_length=126)
    ip = models.CharField(max_length=20)
    port = models.CharField(max_length=10,blank = True)
    login = models.CharField(max_length=26, blank=True)
    password = models.CharField(max_length=126, blank=True)
    time_of_creation = models.DateTimeField(auto_now_add=True)

class EntryLog(models.Model):
    location = models.CharField(max_length=126)
    name = models.CharField(max_length=126)
    date = models.CharField(max_length=126)

class FalseEntryLog(models.Model):
    location = models.CharField(max_length=126)
    image = models.ImageField(upload_to='false_entry')
    date = models.CharField(max_length=126)