# Generated by Django 5.1.6 on 2025-02-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_consultant_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
