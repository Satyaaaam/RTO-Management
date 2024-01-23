# Generated by Django 4.1.2 on 2023-01-05 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rtoapp", "0007_learning_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="learning",
            old_name="user",
            new_name="register",
        ),
        migrations.AddField(
            model_name="learning",
            name="rto",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rtoapp.rto",
            ),
        ),
    ]
