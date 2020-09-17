class MxTunnels():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, mxtunnel_settings):
        uri = "/api/v1/orgs/%s/mxtunnels" % org_id
        body = mxtunnel_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, mxtunnel_id, body={}):
        uri = "/api/v1/orgs/%s/mxtunnels/%s" % (org_id, mxtunnel_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, mxtunnel_id):
        uri = "/api/v1/orgs/%s/mxtunnels/%s" % (org_id, mxtunnel_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/mxtunnels" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, mxtunnel_id):
        uri = "/api/v1/orgs/%s/mxtunnels/%s" % (org_id, mxtunnel_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/stats/mxtunnels/search" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, org_id, mxtunnel_id):
        uri = "/api/v1/orgs/%s/stats/mxtunnels/%s" % (org_id, mxtunnel_id)
        resp = self._session.mist_get(uri)
        return resp
