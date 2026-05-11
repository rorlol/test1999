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
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }