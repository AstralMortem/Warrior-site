from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import ArrayField
from django.utils import timezone
import uuid

# Create your models here.


class Belt(models.Model):
    code = models.CharField(max_length=20,primary_key=True)
    photo = models.ImageField(upload_to='belts')
    title = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title} ({self.code})"
    
class BeltDescription(models.Model):
    id = models.OneToOneField(Belt, verbose_name=_("Belts description"), on_delete=models.CASCADE, primary_key=True, related_name='description')
    ofp = models.TextField(blank=True)
    
    #TODO: expand model

    def __str__(self):
        return str(id)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

class BaseUser(AbstractBaseUser,PermissionsMixin):
    JUDGE_TYPE = [
        ('judge_1',''),
        ('judge_2',''),
        ('judge_3',''),
        ('judge_4',''),
        ('judge_5','')
    ]

    COACH_TYPE = [
        ('coach_1',''),
        ('coach_2',''),
        ('coach_3',''),
        ('coach_4',''),
        ('coach_5','')
    ]

    GENDER = [
        ('m', 'male'),
        ('f', 'female')
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    photo = models.ImageField(upload_to='users/avatars', blank=True, null=True)
    full_name = models.CharField(_('full name'), max_length=250)
    email = models.EmailField(_('email'), unique=True)
    mobile = models.CharField(_("mobile phone"), blank=True)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER, default='m')
    judge_type = models.CharField(_('judge type'), max_length=7, choices=JUDGE_TYPE, null=True, blank=True)
    coach_type = models.CharField(_('coach type'), max_length=7, choices=COACH_TYPE, null=True, blank=True)
    belt = models.ForeignKey(Belt,on_delete=models.SET_NULL, null=True)
    birthday = models.DateField(null=True,blank=True)
    itf_code = models.PositiveBigIntegerField(null=True,blank=True)
    itf_link = models.URLField(null=True,blank=True)
    links = ArrayField(models.URLField(blank=True,null=True), size=8,blank=True,null=True)
    coach = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(_("Active status"), default=True)
    is_staff = models.BooleanField(_("Coach status"),default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if(self.full_name):
            return self.full_name
        return self.email
