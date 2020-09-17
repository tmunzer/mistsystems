class Certificates():
    def __init__(self, session):
        self._session = session

    def get(self, org_id):
        uri = "/api/v1/orgs/{0}/cert".format(org_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_crl(self, org_id):
        uri = "/api/v1/orgs/{0}/crl".format(org_id)
        resp = self._session.mist_get(uri)
        return resp

    def clear(self, org_id):
        uri = "/api/v1/orgs/{0}/cert/regenerate".format(org_id)
        resp = self._session.mist_post(uri)
        return resp
