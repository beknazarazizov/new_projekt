from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Product,Image,Atribute,ProductAtribute,AtributeValue
# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Atribute)
admin.site.register(ProductAtribute)
admin.site.register(AtributeValue)

# admin.site.unregister(Group)
# admin.site.unregister(User)


