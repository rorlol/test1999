#from os.path import basename

from django.urls import path,include
from rest_framework import routers
from .views import (UserProfileViewSet,CategoryViewSet,SubCategoryViewSet,ProductListViewSet,
                    ProductDetailViewSet,ImageProductViewSet,ReviewsViewSet,CartViewSet,
                    CartItemViewSet,FavoriteViewSet,RegisterView,CustomLoginView,LogoutView)

router = routers.DefaultRouter()

router.register(r'user_profile', UserProfileViewSet, basename='user_profile')
router.register(r'category',CategoryViewSet,basename='category')
router.register(r'sub_category',SubCategoryViewSet,basename='sub_category')
router.register(r'image_product',ImageProductViewSet,basename='image_product')
router.register(r'reviews',ReviewsViewSet,basename='reviews')
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'cart_item',CartItemViewSet,basename='cart_item')
router.register(r'favorite',FavoriteViewSet,basename='favorite')


urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('product/', ProductListViewSet.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailViewSet.as_view(), name='product_detail'),

    path('cart/', CartViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='cart'),

    #path('cart/', CartViewSet.as_view({'get': 'list'}), name='cart')
]