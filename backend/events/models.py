from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.

class IEvent(models.Model):
    title = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    date = DateRangeField()
    is_archived = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title} ({self.place},{self.date.lower})"


COMPETITION_PLACE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )

class CompetitionResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="participant_to_competition")
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE, related_name = 'competition_to_participant')

    sparing_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True)
    tul_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True)
    spec_tech_place  = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True)

    comment = models.CharField(max_length=300,blank=True)


class CompetitionJudgment(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="judge_to_competition")
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE, related_name = 'competition_to_judge')

    result = models.CharField(max_length=250, blank=True,null=True)
    comment = models.CharField(max_length=300,blank=True,null=True)

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
    command_sparing = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True)
    command_tul = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True)

    participants = models.ManyToManyField('account.BaseUser',through="CompetitionResult", related_name='competition_participant')
    judgment = models.ManyToManyField('account.BaseUser',through="CompetitionJudgment", related_name='competition_judge')

    def total_medals(self):
        table = self.competition_to_participant.all()
        golden = 0
        silver = 0
        bronze = 0
        for i in table:
            if(i.sparing_place == 1):
                golden += 1
            elif(i.sparing_place == 2):
                silver += 1
            elif(i.sparing_place == 3):
                bronze += 1

            if(i.tul_place == 1):
                golden +=1
            elif(i.tul_place == 2):
                silver += 1
            elif(i.tul_place == 3):
                bronze += 1

            if(i.spec_tech_place == 1):
                golden += 1
            elif(i.spec_tech_place == 2):
                silver += 1
            elif(i.spec_tech_place == 3):
                bronze += 1

        return f"{golden},{silver},{bronze}"





class AttestationResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="participant_to_attestation")
    attestation = models.ForeignKey('Attestation',on_delete=models.CASCADE, related_name="attestation_to_participant")

    from_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_from_belt')
    to_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_to_belt')
    comment = models.CharField(max_length=300,blank=True)
    
class Attestation(IEvent):
    participants = models.ManyToManyField('account.BaseUser',through="AttestationResult", related_name='attestation_participant')

