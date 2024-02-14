from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'category','quantity']

admin.site.register(Author)
admin.site.register(Post)



