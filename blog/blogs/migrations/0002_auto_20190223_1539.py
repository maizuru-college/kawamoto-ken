# Generated by Django 2.1.5 on 2019-02-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='updateed_datetime',
            new_name='updated_datetime',
        ),
    ]
