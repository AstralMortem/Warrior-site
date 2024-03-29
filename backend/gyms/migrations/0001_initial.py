# Generated by Django 5.0.1 on 2024-02-17 21:11

import django.db.models.deletion
import location_field.models.plain
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('calendar', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('calendar', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='group_participants', to=settings.AUTH_USER_MODEL)),
                ('gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gyms.gym')),
            ],
        ),
    ]
