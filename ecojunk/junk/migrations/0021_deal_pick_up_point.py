# Generated by Django 2.0.8 on 2018-12-04 12:48

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junk', '0020_deal_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='pick_up_point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, verbose_name='Pick up point'),
        ),
    ]
