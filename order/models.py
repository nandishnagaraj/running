from django.db import models

from customer.models import Customer

# Create your models here.
class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    CustomerInfo = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.CustomerInfo.EmailID+" - "+str(self.OrderId)
    
    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'