# Generated by Django 3.2.9 on 2022-01-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20220107_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
