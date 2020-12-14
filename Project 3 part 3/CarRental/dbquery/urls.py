from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.customerView, name="customer"),
    path('vehicle', views.vehicleView , name="vehicle"),

]