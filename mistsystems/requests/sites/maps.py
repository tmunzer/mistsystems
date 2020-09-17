class Maps():

    def __init__(self, session):
        self._session = session

    def get(self, site_id, page=1, limit=100):
        """
        Get list of maps
        Parameters:
            site_id: String
            page: Int
            limit: Int
        """
        uri = "/api/v1/sites/%s/maps" % site_id
        resp = self._session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(self, site_id, map_id):
        """
        Get map information
        Parameters:
            site_id: String
            map_id: String
        """
        uri = "/api/v1/sites/{0}/maps/{1}".format(site_id, map_id)
        resp = self._session.mist_get(uri)
        return resp

    def delete(self, site_id, map_id):
        """
        Delete a map
        Parameters:
            site_id: String
            map_id: String
        """
        uri = "/api/v1/sites/%s/maps/%s" % (site_id, map_id)
        resp = self._session.mist_delete(uri)
        return resp

    def create(self, site_id, map_settings):
        """
        Create a map
        Parameters:
            site_id: String
            map_settings: Dict
        """
        uri = "/api/v1/sites/%s/maps" % site_id
        body = map_settings
        resp = self._session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, map_id, map_settings):
        """
        Update a map
        Parameters:
            site_id: String
            map_id: String
            map_settings: Dict
        """
        uri = "/api/v1/sites/{0}/maps/{1}".format(site_id, map_id)
        body = map_settings
        resp = self._session.mist_put(uri, body=body)
        return resp

    def add_image(self, site_id, map_id, image_path):
        """
        Upload an image to a map
        Parameters:
            site_id: String
            map_id: String
            image_path: String
        """
        uri = "/api/v1/sites/%s/maps/%s/image" % (site_id, map_id)
        files = {'file': open(image_path, 'rb').read()}
        resp = self._session.mist_post_file(uri, files=files)
        return resp

    def delete_image(self, site_id, map_id):
        """
        Delete a map image
        Parameters:
            site_id: String
            map_id: String
        """
        uri = "/api/v1/sites/%s/maps/%s/image" % (site_id, map_id)
        resp = self._session.mist_delete(uri)
        return resp

    def replace_image(self, site_id, map_id, image_path, image_settings):
        """
        Delete a map image
        Parameters:
            site_id: String
            map_id: String
            image_path: String
            image_settings: Dict
                transform: object: The name of the map, optional
                x: float: where the (0, 0) of the new image is relative to the original map, default is 0
                y: float: where the (0, 0) of the new image is relative to the original map, default is 0
                scale: float: whether to scale the replacing image, default is 1
                rotation: int: whether to rotate the replacing image, default is 0, in degrees
        """
        uri = "/api/v1/sites/%s/maps/%s/replace" % (site_id, map_id)
        resp = self._session.mist_post(uri, body=image_settings, files=image_path)
        return resp
