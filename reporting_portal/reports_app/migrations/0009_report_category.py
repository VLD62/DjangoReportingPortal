# Generated by Django 3.1.3 on 2020-12-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports_app', '0008_auto_20201207_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('ETC', 'ETC'), ('AEX', 'AEX'), ('OTR', 'OTHER')], default='OTR', max_length=3),
        ),
    ]
