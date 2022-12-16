# Generated by Django 4.1.1 on 2022-09-29 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobarticle", old_name="time", new_name="api_time",
        ),
        migrations.RenameField(
            model_name="jobarticle", old_name="by", new_name="author",
        ),
        migrations.RemoveField(model_name="jobarticle", name="date",),
        migrations.AddField(
            model_name="jobarticle",
            name="time_utc",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 9, 29, 21, 13, 18, 982007, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="jobarticle",
            name="url",
            field=models.TextField(blank=True, null=True),
        ),
    ]