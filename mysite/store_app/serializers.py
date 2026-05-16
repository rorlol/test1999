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
                  'product_image','price','owner']

class ReviewsSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    product = ProductListSerializers()
    class Meta:
        model = Reviews
        fields = ['id','user','product','stars','comment','image','video','created_at']

class ReviewsSimpleSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    class Meta:
        model = Reviews
        fields = ['id','user','product','stars','comment','image','video','created_at']

class ProductDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    sub_category = SubCategorySimpleSerializers()
    owner = UserProfileSerializers()
    images_product = ImageProductSerializers(read_only=True, many=True)
    reviews = ReviewsSimpleSerializers(read_only=True, many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','category','sub_category','get_avg_rating','get_count_rating','product_name','description',
                  'product_image','product_video','price','choose_table','owner',
                  'images_product','reviews']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating
    def get_count_rating(self,obj):
        return obj.get_count_rating

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
