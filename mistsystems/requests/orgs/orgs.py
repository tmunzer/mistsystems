
class Orgs():

    def __init__(self, session):
        self._session = session

    def get_by_id(self, org_id):
        uri = "/api/v1/orgs/%s" % org_id
        resp = self._session.mist_get(uri)
        return resp

    def create(self, data):
        uri = "/api/v1/orgs"
        resp = self._session.mist_post(uri, body=data)
        return resp

    def update(self, org_id, data):
        uri = "/api/v1/orgs/{0}".format(org_id)
        resp = self._session.mist_put(uri, body=data)
        return resp

    def delete(self, org_id):
        uri = "/api/v1/orgs/{0}".format(org_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get_stats(self, org_id):
        uri = "/api/v1/orgs/{0}/stats".format(org_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_settings(self, org_id):
        uri = "/api/v1/orgs/{0}/setting".format(org_id)
        resp = self._session.mist_get(uri)
        return resp

    def update_settings(self, org_id, data):
        uri = "/api/v1/orgs/{0}/setting".format(org_id)
        resp = self._session.mist_put(uri, body=data)
        return resp

    def clone(self, org_id, new_name):
        uri = "/api/v1/orgs/{0}/clone"
        resp = self._session.mist_post(uri, body={"name": new_name})
        return resp
