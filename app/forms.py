from django import forms
from app.models import  Product


class ProductForm(forms.Form):
    title=forms.CharField(max_length=100)
    descriptions=forms.CharField(widget=forms.Textarea)
    price=forms.FloatField()
    reting=forms.FloatField()
    discount=forms.IntegerField()
    quantity=forms.IntegerField()

class ProductMdelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['title','descriptions','price','reting','discount','quantity']
        exclude=()