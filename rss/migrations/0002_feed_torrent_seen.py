# Generated by Django 4.1.2 on 2022-10-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("expire", models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name="torrent",
            name="seen",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
