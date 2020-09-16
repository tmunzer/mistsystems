class Site():

    def __init__(self, session):
        self.session = session

    def get(self, site_id):
        uri = "/api/v1/sites/{0}".format(site_id)
        resp = self.session.mist_get(uri)
        return resp

    def get_stats(self, site_id):
        uri = "/api/v1/sites/{0}/stats".format(site_id)
        resp = self.session.mist_get(uri)
        return resp

    def get_settings(self, site_id):
        uri = "/api/v1/sites/{0}/setting".format(site_id)
        resp = self.session.mist_get(uri)
        return resp

    def get_license_usage(self, site_id):
        uri = "/api/v1/sites/{0}/licenses/usages".format(site_id)
        resp = self.session.mist_get(uri)
        return resp

    def update(self, site_id, site_settings):
        uri = "/api/v1/sites/{0}/setting".format(site_id)
        resp = self.session.mist_put(uri, site_settings)
        return resp

    def search_system_events(self, site_id, query={}, page=1, limit=100):
        uri = "/api/v1/sites/{0}/events/system/search".format(site_id)
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def count_system_events(self, site_id, query={}):
        uri = "/api/v1/sites/{0}/events/system/count".format(site_id)
        resp = self.session.mist_get(uri, query=query)
        return resp

    def delete(self, site_id):
        uri = "/api/v1/sites/{0}".format(site_id)
        resp = self.session.mist_delete(uri)
        return resp

    def create_blocklist(self, site_id, macs=[]):
        uri = "/api/v1/sites/{0}/blacklist".format(site_id)
        body = {"macs": macs}
        resp = self.session.mist_post(uri, body=body)
        return resp

    def delete_blocklist(self, site_id):
        uri = "/api/v1/sites/{0}/blacklist".format(site_id)
        resp = self.session.mist_delete(uri)
        return resp

    def create_allowlist(self, site_id, macs=[]):
        uri = "/api/v1/sites/{0}/whitelist".format(site_id)
        body = {"macs": macs}
        resp = self.session.mist_post(uri, body=body)
        return resp

    def delete_allowlist(self, site_id):
        uri = "/api/v1/sites/{0}/whitelist".format(site_id)
        resp = self.session.mist_delete(uri)
        return resp

    def create_watched_station_list(self, site_id, macs=[]):
        uri = "/api/v1/sites/{0}/watched_station".format(site_id)
        body = {"macs": macs}
        resp = self.session.mist_post(uri, body=body)
        return resp

    def delete_watched_station_list(self, site_id):
        uri = "/api/v1/sites/{0}/watched_station".format(site_id)
        resp = self.session.mist_delete(uri)
        return resp

    def get_uisettings(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/{0}/uisettings".format(site_id)
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_uisettings_derived(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/{0}/uisettings/derived".format(site_id)
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_uisettings_by_id(self, site_id, uisetting_id):
        uri = "/api/v1/sites/{0}/uisettings/{1}".format(site_id, uisetting_id)
        resp = self.session.mist_get(uri)
        return resp

    def create_uisettings(self, site_id, uisettings):
        uri = "/api/v1/sites/{0}/uisettings".format(site_id)
        resp = self.session.mist_post(uri, body=uisettings)
        return resp

    def update_uisettings(self, site_id, uisettings):
        uri = "/api/v1/sites/{0}/uisettings".format(site_id)
        resp = self.session.mist_put(uri, body=uisettings)
        return resp

    def delete_uisettings(self, site_id, uisetting_id):
        uri = "/api/v1/sites/{0}/uisettings/{1}".format(site_id, uisetting_id)
        resp = self.session.mist_delete(uri)
        return resp
