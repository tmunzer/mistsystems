class WxTags():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, wxtag_settings):
        uri = "/api/v1/sites/%s/wxtags" % site_id
        body = wxtag_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, wxtag_id, body={}):
        uri = "/api/v1/sites/%s/wxtags/%s" % (site_id, wxtag_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, wxtag_id):
        uri = "/api/v1/sites/%s/wxtags/%s" % (site_id, wxtag_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        """
        Get list of WxRules
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/wxtags" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, wxtag_id):
        """
        Get one WxRule details
        Parameters:
            site_id: String
            wxtag_id: String
        """
        uri = "/api/v1/sites/{0}/wxtags/{1}".format(site_id, wxtag_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_applications(self, site_id, page=1, limit=100):
        """
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/wxtags/apps" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_matching_clients(self, site_id, wxtag_id, page=1, limit=100):
        """
        Parameters:
            site_id: String
            wxtag_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/wxtags/{1}/clients".format(site_id, wxtag_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
        