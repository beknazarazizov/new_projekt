from django.urls import path

from customer.views.auth import login_page
from customer.views.views import customers, add_customer, delete_customer

urlpatterns = [
    path('customers_list',customers,name='customers'),
    path('add_customer',add_customer,name='add_customer'),
    path('customers/<int:id>',delete_customer,name='delete'),
    path('customer/<int:id>',add_customer,name='edit'),
    path('login_page/',login_page,name='login'),
]
