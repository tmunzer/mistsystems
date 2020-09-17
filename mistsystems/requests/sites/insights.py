class Insights():

    def __init__(self, session):
        self._session = session

    def stats(self, site_id, start, end, metrics, page=1, limit=100):
        uri = "/api/v1/sites/%s/insights/stats" % site_id
        query = {"start": start, "end": end, "metrics": metrics}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def client(self, site_id, client_mac, start, end, interval, metrics, page=1, limit=100):
        uri = "/api/v1/sites/%s/insights/client/%s/stats" % (
            site_id, client_mac)
        query = {"start": start, "end": end,
                 "interval": interval, "metrics": metrics}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def metrics(self, site_id, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/insights/{1}".format(
            site_id, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def device_metrics(self, site_id, device_id, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/insights/ap/{1}/{2}".format(
            site_id, device_id, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def client_metrics(self, site_id, client_mac, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/insights/client/{1}/{2}".format(
            site_id, client_mac, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp


    def anomaly_metrics(self, site_id, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/insights/anomaly/{1}".format(
            site_id, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def device_anomaly_metrics(self, site_id, device_id, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/anomaly/ap/{1}/{2}".format(
            site_id, device_id, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def client_anomaly_metrics(self, site_id, client_mac, metric, start=None, end=None, interval=None, page=1, limit=100):
        uri = "/api/v1/sites/{0}/anomaly/client/{1}/{2}".format(
            site_id, client_mac, metric)
        query = {"start": start, "end": end,
                 "interval": interval}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp