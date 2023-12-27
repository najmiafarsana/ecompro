from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CatagoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stoke','available','created','updated']
    list_editable = ['price','stoke','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)