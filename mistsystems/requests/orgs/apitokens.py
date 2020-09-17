class Apitokens():
    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/apitokens".format(org_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_it(self, org_id, apitoken_id):
        uri = "/api/v1/orgs/{0}/apitokens/{1}".format(org_id, apitoken_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, org_id, name, privileges={}):
        """
        Create an organization API Token
        Parameters:
            org_id: String
            name: String            
            privileges: Array of privileges 
                role: String (admin, write, read)
                scope: String (org, site, sitegroup)
                site_id: String (if scope=site)
                sitegroups_id: String (if scope=sitegroup)
        """
        body = {
            "name": name,
            "privileges": privileges
        }
        uri = "/api/v1/orgs/{0}/apitokens".format(org_id)
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, apitoken_id, name=None, privileges=None):
        """
        Update an organization API Token
        Parameters:
            org_id: String
            apitoken_id: String
            name: String            
            privileges: Array of privileges 
                role: String (admin, write, read)
                scope: String (org, site, sitegroup)
                site_id: String (if scope=site)
                sitegroups_id: String (if scope=sitegroup)
        """
        body = {}
        if name:
            body["name"] = name
        if privileges:
            body["privileges"] = privileges
        uri = "/api/v1/orgs/{0}/apitokens/{1}".format(org_id, apitoken_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, apitoken_id):
        uri = "/api/v1/orgs/{0}/apitokens/{1}".format(org_id, apitoken_id)
        resp = self._session.mist_delete(uri)
        return resp
