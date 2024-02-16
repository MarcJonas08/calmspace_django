# Generated by Django 5.0 on 2024-01-10 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_delete_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=3)),
                ('birthday', models.DateField()),
                ('contact_number', models.CharField(max_length=11)),
                ('emergency_contact_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('medical_history', models.CharField(max_length=1000)),
                ('notes', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clinicbranches')),
            ],
        ),
    ]
