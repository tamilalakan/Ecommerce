# Generated by Django 3.0.8 on 2020-07-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]