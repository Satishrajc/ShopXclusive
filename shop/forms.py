from django import forms
from shop.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
