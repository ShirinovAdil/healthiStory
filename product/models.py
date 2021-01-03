from django.db import models
from ckeditor.fields import RichTextField
from . import choices as c
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Category(models.Model):
    category_code = models.CharField(max_length=50, null=True)
    cat_name = models.CharField(max_length=100, verbose_name=_('Category Name'))
    language = models.CharField(max_length=255, choices=c.LANGUAGE_CHOICES, default=c.ENGLISH_LANG)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    product_code = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=250)
    subtitle = models.TextField()
    description = RichTextField()
    img = models.CharField(max_length=250)
    language = models.CharField(max_length=255, choices=c.LANGUAGE_CHOICES, default=c.ENGLISH_LANG)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
