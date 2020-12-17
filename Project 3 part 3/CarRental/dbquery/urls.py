from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.customerView, name="customer"),
    path('', views.customerView, name="customer"),
    path('vehicle', views.vehicleView , name="vehicle"),
    path('search_rental', views.searchRental, name="searchRental"),
    path('book_rental/<str:pk>/', views.bookRental, name="bookRental"),
    path('submit_booking', views.submitBooking, name="submitBooking"),
    path('update_booking', views.updateBooking, name="updateBooking"),
    path('search_booking', views.searchBooking, name="searchBooking"),
    path('customer_search', views.customerSearchView, name="customerSearchView"),
    path('vehicle_search', views.vehicleSearchView, name="vehicleSearchView"),

]