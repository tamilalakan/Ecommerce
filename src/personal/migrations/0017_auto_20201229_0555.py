# Generated by Django 3.1.2 on 2020-12-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20201225_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='firstname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='lastname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='state',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='zipcode',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
