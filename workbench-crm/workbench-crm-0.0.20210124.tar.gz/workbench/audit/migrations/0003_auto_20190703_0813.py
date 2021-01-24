# Generated by Django 2.2.2 on 2019-07-03 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("audit", "0002_auto_20190321_1626"),
        ("invoices", "0006_auto_20190309_2143"),
    ]

    operations = [
        migrations.RunSQL(
            "UPDATE audit_logged_actions SET row_data=delete(row_data, '_fts');"
            "UPDATE audit_logged_actions SET changed_fields=delete(changed_fields, '_fts');"
            "UPDATE audit_logged_actions SET row_data=delete(row_data, 'position');"
            "UPDATE audit_logged_actions SET changed_fields=delete(changed_fields, 'position');"
        ),
        migrations.RunSQL(
            "SELECT audit_audit_table('contacts_organization', ARRAY['fts_document']);"
            "SELECT audit_audit_table('contacts_person', ARRAY['fts_document', '_fts']);"
            "SELECT audit_audit_table('invoices_invoice', ARRAY['fts_document', '_fts']);"
            "SELECT audit_audit_table('invoices_service', ARRAY['position']);"
            "SELECT audit_audit_table('projects_project', ARRAY['fts_document', '_fts']);"
            "SELECT audit_audit_table('projects_service', ARRAY['position']);"
            "SELECT audit_audit_table('services_servicetype', ARRAY['position']);"
        ),
    ]
