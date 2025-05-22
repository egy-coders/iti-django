from django.db import models
from datetime import datetime

class Category(models.Model): # my_category
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        # db_table = 'my_category'

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)
    price = models.PositiveIntegerField() # 1000
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount Percentage i.e.", default=0) # 10%
    featured = models.BooleanField(default=0)
    image = models.ImageField(default="default.png",upload_to="images/product_images", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    branch = models.ManyToManyField(Branch)

    class Meta:
        verbose_name = 'Our Products'
        verbose_name_plural = 'Our Products'

    def final_price(self):
        """
        Calculate and return new price 
        """
        if self.discount:
            discount_amount = (10 / 100) * (self.price) # 100
            return self.price - discount_amount #1000 - 100
        return self.price

    def __str__(self):
        return f"{self.name}"
    
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL , null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=200, choices=STATUS, null=True)

    def __str__(self):
        return f"{self.customer} | {self.product} | {self.status}"
 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.created_at}"