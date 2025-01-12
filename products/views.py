from rest_framework import viewsets
from .models import Product, Variant, Subvariant, Stock
from .serializers import ProductSerializer, VariantSerializer, SubvariantSerializer, StockSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class SubvariantViewSet(viewsets.ModelViewSet):
    queryset = Subvariant.objects.all()
    serializer_class = SubvariantSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
