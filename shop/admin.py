from django.contrib import admin

from shop.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available']
    list_filter = ['is_available', 'create_date', 'category']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['category', ]
    actions = ("make_available",)

    def make_available(self, request, queryset):
        rows = queryset.update(is_available=True)
        self.message_user(request, f'Action Done On {rows} Items Successfully!')

    make_available.short_description = 'Make Selected Items Available'
