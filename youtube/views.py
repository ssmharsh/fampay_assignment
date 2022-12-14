from rest_framework.decorators import api_view
from rest_framework.response import Response
from youtube.models import Video
from youtube.serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Create your views here.
@api_view(["GET"])
def search_videos(request):
    query = request.GET.get("field")
    response = Video.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    data = [
        VideoSerializer(model).data
        for model in response
    ]
    return Response(data)


@api_view(["GET"])
def all_videos(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    videos = Video.objects.all()
    result_page = paginator.paginate_queryset(videos, request)
    serializer = VideoSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


