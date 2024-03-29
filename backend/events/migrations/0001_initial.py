# Generated by Django 5.0.1 on 2024-02-17 21:11

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('is_archived', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('is_archived', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('competition_type', models.CharField(choices=[('t-1', 'Місцеве змагання'), ('t-2', 'Регіональне змагання'), ('t-3', 'Кубок області'), ('t-4', 'Чемпіонат області'), ('t-5', 'Кубок України'), ('t-6', 'Чемпіонат України'), ('t-7', 'Кубок Європи'), ('t-8', 'Чемпіонат Європи'), ('t-9', 'Кубок Світу'), ('t-10', 'Чемпіонат Світу')], max_length=4)),
                ('command_sparing', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('command_tul', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttestationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('attestation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attestation_to_participant', to='events.attestation')),
                ('from_belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_from_belt', to='account.belt')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_to_attestation', to=settings.AUTH_USER_MODEL)),
                ('to_belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_to_belt', to='account.belt')),
            ],
        ),
        migrations.AddField(
            model_name='attestation',
            name='participants',
            field=models.ManyToManyField(related_name='attestation_participant', through='events.AttestationResult', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CompetitionJudgment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, max_length=250, null=True)),
                ('comment', models.CharField(blank=True, max_length=300, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_to_judge', to='events.competition')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judge_to_competition', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='judgment',
            field=models.ManyToManyField(related_name='competition_judge', through='events.CompetitionJudgment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CompetitionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sparing_place', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('tul_place', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('spec_tech_place', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_to_participant', to='events.competition')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_to_competition', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='participants',
            field=models.ManyToManyField(related_name='competition_participant', through='events.CompetitionResult', to=settings.AUTH_USER_MODEL),
        ),
    ]
