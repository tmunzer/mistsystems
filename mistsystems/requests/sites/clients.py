class Wireless():

    def __init__(self, session):
        self._sessionn = session

    def disconnect_client(self, site_id, client_mac):
        """
        Disconnect a wireless client
        Parameters:
            site_id: String
            client_mac: String
        """
        uri = "/api/v1/sites/{0}/clients/{1}/disconnect".format(
            site_id, client_mac)
        resp = self._sessionn.mist_post(uri)
        return resp

    def disconnect_multiple_clients(self, site_id, client_macs):
        """
        Disconnect multiple wireless clients
        Parameters:
            site_id: String
            client_macs: Array
        """
        uri = "/api/v1/sites/{0}/clients/disconnect".format(site_id)
        resp = self._sessionn.mist_post(uri, body=client_macs)
        return resp

    def unauthorize_client(self, site_id, client_mac):
        """
        Unauthorize a wireless client
        Parameters:
            site_id: String
            client_mac: String
        """
        uri = "/api/v1/sites/{0}/clients/{1}/unauthorize".format(
            site_id, client_mac)
        resp = self._sessionn.mist_post(uri)
        return resp

    def unauthorize_multiple_clients(self, site_id, client_macs):
        """
        Unauthorize multiple wireless clients
        Parameters:
            site_id: String
            client_macs: Array
        """
        uri = "/api/v1/sites/{0}/clients/unauthorize".format(site_id)
        resp = self._sessionn.mist_post(uri, body=client_macs)
        return resp

    def search(self, site_id, search={}, page=1, limit=100):
        """
        Search wireless clients
        Parameters:
            site_id: String
            search: Dict
                mac: string: partial / full MAC address
                hostname: string: partial / full hostname
                device: string: device type, e.g. Mac, Nvidia, iPhone
                os: string: os, e.g. Sierra, Yosemite, Windows 10
                model: string: model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
                ap: string: AP mac where the client has connected to
                ssid: string: SSID
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/search".format(site_id)
        resp = self._sessionn.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def search_client_events(self, site_id, search={}, page=1, limit=100):
        """
        Search client events
        Parameters:
            site_id: String
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/events".format(site_id)
        resp = self._sessionn.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def search_client_sessions(self, site_id, search={}, page=1, limit=100):
        """
        Search client sessions
        Parameters:
            site_id: String
            search: Dict
                ap: string: AP MAC
                band: string: 5 / 24
                client_family: string: E.g. “Mac”, “iPhone”, “Apple watch”
                client_manufacture: string: E.g. “Apple”
                client_model: string: E.g. “8+”, “XS”
                client_os: string: E.g. “Mojave”, “Windows 10”, “Linux”
                ssid: string: SSID
                wlan_id: string: wlan_id
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/sessions/search".format(site_id)
        resp = self._sessionn.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_by_distinct_attributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                mac: string: partial / full MAC address
                hostname: string: partial / full hostname
                device: string: device type, e.g. Mac, Nvidia, iPhone
                os: string: os, e.g. Sierra, Yosemite, Windows 10
                model: string: model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
                ap: string: AP mac where the client has connected to
                ssid: string: SSID
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self._sessionn.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_sessions_by_distinct_attributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                ap: string: AP MAC
                band: string: 5 / 24
                client_family: string: E.g. “Mac”, “iPhone”, “Apple watch”
                client_manufacture: string: E.g. “Apple”
                client_model: string: E.g. “8+”, “XS”
                client_os: string: E.g. “Mojave”, “Windows 10”, “Linux”
                ssid: string: SSID
                wlan_id: string: wlan_id
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/sessions/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self._sessionn.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_events_by_distinct_attributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/events/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self._sessionn.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_client_events(self, site_id, client_mac, search={}, page=1, limit=100):
        """ 
        Get list of client events
        Parameters:
            site_id: String
            client_mac: String
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/clients/{1}/events".format(
            site_id, client_mac)
        resp = self._sessionn.mist_get(uri, query=search, page=page, limit=limit)
        return resp


class Stats():
    def __init__(self, session):
        self._sessionn = session

    def get(self, site_id, page=1, limit=100):
        """
        Get list of client stats
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/clients".format(site_id)
        resp = self._sessionn.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, client_mac):
        """
        Get stats for one client
        Parameters:
            site_id: String
            client_mac: String
        """
        uri = "/api/v1/sites/{0}/stats/clients/{1}".format(site_id, client_mac)
        resp = self._sessionn.mist_get(uri)
        return resp

    def get_on_map(self, site_id, map_id, page=1, limit=100):
        """
        Get list of client stats on a map
        Parameters:
            site_id: String
            map_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/maps/{1}/clients".format(
            site_id, map_id)
        resp = self._sessionn.mist_get(uri, page=page, limit=limit)
        return resp


    def get_unconnected_on_map(self, site_id, map_id, page=1, limit=100):
        """
        Get list of unconnected client stats on a map
        Parameters:
            site_id: String
            map_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/maps/{1}/unconnected_clients".format(
            site_id, map_id)
        resp = self._sessionn.mist_get(uri, page=page, limit=limit)
        return resp
    def get_on_device(self, site_id, device_id, page=1, limit=100):
        """
        Get list of client stats on a device
        Parameters:
            site_id: String
            device_id: Strong
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/devices/{1}/clients".format(
            site_id, device_id)
        resp = self._sessionn.mist_get(uri, page=page, limit=limit)
        return resp


class Wired():
    def __init__(self, session):
        self._sessionn = session

    def search(self, site_id, search={}, page=1, limit=100):
        """
        Search Wired Client
        Parameters:
            site_id: String
            search: Dict
                device_mac: string: device mac
                mac: string: client mac
                port_id: string: port id
                vlan: int: vlan
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/wired_clients/search".format(site_id)
        resp = self._sessionn.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_by_distinct_attributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wired client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up)
            search: Dict
                device_mac: string: device mac
                mac: string: client mac
                port_id: string: port id
                vlan: int: vlan
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/wired_clients/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self._sessionn.mist_get(uri, query=query, page=page, limit=limit)
        return resp
