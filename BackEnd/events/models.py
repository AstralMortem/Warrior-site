from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.

class IEvent(models.Model):
    title = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    date = DateRangeField()
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


COMPETITION_PLACE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )

class CompetitionResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE)
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE)

    sparing_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True)
    tul_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True)
    spec_tech_place  = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True)

    comment = models.CharField(max_length=300,blank=True)

class CompetitionJudgment(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE)
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE)

    result = models.CharField(max_length=250, blank=True)
    comment = models.CharField(max_length=300,blank=True)

class Competition(IEvent):
    COMPETITION_TYPE = (
        ('t-1','Місцеве змагання'),
        ('t-2','Регіональне змагання',),
        ('t-3','Кубок області'),
        ('t-4','Чемпіонат області'),
        ('t-5','Кубок України'),
        ('t-6','Чемпіонат України'),
        ('t-7','Кубок Європи'),
        ('t-8','Чемпіонат Європи'),
        ('t-9','Кубок Світу'),
        ('t-10','Чемпіонат Світу')
    )

    competition_type = models.CharField(max_length=4, choices=COMPETITION_TYPE)
    command_sparing = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True)
    command_tul = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True)

    participants = models.ManyToManyField('account.BaseUser',through="CompetitionResult", related_name='competition_participants')
    judgment = models.ManyToManyField('account.BaseUser',through="CompetitionJudgment", related_name='competition_judges')

class AttestationResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE)
    attestation = models.ForeignKey('Attestation',on_delete=models.CASCADE)

    from_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_from_belt')
    to_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_to_belt')
    comment = models.CharField(max_length=300,blank=True)
    
class Attestation(IEvent):
    participants = models.ManyToManyField('account.BaseUser',through="AttestationResult")
