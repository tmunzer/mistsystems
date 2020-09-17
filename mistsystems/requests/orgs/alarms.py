class Alarms():
    def __init__(self, session):
        self._session = session

    def search(self, org_id, query={}, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/alarms/search".format(org_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count(self, org_id, query={}, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/alarms/count".format(org_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp