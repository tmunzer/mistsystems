class RssiZones():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, rssizone_settings):
        uri = "/api/v1/sites/%s/rssizones" % site_id
        body = rssizone_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, rssizone_id, body={}):
        uri = "/api/v1/sites/%s/rssizones/%s" % (site_id, rssizone_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, rssizone_id):
        uri = "/api/v1/rsites/%s/ssizones/%s" % (site_id, rssizone_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/rssizones" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, rssizone_id):
        uri = "/api/v1/sites/{0}/rssizones/{1}".format(site_id, rssizone_id)
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
        uri = "/api/v1/sites/{0}/rssizones/visits/search".format(site_id)
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
        uri = "/api/v1/sites/{0}/rssizones/visits/count".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp