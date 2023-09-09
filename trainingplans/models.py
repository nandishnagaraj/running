from django import forms
from django.db import models

# Create your models here.

class TrainingPlans(models.Model):
    trainingPlanID = models.PositiveIntegerField(primary_key=True, auto_created=True)
    trainingPackageName = models.CharField(max_length=255)
    trainingPlansPrice = models.DecimalField(max_digits=15, decimal_places=2)
    trainingDurationinWeeks = models.PositiveIntegerField()
    traininglevel = models.CharField(max_length=255,choices=[('1','Level 1'),('2','Level II'),('3','Level III')],default="1")
    imageInfo = models.ImageField(upload_to ='media/',default='Pranesh__Bangalore_Marathon_.xlsx')

    def __str__(self) -> str:
        return self.trainingPackageName
    
    class Meta():
        verbose_name_plural = 'TrainingPlans'
        verbose_name = 'TrainingPlan'