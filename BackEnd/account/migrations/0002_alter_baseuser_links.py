# Generated by Django 5.0.1 on 2024-02-01 10:31

import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='links',
            field=django_jsonform.models.fields.ArrayField(base_field=models.URLField(blank=True, null=True), size=8),
        ),
    ]
