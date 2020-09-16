from mistsystems.models.mist_obj import MistModel
import logging


class OrgModel(MistModel):

    def __init__(self):
        self.json = {}
        self._fields = [
            "id",
            "created_time",
            "modified_time",
            "name",
            "orggroup_ids",
            "msp_id",
            "msp_name",
            "allow_mist",
            "session_expiry",
            "alarmtemplate_id"
        ]

    def get_orgroup_ids(self):
        return self.json["orggroup_ids"]

    def set_orggroup_ids(self, orggroup_ids=[]):
        self.json["orggroup_ids"] = orggroup_ids

    def add_orggroup_ids(self, orggroup_ids=[]):
        for entry in orggroup_ids:
            if not entry in self.json["orggroup_ids"]:
                self.json["orggroup_ids"].append(entry)

    def del_orggroup_ids(self, orggroup_ids=[]):
        for entry in orggroup_ids:
            try:
                index = self.json["orggroup_ids"].index[entry]
                if index:
                    self.json["orggroup_ids"].pop(index)
            except:
                logging.warn("orggroup_id {0} no found".format(entry))

    def get_name(self):
        return self.json["name"]

    def set_name(self, name):
        self.json["name"] = name

    def get_msp_id(self):
        return self.json["msp_id"]

    def _set_msp_id(self, msp_id):
        self.json["msp_id"] = msp_id

    def get_msp_nale(self):
        return self.json["msp_name"]

    def _set_msp_name(self, msp_name):
        self.json["msp_name"] = msp_name

    def get_allow_mist(self):
        return self.json["allow_mist"]

    def set_allow_mist(self, allow_mist=True):
        self.json["allow_mist"] = allow_mist

    def get_session_expiry(self):
        return self.json["session_expiry"]

    def set_session_expiry(self, session_expiry=1440):
        self.json["session_expiry"]= 1440

    def get_alarmtemplate_id(self):
        return self.json["alarmtemplate_id"]

    def set_alarmtemplate_id(self, alarmtemplate_id):
        self.json["alarmtemplate_id"] = alarmtemplate_id



   