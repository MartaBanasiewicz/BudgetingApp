from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)

class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
