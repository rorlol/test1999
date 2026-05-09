from .models import UserProfile,Category,SubCategory,Product,ImageProduct,Reviews,Cart,CartItem,Favorite
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name',)