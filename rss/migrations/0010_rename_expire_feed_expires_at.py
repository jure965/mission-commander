# Generated by Django 4.1.2 on 2022-10-23 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0009_feed_ignore_newer_than_alter_feed_expire_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feed",
            old_name="expire",
            new_name="expires_at",
        ),
    ]
