class Devices():

    def __init__(self, session):
        self._session = session
        self.virtual_chassis = VirtualChassis(self._session)

    def get(self, site_id, name=None, device_type=None, page=1, limit=100):
        """
        get a list of devices
        Parameters:
            site_id: String
            name: optional, device name
            device_type: optional (ap, switch, gateway, all. Default: ap)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices".format(site_id)
        query = {}
        if name:
            query[name] = name
        if device_type:
            query["type"] = device_type
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_available_versions(self, site_id, page=1, limit=100):
        """
        get a list of devices firmwares
        Parameters:
            site_id: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices/versions".format(site_id)
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_config(self, site_id, device_id):
        """
        Get device details
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}".format(site_id, device_id)
        resp = self._session.mist_get(uri)
        return resp

    def get_stats(self, site_id, device_type=None, page=1, limit=100):
        """
        Get stats of the site devices
        Parameters:
            site_id: String
            name: optional, device name
            device_type: optional (ap, switch, gateway, all. Default: ap)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/stats/devices".format(site_id)
        query = {}
        if device_type:
            query["type"] = device_type
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_stats_by_id(self, site_id, device_id):
        """
        Get stats of the site devices
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/stats/devices/{1}".format(site_id, device_id)
        resp = self._session.mist_get(uri)
        return resp

    def create(self, site_id, device_settings):
        """
        Create a new device
        Parameters:
            site_id: String
            device_settings: Dict (please see API documentation)
        """
        uri = "/api/v1/sites/{0}/devices".format(site_id)
        resp = self._session.mist_post(uri, body=device_settings)
        return resp

    def update(self, site_id, device_id, device_settings):
        """
        Update a  device configuration
        Parameters:
            site_id: String
            device_id: Strong
            device_settings: Dict (please see API documentation)
        """
        uri = "/api/v1/sites/{0}/devices/{1}".format(site_id, device_id)
        resp = self._session.mist_put(uri, body=device_settings)
        return resp

    def upload_support_file(self, site_id, device_id):
        """
        Upload device data to Mist support
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/support".format(
            site_id, device_id)
        resp = self._session.mist_post(uri)
        return resp

    def upgrade_device(self, site_id, device_id, version):
        """
        Upgrade a device to a specified version
        Parameters:
            site_id: String
            device_id: String
            version: String
        """
        body = {"version": version}
        uri = "/api/v1/sites/{0}/devices/{1}/upgrade".format(
            site_id, device_id)
        resp = self._session.mist_post(uri, body=body)
        return resp

    def upgrade_multiple_devices(self, site_id, version, device_ids=None, models=None, enable_p2p=False):
        """
        Upgrade a device to a specified version
        Parameters:
            site_id: String
            version: String
            device_id: Array
            models: Array (if device_ids not provided)
            enable_p2p: Boolean
        """
        body = {"version": version}
        if device_ids:
            body["device_ids"] = device_ids
        if models:
            body["models"] = models
        if enable_p2p:
            body["enable_p2p"] = enable_p2p
        uri = "/api/v1/sites/{0}/devices/upgrade".format(site_id)
        resp = self._session.mist_post(uri, body=body)
        return resp

    def reprovision_all_aps(self, site_id):
        """
        To force all APs to reprovision itself again.
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/{0}/devices/reprovision".format(site_id)
        resp = self._session.mist_post(uri)
        return resp

    def zeroise_fips_all_aps(self, site_id):
        """
        Zeroize all FIPS APs in the Site
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/{0}/devices/zerioze".format(site_id)
        resp = self._session.mist_post(uri)
        return resp

    def delete(self, site_id, device_id):
        """
        Delete a  device
        Parameters:
            site_id: String
            device_id: Strong
        """
        uri = "/api/v1/sites/{0}/devices/{1}".format(site_id, device_id)
        resp = self._session.mist_delete(uri)
        return resp

    def add_image(self, site_id, device_id, image_name, image_path):
        """
        Upload device image
        Parameters:
            site_id: String
            device_id: String
            image_name: String
            image_path: String (path to the image)
        """
        uri = "/api/v1/sites/{0}/devices/{1}/image/{2}".format(
            site_id, device_id, image_name)
        files = {'file': open(image_path, 'rb').read()}
        resp = self._session.mist_post_file(uri, files=files)
        return resp

    def delete_image(self, site_id, device_id, image_name):
        """
        Delete device image
        Parameters:
            site_id: String
            device_id: String
            image_name: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/image/{2}".format(
            site_id, device_id, image_name)
        resp = self._session.mist_delete(uri)
        return resp

    def locate_start(self, site_id, device_id):
        """
        for AP ONLY
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/locate".format(
            site_id, device_id)
        resp = self._session.mist_post(uri)
        return resp

    def locate_stop(self, site_id, device_id):
        """
        for AP ONLY
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/unlocate".format(
            site_id, device_id)
        resp = self._session.mist_post(uri)
        return resp

    def restart(self, site_id, device_id):
        """
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/restart".format(
            site_id, device_id)
        resp = self._session.mist_post(uri)
        return resp

    def restart_multiple(self, site_id, device_ids=[]):
        """
        Parameters:
            site_id: String
            device_ids: Array
        """
        body = {"device_ids": device_ids}
        uri = "/api/v1/sites/{0}/devices/restart".format(
            site_id)
        resp = self._session.mist_post(uri, body)
        return resp

    def search(self, site_id, search={}, page=1, limit=100):
        """
        search devices
        Parameters:
            site_id: String
            seach: Dict
                hostname: String
                model: String
                mac: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices/search".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def search_config_history(self, site_id, search={}, page=1, limit=100):
        """
        Search a device config history
        Parameters:
            site_id: String
            search: Dict
                ap: String, option (ap_mac)
                start: Int
                end: Int
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices/config_history/search".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def search_config_last(self, site_id, search={}, page=1, limit=100):
        """
        Search a device config history
        Parameters:
            site_id: String
            search: Dict
                ap: String, option (ap_mac)
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices/last_config/search".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def search_events(self, site_id, search={}, page=1, limit=100):
        """
        search devices events
        Parameters:
            site_id: String
            seach: Dict
                hostname: String
                model: String
                mac: String
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "/api/v1/sites/{0}/devices/events/search".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count(self, site_id, search={}, page=1, limit=100):
        """
        count number of devices events
        Parameters:
            site_id: String
            search: Dict
                distinct: String, optional (type)
                start: Int, optional
                end: Int, optional
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "api/v1/sites/{0}/devices/count".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_events(self, site_id, search={}, page=1, limit=100):
        """
        count number of devices events
        Parameters:
            site_id: String
            search: Dict
                distinct: String, optional (type)
                start: Int, optional
                end: Int, optional
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "api/v1/sites/{0}/devices/events/count".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_config_history(self, site_id, search={}, page=1, limit=100):
        """
        count number of devices configs
        Parameters:
            site_id: String
            search: Dict
                distinct: String, optional (type)
                start: Int, optional
                end: Int, optional
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "api/v1/sites/{0}/devices/config_history/count".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def count_config_last(self, site_id, search={}, page=1, limit=100):
        """
        count number of devices configs
        Parameters:
            site_id: String
            search: Dict
                distinct: String, optional (type)
                start: Int, optional
                end: Int, optional
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "api/v1/sites/{0}/devices/last_config/count".format(site_id)
        resp = self._session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def get_radio_channels(self, site_id, country_code=None, page=1, limit=100):
        """
        list devices radio channels
        Paramters:
            site_id: String
            country_code: String, optional
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri = "api/v1/sites/{0}/devices/ap_channels".format(site_id)
        query = {"country_code": country_code} if country_code else {}
        resp = self._session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_device_config_cmd(self, site_id, device_id):
        """
        SWITCHES ONLY
        get a device configuration commands
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/config_cmd".format(
            site_id, device_id)
        resp = self._session.mist_get(uri)
        return resp

    def set_iot_port(self, site_id, device_id, iot_settings):
        """
        For each IoT pin referenced:
        - The pin must be enabled using the Device ‘iot_config’ API
        - The pin must support the output direction
        Parameters:
            site_id: String
            device_id: String
            iot_settings: Dict (e.g. {"DO": 0, "A1": 1})
        """
        uri = "/api/v1/sites/{0}/devices/{1}/iot".format(
            site_id, device_id)
        resp = self._session.mist_put(uri, iot_settings)
        return resp

    def get_iot_port(self, site_id, device_id):
        """
        Returns the current state of each enabled IoT pin configured as an output.
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/iot".format(
            site_id, device_id)
        resp = self._session.mist_get(uri)
        return resp

    def export_information(self, site_id):
        """
        Download the exported device information
        Parameters:
            site_id: String
        """
        uri = "/api/v1/sites/{0}/devices/export".format(site_id)
        resp = self._session.mist_get(uri)
        return resp


class VirtualChassis():
    def __init__(self, session):
        self._session = session

    def create(self, site_id, device_id, members):
        """
        Create a new Virtual Chassis
        Parameters:
            site_id: String
            device_id: String
            members: Array of Dict
                mac: String (switch mac address)
                memmber: Int (optional, member number)
                cv_ports: Array of Strings (optional, for EX without VC ports)
        """
        body = {"members": members}
        uri = "/api/v1/sites/{0}/devices/{1}/vc".format(site_id, device_id)
        resp = self._session.mist_post(uri, body=body)
        return resp

    def add_member(self, site_id, device_id, members):
        """
        Add members to existing VC
        Parameters:
            site_id: String
            device_id: String
            members: Array of Dict
                mac: String (switch mac address of the members to add)
                memmber: Int (optional, member number)
                cv_ports: Array of Strings (optional, for EX without VC ports)
        """
        body = {
            "op": "add",
            "members": members
        }
        uri = "/api/v1/sites/{0}/devices/{1}/vc".format(site_id, device_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def remove_member(self, site_id, device_id, member_ids):
        """
        Remove members to existing VC
        Parameters:
            site_id: String
            device_id: String
            member_ids: Int (id of the members to remove from the VC)
        """
        body = {
            "op": "add",
            "members": []
        }
        for member_id in member_ids:
            body["members"].append({"member": member_id})
        uri = "/api/v1/sites/{0}/devices/{1}/vc".format(site_id, device_id)
        resp = self._session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, device_id):
        """
        Delete a Virtual Chassis
        Parameters:
            site_id: String
            device_id: String
        """
        uri = "/api/v1/sites/{0}/devices/{1}/vc".format(site_id, device_id)
        resp = self._session.mist_delete(uri)
        return resp
