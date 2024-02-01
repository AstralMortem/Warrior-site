from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.
class Attendance(models.Model):
    coach = models.ForeignKey('account.BaseUser', on_delete=models.SET_NULL, null=True)
    gym = models.ForeignKey('gyms.Gym', on_delete=models.CASCADE)
    group = models.ForeignKey('gyms.Group',on_delete=models.CASCADE)
    date = DateRangeField()

    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField('account.BaseUser', through="AttendanceUser", related_name='attendance_participants')

    def __str__(self):
        return f'Відвідування за {str(self.created_at)}'
    
ATTENDANCE_TYPE = (
    ('pre','Присутній'),
    ('ill','Захворів'),
    ('aps', 'Відсутній'),
    ('gre', 'Поважна причина')
)

class AttendanceUser(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE)
    attendance = models.ForeignKey('Attendance', on_delete=models.CASCADE)

    attendance_type = models.CharField(max_length=3, choices=ATTENDANCE_TYPE)

    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.participant)
