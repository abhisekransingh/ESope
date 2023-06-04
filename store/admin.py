from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.custome import Customes

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','descriptions','image']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,CategoryAdmin)


class CustomAdmin(admin.ModelAdmin):
    list_display=['first_name','email']

admin.site.register(Customes,CustomAdmin)

