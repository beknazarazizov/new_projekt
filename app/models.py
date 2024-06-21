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

    def get_atribute(self) ->list[dict]:
        product_atributes=ProductAtribute.objects.filter(product=self)
        atributes=[]
        for pa in product_atributes:
            atributes.append({
                'atribute_key':pa.atribute.key_name,
                'atribute_value':pa.atribute_value.value_name
            })
        return atributes

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1-self.discount / 1000)
        return self.price

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image=models.ImageField(upload_to='product')
    product=models.ForeignKey('app.Product',on_delete=models.SET_NULL,related_name='images',null=True)



class Atribute(models.Model):
    key_name=models.CharField(max_length=125)
    
    def __str__(self):
        return self.key_name




class AtributeValue(models.Model):
    value_name=models.CharField(max_length=125)
    
    def __str__(self):
        return self.value_name
   

class ProductAtribute(models.Model):
    product=models.ForeignKey('app.Product',on_delete=models.CASCADE)
    atribute=models.ForeignKey('app.Atribute',on_delete=models.CASCADE)
    atribute_value=models.ForeignKey('app.AtributeValue',on_delete=models.CASCADE)

#py manage.py makemigrations


