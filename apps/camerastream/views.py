from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .camera import LiveWebCam
from .models import Camers
from .forms import CameraForm
from .DetectionsNumbers import main
from ..data.models import Person, Car
import time


@login_required
def camerslist(request):
    camers = Camers.objects.all()
    return render(request, 'dashboard/dashboard.html', {'camers':camers})

@login_required
def addnew_camera(request):  
    if request.method == "POST":  
        form = CameraForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                print('i') 
                return redirect('/dashboard/camers/')  
            except:  
                print('ere')
                pass 
    else:  
        form = CameraForm()
    return render(request,'dashboard/add.html',{'form':form}) 

@login_required
def index(request, id):
    camera = Camers.objects.filter(id=id)
    return render(request, 'dashboard/camerastream.html', {'camera':camera[0].id})

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@login_required
def webcam_feed(request, id):
    camera = Camers.objects.get(id=id)
    return StreamingHttpResponse(gen(IPWebCam(camera)),
					content_type='multipart/x-mixed-replace; boundary=frame')

def test(camera):
    result=main(camera)
    yield (result)

@login_required
def recognition(request, id):
    print(id)
    camera = Camers.objects.get(id=id)
    return StreamingHttpResponse(test(camera))

@login_required
def livecam_feed(request, id):
    camera = Camers.objects.get(id=id)
    return StreamingHttpResponse(gen(LiveWebCam(camera)),
					content_type='multipart/x-mixed-replace; boundary=frame')

# def test(request):
#     result = main()
#     return HttpResponse(result)