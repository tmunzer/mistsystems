class Rrm():

    def __init__(self, session):
        self._session = session

    def get_current_channel_planning(self, site_id):
        uri = "/api/v1/sites/%s/rrm/current" % site_id
        resp = self._session.mist_get(uri)
        return resp

    def get_device_rrm_info(self, site_id, device_id, band):
        uri = "/api/v1/sites/%s/rrm/current/devices/%s/band/%s" % (
            site_id, device_id, band)
        resp = self._session.mist_get(uri)
        return resp

    def optimize(self, site_id, band_24=False, band_5=False):
        bands = []
        if band_24:
            bands.append("24")
        if band_5:
            bands.append("5")
        body = {"bands": bands}
        uri = "/api/v1/sites/%s/rrm/optimize" % site_id
        resp = self._session.mist_post(uri, body=body)
        return resp

    def reset(self, site_id):
        uri = "/api/v1/sites/%s/devices/reset_radio_config" % site_id
        resp = self._session.mist_post(uri)
        return resp

    def get_events(self, site_id, band, duration="", page=1, limit=100):
        uri = "/api/v1/sites/%s/rrm/events?band=%s" % (site_id, band)
        query = {"band": band}
        if duration != "":
            query["duration"] = duration
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_interference_events(self, site_id, duration="", page=1, limit=100):
        uri = "/api/v1/sites/%s/events/interference" % site_id
        query = {}
        if duration != "":
            query["duration"] = duration
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_roaming_events(self, site_id, mtype, start="", end="", page=1, limit=100):
        uri = "/api/v1/sites/%s/events/fast_roam" % site_id
        query = {"type": mtype}
        if end != "":
            query["duration"] = end
        if limit != "":
            query["duration"] = limit
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp
