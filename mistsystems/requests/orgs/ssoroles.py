class SsoRoles():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/ssoroles" % org_id
        resp = self._session.mist_get(uri, org_id, page=page, limit=limit)
        return resp

    def create(self, org_id, ssorole):
        uri = "/api/v1/orgs/%s/ssoroles" % org_id
        body = ssorole
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, ssorole_id, ssorole):
        uri = "/api/v1/orgs/%s/ssoroles/%s" % (org_id, ssorole_id)
        body = ssorole
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, ssorole_id):
        uri = "/api/v1/orgs/%s/ssoroles/%s" % (org_id, ssorole_id)
        resp = self._session.mist_delete(uri)
        return resp