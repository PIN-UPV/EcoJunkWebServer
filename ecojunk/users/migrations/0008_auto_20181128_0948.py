# Generated by Django 2.0.8 on 2018-11-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0007_auto_20181128_0937")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="permissions",
            field=models.ManyToManyField(
                to="users.Permission", verbose_name="Permissions"
            ),
        )
    ]
