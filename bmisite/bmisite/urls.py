from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bmi/', include('bmi.urls')),
    path('admin/', admin.site.urls),
]