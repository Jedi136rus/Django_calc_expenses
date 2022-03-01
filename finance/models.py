from django.db import models


class Expense(models.Model):
    exp_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    exp_cat = models.CharField(max_length=10, verbose_name='Категория')
    exp_sum = models.IntegerField(verbose_name='Потраченная сумма')
    exp_text = models.CharField(max_length=200, verbose_name='Примечание')
    exp_ostan = models.IntegerField(verbose_name='Остаток')


class Wallet(models.Model):
    exp_wallet = models.IntegerField(verbose_name='Остаток')
