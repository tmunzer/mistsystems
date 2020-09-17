class Assets():

    def __init__(self, session):
        self._session = session

    def create(self, site_id, asset_settings):
        """
        Create site asset 
        Parameters:
            site_id: String
            asset_settings: Dict
                name|string|name / label of the device
                mac|string|bluetooth MAC
        """
        uri = "/api/v1/sites/{0}/assets".format(site_id)
        body = asset_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, asset_id, asset_settings):
        """
        Update site asset settings
        Parameters:
            site_id: String
            asset_id: String
            asset_settings: Dict
                name|string|name / label of the device
                mac|string|bluetooth MAC
        """
        uri = "/api/v1/sites/{0}/assets/{1}".format(site_id, asset_id)
        resp = self._session.mist_put(uri, body=asset_settings)
        return resp

    def delete(self, site_id, asset_id):
        """
        Delete site asset
        Parameters:
            site_id: String
            asset_id: String
        """
        uri = "/api/v1/sites/{0}/assets/{1}".format(site_id, asset_id)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, query={}, page=1, limit=100):
        """
        Get the list of the site assets
        Parameters:
            site_id: String
            query: Dict (dict of search filters)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/assets".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, asset_id):
        """
        Get the list of the site asset filters
        Parameters:
            site_id: String
            asset_id: String
        """
        uri = "/api/v1/sites/{0}/assets/{1}".format(site_id, asset_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, site_id, page=1, limit=100):
        """
        Get stats of the site assets
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/assets".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, site_id, asset_id):
        """
        Get stats of one site asset
        Parameters:
            site_id: String
            asset_id: String
        """
        uri = "/api/v1/sites/{0}/stats/assets/{1}".format(site_id, asset_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_discovered_asset(self, site_id, page=1, limit=100):
        """
        Get stats of the dscovered site assets
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/discovered_assets".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_discovered_asset_by_map(self, site_id, map_id, page=1, limit=100):
        """
        Get stats of the dscovered site assets by map
        Parameters:
            site_id: String
            map_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/maps/{1}/discovered_assets".format(site_id, map_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

