from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)
    ProductImage = models.ImageField(upload_to="uploads/", blank=True, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.ProductName

class Variant(models.Model):
    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    options = models.JSONField()  # Store variant options like 'sizes', 'colors'

    def __str__(self):
        return f"{self.name} - {self.product.ProductName}"

class Subvariant(models.Model):
    variant = models.ForeignKey(Variant, related_name="subvariants", on_delete=models.CASCADE)
    option = models.CharField(max_length=255)  # Specific options like 'S', 'M', 'L'

    def __str__(self):
        return self.option

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    subvariant = models.ForeignKey(Subvariant, on_delete=models.CASCADE)
    quantity = models.IntegerField()  # Stock level for a specific subvariant

    def __str__(self):
        return f"{self.product.ProductName} - {self.variant.name} - {self.subvariant.option}"
