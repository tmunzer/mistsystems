class Inventory():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/inventory" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def add(self, org_id, serials):
        uri = "/api/v1/orgs/%s/inventory" % org_id
        body = serials
        resp = self._session.mist_post(uri, body=body)
        return resp

    def delete_multiple(self, org_id, serials=[], macs=[]):
        uri = "/api/v1/orgs/%s/inventory" % org_id
        body = {
            "op": "delete",
            "serials": serials,
            "macs": macs
        }
        resp = self._session.mist_put(uri, body=body)
        return resp

    def unassign(self, org_id, macs):
        uri = "/api/v1/orgs/%s/inventory" % org_id
        body = {
            "op": "unassign",
            "macs": macs,
        }
        resp = self._session.mist_put(uri, body=body)
        return resp

    def assign_macs_to_site(self, org_id, site_id, macs):
        uri = "/api/v1/orgs/%s/inventory" % org_id
        if type(macs) == str:
            macs = [macs]
        body = {
            "op": "assign",
            "site_id": site_id,
            "macs": macs,
            "no_reassign": False
        }
        resp = self._session.mist_put(uri, body=body)
        return resp
