# Generated by Django 2.2.5 on 2019-09-09 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190908_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 23, 27, 14, 418101), verbose_name='date published'),
        ),
    ]
