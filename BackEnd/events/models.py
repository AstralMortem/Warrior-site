from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

# Create your models here.

class IEvent(models.Model):
    title = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    date = DateTimeRangeField()
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Competition(IEvent):
    pass
    
class Attestation(IEvent):
    pass