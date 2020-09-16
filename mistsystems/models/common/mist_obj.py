from tabulate import tabulate


class MistModel():

    def __init__(self):
        self.json = {}

    # def __str__(self):
    #     return "{0}".format(self.json)
    def __str__(self):
        return "{0}".format(self.json)

    def _set_id(self, obj_id):
        self.json["id"] = obj_id

    def _set_created_time(self, created_time):
        self.json["created_time"] = created_time

    def _set_modified_time(self, modified_time):
        self.json["modified_time"] = modified_time

    def get_id(self):
        return self.json["id"]

    def get_created_time(self):
        return self.json["created_time"]

    def get_modified_time(self):
        return self.json["modified_time"]

    def get_json(self):
        return self.json

    def set_json(self, json):
        self.json = json

    def _get_attribute(self, attribute):
        if attribute in self.json:
            return self.json["attribute"]
        else:
            return None

    def _set_attribute(self, attribute, value):
        self.json[attribute] = value
