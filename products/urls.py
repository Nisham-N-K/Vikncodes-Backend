from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, VariantViewSet, SubvariantViewSet, StockViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'variants', VariantViewSet)
router.register(r'subvariants', SubvariantViewSet)
router.register(r'stock', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
