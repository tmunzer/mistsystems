class Const():

    def __init__(self, session):
        self._session = session

    def get_applications(self):
        uri = "/api/v1/const/applications"
        resp = self._session.mist_get(uri)
        return resp

    def get_ap_led_status(self):
        uri = "/api/v1/const/ap_led_status"
        resp = self._session.mist_get(uri)
        return resp

    def get_ap_models(self):
        uri = "/api/v1/const/device_models"
        resp = self._session.mist_get(uri)
        return resp

    def get_ap_channels(self, country_code):
        uri = "/api/v1/const/ap_channels"
        query = {"country_code": country_code}
        resp = self._session.mist_get(uri=uri, query=query)
        return resp

    def get_client_events(self):
        uri = "/api/v1/const/client_events"
        resp = self._session.mist_get(uri)
        return resp

    def get_country_codes(self):
        uri = "/api/v1/const/countries"
        resp = self._session.mist_get(uri)
        return resp

    def get_system_events(self):
        uri = "/api/v1/const/system_events"
        resp = self._session.mist_get(uri)
        return resp

    def get_insights(self):
        uri = "/api/v1/const/insight_metrics"
        resp = self._session.mist_get(uri)
        return resp
