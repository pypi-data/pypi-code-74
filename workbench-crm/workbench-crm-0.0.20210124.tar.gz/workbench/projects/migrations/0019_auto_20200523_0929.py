# Generated by Django 3.1a1 on 2020-05-23 07:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from workbench.tools import search


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0012_person_date_of_birth"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0018_auto_20200402_2212"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campaign",
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
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("_fts", models.TextField(blank=True, editable=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contacts.organization",
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
                "verbose_name": "campaign",
                "verbose_name_plural": "campaigns",
                "ordering": ["-id"],
            },
        ),
        migrations.AddField(
            model_name="project",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="projects",
                to="projects.campaign",
                verbose_name="campaign",
            ),
        ),
        migrations.RunSQL(search.create_structure("projects_campaign")),
        migrations.RunSQL(
            search.fts("projects_campaign", ["title", "description", "_fts"])
        ),
        migrations.RunSQL(
            "SELECT audit_audit_table('projects_campaign', ARRAY['fts_document', '_fts']);"
        ),
    ]
