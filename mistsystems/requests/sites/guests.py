class Guests():
    def __init__(self, session):
        self._session = session

    def get(self, site_id, page=1, limit=100):
        """
        get all the authorized guests
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/guests".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, guest_mac):
        """
        get the information about an authorized guest
        Parameters:
            site_id: String
            guest_mac: String
        """
        uri = "/api/v1/sites/{0}/guests/{1}".format(site_id, guest_mac)
        resp = self._session.mist_get(uri)
        return resp

    def search(self, site_id, search={}, page=1, limit=100):
        """
        search for authorized guests
        Parameters:
            site_id: String
            search: Dict 
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/guests/search".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def count(self, site_id, distinct="auth_method", page=1, limit=100):
        """
        search for authorized guests
        Parameters:
            site_id: String
            distinct: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/guests/count".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def update(self, site_id, guest_mac, guest_settings):
        """
        update guest authorization
        Parameters:
            site_id: String
            guest_mac: String
            guest_settings: Dict
        """
        uri = "/api/v1/sites/{0}/guests/{1}".format(site_id, guest_mac)
        resp = self._session.mist_put(uri, guest_settings)
        return resp

    def delete(self, site_id, guest_mac):
        """
        delete guest authorization
        Parameters:
            site_id: String
            guest_mac: String
        """
        uri = "/api/v1/sites/{0}/guests/{1}".format(site_id, guest_mac)
        resp = self._session.mist_delete(uri)
        return resp
