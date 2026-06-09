from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.urls import path, include


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('departments/', include('departments.urls')),
    path('courses/', include('courses.urls')),
    path("api/", include("university_portal.api_urls")),
]