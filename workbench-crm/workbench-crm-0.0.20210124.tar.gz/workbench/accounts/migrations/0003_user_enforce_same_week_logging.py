# Generated by Django 2.1.7 on 2019-03-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0002_auto_20190304_2247")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="enforce_same_week_logging",
            field=models.BooleanField(
                default=True, verbose_name="enforce same week logging"
            ),
        )
    ]
