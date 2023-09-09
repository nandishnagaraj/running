from django.db import models

from customer.models import Customer
from trainingplans.models import TrainingPlans

# Create your models here.
class Order(models.Model):
    OrderId = models.AutoField(primary_key=True,auto_created=True)
    CustomerInfo = models.ForeignKey(Customer, on_delete=models.CASCADE)
    TrainingPlans = models.ManyToManyField(TrainingPlans)
    OrderDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.CustomerInfo.emailID+" - "+str(self.OrderId) +" - "+str(self.OrderDate)
    
    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'
