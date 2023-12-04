import django.contrib

from django.contrib import admin
from .models import BankBalance, Expense, Investment

admin.site.register(BankBalance)
admin.site.register(Expense)
admin.site.register(Investment)
