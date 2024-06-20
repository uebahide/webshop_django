from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_types'
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'

    def __str__(self) -> str:
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
      db_table='manufacturers'

    def __str__(self) -> str:
      return self.name


class ProductPicture(models.Model):
    picture = models.FileField(upload_to='store/', blank=True)
    order = models.IntegerField()
    product = models.ForeignKey(
        'Product',
        related_name='product_pictures',
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = 'product_pictures'

    def __str__(self) -> str:
      return f"picture for {self.product.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_type = models.ForeignKey(
        'ProductType',
        on_delete = models.CASCADE
    )
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = 'products'


    def __str__(self) -> str:
       return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        'accounts.User',
        on_delete = models.CASCADE,
        primary_key = True
    )

    class Meta:
        db_table = 'carts'

    def __str__(self):
        return f"{self.user.name}'s cart"
    
class CartItem(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete = models.CASCADE
    )
    cart = models.ForeignKey(
        'Cart',
        on_delete = models.CASCADE
    )
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart_items'
        unique_together = [['product', 'cart']]

    def __str__(self):
        return f"{self.product.name}-{self.cart.user.name}"