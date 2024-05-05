from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50)
    rating = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    production_date = models.DateField(null=True, blank=True)
    country_of_origin = models.CharField(max_length=50, blank=True)
    manufacturer = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    anti_counterfeit_code = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.product.name    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()

    def __str__(self):
        return self.product.name