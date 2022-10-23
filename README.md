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

Use poetry to create a virtual environment and install packages.

```shell
docker compose up -d
poetry install --no-root
poetry shell
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```

Also run celery worker.

```shell
poetry shell
celery -A mc worker -l INFO
```

And celery beat.

```shell
poetry shell
celery -A mc beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Production deployment

First have a fresh host or vm with docker, including docker compose plugin, and git installed.

Clone this repo and cd into cloned folder.

Copy _.env.example_ to _.env_ file. Edit the contents of _.env_ file, change the SECRET_KEY to
some random string.

Build docker image, start postgres and redis, run migrations, collect static files, create
superuser, and finally start the rest of the stack:

```shell
docker build -t mission-commander/mc:latest .
docker compose -f docker-compose-prod.yml up -d postgres redis
docker compose -f docker-compose-prod.yml run web python manage.py migrate
docker compose -f docker-compose-prod.yml run web python manage.py collectstatic
docker compose -f docker-compose-prod.yml run web python manage.py createsuperuser
docker compose -f docker-compose-prod.yml up -d
```

Now access the web UI via http://<your_host_ip>:8000/admin

Log in with your username and password that you set earlier.

Open __Intervals__, add new interval with number of periods __1__ and
interval period __Hours__. You may customize this to your liking.

Open __Periodic tasks__, add new periodic task with name __fetch feeds__, select
a registered task __rss.tasks.fetch_feeds__ and select __Interval schedule__ that
was created in previous step.

### Update deployment

Update repository:

```shell
git pull --ff-only
```

Shutdown stack, build docker image, start postgres and redis, apply migrations, collect
static files, and start the rest of the stack:

```shell
docker compose -f docker-compose-prod.yml down
docker build -t mission-commander/mc:latest .
docker compose -f docker-compose-prod.yml up -d postgres redis
docker compose -f docker-compose-prod.yml run web python manage.py migrate
docker compose -f docker-compose-prod.yml run web python manage.py collectstatic
docker compose -f docker-compose-prod.yml up -d
```

## Usage

In Django admin pages, add a transmission client, then add a feed.

You can manually trigger _fetch feeds_ task in __Periodic tasks__, tick _fetch feeds_
task and choose __Run selected tasks__ action, then click __Go__.

## TODO

- option to start torrents paused
- filter feed items with regex
