from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(max_length=225, blank=True)
    image = models.ImageField(upload_to='photos/categories')


    class Meta:
            verbose_name_plural = 'Categories',
            constraints = [
                models.UniqueConstraint(
                                        fields=['name'],
                                        name='unique_category_name',
                                        condition=models.Q(name__isnull=False)
                                        )
            ]

    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Sizes',
        constraints = [
            models.UniqueConstraint(
                                    fields=['name'], 
                                    name='unique_size_name', 
                                    condition=models.Q(name__isnull=False)
                                    )
        ]

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image = models.ImageField(upload_to='product_images')
    color = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[str(self.id)])


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Size: {self.size.name} - Quantity: {self.quantity}"

 
class User(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)

    class Meta:
        constraints= [
            models.UniqueConstraint(
                                    fields=['dni', 'email'],
                                    name='unique_customer'
                                    )
        ]

    def __repr__(self):
        return f"<Customer: {self.first_name} ({self.dni}$)>"
   
class Inventory(models.Model):  
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gte=0), name='non_negative_quantity')
        ]
    
    def __repr__(self):
        return f"Inventory: Product={self.product}, quantity={self.quantity}"
    
    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"
    

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    total =  models.DecimalField(max_digits=10, decimal_places=2)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Sale: Customer:{self.user}, date={self.date}, total={self.total}"
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='CartProduct')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Cart {self.pk} for {self.user}"