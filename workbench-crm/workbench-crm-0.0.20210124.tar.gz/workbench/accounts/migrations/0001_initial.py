# Generated by Django 2.1.7 on 2019-03-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is active"),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="is admin"),
                ),
                (
                    "_short_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="initials"
                    ),
                ),
                (
                    "_full_name",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="full name"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "ordering": ("_full_name",),
            },
        )
    ]
