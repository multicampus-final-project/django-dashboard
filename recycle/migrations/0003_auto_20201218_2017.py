# Generated by Django 3.1.4 on 2020-12-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0002_collection_machine_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='machine',
            name='lng',
            field=models.FloatField(default=0.0),
        ),
    ]
