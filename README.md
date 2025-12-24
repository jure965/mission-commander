# mission-commander :rocket:

This software stack works as an RSS feed bridge for Transmission clients.

Inspired by [transmission-rss](https://github.com/nning/transmission-rss) project.

Features:

- manage configuration and RSS feeds through web UI
- works with one or more Transmission clients
- feeds can be set to expire, i.e. stop fetching certain feeds after set date
- easy deployment with docker

## Development setup

Clone the repo.

Copy _.env.example_ to _.env_ file. Add `DEBUG=true` to _.env_ file.

Start postgres and redis services using docker compose:

```shell
docker compose -f compose-dev.yaml up -d
```

Use uv to create a virtual environment and install packages.

```shell
uv sync
uv run python manage.py migrate
uv run manage.py collectstatic
uv run manage.py createsuperuser
uv run manage.py runserver
```

Also run celery worker.

```shell
uv run celery -A mission_commander worker -l INFO
```

And celery beat.

```shell
uv run celery -A mission_commander beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Production deployment

First have a fresh host or vm with docker, including docker compose plugin.

Clone this repo and cd into cloned folder.

Copy _.env.example_ to _.env_ file. Edit the contents of _.env_ file, change the SECRET_KEY to
some random string.

Run docker compose:

```shell
docker compose up -d
docker compose exec web bash
# now inside web container:
uv run python manage.py createsuperuser
# follow instructions, then leave container:
exit
```

Now access the web UI via http://<your_host_ip>:8000/admin

Log in with your superuser that you set earlier.

Open __Intervals__, add new interval with number of periods __1__ and
interval period __Hours__. You may customize this to your liking.

Open __Periodic tasks__, add new periodic task with name __fetch feeds__, select
a registered task __rss.tasks.fetch_feeds__ and select __Interval schedule__ that
was created in previous step.

### Update deployment

```shell
docker compose down
git pull --ff-only
docker compose pull
docker compose up -d
```

## Setup and usage

In Django admin pages, add a transmission client, then add a feed.

You can manually trigger _fetch feeds_ task in __Periodic tasks__, tick _fetch feeds_
task and choose __Run selected tasks__ action, then click __Go__.

## TODO

- replace celery with dramatiq
- replace celery-beat with periodiq
- replace black and flake8 with ruff
- add search for torrents
- add some logging
- view and manage torrents per client

If additional features are desired, please create an issue on GitHub.
