from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect  
from .forms import PersonForm, CarForm 
from .models import Person, Car 


@login_required
def addnew_person(request):  
    print(request.POST)
    if request.method == "POST":  
        form = PersonForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                print('i')
                form.save()  
                return redirect('/database/persones/')  
            except:
                print('errore')  
                pass 
    else:  
        form = PersonForm()  
    return render(request,'persones/index.html',{'form':form}) 

@login_required
def index_person(request):  
    persones = Person.objects.all()  
    return render(request,"persones/show.html",{'persones': persones}) 

@login_required
def update_person(request, id):  
    persones = Person.objects.get(id=id)  
    form =PersonForm(request.POST,request.FILES, instance = persones)  
    if form.is_valid():  
        form.save()  
        return redirect("/database/persones/")  
    return render(request, 'persones/edit.html', {'persones': persones})

@login_required
def destroy_person(request, id):  
    person = Person.objects.get(id=id)  
    person.delete()  
    return redirect("/database/persones/")  

@login_required
def addnew_car(request):  
    if request.method == "POST":  
        form = CarForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/database/cars/')  
            except:  
                pass 
    else:  
        form = CarForm()  
    return render(request,'cars/index.html',{'form':form}) 

@login_required
def index_car(request):  
    persones = Car.objects.all()  
    return render(request,"cars/show.html",{'cars': persones})

@login_required
def update_car(request, id):  
    cars = Car.objects.get(id=id)  
    form = CarForm(request.POST,request.FILES, instance = cars)  
    if form.is_valid():
        print('!')  
        form.save()  
        return redirect("/database/cars/")  
    return render(request, 'cars/edit.html', {'cars': cars}) 

@login_required
def destroy_car(request, id):  
    car = Car.objects.get(id=id)  
    car.delete()  
    return redirect("/database/cars/")