# Generated by Django 2.2 on 2019-05-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20190518_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_sub',
            field=models.BooleanField(default=False),
        ),
    ]