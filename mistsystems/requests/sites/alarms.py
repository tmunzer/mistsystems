class Alarms():

    def __init__(self, session):
        self._session = session        
        
    def ack(self, site_id, alarm_id, note=""):
        """
        Acknowledge one site alarm.
        Parameters:
            site_id: String
            alarm_id: String (the id of the alarm to ack)
            note: String (optional)
        """
        uri = "/api/v1/sites/{0}/alarms/{1}/ack".format(site_id, alarm_id)
        body = {"note": note}
        resp = self._session.mist_post(uri, body=body)
        return resp

    def unack(self, site_id, alarm_id):
        """
        Un-acknowledge one site alarm.
        Parameters:
            site_id: String
            alarm_id: String (the id of the alarm to unack)
        """
        uri = "/api/v1/sites/{0}/alarms/{1}/unack".format(site_id, alarm_id)
        resp = self._session.mist_post(uri)
        return resp

    def multi_ack(self, site_id, alarm_ids=[], note=""):
        """
        Acknowledge multiple site alarms.
        Parameters:
            site_id: String
            alarm_id: Array (array of String with the id of the alarms to ack)
            note: String (optional)
        """
        uri = "/api/v1/sites/{0}/alarms/ack".format(site_id)
        body = {"alarm_ids": alarm_ids, "note": note}
        resp = self._session.mist_post(uri, body=body)
        return resp

    def multi_unack(self, site_id, alarm_ids=[]):
        """
        Un-acknowledge multiple site alarms.
        Parameters:
            site_id: String
            alarm_id: Array (array of String with the id of the alarms to unack)
        """
        uri = "/api/v1/sites/{0}/alarms/unack".format(site_id)
        body = {"alarm_ids": alarm_ids}
        resp = self._session.mist_post(uri, body=body)
        return resp

    def ack_all(self, site_id, note=""):
        """
        Acknowledge all the site alarms.
        Parameters:
            site_id: String
            note: String (optional)
        """
        uri = "/api/v1/sites/{0}/alarms/ack".format(site_id)        
        body={"note": note}
        resp = self._session.mist_post(uri, body=body)
        return resp

    def unack_all(self, site_id):
        """
        Un-acknowledge all the site alarms.
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/{0}/alarms/unack".format(site_id)        
        resp = self._session.mist_post(uri)
        return resp

    def get(self, site_id, query={}, page=1, limit=100):
        """
        Get the list of the site alarms
        Parameters:
            site_id: String
            query: Dict (dict of search filters)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/alarms/search".format(site_id)
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count(self, site_id):
        """
        Count the number of alarms
        Parameters:
            site_id: String            
        """
        uri = "/api/v1/sites/{0}/alarms/count".format(site_id)
        resp = self._session.mist_get(uri)
        return resp


