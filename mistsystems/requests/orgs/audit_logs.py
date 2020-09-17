class AuditLogs():
    def __init__(self, session):
        self._session = session

    def get(self, org_id, query={}, page=1, limit=100):
        """
        Parameters: 
            org_id: String
            query: Dict
                site_id: String
                admin_name: String
                message: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/orgs/{0}/logs".format(org_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_by_distinct_attributes(self, org_id, distrinct='admin_name', page=1, limit=100):
        """
        Parameters: 
            org_id: String
            distrinct: String (admin_id / admin_name / message / site_id, default is admin_name)
        """
        uri = "/api/v1/orgs/{0}/logs/count".format(org_id)
        resp = self._session.mist_get(uri, query={"distinct": distrinct}, page=page, limit=limit)
        return resp