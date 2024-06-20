from django.contrib import admin
from .models import ProductType, ProductPicture, Manufacturer, Product

# Register your models here.

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):

    list_display = ('name',)
    ordering = ('name',)


admin.site.register(Product)
admin.site.register(ProductPicture)