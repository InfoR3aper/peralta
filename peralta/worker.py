from . import query, parse

def main():
    data = query()
    jobs = []
    for d in data['items']:
        jobs.append(parse(d))

    for j in jobs:
        print("{} {} {}".format(j['name'], j['url'], j['desc']))
