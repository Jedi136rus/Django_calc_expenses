# Generated by Django 4.0.2 on 2022-02-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='exp_ostan',
            field=models.IntegerField(default=1, verbose_name='Остаток'),
            preserve_default=False,
        ),
    ]
