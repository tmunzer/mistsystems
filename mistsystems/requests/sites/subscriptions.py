class Subscriptions():

    def __init__(self, session):
        self._session = session

    def subscribe(self, site_id):
        uri = "/api/v1/rsites/{0}/subscriptions".format(site_id)
        resp = self._session.mist_post(uri)
        return resp

    def unsubscribe(self, site_id, rssizone_id):
        uri = "/api/v1/rsites/{0}/subscriptions".format(site_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/self/subscriptions"
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
