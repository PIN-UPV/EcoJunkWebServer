# Generated by Django 2.0.8 on 2018-11-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("junk", "0013_auto_20181120_1248")]

    operations = [
        migrations.RenameField(
            model_name="deal", old_name="date", new_name="created_date"
        ),
        migrations.AddField(
            model_name="deal",
            name="accepted_date",
            field=models.DateTimeField(null=True, verbose_name="Date"),
        ),
    ]
