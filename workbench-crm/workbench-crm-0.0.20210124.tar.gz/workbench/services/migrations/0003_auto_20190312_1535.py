# Generated by Django 2.1.7 on 2019-03-12 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("services", "0002_auto_20190304_2247")]

    operations = [
        migrations.RenameField(
            model_name="servicetype",
            old_name="billing_per_hour",
            new_name="hourly_rate",
        ),
        migrations.AlterField(
            model_name="servicetype",
            name="hourly_rate",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="hourly rate",
            ),
        ),
    ]
