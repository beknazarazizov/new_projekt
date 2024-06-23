from django.shortcuts import render
from customer.models import Customer
# Create your views here.

def customers(request):
    customer_list=Customer.objects.all()
    context={
        'customer_list' : customer_list

    }
    return render(request,'customer/customer_list.html',context)