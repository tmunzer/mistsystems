class AssetFilters():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, assetfilter_settings):
        uri = "/api/v1/orgs/%s/assetfilters" % org_id
        body = assetfilter_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, assetfilter_id, body={}):
        uri = "/api/v1/orgs/%s/assetfilters/%s" % (org_id, assetfilter_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, assetfilter_id):
        uri = "/api/v1/orgs/%s/assetfilters/%s" % (org_id, assetfilter_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/assetfilters" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, assetfilter_id):
        uri = "/api/v1/orgs/%s/assetfilters/%s" % (org_id, assetfilter_id)
        resp = self._session.mist_get(uri)
        return resp