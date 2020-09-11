class Wlans():

    def __init__(self, session):
        self.session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/wlans" % org_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def create(self, org_id, wlan_settings):
        uri = "/api/v1/orgs/%s/wlans" % org_id
        resp = self.session.mist_post(uri, body=wlan_settings)
        return resp

    def delete(self, org_id, wlan_id):
        uri = "/api/v1/orgs/%s/wlans/%s" % (org_id, wlan_id)
        resp = self.session.mist_delete(uri)
        return resp

    def add_portal_image(self, org_id, wlan_id, image_path):
        uri = "/api/v1/orgs/%s/wlans/%s/portal_image" % (org_id, wlan_id)
        files = {'file': open(image_path, 'rb').read()}
        resp = self.session.mist_post_file(uri, files=files)
        return resp

    def delete_portal_image(self, org_id, wlan_id):
        uri = "/api/v1/orgs/%s/wlans/%s/portal_image" % (org_id, wlan_id)
        resp = self.session.mist_delete(uri)
        return resp

    def set_portal_template(self, org_id, wlan_id, portal_template_body):
        uri = "/api/v1/orgs/%s/wlans/%s/portal_template" % (org_id, wlan_id)
        body = portal_template_body
        resp = self.session.mist_put(uri, body=body)
        return resp