class AssetFilters():

    def __init__(self, session):
        self._session = session
        
    def create(self, site_id, assetfilter_settings):
        """
        Create site asset filter
        Parameters:
            site_id: String
            assetfilter_settings: Dict
                name: String (asset filter name)
                disabled: Boolean (optional; whether the asset filter is disabled, default is false)
                ibeacon_uuid: String (optional; ibeacon uuid used to filter assets)
                ibeacon_major: Int (optional; ibeacon major value used to filter assets)
                eddystone_uid_namespace: String (optional; eddystone uid namespace used to filter assets)
                eddystone_url: String (optional; eddystone url used to filter assets)
                mfg_company_id: Int (optional; ble manufacturing-specific company-id used to filter assets)
        """
        uri = "/api/v1/sites/{0}/assetfilters".format(site_id)
        body = assetfilter_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, assetfilter_id, assetfilter_settings):
        """
        Update site asset filter settings
        Parameters:
            site_id: String
            assetfilter_id: String
            assetfilter_settings: Dict
                name: String (optional; asset filter name)
                disabled: Boolean (optional; whether the asset filter is disabled, default is false)
                ibeacon_uuid: String (optional; ibeacon uuid used to filter assets)
                ibeacon_major: Int (optional; ibeacon major value used to filter assets)
                eddystone_uid_namespace: String (optional; eddystone uid namespace used to filter assets)
                eddystone_url: String (optional; eddystone url used to filter assets)
                mfg_company_id: Int (optional; ble manufacturing-specific company-id used to filter assets)
        """
        uri = "/api/v1/sites/{0}/assetfilters/{1}".format(site_id, assetfilter_id)
        resp = self._session.mist_put(uri, body=assetfilter_settings)
        return resp
        
    def delete(self, site_id, assetfilter_id):
        uri = "/api/v1/sites/{0}/assetfilters/{1}".format(site_id, assetfilter_id)
        """
        Delete site asset filter
        Parameters:
            site_id: String
            assetfilter_id: String            
        """
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, site_id, query={}, page=1, limit=100):
        """
        Get the list of the site asset filters
        Parameters:
            site_id: String
            query: Dict (dict of search filters)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/assetfilters".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp


    def get_by_id(self, site_id, assetfilter_id):
        """
        Get the list of the site asset filters
        Parameters:
            site_id: String
            assetfilter_id: String
        """
        uri = "/api/v1/sites/{0}/assetfilters/{1}".format(site_id, assetfilter_id)
        resp = self._session.mist_get(uri)
        return resp
