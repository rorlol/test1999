from rest_framework import viewsets, generics, permissions
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite
from .serializers import (UserProfileSerializers,CategorySerializers,SubCategorySerializers,
                          ProductListSerializers,ProductDetailSerializers,ImageProductSerializers,
                          ReviewsSerializers,CartSerializers,CartItemSerializers,FavoriteSerializers)
from rest_framework.filters import SearchFilter,OrderingFilter
from .filter import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CheckOwner

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductListViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['product_name', 'price']
    ordering_fields = ['price']
    filterset_class = ProductFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,CheckOwner]

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = ImageProduct.objects.all()
    serializer_class = ImageProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

