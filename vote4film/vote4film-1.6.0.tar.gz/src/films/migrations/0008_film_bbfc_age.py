# Generated by Django 2.2.11 on 2020-03-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0007_auto_20191116_2302"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="bbfc_age",
            field=models.CharField(
                choices=[
                    ("U", "Universal (4+)"),
                    ("PG", "Parental Guidance (8+)"),
                    ("12", "12+"),
                    ("15", "15+"),
                    ("18", "18+"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
