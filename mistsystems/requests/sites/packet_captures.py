class PacketCaptures():
    def __init__(self, session):
        self._session = session

    def get(self, site_id, client_mac=None, start=None, end=None, page=1, limit=100):
        """
        Get list of existing packet captures
        Parameters:
            site_id: String
            client_mac: String
            start: Int
            end: Int
            page: Int
            limit: Int
        """
        query = {}
        if client_mac:
            query["client_mac"] = client_mac
        if start:
            query["start"] = start
        if end:
            query["end"] = end
        uri = "/api/v1/sites/{0}/pcaps".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_status(self, site_id):
        """
        Get packet capture status
        Parameters:
            site_id: String
            mxedge_id: String
        """
        uri = "/api/v1/sites/{0}/pcaps/capture".format(site_id)
        resp = self._session.mist_get(uri)
        return resp

    def start(self, site_id, capture_type, num_packets=None, duration=None, max_pkt_length=None, ssid=None, ap_mac=None, client_mac=None):
        """
        Start a packet capture on APs
        Parameters:
            site_id: String
            capture_type: String (client, new_assoc, wired)
            num_packets: Int (0=unlimited, defaut is 1024 for client type, 100 for now_assoc)
            duration: Int (default is 600, max 86400)
            max_pkt_length: Int (default is 128, max is 2048)
            ssid: String (optional)
            ap_mac: String (optional)
            client_mac: String (optional)
        """
        body = {"type": capture_type}
        if num_packets:
            body["num_packets"] = num_packets
        if duration:
            body["duration"] = duration
        if max_pkt_length:
            body["num_packets"] = num_packets
        if ssid:
            body["ssid"] = ssid
        if ap_mac:
            body["ap_mac"] = ap_mac
        if client_mac:
            body["client_mac"] = client_mac
        uri = "/api/v1/sites/{0}/pcaps/capture".format(site_id)
        resp = self._session.mist_post(uri, body=body)
        return resp

    def stop(self, site_id):
        """
        Stop current packet capture
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/{0}/pcaps/capture".format(site_id)
        resp = self._session.mist_delete(uri)
        return resp
