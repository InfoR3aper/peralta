#!/usr/bin/env python3.6
import os
import requests

def main():
    """fetch and parse data"""

    params = {'cx': '007775541357642725620:_e0fcphnv60',
              'q': 'intitle:devops intext:remote',
              'key': os.environ['API_KEY']}

    resp = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
    data = resp.json()
    for item in data['items']:
        print(item['title'])
        print(item['link'])
        for metatag in item['pagemap']['metatags']:
            if 'og:description' in metatag:
                print(metatag['og:description'])

if __name__ == '__main__':
    main()
