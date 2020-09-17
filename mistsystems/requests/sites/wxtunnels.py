class WxTunnels():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, wxtunnel_settings):
        uri = "/api/v1/sites/%s/wxtunnels" % site_id
        body = wxtunnel_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, wxtunnel_id, body={}):
        uri = "/api/v1/sites/%s/wxtunnels/%s" % (site_id, wxtunnel_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, wxtunnel_id):
        uri = "/api/v1/sites/%s/wxtunnels/%s" % (site_id, wxtunnel_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        """
        Get list of Tunnels
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/wxtunnels" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, wxtunnel_id):
        """
        Get one Tunnel details
        Parameters:
            site_id: String
            wxtunnel_id: String
        """
        uri = "/api/v1/sites/{0}/wxtunnels/{1}".format(site_id, wxtunnel_id)
        resp = self._session.mist_get(uri)
        return resp
