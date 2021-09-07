from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, CreateView, UpdateView,
                                  DetailView, ListView, DeleteView)

# from shop.forms import ProductsForm
from shop.models import Products


class HomeView(TemplateView):
    template_name = 'shop/home.html'


class AddProducts(CreateView):
    template_name = 'shop/add_products.html'
    model = Products
    fields = ('product_name', 'category', 'information')


class ProductListView(ListView):
    template_name = 'shop/products_list.html'
    model = Products
    context_object_name = 'products_list'


class ProductDetailsView(DetailView):
    template_name = 'shop/products_detail.html'
    model = Products
    context_object_name = 'products_detail'


class ProductUpdateView(UpdateView):
    fields = ('product_name', 'category', 'information')
    model = Products


class ProductDeleteView(DeleteView):
    template_name = 'shop/products_confirm_delete.html'
    model = Products
    success_url = reverse_lazy("shop:list")
