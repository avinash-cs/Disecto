from django.db import models

# Create your models here.
class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=100)
    description = models.TextField(blank=True,default="")
    price = models.DecimalField(max_digits=7,decimal_places=2)
    quantity_avail = models.IntegerField()
    def __str__(self):
        return f'{self.name}'
class Orders(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete= models.SET_NULL, null=True)
    quantity = models.IntegerField()
    def __str__(self):
        
        return f'{self.product}'

class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return str(self.customer)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)
   