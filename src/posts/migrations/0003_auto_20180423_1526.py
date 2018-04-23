# Generated by Django 2.0.4 on 2018-04-23 07:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 4, 23, 7, 26, 49, 368331, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
