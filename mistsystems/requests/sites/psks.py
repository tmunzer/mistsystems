class Psks():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, psk_settings):
        """
        Create a new Personal PSK
        Parameters:
            site_id: String
            psk_settings: Dict
                name: string: a name for the PSK
                passphrase: string: passphrase of the PSK (8-63 character or 64 in hex)
                ssid: string: SSID this PSK should be applicable to
                usage: string: multi (default) / single
                vlan_id: int: VLAN for this PSK key
                mac: string: if usage==single, the mac that this PSK ties to, empty if auto-binding
        """
        uri = "/api/v1/sites/%s/psks" % site_id
        resp = self._session.mist_post(uri, body=psk_settings)
        return resp

    def get(self, site_id, name=None, ssid=None, page=1, limit=100):
        """
        Get list of Personal PSKs
        Parameters:
            site_id: String
            name: String (optional)
            ssid: String (optional)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/psks" % site_id
        query = {}
        if name:
            query["name"] = name
        if ssid:
            query["ssid"] = ssid
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, psk_id):
        """
        Get one Personal PSK
        Parameters:
            site_id: String
            psk_id: String
        """
        uri = "/api/v1/sites/{0}/psks/{1}".format(site_id, psk_id)
        resp = self._session.mist_get(uri)
        return resp


    def delete(self, site_id, psk_id):
        """
        Delete one Personal PSK
        Parameters:
            site_id: String
            psk_id: String
        """
        uri = "/api/v1/sites/{0}/psks/{1}".format(site_id, psk_id)
        resp = self._session.mist_delete(uri)
        return resp
