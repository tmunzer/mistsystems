class Rogues():

    def __init__(self, session):
        self._session = session

    def get_aps(self, site_id, duration=None, rogue_type=None, page=1, limit=100):
        """
        Get list of rogue APs
        Parameters:
            site_id: String
            duraton: String (optional. 1d or 1h, default is 1d)
            rogue_type: String (optional, honeypot, lan, others, spoof. Default is others)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/insights/rogues" % site_id
        query = {}
        if duration: query["duration"]=duration
        if rogue_type: query["type"]=rogue_type
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_clients(self, site_id, duration=None, page=1, limit=100):
        """
        Get list of rogue APs
        Parameters:
            site_id: String
            duraton: String (optional. 1d or 1h, default is 1d)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/insights/rogues/clients" % site_id
        query = {}
        if duration: query["duration"]=duration
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_ap_by_id(self, site_id, rogue_bssid):
        """
        Get list of rogue APs
        Parameters:
            site_id: String
            rogue_bssid: String            
        """
        uri = "/api/v1/sites/{0}/rogues/{1}".format(site_id, rogue_bssid)
        resp = self._session.mist_get(uri)
        return resp

    def search_events(self, site_id, duration=None, rogue_type=None, page=1, limit=100):
        """
        search list of rogue APs events
        Parameters:
            site_id: String
            duraton: String (optional. 1d or 1h, default is 1d)
            rogue_type: String (optional, honeypot, lan, others, spoof. Default is others)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/rogues/events/search".format(site_id)
        query = {}
        if duration: query["duration"]=duration
        if rogue_type: query["type"]=rogue_type
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_events(self, site_id, duration=None, rogue_type=None, page=1, limit=100):
        """
        count list of rogue APs events
        Parameters:
            site_id: String
            duraton: String (optional. 1d or 1h, default is 1d)
            rogue_type: String (optional, honeypot, lan, others, spoof. Default is others)
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/{0}/rogues/events/count".format(site_id)
        query = {}
        if duration: query["duration"]=duration
        if rogue_type: query["type"]=rogue_type
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    
    def deauth_clients(self, site_id, rogue_bssid):
        """
        Send Deauth frame to clients connected to a Rogue AP
        Parameters:
            site_id: String
            rogue_bssid: String
        """
        uri = "/api/v1/sites/{0}/rogues/{1}/deauth_clients".format(site_id, rogue_bssid)
        resp = self._session.mist_post(uri)
        return resp