class Wlans():

    def __init__(self, session):
        self._session = session

    def get(self, site_id, page=1, limit=100):
        """
        Get list of Wlans
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/wlans" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_derived(self, site_id, resolve, page=1, limit=100):
        """
        Get list of Wlans derived
        Parameters:
            site_id: String
            resolve: Boolean (whether to resolve SITE_VARS, default is false)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/wlans/derived".format(site_id)
        query = {"resolve": resolve} if resolve else {}
        resp = self._session.mist_get(uri, query, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, wlan_id):
        """
        Get one Wlans details
        Parameters:
            site_id: String
            wlan_id: String
        """
        uri = "/api/v1/sites/{0}/wlans/{1}".format(site_id, wlan_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, site_id, wlan_settings):
        """
        Create a Wlan
        Parameters:
            site_id: String
            wlan_settings: Dict (see API documentation)
        """
        uri = "/api/v1/sites/%s/wlans" % site_id
        resp = self._session.mist_post(uri, body=wlan_settings)
        return resp

    def update(self, site_id, wlan_id, wlan_settings):
        """
        Update a Wlan
        Parameters:
            site_id: String
            wlan_id: String
            wlan_settings: Dict (see API documentation)
        """
        uri = "/api/v1/sites/{0}/wlans/{1}".format(site_id, wlan_id)
        resp = self._session.mist_put(uri, body=wlan_settings)
        return resp

    def delete(self, site_id, wlan_id):
        """
        Delete a Wlan
        Parameters:
            site_id: String
            wlan_id: String
        """
        uri = "/api/v1/sites/%s/wlans/%s" % (site_id, wlan_id)
        resp = self._session.mist_delete(uri)
        return resp

    def add_portal_image(self, site_id, wlan_id, image_path):
        uri = "/api/v1/sites/%s/wlans/%s/portal_image" % (site_id, wlan_id)
        files = {'file': open(image_path, 'rb').read()}
        resp = self._session.mist_post_file(uri, files=files)
        return resp

    def delete_portal_image(self, site_id, wlan_id):
        uri = "/api/v1/sites/%s/wlans/%s/portal_image" % (site_id, wlan_id)
        resp = self._session.mist_delete(uri)
        return resp

    def update_portal_template(self, site_id, wlan_id, portal_template_body):
        uri = "/api/v1/sites/%s/wlans/%s/portal_template" % (site_id, wlan_id)
        body = portal_template_body
        resp = self._session.mist_put(uri, body=body)
        return resp

