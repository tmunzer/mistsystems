from mistsystems.models.orgs.alarms import AlarmsModel

class Alarms(AlarmsModel):
    def __init__(self, session, org_id):
        self._session = session
        self._org_id = org_id


    def count(self, severity=None, alarm_type=None, group=None):
        query={}
        if severity:
            query["severity"]=severity
        if alarm_type:
            query["type"]=alarm_type
        if group:
            query["group"]=group
        data = self._session.orgs.alarms.count(org_id=self._org_id, query=query)["result"]
        return data


    def search(self, severity=None, alarm_type=None, group=None):
        query={}
        if severity:
            query["severity"]=severity
        if alarm_type:
            query["type"]=alarm_type
        if group:
            query["group"]=group
        data = self._session.orgs.alarms.search(org_id=self._org_id, query=query)["result"]
        return data
