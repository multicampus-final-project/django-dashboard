# Generated by Django 3.1.4 on 2020-12-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0003_auto_20201218_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]