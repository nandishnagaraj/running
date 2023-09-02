from django import forms
from django.db import models

# Create your models here.

class TrainingPlans(models.Model):
    trainingPackage = models.CharField(max_length=255)
    trainingPlansPrice = models.PositiveIntegerField()
    trainingDurationinWeeks = models.PositiveIntegerField()
    trainingsheet = models.FileField(upload_to='plans')


    def __str__(self) -> str:
        return self.trainingPackage