# Generated by Django 4.1.1 on 2022-10-01 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_rename_time_newsarticle_api_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsarticle",
            name="time_utc",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 10, 1, 7, 23, 54, 107282, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
