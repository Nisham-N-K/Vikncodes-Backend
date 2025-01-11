from django.db import models
from products.models import Product, Variant, Subvariant

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    subvariant = models.ForeignKey(Subvariant, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.ProductName} - {self.variant.name} - {self.subvariant.option} - {self.quantity}"
