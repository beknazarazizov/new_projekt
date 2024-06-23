from django.shortcuts import render
from app.models import Product
from app.forms import ProductModelForm
from app.forms import ProductForm
from django.shortcuts import redirect
# Create your views here.
def index(request):
    products=Product.objects.all().order_by('-id')[2:4]
    context={'products':products}
    return render(request, 'app/index.html',context)


def product_detail(request,product_id):
    product=Product.objects.get(id=product_id)
    atributes=product.get_atribute()
    context={'product':product,
            'atributes':atributes}
    return render(request, 'app/product_details.html',context)
#
# def add_product(request):
#     form=ProductForm()
#     if request.method == 'POST':
#         form=ProductForm(request.POST)
#         title= request.POST['title']
#         descriptions=request.POST['descriptions']
#         price=request.POST['price']
#         reting=request.POST['reting']
#         discount=request.POST['discount']
#         quantity=request.POST['quantity']
#         product=Product(title=title,descriptions=descriptions,price=price,reting=reting,discount=discount,quantity=quantity)
#         if form.is_valid():
#             product.save()
#             return redirect('index')
#
#     else:
#         form=ProductForm()
#     context={
#         'form' : form
#     }
#     return render(request,'app/add_product.html',context)

def add_product(request):
    form = ProductModelForm()
    if request.method =='POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form' : form
    }
    return render(request,'app/add_product.html',context)