from rest_framework import serializers
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name','category_image']

class SubCategorySerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = SubCategory
        fields = ['id','category','subcategory_name']

class SubCategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','category','subcategory_name']

class ImageProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['image']

class ProductListSerializers(serializers.ModelSerializer):
    owner = UserProfileSerializers()
    class Meta:
        model = Product
        fields = ['id','product_name',
                  'product_image','price','owner',]

class ProductDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    sub_category = SubCategorySimpleSerializers()
    owner = UserProfileSerializers()
    images_product = ImageProductSerializers(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id','category','sub_category','product_name','description',
                  'product_image','product_video','price','choose_table','owner',
                  'images_product']

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
