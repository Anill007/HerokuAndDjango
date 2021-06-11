from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name="helloworld"),
    path('', views.helloworld2, name="helloworld2"),
]
