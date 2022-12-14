from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.TextField("Title of video")
    description = models.TextField("Description of video")
    published_on = models.DateTimeField(" video publishing datetime")
    thumb_url = models.URLField("Thumbnail URL", max_length=255)
    video_link = models.URLField("Video Link", max_length=255)

    class Meta:
        ordering = ["-published_on"]
