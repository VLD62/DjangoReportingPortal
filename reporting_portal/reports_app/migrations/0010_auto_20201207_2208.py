# Generated by Django 3.1.3 on 2020-12-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports_app', '0009_report_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('ETC', 'ETC'), ('AEX', 'AEX'), ('OTHER', 'OTHER')], default='OTHER', max_length=5),
        ),
    ]
