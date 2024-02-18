from django.contrib import admin
from .models import Competition, Attestation, CompetitionResult, AttestationResult, CompetitionJudgment
from django.contrib.postgres.fields import DateRangeField
from django.contrib.postgres.forms import RangeWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _
# Register your models here.

class CompetitionResultAdmin(admin.StackedInline):
    model = CompetitionResult
    extra = 1

class CompetitionJudgmentResult(admin.StackedInline):
    model = CompetitionJudgment
    extra = 1

class CompetitionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        DateRangeField: {
            'widget': RangeWidget(AdminDateWidget),
        },
    }
    fieldsets = (
        (None, {'fields': ('title','place', 'date','competition_type','is_completed', 'is_archived')}),
        (_('Command result'), {'fields': ('command_sparing','command_tul')}),
    )
    inlines = [CompetitionResultAdmin,CompetitionJudgmentResult]

    list_display = ('title', 'place','date','is_completed', 'is_archived')
    search_fields = ('title', 'place','date')
    ordering = ('is_completed','is_archived','date')


class AttestationResultAdmin(admin.StackedInline):
    model = AttestationResult
    extra = 1

class AttestationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        DateRangeField: {
            'widget': RangeWidget(AdminDateWidget),
        },
    }
    inlines = [AttestationResultAdmin]


admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Attestation,AttestationAdmin)