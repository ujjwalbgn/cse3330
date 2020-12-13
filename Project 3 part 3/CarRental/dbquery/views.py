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
        # cursor.execute('''SELECT * FROM Customer''')
        # customers = cursor.fetchall()

        customers = get_all_customer()

        content = {'customers':customers,'form': form}

        # return HttpResponse(customers)
        return render(request,'dbquery/customer.html',content)

