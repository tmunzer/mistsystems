class MxEdges():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, mxedge_settings):
        uri = "/api/v1/orgs/%s/mxedges" % org_id
        body = mxedge_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, mxedge_id, body={}):
        uri = "/api/v1/orgs/%s/mxedges/%s" % (org_id, mxedge_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, mxedge_id):
        uri = "/api/v1/orgs/%s/mxedges/%s" % (org_id, mxedge_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/mxedges" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, mxedge_id):
        uri = "/api/v1/orgs/%s/mxedges/%s" % (org_id, mxedge_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/stats/mxedges" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, org_id, mxedge_id):
        uri = "/api/v1/orgs/%s/stats/mxedges/%s" % (org_id, mxedge_id)
        resp = self._session.mist_get(uri)
        return resp

    def unregister(self, org_id, mxedge_id):
        uri = "/api/v1/orgs/%s/stats/mxedges/%s/unregister" % (org_id, mxedge_id)
        resp = self._session.mist_post(uri)
        return resp

    def restart(self, org_id, mxedge_id):
        uri = "/api/v1/orgs/%s/stats/mxedges/%s/restart" % (org_id, mxedge_id)
        resp = self._session.mist_post(uri)
        return resp

    def claim(self, org_id, claim_code):
        uri = "/api/v1/orgs/%s/stats/mxedges" % (org_id)
        resp = self._session.mist_post(uri, body={"code": claim_code})
        return resp

    def assign_to_site(self, org_id, mxedge_ids, site_id):
        uri = "/api/v1/orgs/%s/stats/mxedges/assign" % (org_id)
        body = {
            "site_id" : site_id,
            "mxedge_ids" : mxedge_ids
        }
        resp = self._session.mist_post(uri, body=body)
        return resp


    def unassign_from_site(self, org_id, mxedge_ids):
        uri = "/api/v1/orgs/%s/stats/mxedges/assign" % (org_id)
        body = {
            "mxedge_ids" : mxedge_ids
        }
        resp = self._session.mist_post(uri, body=body)
        return resp
