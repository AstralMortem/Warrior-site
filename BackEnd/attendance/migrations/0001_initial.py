# Generated by Django 5.0.1 on 2024-02-01 14:20

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gyms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gyms.group')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gyms.gym')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_type', models.CharField(choices=[('pre', 'Присутній'), ('ill', 'Захворів'), ('aps', 'Відсутній'), ('gre', 'Поважна причина')], max_length=3)),
                ('comment', models.CharField(max_length=100)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.attendance')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='participants',
            field=models.ManyToManyField(related_name='attendance_participants', through='attendance.AttendanceUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
