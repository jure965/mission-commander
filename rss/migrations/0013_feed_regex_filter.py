# Generated by Django 4.1.2 on 2022-10-29 17:25

from django.db import migrations
import rss.fields


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0012_feed_start_paused_alter_transmissionclient_password_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="regex_filter",
            field=rss.fields.RegexField(blank=True, max_length=2048),
        ),
    ]
