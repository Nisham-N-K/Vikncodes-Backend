# Vikncodes-Backend
Vikncodes Backend Project 

# Product Management Dashboard

This is a Product Management Dashboard built using React for the frontend and Django for the backend. The dashboard allows you to add, update, and delete products, manage their stock levels, and handle variants and sub-variants.

## Task Overview

### Task 1: Backend (Django)

You are required to build APIs and models for managing products and stock levels in the backend.

#### 1. Product Model

Use the following `Products` model to store product information:

```python
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)
    ProductImage = VersatileImageField(upload_to="uploads/", blank=True, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        db_table = "products_product"
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")
