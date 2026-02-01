from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index),
    path('register', views.my_form_view),
    path('', views.enter_view),
]
