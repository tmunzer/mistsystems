class Webhooks():

    def __init__(self, session):
        self._session = session

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/webhooks" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, webhook_id):
        uri = "/api/v1/sites/%s/webhooks/%s" % (site_id, webhook_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, site_id, webhook):
        uri = "/api/v1/sites/%s/webhooks" % site_id
        resp = self._session.mist_post(uri, body=webhook)
        return resp

    def update(self, site_id, webhook_id, webhook_settings):
        uri = "/api/v1/sites/%s/webhooks/%s" % (site_id, webhook_id)
        resp = self._session.mist_put(uri, body=webhook_settings)
        return resp

    def delete(self, site_id, webhook_id):
        uri = "/api/v1/sites/%s/webhooks/%s" % (site_id, webhook_id)
        resp = self._session.mist_delete(uri)
        return resp

    def ping (self, site_id, webhook_id):
        uri = "/api/v1/sites/{0}/webhooks/{1}/ping".format(site_id, webhook_id)
        resp = self._session.mist_post(uri, body=webhook_id)
        return resp