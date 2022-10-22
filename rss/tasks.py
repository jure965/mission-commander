from celery import Celery

app = Celery("rss")


@app.task
def fetch_feeds():
    pass  # todo: add fetch jobs
