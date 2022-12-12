from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  
    path('database/', include("apps.data.urls")),
    path('dashboard/', include("apps.camerastream.urls")),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()