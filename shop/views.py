from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .mixins import GetQuerySetMixin, DropdownMixin

class ProductListView(GetQuerySetMixin, DropdownMixin, ListView):
    model = Product 
    template_name = 'product_list.html'
    paginate_by = 6
    ordering = ('-date',)



class ProductDetailView(DropdownMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'

class Search(ListView):
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context

    


