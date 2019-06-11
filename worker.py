#!/usr/bin/env python3
import time
import os
from peralta import search, database

def main(host):
    db = database.db(host)
    index = [None, 10, 20, 30]

    for i in index:
        print(i)
        data = search.query(i)
        jobs = []
        for item in data['items']:
            jobs.append(search.parse(item))

        for job in jobs:
            if 'desc' in job:
                db.insert(job['name'], job['url'], job['desc'])
            else:
                db.insert(job['name'], job['url'])

if __name__ == '__main__':
    db_host = os.environ['DB_HOST'] if 'DB_HOST' in os.environ else '127.0.0.1'
    while True:
        main(db_host)
        hour = 60 * 60
        duration = 12 * hour
        time.sleep(duration)
