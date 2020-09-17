class Beacons():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, beacon_settings):
        """
        Create site beacon
        Parameters:
            site_id: String
            beacon_settings: Dict
                type: tring: default is eddystone-uid
                ibeacon_uuid: string: bluetooth tag UUID
                ibeacon_major: int: bluetooth tag major
                ibeacon_minor: int: bluetooth tag minor
                eddystone_namespace: string: Eddystone-UID namespace (10 bytes) in hexstring format
                eddystone_instance: string: Eddystone-UID instance (6 bytes) in hexstring format
                eddystone_url: string: Eddystone-URL url
                power: int: in dBm, default is -12
                name: string: name / label of the device
                map_id: string: map where the device belongs to
                x: float: x in pixel
                y: float: y in pixel
                mac: string: optional, MAC of the beacon, currently used only to identify battery voltage
        """
        uri = "/api/v1/sites/{0}/beacons".format(site_id)
        resp = self._session.mist_post(uri, body=beacon_settings)
        return resp

    def update(self, site_id, beacon_id, beacon_settings):
        """
        Update site beacon
        Parameters:
            site_id: String
            beacon_id: String
            beacon_settings: Dict
                type: tring: default is eddystone-uid
                ibeacon_uuid: string: bluetooth tag UUID
                ibeacon_major: int: bluetooth tag major
                ibeacon_minor: int: bluetooth tag minor
                eddystone_namespace: string: Eddystone-UID namespace (10 bytes) in hexstring format
                eddystone_instance: string: Eddystone-UID instance (6 bytes) in hexstring format
                eddystone_url: string: Eddystone-URL url
                power: int: in dBm, default is -12
                name: string: name / label of the device
                map_id: string: map where the device belongs to
                x: float: x in pixel
                y: float: y in pixel
                mac: string: MAC of the beacon, currently used only to identify battery voltage
        """
        uri = "/api/v1/sites/{0}/beacons/{1}".format(site_id, beacon_id)
        resp = self._session.mist_put(uri, body=beacon_settings)
        return resp

    def delete(self, site_id, beacon_id):
        """
        Delete site beacon
        Parameters:
            site_id: String
            beacon_id: String
        """
        uri = "/api/v1/sites/{0}/beacons/{1}".format(site_id, beacon_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        """
        Get list of the site beacons
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/beacons".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, beacon_id):
        """
        Get details of the site beacon
        Parameters:
            site_id: String
            beacon_id: String            
        """
        uri = "/api/v1/sites/{0}/beacons/{1}".format(site_id, beacon_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, site_id, page=1, limit=100):
        """
        Get stats of the site breacons
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/beacons".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp