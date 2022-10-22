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
