from django.shortcuts import render,redirect
import request
from django.db import connection
from django.http import HttpResponse
import datetime
from django.contrib import messages


from .models import *
from .forms import *
from .sql_query import  *
# Create your views here.

def customerView(request):
    if request.method == 'POST':
        form = CustomerForms(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data['name'])
            phone = str(form.cleaned_data['phone'])

            new_customer = [name,phone]
            add_new_customer(new_customer)

            return redirect('customer')

    else:
        form = CustomerForms()

        # customers = get_all_customer()

        name_map = {'name': 'name', 'phone': 'phone','pk' : 'CustId'}
        customers = Customer.objects.raw('SELECT * FROM customer',translations=name_map)
        print(customers)
        content = {'customers':customers,'form': form}

        return render(request,'dbquery/customer.html',content)


def vehicleView(request):
    if request.method == 'POST':
        form = VehicleForms(request.POST)
        if form.is_valid():
            vehicleid = str(form.cleaned_data['vehicleid'])
            description = str(form.cleaned_data['description'])
            year = int(form.cleaned_data['year'])
            type = int(form.cleaned_data['type'])
            category = int(form.cleaned_data['category'])

            new_vehicle = [vehicleid, description,year,type,category]

            add_new_vehicle(new_vehicle)
            return redirect('vehicle')

    else:
        form = VehicleForms()

        # vehicles = get_all_vehicle()

        name_map = {'description': 'description', 'year': 'year','type': 'type',
                    'category': 'category','pk' : 'vehicleid'}

        vehicles = Vehicle.objects.raw('SELECT * FROM vehicle',translations=name_map)
        # print(vehicles)
        content = {'vehicles': vehicles, 'form': form}

        return render(request, 'dbquery/vehicle.html', content)

def searchRental(request):

    if request.method == 'POST':
        start_date = str(request.POST['start_date'])

        request.session['rental_start_date'] = start_date

        name_map = {'description': 'description', 'year': 'year', 'type': 'type',
                    'category': 'category', 'pk': 'vehicleid','daily_rate': 'daily_rate'}
        vehicles = Rental.objects.raw(
            'SELECT  DISTINCT vehicle.vehicleid as id, description as description, year as year, rate.type as type, '
            'rate.category as category, rate.Daily as daily_rate '
            '  FROM vehicle, rental, rate WHERE (vehicle.vehicleid NOT IN (SELECT rental.VehicleID from rental) '
            'AND rental.ReturnDate < %s ) AND vehicle.Category = RATE.Category '
            'AND vehicle.Type = rate.Type',[start_date],translations=name_map)

        # print(vehicles)
        content = {'vehicles': vehicles}
        return render(request, 'dbquery/search_rental.html', content)
    else:
        # form = SearchRentalForm()
        content = {}
        return render(request, 'dbquery/search_rental.html', content)

def bookRental(request,pk):
    if request.method == 'POST':
        vehicle_id = pk
        vehicle = Vehicle.objects.get(vehicleid= pk )
        # print(vehicle.description)
        request.session['vehicle_id'] = vehicle_id
        start_date = request.session['rental_start_date']
        form = RentalForms()
        order_date = datetime.date.today().strftime ("%Y-%m-%d")
        request.session['order_date'] = order_date

        content = {'vehicle' : vehicle, 'form':form, 'order_date': order_date, 'start_date':start_date}
        return render(request, 'dbquery/book_rental.html', content)

def submitBooking(request):
    if request.method == 'POST':
        form = RentalForms(request.POST)
        if form.is_valid():
            vehicleid = request.session['vehicle_id']
            start_date = request.session['rental_start_date']
            order_date = request.session['order_date']
            custid = str(request.POST['custid'])
            rentaltype = str(form.cleaned_data['rentaltype'])
            qty = str(form.cleaned_data['qty'])
            returndate = str(form.cleaned_data['returndate'])
            totalamount = str(form.cleaned_data['totalamount'])
            paymentdate = str(form.cleaned_data['paymentdate'])
            returned = str(0)

            rental =[custid,vehicleid,start_date,order_date,rentaltype,qty,returndate,totalamount,paymentdate,returned]
            add_new_rental(rental)
            print(rental)
            messages.success(request, 'Booking has been Saved. You can make another booking.')
            return redirect('searchRental')
