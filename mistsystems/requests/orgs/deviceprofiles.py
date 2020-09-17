class DeviceProfiles():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, deviceprofile_settings):
        uri = "/api/v1/orgs/%s/deviceprofiles" % org_id
        body = deviceprofile_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, deviceprofile_id, body={}):
        uri = "/api/v1/orgs/%s/deviceprofiles/%s" % (org_id, deviceprofile_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, deviceprofile_id):
        uri = "/api/v1/orgs/%s/deviceprofiles/%s" % (org_id, deviceprofile_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/deviceprofiles" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, deviceprofile_id):
        uri = "/api/v1/orgs/{0}/deviceprofiles/{1}".format(org_id, deviceprofile_id)
        resp = self._session.mist_get(uri)
        return resp

    def assign(self, org_id, deviceprofile_id, macs=[]):
        uri = "/api/v1/orgs/{0}/deviceprofiles/{1}/assign".format(org_id, deviceprofile_id)
        body = {"macs": macs}
        resp = self._session.mist_post(uri, body=body)
        return resp

    def unassign(self, org_id, deviceprofile_id, macs=[]):
        uri = "/api/v1/orgs/{0}/deviceprofiles/{1}/unassign".format(org_id, deviceprofile_id)
        body = {"macs": macs}
        resp = self._session.mist_post(uri, body=body)
        return resp
