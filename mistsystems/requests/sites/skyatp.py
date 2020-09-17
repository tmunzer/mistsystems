class SkyAtp():
    def __init__(self, session):
        self._session = session

    def search_events(self, site_id, query={}, page=1, limit=100):
        """
        Parameters:
            site_id: String
            query: Dict
                type: string	event type, e.g. cc, fs, mw
                mac: string	client MAC
                device_mac: string	device MAC
                threat_level: int	threat level
                ip: string	client ip
            page: Int
            limit: Int
        """
        uri="/api/v1/sites/{0}/skyatp/events/search".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_events(self, site_id, distinct="type", page=1, limit=100):
        """
        Parameters:
            site_id: String
            distinct: String (ype, mac, device_mac, threat_level, default is type)
            page: Int
            limit: Int
        """
        uri="/api/v1/sites/{0}/skyatp/events/count".format(site_id)
        resp = self._session.mist_get(uri, query={"distinct": distinct}, page=page, limit=limit)
        return resp