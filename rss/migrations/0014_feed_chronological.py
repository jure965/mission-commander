# Generated by Django 4.1.2 on 2022-10-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0013_feed_regex_filter"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="chronological",
            field=models.BooleanField(
                default=True, help_text="Add torrents in chronological order"
            ),
        ),
    ]
