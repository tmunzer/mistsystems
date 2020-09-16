from mistsystems.models.orgs.admins import AdminModel

class Admins(AdminModel):
    def __init__(self, session, org_id):
        self._session = session
        self._org_id = org_id

    def save(self):
        obj = self.json
        obj_id = self.get_id()

        if obj_id:
            print("updating {0} at {1}".format(obj, obj_id))
        else:
            print("creating {0}".format(obj))

    def get(self):
        site_json = self._session.orgs.admins.get(org_id=self._org_id)["result"]
        self.set_json(site_json)
        return self

    def revoke(self):
        self._session.orgs.admins.revoke(self._org_id, self._get_attribute("admin_id"))

    def search(self, first_name=""):
        sites = []
        data = self._session.orgs.sites.get(org_id=self._org_id)["result"]

        for site_json in data:
            self.set_json(site_json)
            sites.append(self)
        return sites
