# Generated by Django 2.0.8 on 2018-10-17 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junk', '0002_auto_20181010_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junkpoint',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='points', to='junk.JunkPointType', verbose_name='Junk point'),
        ),
    ]
