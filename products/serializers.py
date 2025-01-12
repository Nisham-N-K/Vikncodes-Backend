from rest_framework import serializers
from .models import Product, Variant, Subvariant, Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class SubvariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subvariant
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'