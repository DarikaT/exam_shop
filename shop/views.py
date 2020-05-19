from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .mixins import GetQuerySetMixin, DropdownMixin
from django.db.models import Q

class ProductListView(GetQuerySetMixin, DropdownMixin, ListView):
    model = Product 
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        query_result = self.request.GET.get('q')
        if query_result: 
            queryset = Product.objects.filter(
                Q(name__icontains=query_result)|
                Q(price__icontains=query_result)
            )
        else:
            queryset = Product.objects.all()
        return queryset

class ProductDetailView(GetQuerySetMixin, DropdownMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'




