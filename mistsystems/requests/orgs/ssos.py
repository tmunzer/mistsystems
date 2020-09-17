class Ssos():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/ssos" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def create(self, org_id, sso):
        uri = "/api/v1/orgs/%s/ssos" % org_id
        body = sso
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, sso_id, sso):
        uri = "/api/v1/orgs/%s/ssos/%s" % (org_id, sso_id)
        body = sso
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, sso_id):
        uri = "/api/v1/orgs/%s/ssos/%s" % (org_id, sso_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get_saml_metadata(self, org_id, sso_id):
        uri = "/api/v1/orgs/%s/ssos/%s/metadata" % (org_id, sso_id)
        resp = self._session.mist_get(uri)
        return resp

    def download_saml_metadata(self, org_id, sso_id):
        uri = "/api/v1/orgs/%s/ssos/%s/metadata.xml" % (org_id, sso_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_sso_failures(self, org_id, sso_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/ssos/%s/failures" % (org_id, sso_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
