from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    pub_date = models.DateField(null=True)
    price = models.PositiveIntegerField()
    featured = models.BooleanField(default=0)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True)
    image = models.CharField(max_length=190, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.address}"
    
