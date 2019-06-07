from pymongo import MongoClient

class db():
    def __init__(self, host='mongo'):
        self.client = None
        self.db = None
        self.host = host

    def _connect(self):
        # TODO: add error handling
        self.client = MongoClient(self.host)
        self.db = self.client.peralta

    def _close(self):
        # TODO: add validation
        self.client.close()

    def insert(self, job):
        # TODO: add error handling
        self._connect()
        r = self.db.job.insert_one(job)
        self._close()
        return r

    def find(self, query):
        # TODO: add error handling
        self._connect()
        r = self.db.job.find(query)
        self._close()
        return r
