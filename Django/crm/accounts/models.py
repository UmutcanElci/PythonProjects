from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length= 100, null=True)
    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=30,null=True) 
    email = models.CharField(max_length= 50, null= True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:#To see the name in database when created 
        return self.name
   
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length= 100,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length= 20,null=True,choices=CATEGORY)
    description = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.name
    


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,null=True,choices=STATUS)
   
    def __str__(self) -> str:
        return self.product.name
    
    