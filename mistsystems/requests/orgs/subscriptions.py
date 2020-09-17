class Subscriptions():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/self/subscriptions" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def subscribe(self, org_id, subscription):
        uri = "/api/v1/orgs/%s/subscriptions" % org_id
        body = subscription
        resp = self._session.mist_post(uri, body=body)
        return resp

    def ussubscribe(self, org_id, subscription_id):
        uri = "/api/v1/orgs/%s/subscriptions/%s" % (org_id, subscription_id)
        resp = self._session.mist_delete(uri)
        return resp
