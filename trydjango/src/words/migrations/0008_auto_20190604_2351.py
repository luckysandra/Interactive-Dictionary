# Generated by Django 2.2.2 on 2019-06-04 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_auto_20190604_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='name',
            new_name='word',
        ),
    ]
