from django.contrib import admin
from .models import Expense, Wallet

admin.site.register(Expense)
admin.site.register(Wallet)