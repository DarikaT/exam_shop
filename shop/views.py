from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .mixins import GetQuerySetMixin

class ProductListView(GetQuerySetMixin, ListView):
    model = Product 
    template_name = 'product_list.html'
    paginate_by = 6
    ordering = ('-date',)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class CategoryListView(ListView):
    model = Category
    template_name = ('product_list.html', 'product_detail.html')
    


