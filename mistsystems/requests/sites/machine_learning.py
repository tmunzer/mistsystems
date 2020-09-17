class MachineLearning():

    def __init__(self, session):
        self._session = session

    def reset(self, site_id, map_id):
        uri = "/api/v1/sites/%s/location/ml/reset/map/%s" % (site_id, map_id)
        resp = self._session.mist_post(uri)
        return resp
