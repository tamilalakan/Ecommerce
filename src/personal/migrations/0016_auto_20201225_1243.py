# Generated by Django 3.1.2 on 2020-12-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_useraccount_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rate',
            field=models.FloatField(max_length=32, null=True),
        ),
    ]
