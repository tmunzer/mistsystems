class Wireless():
    def __init__(self, session):
        self._session = session

    def search(self, org_id, query={}, page=1, limit=100):
        """
        Parameters:
            org_id: String
            query: Dict
                mac	string	partial / full MAC address
                hostname	string	partial / full hostname
                device	string	device type, e.g. Mac, Nvidia, iPhone
                os	string	os, e.g. Sierra, Yosemite, Windows 10
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/clients/search".format(org_id)
        resp = self._session.mist_get(uri, query=query,page=page, limit=limit)
        return resp

    def count(self, org_id, distinct="device", page=1, limit=100):
        """
        Parameters:
            org_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/clients/count".format(org_id)
        resp = self._session.mist_get(uri, query={"distinct": distinct},page=page, limit=limit)
        return resp


    def search_sessions(self, org_id, query={}, page=1, limit=100):
        """
        Parameters:
            org_id: String
            query: Dict
                ap	string	AP MAC
                band	string	5 / 24
                client_family	string	E.g. “Mac”, “iPhone”, “Apple watch”
                client_manufacture	string	E.g. “Apple”
                client_model	string	E.g. “8+”, “XS”
                client_os	string	E.g. “Mojave”, “Windows 10”, “Linux”
                ssid	string	SSID
                wlan_id	string	wlan_id
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/clients/sessions/search".format(org_id)
        resp = self._session.mist_get(uri, query=query,page=page, limit=limit)
        return resp

    def count_sessions(self, org_id, distinct="mac", page=1, limit=100):
        """
        Parameters:
            org_id: String
            distinct: String (ssid, wlan_id, ap, mac, client_family, client_manufacture, client_model, client_os, site_id, default is mac)
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/clients/sessions/count".format(org_id)
        resp = self._session.mist_get(uri, query={"distinct": distinct},page=page, limit=limit)
        return resp

        