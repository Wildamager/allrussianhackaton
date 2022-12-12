from django import forms  
from .models import Camers

class CameraForm(forms.ModelForm):  
    class Meta:  
        model = Camers  
        fields = ['location', 'ip', 'port', 'login', 'password'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'location': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'ip': forms.TextInput(attrs={ 'class': 'form-control' }),
            'port': forms.TextInput(attrs={ 'class': 'form-control' }),
            'login': forms.TextInput(attrs={ 'class': 'form-control' }, ),
            'password': forms.TextInput(attrs={ 'class': 'form-control' }, ),
        }