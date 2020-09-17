class AlarmTemplates():

    def __init__(self, session):
        self._session = session

    def create(self, org_id, alarmtemplate_settings):
        uri = "/api/v1/orgs/%s/alarmtemplates" % org_id
        body = alarmtemplate_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, alarmtemplate_settings, body={}):
        uri = "/api/v1/orgs/%s/alarmtemplates/%s" % (
            org_id, alarmtemplate_settings)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, alarmtemplate_settings):
        uri = "/api/v1/orgs/%s/alarmtemplates/%s" % (
            org_id, alarmtemplate_settings)
        resp = self._session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/alarmtemplates" % org_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, org_id, alarmtemplate_id):
        uri = "/api/v1/orgs/%s/alarmtemplates/%s" % (org_id, alarmtemplate_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_alarm_template_rules(self, org_id, alarmtemplate_id):
        uri = "/api/v1/orgs/{0}/alarmtemplates/{1}/alarmrules".format(org_id, alarmtemplate_id)
        resp = self._session.mist_get(uri)
        return resp

    def suppress(self, org_id, duration, sitegroup_ids=None, site_ids=None):
        """
        In certain situations, for example, scheduled maintanance, you may want to suspend alarms to be triggered for a period of time.
        Parameters:
            org_id: String
            duration: int (duration, in seconds. Deafult is 60. Maximum allowed duration is 1 day (86400).)
            sitegroup_ids: Array
            site_ids: Array
        """
        uri = "/api/v1/orgs/{0}/alarmtemplates/suppress".format(org_id)
        body = {
            "duration": duration, 
            "applies": {"org_id": org_id}
            }
        if sitegroup_ids: body["applies"]["sitegroup_ids"] = sitegroup_ids
        if site_ids: body["applies"]["site_ids"] = site_ids
        resp = self._session.mist_post(uri, body=body)
        return resp
