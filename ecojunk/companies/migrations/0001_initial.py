# Generated by Django 2.0.8 on 2018-10-10 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "promoted",
                    models.BooleanField(default=False, verbose_name="promoted"),
                ),
            ],
            options={"verbose_name": "Company", "verbose_name_plural": "Companies"},
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("end_date", models.DateTimeField(verbose_name="End date")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="companies.Company",
                        verbose_name="Company",
                    ),
                ),
            ],
            options={"verbose_name": "Contract", "verbose_name_plural": "Contracts"},
        ),
    ]