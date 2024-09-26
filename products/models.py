from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering=['name']

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    catergory=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_products',
                                verbose_name='Category')
    description=models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering=['name']
    def __str__(self):
        return self.name

class Suppliers (models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    email = models.EmailField(max_length=255, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    address = models.CharField(max_length=255, verbose_name='Address')
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering=['name']
    def __str__(self):
        return self.name

class ProductSupplier(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='get_suppliers',
                              verbose_name='Product')
    supplier=models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='get_products',
                               verbose_name='Supplier')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    class Meta:
        verbose_name = 'Product Supplier'
        verbose_name_plural = 'Product Suppliers'
        ordering=['product']
    def __str__(self):
        return self.product.name

