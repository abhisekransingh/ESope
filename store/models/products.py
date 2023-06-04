from django.db import models
from .category import Category
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    descriptions=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='images')



# Gets all Product
    @staticmethod
    def get_product():
        return Product.objects.all()
    
# Get Products based on filtert
    @staticmethod
    def get_producr_ByCategoryID(category_id):
        return Product.objects.filter(category_id=category_id)
