from tabulate import tabulate

class MistModel():

    def __init__(self):
        self._fields = []
        self.json = {}

    # def __str__(self):
    #     return "{0}".format(self.json)
    def __str__(self):
        columns_headers = self._fields
        table = []
        temp = []
        for field in columns_headers:
            if hasattr(self.json, field):
                temp.append(str(getattr(self.json, field)))
            else:
                temp.append("")
        table.append(temp)
        return tabulate(table, columns_headers)

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

    def from_json(self, data):
        self.json = data