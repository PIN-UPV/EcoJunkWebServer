# Generated by Django 2.0.8 on 2018-11-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junk', '0017_auto_20181127_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junkpoint',
            name='types',
            field=models.ManyToManyField(to='junk.JunkPointType'),
        ),
    ]