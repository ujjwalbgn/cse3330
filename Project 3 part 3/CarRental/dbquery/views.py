from django.shortcuts import render,redirect
import request
from django.db import connection
from django.http import HttpResponse

from .models import *
from .forms import *
from .sql_query import  *
# Create your views here.

def Customer(request):
    cursor = connection.cursor()

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

        customers = get_all_customer()

        content = {'customers':customers,'form': form}

        return render(request,'dbquery/customer.html',content)


def Vehicle(request):
    cursor = connection.cursor()

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

        vehicles = get_all_vehicle()

        content = {'vehicles': vehicles, 'form': form}

        return render(request, 'dbquery/vehicle.html', content)