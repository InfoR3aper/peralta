#!/usr/bin/env python3
import peralta

def main():
    data = peralta.query()
    jobs = []
    for d in data['items']:
        jobs.append(peralta.parse(d))

    for j in jobs:
        print("{} {} {}".format(j['name'], j['url'], j['desc']))

if __name__ == '__main__':
    main()
