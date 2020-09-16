from mistsystems.models.common.mist_obj import MistModel
import logging


class SiteModel(MistModel):
    def __init__(self):
        self.json = {}

    def get_org_id(self):
        return self._get_attribute("org_id")

    def _set_org_id(self, org_id):
        self.json["org_id"] = org_id

    def get_name(self):
        return self._get_attribute("name")

    def set_name(self, name):
        self.json["name"] = name

    def get_timezone(self):
        return self._get_attribute("timezone")

    def set_timezone(self, timezone):
        self.json["timezone"] = timezone

    def get_country_code(self):
        return self._get_attribute("country_code")

    def set_country_code(self, country_code):
        self.json["country_code"] = country_code

    def get_latlng(self):
        return self._get_attribute("latlng")

    def set_latlng(self, latlng):
        self.json["latlng"] = latlng

    def get_address(self):
        return self._get_attribute("address")

    def set_address(self, address):
        self.json["address"] = address

    def get_sitegroup_ids(self):
        return self._get_attribute("sitegroup_ids")

    def set_sitegroup_ids(self, sitegroup_ids=[]):
        self.json["sitegroup_ids"] = sitegroup_ids

    def add_sitegroup_ids(self, sitegroup_ids=[]):
        for entry in sitegroup_ids:
            if not entry in self.json["sitegroup_ids"]:
                self.json["sitegroup_ids"].append(entry)

    def del_sitegroup_ids(self, sitegroup_ids=[]):
        for entry in sitegroup_ids:
            try:
                index = self.json["sitegroup_ids"].index(entry)
                if index:
                    self.json["sitegroup_ids"].pop(index)
            except:
                logging.warn("sitegroup_id {0} no found".format(entry))

    def get_lat(self):
        return self._get_attribute("lat")

    def set_lat(self, lat):
        self.json["lat"] = lat

    def get_lng(self):
        return self._get_attribute("lng")

    def set_lng(self, lng):
        self.json["lng"] = lng

    def get_rftempalte_id(self):
        return self._get_attribute("rftempalte_id")

    def set_rftempalte_id(self, rftempalte_id):
        self.json["rftempalte_id"] = rftempalte_id

    def get_secpolicy_id(self):
        return self._get_attribute("secpolicy_id")

    def set_secpolicy_id(self, secpolicy_id):
        self.json["secpolicy_id"] = secpolicy_id

    def get_alarmtemplate_id(self):
        return self._get_attribute("alarmtemplate_id")

    def set_alarmtemplate_id(self, alarmtemplate_id):
        self.json["alarmtemplate_id"] = alarmtemplate_id

    def get_networktemplate_id(self):
        return self._get_attribute("networktemplate_id")

    def set_networktemplate_id(self, networktemplate_id):
        self.json["networktemplate_id"] = networktemplate_id

    def get_tzoffset(self):
        return self._get_attribute("tzoffset")

    def set_tzoffset(self, tzoffset):
        self.json["tzoffset"] = tzoffset

  
