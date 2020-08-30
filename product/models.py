from django.db import models


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    img = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title