from mistsystems.models.common.mist_obj import MistModel


class AdminModel(MistModel):

    def __init__(self):
        self.json = {}
        self._fields = [
            "admin_id",
            "email",
            "first_name",
            "last_name",
            "hours",
            "privileges"
        ]

    def get_admin_id(self):
        return self._get_attribute("admin_id")

    def _set_admin_id(self, admin_id):
        self.json["admin_id"] = admin_id

    def get_email(self):
        return self._get_attribute("email")

    def set_email(self, email=""):
        self.json["email"] = email

    def get_first_name(self):
        return self._get_attribute("first_name")

    def set_first_name(self, first_name):
        self.json["first_name"] = first_name

    def get_last_name(self):
        return self._get_attribute("last_name")

    def set_last_name(self, last_name):
        self.json["last_name"] = last_name

    def get_hours(self):
        return self._get_attribute("hours")

    def set_hours(self, hours):
        self.json["hours"] = hours
