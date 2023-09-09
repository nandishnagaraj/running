from django.db import models

# Create your models here.

class Customer(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    PhoneNumber = models.PositiveIntegerField()
    EmailID = models.EmailField(unique=True,primary_key=True)
    DateofBirth = models.DateField(editable=True)
    FiveKMTime = models.TimeField(editable=True)
    IsAdmin = models.BooleanField(default=False)
    IsTrainer = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.FirstName+" - "+self.EmailID
    
    class Meta:
        verbose_name_plural = 'Customers'
        verbose_name = 'Customer'