# Generated by Django 2.2.11 on 2020-04-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20200416_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-04-16-21.09.30', max_length=100),
        ),
    ]