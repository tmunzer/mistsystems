class Sites():

    def __init__(self, session):
        self._sessionn = session

    def create(self, org_id, site_settings):
        uri = "/api/v1/orgs/%s/sites" % org_id
        body = site_settings
        resp = self._sessionn.mist_post(uri, body=body)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/sites" % org_id
        resp = self._sessionn.mist_get(uri, page=page, limit=limit)
        return resp