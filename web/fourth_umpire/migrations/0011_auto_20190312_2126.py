# Generated by Django 2.1.7 on 2019-03-12 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_umpire', '0010_auto_20190312_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='media',
            new_name='data',
        ),
    ]
