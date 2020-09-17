class Devices():
    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/devices".format(org_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_stats(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/stats/devices".format(org_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def search(self, org_id, search={}, page=1, limit=100):
        """
        Parameters
        org_id: String
        search: Dict
            hostname	string	partial / full hostname
            site_id	string	site id
            model	string	device model
            mac	string	AP mac
            version	string	version
        page: Int
        limit: Int
        """
        uri = "/api/v1/orgs/{0}/devices/search".format(org_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count(self, org_id, distinct="model", page=1, limit=100):
        """
        Parameters
        org_id: String
        distinct: String (default model)
        page: Int
        limit: Int
        """
        uri = "/api/v1/orgs/{0}/devices/count".format(org_id)
        resp = self._session.mist_get(
            uri, query={"distinct": distinct}, page=page, limit=limit)
        return resp


    def search_events(self, org_id, search={}, page=1, limit=100):
        """
        Parameters
        org_id: String
        search: Dict
            org_id	string	org id
            site_id	string	site id
            ap	string	AP mac
            apfw	string	AP Firmware
            model	string	device model
            text	string	event message
            timestamp	string	event time
            type	string	AP_CONFIG_CHANGED_BY_RRM AP_CONFIG_CHANGED_BY_USER AP_CONFIGURED AP_RECONFIGURED AP_RESTART_BY_USER AP_RESTARTED AP_RRM_ACTION CLIENT_DNS_OK MARVIS_DNS_FAILURE
        page: Int
        limit: Int
        """
        uri = "/api/v1/orgs/{0}/devices/events/search".format(org_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_events(self, org_id, distinct="model", page=1, limit=100):
        """
        Parameters
        org_id: String
        distinct: String (default model)
        page: Int
        limit: Int
        """
        uri = "/api/v1/orgs/{0}/devices/events/count".format(org_id)
        resp = self._session.mist_get(
            uri, query={"distinct": distinct}, page=page, limit=limit)
        return resp

    def replace(self, org_id, site_id, mac_old_device, mac_inventory_device):
        """
        Parameters
        org_id: String
        site_id: String (the site_id of the device to be replaced)
        mac_old_device: String (device mac)
        mac_inventory_device: String (mac of the inventory that will be replacing the old one. It has to be claimed and unassigned.)
        """
        uri = "/api/v1/orgs/{0}/inventory/replace".format(org_id)
        body = {
            "site_id": site_id,
            "mac": mac_old_device,
            "inventory_mac": mac_inventory_device
        }
        resp = self._session.mist_post(
            uri, body=body)
        return resp