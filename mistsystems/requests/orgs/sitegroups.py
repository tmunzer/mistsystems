class SiteGroups():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/sitegroups" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, sitegroup_id):
        uri = "/api/v1/orgs/%s/sitegroups/%s" % (org_id, sitegroup_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, org_id, group_name):
        uri = "/api/v1/orgs/%s/sitegroups" % org_id
        body = group_name
        resp = self._session.mist_post(uri, body=body)
        return resp

    def delete(self, org_id, sitegroup_id):
        uri = "/api/v1/orgs/%s/sitegroups/%s" % (org_id, sitegroup_id)
        resp = self._session.mist_delete(uri)
        return resp
