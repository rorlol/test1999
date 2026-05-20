from rest_framework import serializers
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

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

class CartItemSerializers(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ['id','product','quantity']

class CartItemSimpleSerializers(serializers.ModelSerializer):
    product = ProductListSerializers()
    get_sum_product = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','get_sum_product']

    def get_sum_product(self,obj):
        return obj.get_sum_product

class CartSerializers(serializers.ModelSerializer):
    items = CartItemSimpleSerializers(read_only=True,many=True)
    user = UserProfileSerializers()
    get_all_sum_product = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','user','items','get_all_sum_product']

    def get_all_sum_product(self,obj):
        return obj.get_all_sum_produc()

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
