from .models import Product
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