# mission-commander :rocket:

This software stack works as an RSS feed bridge for Transmission and qBittorrent clients.

Inspired by [transmission-rss](https://github.com/nning/transmission-rss) project.

Features:

- manage configuration and RSS feeds through web UI
- works with one or more Transmission and qBittorrent clients
- feeds can be set to expire, i.e., stop fetching certain feeds after a set date
- easy deployment with docker

## Development setup

Clone the repo.

Copy _.env.example_ to _.env_ file. Add `DEBUG=true` to _.env_ file.

Start Postgres and Redis services using docker compose:

```shell
docker compose -f compose-dev.yaml up -d
```

Use uv to create a virtual environment and install packages.

```shell
uv sync
uv run python manage.py migrate
uv run manage.py collectstatic
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

Prerequisites are a host or vm and docker with docker compose plugin installed.

Create a folder on the host for the application.

Copy `compose.yaml` file from this repo to the host in the created folder.

Edit `compose.yaml` file, change `SECRET_KEY` variable value to a random string.

Change the current directory to the created folder and run `docker compose up -d`.

Now access the web UI via http://<your_host_ip>:8000/setup/ and follow instructions for first time setup.

To update the deployment in the future, run `docker compose pull && docker compose down && docker compose up -d`.

From time to time, check if there is a new version of `compose.yaml` in the repo.

## TODO

- add search for torrents
- view and manage torrents per client

If additional features are desired, please create an issue on GitHub.
