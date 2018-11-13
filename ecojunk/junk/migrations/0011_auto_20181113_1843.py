# Generated by Django 2.0.8 on 2018-11-13 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("junk", "0010_auto_20181113_1842")]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="deals",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Customer",
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="rider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="deliveries",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Rider",
            ),
        ),
    ]
