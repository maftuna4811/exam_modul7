# Generated by Django 5.1 on 2024-08-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
