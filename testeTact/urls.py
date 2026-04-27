from django.contrib import admin
from django.urls import path, include
from . import views

app_name='site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.site_home, name='home'),
    path('data/', include('data.urls')),
    path('dashboards/', include('dashboards.urls')),
]
