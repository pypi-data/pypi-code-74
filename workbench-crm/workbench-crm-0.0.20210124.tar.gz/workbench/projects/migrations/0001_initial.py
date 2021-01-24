# Generated by Django 2.1.7 on 2019-03-04 21:39

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contacts", "0001_initial"),
        ("offers", "0001_initial"),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cost",
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
                ("title", models.CharField(max_length=200, verbose_name="title")),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2,
                        default=None,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="cost",
                    ),
                ),
                (
                    "third_party_costs",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=None,
                        help_text="Total incl. tax for third-party services.",
                        max_digits=10,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="third party costs",
                    ),
                ),
                (
                    "position",
                    models.PositiveIntegerField(default=0, verbose_name="position"),
                ),
            ],
            options={
                "verbose_name": "cost",
                "verbose_name_plural": "costs",
                "ordering": ("position", "pk"),
            },
        ),
        migrations.CreateModel(
            name="Effort",
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
                ("title", models.CharField(max_length=200, verbose_name="title")),
                (
                    "billing_per_hour",
                    models.DecimalField(
                        decimal_places=2,
                        default=None,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="billing per hour",
                    ),
                ),
                (
                    "hours",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.1"))
                        ],
                        verbose_name="hours",
                    ),
                ),
            ],
            options={
                "verbose_name": "effort",
                "verbose_name_plural": "efforts",
                "ordering": ("service_type",),
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200, verbose_name="title")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        verbose_name="project description",
                        help_text="Do not use this for the offer description. You can add the offer description later.",
                    ),
                ),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[
                            (10, "Acquisition"),
                            (20, "Work in progress"),
                            (30, "Finished"),
                            (40, "Declined"),
                        ],
                        default=10,
                        verbose_name="status",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created at"
                    ),
                ),
                (
                    "invoicing",
                    models.BooleanField(
                        default=True,
                        help_text="This project is eligible for invoicing.",
                        verbose_name="invoicing",
                    ),
                ),
                (
                    "maintenance",
                    models.BooleanField(
                        default=False,
                        help_text="This project is used for maintenance work.",
                        verbose_name="maintenance",
                    ),
                ),
                ("_code", models.IntegerField(verbose_name="code")),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contacts.Person",
                        verbose_name="contact",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contacts.Organization",
                        verbose_name="customer",
                    ),
                ),
                (
                    "owned_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="responsible",
                    ),
                ),
            ],
            options={
                "verbose_name": "project",
                "verbose_name_plural": "projects",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Service",
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
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created at"
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "position",
                    models.PositiveIntegerField(default=0, verbose_name="position"),
                ),
                (
                    "effort_hours",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.1"))
                        ],
                        verbose_name="effort hours",
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="cost",
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="services",
                        to="offers.Offer",
                        verbose_name="offer",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="projects.Project",
                        verbose_name="project",
                    ),
                ),
            ],
            options={
                "verbose_name": "service",
                "verbose_name_plural": "services",
                "ordering": ("position", "created_at"),
            },
        ),
        migrations.AddField(
            model_name="effort",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="efforts",
                to="projects.Service",
                verbose_name="service",
            ),
        ),
        migrations.AddField(
            model_name="effort",
            name="service_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="services.ServiceType",
                verbose_name="service type",
            ),
        ),
        migrations.AddField(
            model_name="cost",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="costs",
                to="projects.Service",
                verbose_name="service",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="effort", unique_together={("service", "service_type")}
        ),
    ]
