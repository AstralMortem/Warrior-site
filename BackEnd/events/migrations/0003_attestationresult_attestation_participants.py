# Generated by Django 5.0.1 on 2024-02-01 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('events', '0002_alter_competitionresult_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttestationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('attestation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.attestation')),
                ('from_belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_from_belt', to='account.belt')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_belt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_to_belt', to='account.belt')),
            ],
        ),
        migrations.AddField(
            model_name='attestation',
            name='participants',
            field=models.ManyToManyField(through='events.AttestationResult', to=settings.AUTH_USER_MODEL),
        ),
    ]