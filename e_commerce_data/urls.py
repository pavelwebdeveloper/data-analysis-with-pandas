from django.urls import path

from . import views

urlpatterns = [
    path('', views.e_commerce_data, name='e_commerce_data'),
]