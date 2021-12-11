from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("put_data_to_databasa", views.put_data_to_databasa,name='put_data_to_databasa')
]


