# Generated by Django 5.0 on 2024-01-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_alter_customuser_is_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_doctor',
            field=models.BooleanField(null=True),
        ),
    ]
