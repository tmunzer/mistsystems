from mistsystems.models.orgs.orgs import OrgModel
from mistsystems.core.sites.sites import Sites


class Orgs(OrgModel):
    def __init__(self, session):
        OrgModel.__init__(self)
        self._session = session
        self.sites = None

    def get_by_id(self, org_id):
        json = self._session.orgs.orgs.get_by_id(org_id=org_id)["result"]
        self.from_json(json)
        self.sites = Sites(self._session, org_id)
        return self

    def save(self):
        obj = self.json
        obj_id = self.get_id()

        if obj_id:
            print("updating {0} at {1}".format(obj, obj_id))
        else:
            print("creating {0}".format(obj))
