# Generated by Django 2.2 on 2019-05-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0006_claim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='desc',
            new_name='description',
        ),
    ]