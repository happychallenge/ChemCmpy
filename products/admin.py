from django.contrib import admin

# Register your models here.
from .models import Provider, Tag, Contact, Category, Product, CompanyProduct


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    class Meta:
        model = Provider
    list_display = ['cn_name', 'en_name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
    list_display = ['tag', ]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
    list_display = ['cn_name', 'role', 'email', 'mobile', 'wechat', 'qq']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
    list_display = ['cn_name', 'en_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    list_display = ['cn_name', 'en_name', 'category']

@admin.register(CompanyProduct)
class CompanyProductAdmin(admin.ModelAdmin):
    class Meta:
        model = CompanyProduct
    list_display = ['provider', 'product', 'created_at']



