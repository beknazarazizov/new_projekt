from datetime import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from customer.managers import CustomUserManager


# Create your models here.

class Customer(models.Model):
    full_name=models.CharField(max_length=155,null=True,blank=True,verbose_name='To`liq ismi sharifi')
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13,verbose_name='Telefon raqam')
    address=models.CharField(max_length=150,verbose_name='Manzili')
    joined=models.DateTimeField(default=datetime.now(),verbose_name='qo`shilgan vaqti')
    image=models.ImageField(upload_to='customer/customer_img',null=True,blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-joined',)
        verbose_name_plural = 'Xaridorlar'


class User(AbstractUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=155,null=True,blank=True)
    birth_of_date=models.DateField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)

    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email