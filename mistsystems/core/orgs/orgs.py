from mistsystems.models.orgs.orgs import OrgModel
from mistsystems.core import orgs
from mistsystems.core.sites.sites import Sites


class Orgs(OrgModel):
    def __init__(self, session):
        OrgModel.__init__(self)
        self._session = session

        self.admin = None
        self.alarms = None
        # self.alarmtemplates = orgs.alarmtemplates.AlarmTemplates(session)
        # self.assetfilters = orgs.assetfilters.AssetFilters(session)
        # self.audit_logs = orgs.audit_logs.AuditLogs(session)
        # self.certificates = orgs.certificates.Certificates(session)
        # self.clients = {
        #     "wireless": orgs.clients.Wireless(session)
        # }
        # self.devices = orgs.devices.Devices(session)
        # self.deviceprofiles = orgs.deviceprofiles.DeviceProfiles(session)
        # self.inventory = orgs.inventory.Inventory(session)
        # self.juniper = orgs.juniper.Juniper(session)
        # self.licenses = orgs.licenses.Licenses(session)
        # self.maps = orgs.maps.Maps(session)
        # self.mxclusters = orgs.mxclusters.MxClusters(session)
        # self.mxedges = orgs.mxedges.MxEdges(session)
        # self.mxtunnels = orgs.mxtunnels.MxTunnels(session)
        # self.networktemplates = orgs.networktemplates.NetworkTemplates(session)
        # self.orgs = orgs.orgs.Orgs(session)
        # self.pcap_bucket = orgs.pcap_bucket.PcapBucket(session)
        # self.psks = orgs.psks.Psks(session)
        # self.rftemplates = orgs.rftemplates.RfTemplates(session)
        # self.secpolicies = orgs.secpolicies.SecPolicies(session)
        # self.sitegroups = orgs.sitegroups.SiteGroups(session)
        self.sites = None
        # self.ssoroles = orgs.ssoroles.SsoRoles(session)
        # self.ssos = orgs.ssos.Ssos(session)
        # self.subscriptions = orgs.subscriptions.Subscriptions(session)
        # self.templates = orgs.templates.Templates(session)
        # self.tickets = orgs.tickets.Tickets(session)
        # self.webhooks = orgs.webhooks.Webhooks(session)
        # self.wlans = orgs.wlans.Wlans(session)
        # self.wxrules = orgs.wxrules.WxRules(session)
        # self.wxtags = orgs.wxtags.WxTags(session)
        # self.wxtunnels = orgs.wxtunnels.WxTunnels(session)

    def get_by_id(self, org_id):
        json = self._session.orgs.orgs.get_by_id(org_id=org_id)["result"]
        self.set_json(json)
        self.admins = orgs.admins.Admins(self._session, org_id)
        self.alarms = orgs.alarms.Alarms(self._session, org_id)
        self.sites = Sites(self._session, org_id)
        return self

    def save(self):
        obj = self.json
        obj_id = self.get_id()

        if obj_id:
            print("updating {0} at {1}".format(obj, obj_id))
        else:
            print("creating {0}".format(obj))
