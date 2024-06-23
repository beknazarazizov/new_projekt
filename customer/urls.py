from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from root import settings
from customer.views import customers

urlpatterns = [
    path('customers_list',customers,name='customers')
]
