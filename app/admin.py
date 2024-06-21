from django.contrib import admin
from app.models import Product,Image,Atribute,ProductAtribute,AtributeValue
# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Atribute)
admin.site.register(ProductAtribute)
admin.site.register(AtributeValue)


