from mistsystems.requests import orgs, sites, const

class Const():
    def __init__(self, session):
        self.const = const.const.Const(session)

class Orgs():
    def __init__(self, session):
        self.admin = orgs.admins.Admins(session)
        self.alarms = orgs.alarms.Alarms(session)
        self.alarmtemplates = orgs.alarmtemplates.AlarmTemplates(session)
        self.apitokens = orgs.apitokens.Apitokens(session)
        self.assetfilters = orgs.assetfilters.AssetFilters(session)
        self.audit_logs = orgs.audit_logs.AuditLogs(session)
        self.certificates = orgs.certificates.Certificates(session)
        self.clients = {
            "wireless": orgs.clients.Wireless(session)
        }
        self.devices = orgs.devices.Devices(session)
        self.deviceprofiles = orgs.deviceprofiles.DeviceProfiles(session)
        self.inventory = orgs.inventory.Inventory(session)
        self.juniper = orgs.juniper.Juniper(session)
        self.licenses = orgs.licenses.Licenses(session)
        self.maps = orgs.maps.Maps(session)
        self.mxclusters = orgs.mxclusters.MxClusters(session)
        self.mxedges = orgs.mxedges.MxEdges(session)
        self.mxtunnels = orgs.mxtunnels.MxTunnels(session)
        self.networktemplates = orgs.networktemplates.NetworkTemplates(session)
        self.orgs = orgs.orgs.Orgs(session)
        self.pcap_bucket = orgs.pcap_bucket.PcapBucket(session)
        self.psks = orgs.psks.Psks(session)
        self.rftemplates = orgs.rftemplates.RfTemplates(session)
        self.secpolicies = orgs.secpolicies.SecPolicies(session)
        self.sitegroups = orgs.sitegroups.SiteGroups(session)
        self.sites = orgs.sites.Sites(session)
        self.ssoroles = orgs.ssoroles.SsoRoles(session)
        self.ssos = orgs.ssos.Ssos(session)
        self.subscriptions = orgs.subscriptions.Subscriptions(session)
        self.templates = orgs.templates.Templates(session)
        self.tickets = orgs.tickets.Tickets(session)
        self.webhooks = orgs.webhooks.Webhooks(session)
        self.wlans = orgs.wlans.Wlans(session)
        self.wxrules = orgs.wxrules.WxRules(session)
        self.wxtags = orgs.wxtags.WxTags(session)
        self.wxtunnels = orgs.wxtunnels.WxTunnels(session)


class Sites():
    def __init__(self, session):
        self.alarms = sites.alarms.Alarms(session)
        self.assetfilters = sites.assetfilters.AssetFilters(session)
        self.assets = sites.assets.Assets(session)
        self.beacons = sites.beacons.Beacons(session)
        self.clients = {
            "wireless": sites.clients.Wireless(session),
            "wired": sites.clients.Wired(session),
            "stats": sites.clients.Stats(session)
        }
        self.devices = sites.devices.Devices(session)
        self.guests = sites.guests.Guests(session)
        self.insights = sites.insights.Insights(session)
        self.location = sites.location.Location(session)
        self.machine_learning = sites.machine_learning.MachineLearning(session)
        self.maps = sites.maps.Maps(session)
        self.mxedges = sites.mxedges.MxEdges(session)
        self.packet_captures = sites.packet_captures.PacketCaptures(session)
        self.psks = sites.psks.Psks(session)
        self.rogues = sites.rogues.Rogues(session)
        self.rrm = sites.rrm.Rrm(session)
        self.rssizones = sites.rssizones.RssiZones(session)
        self.settings = sites.settings.Settings(session)
        self.site = sites.site.Site(session)
        self.skyatp = sites.skyatp.SkyAtp(session)
        self.stats = sites.stats.Stats(session)
        self.subscriptions = sites.subscriptions.Subscriptions(session)
        self.system_events = sites.system_events.SystemEvents(session)
        self.vbeacons = sites.vbeacons.VBeacons(session)
        self.webhooks = sites.webhooks.Webhooks(session)
        self.wlans = sites.wlans.Wlans(session)
        self.wxrules = sites.wxrules.WxRules(session)
        self.wxtags = sites.wxtags.WxTags(session)
        self.wxtunnels = sites.wxtunnels.WxTunnels(session)
        self.zones = sites.zones.Zones(session)
