from rest_framework import serializers
from .models import Stock
from products.serializers import ProductSerializer, VariantSerializer, SubvariantSerializer

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    variant = VariantSerializer()
    subvariant = SubvariantSerializer()

    class Meta:
        model = Stock
        fields = '__all__'
