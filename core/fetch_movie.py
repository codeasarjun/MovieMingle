import requests

def fetch_movie_data(API_KEY, BASE_URL):
    url = f'{BASE_URL}/discover/movie'
    params = {
        'api_key': API_KEY,
        'sort_by': 'popularity.desc',
        'language': 'en-US',
        'include_adult': 'false',
        'include_video': 'false',
        'page': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['results']
