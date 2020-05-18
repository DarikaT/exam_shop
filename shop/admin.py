from django.contrib import admin
from .models import Category, Product, Favorite, Reviews
from django.utils.safestring import mark_safe

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
    list_display = ('id', 'name', 'description', 'category', 'price', 'get_image', 'quantity', 'url', 'draft')
    list_display_links = ('name',)
    list_filter = ('category__name', 'name', 'price')
    search_fields = ('name', 'price', 'category__name')
    inline = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    readonly_fields = ('get_image', )
    actions = ['publish', 'unpublish']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="120"')

    get_image.short_description = 'Изображение'

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была добавлена'
        else:
            message_bit = f'{row_update} записей были добавлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change', )

@admin.register(Favorite)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'add', 'product')
    search_fields = ('product',)
    fieldsets = (
        ('Favorites', {
            'fields': (('product', 'add'),)
        }),
    )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'product')
    readonly_fields = ('name', 'email')


admin.site.site_title = 'Exam Django'
admin.site.site_header = 'Exam Django'