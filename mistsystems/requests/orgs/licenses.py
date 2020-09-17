class Licenses():

    def __init__(self, session):
        self._session = session

    def summary(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/{0}/licenses".format(org_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def usage_by_site(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/licenses/usages" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def delete(self, org_id, subscription_id): 
        uri = "/api/v1/orgs/{0}/licenses".format(org_id)
        body = {
            "op": "delete",
            "subscription_id": subscription_id
        }
        resp = self._session.mist_post(uri, body=body)
        return resp


    def claim_order(self, org_id, code, mtype="all"):
        uri = "/api/v1/orgs/%s/claim" % org_id
        body = {
            "code": code,
            "type": mtype
        }
        resp = self._session.mist_post(uri, body=body)
        return resp

    def move_to_another_org(self, org_id, subscription_id, dst_org_id, quantity=1):
        uri = "/api/v1/orgs/{0}/licenses".format(org_id)
        body = {
            "op": "amend",
            "subscription_id": subscription_id,
            "dst_org_id": dst_org_id,
            "quantity": quantity
        }
        resp = self._session.mist_put(uri, body=body)
        return resp

    def undo_licence_move(self, org_id, amendment_id):
        uri = "/api/v1/orgs/{0}/licenses".format(org_id)
        body = {
            "op": "unamend",
            "amendment_id": amendment_id
        }
        resp = self._session.mist_put(uri, body=body)
        return resp
