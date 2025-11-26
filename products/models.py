from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, help_text="Emoji or icon name")
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='kg', help_text="e.g., kg, bag, piece")
    quantity_available = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']