from django.shortcuts import render
from app.models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'app/index.html',context)


def product_detail(request,product_id):
    product=Product.objects.get(id=product_id)
    atributes=product.get_atribute()
    context={'product':product,
            'atributes':atributes}
    return render(request, 'app/product_details.html',context)