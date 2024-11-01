# from itertools import product
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Collection
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "description", "inventory_status", "collections"]
    list_per_page = 10
    list_editable = ["price", "description"]
    search_fields = ["title"]

    @admin.display(ordering='-inventory')
    def inventory_status(self, product: Product):
        if product.inventory > 20:
            return "LOW"
        return "HIGH"

@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["title", "product_count"]
    list_per_page = 10
    search_fields = ["title"]

    def product_count(self, collection: Collection):
        return collection.product_set.count()




