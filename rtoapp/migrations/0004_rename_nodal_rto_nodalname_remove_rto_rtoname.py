# Generated by Django 4.1.2 on 2023-01-02 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rtoapp", "0003_rto"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rto",
            old_name="nodal",
            new_name="nodalname",
        ),
        migrations.RemoveField(
            model_name="rto",
            name="rtoname",
        ),
    ]