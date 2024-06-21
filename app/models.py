from django.db import models

# Create your models here.



#Product => title,descriptins,price,reting,discount, quantity
# Image => image,product=>fk


class Product(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField(null=True)
    price=models.FloatField()
    reting=models.FloatField()
    discount=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1-self.discount / 1000)
        return self.price

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image=models.ImageField(upload_to='product')
    product=models.ForeignKey('app.Product',on_delete=models.SET_NULL,null=True)

#py manage.py makemigrations
