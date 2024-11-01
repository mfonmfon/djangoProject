import collection
from rest_framework import serializers

from store.models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # inventory = serializers.IntegerField(max_value=255)
    class meta:
        model = Product
        fields = ['title', 'description', 'price', 'inventory', 'collection']
    collection = serializers.StringRelatedField()

class CollectionSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    #
    class Meta:
        model = Collection
        fields = ['title']
