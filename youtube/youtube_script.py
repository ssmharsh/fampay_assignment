import requests

from assignment.settings import (
    MAX_RESULTS,
    PUBLISHED_AFTER,
    QUERY_FIELD,
    API_KEY,
    YOUTUBE_URL
)

def fetch_youtube_data():
    Params = {}
    Params['part'] = 'snippet'
    Params['maxResults'] = MAX_RESULTS
    Params['order'] = 'date'
    Params['publishedAfter'] = PUBLISHED_AFTER
    Params['q'] = QUERY_FIELD
    Params['type'] = 'video'
    Params['key'] = API_KEY
    search_response = requests.get(url=YOUTUBE_URL, params=Params)
    search_data = search_response.json()
    return search_data