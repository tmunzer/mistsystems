class SystemEvents():

    def __init__(self, session):
        self._session = session

    def get_definition(self):
        uri = "/api/v1/const/system_events"
        resp = self._session.mist_get(uri)
        return resp

    def search(self, site_id, mtype, start, end):
        uri = "/api/v1/sites/%s/events/system/search" % site_id
        query = {"type": mtype, "start": start, "end": end}
        resp = self._session.mist_get(uri, query=query)
        return resp

    def count(self, site_id, mtype, start, end):
        uri = "/api/v1/sites/%s/events/system/coun" % site_id
        query = {"type": mtype, "start": start, "end": end}
        resp = self._session.mist_get(uri, query=query)
        return resp
