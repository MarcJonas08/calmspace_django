# Generated by Django 5.0 on 2024-02-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_doctor_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]