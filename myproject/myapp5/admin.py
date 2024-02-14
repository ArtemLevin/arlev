from django.contrib import admin
from .models import *

@admin.action(description='Сбросить количество в ноль')
def reset_quntity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'category','quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Search by description'
    actions = [reset_quntity]

    fields = ['name', 'category', 'description', 'rating', 'quantity', 'date_added']
    readonly_fields = ['date_added', 'rating']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
