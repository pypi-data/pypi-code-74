# Generated by Django 2.2.5 on 2019-09-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contacts", "0010_organization_default_billing_address")]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="groups",
            field=models.ManyToManyField(
                blank=True, to="contacts.Group", verbose_name="groups"
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="groups",
            field=models.ManyToManyField(
                blank=True, to="contacts.Group", verbose_name="groups"
            ),
        ),
    ]
