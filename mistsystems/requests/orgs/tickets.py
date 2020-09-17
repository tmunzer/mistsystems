class Tickets():

    def __init__(self, session):
        self._session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/tickets" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, ticket_id):
        uri = "/api/v1/orgs/%s/tickets/%s" % (org_id, ticket_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, org_id, subject, ticket_type, comment):
        uri = "/api/v1/orgs/%s/tickets" % org_id
        body = {
            "subject": subject,
            "type": ticket_type,
            "comment": comment
        }
        resp = self._session.mist_post(uri, body=body)
        return resp

    def add_comment(self, org_id, ticket_id, comment, file=None):
        uri = "/api/v1/orgs/{0}/tickets/{1}/comments".format(org_id, ticket_id)
        resp = self._session.mist_post(
            uri, body={"comment": comment}, files=file)
        return resp

    def update(self, org_id, ticket_id, subject=None, ticket_type=None, status=None):
        uri = "/api/v1/orgs/{0}/tickets/{1}".format(org_id, ticket_id)
        body={}
        if subject: body["subject"]= subject
        if ticket_type: body["type"]= ticket_type
        if status: body["status"]= status
        resp = self._session.mist_put(uri, body=body)
        return resp
