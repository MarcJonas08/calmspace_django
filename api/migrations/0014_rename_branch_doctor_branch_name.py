# Generated by Django 5.0 on 2024-01-02 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='branch',
            new_name='branch_name',
        ),
    ]