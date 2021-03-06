# Generated by Django 2.0.8 on 2018-10-10 09:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("companies", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Deal",
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
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Date")),
            ],
            options={"verbose_name": "Deals"},
        ),
        migrations.CreateModel(
            name="JunkPoint",
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
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=4326, verbose_name="Location"
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="points",
                        to="companies.Contract",
                        verbose_name="Contract",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="points",
                        to="junk.JunkPoint",
                        verbose_name="Junk point",
                    ),
                ),
            ],
            options={
                "verbose_name": "Junk point",
                "verbose_name_plural": "Junk points",
            },
        ),
        migrations.CreateModel(
            name="JunkPointType",
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
                    "description",
                    models.TextField(max_length=512, verbose_name="Description"),
                ),
            ],
            options={
                "verbose_name": "Junk point type",
                "verbose_name_plural": "Junk point types",
            },
        ),
        migrations.CreateModel(
            name="Trash",
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
                    "description",
                    models.TextField(max_length=512, verbose_name="Description"),
                ),
                (
                    "deal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trash",
                        to="junk.Deal",
                        verbose_name="Deal",
                    ),
                ),
            ],
            options={"verbose_name": "Trash", "verbose_name_plural": "Trash"},
        ),
        migrations.CreateModel(
            name="TrashType",
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
            ],
            options={"verbose_name": "Trash type", "verbose_name_plural": "Trash type"},
        ),
        migrations.AddField(
            model_name="trash",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="deals",
                to="junk.TrashType",
                verbose_name="Trash type",
            ),
        ),
    ]
