from tkinter import CASCADE
from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator



class Alert(models.Model):
    first_alert = models.DateField(auto_now=True)
    second_alert = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.due_date


class DrugBatch(models.Model):
    batch_no = models.CharField(max_length=10)
    drug_types = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=8,decimal_places=2, validators=[MinValueValidator(1)])
    inventory = models.CharField(max_length=255, validators=[MinValueValidator(1)])
    expiry_date = models.DateField(auto_now=True)
    alert = models.OneToOneField(Alert,on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return self.batch_no


class Drug(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2, validators=[MinValueValidator(1)])
    desription =models.TextField()
    expiry_date = models.DateField(auto_now=True)
    batch = models.ForeignKey(DrugBatch, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name





    




