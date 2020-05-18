from django.contrib import admin
from .models import Category, Product, Favorite, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class ReviewInline():
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'price', 'image', 'quantity', 'url', 'draft')
    list_display_links = ('name',)
    list_filter = ('category__name', 'name', 'price')
    search_fields = ('name', 'price', 'category__name')
    inline = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)


@admin.register(Favorite)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'add', 'product')
    search_fields = ('product',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'product')
    readonly_fields = ('name', 'email')
