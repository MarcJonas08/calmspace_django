# Generated by Django 5.0 on 2023-12-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_assessments_anxietyscore_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('resource_type', models.CharField(choices=[('article', 'Article'), ('video', 'Video'), ('news', 'News')], max_length=10)),
            ],
        ),
    ]