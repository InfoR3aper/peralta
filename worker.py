#!/usr/bin/env python3
from peralta import search, database

def main():
    db = database.db()

    data = search.query()
    jobs = []
    for i in data['items']:
        jobs.append(search.parse(i))

    for job in jobs:
        db.insert(job)

if __name__ == '__main__':
    main()
