from django.urls import path
from .views import *
from .models import Product

urlpatterns = [
   
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail_url'),
    path('', ProductListView.as_view(), name='product_list_url'),
]