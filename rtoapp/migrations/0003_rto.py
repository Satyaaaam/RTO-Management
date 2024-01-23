# Generated by Django 4.1.2 on 2023-01-02 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rtoapp", "0002_rename_name_city_cityname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rtoname", models.CharField(blank=True, max_length=200, null=True)),
                ("nodal", models.CharField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("creationdate", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rtoapp.city",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rtoapp.state",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
