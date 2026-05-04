from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(16), MaxValueValidator(80)])
    profile_image = models.ImageField()

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField()


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_video = models.FileField()
    product_image = models.ImageField()
    price = models.PositiveIntegerField(default=0)
    size_table_choices = (
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
    ('2XL','2XL'),
    ('3XL','3XL'),
    )
    choose_table = models.CharField(max_length=3, choices=size_table_choices)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i,str(i))for i in range(1,6)])
    image = models.ImageField()
    video = models.FileField()
    created_at = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)