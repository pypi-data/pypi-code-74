# Generated by Django 2.2.5 on 2019-09-13 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("logbook", "0011_merge_20190719_0941")]

    operations = [
        migrations.AlterField(
            model_name="loggedhours",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="loggedhours_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="created by",
            ),
        )
    ]
