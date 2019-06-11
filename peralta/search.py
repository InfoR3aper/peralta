import os
import requests

URL = 'https://www.googleapis.com/customsearch/v1'
CX = '007775541357642725620:_e0fcphnv60'
Q = 'intitle:devops intext:remote'

try:
    API_KEY = os.environ['API_KEY']
except KeyError as e:
    raise KeyError("API_KEY environment variable not found")

def query(index=None):
    """fetch data"""
    query_params = {'cx': CX,
                    'q': Q,
                    'key': API_KEY,
                    'start': index,
                    'sort': 'date'}

    # TODO: add error handling
    resp = requests.get(URL, params=query_params)
    return resp.json()

def parse(job):
    """extract data from job listing"""
    f = {}
    f['name'] = job['title']
    f['url'] = job['link']
    for metatag in job['pagemap']['metatags']:
        if 'og:description' in metatag:
            f['desc'] = metatag['og:description']
    return f
