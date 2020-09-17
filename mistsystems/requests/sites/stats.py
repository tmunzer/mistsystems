class Stats():

    def __init__(self, session):
        self._session = session

    def clients(self, site_id):
        uri = "/api/v1/sites/%s/stats/clients" % (site_id)
        resp = self._session.mist_get(uri)
        return resp
