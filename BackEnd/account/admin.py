from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BeltDescription, Belt, BaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField
from django import forms
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
# Register your models here.



class BeltDescriptionAdmin(admin.StackedInline):
    model = BeltDescription

class BeltAdmin(admin.ModelAdmin):
    inlines = [BeltDescriptionAdmin]




class CustomUserAdmin(UserAdmin,DynamicArrayMixin):
    
    fieldsets = (
        (None, {'fields': ('email','mobile', 'password')}),
        (_('Personal info'), {'fields': ('photo','full_name','gender','belt', 'coach_type', 'judge_type', 
                                         'itf_code', 'itf_link', 'links')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('birthday','last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.register(BaseUser,CustomUserAdmin)
admin.site.register(Belt,BeltAdmin)
