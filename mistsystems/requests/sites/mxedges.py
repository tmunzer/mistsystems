class MxEdges():
    def __init__(self, session):
        self._session= session

    def get_stats(self, site_id, page=1, limit=100):
        """
        Get site mist edges stats
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/stats/mxedges" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, site_id, mxedge_id):
        """
        Get one site mist edge stat
        Parameters:
            site_id: String
            mxedge_id: String
        """
        uri = "/api/v1/sites/{0}/mxedges/{1}".format(site_id, mxedge_id)
        resp = self._session.mist_get(uri)
        return resp