# Generated by Django 3.2.8 on 2021-12-04 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apsKota_web', '0002_auto_20211203_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upload_to',
        ),
    ]
