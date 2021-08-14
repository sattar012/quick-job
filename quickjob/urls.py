
from django.contrib import admin
from django.urls import path, include
from portal import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('accounts/', include('accounts.urls')),
    path('portal/', include('portal.urls')),
    path('pluto/', include('pluto.urls')),
    path('blogs/', include('blogs.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
