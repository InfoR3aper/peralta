#!/usr/bin/env python3.6
import os
import requests

class Peralta():
    def __init__(self,
                 url='https://www.googleapis.com/customsearch/v1',
                 cx='007775541357642725620:_e0fcphnv60',
                 q='intitle:devops intext:remote'):
        self.url = url
        self.cx = cx
        self.q = q

    def query(self):
        """fetch data"""

        # TODO: add error handling
        api_key = os.environ['API_KEY']
        query_params = {'cx': self.cx,
                        'q': self.q,
                        'key': api_key}

        # TODO: add error handling
        resp = requests.get(self.url, params=query_params)

        data = resp.json()
        for item in data['items']:
            print(item['title'])
            print(item['link'])
            for metatag in item['pagemap']['metatags']:
                if 'og:description' in metatag:
                    print(metatag['og:description'])

if __name__ == '__main__':
    p = Peralta()
    p.query()
