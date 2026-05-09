from django.contrib import admin
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ImageProduct)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Favorite)

