# Create your models here.
import uuid
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_slug(self, *args, **kwargs):
        random_id = str(uuid.uuid4()).hex[:6]
        slug = ''.join([random_id, self.name])
        return slug
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    class Weight(models.TextChoices):
        GRAMS_250 = '250', '250g'
        GRAMS_500 = '500', '500g'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    weight = models.CharField(max_length=10, choices=Weight.choices, default=Weight.GRAMS_250)  # e.g., "250g", "500g", "Whole Bean"
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=100, unique=True)
    
    def generate_sku(self, *args, **kwargs):
        sku = '-'.join([self.product.name[:3].upper(), self.weight])
        return sku

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sku
    
