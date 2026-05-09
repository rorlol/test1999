from django.contrib import admin
from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite

class ImageProductInLine(admin.TabularInline):
    model = ImageProduct
    extra = 1

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(ImageProduct)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Favorite)

from modeltranslation.admin import TranslationAdmin
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ImageProductInLine]

    class Media:
        js = (
            'admin/js/jquery.init.js',
            'js/admin/custom.js',
        )

        css = {
            'all': (
                'css/admin/custom.css',
            )
        }