from django.urls import path
from . import views

urlpatterns = [
    path('', views.enters, name='enters'),
]
