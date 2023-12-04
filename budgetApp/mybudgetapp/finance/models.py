from django.db import models

class BankBalance(models.Model):
    date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Investment(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
