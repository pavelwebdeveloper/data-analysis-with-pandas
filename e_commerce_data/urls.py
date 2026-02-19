from django.urls import path

from . import views

urlpatterns = [
    path('', views.e_commerce_data, name='e_commerce_data'),
    path('e_commerce_data_aggregating_statistics/', views.e_commerce_data_aggregating_statistics, name='e_commerce_data_aggregating_statistics'),
    path('e_commerce_data_info/', views.e_commerce_data_info, name='e_commerce_data_info'),
    path('plots/', views.plots, name='plots'),
]