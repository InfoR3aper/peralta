#!/usr/bin/env python3.6
import os
import requests

URL = 'https://www.googleapis.com/customsearch/v1'
CX = '007775541357642725620:_e0fcphnv60'
Q = 'intitle:devops intext:remote'

# TODO: add error handling
API_KEY = os.environ['API_KEY']

def query():
    """fetch data"""
    query_params = {'cx': CX,
                    'q': Q,
                    'key': API_KEY}

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


if __name__ == '__main__':
    data = query()
    jobs = []
    for d in data['items']:
        jobs.append(parse(d))

    for j in jobs:
        print("{} {} {}".format(j['name'], j['url'], j['desc']))
