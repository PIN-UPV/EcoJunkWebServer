# Generated by Django 2.0.8 on 2018-11-13 18:36

from django.db import migrations
from ecojunk.users.constants import RIDER, USER


def create_initial_roles(apps, schema_editor):
    Permission = apps.get_model("users", "Permission")
    Permission.objects.create(rol=RIDER)
    Permission.objects.create(rol=USER)


class Migration(migrations.Migration):

    dependencies = [("users", "0004_auto_20181109_1509")]

    operations = [migrations.RunPython(create_initial_roles)]
