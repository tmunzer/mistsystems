class Webhooks():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, webhook_settings):
        uri = "/api/v1/orgs/%s/webhooks" % org_id
        body = webhook_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, webhook_id, body={}):
        uri = "/api/v1/orgs/%s/webhooks/%s" % (org_id, webhook_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, webhook_id):
        uri = "/api/v1/orgs/%s/webhooks/%s" % (org_id, webhook_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/webhooks" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, webhook_id):
        uri = "/api/v1/orgs/%s/webhooks/%s" % (org_id, webhook_id)
        resp = self._session.mist_get(uri)
        return resp