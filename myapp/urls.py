from django.urls import path
from . import views

urlpatterns = [
    path('1', views.helloworld, name="helloworld"),
    path('2', views.helloworld2, name="helloworld2"),
]
