from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

class Gym(models.Model):
    title = models.CharField(max_length=250)
    coach = models.ForeignKey("account.BaseUser",on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    calendar = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    location = PlainLocationField(zoom=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Group(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    coach = models.ForeignKey("account.BaseUser",on_delete=models.CASCADE)

    calendar = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

    participants = models.ManyToManyField('account.BaseUser', related_name='group_participants')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

