class WxRules():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, wxrule_settings):
        uri = "/api/v1/sites/%s/wxrules" % site_id
        body = wxrule_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, wxrule_id, body={}):
        uri = "/api/v1/sites/%s/wxrules/%s" % (site_id, wxrule_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, wxrule_id):
        uri = "/api/v1/sites/%s/wxrules/%s" % (site_id, wxrule_id)
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
        uri = "/api/v1/sites/%s/wxrules" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_derived(self, site_id, resolve, page=1, limit=100):
        """
        Get list of WxRules derived
        Parameters:
            site_id: String
            resolve: Boolean (whether to resolve SITE_VARS, default is false)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/wxrules/derived".format(site_id)
        query = {"resolve": resolve} if resolve else {}
        resp = self._session.mist_get(uri, query, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, wxrule_id):
        """
        Get one WxRule details
        Parameters:
            site_id: String
            wxrule_id: String
        """
        uri = "/api/v1/sites/{0}/wxrules/{1}".format(site_id, wxrule_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_usages(self, site_id, page=1, limit=100):
        """
        Get one WxRule usages
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/%s/stats/wxrules" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_currently_used_by_client(self, site_id, client_mac, page=1, limit=100):
        uri = "/api/v1/sites/{0}/stats/wxrules/{1}".format(site_id, client_mac)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
