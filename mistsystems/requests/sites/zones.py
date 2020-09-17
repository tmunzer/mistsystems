class Zones():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, zone_settings):
        uri = "/api/v1/sites/%s/zones" % site_id
        body = zone_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, zone_id, body={}):
        uri = "/api/v1/sites/%s/zones/%s" % (site_id, zone_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, zone_id):
        uri = "/api/v1/sites/%s/zones/%s" % (site_id, zone_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        """
        Get list of Zones
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/zones" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, zone_id):
        """
        Get one Zone details
        Parameters:
            site_id: String
            zone_id: String
        """
        uri = "/api/v1/sites/{0}/zones/{1}".format(site_id, zone_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, site_id, map_id, page=1, limit=100):
        uri = "/api/v1/sites/{0}/stats/zones".format(site_id)
        query = {"map_id": map_id}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, site_id, zone_id):
        uri = "/api/v1/sites/{0}/stats/zones/{1}".format(site_id, zone_id)
        resp = self._session.mist_get(uri)
        return resp

    def search_sessions(self, site_id, query, page=1, limit=100):
        """
        Recent Zone Visits (7-days) are searchable via the following APIs
        Parameters:
            site_id: String
            query: Dict
                user_type: string: user type, client (default) / sdkclient / asset
                user: string: client MAC / Asset MAC / SDK UUID
                scope_id: string: if scope == map/zone/rssizone, the scope id
                scope: string: scope, site (default) / map / zone / rssizone
                tags: string: tags
        """
        uri = "/api/v1/sites/{0}/zones/visits/search".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_sessions(self, site_id, query, page=1, limit=100):
        """
        Parameters:
            site_id: String
            query: Dict
                user_type: string: user type, client (default) / sdkclient / asset
                user: string: client MAC / Asset MAC / SDK UUID
                scope_id: string: if scope == map/zone/rssizone, the scope id
                scope: string: scope, site (default) / map / zone / rssizone
                tags: string: tags
        """
        uri = "/api/v1/sites/{0}/zones/visits/count".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp
