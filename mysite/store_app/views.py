from rest_framework import viewsets, generics
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite
from .serializers import (UserProfileSerializers,CategorySerializers,SubCategorySerializers,
                          ProductListSerializers,ProductDetailSerializers,ImageProductSerializers,
                          ReviewsSerializers,CartSerializers,CartItemSerializers,FavoriteSerializers)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers

class ProductListViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers

class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = ImageProduct.objects.all()
    serializer_class = ImageProductSerializers

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers

