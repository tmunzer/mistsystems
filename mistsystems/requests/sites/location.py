class Location():
    def __init__(self, session):
        self._sessionn = session

    def get_sdk_stats(self, site_id, map_id):
        uri = "/api/v1/sites/{0}/stats/maps/{1}/sdkclients".format(
            site_id, map_id)
        resp = self._sessionn.mist_get(uri)
        return resp

    def get_sdk_stats_by_id(self, site_id, map_id, sdkclient_uuid):
        uri = "/api/v1/sites/{0}/stats/maps/{1}/sdkclients/{2}".format(
            site_id, map_id, sdkclient_uuid)
        resp = self._sessionn.mist_get(uri)
        return resp
