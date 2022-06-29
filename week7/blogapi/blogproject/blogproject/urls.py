from django.contrib import admin
from django.urls import path, include
import blogapi.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapi.urls')),
]

