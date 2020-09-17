class Settings():

    def __init__(self, session):
        self._session = session

    def get(self, site_id):
        uri = "/api/v1/sites/%s/setting" % site_id
        resp = self._session.mist_get(uri)
        return resp

    def update(self, site_id, settings):
        uri = "/api/v1/sites/%s/setting" % site_id
        resp = self._session.mist_put(uri, body=settings)
        return resp
