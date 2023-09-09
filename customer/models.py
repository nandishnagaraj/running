from datetime import date
from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.PositiveIntegerField()
    emailID = models.EmailField(unique=True,primary_key=True)
    dateofBirth = models.DateField(editable=True)
    fiveKMTime = models.TimeField(editable=True)
    isAdmin = models.BooleanField(default=False)
    isTrainer = models.BooleanField(default=False)
    age = models.IntegerField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.firstName+" - "+self.emailID
    
    def save(self, *args, **kwargs):
        today = date.today()
        age = today.year - self.dateofBirth.year - ((today.month, today.day) < (self.dateofBirth.month, self.dateofBirth.day))
        self.age = age
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Customers'
        verbose_name = 'Customer'