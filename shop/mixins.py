from .models import Product, Category
from django.db.models import Q

class GetQuerySetMixin():
    def get_queryset(self):
        query_result = self.request.GET.get('search_name')
        if query_result: 
            queryset = Product.objects.filter(
                Q(name__icontains=query_result)|
                Q(price__icontains=query_result)
            )
        else:
            queryset = Product.objects.all()
        return queryset

class DropdownMixin():
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context