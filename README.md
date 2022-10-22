# mission-commander :rocket:

Manage your torrent RSS feeds from the comfort of the web UI.

Features:

- adds RSS feed functionality to your Transmission daemon clients
- manage RSS feeds via web UI
- feeds can be set to expire, i.e. stop fetching certain feeds after set date

## Development setup

Clone the repo.

Copy _.env.example_ to _.env_ file.

Use poetry to create a virtual environment and install packages.

```shell
docker compose up -d
poetry install --no-root
poetry shell
./manage.py migrate
./manage.py collectstatic
./manage.py runserver
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

Build docker image, run docker compose and create superuser:

```shell
docker build -t mission-commander/mc:latest .
docker compose -f docker-compose-prod.yml up
docker compose -f docker-compose-prod.yml run web python manage.py createsuperuser
```

Now access the web UI via http://<your_host_ip>:8000/admin

Log in with your username and password that you set earlier.

Open __Intervals__, add new interval with number of periods 1 and
interval period __Hours__. You may customize this accordingly.

Open __Periodic tasks__, add new periodic task with name __fetch feeds__, select
a registered task __rss.tasks.fetch_feeds__ and select __Interval schedule__ that
was created in previous step.

## Usage

In Django admin pages, add a transmission client, then add a feed.
