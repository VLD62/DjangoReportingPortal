# Generated by Django 3.1.3 on 2020-12-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports_app', '0010_auto_20201207_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='added_by',
            new_name='user',
        ),
    ]
