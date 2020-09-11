class PcapBucket():
    def __init__(self, session):
        self.session = session

    def set_bucket(self, org_id, bucket):
        uri = "/api/v1/orgs/{0}/setting/pcap_bucket/setup"
        body = {"bucket": bucket}
        resp = self.session.mist_port(uri, body= body)
        return resp

    def verify_bucket(self, org_id, bucket, verify_token):
        """
        NOTE: If successful, a “VERIFIED” file will be created in the bucket
        """
        uri = "/api/v1/orgs/{0}/setting/pcap_bucket/verify"
        body = {"bucket": bucket, "verify_token": verify_token}
        resp = self.session.mist_port(uri, body= body)
        return resp
