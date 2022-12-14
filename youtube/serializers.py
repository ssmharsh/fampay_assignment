from rest_framework import serializers
from youtube.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "description",
            "published_on",
            "thumb_url",
            "video_link",
        )
