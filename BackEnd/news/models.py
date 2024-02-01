from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django_jsonform.models.fields import ArrayField



class News(models.Model):
    title = models.CharField(_("title"),max_length=250)
    text = RichTextField(_("news text"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    author = models.ForeignKey("account.BaseUser",on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")


class NewsImage(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m/%d')

    def __str__(self):
        return self.news.title
