class WxTags():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, wxtag_settings):
        uri = "/api/v1/orgs/%s/wxtags" % org_id
        body = wxtag_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, wxtag_id, body={}):
        uri = "/api/v1/orgs/%s/wxtags/%s" % (org_id, wxtag_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, wxtag_id):
        """
        Parameters:
            org_id: String
            wxtag_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/%s/wxtags/%s" % (org_id, wxtag_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        """
        Parameters:
            org_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/%s/wxtags" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, wxtag_id):
        """
        Parameters:
            org_id: String
            wxtag_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/%s/wxtags/%s" % (org_id, wxtag_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_applications(self, org_id, page=1, limit=100):
        """
        Parameters:
            org_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/%s/wxtags/apps" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_matching_clients(self, org_id, wxtag_id, page=1, limit=100):
        """
        Parameters:
            org_id: String
            wxtag_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/wxtags/{1}/clients".format(org_id, wxtag_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
        
