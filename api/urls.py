from django.urls import path

from .views import add_cpu_load

urlpatterns = [
    path('add_cpu_load/', add_cpu_load, name='add_cpu_load'),
]
