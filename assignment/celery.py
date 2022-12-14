from youtube.youtube_script import fetch_youtube_data
from youtube.models import Video
import os
from celery import Celery
from dateutil import parser
from assignment.settings import BASE_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assignment.settings")
app = Celery("assignment")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def insertData(self):
    search_data = fetch_youtube_data()

    for item in search_data['items']:
        if Video.objects.filter(video_link=BASE_URL + item["id"]["videoId"]).exists():
            continue
        snippet = item["snippet"]
        video = Video(
            title=snippet["title"],
            description=snippet["description"],
            published_on=parser.parse(snippet["publishedAt"]),
            thumb_url=snippet["thumbnails"]["default"]["url"],
            video_link=BASE_URL + item["id"]["videoId"],
        )
        video.save()