from django.contrib import admin  
from django.urls import path  
from .views import *  

urlpatterns = [  
    path('persones/', index_person, name='persones'),  
    path('persones/addnew',addnew_person, name='addnew'),  
    path('persones/update/<int:id>', update_person, name='update'),  
    path('persones/delete/<int:id>', destroy_person, name='delete'),
    path('cars/', index_car, name='cars'),  
    path('cars/addnew',addnew_car, name='addnew_car'),  
    path('cars/update/<int:id>', update_car, name='update_car'),  
    path('cars/delete/<int:id>', destroy_car, name='delete_car'),  
] 

