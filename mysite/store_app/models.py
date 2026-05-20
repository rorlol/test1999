from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


USER_STATUS = (
('gold','gold'),
('silver','silver'),
('bronze','bronze'),
('simple','simple')
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(16), MaxValueValidator(80)])

    phone_number = PhoneNumberField(region='KG', default='+996')
    profile_image = models.ImageField(null=True,blank=True)
    status = models.CharField(max_length=100,choices=USER_STATUS, default='simple')

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField()

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
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
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum([i.stars for i in reviews]) / reviews.count()
        return 0

    def get_count_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return reviews.count()
        return 0

class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_product')
    image = models.ImageField()

class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i,str(i))for i in range(1,6)])
    image = models.ImageField(null=True,blank=True)
    video = models.FileField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.product}'

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def get_all_sum_product(self):
        items = self.items.all()
        all_sum =  sum([i.get_sum_product() for i in items])
        discount = 0
        if self.user.status == 'gold':
            discount = 0.70
        elif self.user.status == 'silver':
            discount = 0.50
        elif self.user.status == 'bronze':
            discount = 0.25

        finally_sum = all_sum * (1 - discount)
        return f'old sum: {all_sum}, discount:{round(100 * discount)}%, finally sum: {finally_sum}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_sum_product(self):
        return self.product.price * self.quantity

class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)