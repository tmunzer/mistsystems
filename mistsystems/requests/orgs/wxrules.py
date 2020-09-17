class WxRules():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, wxrule_settings):
        uri = "/api/v1/orgs/%s/wxrules" % org_id
        body = wxrule_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, wxrule_id, body={}):
        uri = "/api/v1/orgs/%s/wxrules/%s" % (org_id, wxrule_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, wxrule_id):
        uri = "/api/v1/orgs/%s/wxrules/%s" % (org_id, wxrule_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        """
        Get list of WxRules
        Parameters:
            org_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/%s/wxrules" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_derived(self, org_id, resolve, page=1, limit=100):
        """
        Get list of WxRules derived
        Parameters:
            org_id: String
            resolve: Boolean (whether to resolve SITE_VARS, default is false)
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/wxrules/derived".format(org_id)
        query = {"resolve": resolve} if resolve else {}
        resp = self._session.mist_get(uri, query, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, wxrule_id):
        """
        Get one WxRule details
        Parameters:
            org_id: String
            wxrule_id: String
        """
        uri = "/api/v1/orgs/{0}/wxrules/{1}".format(org_id, wxrule_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_usages(self, org_id, page=1, limit=100):
        """
        Get one WxRule usages
        Parameters:
            org_id: String
        """
        uri = "/api/v1/orgs/%s/stats/wxrules" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_currently_used_by_client(self, org_id, client_mac, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/stats/wxrules/{1}".format(org_id, client_mac)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp
