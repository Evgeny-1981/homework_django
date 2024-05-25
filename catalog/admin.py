from django.contrib import admin

from catalog.models import Category, Product, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'created_at', 'published',)
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at', 'published',)
