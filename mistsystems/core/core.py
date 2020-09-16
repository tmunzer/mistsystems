from mistsystems.core import sites, orgs


class Orgs():
    def __init__(self, api_session):
        self._api_session = api_session
        self.orgs = orgs.orgs.Orgs(self._api_session)
