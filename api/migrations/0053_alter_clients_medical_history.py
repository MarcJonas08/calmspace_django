# Generated by Django 5.0 on 2024-02-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_remove_clinicbranches_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='medical_history',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
