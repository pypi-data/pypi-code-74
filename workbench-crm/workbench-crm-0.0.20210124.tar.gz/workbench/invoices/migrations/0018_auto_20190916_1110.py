# Generated by Django 2.2.5 on 2019-09-16 09:10

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invoices", "0017_auto_20190916_1108")]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="total_excl_tax",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="total excl. tax",
            ),
        ),
        migrations.AlterField(
            model_name="recurringinvoice",
            name="total_excl_tax",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="total excl. tax",
            ),
        ),
    ]
