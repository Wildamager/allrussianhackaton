from django.db import models

class Person(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    image = models.ImageField(upload_to='persones')
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_of_update = models.DateTimeField(auto_now=True)
    class Meta:  
        db_table = "employee"

class Car (models.Model):
    owner = models.TextField()
    number = models.TextField(max_length= 32)
    brand = models.TextField()
    image = models.ImageField(upload_to='cars')
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_of_update = models.DateTimeField(auto_now=True)
