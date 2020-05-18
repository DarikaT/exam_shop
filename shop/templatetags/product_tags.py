from django import template
from shop.models import Product

register = template.Library()

@register.inclusion_tag('tags/last_products.html')
def get_last_products(count=5):
    products = Product.objects.order_by('id')[:count]
    return {'last_products':products}
