# Generated by Django 3.1.3 on 2021-01-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210103_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='User ID'),
        ),
    ]
