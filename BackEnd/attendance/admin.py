from django.contrib import admin
from .models import Attendance, AttendanceUser
from django.contrib.postgres.fields import DateRangeField
from django.contrib.postgres.forms import RangeWidget
from django.contrib.admin.widgets import AdminDateWidget
# Register your models here.

class AttendanceUserAdmin(admin.StackedInline):
    model = AttendanceUser
    extra = 1

class AttendanceAdmin(admin.ModelAdmin):
    inlines = [AttendanceUserAdmin]
    formfield_overrides = {
        DateRangeField: {
            'widget': RangeWidget(AdminDateWidget),
        },
    }

admin.site.register(Attendance,AttendanceAdmin)
