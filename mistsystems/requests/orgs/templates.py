class Templates():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/templates" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, template_id):
        uri = "/api/v1/orgs/%s/templates/%s" % (org_id, template_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, org_id, template_settings):
        uri = "/api/v1/orgs/%s/templates" % org_id
        resp = self._session.mist_post(uri, body=template_settings)
        return resp

    def update(self, org_id, template_id, template_settings):
        uri = "/api/v1/orgs/{0}/templates/{1}".format(org_id, template_id)
        resp = self._session.mist_put(uri, body=template_settings)
        return resp

    def clone(self, org_id, template_id, name):
        uri = "/api/v1/orgs/{0}/templates/{1}/clone".format(
            org_id, template_id)
        resp = self._session.mist_post(uri, body={"name": name})
        return resp

    def delete(self, org_id, template_id):
        uri = "/api/v1/orgs/%s/templates/%s" % (org_id, template_id)
        resp = self._session.mist_delete(uri)
        return resp
