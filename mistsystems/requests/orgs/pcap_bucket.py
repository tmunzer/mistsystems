class PcapBucket():
    def __init__(self, session):
        self._session = session

    def set_bucket(self, org_id, bucket):
        uri = "/api/v1/orgs/{0}/setting/pcap_bucket/setup".format(org_id)
        body = {"bucket": bucket}
        resp = self._session.mist_post(uri, body= body)
        return resp

    def verify_bucket(self, org_id, bucket, verify_token):
        """
        NOTE: If successful, a “VERIFIED” file will be created in the bucket
        """
        uri = "/api/v1/orgs/{0}/setting/pcap_bucket/verify".format(org_id)
        body = {"bucket": bucket, "verify_token": verify_token}
        resp = self._session.mist_post(uri, body= body)
        return resp
