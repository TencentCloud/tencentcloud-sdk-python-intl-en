# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccelerateType(AbstractModel):
    """Acceleration type

    """

    def __init__(self):
        r"""
        :param Switch: Acceleration switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclCondition(AbstractModel):
    """The condition that makes up an access control rule

    """

    def __init__(self):
        r"""
        :param MatchFrom: The field to match. Values:
<li>`host`: Request domain name</li>
<li>`sip`: Client IP</li>
<li>`ua`: User-Agent</li>
<li>`cookie`: Cookie</li>
<li>`cgi`: CGI script</li>
<li>`xff`: XFF header</li>
<li>`url`: Request URL</li>
<li>`accept`: Request content type</li>
<li>`method`: Request method</li>
<li>`header`: Request header</li>
<li>`sip_proto`: Network layer protocol</li>
        :type MatchFrom: str
        :param MatchParam: The parameter of the field. When `MatchFrom = header`, the key contained in the header can be passed.
        :type MatchParam: str
        :param Operator: The logical operator. Values:
<li>`equal`: Value equals</li>
<li>`not_equal`: Value not equals</li>
<li>`include`: String contains</li>
<li>`not_include`: String not contains</li>
<li>`match`: IP matches</li>
<li>`not_match`: IP not matches</li>
<li>`include_area`: Regions contain</li>
<li>`is_empty`: Value left empty</li>
<li>`not_exists`: Key fields not exist</li>
<li>`regexp`: Regex matches</li>
<li>`len_gt`: Value greater than</li>
<li>`len_lt`: Value smaller than</li>
<li>`len_eq`: Value equals</li>
<li>`match_prefix`: Prefix matches</li>
<li>`match_suffix`: Suffix matches</li>
<li>`wildcard`: Wildcard</li>
        :type Operator: str
        :param MatchContent: The content to match.
        :type MatchContent: str
        """
        self.MatchFrom = None
        self.MatchParam = None
        self.Operator = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.MatchFrom = params.get("MatchFrom")
        self.MatchParam = params.get("MatchParam")
        self.Operator = params.get("Operator")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfig(AbstractModel):
    """ACL configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param AclUserRules: The custom rule.
        :type AclUserRules: list of AclUserRule
        """
        self.Switch = None
        self.AclUserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("AclUserRules") is not None:
            self.AclUserRules = []
            for item in params.get("AclUserRules"):
                obj = AclUserRule()
                obj._deserialize(item)
                self.AclUserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclUserRule(AbstractModel):
    """The custom rule

    """

    def __init__(self):
        r"""
        :param RuleName: The rule name.
        :type RuleName: str
        :param Action: The rule action. Values:
<li>`trans`: Allow the request.</li>
<li>`drop`: Block the request.</li>
<li>`monitor`: Observe the request.</li>
<li>`ban`: Block the IP.</li>
<li>`redirect`: Redirect the request.</li>
<li>`page`: Return the specified page.</li>
<li>`alg`: Verify the request by Javascript challenge.</li>
        :type Action: str
        :param RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
        :type RuleStatus: str
        :param AclConditions: The custom rule.
        :type AclConditions: list of AclCondition
        :param RulePriority: The rule priority. Value range: 0-100.
        :type RulePriority: int
        :param RuleID: The rule ID, which is only used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleID: int
        :param UpdateTime: The update time, which is only used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param PunishTime: The IP blocking duration. Value range: 0 seconds - 2 days. Default value: 0 seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PunishTime: int
        :param PunishTimeUnit: The unit of the IP blocking duration. Values:
<li>`second`: Second</li>
<li>`minutes`: Minute</li>
<li>`hour`: Hour</li>Default value: second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PunishTimeUnit: str
        :param Name: The name of the custom page, which defaults to an empty string.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param PageId: The ID of the custom page, which defaults to 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageId: int
        :param RedirectUrl: The redirection URL, which must be a subdomain name of the site. It defaults to an empty string.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param ResponseCode: The response code returned after redirection, which defaults to 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResponseCode: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.AclConditions = None
        self.RulePriority = None
        self.RuleID = None
        self.UpdateTime = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.Name = None
        self.PageId = None
        self.RedirectUrl = None
        self.ResponseCode = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self.AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AclConditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.Name = params.get("Name")
        self.PageId = params.get("PageId")
        self.RedirectUrl = params.get("RedirectUrl")
        self.ResponseCode = params.get("ResponseCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Action(AbstractModel):
    """Rule engine feature operation. A feature can be of only one of the following three types, so each item in the `RuleAction` array can be of only one of the following types. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view more requirements for entering feature items.

    """

    def __init__(self):
        r"""
        :param NormalAction: Common feature operation. Features of this type include:
<li>`AccessUrlRedirect`: Access URL rewrite</li>
<li>`UpstreamUrlRedirect`: Origin-pull URL rewrite</li>
<li>`QUIC`: QUIC</li>
<li>`WebSocket`: WebSocket</li>
<li>`VideoSeek`: Video dragging</li>
<li>`Authentication`: Token authentication</li>
<li>`CacheKey`: Custom cache key</li>
<li>`Cache`: Node cache TTL</li>
<li>`MaxAge`: Browser cache TTL</li>
<li>`OfflineCache`: Offline cache</li>
<li>`SmartRouting`: Smart acceleration</li>
<li>`RangeOriginPull`: Range GETs</li>
<li>`UpstreamHttp2`: HTTP/2 forwarding</li>
<li>`HostHeader`: Host header rewrite</li>
<li>`ForceRedirect`: Force HTTPS</li>
<li>`OriginPullProtocol`: Origin-pull HTTPS</li>
<li>`CachePrefresh`: Cache prefresh</li>
<li>`Compression`: Smart compression</li>
<li>`Hsts`</li>
<li>`ClientIpHeader`</li>
<li>`TlsVersion`</li>
<li>`OcspStapling`</li>
<li>`Http2`: HTTP/2 access</li>
<li>`UpstreamFollowRedirect: Follow origin redirect</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NormalAction: :class:`tencentcloud.teo.v20220901.models.NormalAction`
        :param RewriteAction: Feature operation with a request/response header. Features of this type include:
<li>`RequestHeader`: HTTP request header modification.</li>
<li>`ResponseHeader`: HTTP response header modification.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RewriteAction: :class:`tencentcloud.teo.v20220901.models.RewriteAction`
        :param CodeAction: Feature operation with a status code. Features of this type include:
<li>`ErrorPage`: Custom error page.</li>
<li>`StatusCodeCache`: Status code cache TTL.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type CodeAction: :class:`tencentcloud.teo.v20220901.models.CodeAction`
        """
        self.NormalAction = None
        self.RewriteAction = None
        self.CodeAction = None


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self.NormalAction = NormalAction()
            self.NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self.RewriteAction = RewriteAction()
            self.RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self.CodeAction = CodeAction()
            self.CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedFilter(AbstractModel):
    """Key-value pair filters for conditional filtering queries and fuzzy queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If one filter has multiple values, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param Name: Field to be filtered.
        :type Name: str
        :param Values: Value of the filtered field.
        :type Values: list of str
        :param Fuzzy: Whether to enable fuzzy query.
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedOriginGroup(AbstractModel):
    """Advanced origin-pull configuration

    """

    def __init__(self):
        r"""
        :param OriginGroupConditions: Matching condition. The "Target" field must be unique.
        :type OriginGroupConditions: list of OriginGroupCondition
        :param OriginGroupId: ID of the primary origin server.
        :type OriginGroupId: str
        :param BackupOriginGroupId: ID of the secondary origin server.
        :type BackupOriginGroupId: str
        """
        self.OriginGroupConditions = None
        self.OriginGroupId = None
        self.BackupOriginGroupId = None


    def _deserialize(self, params):
        if params.get("OriginGroupConditions") is not None:
            self.OriginGroupConditions = []
            for item in params.get("OriginGroupConditions"):
                obj = OriginGroupCondition()
                obj._deserialize(item)
                self.OriginGroupConditions.append(obj)
        self.OriginGroupId = params.get("OriginGroupId")
        self.BackupOriginGroupId = params.get("BackupOriginGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRule(AbstractModel):
    """AI rule engine

    """

    def __init__(self):
        r"""
        :param Mode: The status of the AI rule engine. Values:
<li>`smart_status_close`: Disabled</li>
<li>`smart_status_open`: Block</li>
<li>`smart_status_observe`: Observe</li>
        :type Mode: str
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AliasDomain(AbstractModel):
    """Information of the alias domain name

    """

    def __init__(self):
        r"""
        :param AliasName: The alias domain name.
        :type AliasName: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param TargetName: The target domain name.
        :type TargetName: str
        :param Status: Status of the alias domain name. Values:
<li>`active`: Activated</li>
<li>`pending`: Deploying</li>
<li>`conflict`: Reclaimed</li>
<li>`stop`: Stopped</li>
        :type Status: str
        :param ForbidMode: The blocking mode. Values:
<li>`0`: Not blocked</li>
<li>`11`: Blocked due to regulatory compliance</li>
<li>`14`: Blocked due to ICP filing not obtained</li>
        :type ForbidMode: int
        :param CreatedOn: Creation time of the alias domain name.
        :type CreatedOn: str
        :param ModifiedOn: Modification time of the alias domain name.
        :type ModifiedOn: str
        """
        self.AliasName = None
        self.ZoneId = None
        self.TargetName = None
        self.Status = None
        self.ForbidMode = None
        self.CreatedOn = None
        self.ModifiedOn = None


    def _deserialize(self, params):
        self.AliasName = params.get("AliasName")
        self.ZoneId = params.get("ZoneId")
        self.TargetName = params.get("TargetName")
        self.Status = params.get("Status")
        self.ForbidMode = params.get("ForbidMode")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxy(AbstractModel):
    """Application proxy instance

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param ProxyName: The domain name or subdomain name when `ProxyType=hostname`.
The instance name when `ProxyType=instance`.
        :type ProxyName: str
        :param ProxyType: The proxy type. Values:
<li>`hostname`: The proxy is created by subdomain name.</li>
<li>`instance`: The proxy is created by instance.</li>
        :type ProxyType: str
        :param PlatType: The scheduling mode. Values:
<li>`ip`: Schedule via Anycast IP.</li>
<li>`domain`: Schedule via CNAME.</li>
        :type PlatType: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
Default value: overseas.
        :type Area: str
        :param SecurityType: Whether to enable security protection. Values:
<li>`0`: Disable security protection.</li>
<li>`1`: Enable security protection.</li>
        :type SecurityType: int
        :param AccelerateType: Whether to enable acceleration. Values:
<li>`0`: Disable acceleration.</li>
<li>`1`: Enable acceleration.</li>
        :type AccelerateType: int
        :param SessionPersistTime: The session persistence duration.
        :type SessionPersistTime: int
        :param Status: The rule status. Values:
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
<li>`progress`: Deploying</li>
<li>`stopping`: Disabling</li>
<li>`fail`: Failed to deploy or disable</li>
        :type Status: str
        :param BanStatus: The blocking status of the proxy. Values:
<li>`banned`: Blocked</li>
<li>`banning`: Blocking</li>
<li>`recover`: Unblocked</li>
<li>`recovering`: Unblocking</li>
        :type BanStatus: str
        :param ScheduleValue: Scheduling information.
        :type ScheduleValue: list of str
        :param HostId: When `ProxyType=hostname`:
This field indicates the unique ID of the subdomain name.
        :type HostId: str
        :param Ipv6: The IPv6 access configuration.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param UpdateTime: The update time.
        :type UpdateTime: str
        :param ApplicationProxyRules: List of rules.
        :type ApplicationProxyRules: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyId = None
        self.ProxyName = None
        self.ProxyType = None
        self.PlatType = None
        self.Area = None
        self.SecurityType = None
        self.AccelerateType = None
        self.SessionPersistTime = None
        self.Status = None
        self.BanStatus = None
        self.ScheduleValue = None
        self.HostId = None
        self.Ipv6 = None
        self.UpdateTime = None
        self.ApplicationProxyRules = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ProxyType = params.get("ProxyType")
        self.PlatType = params.get("PlatType")
        self.Area = params.get("Area")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.Status = params.get("Status")
        self.BanStatus = params.get("BanStatus")
        self.ScheduleValue = params.get("ScheduleValue")
        self.HostId = params.get("HostId")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ApplicationProxyRules") is not None:
            self.ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.ApplicationProxyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """Application proxy rule

    """

    def __init__(self):
        r"""
        :param Proto: The protocol. Values:
<li>`TCP`: TCP protocol.</li>
<li>`UDP`: UDP protocol.</li>
        :type Proto: str
        :param Port: The access port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
Note that each rule can have up to 20 ports.
        :type Port: list of str
        :param OriginType: The origin type. Values:
<li>`custom`: Specified origins</li>
<li>`origins`: Origin group</li>
        :type OriginType: str
        :param OriginValue: Origin server information:
<li>When `OriginType=custom`, it indicates one or more origin servers, such as ["8.8.8.8","9.9.9.9"] or ["test.com"].</li>
<li>When `OriginType=origins`, it indicates an origin group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>
        :type OriginValue: list of str
        :param RuleId: The rule ID.
        :type RuleId: str
        :param Status: The rule status. Values:
<li>`online`: Enabled.</li>
<li>`offline`: Disabled.</li>
<li>`progress`: Deploying</li>
<li>`stopping`: Disabling</li>
<li>`fail`: Failed to deploy or disable</li>
        :type Status: str
        :param ForwardClientIp: Passes the client IP. Values:
<li>`TOA`: Pass the client IP via TOA (available only when `Proto=TCP`).</li>
<li>`PPV1`: Pass the client IP via Proxy Protocol V1 (available only when `Proto=TCP`).</li>
<li>`PPV2`: Pass the client IP via Proxy Protocol V2.</li>
<li>`OFF`: Not pass the client IP.</li>Default value: OFF.
        :type ForwardClientIp: str
        :param SessionPersist: Whether to enable session persistence. Values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>Default value: false
        :type SessionPersist: bool
        :param OriginPort: The origin port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
        :type OriginPort: str
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AscriptionInfo(AbstractModel):
    """The site ownership information

    """

    def __init__(self):
        r"""
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: The record type.
        :type RecordType: str
        :param RecordValue: The record value.
        :type RecordValue: str
        """
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None


    def _deserialize(self, params):
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanRequest(AbstractModel):
    """BindZoneToPlan request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site to be bound.
        :type ZoneId: str
        :param PlanId: ID of the target plan.
        :type PlanId: str
        """
        self.ZoneId = None
        self.PlanId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanResponse(AbstractModel):
    """BindZoneToPlan response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BotConfig(AbstractModel):
    """Bot security configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable bot security. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param BotManagedRule: The settings of the bot managed rule. If it is null, the settings that were last configured will be used.
        :type BotManagedRule: :class:`tencentcloud.teo.v20220901.models.BotManagedRule`
        :param BotPortraitRule: The settings of the client reputation rule. If it is null, the settings that were last configured will be used.
        :type BotPortraitRule: :class:`tencentcloud.teo.v20220901.models.BotPortraitRule`
        :param IntelligenceRule: The bot intelligence settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220901.models.IntelligenceRule`
        """
        self.Switch = None
        self.BotManagedRule = None
        self.BotPortraitRule = None
        self.IntelligenceRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("BotManagedRule") is not None:
            self.BotManagedRule = BotManagedRule()
            self.BotManagedRule._deserialize(params.get("BotManagedRule"))
        if params.get("BotPortraitRule") is not None:
            self.BotPortraitRule = BotPortraitRule()
            self.BotPortraitRule._deserialize(params.get("BotPortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self.IntelligenceRule = IntelligenceRule()
            self.IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLog(AbstractModel):
    """Bot attack log

    """

    def __init__(self):
        r"""
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        :param AttackIp: The attacker IP.
        :type AttackIp: str
        :param Domain: The attacked domain name.
        :type Domain: str
        :param RequestUri: The URI.
        :type RequestUri: str
        :param AttackType: Attack type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param RequestMethod: Request method.
        :type RequestMethod: str
        :param AttackContent: The attack content.
        :type AttackContent: str
        :param RiskLevel: The attack level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param RuleId: The rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param SipCountryCode: The country code of the attacker IP, which is defined in ISO-3166 alpha-2. For the list of country codes, see [ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json).
        :type SipCountryCode: str
        :param EventId: The attack event ID.
        :type EventId: str
        :param DisposalMethod: The processing method.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param HttpLog: The HTTP log.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param Ua: The user agent.
        :type Ua: str
        :param DetectionMethod: The detection method.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetectionMethod: str
        :param Confidence: The credibility level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Confidence: str
        :param Maliciousness: Maliciousness
Note: This field may return null, indicating that no valid values can be obtained.
        :type Maliciousness: str
        :param RuleDetailList: The security rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param Label: The bot tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Label: str
        """
        self.AttackTime = None
        self.AttackIp = None
        self.Domain = None
        self.RequestUri = None
        self.AttackType = None
        self.RequestMethod = None
        self.AttackContent = None
        self.RiskLevel = None
        self.RuleId = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.Ua = None
        self.DetectionMethod = None
        self.Confidence = None
        self.Maliciousness = None
        self.RuleDetailList = None
        self.Label = None


    def _deserialize(self, params):
        self.AttackTime = params.get("AttackTime")
        self.AttackIp = params.get("AttackIp")
        self.Domain = params.get("Domain")
        self.RequestUri = params.get("RequestUri")
        self.AttackType = params.get("AttackType")
        self.RequestMethod = params.get("RequestMethod")
        self.AttackContent = params.get("AttackContent")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleId = params.get("RuleId")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.Ua = params.get("Ua")
        self.DetectionMethod = params.get("DetectionMethod")
        self.Confidence = params.get("Confidence")
        self.Maliciousness = params.get("Maliciousness")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot managed rules. The rule IDs can be obtained from the output of DescribeBotManagedRules.

    """

    def __init__(self):
        r"""
        :param Action: The rule action. Values:
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`alg`: JavaScript challenge</li>
<li>`monitor`: Observe</li>
        :type Action: str
        :param RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param TransManagedIds: The ID of the rule that applies the "Allow" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransManagedIds: list of int
        :param AlgManagedIds: The ID of the rule that applies the "JavaScript challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlgManagedIds: list of int
        :param CapManagedIds: The ID of the rule that applies the "Managed challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CapManagedIds: list of int
        :param MonManagedIds: The ID of the rule that applies the "Observe" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonManagedIds: list of int
        :param DropManagedIds: The ID of the rule that applies the "Block" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DropManagedIds: list of int
        """
        self.Action = None
        self.RuleID = None
        self.TransManagedIds = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.RuleID = params.get("RuleID")
        self.TransManagedIds = params.get("TransManagedIds")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRuleDetail(AbstractModel):
    """Bot managed rule details

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param Description: The rule description.
        :type Description: str
        :param RuleTypeName: Rule type
        :type RuleTypeName: str
        :param Status: The rule status.
        :type Status: str
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPortraitRule(AbstractModel):
    """Bot user portrait rules

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param AlgManagedIds: The ID of the rule that applies the "JavaScript challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlgManagedIds: list of int
        :param CapManagedIds: The ID of the rule that applies the "Managed challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CapManagedIds: list of int
        :param MonManagedIds: The ID of the rule that applies the "Observe" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonManagedIds: list of int
        :param DropManagedIds: The ID of the rule that applies the "Block" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DropManagedIds: list of int
        """
        self.Switch = None
        self.RuleID = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleID = params.get("RuleID")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CC(AbstractModel):
    """CC configuration item.

    """

    def __init__(self):
        r"""
        :param Switch: WAF switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param PolicyId: ID of the policy
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEvent(AbstractModel):
    """CC block event

    """

    def __init__(self):
        r"""
        :param ClientIp: The client IP.
        :type ClientIp: str
        :param InterceptNum: The requests per minute that are blocked.
        :type InterceptNum: int
        :param InterceptTime: Block time in seconds.
        :type InterceptTime: int
        """
        self.ClientIp = None
        self.InterceptNum = None
        self.InterceptTime = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.InterceptNum = params.get("InterceptNum")
        self.InterceptTime = params.get("InterceptTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable cache configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param CacheTime: Cache expiration time setting.
Unit: second. The maximum value is 365 days.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheTime: int
        :param IgnoreCacheControl: Whether to enable force cache. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        """
        self.Switch = None
        self.CacheTime = None
        self.IgnoreCacheControl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration.

    """

    def __init__(self):
        r"""
        :param Cache: Cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220901.models.Cache`
        :param NoCache: No-cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220901.models.NoCache`
        :param FollowOrigin: Follows the origin server configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220901.models.FollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = NoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = FollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """The cache key configuration.

    """

    def __init__(self):
        r"""
        :param FullUrlCache: Whether to enable full-path cache. Values:
<li>`on`: Enable full-path cache (i.e., disable Ignore Query String).</li>
<li>`off`: Disable full-path cache (i.e., enable Ignore Query String).</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullUrlCache: str
        :param IgnoreCase: Whether to ignore case in the cache key. Values:
<li>`on`: Ignore</li>
<li>`off`: Not ignore</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220901.models.QueryString`
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """Cache prefresh

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable cache prefresh. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Percent: The cache prefresh percentage. Values: 1-99
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        """
        self.Switch = None
        self.Percent = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate request structure.

    """

    def __init__(self):
        r"""
        :param Certificate: Content of the certificate.
        :type Certificate: str
        :param PrivateKey: Content of the private key.
        :type PrivateKey: str
        """
        self.Certificate = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateResponse(AbstractModel):
    """CheckCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClientIpCountry(AbstractModel):
    """Location information of the client IP carried in origin-pull. It is formatted as a two-letter ISO-3166-1 country/region code.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param HeaderName: Header name of ClientIpCountry. This field is valid only when `Switch=on`.
If it is left empty, the default value `EO-Client-IPCountry` will be used.
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpHeader(AbstractModel):
    """The client IP header configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param HeaderName: The name of the HTTP header that contains the client IP, which is used for forwarding.
If this field is not specified, the default value `X-Forwarded-IP` will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientRule(AbstractModel):
    """The client rule information

    """

    def __init__(self):
        r"""
        :param ClientIp: The client IP.
        :type ClientIp: str
        :param RuleType: The rule type.
        :type RuleType: str
        :param RuleId: The rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param Description: The rule description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param IpStatus: The blocking status. Values:
<li>`block`: Block;</li>
<li>`allow`: Allow.</li>
        :type IpStatus: str
        :param BlockTime: The blocking time recorded in UNIX timestamp.
        :type BlockTime: int
        :param Id: The data entry ID.
        :type Id: str
        """
        self.ClientIp = None
        self.RuleType = None
        self.RuleId = None
        self.Description = None
        self.IpStatus = None
        self.BlockTime = None
        self.Id = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.IpStatus = params.get("IpStatus")
        self.BlockTime = params.get("BlockTime")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogTopicInfo(AbstractModel):
    """The log topic information

    """

    def __init__(self):
        r"""
        :param TaskName: Name of the task.
        :type TaskName: str
        :param ZoneName: Name of the site.
        :type ZoneName: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param TopicId: ID of the log topic.
        :type TopicId: str
        :param EntityType: Type of the task.
        :type EntityType: str
        :param Period: Retention period of the log topic.
        :type Period: int
        :param Enabled: Whether the log topic is enabled.
        :type Enabled: bool
        :param Deleted: Whether the log topic is deleted.
        :type Deleted: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param Target: Target location. Values:
<li>`cls`: Ship logs to CLS;</li>
<li>`custom_enpoint`: Ship logs to a custom address.</li>
        :type Target: str
        :param LogSetRegion: Region of the logset.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetRegion: str
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland).</li>
        :type Area: str
        :param LogSetType: Type of the shipping task. Values:
<li>`cls`: Ship logs to CLS.</li>
<li>`custom_endpoint`: Ship logs to custom APIs.</li>
        :type LogSetType: str
        """
        self.TaskName = None
        self.ZoneName = None
        self.LogSetId = None
        self.TopicId = None
        self.EntityType = None
        self.Period = None
        self.Enabled = None
        self.Deleted = None
        self.CreateTime = None
        self.Target = None
        self.LogSetRegion = None
        self.ZoneId = None
        self.Area = None
        self.LogSetType = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.ZoneName = params.get("ZoneName")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.EntityType = params.get("EntityType")
        self.Period = params.get("Period")
        self.Enabled = params.get("Enabled")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.Target = params.get("Target")
        self.LogSetRegion = params.get("LogSetRegion")
        self.ZoneId = params.get("ZoneId")
        self.Area = params.get("Area")
        self.LogSetType = params.get("LogSetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeAction(AbstractModel):
    """Rule engine action with a status code

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Operation parameter.
        :type Parameters: list of RuleCodeActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleCodeActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable smart compression. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Algorithms: Compression algorithm. Values:
<li>`brotli`: Brotli algorithm</li>
<li>`gzip`: Gzip algorithm</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Algorithms: list of str
        """
        self.Switch = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasDomainRequest(AbstractModel):
    """CreateAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param AliasName: The alias domain name.
        :type AliasName: str
        :param TargetName: The target domain name.
        :type TargetName: str
        :param CertType: Certificate configuration. Values:
<li>`none`: Off</li>
<li>`hosting`: Managed SSL certificate</li>
<li>`apply`: Free certificate</li>Default value: none
        :type CertType: str
        :param CertId: The certificate ID. This field is required when `CertType=hosting`.
        :type CertId: list of str
        """
        self.ZoneId = None
        self.AliasName = None
        self.TargetName = None
        self.CertType = None
        self.CertId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasName = params.get("AliasName")
        self.TargetName = params.get("TargetName")
        self.CertType = params.get("CertType")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasDomainResponse(AbstractModel):
    """CreateAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyName: When `ProxyType=hostname`, this field indicates a domain name or subdomain name.
When `ProxyType=instance`, it indicates a proxy instance.
        :type ProxyName: str
        :param PlatType: The scheduling mode. Values:
<li>`ip`: Schedule via Anycast IP.</li>
<li>`domain`: Schedule via CNAME.</li>
        :type PlatType: str
        :param SecurityType: Whether to enable security protection. Values:
<li>`0`: Disable security protection.</li>
<li>`1`: Enable security protection.</li>
        :type SecurityType: int
        :param AccelerateType: Whether to enable acceleration. Values:
<li>`0`: Disable acceleration.</li>
<li>`1`: Enable acceleration.</li>
        :type AccelerateType: int
        :param ProxyType: The proxy type. Values:
<li>`hostname`: The proxy is created by subdomain name.</li>
<li>`instance`: The proxy is created by instance.</li>If not specified, this field uses the default value `instance`.
        :type ProxyType: str
        :param SessionPersistTime: The session persistence duration. Value range: 30-3600 (in seconds).
If not specified, this field uses the default value 600.
        :type SessionPersistTime: int
        :param Ipv6: The IPv6 access configuration.
If this field is not specified, IPv6 access will be disabled.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ApplicationProxyRules: The rule details.
If this field is not specified, an application proxy rule will not be created.
        :type ApplicationProxyRules: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ProxyType = None
        self.SessionPersistTime = None
        self.Ipv6 = None
        self.ApplicationProxyRules = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ProxyType = params.get("ProxyType")
        self.SessionPersistTime = params.get("SessionPersistTime")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ApplicationProxyRules") is not None:
            self.ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.ApplicationProxyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: The L4 application proxy ID.
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param Proto: The protocol. Values:
<li>`TCP`: TCP protocol</li>
<li>`UDP`: UDP protocol</li>
        :type Proto: str
        :param Port: The access port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-90</li>
        :type Port: list of str
        :param OriginType: The origin type. Values:
<li>`custom`: Specified origins</li>
<li>`origins`: Origin group</li>
        :type OriginType: str
        :param OriginValue: Origin server information:
<li>When `OriginType=custom`, it indicates one or more origin servers, such as ["8.8.8.8","9.9.9.9"] or ["test.com"].</li>
<li>When `OriginType=origins`, it indicates an origin group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. Values:
<li>`TOA`: Pass the client IP via TOA (available only when `Proto=TCP`).</li>
<li>`PPV1`: Pass the client IP via Proxy Protocol V1 (available only when `Proto=TCP`).</li>
<li>`PPV2`: Pass the client IP via Proxy Protocol V2.</li>
<li>`OFF`: Not pass the client IP.</li>Default value: OFF.
        :type ForwardClientIp: str
        :param SessionPersist: Whether to enable session persistence. Values:
<li>`true`: Enable.</li>
<li>`false`: Disable.</li>Default value: false.
        :type SessionPersist: bool
        :param OriginPort: The origin port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
        :type OriginPort: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateCredentialRequest(AbstractModel):
    """CreateCredential request structure.

    """


class CreateCredentialResponse(AbstractModel):
    """CreateCredential response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCustomErrorPageRequest(AbstractModel):
    """CreateCustomErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name.
        :type Entity: str
        :param Name: Name of the file specified to be returned.
        :type Name: str
        :param Content: The custom page content, which is passed after being URL-encoded.
        :type Content: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Name = None
        self.Content = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomErrorPageResponse(AbstractModel):
    """CreateCustomErrorPage response structure.

    """

    def __init__(self):
        r"""
        :param PageId: ID of the custom page
        :type PageId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageId = params.get("PageId")
        self.RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record.
        :type ZoneId: str
        :param Type: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type Type: str
        :param Name: The DNS record name.
        :type Name: str
        :param Content: The DNS record content.
        :type Content: str
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Mode: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect. Default value: 300
        :type TTL: int
        :param Priority: Specifies a value in the range 1–50 when you make changes to the MX records. A smaller value indicates higher priority. Note that the default value 0 will be used if this field is not specified.
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.TTL = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDnsRecordResponse(AbstractModel):
    """CreateDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The DNS record ID.
        :type DnsRecordId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DnsRecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.RequestId = params.get("RequestId")


class CreateIpTableListRequest(AbstractModel):
    """CreateIpTableList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name/layer-4 proxy.
        :type Entity: str
        :param IpTableRules: List of basic access control rules.
        :type IpTableRules: list of IpTableRule
        """
        self.ZoneId = None
        self.Entity = None
        self.IpTableRules = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        if params.get("IpTableRules") is not None:
            self.IpTableRules = []
            for item in params.get("IpTableRules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self.IpTableRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIpTableListResponse(AbstractModel):
    """CreateIpTableList response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Host: The load balancing hostname.
        :type Host: str
        :param Type: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Type: str
        :param OriginGroupId: The ID of the primary origin group.
        :type OriginGroupId: str
        :param BackupOriginGroupId: The ID of the secondary origin group (only available when `Type=proxied`). If not specified, it indicates that secondary origins are not used.
        :type BackupOriginGroupId: str
        :param TTL: When `Type=dns_only`, it indicates the amount of time that DNS records remain in the cache of a DNS server.
Value range: 60-86400 (in seconds). If it's not specified, the default value 600 will be used.
        :type TTL: int
        :param OriginType: The origin-pull type. Values:
<li>`normal`: Primary/Secondary origin-pull</li>
<li>`advanced`: Advanced origin-pull (only used when `Type=proxied`)</li>If it is left empty, primary/secondary origin-pull is applied.
        :type OriginType: str
        :param AdvancedOriginGroups: Advanced origin-pull configuration. This field is valid when `OriginType=advanced`.
        :type AdvancedOriginGroups: list of AdvancedOriginGroup
        """
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.OriginGroupId = None
        self.BackupOriginGroupId = None
        self.TTL = None
        self.OriginType = None
        self.AdvancedOriginGroups = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.OriginGroupId = params.get("OriginGroupId")
        self.BackupOriginGroupId = params.get("BackupOriginGroupId")
        self.TTL = params.get("TTL")
        self.OriginType = params.get("OriginType")
        if params.get("AdvancedOriginGroups") is not None:
            self.AdvancedOriginGroups = []
            for item in params.get("AdvancedOriginGroups"):
                obj = AdvancedOriginGroup()
                obj._deserialize(item)
                self.AdvancedOriginGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancingResponse(AbstractModel):
    """CreateLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: The load balancer ID.
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class CreateLogSetRequest(AbstractModel):
    """CreateLogSet request structure.

    """

    def __init__(self):
        r"""
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        """
        self.LogSetName = None
        self.LogSetRegion = None


    def _deserialize(self, params):
        self.LogSetName = params.get("LogSetName")
        self.LogSetRegion = params.get("LogSetRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogSetResponse(AbstractModel):
    """CreateLogSet response structure.

    """

    def __init__(self):
        r"""
        :param LogSetId: ID of the logset created.
        :type LogSetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogSetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogSetId = params.get("LogSetId")
        self.RequestId = params.get("RequestId")


class CreateLogTopicTaskRequest(AbstractModel):
    """CreateLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param TopicName: Topic name of the logset.
        :type TopicName: str
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param ZoneName: Name of the site.
        :type ZoneName: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        :param Period: Retention period of the log topic. Value range: 1–366 (in days).
        :type Period: int
        :param EntityList: List of shipping entities.
        :type EntityList: list of str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Global (outside the Chinese mainland).</li> If this field is not specified, the acceleration region will be determined based on the user’s region.
        :type Area: str
        """
        self.LogSetId = None
        self.LogSetRegion = None
        self.TopicName = None
        self.TaskName = None
        self.ZoneId = None
        self.ZoneName = None
        self.EntityType = None
        self.Period = None
        self.EntityList = None
        self.Area = None


    def _deserialize(self, params):
        self.LogSetId = params.get("LogSetId")
        self.LogSetRegion = params.get("LogSetRegion")
        self.TopicName = params.get("TopicName")
        self.TaskName = params.get("TaskName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.EntityType = params.get("EntityType")
        self.Period = params.get("Period")
        self.EntityList = params.get("EntityList")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogTopicTaskResponse(AbstractModel):
    """CreateLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the log topic created.
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param OriginType: The origin type. Values:
<li>`self`: Customer origin</li>
<li>`third_party`: Third-party origin</li>
<li>`cos`: Tencent Cloud COS origin</li>
        :type OriginType: str
        :param OriginGroupName: The name of the origin group.
        :type OriginGroupName: str
        :param ConfigurationType: The origin configuration type when `OriginType=self`. Values:
<li>`area`: Configure by region.</li>
<li>`weight`: Configure by weight.</li>
<li>`proto`: Configure by HTTP protocol.</li>When `OriginType=third_party/cos`, leave this field empty.
        :type ConfigurationType: str
        :param OriginRecords: Details of the origin record.
        :type OriginRecords: list of OriginRecord
        :param HostHeader: The origin domain. This field can be specified only when `OriginType=self`.
        :type HostHeader: str
        """
        self.ZoneId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOriginGroupResponse(AbstractModel):
    """CreateOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param OriginGroupId: The ID of the origin group.
        :type OriginGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginGroupId = params.get("OriginGroupId")
        self.RequestId = params.get("RequestId")


class CreatePlanForZoneRequest(AbstractModel):
    """CreatePlanForZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param PlanType: The plan option. Values:
<li>`sta`: Standard plan that supports content delivery network outside the Chinese mainland.</li>
<li>`sta_with_bot`: Standard plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`sta_cm`: Standard plan that supports content delivery network inside the Chinese mainland.</li>
<li>`sta_cm_with_bot`: Standard plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`sta_global`: Standard plan that supports content delivery network over the globe.</li>
<li>`sta_global_with_bot`: Standard plan that supports content delivery network over the globe and bot management.</li>
<li>`ent`: Enterprise plan that supports content delivery network outside the Chinese mainland.</li>
<li>`ent_with_bot`: Enterprise plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`ent_cm`: Enterprise plan that supports content delivery network inside the Chinese mainland.</li>
<li>`ent_cm_with_bot`: Enterprise plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`ent_global`: Enterprise plan that supports content delivery network over the globe.</li>
<li>`ent_global_with_bot`: Enterprise plan that supports content delivery network over the globe and bot management.</li>To get the available plan options for your account, view the output from <a href="https://tcloud4api.woa.com/document/product/1657/80124?!preview&!document=1">DescribeAvailablePlans</a>.
        :type PlanType: str
        """
        self.ZoneId = None
        self.PlanType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanForZoneResponse(AbstractModel):
    """CreatePlanForZone response structure.

    """

    def __init__(self):
        r"""
        :param ResourceNames: List of purchased resources.
        :type ResourceNames: list of str
        :param DealNames: List or order numbers.
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResourceNames = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceNames = params.get("ResourceNames")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: Whether to encode a URL according to RFC3986. Enable this field when the URL contains non-ASCII characters.
        :type EncodeUrl: bool
        :param Headers: HTTP header information
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Type: Mode of cache purging. Values:
<li>`purge_url`: Purge by URL</li>
<li>`purge_prefix`: Purge by prefix</li>
<li>`purge_host`: Purge by hostname</li>
<li>`purge_all`: Purge all caches</li>
<li>`purge_cache_tag`: Purge by cache tag</li>
        :type Type: str
        :param Targets: Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Enter the hostname, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Enter the prefix, such as http://www.example.com/example.
3. When `Type = purge_url`:
Enter the URL, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`:
This field can be left empty.
5. When `Type = purge_cache_tag`:
Enter the cache tag, such as tag1.
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks and reasons.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateReplayTaskRequest(AbstractModel):
    """CreateReplayTask request structure.

    """

    def __init__(self):
        r"""
        :param Ids: List of replay task IDs.
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplayTaskResponse(AbstractModel):
    """CreateReplayTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks and reasons.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleName: The rule name (1 to 255 characters)
        :type RuleName: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        :param Tags: Tag of the rule.
        :type Tags: list of str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateSecurityDropPageRequest(AbstractModel):
    """CreateSecurityDropPage request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name.
        :type Entity: str
        :param Name: Name of the block page file.
        :type Name: str
        :param Content: The block page content, which is passed after being URL-encoded.
        :type Content: str
        :param Type: How to build the block page. Values:
<li>`file`: Upload a file to be URL-encoded.</li>
<li>`url`: Upload a URL to be URL-encoded.</li>
        :type Type: str
        :param Module: The module that applies on the block page. Values:
<li>`waf`: Managed rules</li>
<li>`rate`: Custom rules</li>
        :type Module: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Name = None
        self.Content = None
        self.Type = None
        self.Module = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Type = params.get("Type")
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityDropPageResponse(AbstractModel):
    """CreateSecurityDropPage response structure.

    """

    def __init__(self):
        r"""
        :param PageId: ID of the custom page.
        :type PageId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageId = params.get("PageId")
        self.RequestId = params.get("RequestId")


class CreateSpeedTestingRequest(AbstractModel):
    """CreateSpeedTesting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Host: The subdomain name to test.
        :type Host: str
        """
        self.ZoneId = None
        self.Host = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSpeedTestingResponse(AbstractModel):
    """CreateSpeedTesting response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Type: The access mode. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>This field will be set to the default value `full` if not specified.
        :type Type: str
        :param JumpStart: Whether to skip scanning the existing DNS records of the site. Default value: false.
        :type JumpStart: bool
        :param Tags: The resource tag.
        :type Tags: list of Tag
        :param AllowDuplicates: Whether to allow duplicate sites. Values:
<li>`true`: Duplicate sites are allowed.</li>
<li>`false`: Duplicate sites are not allowed.</li>If it is left empty, the default value `false` is used.
        :type AllowDuplicates: bool
        :param AliasZoneName: The site alias. It can be up to 20 characters consisting of digits, letters, hyphens (-) and underscores (_).
        :type AliasZoneName: str
        """
        self.ZoneName = None
        self.Type = None
        self.JumpStart = None
        self.Tags = None
        self.AllowDuplicates = None
        self.AliasZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AllowDuplicates = params.get("AllowDuplicates")
        self.AliasZoneName = params.get("AliasZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneResponse(AbstractModel):
    """CreateZone response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class DDoS(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAcl(AbstractModel):
    """DDoS port filtering

    """

    def __init__(self):
        r"""
        :param DDoSAclRules: Array of port filtering rules.
        :type DDoSAclRules: list of DDoSAclRule
        :param Switch: Whether to clear port filtering rules. Values:
<li>`off`: Clear port filtering rules.</li>
<li>`on`: Configure port filtering rules. In this case, DDoSAclRules needs to be specified.</li>
        :type Switch: str
        """
        self.DDoSAclRules = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("DDoSAclRules") is not None:
            self.DDoSAclRules = []
            for item in params.get("DDoSAclRules"):
                obj = DDoSAclRule()
                obj._deserialize(item)
                self.DDoSAclRules.append(obj)
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAclRule(AbstractModel):
    """DDoS port filtering configuration

    """

    def __init__(self):
        r"""
        :param DportEnd: End of the destination port. Value range: 0–65535.
        :type DportEnd: int
        :param DportStart: Start of the destination port. Value range: 0–65535.
        :type DportStart: int
        :param SportEnd: End of the source port. Value range: 0–65535.
        :type SportEnd: int
        :param SportStart: Start of the source port. Value range: 0–65535.
        :type SportStart: int
        :param Protocol: The protocol. Values:
<li>`tcp`: TCP protocol</li>
<li>`udp`: UDP protocol</li>
<li>`all`: All protocols</li>
        :type Protocol: str
        :param Action: Action to be executed. Values:
<li>`drop`: Discard</li>
<li>`transmit`: Allow</li>
<li>`forward`: Continue protection</li>
        :type Action: str
        """
        self.DportEnd = None
        self.DportStart = None
        self.SportEnd = None
        self.SportStart = None
        self.Protocol = None
        self.Action = None


    def _deserialize(self, params):
        self.DportEnd = params.get("DportEnd")
        self.DportStart = params.get("DportStart")
        self.SportEnd = params.get("SportEnd")
        self.SportStart = params.get("SportStart")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAllowBlock(AbstractModel):
    """IP Allowlist/Blocklist

    """

    def __init__(self):
        r"""
        :param DDoSAllowBlockRules: Array of objects in the blocklist/allowlist configuration.
        :type DDoSAllowBlockRules: list of DDoSAllowBlockRule
        :param Switch: Whether to clear the blocklist/allowlist. Values:
<li>`off`: Disable.</li>
<li>`on`: Enable. In this case, UserAllowBlockIp needs to be specified.</li>
        :type Switch: str
        """
        self.DDoSAllowBlockRules = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("DDoSAllowBlockRules") is not None:
            self.DDoSAllowBlockRules = []
            for item in params.get("DDoSAllowBlockRules"):
                obj = DDoSAllowBlockRule()
                obj._deserialize(item)
                self.DDoSAllowBlockRules.append(obj)
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAllowBlockRule(AbstractModel):
    """Details of the IP blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param Ip: The client IP, which can be a single IP, IP range, or subnet range, such as "1.1.1.1", "1.1.1.2-1.1.1.3", and "1.2.1.0/24-1.2.2.0/24".
        :type Ip: str
        :param Type: The type. Values:
<li>`block`: Blocklist</li><li>`allow`: Allowlist</li>
        :type Type: str
        :param UpdateTime: The 10-digit timestamp, such as `1199116800`. The current time will be used if this field is not specified.
        :type UpdateTime: int
        """
        self.Ip = None
        self.Type = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAntiPly(AbstractModel):
    """DDoS protection against protocol and connection attacks

    """

    def __init__(self):
        r"""
        :param DropTcp: Whether to enable TCP protocol blocking. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type DropTcp: str
        :param DropUdp: Whether to enable UDP protocol blocking. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type DropUdp: str
        :param DropIcmp: Whether to enable ICMP protocol blocking. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type DropIcmp: str
        :param DropOther: Whether to enable blocking of other protocols. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type DropOther: str
        :param SourceCreateLimit: Maximum number of new connections to the origin per second. Value range: 0–4294967295.
        :type SourceCreateLimit: int
        :param SourceConnectLimit: Maximum number of concurrent connections to the origin. Value range: 0–4294967295.
        :type SourceConnectLimit: int
        :param DestinationCreateLimit: Maximum number of new connections to the destination port per second. Value range: 0–4294967295.
        :type DestinationCreateLimit: int
        :param DestinationConnectLimit: Maximum number of concurrent connections to the destination port. Value range: 0–4294967295.
        :type DestinationConnectLimit: int
        :param AbnormalConnectNum: Maximum number of abnormal connections per second. Value range: 0–4294967295.
        :type AbnormalConnectNum: int
        :param AbnormalSynRatio: Maximum percentage of abnormal SYN packets. Value range: 0–100.
        :type AbnormalSynRatio: int
        :param AbnormalSynNum: Maximum number of abnormal SYN packets. Value range: 0–65535.
        :type AbnormalSynNum: int
        :param ConnectTimeout: Maximum number of detected connections timed out per second. Value range: 0–65535.
        :type ConnectTimeout: int
        :param EmptyConnectProtect: Whether to enable null session protection. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type EmptyConnectProtect: str
        :param UdpShard: Whether to enable UDP fragmentation. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type UdpShard: str
        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.SourceCreateLimit = None
        self.SourceConnectLimit = None
        self.DestinationCreateLimit = None
        self.DestinationConnectLimit = None
        self.AbnormalConnectNum = None
        self.AbnormalSynRatio = None
        self.AbnormalSynNum = None
        self.ConnectTimeout = None
        self.EmptyConnectProtect = None
        self.UdpShard = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.SourceCreateLimit = params.get("SourceCreateLimit")
        self.SourceConnectLimit = params.get("SourceConnectLimit")
        self.DestinationCreateLimit = params.get("DestinationCreateLimit")
        self.DestinationConnectLimit = params.get("DestinationConnectLimit")
        self.AbnormalConnectNum = params.get("AbnormalConnectNum")
        self.AbnormalSynRatio = params.get("AbnormalSynRatio")
        self.AbnormalSynNum = params.get("AbnormalSynNum")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.EmptyConnectProtect = params.get("EmptyConnectProtect")
        self.UdpShard = params.get("UdpShard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEvent(AbstractModel):
    """The DDoS attacker information

    """

    def __init__(self):
        r"""
        :param EventId: The event ID.
        :type EventId: str
        :param AttackType: The attack type.
        :type AttackType: str
        :param AttackStatus: The attack status.
        :type AttackStatus: int
        :param AttackMaxBandWidth: The maximum attack bandwidth.
        :type AttackMaxBandWidth: int
        :param AttackPacketMaxRate: The peak attack packet rate.
        :type AttackPacketMaxRate: int
        :param AttackStartTime: The attack start time recorded in seconds.
        :type AttackStartTime: int
        :param AttackEndTime: The attack end time recorded in seconds.
        :type AttackEndTime: int
        :param PolicyId: The DDoS policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        """
        self.EventId = None
        self.AttackType = None
        self.AttackStatus = None
        self.AttackMaxBandWidth = None
        self.AttackPacketMaxRate = None
        self.AttackStartTime = None
        self.AttackEndTime = None
        self.PolicyId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self.AttackStartTime = params.get("AttackStartTime")
        self.AttackEndTime = params.get("AttackEndTime")
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEventDetailData(AbstractModel):
    """The details of a DDoS attack event

    """

    def __init__(self):
        r"""
        :param AttackStatus: The attack status. Values:
<li>`1`: The attack is being observed;</li>
<li>`2`: The attack started;</li>
<li>`3`: The attack ended.</li>
        :type AttackStatus: int
        :param AttackType: The attack type.
        :type AttackType: str
        :param EndTime: The end time.
        :type EndTime: int
        :param StartTime: The start time.
        :type StartTime: int
        :param MaxBandWidth: The maximum bandwidth.
        :type MaxBandWidth: int
        :param PacketMaxRate: The maximum packet rate.
        :type PacketMaxRate: int
        :param EventId: The event ID.
        :type EventId: str
        :param PolicyId: The DDoS policy ID.
        :type PolicyId: int
        """
        self.AttackStatus = None
        self.AttackType = None
        self.EndTime = None
        self.StartTime = None
        self.MaxBandWidth = None
        self.PacketMaxRate = None
        self.EventId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.AttackStatus = params.get("AttackStatus")
        self.AttackType = params.get("AttackType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.PacketMaxRate = params.get("PacketMaxRate")
        self.EventId = params.get("EventId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceEvent(AbstractModel):
    """The DDoS attacker information

    """

    def __init__(self):
        r"""
        :param AttackSourceIp: The attacker IP.
        :type AttackSourceIp: str
        :param AttackRegion: The country or region.
        :type AttackRegion: str
        :param AttackFlow: The accumulative attack traffic.
        :type AttackFlow: int
        :param AttackPacketNum: The accumulative attack packets.
        :type AttackPacketNum: int
        """
        self.AttackSourceIp = None
        self.AttackRegion = None
        self.AttackFlow = None
        self.AttackPacketNum = None


    def _deserialize(self, params):
        self.AttackSourceIp = params.get("AttackSourceIp")
        self.AttackRegion = params.get("AttackRegion")
        self.AttackFlow = params.get("AttackFlow")
        self.AttackPacketNum = params.get("AttackPacketNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSBlockData(AbstractModel):
    """The blocking time of a DDoS attack

    """

    def __init__(self):
        r"""
        :param StartTime: The start time recorded in UNIX timestamp.
        :type StartTime: int
        :param EndTime: The start time recorded in UNIX timestamp.
        :type EndTime: int
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSFeaturesFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param Action: Action to be executed. Valid values:
<li>`drop`: Discard</li>
<li>`transmit`: Allow</li>
<li>`drop_block`: Discard and block</li>
<li>`forward`: Continue protection</li>
        :type Action: str
        :param Protocol: The protocol. Values:
<li>`tcp`: TCP protocol</li>
<li>`udp`: UDP protocol</li>
<li>`icmp`: ICMP protocol</li>
<li>`all`: All protocols</li>
        :type Protocol: str
        :param DportStart: Start of the destination port. Value range: 0–65535.
        :type DportStart: int
        :param DportEnd: End of the destination port. Value range: 0–65535.
        :type DportEnd: int
        :param PacketMin: Minimum packet length. Value range: 0–1500.
        :type PacketMin: int
        :param PacketMax: Maximum packet length. Value range: 0–1500.
        :type PacketMax: int
        :param SportStart: Start of the source port. Value range: 0–65535.
        :type SportStart: int
        :param SportEnd: End of the source port. Value range: 0–65535.
        :type SportEnd: int
        :param MatchType: Matching method 1 of **feature 1**. Values:
<li>`pcre`: Regular expression match</li>
<li>`sunday`: String match</li>An empty string is used by default.
        :type MatchType: str
        :param IsNot: Whether the pattern in **feature 1** is matched. This parameter is used together with `MatchType`. Values:
<li>`0`: Matched</li>
<li>`1`: Not matched</li>
        :type IsNot: int
        :param Offset: Offset 1 of **feature 1**. Value range: 0–1500.
        :type Offset: int
        :param Depth: The depth to inspect **feature 1** in the packet. Value range: 1–1500.
        :type Depth: int
        :param MatchBegin: The layer from which each match starts. Values:
<li>`begin_l5`: Start from the payload.</li>
<li>`begin_l4`: Start from the TCP/UDP header.</li>
<li>`begin_l3`: Start from the IP header.</li>
        :type MatchBegin: str
        :param Str: The match content of **feature 1**.
        :type Str: str
        :param MatchType2: Matching method 2 of **feature 2**. Values:
<li>`pcre`: Regular expression match</li>
<li>`sunday`: String match</li>An empty string is used by default.
        :type MatchType2: str
        :param IsNot2: Whether the pattern in **feature 2** is matched. This parameter is used together with `MatchType2`. Values:
<li>`0`: Matched</li>
<li>`1`: Not matched</li>
        :type IsNot2: int
        :param Offset2: Offset 2 of **feature 2**. Value range: 0–1500.
        :type Offset2: int
        :param Depth2: The depth to inspect **feature 2** in the packet. Value range: 1–1500.
        :type Depth2: int
        :param MatchBegin2: The layer from which each match starts. Values:
<li>`begin_l5`: Start from the payload.</li>
<li>`begin_l4`: Start from the TCP/UDP header.</li>
<li>`begin_l3`: Start from the IP header.</li>
        :type MatchBegin2: str
        :param Str2: The match content of **feature 2**.
        :type Str2: str
        :param MatchLogic: Multi-feature relationship. Enter `none` if only **feature 1** is configured. If **feature 2** exists, you can leave this parameter empty.
        :type MatchLogic: str
        """
        self.Action = None
        self.Protocol = None
        self.DportStart = None
        self.DportEnd = None
        self.PacketMin = None
        self.PacketMax = None
        self.SportStart = None
        self.SportEnd = None
        self.MatchType = None
        self.IsNot = None
        self.Offset = None
        self.Depth = None
        self.MatchBegin = None
        self.Str = None
        self.MatchType2 = None
        self.IsNot2 = None
        self.Offset2 = None
        self.Depth2 = None
        self.MatchBegin2 = None
        self.Str2 = None
        self.MatchLogic = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Protocol = params.get("Protocol")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PacketMin = params.get("PacketMin")
        self.PacketMax = params.get("PacketMax")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.MatchType = params.get("MatchType")
        self.IsNot = params.get("IsNot")
        self.Offset = params.get("Offset")
        self.Depth = params.get("Depth")
        self.MatchBegin = params.get("MatchBegin")
        self.Str = params.get("Str")
        self.MatchType2 = params.get("MatchType2")
        self.IsNot2 = params.get("IsNot2")
        self.Offset2 = params.get("Offset2")
        self.Depth2 = params.get("Depth2")
        self.MatchBegin2 = params.get("MatchBegin2")
        self.Str2 = params.get("Str2")
        self.MatchLogic = params.get("MatchLogic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIp(AbstractModel):
    """DDoS regional blocking

    """

    def __init__(self):
        r"""
        :param Switch: Whether to clear the blocklist of the region. Values:
<li>`off`: Clear the blocklist of the region.</li>
<li>`on`: Perform no operations.</li>
        :type Switch: str
        :param RegionIds: Region information. For more information on the ID, see [DescribeSecurityPolicyRegions](https://tcloud4api.woa.com/document/product/1657/81247?!preview&!document=1).
        :type RegionIds: list of int
        """
        self.Switch = None
        self.RegionIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RegionIds = params.get("RegionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSHost(AbstractModel):
    """DDoS protection for the application layer (layer 7)

    """

    def __init__(self):
        r"""
        :param Host: The second-level domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param Status: Status of the domain name. Values:
`init`: NS to be switched
`offline`: Site acceleration not enabled with DNS
`process`: Deployment in progress
`online`: Normal
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param AccelerateType: Site acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `SecurityType`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccelerateType: str
        :param SecurityType: Security acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `AccelerateType`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: str
        """
        self.Host = None
        self.Status = None
        self.AccelerateType = None
        self.SecurityType = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Status = params.get("Status")
        self.AccelerateType = params.get("AccelerateType")
        self.SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSMajorAttackEvent(AbstractModel):
    """The large DDoS attack event

    """

    def __init__(self):
        r"""
        :param PolicyId: The DDoS policy ID.
        :type PolicyId: int
        :param AttackMaxBandWidth: The maximum attack bandwidth.
        :type AttackMaxBandWidth: int
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        """
        self.PolicyId = None
        self.AttackMaxBandWidth = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPacketFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param DDoSFeaturesFilters: Array of feature filtering rules.
        :type DDoSFeaturesFilters: list of DDoSFeaturesFilter
        :param Switch: Whether to clear feature filtering rules. Values:
<li>`off`: Clear feature filtering rules.</li>
<li>`on`: Configure feature filtering rules. In this case, `DDoSFeaturesFilters` needs to be specified.</li>
        :type Switch: str
        """
        self.DDoSFeaturesFilters = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("DDoSFeaturesFilters") is not None:
            self.DDoSFeaturesFilters = []
            for item in params.get("DDoSFeaturesFilters"):
                obj = DDoSFeaturesFilter()
                obj._deserialize(item)
                self.DDoSFeaturesFilters.append(obj)
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSRule(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param DDoSStatusInfo: The DDoS mitigation level. If it is null, the setting that was last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSStatusInfo: :class:`tencentcloud.teo.v20220901.models.DDoSStatusInfo`
        :param DDoSGeoIp: The regional blocking settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSGeoIp: :class:`tencentcloud.teo.v20220901.models.DDoSGeoIp`
        :param DDoSAllowBlock: The IP blocklist/allowlist. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSAllowBlock: :class:`tencentcloud.teo.v20220901.models.DDoSAllowBlock`
        :param DDoSAntiPly: The protocol and connection protection settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSAntiPly: :class:`tencentcloud.teo.v20220901.models.DDoSAntiPly`
        :param DDoSPacketFilter: The feature filtering settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSPacketFilter: :class:`tencentcloud.teo.v20220901.models.DDoSPacketFilter`
        :param DDoSAcl: The port filtering settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSAcl: :class:`tencentcloud.teo.v20220901.models.DDoSAcl`
        :param Switch: Whether to enable DDoS mitigation. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>If it is null, the setting that was last configured will be used.
        :type Switch: str
        :param UdpShardOpen: Whether to enable UDP fragmentation. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>It is required only when used as an output parameter.
        :type UdpShardOpen: str
        :param DDoSSpeedLimit: The settings of the rate limiting rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSSpeedLimit: :class:`tencentcloud.teo.v20220901.models.DDoSSpeedLimit`
        """
        self.DDoSStatusInfo = None
        self.DDoSGeoIp = None
        self.DDoSAllowBlock = None
        self.DDoSAntiPly = None
        self.DDoSPacketFilter = None
        self.DDoSAcl = None
        self.Switch = None
        self.UdpShardOpen = None
        self.DDoSSpeedLimit = None


    def _deserialize(self, params):
        if params.get("DDoSStatusInfo") is not None:
            self.DDoSStatusInfo = DDoSStatusInfo()
            self.DDoSStatusInfo._deserialize(params.get("DDoSStatusInfo"))
        if params.get("DDoSGeoIp") is not None:
            self.DDoSGeoIp = DDoSGeoIp()
            self.DDoSGeoIp._deserialize(params.get("DDoSGeoIp"))
        if params.get("DDoSAllowBlock") is not None:
            self.DDoSAllowBlock = DDoSAllowBlock()
            self.DDoSAllowBlock._deserialize(params.get("DDoSAllowBlock"))
        if params.get("DDoSAntiPly") is not None:
            self.DDoSAntiPly = DDoSAntiPly()
            self.DDoSAntiPly._deserialize(params.get("DDoSAntiPly"))
        if params.get("DDoSPacketFilter") is not None:
            self.DDoSPacketFilter = DDoSPacketFilter()
            self.DDoSPacketFilter._deserialize(params.get("DDoSPacketFilter"))
        if params.get("DDoSAcl") is not None:
            self.DDoSAcl = DDoSAcl()
            self.DDoSAcl._deserialize(params.get("DDoSAcl"))
        self.Switch = params.get("Switch")
        self.UdpShardOpen = params.get("UdpShardOpen")
        if params.get("DDoSSpeedLimit") is not None:
            self.DDoSSpeedLimit = DDoSSpeedLimit()
            self.DDoSSpeedLimit._deserialize(params.get("DDoSSpeedLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimit(AbstractModel):
    """The DDoS rate limits

    """

    def __init__(self):
        r"""
        :param PackageLimit: The limit on origin packet rate. Value range: 1 pps - 1000 Gpps. If 0 is passed, the packet rate will not be restricted.
        :type PackageLimit: str
        :param FluxLimit: The limit on origin traffic rate. Value range: 1 bps - 10000 Gbps. If 0 is passed, the traffic rate will not be restricted.
        :type FluxLimit: str
        """
        self.PackageLimit = None
        self.FluxLimit = None


    def _deserialize(self, params):
        self.PackageLimit = params.get("PackageLimit")
        self.FluxLimit = params.get("FluxLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSStatusInfo(AbstractModel):
    """DDoS protection level

    """

    def __init__(self):
        r"""
        :param PlyLevel: The policy level. Values:
<li>`low`: Loose.</li>
<li>`middle`: Moderate</li>
<li>`high`: Strict</li>
        :type PlyLevel: str
        """
        self.PlyLevel = None


    def _deserialize(self, params):
        self.PlyLevel = params.get("PlyLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Type: Type of the certificate. Values:
<li>`default`: Default certificate;</li>
<li>`upload`: Custom certificate;</li>
<li>`managed`: Tencent Cloud-managed certificate.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param EffectiveTime: Time when the certificate takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EffectiveTime: str
        :param CommonName: Common name of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonName: str
        :param SubjectAltName: Domain names added to the SAN certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param Status: Deployment status. Values:
<li>`processing`: Deployment in progress</li>
<li>`deployed`: Deployed</li>
<li>`failed`: Deployment failed</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param Message: Failure description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param SignAlgo: Certificate algorithm.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SignAlgo: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.EffectiveTime = None
        self.CommonName = None
        self.SubjectAltName = None
        self.Status = None
        self.Message = None
        self.SignAlgo = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.CommonName = params.get("CommonName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasDomainRequest(AbstractModel):
    """DeleteAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param AliasNames: The alias domain name to be deleted. If it is left empty, the delete operation is not performed.
        :type AliasNames: list of str
        """
        self.ZoneId = None
        self.AliasNames = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasDomainResponse(AbstractModel):
    """DeleteAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param RuleId: The rule ID.
        :type RuleId: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record to be deleted.
        :type ZoneId: str
        :param DnsRecordIds: The ID of the DNS record to be deleted.
        :type DnsRecordIds: list of str
        """
        self.ZoneId = None
        self.DnsRecordIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DnsRecordIds = params.get("DnsRecordIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsResponse(AbstractModel):
    """DeleteDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param LoadBalancingId: The load balancer ID.
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancingResponse(AbstractModel):
    """DeleteLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogTopicTaskRequest(AbstractModel):
    """DeleteLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the shipping task to be deleted.
        :type TopicId: str
        :param LogSetRegion: Region of the logset to be shipped. This field is only required when you configure CLS shipping tasks.
        :type LogSetRegion: str
        """
        self.TopicId = None
        self.LogSetRegion = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.LogSetRegion = params.get("LogSetRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogTopicTaskResponse(AbstractModel):
    """DeleteLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param OriginGroupId: The ID of the origin group.
        :type OriginGroupId: str
        """
        self.ZoneId = None
        self.OriginGroupId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginGroupId = params.get("OriginGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOriginGroupResponse(AbstractModel):
    """DeleteOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRulesRequest(AbstractModel):
    """DeleteRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleIds: IDs of the rules to be deleted.
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    """DeleteRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAddableEntityListRequest(AbstractModel):
    """DescribeAddableEntityList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        """
        self.ZoneId = None
        self.EntityType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.EntityType = params.get("EntityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddableEntityListResponse(AbstractModel):
    """DescribeAddableEntityList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param EntityList: List of available shipping entities.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EntityList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.EntityList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.EntityList = params.get("EntityList")
        self.RequestId = params.get("RequestId")


class DescribeAliasDomainsRequest(AbstractModel):
    """DescribeAliasDomains request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`target-name`:<br>   Filter by <strong>target domain name</strong><br>   Type: String<br>   Required: No</li><li>`alias-name`:<br>   Filter by <strong>alias domain name</strong><br>   Type: String<br>   Required: No</li>Only `alias-name` supports fuzzy query.
        :type Filters: list of AdvancedFilter
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasDomainsResponse(AbstractModel):
    """DescribeAliasDomains response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total eligible alias domain names.
        :type TotalCount: int
        :param AliasDomains: Information of the eligible alias domain names.
        :type AliasDomains: list of AliasDomain
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AliasDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AliasDomains") is not None:
            self.AliasDomains = []
            for item in params.get("AliasDomains"):
                obj = AliasDomain()
                obj._deserialize(item)
                self.AliasDomains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxiesRequest(AbstractModel):
    """DescribeApplicationProxies request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The paginated query offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries. <li>`proxy-id`:<br>   Filter by <strong>proxy ID</strong>, such as proxy-ev2sawbwfd<br>   Type: String<br>   Required: No</li><li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-vawer2vadg<br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxiesResponse(AbstractModel):
    """DescribeApplicationProxies response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationProxies: List of application proxies.
        :type ApplicationProxies: list of ApplicationProxy
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationProxies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationProxies") is not None:
            self.ApplicationProxies = []
            for item in params.get("ApplicationProxies"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.ApplicationProxies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans request structure.

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans response structure.

    """

    def __init__(self):
        r"""
        :param PlanInfo: Plans available for the current user
Note: This field may return null, indicating that no valid values can be obtained.
        :type PlanInfo: list of PlanInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PlanInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlanInfo") is not None:
            self.PlanInfo = []
            for item in params.get("PlanInfo"):
                obj = PlanInfo()
                obj._deserialize(item)
                self.PlanInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBotClientIpListRequest(AbstractModel):
    """DescribeBotClientIpList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland).</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotClientIpListResponse(AbstractModel):
    """DescribeBotClientIpList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of client IP data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecClientIp
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecClientIp()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotDataRequest(AbstractModel):
    """DescribeBotData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`bot_interceptNum`: Blocked bot requests;</li>
<li>`bot_noneRequestNum`: Uncategorized bot requests;</li>
<li>`bot_maliciousRequestNum`: Malicious bot requests;</li>
<li>`bot_suspectedRequestNum`: Suspected bot requests;</li>
<li>`bot_friendlyRequestNum`: Friendly bot requests;</li>
<li>`bot_normalRequestNum`: Normal bot requests.</li>
        :type MetricNames: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Domains = None
        self.ZoneIds = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Domains = params.get("Domains")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotDataResponse(AbstractModel):
    """DescribeBotData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotHitRuleDetailRequest(AbstractModel):
    """DescribeBotHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotHitRuleDetailResponse(AbstractModel):
    """DescribeBotHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The hit rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
<li>`sipCountryCode`: The country code of the attacker IP;</li>
<li>`attackIp`: Attacker IP;</li>
<li>`ruleId`: Rule ID;</li>
<li>`eventId`: The event ID;</li>
<li>`ua`: User agent;</li>
<li>`requestMethod`: Request method;</li>
<li>`uri`: Uniform resource identifier.</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotLogResponse(AbstractModel):
    """DescribeBotLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of BotLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BotLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotManagedRulesRequest(AbstractModel):
    """DescribeBotManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param ZoneId: The site ID. You must specify either "ZoneId+Entity" or "TemplateId".
        :type ZoneId: str
        :param Entity: The subdomain name/L4 proxy. You must specify either "ZoneId+Entity" or "TemplateId".
        :type Entity: str
        :param RuleType: The rule type. Values:
<li>`idcid`</li>
<li>`sipbot`</li>
<li>`uabot`</li>If no value or 0 is passed, all rule types will be selected.
        :type RuleType: str
        :param TemplateId: The template ID. You must specify either "ZoneId+Entity" or "TemplateId".
        :type TemplateId: str
        """
        self.Offset = None
        self.Limit = None
        self.ZoneId = None
        self.Entity = None
        self.RuleType = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.RuleType = params.get("RuleType")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotManagedRulesResponse(AbstractModel):
    """DescribeBotManagedRules response structure.

    """

    def __init__(self):
        r"""
        :param Count: Number of bot managed rules returned.
        :type Count: int
        :param BotManagedRuleDetails: The bot managed rule.
        :type BotManagedRuleDetails: list of BotManagedRuleDetail
        :param Total: The total number of bot managed rules.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.BotManagedRuleDetails = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("BotManagedRuleDetails") is not None:
            self.BotManagedRuleDetails = []
            for item in params.get("BotManagedRuleDetails"):
                obj = BotManagedRuleDetail()
                obj._deserialize(item)
                self.BotManagedRuleDetails.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBotTopDataRequest(AbstractModel):
    """DescribeBotTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: List of statistical metric. Values:
<li>`bot_requestNum_labelType`: Top-ranked tag types by bot requests.</li>
<li>`bot_requestNum_url`: Top-ranked URLs by bot requests.</li>
<li>`bot_cipRequestNum_region`: Top-ranked client IPs by bot requests.</li>
        :type MetricName: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Queries the top rows of data. Maximum value: 1000. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotTopDataResponse(AbstractModel):
    """DescribeBotTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClientRuleListRequest(AbstractModel):
    """DescribeClientRuleList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The ID of the site to be queried.
        :type ZoneId: str
        :param Domain: The subdomain name to be queried.
        :type Domain: str
        :param RuleType: Rule type. Values:
<li>`acl`: Custom rules;</li>
<li>`rate`: Rate limiting rules.</li>All rules will be queried if this field is not specified.
        :type RuleType: str
        :param RuleId: The rule ID.
        :type RuleId: int
        :param SourceClientIp: The client IP.
        :type SourceClientIp: str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.ZoneId = None
        self.Domain = None
        self.RuleType = None
        self.RuleId = None
        self.SourceClientIp = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Domain = params.get("Domain")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.SourceClientIp = params.get("SourceClientIp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientRuleListResponse(AbstractModel):
    """DescribeClientRuleList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The blocked client information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ClientRule
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ClientRule()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeContentQuotaRequest(AbstractModel):
    """DescribeContentQuota request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentQuotaResponse(AbstractModel):
    """DescribeContentQuota response structure.

    """

    def __init__(self):
        r"""
        :param PurgeQuota: Purging quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PurgeQuota: list of Quota
        :param PrefetchQuota: Pre-warming quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrefetchQuota: list of Quota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PurgeQuota = None
        self.PrefetchQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeQuota") is not None:
            self.PurgeQuota = []
            for item in params.get("PurgeQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PurgeQuota.append(obj)
        if params.get("PrefetchQuota") is not None:
            self.PrefetchQuota = []
            for item in params.get("PrefetchQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PrefetchQuota.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackDataRequest(AbstractModel):
    """DescribeDDoSAttackData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`ddos_attackMaxBandwidth`: Peak attack bandwidth;</li>
<li>`ddos_attackMaxPackageRate`: Peak attack packet rate;</li>
<li>`ddos_attackBandwidth`: Attack bandwidth;</li>
<li>`ddos_attackPackageRate`: Attack packet rate.</li>
        :type MetricNames: list of str
        :param Port: The port number.
        :type Port: int
        :param AttackType: The attack type. Values:
<li>`flood`: Flood;</li>
<li>`icmpFlood`: ICMP flood;</li>
<li>`all`: All attack types.</li>This field will be set to the default value `all` if not specified.
        :type AttackType: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Port = None
        self.AttackType = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Port = params.get("Port")
        self.AttackType = params.get("AttackType")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackDataResponse(AbstractModel):
    """DescribeDDoSAttackData response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackEventDetailRequest(AbstractModel):
    """DescribeDDoSAttackEventDetail request structure.

    """

    def __init__(self):
        r"""
        :param EventId: The event ID to be queried.
        :type EventId: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.EventId = None
        self.Area = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventDetailResponse(AbstractModel):
    """DescribeDDoSAttackEventDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The details of a DDoS attack event.
        :type Data: :class:`tencentcloud.teo.v20220901.models.DDoSAttackEventDetailData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDoSAttackEventDetailData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackEventRequest(AbstractModel):
    """DescribeDDoSAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param ShowDetail: Whether to display the details.
        :type ShowDetail: bool
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ProtocolType = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Limit = None
        self.Offset = None
        self.ShowDetail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProtocolType = params.get("ProtocolType")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ShowDetail = params.get("ShowDetail")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventResponse(AbstractModel):
    """DescribeDDoSAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSAttackEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSAttackEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceEventRequest(AbstractModel):
    """DescribeDDoSAttackSourceEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ProtocolType = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProtocolType = params.get("ProtocolType")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceEventResponse(AbstractModel):
    """DescribeDDoSAttackSourceEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of DDoS attacker data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSAttackSourceEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSAttackSourceEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackTopDataRequest(AbstractModel):
    """DescribeDDoSAttackTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The statistical metric. Values:
<li>`ddos_attackFlux_protocol`: Top-ranked protocols by DDoS attack traffic.</li>
<li>`ddos_attackPackageNum_protocol`: Top-ranked protocols by DDoS attack packets.</li>
<li>`ddos_attackNum_attackType`: Top-ranked attack types by DDoS attacks.</li>
<li>`ddos_attackNum_sregion`: Top-ranked attack source regions by DDoS attacks.</li>
<li>`ddos_attackFlux_sip`: Top-ranked attacker IPs by DDoS attack traffic.</li>
<li>`ddos_attackFlux_sregion`: Top-ranked attack source regions by DDoS attack traffic.</li>
        :type MetricName: str
        :param ZoneIds: List of site IDs to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param AttackType: The attack type. Values:
<li>`flood`: Flood;</li>
<li>`icmpFlood`: ICMP flood;</li>
<li>`all`: All attack types.</li>This field will be set to the default value `all` if not specified.
        :type AttackType: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Port: The port number.
        :type Port: int
        :param Limit: Queries the top n rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.AttackType = None
        self.ProtocolType = None
        self.Port = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.AttackType = params.get("AttackType")
        self.ProtocolType = params.get("ProtocolType")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackTopDataResponse(AbstractModel):
    """DescribeDDoSAttackTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSBlockListRequest(AbstractModel):
    """DescribeDDoSBlockList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time of the attack event.
        :type StartTime: str
        :param EventIds: The list of attack events.
        :type EventIds: list of str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EventIds = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EventIds = params.get("EventIds")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockListResponse(AbstractModel):
    """DescribeDDoSBlockList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The blocking time of a DDoS attack.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSBlockData
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSBlockData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSMajorAttackEventRequest(AbstractModel):
    """DescribeDDoSMajorAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSMajorAttackEventResponse(AbstractModel):
    """DescribeDDoSMajorAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of large DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSMajorAttackEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSMajorAttackEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param PolicyId: Policy ID
        :type PolicyId: int
        """
        self.ZoneId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param DDoSRule: DDoS mitigation configuration.
        :type DDoSRule: :class:`tencentcloud.teo.v20220901.models.DDoSRule`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DDoSRule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDoSRule") is not None:
            self.DDoSRule = DDoSRule()
            self.DDoSRule._deserialize(params.get("DDoSRule"))
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter criteria. Each filter criteria can have up to 5 entries.
<li>`zone-id`: <br>Filter by <strong>site ID</strong>, such as zone-xxx<br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        :param Offset: Offset for paginated queries. Default value: `0`
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of certificates
        :type TotalCount: int
        :param DefaultServerCertInfo: List of default certificates
        :type DefaultServerCertInfo: list of DefaultServerCertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DefaultServerCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DefaultServerCertInfo") is not None:
            self.DefaultServerCertInfo = []
            for item in params.get("DefaultServerCertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.DefaultServerCertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone`:<br>   Filter by <strong>site name</strong>, such as tencent.com (up to one entry)<br>   Type: String<br>   Required: No
<li>`host`:<br>   Filter by <strong>domain name</strong>, such as test.tencent.com (up to one entry)<br>   Type: String<br>   Required: No
<li>`type`:<br>   Filter by <strong>DNS record type</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `A`: A record<br>   `AAAA`: AAAA record<br>   `CNAME`: CNAME record<br>   `MX`: MX record<br>   `TXT`: TXT record<br>   `NS`: NS record<br>   `SRV`: SRV record<br>   `CAA`: CAA record
<li>`code`:<br>   Filter by <strong>DNS status code</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `NoError`: Success<br>   `NXDomain`: Not found the request domain<br>   `NotImp`: Not supported request type<br>   `Refused`: The domain name server refuses to execute the request for policy reasons
<li>`area`:<br>   Filter by <strong>DNS region</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `Asia`<br>   `Europe`<br>   `Africa`<br>   `Oceania`<br>   `Americas`
        :type Filters: list of Filter
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>This field will be set to the default value `min` if not specified.
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsDataResponse(AbstractModel):
    """DescribeDnsData response structure.

    """

    def __init__(self):
        r"""
        :param Data: DNS statistics.
        :type Data: list of DnsData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DnsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record. All sites’ DNS records will be returned if this field is not specified.
        :type ZoneId: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`record-id`:<br>   Filter by <strong>DNS record ID</strong>, such as record-1a8df68z<br>   Type: String<br>Required: No
<li>`record-name`:<br>   Filter by <strong>DNS record name</strong><br>   Type: String<br>Required: No
<li>`record-type`:<br>   Filter by <strong>DNS record type</strong><br>   Type: String<br>Required: No<br>   Values:<br>   `A`: Point a domain name to an IPv4 address, such as 8.8.8.8.<br>   `AAAA`: Point a domain name to an IPv6 address.<br>   `CNAME`: Point a domain name to another domain name that can be resolved to an IP address.<br>   `TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).<br>   `NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.<br>   `CAA`: Specify CAs to issue certificates for sites.<br>   `SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.<br>  `MX`: Specify the mail server for receiving emails.
<li>`mode`:<br>   Filter by <strong>proxy mode</strong><br>   Type: String<br>Required: No<br>   Values:<br>   `dns_only`: Only DNS<br>   `proxied`: Proxied
<li>`ttl`:<br>   Filter by <strong>TTL</strong><br>   Type: String<br>Required: No
        :type Filters: list of AdvancedFilter
        :param Direction: The sorting order. Values:
<li>`ASC`: Ascending order</li>
<li>`desc`: Descending order</li> Default value: asc
        :type Direction: str
        :param Match: The match mode. Values:
<li>`all`: Return all records that match the specified filter.</li>
<li>`any`: Return any record that matches the specified filter.</li>Default value: all.
        :type Match: str
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Order: The sorting criteria. Values:
<li>`content`: DNS record content.</li>
<li>`created_on`: Creation time of the DNS record.</li>
<li>`mode`: Proxy mode.</li>
<li>`record-name`: DNS record name.</li>
<li>`ttl`: DNS TTL.</li>
<li>`record-type`: DNS record type.</li>If this field is not specified, the DNS records are sorted based on `record-type` and `recrod-name`.
        :type Order: str
        """
        self.ZoneId = None
        self.Filters = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsRecordsResponse(AbstractModel):
    """DescribeDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of DNS records.
        :type TotalCount: int
        :param DnsRecords: List of DNS records
        :type DnsRecords: list of DnsRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DnsRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DnsRecords") is not None:
            self.DnsRecords = []
            for item in params.get("DnsRecords"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.DnsRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnssecResponse(AbstractModel):
    """DescribeDnssec response structure.

    """

    def __init__(self):
        r"""
        :param Status: The DNSSEC status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        :param DnssecInfo: The DNSSEC information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DnssecInfo: :class:`tencentcloud.teo.v20220901.models.DnssecInfo`
        :param ModifiedOn: The update time of the site information.
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.DnssecInfo = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("DnssecInfo") is not None:
            self.DnssecInfo = DnssecInfo()
            self.DnssecInfo._deserialize(params.get("DnssecInfo"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0. Minimum value: 0.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`host`:<br>   Filter by <strong>domain name </strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting response structure.

    """

    def __init__(self):
        r"""
        :param DetailHosts: List of domain names.
        :type DetailHosts: list of DetailHost
        :param TotalNumber: Number of domain names
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailHosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailHosts") is not None:
            self.DetailHosts = []
            for item in params.get("DetailHosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.DetailHosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationsRequest(AbstractModel):
    """DescribeIdentifications request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-name`: <br>Filter by <strong>site name</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationsResponse(AbstractModel):
    """DescribeIdentifications response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param Identifications: The site verification information.
        :type Identifications: list of Identification
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Identifications = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Identifications") is not None:
            self.Identifications = []
            for item in params.get("Identifications"):
                obj = Identification()
                obj._deserialize(item)
                self.Identifications.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for paginated queries. Default value: 0.
        :type Offset: int
        :param Limit: Limit on paginated queries. Value range: 1-1000. Default value: 10.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-1a8df68z<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported
</li><li>`load-balancing-id`<br>   Filter by <strong>load balancer ID</strong>, such as lb-d21bfaf7-8d72-11ec-841d-00ff977fb3c8<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported
</li><li>`host`:<br>   Filter by <strong>load balancing hostname</strong>, such as lb.tencent.com<br>   Type: String<br>   Required: No<br>   Fuzzy query: Supported (only one hostname allowed in a query)</li>
        :type Filters: list of AdvancedFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingResponse(AbstractModel):
    """DescribeLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param Data: Load balancer information.
        :type Data: list of LoadBalancing
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LoadBalancing()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogSetsRequest(AbstractModel):
    """DescribeLogSets request structure.

    """

    def __init__(self):
        r"""
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        """
        self.LogSetRegion = None
        self.LogSetId = None
        self.LogSetName = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetId = params.get("LogSetId")
        self.LogSetName = params.get("LogSetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSetsResponse(AbstractModel):
    """DescribeLogSets response structure.

    """

    def __init__(self):
        r"""
        :param LogSetList: List of logsets.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetList: list of LogSetInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogSetList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogSetList") is not None:
            self.LogSetList = []
            for item in params.get("LogSetList"):
                obj = LogSetInfo()
                obj._deserialize(item)
                self.LogSetList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLogTopicTaskDetailRequest(AbstractModel):
    """DescribeLogTopicTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the shipping task.
        :type TopicId: str
        :param ZoneId: ID of the site.
        :type ZoneId: str
        """
        self.TopicId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTopicTaskDetailResponse(AbstractModel):
    """DescribeLogTopicTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param LogTopicDetailInfo: The shipping task details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogTopicDetailInfo: :class:`tencentcloud.teo.v20220901.models.LogTopicDetailInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogTopicDetailInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogTopicDetailInfo") is not None:
            self.LogTopicDetailInfo = LogTopicDetailInfo()
            self.LogTopicDetailInfo._deserialize(params.get("LogTopicDetailInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLogTopicTasksRequest(AbstractModel):
    """DescribeLogTopicTasks request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Offset: Page offset. Default value: 0.
        :type Offset: int
        """
        self.ZoneId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTopicTasksResponse(AbstractModel):
    """DescribeLogTopicTasks response structure.

    """

    def __init__(self):
        r"""
        :param TopicList: List of shipping tasks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of ClsLogTopicInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ClsLogTopicInfo()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for paginated queries. Default value: 0.
        :type Offset: int
        :param Limit: Limit on paginated queries. Value range: 1-1000. Default value: 10.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-id`<br>   Filter by <strong>site ID</strong>, such as zone-20hzkd4rdmy0<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`origin-group-id`:<br>   Filter by <strong>origin group ID</strong>, such as origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`origin-group-name`:<br>   Filter by <strong>origin group name</strong><br>   Type: String<br>   Required: No<br>   Fuzzy query: Supported (only one origin group name allowed in a query)
        :type Filters: list of AdvancedFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupResponse(AbstractModel):
    """DescribeOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param OriginGroups: Origin group information.
        :type OriginGroups: list of OriginGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.OriginGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OriginGroups") is not None:
            self.OriginGroups = []
            for item in params.get("OriginGroups"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.OriginGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Flow_outFlux`: Access traffic;</li>
<li>`l7Flow_request`: Access requests;</li>
<li>`l7Flow_outBandwidth`: Access bandwidth.</li>
<li>`l7Flow_hit_outFlux`: Cache hit traffic.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Protocol: The protocol type. Values:
<li>`http`: HTTP protocol;</li>
<li>`https`: HTTPS protocol;</li>
<li>`http2`: HTTP2 protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type Protocol: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`tagKey`:<br>   Filter by <strong>tag key</strong><br>   Type: String<br>   Required: No</li>
<li>`tagValue`<br>  Filter by <strong>tag value</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None
        self.Interval = None
        self.Area = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L7 traffic summary statistics recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the query.
        :type StartTime: str
        :param EndTime: End time of the query.
        :type EndTime: str
        :param Offset: Offset for paginated queries. Default value: `0`.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-1379afjk91u32h (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`job-id`:<br>   Filter by <strong>task ID</strong>, such as 1379afjk91u32h (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`target`:<br>   Filter by <strong>target resource</strong>, such as http://www.qq.com/1.txt (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`domains`:<br>   Filter by <strong>domain name</strong>, such as www.qq.com<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`statuses`:<br>   Filter by <strong>task status</strong><br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `processing`: The task is in progress.<br>   `success`: The task succeeded.<br>   `failed`: The task failed.<br>   `timeout`: The task timed out.</li>
        :type Filters: list of AdvancedFilter
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition.
        :type TotalCount: int
        :param Tasks: List of tasks returned.
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Disused. Use "zone-id" in "Filters" instead.
        :type ZoneId: str
        :param StartTime: Start time of the query.
        :type StartTime: str
        :param EndTime: End time of the query.
        :type EndTime: str
        :param Offset: Offset for paginated queries. Default value: `0`.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries. <li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-xxx (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`job-id`:<br>   Filter by <strong>task ID</strong>, such as 1379afjk91u32h (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`target`:<br>   Filter by <strong>target resource</strong>, such as http://www.qq.com/1.txt and tag1<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`domains`:<br>   Filter by <strong>domain name</strong>, such as www.qq.com<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported</li><li>`statuses`:<br>   Filter by <strong>task status</strong><br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `processing`: The task is in progress.<br>   `success`: The task succeeded.<br>   `failed`: The task failed.<br>   `timeout`: The task timed out.<li>`type`:<br>   Filter by <strong>purging mode</strong> (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `purge_url`: Purge by URL.<br>   `purge_prefix`: Purge by prefix.<br>   `purge_all`: Purge all caches.<br>   `purge_host`: Purge by hostname.<br>   `purge_cache_tag`: Purge by cache tag.</li>
        :type Filters: list of AdvancedFilter
        """
        self.ZoneId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition.
        :type TotalCount: int
        :param Tasks: List of tasks returned.
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRateLimitIntelligenceRuleRequest(AbstractModel):
    """DescribeRateLimitIntelligenceRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name/layer-4 proxy.
        :type Entity: str
        """
        self.ZoneId = None
        self.Entity = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRateLimitIntelligenceRuleResponse(AbstractModel):
    """DescribeRateLimitIntelligenceRule response structure.

    """

    def __init__(self):
        r"""
        :param RateLimitIntelligenceRuleDetails: The intelligent rate limiting rule.
        :type RateLimitIntelligenceRuleDetails: list of RateLimitIntelligenceRuleDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RateLimitIntelligenceRuleDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RateLimitIntelligenceRuleDetails") is not None:
            self.RateLimitIntelligenceRuleDetails = []
            for item in params.get("RateLimitIntelligenceRuleDetails"):
                obj = RateLimitIntelligenceRuleDetail()
                obj._deserialize(item)
                self.RateLimitIntelligenceRuleDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`rule-id`:<br>   Filter by the <strong>rule ID</strong><br>   Type: string<br>   Required: No
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleItems: List of rules. Rules are sorted in order of execution.
        :type RuleItems: list of RuleItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RuleItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("RuleItems") is not None:
            self.RuleItems = []
            for item in params.get("RuleItems"):
                obj = RuleItem()
                obj._deserialize(item)
                self.RuleItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesSettingRequest(AbstractModel):
    """DescribeRulesSetting request structure.

    """


class DescribeRulesSettingResponse(AbstractModel):
    """DescribeRulesSetting response structure.

    """

    def __init__(self):
        r"""
        :param Actions: List of the settings of the rule engine that can be used for request match and their detailed recommended configuration information.
        :type Actions: list of RulesSettingAction
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Actions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = RulesSettingAction()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupManagedRulesRequest(AbstractModel):
    """DescribeSecurityGroupManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID. You must specify either "ZoneId+Entity" or "TemplateId".
        :type ZoneId: str
        :param Entity: The subdomain name/L4 proxy. You must specify either "ZoneId+Entity" or "TemplateId".
        :type Entity: str
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param TemplateId: The template ID. You must specify either this field or ZoneId+Entity".
        :type TemplateId: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Offset = None
        self.Limit = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupManagedRulesResponse(AbstractModel):
    """DescribeSecurityGroupManagedRules response structure.

    """

    def __init__(self):
        r"""
        :param Count: The number of bot managed rules returned.
        :type Count: int
        :param Total: The total number of rules.
        :type Total: int
        :param WafGroupInfo: Details of the managed rule.
        :type WafGroupInfo: :class:`tencentcloud.teo.v20220901.models.WafGroupInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.Total = None
        self.WafGroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Total = params.get("Total")
        if params.get("WafGroupInfo") is not None:
            self.WafGroupInfo = WafGroupInfo()
            self.WafGroupInfo._deserialize(params.get("WafGroupInfo"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyListRequest(AbstractModel):
    """DescribeSecurityPolicyList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyListResponse(AbstractModel):
    """DescribeSecurityPolicyList response structure.

    """

    def __init__(self):
        r"""
        :param SecurityEntities: List of protected resources
        :type SecurityEntities: list of SecurityEntity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityEntities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityEntities") is not None:
            self.SecurityEntities = []
            for item in params.get("SecurityEntities"):
                obj = SecurityEntity()
                obj._deserialize(item)
                self.SecurityEntities.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRegionsRequest(AbstractModel):
    """DescribeSecurityPolicyRegions request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyRegionsResponse(AbstractModel):
    """DescribeSecurityPolicyRegions response structure.

    """

    def __init__(self):
        r"""
        :param Count: Total number of regions.
        :type Count: int
        :param GeoIps: Region information.
        :type GeoIps: list of GeoIp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.GeoIps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("GeoIps") is not None:
            self.GeoIps = []
            for item in params.get("GeoIps"):
                obj = GeoIp()
                obj._deserialize(item)
                self.GeoIps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRequest(AbstractModel):
    """DescribeSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name/L4 proxy. You must specify either "Entity" or "TemplateId".
        :type Entity: str
        :param TemplateId: The template ID. You must specify either this field or "Entity".
        :type TemplateId: str
        """
        self.ZoneId = None
        self.Entity = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyResponse(AbstractModel):
    """DescribeSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param SecurityConfig: Security configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityConfig: :class:`tencentcloud.teo.v20220901.models.SecurityConfig`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityPortraitRulesRequest(AbstractModel):
    """DescribeSecurityPortraitRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID. You must specify either "ZoneId+Entity" or "TemplateId".
        :type ZoneId: str
        :param Entity: The subdomain name/L4 proxy. You must specify either "ZoneId+Entity" or "TemplateId".
        :type Entity: str
        :param TemplateId: The template ID. You must specify either this field or "ZoneId+Entity". 
        :type TemplateId: str
        """
        self.ZoneId = None
        self.Entity = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPortraitRulesResponse(AbstractModel):
    """DescribeSecurityPortraitRules response structure.

    """

    def __init__(self):
        r"""
        :param Count: The number of rules returned.
        :type Count: int
        :param PortraitManagedRuleDetails: The bot client reputation rule.
        :type PortraitManagedRuleDetails: list of PortraitManagedRuleDetail
        :param Total: The total number of rules.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.PortraitManagedRuleDetails = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("PortraitManagedRuleDetails") is not None:
            self.PortraitManagedRuleDetails = []
            for item in params.get("PortraitManagedRuleDetails"):
                obj = PortraitManagedRuleDetail()
                obj._deserialize(item)
                self.PortraitManagedRuleDetails.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeSecurityRuleIdRequest(AbstractModel):
    """DescribeSecurityRuleId request structure.

    """

    def __init__(self):
        r"""
        :param RuleIdList: Array of rule IDs.
        :type RuleIdList: list of int
        :param RuleType: Rule type. Values:
<li>`waf`: Web managed rules</li>
<li>`acl`: Custom rules</li>
<li>`rate`: Rate limiting rules</li>
<li>`bot`: Bot managed rules</li>
        :type RuleType: str
        :param Entity: The subdomain name/layer-4 proxy.
        :type Entity: str
        """
        self.RuleIdList = None
        self.RuleType = None
        self.Entity = None


    def _deserialize(self, params):
        self.RuleIdList = params.get("RuleIdList")
        self.RuleType = params.get("RuleType")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityRuleIdResponse(AbstractModel):
    """DescribeSecurityRuleId response structure.

    """

    def __init__(self):
        r"""
        :param WafGroupRules: List of rules.
        :type WafGroupRules: list of WafGroupRule
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WafGroupRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WafGroupRules") is not None:
            self.WafGroupRules = []
            for item in params.get("WafGroupRules"):
                obj = WafGroupRule()
                obj._deserialize(item)
                self.WafGroupRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSingleL7AnalysisDataRequest(AbstractModel):
    """DescribeSingleL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Flow_singleIpRequest`: Number of requests from a single IP.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSingleL7AnalysisDataResponse(AbstractModel):
    """DescribeSingleL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L7 dimensional data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SingleDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SingleDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingDetailsRequest(AbstractModel):
    """DescribeSpeedTestingDetails request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpeedTestingDetailsResponse(AbstractModel):
    """DescribeSpeedTestingDetails response structure.

    """

    def __init__(self):
        r"""
        :param SpeedTestingDetailData: The site’s load speed across regions.
        :type SpeedTestingDetailData: :class:`tencentcloud.teo.v20220901.models.SpeedTestingDetailData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpeedTestingDetailData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingDetailData") is not None:
            self.SpeedTestingDetailData = SpeedTestingDetailData()
            self.SpeedTestingDetailData._deserialize(params.get("SpeedTestingDetailData"))
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingMetricDataRequest(AbstractModel):
    """DescribeSpeedTestingMetricData request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpeedTestingMetricDataResponse(AbstractModel):
    """DescribeSpeedTestingMetricData response structure.

    """

    def __init__(self):
        r"""
        :param SpeedTestingMetricData: The site test metrics.
        :type SpeedTestingMetricData: :class:`tencentcloud.teo.v20220901.models.SpeedTestingMetricData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpeedTestingMetricData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingMetricData") is not None:
            self.SpeedTestingMetricData = SpeedTestingMetricData()
            self.SpeedTestingMetricData._deserialize(params.get("SpeedTestingMetricData"))
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingQuotaRequest(AbstractModel):
    """DescribeSpeedTestingQuota request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpeedTestingQuotaResponse(AbstractModel):
    """DescribeSpeedTestingQuota response structure.

    """

    def __init__(self):
        r"""
        :param SpeedTestingQuota: The quota limit on site tests.
        :type SpeedTestingQuota: :class:`tencentcloud.teo.v20220901.models.SpeedTestingQuota`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SpeedTestingQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingQuota") is not None:
            self.SpeedTestingQuota = SpeedTestingQuota()
            self.SpeedTestingQuota._deserialize(params.get("SpeedTestingQuota"))
        self.RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: Metric to query. Values:
<li>`l4Flow_connections`: Access connections;</li>
<li>`l4Flow_flux`: Access traffic;</li>
<li>`l4Flow_inFlux`: Inbound traffic;</li>
<li>`l4Flow_outFlux`: Outbound traffic;</li>
<li>`l4Flow_outPkt`: Outbound packets.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param ProxyIds: List of L4 proxy IDs. All L4 proxies will be selected if this field is not specified.
        :type ProxyIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`ruleId`: Filter by rule ID;</li>
<li>`proxyId`: Filter by connection ID.</li>
        :type Filters: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L4 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The list of metrics. Values:
<li>`l7Flow_outFlux`: Access traffic;</li>
<li>`l7Flow_request`: Access requests;</li>
<li>`l7Flow_outBandwidth`: Access bandwidth.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`resourceType`: Resource type;</li>
<li>`statusCode`: Status code;</li>
<li>`browserType`: Browser type;</li>
<li>`deviceType`: Device type;</li>
<li>`operatingSystemType`: OS type;</li>
<li>`tlsVersion`: TLS version;</li>
<li>`url`: URL address;</li>
<li>`referer`: Refer header;</li>
<li>`ipVersion`: IP version;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L7 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Cache_outFlux`: Response traffic.</li>
<li>`l7Cache_request`: Response requests.</li>
<li>`l7Cache_outBandwidth`: Response bandwidth.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`cacheType`: Cache type;</li>
<li>`domain`: Host/domain name;</li>
<li>`resourceType`: Resource type;</li>
<li>`url`: URL address;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of cached L7 time-series data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The query metric. Values:
<li>`l7Flow_outFlux_country`: Country the request came from;</li>
<li>`l7Flow_outFlux_statusCode`: Status code of the request;</li>
<li>`l7Flow_outFlux_domain`: Domain name of the request;</li>
<li>`l7Flow_outFlux_url`: URL of the request;</li>
<li>`l7Flow_outFlux_resourceType`: Resource type;</li>
<li>`l7Flow_outFlux_sip`: Client IP;</li>
<li>`l7Flow_outFlux_referers`: Refer header;</li>
<li>`l7Flow_outFlux_ua_device`: Device type;</li>
<li>`l7Flow_outFlux_ua_browser`: Browser type;</li>
<li>`l7Flow_outFlux_us_os`: OS type;</li>
        :type MetricName: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Queries the top n rows of data. Maximum value: 1000. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`resourceType`: Resource type;</li>
<li>`statusCode`: Status code;</li>
<li>`browserType`: Browser type;</li>
<li>`deviceType`: Device type;</li>
<li>`operatingSystemType`: OS type;</li>
<li>`tlsVersion`: TLS version;</li>
<li>`url`: URL address;</li>
<li>`referer`: Refer header;</li>
<li>`ipVersion`: IP version;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked L7 traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The query metric. Values:
<li>`l7Cache_outFlux_domain`: Host/Domain name;</li>
<li>`l7Cache_outFlux_url`: URL address;</li>
<li>`l7Cache_outFlux_resourceType`: Resource type;</li>
<li>`l7Cache_outFlux_statusCode`: Status code.</li>
        :type MetricName: str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Queries the top rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`cacheType`: Cache type;</li>
<li>`domain`: Host/domain name;</li>
<li>`resourceType`: Resource type;</li>
<li>`url`: URL address;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of cached L7 top-ranked traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`waf_interceptNum`: Requests blocked by WAF.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesDataResponse(AbstractModel):
    """DescribeWebManagedRulesData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of WAF attack data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesHitRuleDetailRequest(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesHitRuleDetailResponse(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The hit rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`attackType`: Attack type;</li>
<li>`riskLevel`: Risk level;</li>
<li>`action`: Action;</li>
<li>`ruleId`: Rule ID;</li>
<li>`sipCountryCode`: Country code of the attacker IP;</li>
<li>`attackIp`: Attacker IP;</li>
<li>`oriDomain`: Attacked subdomain name;</li>
<li>`eventId`: Event ID;</li>
<li>`ua`: User agent;</li>
<li>`requestMethod`: Request method;</li>
<li>`uri`: Uniform resource identifier.</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesLogResponse(AbstractModel):
    """DescribeWebManagedRulesLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of web log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of WebLogs
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WebLogs()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionAttackEventsRequest(AbstractModel):
    """DescribeWebProtectionAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionAttackEventsResponse(AbstractModel):
    """DescribeWebProtectionAttackEvents response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC attack events.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of CCInterceptEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CCInterceptEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionClientIpListRequest(AbstractModel):
    """DescribeWebProtectionClientIpList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionClientIpListResponse(AbstractModel):
    """DescribeWebProtectionClientIpList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC attacker IPs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecClientIp
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecClientIp()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: Metrics to query. Values:
<li>`ccRate_interceptNum`: Requests restricted by the rate limiting rules;</li>
<li>`ccAcl_interceptNum`: Requests restricted by the custom rules.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionDataResponse(AbstractModel):
    """DescribeWebProtectionData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC protection data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionHitRuleDetailRequest(AbstractModel):
    """DescribeWebProtectionHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param EntityType: The rule type. Values:
<li>`rate`: Rate limiting rules;</li>
<li>`acl`: Custom rules.</li>
        :type EntityType: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.EntityType = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EntityType = params.get("EntityType")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionHitRuleDetailResponse(AbstractModel):
    """DescribeWebProtectionHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of hit CC protection rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionTopDataRequest(AbstractModel):
    """DescribeWebProtectionTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: List of statistical metric. Values:
<li>`ccRate_requestNum_url`: Top-ranked URLs by rate limiting requests.</li>
<li>`ccRate_cipRequestNum_region`: Top-ranked client IPs by rate limiting requests.</li>
<li>`ccAcl_requestNum_url`: Top-ranked URLs by custom rule requests.</li>
<li>`ccAcl_requestNum_cip`: Top-ranked client IPs by custom rule execution requests.</li>
<li>`ccAcl_cipRequestNum_region`: Top-ranked clients by custom rule execution requests.</li>
        :type MetricName: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Queries the top n rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionTopDataResponse(AbstractModel):
    """DescribeWebProtectionTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked CC protection data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeZoneDDoSPolicyRequest(AbstractModel):
    """DescribeZoneDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDDoSPolicyResponse(AbstractModel):
    """DescribeZoneDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param ShieldAreas: DDoS mitigation configuration.
        :type ShieldAreas: list of ShieldArea
        :param DDoSHosts: Information of the proxied subdomain names.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSHosts: list of DDoSHost
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ShieldAreas = None
        self.DDoSHosts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ShieldAreas") is not None:
            self.ShieldAreas = []
            for item in params.get("ShieldAreas"):
                obj = ShieldArea()
                obj._deserialize(item)
                self.ShieldAreas.append(obj)
        if params.get("DDoSHosts") is not None:
            self.DDoSHosts = []
            for item in params.get("DDoSHosts"):
                obj = DDoSHost()
                obj._deserialize(item)
                self.DDoSHosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param ZoneSetting: The site configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneSetting: :class:`tencentcloud.teo.v20220901.models.ZoneSetting`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneSetting = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneSetting") is not None:
            self.ZoneSetting = ZoneSetting()
            self.ZoneSetting._deserialize(params.get("ZoneSetting"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-name`:<br>   Filter by <strong>site name</strong><br>   Type: String<br>   Required: No</li><li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-xxx<br>   Type: String<br>   Required: No</li><li>`status`:<br>   Filter by <strong>site status</strong><br>   Type: String<br>   Required: No</li><li>`tag-key`:<br>   Filter by <strong>tag key</strong><br>   Type: String<br>   Required: No</li><li>`tag-value`:<br>   Filter by <strong>tag value</strong><br>   Type: String<br>   Required: No</li>Only `zone-name` supports fuzzy query.
        :type Filters: list of AdvancedFilter
        :param Order: The sorting field. Values:
<li>`type`: Access mode</li>
<li>`area`: Acceleration region</li>
<li>`create-time`: Creation date</li>
<li>`zone-name`: Site name</li>
<li>`use-time`: Last used date</li>
<li>`active-status`: Activation status</li>If it is left empty, the default value `create-time` is used.
        :type Order: str
        :param Direction: The sorting direction. Values:
<li>`asc`: From smallest to largest</li>
<li>`desc`: From largest to smallest</li>If it is left empty, the default value `desc` is used.
        :type Direction: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Order = None
        self.Direction = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param Zones: Details of sites
        :type Zones: list of Zone
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """Domain name configuration information

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The acceleration status. Values:
<li>`process`: In progress</li>
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
        :type Status: str
        :param Host: The domain name.
        :type Host: str
        :param ZoneName: Name of the site
        :type ZoneName: str
        :param Cname: The assigned CNAME
        :type Cname: str
        :param Id: The resource ID.
        :type Id: str
        :param InstanceId: The instance ID.
        :type InstanceId: str
        :param Lock: The lock status.
        :type Lock: int
        :param Mode: The domain name status.
        :type Mode: int
        :param Area: The acceleration area of the domain name. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param AccelerateType: The acceleration type configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccelerateType: :class:`tencentcloud.teo.v20220901.models.AccelerateType`
        :param Https: The HTTPS configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param CacheConfig: The cache configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: The origin configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SecurityType: The security type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: :class:`tencentcloud.teo.v20220901.models.SecurityType`
        :param CacheKey: The cache key configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Compression: The smart compression configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param Waf: The WAF protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Waf: :class:`tencentcloud.teo.v20220901.models.Waf`
        :param CC: The CC protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CC: :class:`tencentcloud.teo.v20220901.models.CC`
        :param DDoS: DDoS mitigation configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoS: :class:`tencentcloud.teo.v20220901.models.DDoS`
        :param SmartRouting: The smart routing configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param Ipv6: The IPv6 access configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: Whether to carry the location information of the client IP during origin-pull.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneId = None
        self.Status = None
        self.Host = None
        self.ZoneName = None
        self.Cname = None
        self.Id = None
        self.InstanceId = None
        self.Lock = None
        self.Mode = None
        self.Area = None
        self.AccelerateType = None
        self.Https = None
        self.CacheConfig = None
        self.Origin = None
        self.SecurityType = None
        self.CacheKey = None
        self.Compression = None
        self.Waf = None
        self.CC = None
        self.DDoS = None
        self.SmartRouting = None
        self.Ipv6 = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.Lock = params.get("Lock")
        self.Mode = params.get("Mode")
        self.Area = params.get("Area")
        if params.get("AccelerateType") is not None:
            self.AccelerateType = AccelerateType()
            self.AccelerateType._deserialize(params.get("AccelerateType"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SecurityType") is not None:
            self.SecurityType = SecurityType()
            self.SecurityType._deserialize(params.get("SecurityType"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("Waf") is not None:
            self.Waf = Waf()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self.CC = CC()
            self.CC._deserialize(params.get("CC"))
        if params.get("DDoS") is not None:
            self.DDoS = DDoS()
            self.DDoS._deserialize(params.get("DDoS"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistrictStatistics(AbstractModel):
    """The site’s load speed across regions

    """

    def __init__(self):
        r"""
        :param Alpha2: The ISO 3166-2 Alpha-2 country code. For the list of country codes, see [ISO 3166-2](https://zh.m.wikipedia.org/zh-hans/ISO_3166-2).
        :type Alpha2: str
        :param LoadTime: The overall load time, in milliseconds.
        :type LoadTime: int
        """
        self.Alpha2 = None
        self.LoadTime = None


    def _deserialize(self, params):
        self.Alpha2 = params.get("Alpha2")
        self.LoadTime = params.get("LoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsData(AbstractModel):
    """DNS data points

    """

    def __init__(self):
        r"""
        :param Time: The time.
        :type Time: str
        :param Value: The value.
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecord(AbstractModel):
    """DNS record

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The record ID.
        :type DnsRecordId: str
        :param DnsRecordType: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type DnsRecordType: str
        :param DnsRecordName: The record name.
        :type DnsRecordName: str
        :param Content: The record value.
        :type Content: str
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Mode: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect.
        :type TTL: int
        :param Priority: The MX record priority. The smaller the value, the higher the priority.
        :type Priority: int
        :param CreatedOn: The creation time.
        :type CreatedOn: str
        :param ModifiedOn: The modification time.
        :type ModifiedOn: str
        :param Locked: The lock status of the domain name.
        :type Locked: bool
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Status: The DNS record status. Values:
<li>`active`: Activated</li>
<li>`pending`: Deactivated</li>
        :type Status: str
        :param Cname: The CNAME address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param DomainStatus: The service used by the domain name. Values:
<li>`lb`: Load balancing</li>
<li>`security`: Security protection</li>
<li>`l4`: L4 proxy</li>
        :type DomainStatus: list of str
        """
        self.DnsRecordId = None
        self.DnsRecordType = None
        self.DnsRecordName = None
        self.Content = None
        self.Mode = None
        self.TTL = None
        self.Priority = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Locked = None
        self.ZoneId = None
        self.ZoneName = None
        self.Status = None
        self.Cname = None
        self.DomainStatus = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.DnsRecordType = params.get("DnsRecordType")
        self.DnsRecordName = params.get("DnsRecordName")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Locked = params.get("Locked")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.DomainStatus = params.get("DomainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnssecInfo(AbstractModel):
    """DNSSEC information

    """

    def __init__(self):
        r"""
        :param Flags: Flag
        :type Flags: int
        :param Algorithm: Encryption algorithm
        :type Algorithm: str
        :param KeyType: Encryption type
        :type KeyType: str
        :param DigestType: Digest type
        :type DigestType: str
        :param DigestAlgorithm: Digest algorithm
        :type DigestAlgorithm: str
        :param Digest: Digest message
        :type Digest: str
        :param DS: DS record value
        :type DS: str
        :param KeyTag: Key tag
        :type KeyTag: int
        :param PublicKey: Public key
        :type PublicKey: str
        """
        self.Flags = None
        self.Algorithm = None
        self.KeyType = None
        self.DigestType = None
        self.DigestAlgorithm = None
        self.Digest = None
        self.DS = None
        self.KeyTag = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.Flags = params.get("Flags")
        self.Algorithm = params.get("Algorithm")
        self.KeyType = params.get("KeyType")
        self.DigestType = params.get("DigestType")
        self.DigestAlgorithm = params.get("DigestAlgorithm")
        self.Digest = params.get("Digest")
        self.DS = params.get("DS")
        self.KeyTag = params.get("KeyTag")
        self.PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsRequest(AbstractModel):
    """DownloadL4Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param ProxyIds: List of L4 proxy IDs.
        :type ProxyIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsResponse(AbstractModel):
    """DownloadL4Logs response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L4 log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of L4OfflineLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L4OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L7 log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of L7OfflineLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DropPageConfig(AbstractModel):
    """Block page configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param WafDropPageDetail: The settings of the block page that applies managed rules. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WafDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        :param AclDropPageDetail: The settings of the block page that applies custom rules. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AclDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        """
        self.Switch = None
        self.WafDropPageDetail = None
        self.AclDropPageDetail = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("WafDropPageDetail") is not None:
            self.WafDropPageDetail = DropPageDetail()
            self.WafDropPageDetail._deserialize(params.get("WafDropPageDetail"))
        if params.get("AclDropPageDetail") is not None:
            self.AclDropPageDetail = DropPageDetail()
            self.AclDropPageDetail._deserialize(params.get("AclDropPageDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropPageDetail(AbstractModel):
    """The configuration details of the block page

    """

    def __init__(self):
        r"""
        :param PageId: The ID of the block page, which can be obtained from the CreateSecurityDropPage API.
If 0 is passed, the default block page will be used.
        :type PageId: int
        :param StatusCode: The HTTP status code of the block page. Value range: 100-600.
        :type StatusCode: int
        :param Name: The block page file or URL.
        :type Name: str
        :param Type: Type of the block page. Values:
<li>`file`: Block page file</li>
<li>`url`: Block page URL</li>
        :type Type: str
        """
        self.PageId = None
        self.StatusCode = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.PageId = params.get("PageId")
        self.StatusCode = params.get("StatusCode")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptConfig(AbstractModel):
    """Exception rules, which are used to bypass specific rules

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param ExceptUserRules: The settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRules: list of ExceptUserRule
        """
        self.Switch = None
        self.ExceptUserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ExceptUserRules") is not None:
            self.ExceptUserRules = []
            for item in params.get("ExceptUserRules"):
                obj = ExceptUserRule()
                obj._deserialize(item)
                self.ExceptUserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRule(AbstractModel):
    """The settings of the exception rule

    """

    def __init__(self):
        r"""
        :param RuleName: The rule name.
        :type RuleName: str
        :param Action: The rule action. It only supports the value `skip`, which indicates skipping all managed rules.
        :type Action: str
        :param RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
        :type RuleStatus: str
        :param RuleID: The rule ID, which is automatically created and only used as an output parameter.
        :type RuleID: int
        :param UpdateTime: The update time. If it is null, the current date and time is recorded.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param ExceptUserRuleConditions: The matching condition.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRuleConditions: list of ExceptUserRuleCondition
        :param ExceptUserRuleScope: The scope to which the exception rule applies.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRuleScope: :class:`tencentcloud.teo.v20220901.models.ExceptUserRuleScope`
        :param RulePriority: The rule priority. Value range: 0-100. If it is null, it defaults to 0.
        :type RulePriority: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.RuleID = None
        self.UpdateTime = None
        self.ExceptUserRuleConditions = None
        self.ExceptUserRuleScope = None
        self.RulePriority = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ExceptUserRuleConditions") is not None:
            self.ExceptUserRuleConditions = []
            for item in params.get("ExceptUserRuleConditions"):
                obj = ExceptUserRuleCondition()
                obj._deserialize(item)
                self.ExceptUserRuleConditions.append(obj)
        if params.get("ExceptUserRuleScope") is not None:
            self.ExceptUserRuleScope = ExceptUserRuleScope()
            self.ExceptUserRuleScope._deserialize(params.get("ExceptUserRuleScope"))
        self.RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleCondition(AbstractModel):
    """The condition of the exception rule

    """

    def __init__(self):
        r"""
        :param MatchFrom: The field to match. Values:
<li>`host`: Request domain name</li>
<li>`sip`: Client IP</li>
<li>`ua`: User-Agent</li>
<li>`cookie`: Cookie</li>
<li>`cgi`: CGI script</li>
<li>`xff`: XFF header</li>
<li>`url`: Request URL</li>
<li>`accept`: Request content type</li>
<li>`method`: Request method</li>
<li>`header`: Request header</li>
<li>`sip_proto`: Network layer protocol</li>
        :type MatchFrom: str
        :param MatchParam: The parameter of the field. Only when `MatchFrom = header`, the key contained in the header can be passed.
        :type MatchParam: str
        :param Operator: The logical operator. Values:
<li>`equal`: String equals</li>
<li>`not_equal`: Value not equals</li>
<li>`include`: String contains</li>
<li>`not_include`: String not contains</li>
<li>`match`: IP matches</li>
<li>`not_match`: IP not matches</li>
<li>`include_area`: Regions contain</li>
<li>`is_empty`: Value left empty</li>
<li>`not_exists`: Key fields not exist</li>
<li>`regexp`: Regex matches</li>
<li>`len_gt`: Value greater than</li>
<li>`len_lt`: Value smaller than</li>
<li>`len_eq`: Value equals</li>
<li>`match_prefix`: Prefix matches</li>
<li>`match_suffix`: Suffix matches</li>
<li>`wildcard`: Wildcard</li>
        :type Operator: str
        :param MatchContent: The value of the parameter.
        :type MatchContent: str
        """
        self.MatchFrom = None
        self.MatchParam = None
        self.Operator = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.MatchFrom = params.get("MatchFrom")
        self.MatchParam = params.get("MatchParam")
        self.Operator = params.get("Operator")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleScope(AbstractModel):
    """The scope to which the exception rule applies

    """

    def __init__(self):
        r"""
        :param Type: Exception mode. Values:
<li>`complete`: Skip the exception rule for full requests.</li>
<li>`partial`: Skip the exception rule for partial requests.</li>
        :type Type: str
        :param Modules: The module to be activated. Values:
<li>`waf`: Managed rules</li>
<li>`cc`: Rate limiting rules</li>
<li>`bot`: bot protection</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Modules: list of str
        :param PartialModules: Module settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PartialModules: list of PartialModule
        :param SkipConditions: Condition settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SkipConditions: list of SkipCondition
        """
        self.Type = None
        self.Modules = None
        self.PartialModules = None
        self.SkipConditions = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Modules = params.get("Modules")
        if params.get("PartialModules") is not None:
            self.PartialModules = []
            for item in params.get("PartialModules"):
                obj = PartialModule()
                obj._deserialize(item)
                self.PartialModules.append(obj)
        if params.get("SkipConditions") is not None:
            self.SkipConditions = []
            for item in params.get("SkipConditions"):
                obj = SkipCondition()
                obj._deserialize(item)
                self.SkipConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param Reason: Failure reason.
        :type Reason: str
        :param Targets: List of resources failed to be processed. 
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAscriptionInfo(AbstractModel):
    """Verification file, used to verify site ownership

    """

    def __init__(self):
        r"""
        :param IdentifyPath: Directory of the verification file.
        :type IdentifyPath: str
        :param IdentifyContent: Content of the verification file.
        :type IdentifyContent: str
        """
        self.IdentifyPath = None
        self.IdentifyContent = None


    def _deserialize(self, params):
        self.IdentifyPath = params.get("IdentifyPath")
        self.IdentifyContent = params.get("IdentifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values under the same filter is `OR`.

    """

    def __init__(self):
        r"""
        :param Name: Fields to be filtered.
        :type Name: str
        :param Values: Value of the filtered field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowOrigin(AbstractModel):
    """The origin cache configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration of following the origin server. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param DefaultCacheTime: Sets the default cache time when the origin server does not return the Cache-Control header.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DefaultCacheTime: int
        :param DefaultCache: Specifies whether to enable cache when the origin server does not return the Cache-Control header.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DefaultCache: str
        """
        self.Switch = None
        self.DefaultCacheTime = None
        self.DefaultCache = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.DefaultCacheTime = params.get("DefaultCacheTime")
        self.DefaultCache = params.get("DefaultCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable force HTTPS redirect. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param RedirectStatusCode: Redirect status code. Values:
<li>`301`: 301 redirect</li>
<li>`302`: 302 redirect</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeoIp(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID
        :type RegionId: int
        :param Country: Country name
        :type Country: str
        :param Continent: The continent.
        :type Continent: str
        :param Province: The state/province.
        :type Province: str
        """
        self.RegionId = None
        self.Country = None
        self.Continent = None
        self.Province = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Country = params.get("Country")
        self.Continent = params.get("Continent")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """HTTP header, used as input for the CreatePrefetchTask API

    """

    def __init__(self):
        r"""
        :param Name: HTTP header name.
        :type Name: str
        :param Value: HTTP header value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param MaxAge: The MaxAge value in seconds. Maximum value: `86400` (one day)
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxAge: int
        :param IncludeSubDomains: Whether to contain subdomain names. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeSubDomains: str
        :param Preload: Whether to enable preloading. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Preload: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None
        self.Preload = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        self.Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Http2: Whether to enable HTTP2. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param OcspStapling: Whether to enable OCSP. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param TlsVersion: TLS version. Values:
<li>`TLSv1`: TLSv1 version</li>
<li>`TLSV1.1`: TLSv1.1 version</li>
<li>`TLSV1.2`: TLSv1.2 version</li>
<li>`TLSv1.3`: TLSv1.3 version</li>Only consecutive versions can be enabled at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        :param Hsts: HSTS Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220901.models.Hsts`
        :param CertInfo: The certificate configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertInfo: list of ServerCertInfo
        :param ApplyType: Whether the certificate is managed by EdgeOne. Values:
<li>`apply`: Managed by EdgeOne.</li>
<li>`none`: Not managed by EdgeOne.</li>If it is left empty, the default value `none` is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ApplyType: str
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None
        self.CertInfo = None
        self.ApplyType = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identification(AbstractModel):
    """The site verification information

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Status: The verification status. Values:
<li>`pending`: The verification is ongoing.</li>
<li>`finished`: The verification completed.</li>
        :type Status: str
        :param Ascription: Details of the DNS record.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param OriginalNameServers: The NS record of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalNameServers: list of str
        :param FileAscription: Details of the verification file.
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        """
        self.ZoneName = None
        self.Status = None
        self.Ascription = None
        self.OriginalNameServers = None
        self.FileAscription = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        self.OriginalNameServers = params.get("OriginalNameServers")
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone response structure.

    """

    def __init__(self):
        r"""
        :param Ascription: Details of the DNS record.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param FileAscription: Details of the verification file.
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ascription = None
        self.FileAscription = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
        self.RequestId = params.get("RequestId")


class IntelligenceRule(AbstractModel):
    """Bot intelligence rules

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param IntelligenceRuleItems: Items in a bot intelligence rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRuleItems: list of IntelligenceRuleItem
        """
        self.Switch = None
        self.IntelligenceRuleItems = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("IntelligenceRuleItems") is not None:
            self.IntelligenceRuleItems = []
            for item in params.get("IntelligenceRuleItems"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self.IntelligenceRuleItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRuleItem(AbstractModel):
    """Bot intelligence rule items

    """

    def __init__(self):
        r"""
        :param Label: The tag to categorize bots. Values:
<li>`evil_bot`: Malicious bot</li>
<li>`suspect_bot`: Suspected bot</li>
<li>`good_bot`: Good bot</li>
<li>`normal`: Normal request</li>
        :type Label: str
        :param Action: The action taken on bots. Values
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`alg`: JavaScript challenge</li>
<li>`captcha`: Managed challenge</li>
<li>`monitor`: Observe</li>
        :type Action: str
        """
        self.Label = None
        self.Action = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableConfig(AbstractModel):
    """IP/Region blocklist/allowlist configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param IpTableRules: The settings of the basic access control rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpTableRules: list of IpTableRule
        """
        self.Switch = None
        self.IpTableRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("IpTableRules") is not None:
            self.IpTableRules = []
            for item in params.get("IpTableRules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self.IpTableRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableRule(AbstractModel):
    """IP blocklist/allowlist rule details

    """

    def __init__(self):
        r"""
        :param Action: The action. Values:
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`monitor`: Observe</li>
        :type Action: str
        :param MatchFrom: The matching dimension. Values:
<li>`ip`: Match by IP.</li>
<li>`area`: Match by IP region.</li>
        :type MatchFrom: str
        :param MatchContent: The matching content.
        :type MatchContent: str
        :param RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param UpdateTime: The update time, which is only used as an output parameter.
        :type UpdateTime: str
        :param Status: The rule status. A null value indicates that the rule is enabled. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self.Action = None
        self.MatchFrom = None
        self.MatchContent = None
        self.RuleID = None
        self.UpdateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContent = params.get("MatchContent")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """The IPv6 access configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable IPv6 access. Values:
<li>`on`: Enable IPv6 access.</li>
<li>`off`: Disable IPv6 access.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4OfflineLog(AbstractModel):
    """The L7 log details

    """

    def __init__(self):
        r"""
        :param LogTime: The start time of the log packaging.
        :type LogTime: int
        :param ProxyId: The L4 proxy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param Size: The log size, in bytes.
        :type Size: int
        :param Url: The download address.
        :type Url: str
        :param LogPacketName: The log package name.
        :type LogPacketName: str
        :param Area: The acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
        :type Area: str
        """
        self.LogTime = None
        self.ProxyId = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.ProxyId = params.get("ProxyId")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """Layer-7 offline log details

    """

    def __init__(self):
        r"""
        :param LogTime: Start time of the log packaging
        :type LogTime: int
        :param Domain: The subdomain name.
        :type Domain: str
        :param Size: Log size, in bytes.
        :type Size: int
        :param Url: Download address
        :type Url: str
        :param LogPacketName: Log package name
        :type LogPacketName: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
        :type Area: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancing(AbstractModel):
    """CLB information

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: The load balancer ID.
        :type LoadBalancingId: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Type: str
        :param TTL: The cache time of DNS records when `Type=dns_only`.
        :type TTL: int
        :param Status: The load balancer status. Values:
<li>`online`: Deployed</li>
<li>`process`: Deployment in progress</li>
        :type Status: str
        :param Cname: Schedules domain names.
        :type Cname: str
        :param OriginGroupId: The ID of the primary origin group.
        :type OriginGroupId: str
        :param BackupOriginGroupId: The ID of the secondary origin group. If not specified, it indicates that secondary origins are not used.
        :type BackupOriginGroupId: str
        :param UpdateTime: The update time.
        :type UpdateTime: str
        :param OriginType: The origin-pull type. Values:
<li>`normal`: Primary/Secondary origin-pull</li>
<li>`advanced`: Advanced origin-pull</li>
        :type OriginType: str
        :param AdvancedOriginGroups: Advanced origin-pull configuration. This field is valid when `OriginType=advanced`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvancedOriginGroups: list of AdvancedOriginGroup
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.Status = None
        self.Cname = None
        self.OriginGroupId = None
        self.BackupOriginGroupId = None
        self.UpdateTime = None
        self.OriginType = None
        self.AdvancedOriginGroups = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.OriginGroupId = params.get("OriginGroupId")
        self.BackupOriginGroupId = params.get("BackupOriginGroupId")
        self.UpdateTime = params.get("UpdateTime")
        self.OriginType = params.get("OriginType")
        if params.get("AdvancedOriginGroups") is not None:
            self.AdvancedOriginGroups = []
            for item in params.get("AdvancedOriginGroups"):
                obj = AdvancedOriginGroup()
                obj._deserialize(item)
                self.AdvancedOriginGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param Deleted: Whether the logset is deleted. Values:
<li>`no`: The logset is not deleted;</li>
<li>`yes`: The logset is deleted.</li>
        :type Deleted: str
        """
        self.LogSetRegion = None
        self.LogSetName = None
        self.LogSetId = None
        self.Deleted = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetName = params.get("LogSetName")
        self.LogSetId = params.get("LogSetId")
        self.Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogTopicDetailInfo(AbstractModel):
    """Details of the shipping task

    """

    def __init__(self):
        r"""
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param EntityType: Type of the shipping task.
        :type EntityType: str
        :param EntityList: List of tasks.
        :type EntityList: list of str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param TopicId: Topic ID of the shipping task.
        :type TopicId: str
        :param TopicName: Topic name of the shipping task.
        :type TopicName: str
        :param Period: Retention period of the shipping task topic. Unit: day.
        :type Period: int
        :param Enabled: Whether the shipping task is enabled.
        :type Enabled: bool
        :param CreateTime: Creation time in the format of YYYY-mm-dd HH:MM:SS.
        :type CreateTime: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland).</li>
        :type Area: str
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param ZoneName: Name of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param Deleted: Whether the shipping task is deleted. Values:
<li>`yes`: The shipping task is deleted;</li>
<li>`no`: The shipping task is not deleted.</li>
        :type Deleted: str
        """
        self.TaskName = None
        self.LogSetRegion = None
        self.EntityType = None
        self.EntityList = None
        self.LogSetId = None
        self.LogSetName = None
        self.TopicId = None
        self.TopicName = None
        self.Period = None
        self.Enabled = None
        self.CreateTime = None
        self.Area = None
        self.ZoneId = None
        self.ZoneName = None
        self.Deleted = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.LogSetRegion = params.get("LogSetRegion")
        self.EntityType = params.get("EntityType")
        self.EntityList = params.get("EntityList")
        self.LogSetId = params.get("LogSetId")
        self.LogSetName = params.get("LogSetName")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Period = params.get("Period")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration, which is used to set the default value of `MaxAge` and is disabled by default.

    """

    def __init__(self):
        r"""
        :param FollowOrigin: Whether to follow the origin server. Values:
<li>`on`: Follow the origin server and ignore the field MaxAgeTime;</li>
<li>`off`: Do not follow the origin server and apply the field MaxAgeTime.</li>
        :type FollowOrigin: str
        :param MaxAgeTime: Specifies the maximum amount of time (in seconds). The maximum value is 365 days.
Note: The value `0` means not to cache.
        :type MaxAgeTime: int
        """
        self.FollowOrigin = None
        self.MaxAgeTime = None


    def _deserialize(self, params):
        self.FollowOrigin = params.get("FollowOrigin")
        self.MaxAgeTime = params.get("MaxAgeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmConfigRequest(AbstractModel):
    """ModifyAlarmConfig request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: The alarm service type. Values:
<li>`ddos`: DDoS alarm service.</li>
        :type ServiceType: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param EntityList: The list of protection entities.
        :type EntityList: list of str
        :param Threshold: The alarm threshold. When no value or 0 is passed, the default alarm threshold will be used.
        :type Threshold: int
        :param IsDefault: Whether the default alarm threshold is used.
        :type IsDefault: bool
        """
        self.ServiceType = None
        self.ZoneId = None
        self.EntityList = None
        self.Threshold = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ZoneId = params.get("ZoneId")
        self.EntityList = params.get("EntityList")
        self.Threshold = params.get("Threshold")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmConfigResponse(AbstractModel):
    """ModifyAlarmConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmDefaultThresholdRequest(AbstractModel):
    """ModifyAlarmDefaultThreshold request structure.

    """

    def __init__(self):
        r"""
        :param ServiceType: The alarm service type. Values:
<li>`ddos`: DDoS alarm service.</li>
        :type ServiceType: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Threshold: The threshold in Mbps. Maximum value: 10.
        :type Threshold: int
        :param Entity: The protection entity, which is a proxy ID when layer-4 protection is enabled, or a site name when layer-7 protection is on.
        :type Entity: str
        """
        self.ServiceType = None
        self.ZoneId = None
        self.Threshold = None
        self.Entity = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ZoneId = params.get("ZoneId")
        self.Threshold = params.get("Threshold")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmDefaultThresholdResponse(AbstractModel):
    """ModifyAlarmDefaultThreshold response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAliasDomainRequest(AbstractModel):
    """ModifyAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param AliasName: The alias domain name.
        :type AliasName: str
        :param TargetName: The target domain name.
        :type TargetName: str
        :param CertType: Certificate configuration. Values:
<li>`none`: Off</li>
<li>`hosting`: Managed SSL certificate</li>
<li>`apply`: Free certificate</li>The original configuration will apply if this field is not specified.
        :type CertType: str
        :param CertId: The certificate ID. This field is required when `CertType=hosting`.
        :type CertId: list of str
        """
        self.ZoneId = None
        self.AliasName = None
        self.TargetName = None
        self.CertType = None
        self.CertId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasName = params.get("AliasName")
        self.TargetName = params.get("TargetName")
        self.CertType = params.get("CertType")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainResponse(AbstractModel):
    """ModifyAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAliasDomainStatusRequest(AbstractModel):
    """ModifyAliasDomainStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Paused: Status of the alias domain name. Values:
<li>`false`: Enable the alias domain name.</li>
<li>`true`: Disable the alias domain name.</li>
        :type Paused: bool
        :param AliasNames: The alias domain name you want to modify its status. If it is left empty, the modify operation is not performed.
        :type AliasNames: list of str
        """
        self.ZoneId = None
        self.Paused = None
        self.AliasNames = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Paused = params.get("Paused")
        self.AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainStatusResponse(AbstractModel):
    """ModifyAliasDomainStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param ProxyName: The domain name or subdomain name when `ProxyType=hostname`.
The instance name when `ProxyType=instance`.
        :type ProxyName: str
        :param SessionPersistTime: The session persistence duration. Value range: 30-3600 (in seconds).
The original configuration will apply if this field is not specified.
        :type SessionPersistTime: int
        :param ProxyType: The proxy type. Values:
<li>`hostname`: The proxy is created by subdomain name.</li>
<li>`instance`: The proxy is created by instance.</li>If not specified, this field uses the default value `instance`.
        :type ProxyType: str
        :param Ipv6: The IPv6 access configuration. The original configuration will apply if this field is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.Ipv6 = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param RuleId: The rule ID.
        :type RuleId: str
        :param OriginType: The origin type. Values:
<li>`custom`: Specified origins</li>
<li>`origins`: Origin group</li></li>The original configuration will apply if this field is not specified.
        :type OriginType: str
        :param Port: The access port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-90</li>
        :type Port: list of str
        :param Proto: The protocol. Values:
<li>`TCP`: TCP protocol</li>
<li>`UDP`: UDP protocol</li>The original configuration will apply if this field is not specified.
        :type Proto: str
        :param OriginValue: Origin server information:
<li>When `OriginType=custom`, it indicates one or more origin servers, such as ["8.8.8.8","9.9.9.9"] or ["test.com"].</li>
<li>When `OriginType=origins`, it indicates an origin group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>

The original configuration will apply if this field is not specified.
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. Values:
<li>`TOA`: Pass the client IP via TOA (available only when `Proto=TCP`).</li>
<li>`PPV1`: Pass the client IP via Proxy Protocol V1 (available only when `Proto=TCP`).</li>
<li>`PPV2`: Pass the client IP via Proxy Protocol V2.</li>
<li>`OFF`: Not pass the client IP.</li>If not specified, this field uses the default value OFF.
        :type ForwardClientIp: str
        :param SessionPersist: Whether to enable session persistence. Values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>If it is left empty, the default value `false` is used.
        :type SessionPersist: bool
        :param OriginPort: The origin port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
        :type OriginPort: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.OriginType = None
        self.Port = None
        self.Proto = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.OriginType = params.get("OriginType")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param RuleId: The rule ID.
        :type RuleId: str
        :param Status: The rule status. Values:
<li>`offline`: Disabled</li>
<li>`online`: Enabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ProxyId: The proxy ID.
        :type ProxyId: str
        :param Status: The proxy status. Values:
<li>`offline`: The proxy is disabled.</li>
<li>`online`: The proxy is enabled.</li>
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyHostRequest(AbstractModel):
    """ModifyDDoSPolicyHost request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Host: The subdomain name/layer-4 proxy.
        :type Host: str
        :param AccelerateType: Whether to enabled acceleration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type AccelerateType: str
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param SecurityType: Whether to enable security protection. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type SecurityType: str
        """
        self.ZoneId = None
        self.Host = None
        self.AccelerateType = None
        self.PolicyId = None
        self.SecurityType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.AccelerateType = params.get("AccelerateType")
        self.PolicyId = params.get("PolicyId")
        self.SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyHostResponse(AbstractModel):
    """ModifyDDoSPolicyHost response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param DDoSRule: Details of the DDoS mitigation configuration.
        :type DDoSRule: :class:`tencentcloud.teo.v20220901.models.DDoSRule`
        """
        self.PolicyId = None
        self.ZoneId = None
        self.DDoSRule = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        if params.get("DDoSRule") is not None:
            self.DDoSRule = DDoSRule()
            self.DDoSRule._deserialize(params.get("DDoSRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param CertId: ID of the certificate.
        :type CertId: str
        :param Status: Status of the certificate. Values:
<li>`deployed`: The certificate is deployed;</li>
<li>`disabled`: The certificate is disabled.</li>When a deployment fails, you can try again.
        :type Status: str
        """
        self.ZoneId = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateResponse(AbstractModel):
    """ModifyDefaultCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnsRecordRequest(AbstractModel):
    """ModifyDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The record ID.
        :type DnsRecordId: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param DnsRecordType: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type DnsRecordType: str
        :param DnsRecordName: The record name, which consists of the host record and site name. Note that the original configuration will be used if this field is not specified.
        :type DnsRecordName: str
        :param Content: The record content. Note that the original configuration will be used if this field is not specified.
        :type Content: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect. Default value: 300. Note that the original configuration will be used if this field is not specified.
        :type TTL: int
        :param Priority: Specifies a value in the range 1–50 when you make changes to the MX records. A smaller value indicates higher priority. Note that the default value 0 will be used if this field is not specified.
        :type Priority: int
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li></li>The original configuration will apply if this field is not specified.
        :type Mode: str
        """
        self.DnsRecordId = None
        self.ZoneId = None
        self.DnsRecordType = None
        self.DnsRecordName = None
        self.Content = None
        self.TTL = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.ZoneId = params.get("ZoneId")
        self.DnsRecordType = params.get("DnsRecordType")
        self.DnsRecordName = params.get("DnsRecordName")
        self.Content = params.get("Content")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnsRecordResponse(AbstractModel):
    """ModifyDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The DNSSEC status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnssecResponse(AbstractModel):
    """ModifyDnssec response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Hosts: List of domain names that the certificate will be attached to.
        :type Hosts: list of str
        :param ServerCertInfo: Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :type ServerCertInfo: list of ServerCertInfo
        :param ApplyType: Whether the certificate is managed by EdgeOne. Values:
<li>`apply`: Managed by EdgeOne</li>
<li>`none`: Not managed by EdgeOne</li>If it is left empty, the default value `apply` is used.
        :type ApplyType: str
        """
        self.ZoneId = None
        self.Hosts = None
        self.ServerCertInfo = None
        self.ApplyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("ServerCertInfo") is not None:
            self.ServerCertInfo = []
            for item in params.get("ServerCertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.ServerCertInfo.append(obj)
        self.ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingRequest(AbstractModel):
    """ModifyLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param LoadBalancingId: The load balancer ID.
        :type LoadBalancingId: str
        :param Type: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Type: str
        :param OriginGroupId: The ID of the primary origin group.
        :type OriginGroupId: str
        :param BackupOriginGroupId: The ID of the secondary origin group (only available when `Type=proxied`). If not specified, it indicates that secondary origins are not used.
        :type BackupOriginGroupId: str
        :param TTL: When `Type=dns_only`, it indicates the amount of time that DNS records remain in the cache of a DNS server.
Value range: 60-86400 (in seconds). If it's not specified, the default value 600 will be used.
        :type TTL: int
        :param OriginType: The origin-pull type. Values:
<li>`normal`: Primary/Secondary origin-pull</li>
<li>`advanced`: Advanced origin-pull (only used when `Type=proxied`)</li>If it is left empty, primary/secondary origin-pull is applied.
        :type OriginType: str
        :param AdvancedOriginGroups: Advanced origin-pull configuration. This field is valid when `OriginType=advanced`.
If it is left empty, this configuration is not used.
        :type AdvancedOriginGroups: list of AdvancedOriginGroup
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Type = None
        self.OriginGroupId = None
        self.BackupOriginGroupId = None
        self.TTL = None
        self.OriginType = None
        self.AdvancedOriginGroups = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Type = params.get("Type")
        self.OriginGroupId = params.get("OriginGroupId")
        self.BackupOriginGroupId = params.get("BackupOriginGroupId")
        self.TTL = params.get("TTL")
        self.OriginType = params.get("OriginType")
        if params.get("AdvancedOriginGroups") is not None:
            self.AdvancedOriginGroups = []
            for item in params.get("AdvancedOriginGroups"):
                obj = AdvancedOriginGroup()
                obj._deserialize(item)
                self.AdvancedOriginGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingResponse(AbstractModel):
    """ModifyLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param LoadBalancingId: The load balancer ID.
        :type LoadBalancingId: str
        :param Status: The load balancer status. Values:
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingStatusResponse(AbstractModel):
    """ModifyLoadBalancingStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLogTopicTaskRequest(AbstractModel):
    """ModifyLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param TopicId: ID of the log topic.
        :type TopicId: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param TopicName: The new topic name. If you do not specify this field, no changes will be made.
        :type TopicName: str
        :param LogSetName: The new logset name.
        :type LogSetName: str
        :param Period: The retention period of the updated logset.
        :type Period: int
        :param DropEntityList: List of shipping entities to be deleted.
        :type DropEntityList: list of str
        :param AddedEntityList: List of shipping entities to be added.
        :type AddedEntityList: list of str
        """
        self.ZoneId = None
        self.LogSetRegion = None
        self.LogSetId = None
        self.TopicId = None
        self.EntityType = None
        self.TaskName = None
        self.TopicName = None
        self.LogSetName = None
        self.Period = None
        self.DropEntityList = None
        self.AddedEntityList = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.EntityType = params.get("EntityType")
        self.TaskName = params.get("TaskName")
        self.TopicName = params.get("TopicName")
        self.LogSetName = params.get("LogSetName")
        self.Period = params.get("Period")
        self.DropEntityList = params.get("DropEntityList")
        self.AddedEntityList = params.get("AddedEntityList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogTopicTaskResponse(AbstractModel):
    """ModifyLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param OriginGroupId: The ID of the origin group.
        :type OriginGroupId: str
        :param OriginType: The origin type. Values:
<li>`self`: Customer origin</li>
<li>`third_party`: Third-party origin</li>
<li>`cos`: Tencent Cloud COS origin</li>
        :type OriginType: str
        :param OriginGroupName: The name of the origin group.
        :type OriginGroupName: str
        :param ConfigurationType: The origin configuration type when `OriginType=self`. Values:
<li>`area`: Configure by region.</li>
<li>`weight`: Configure by weight.</li>
<li>`proto`: Configure by HTTP protocol.</li> When `OriginType=third_party/cos`, leave this field empty.
        :type ConfigurationType: str
        :param OriginRecords: Details of the origin record.
        :type OriginRecords: list of OriginRecord
        :param HostHeader: The origin domain. This field can be specified only when `OriginType=self`.
If it is left empty, the existing configuration is used.
        :type HostHeader: str
        """
        self.ZoneId = None
        self.OriginGroupId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginGroupId = params.get("OriginGroupId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOriginGroupResponse(AbstractModel):
    """ModifyOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRulePriorityRequest(AbstractModel):
    """ModifyRulePriority request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleIds: Order of rule IDs. If there are multiple rules, they will be executed in order from top to bottom.
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRulePriorityResponse(AbstractModel):
    """ModifyRulePriority response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        :param RuleId: The rule ID.
        :type RuleId: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param Tags: Tag of the rule.
        :type Tags: list of str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Rules = None
        self.RuleId = None
        self.Status = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param SecurityConfig: Security configuration.
        :type SecurityConfig: :class:`tencentcloud.teo.v20220901.models.SecurityConfig`
        :param Entity: The subdomain name/L4 proxy. You must specify either "Entity" or "TemplateId".
        :type Entity: str
        :param TemplateId: The template ID. You must specify either this field or "Entity".
        :type TemplateId: str
        """
        self.ZoneId = None
        self.SecurityConfig = None
        self.Entity = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        self.Entity = params.get("Entity")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityWafGroupPolicyRequest(AbstractModel):
    """ModifySecurityWafGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID. You must specify either "ZoneId+Entity" or "TemplateId".
        :type ZoneId: str
        :param Entity: The subdomain name. You must specify either "ZoneId+Entity" or "TemplateId". 
        :type Entity: str
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>If not specified, it defaults to the setting that was last configured.
        :type Switch: str
        :param Level: The rule level. Values:
<li>`loose`: Loose</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`stricter`: Super strict</li>
<li>`custom`: Custom</li>If not specified, it defaults to the setting that was last configured.
        :type Level: str
        :param Mode: The rule action. Values:
<li>`block`: Block</li>
<li>`observe`: Observe</li>If not specified, it defaults to the setting that was last configured.
        :type Mode: str
        :param WafRules: The settings of the managed rule. If not specified, it defaults to the settings that were last configured.
        :type WafRules: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param AiRule: The settings of the AI rule engine. If not specified, it defaults to the settings that were last configured.
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        :param WafGroups: The settings of the managed rule group. If not specified, it defaults to the settings that were last configured.
        :type WafGroups: list of WafGroup
        :param TemplateId: The template ID. You must specify either this field or "ZoneId+Entity".
        :type TemplateId: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRules = None
        self.AiRule = None
        self.WafGroups = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRules") is not None:
            self.WafRules = WafRule()
            self.WafRules._deserialize(params.get("WafRules"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
        if params.get("WafGroups") is not None:
            self.WafGroups = []
            for item in params.get("WafGroups"):
                obj = WafGroup()
                obj._deserialize(item)
                self.WafGroups.append(obj)
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityWafGroupPolicyResponse(AbstractModel):
    """ModifySecurityWafGroupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The CNAME acceleration status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCnameSpeedUpResponse(AbstractModel):
    """ModifyZoneCnameSpeedUp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Type: The site access method. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>The original configuration will apply if this field is not specified.
        :type Type: str
        :param VanityNameServers: The custom name servers. If this field is not specified, the default name servers will be used.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param AliasZoneName: The site alias. It can be up to 20 characters consisting of digits, letters, hyphens (-) and underscores (_).
        :type AliasZoneName: str
        """
        self.ZoneId = None
        self.Type = None
        self.VanityNameServers = None
        self.AliasZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        self.AliasZoneName = params.get("AliasZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID to be modified.
        :type ZoneId: str
        :param CacheConfig: Cache expiration time configuration
The original configuration will apply if this field is not specified.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param CacheKey: The node cache key configuration.
The original configuration will apply if this field is not specified.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param MaxAge: The browser cache configuration.
The original configuration will apply if this field is not specified.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: The offline cache configuration.
The original configuration will apply if this field is not specified.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param Quic: The QUIC access configuration.
The original configuration will apply if this field is not specified.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: The POST transport configuration.
The original configuration will apply if this field is not specified.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: The smart compression configuration.
The original configuration will apply if this field is not specified.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: The HTTP2 origin-pull configuration.
The original configuration will apply if this field is not specified.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: The force HTTPS redirect configuration.
The original configuration will apply if this field is not specified.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param Https: The HTTPS acceleration configuration.
The original configuration will apply if this field is not specified.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param Origin: The origin server configuration.
The original configuration will apply if this field is not specified.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: The smart acceleration configuration.
The original configuration will apply if this field is not specified.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param WebSocket: The WebSocket configuration.
The original configuration will apply if this field is not specified.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: The origin-pull client IP header configuration.
The original configuration will apply if this field is not specified.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: The cache prefresh configuration.
The original configuration will apply if this field is not specified.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: The IPv6 access configuration.
The original configuration will apply if this field is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: Whether to carry the location information of the client IP during origin-pull.
The original configuration will apply if this field is not specified.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneId = None
        self.CacheConfig = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Paused: The site status. Values:
<li>`false`: Disabled</li>
<li>`true`: Enabled</li>
        :type Paused: bool
        """
        self.ZoneId = None
        self.Paused = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NoCache(AbstractModel):
    """No-cache configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable no-cache configuration. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalAction(AbstractModel):
    """Common action of the rule engine

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Parameter
        :type Parameters: list of RuleNormalActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleNormalActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineCache(AbstractModel):
    """Offline cache feature status switch.

    """

    def __init__(self):
        r"""
        :param Switch: Whether offline cache is enabled. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptimizeAction(AbstractModel):
    """The optimization suggestions

    """

    def __init__(self):
        r"""
        :param Name: The optimization metric. Values:
<li>`Http2`</li>
<li>`Http3`</li>
<li>`Brotli`</li>
        :type Name: str
        :param Connectivity: The network environment.
        :type Connectivity: str
        :param Value: The estimated load time, in milliseconds.
        :type Value: int
        :param Ratio: The estimated improvement ratio, in %.
        :type Ratio: int
        """
        self.Name = None
        self.Connectivity = None
        self.Value = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Connectivity = params.get("Connectivity")
        self.Value = params.get("Value")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """The origin server configuration.

    """

    def __init__(self):
        r"""
        :param Origins: Primary origin server list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param BackupOrigins: The list of backup origin servers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param OriginPullProtocol: Origin-pull protocol configuration. Values:
<li>`http`: Force HTTP for origin-pull.</li>
<li>`follow`: Follow protocol.</li>
<li>`https`: Force HTTPS for origin-pull.</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        :param CosPrivateAccess: Whether to allow private access to buckets when `OriginType=cos`. Values:
<li>`on`: Allow private access.</li>
<li>`off`: Allow public access.</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CosPrivateAccess: str
        """
        self.Origins = None
        self.BackupOrigins = None
        self.OriginPullProtocol = None
        self.CosPrivateAccess = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.BackupOrigins = params.get("BackupOrigins")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """Origin group information.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param OriginGroupId: The ID of the origin group.
        :type OriginGroupId: str
        :param OriginType: The origin type. Values:
<li>`self`: Customer origin</li>
<li>`third_party`: Third-party origin</li>
<li>`cos`: Tencent Cloud COS origin</li>
        :type OriginType: str
        :param OriginGroupName: The name of the origin group.
        :type OriginGroupName: str
        :param ConfigurationType: The origin configuration type when `OriginType=self`. Values:
<li>`area`: Configure by region.</li>
<li>`weight`: Configure by weight.</li>
<li>`proto`: Configure by HTTP protocol.</li>When `OriginType=third_party/cos`, leave this field empty.
        :type ConfigurationType: str
        :param OriginRecords: The origin record information.
        :type OriginRecords: list of OriginRecord
        :param UpdateTime: The update time of the origin group.
        :type UpdateTime: str
        :param HostHeader: The origin domain when `OriginType=self`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HostHeader: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginGroupId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.UpdateTime = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginGroupId = params.get("OriginGroupId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroupCondition(AbstractModel):
    """Origin-pull condition

    """

    def __init__(self):
        r"""
        :param Target: Match type. Values:
<li>`url`: Partial URL path under the current site, such as "/example" and "/example/foo.jpg". You can use an asterisk (*) to indicate all values and a question mark (?) to indicate any single character.
</li>
        :type Target: str
        :param Operator: The operator. Values:
<li>`equal`: Equals</li>
        :type Operator: str
        :param Values: Values of the match type.
        :type Values: list of str
        """
        self.Target = None
        self.Operator = None
        self.Values = None


    def _deserialize(self, params):
        self.Target = params.get("Target")
        self.Operator = params.get("Operator")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """Origin group record

    """

    def __init__(self):
        r"""
        :param Record: The origin record value, which can be an IPv4/IPv6 address or a domain name.
        :type Record: str
        :param RecordId: The origin record ID.
        :type RecordId: str
        :param Port: The origin port. Value rang: 1-65535.
        :type Port: int
        :param Weight: The weight when `ConfigurationType=weight`.
If 0 or no value is passed, the weight of each origin in a group will be 0 or left empty, indicating that origin-pull is performed by round-robin.
If a value between 1-100 is passed, the total weight of multiple origins in a group should be 100, indicating that origin-pull is performed by weight.
The weight when `ConfigurationType=proto`.
If 0 or no value is passed, the weight of each origin in a group will be 0 or left empty, indicating that origin-pull is performed by round-robin.
If a value between 1-100 is passed, the total weight of multiple origins with the same protocol in a group should be 100, indicating that origin-pull is performed by weight.
        :type Weight: int
        :param Proto: The origin protocol when `ConfigurationType=proto`, indicating that origin-pull is performed by protocol.
<li>`http`: HTTP protocol</li>
<li>`https`: HTTPS protocol</li>
        :type Proto: str
        :param Area: The region when `ConfigurationType=area`, which is specified by country code (ISO 3166 alpha-2) or continent code. If not specified, it indicates all regions. Supported continent codes:
<li>`Asia`</li>
<li>`Europe`</li>
<li>`Africa`</li>
<li>`Oceania`</li>
<li>`Americas`</li>An origin group must have at least one origin configured with all regions.
        :type Area: list of str
        :param Private: It is valid only when `OriginType=third_part`.
Whether the origin group is private. Values:
<li>`true`: Yes.</li>
<li>`false`: No.</li>If not specified, it defaults to false.
        :type Private: bool
        :param PrivateParameters: The authentication parameter, which is used when `Private=true`.
        :type PrivateParameters: list of PrivateParameter
        """
        self.Record = None
        self.RecordId = None
        self.Port = None
        self.Weight = None
        self.Proto = None
        self.Area = None
        self.Private = None
        self.PrivateParameters = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.RecordId = params.get("RecordId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Proto = params.get("Proto")
        self.Area = params.get("Area")
        self.Private = params.get("Private")
        if params.get("PrivateParameters") is not None:
            self.PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self.PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartialModule(AbstractModel):
    """Module settings of the exception rule

    """

    def __init__(self):
        r"""
        :param Module: The module. Values:
<li>`waf`: Managed rules</li>
        :type Module: str
        :param Include: List of managed rule IDs to be skipped.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Include: list of int
        """
        self.Module = None
        self.Include = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Include = params.get("Include")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """EdgeOne plan information

    """

    def __init__(self):
        r"""
        :param Currency: Settlement currency. Values:
<li>`CNY`: Settled by Chinese RMB;</li>
<li>`USD`: Settled by US dollars.</li>
        :type Currency: str
        :param Flux: Traffic quota of the plan. It includes the traffic for security acceleration, content acceleration and smart acceleration. Unit: byte.
        :type Flux: int
        :param Frequency: Settlement cycle. Values:
<li>`y`: Settled by year;</li>
<li>`m`: Settled by month;</li>
<li>`h`: Settled by hour;</li>
<li>`M`: Settled by minute;</li>
<li>`s`: Settled by second.</li>
        :type Frequency: str
        :param PlanType: The plan option. Values:
<li>`sta`: Standard plan that supports content delivery network outside the Chinese mainland.</li>
<li>`sta_with_bot`: Standard plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`sta_cm`: Standard plan that supports content delivery network inside the Chinese mainland.</li>
<li>`sta_cm_with_bot`: Standard plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`sta`: Standard plan that supports content delivery network over the globe.</li>
<li>`sta_global_with_bot`: Standard plan that supports content delivery network over the globe and bot management.</li>
<li>`ent`: Enterprise plan that supports content delivery network outside the Chinese mainland.</li>
<li>`ent_with_bot`: Enterprise plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`ent_cm`: Enterprise plan that supports content delivery network inside the Chinese mainland.</li>
<li>`ent_cm_with_bot`: Enterprise plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`ent_global`: Enterprise plan that supports content delivery network over the globe.</li>
<li>`ent_global_with_bot`: Enterprise plan that supports content delivery network over the globe and bot management.</li>
        :type PlanType: str
        :param Price: Plan price (in CNY fen/US cent). The price unit depends on the settlement currency.
        :type Price: float
        :param Request: Quota on security acceleration requests
        :type Request: int
        :param SiteNumber: Number of sites to be bound to the plan
        :type SiteNumber: int
        :param Area: The acceleration region. Values:
<li>`mainland`: Chinese mainland</li>
<li>`overseas`: Global (Chinese mainland not included)</li>
<li>`global`: Global (Chinese mainland included)</li>
        :type Area: str
        """
        self.Currency = None
        self.Flux = None
        self.Frequency = None
        self.PlanType = None
        self.Price = None
        self.Request = None
        self.SiteNumber = None
        self.Area = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Flux = params.get("Flux")
        self.Frequency = params.get("Frequency")
        self.PlanType = params.get("PlanType")
        self.Price = params.get("Price")
        self.Request = params.get("Request")
        self.SiteNumber = params.get("SiteNumber")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortraitManagedRuleDetail(AbstractModel):
    """User profiling rule details

    """

    def __init__(self):
        r"""
        :param RuleId: Unique rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param Description: Rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param RuleTypeName: Rule type name: botdb (user profile)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleTypeName: str
        :param ClassificationId: The ID that classifies the rule category.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClassificationId: int
        :param Status: Action status of the rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.ClassificationId = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.ClassificationId = params.get("ClassificationId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable POST upload limit (default limit: 32 MB). Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateParameter(AbstractModel):
    """Origin authentication parameter

    """

    def __init__(self):
        r"""
        :param Name: The parameter name. Values
<li>`AccessKeyId`: Access Key ID</li>
<li>`SecretAccessKey`: Secret Access Key</li>
        :type Name: str
        :param Value: The parameter value.
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """The query condition

    """

    def __init__(self):
        r"""
        :param Key: The key of QueryCondition.
        :type Key: str
        :param Operator: The conditional operator. Values:
<li>`equals`: Equals</li>
<li>`notEquals`: Does not equal</li>
<li>`include`: Contains</li>
<li>`notInclude`: Does not contain</li>
<li>`startWith`: Starts with</li>
<li>`notStartWith`: Does not start with</li>
<li>`endWith`: Ends with</li>
<li>`notEndWith`: Does not end with</li>
        :type Operator: str
        :param Value: The value of QueryCondition.
        :type Value: list of str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """Request parameter contained in `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Values:
<li>`on`: Yes</li>
<li>`off`: No</li>
        :type Switch: str
        :param Action: Specifies how to use query strings in the cache key. Values:
<li>`includeCustom`: `Include partial query strings.</li>
<li>`excludeCustom`: Exclude partial query strings.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param Value: Array of query strings used/excluded
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: list of str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable QUIC. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Purging/Pre-warming available usage and quota

    """

    def __init__(self):
        r"""
        :param Batch: 
        :type Batch: int
        :param Daily: Daily submission quota limit.
        :type Daily: int
        :param DailyAvailable: Remaining daily submission quota.
        :type DailyAvailable: int
        :param Type: Type of cache purging/pre-warming. Values:
<li>`purge_prefix`: Purge by prefix</li>
<li>`purge_url`: Purge by URL</li>
<li>`purge_host`: Purge by hostname</li>
<li>`purge_all`: Purge all caches</li>
<li>`purge_cache_tag`: Purge by cache tag</li><li>`prefetch_url`: Pre-warm by URL</li>
        :type Type: str
        """
        self.Batch = None
        self.Daily = None
        self.DailyAvailable = None
        self.Type = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Daily = params.get("Daily")
        self.DailyAvailable = params.get("DailyAvailable")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """Rate limiting configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param RateLimitUserRules: The settings of the custom rate limiting rule. If it is null, the settings that were last configured will be used.
        :type RateLimitUserRules: list of RateLimitUserRule
        :param RateLimitTemplate: The settings of the rate limiting template. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitTemplate: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplate`
        :param RateLimitIntelligence: The client filtering settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitIntelligence: :class:`tencentcloud.teo.v20220901.models.RateLimitIntelligence`
        """
        self.Switch = None
        self.RateLimitUserRules = None
        self.RateLimitTemplate = None
        self.RateLimitIntelligence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RateLimitUserRules") is not None:
            self.RateLimitUserRules = []
            for item in params.get("RateLimitUserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self.RateLimitUserRules.append(obj)
        if params.get("RateLimitTemplate") is not None:
            self.RateLimitTemplate = RateLimitTemplate()
            self.RateLimitTemplate._deserialize(params.get("RateLimitTemplate"))
        if params.get("RateLimitIntelligence") is not None:
            self.RateLimitIntelligence = RateLimitIntelligence()
            self.RateLimitIntelligence._deserialize(params.get("RateLimitIntelligence"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligence(AbstractModel):
    """Client filtering

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Action: Action to be executed. Values:
<li>`monitor`: Observe</li>
<li>`alg`: Challenge</li>
        :type Action: str
        """
        self.Switch = None
        self.Action = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligenceRuleDetail(AbstractModel):
    """Details of the intelligent rate limiting rule

    """

    def __init__(self):
        r"""
        :param MatchContent: The client IP detected.
        :type MatchContent: str
        :param Action: The action taken.
        :type Action: str
        :param EffectiveTime: Update time
        :type EffectiveTime: str
        :param ExpireTime: The expiration time.
        :type ExpireTime: str
        :param RuleId: The rule ID.
        :type RuleId: int
        :param Status: The action status. `allowed` indicates that the request is allowed.
        :type Status: str
        """
        self.MatchContent = None
        self.Action = None
        self.EffectiveTime = None
        self.ExpireTime = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.MatchContent = params.get("MatchContent")
        self.Action = params.get("Action")
        self.EffectiveTime = params.get("EffectiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplate(AbstractModel):
    """Rate limit template

    """

    def __init__(self):
        r"""
        :param Mode: The mode. Values:
<li>`sup_loose`: Super loose</li>
<li>`loose`: Loose</li>
<li>`emergency`: Emergency</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`close`: Off</li>
        :type Mode: str
        :param Action: The action. Values:
<li>`alg`: JavaScript challenge</li>
<li>`monitor`: Observe</li>If it is left empty, the default value `alg` is used.
        :type Action: str
        :param RateLimitTemplateDetail: The settings of the rate limiting template. It is only used as an output parameter.
        :type RateLimitTemplateDetail: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplateDetail`
        """
        self.Mode = None
        self.Action = None
        self.RateLimitTemplateDetail = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Action = params.get("Action")
        if params.get("RateLimitTemplateDetail") is not None:
            self.RateLimitTemplateDetail = RateLimitTemplateDetail()
            self.RateLimitTemplateDetail._deserialize(params.get("RateLimitTemplateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """The settings of the rate limiting template

    """

    def __init__(self):
        r"""
        :param Mode: The mode. Values:
<li>`sup_loose`: Super loose</li>
<li>`loose`: Loose</li>
<li>`emergency`: Emergency</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`close`: Off</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param ID: The unique ID.
        :type ID: int
        :param Action: The action. Values:
<li>`alg`: JavaScript challenge</li>
<li>`monitor`: Observe</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param PunishTime: The blocking duration, in seconds. Value range: 0-172800.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param Threshold: The request threshold. Value range: 0-4294967294.
        :type Threshold: int
        :param Period: The statistical period. Value range: 0-120 seconds.
        :type Period: int
        """
        self.Mode = None
        self.ID = None
        self.Action = None
        self.PunishTime = None
        self.Threshold = None
        self.Period = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.ID = params.get("ID")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitUserRule(AbstractModel):
    """Rate limit rule

    """

    def __init__(self):
        r"""
        :param Threshold: The request threshold. Value range: 0-4294967294.
        :type Threshold: int
        :param Period: The statistical period. The value can be 10, 20, 30, 40, 50, or 60 seconds.
        :type Period: int
        :param RuleName: The rule name, which consists of only letters, digits, and underscores and cannot start with an underscore.
        :type RuleName: str
        :param Action: The action. Values:
<li>`monitor`: Observe</li>
<li>`drop`: Block</li>
<li>`alg`: JavaScript challenge</li>
        :type Action: str
        :param PunishTime: The amount of time taken to perform the action. Value range: 0 seconds - 2 days.
        :type PunishTime: int
        :param PunishTimeUnit: The time unit. Values:
<li>`second`: Second</li>
<li>`minutes`: Minute</li>
<li>`hour`: Hour</li>
        :type PunishTimeUnit: str
        :param RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>Default value: on
        :type RuleStatus: str
        :param AclConditions: The rule details.
        :type AclConditions: list of AclCondition
        :param RulePriority: The rule weight. Value range: 0-100.
        :type RulePriority: int
        :param RuleID: The rule ID, which is only used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleID: int
        :param FreqFields: The filter. Values:
<li>`sip`: Client IP</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FreqFields: list of str
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param FreqScope: The statistical dimension. Values:
<li>`source_to_eo`: Responses from the origin server to EdgeOne</li>
<li>`client_to_eo`: Requests from the client to EdgeOne</li>
Note: A null value indicates responses from the origin server to EdgeOne are recorded.
        :type FreqScope: list of str
        """
        self.Threshold = None
        self.Period = None
        self.RuleName = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.RuleStatus = None
        self.AclConditions = None
        self.RulePriority = None
        self.RuleID = None
        self.FreqFields = None
        self.UpdateTime = None
        self.FreqScope = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self.AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AclConditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.FreqFields = params.get("FreqFields")
        self.UpdateTime = params.get("UpdateTime")
        self.FreqScope = params.get("FreqScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimAliasDomainRequest(AbstractModel):
    """ReclaimAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        """
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimAliasDomainResponse(AbstractModel):
    """ReclaimAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Billable resource

    """

    def __init__(self):
        r"""
        :param Id: The resource ID.
        :type Id: str
        :param PayMode: Billing mode
`0`: Pay-as-you-go
        :type PayMode: int
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param EnableTime: The effective time.
        :type EnableTime: str
        :param ExpireTime: The expiration time.
        :type ExpireTime: str
        :param Status: The plan status. Values:
<li>`normal`: Normal</li>
<li>`isolated`: Isolated</li>
<li>`destroyed`: Terminated</li>
        :type Status: str
        :param Sv: Pricing query parameter
        :type Sv: list of Sv
        :param AutoRenewFlag: Whether to enable auto-renewal. Values:
<li>`0`: Default status.</li>
<li>`1`: Enable auto-renewal.</li>
<li>`2`: Disable auto-renewal.</li>
        :type AutoRenewFlag: int
        :param PlanId: ID of the resource associated with the plan.
        :type PlanId: str
        :param Area: The region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        """
        self.Id = None
        self.PayMode = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.Status = None
        self.Sv = None
        self.AutoRenewFlag = None
        self.PlanId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        if params.get("Sv") is not None:
            self.Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self.Sv.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PlanId = params.get("PlanId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteAction(AbstractModel):
    """Rule engine action for the HTTP request/response header

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Parameter
        :type Parameters: list of RuleRewriteActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleRewriteActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Rule item of the rule engine. The items in the `Conditions` array are in `OR` relationship, and the items in the inner `Conditions` list are in `AND` relationship.

    """

    def __init__(self):
        r"""
        :param Actions: Feature to be executed.
        :type Actions: list of Action
        :param Conditions: Feature execution conditions.
Note: If any condition in the array is met, the feature will run.
        :type Conditions: list of RuleAndConditions
        :param SubRules: The nested rule.
        :type SubRules: list of SubRuleItem
        """
        self.Actions = None
        self.Conditions = None
        self.SubRules = None


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("SubRules") is not None:
            self.SubRules = []
            for item in params.get("SubRules"):
                obj = SubRuleItem()
                obj._deserialize(item)
                self.SubRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAndConditions(AbstractModel):
    """List of rule engine conditions in `AND` relationship

    """

    def __init__(self):
        r"""
        :param Conditions: Rule engine condition. This condition will be considered met if all items in the array are met.
        :type Conditions: list of RuleCondition
        """
        self.Conditions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleChoicePropertiesItem(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match, which are optional parameter configuration items.

    """

    def __init__(self):
        r"""
        :param Name: The parameter name.
        :type Name: str
        :param Type: The parameter value type.
<li>CHOICE: The parameter value can be selected only from `Values`.</li>
<li>TOGGLE: The parameter value is of switch type and can be selected from `ChoicesValue`.</li>
<li>CUSTOM_NUM: The parameter value is a custom integer.</li>
<li>CUSTOM_STRING: The parameter value is a custom string.</li>
        :type Type: str
        :param ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param ExtraParameter: Special parameter.
<li>NULL: Select `NormalAction` for `RuleAction`. </li>
<li>If the member parameter `Id` is `Action`, select `RewirteAction` for `RuleAction`.</li>
<li>If the member parameter `Id` is `StatusCode`, select `CodeAction` for `RuleAction`.</li>
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self.Name = None
        self.Type = None
        self.ChoicesValue = None
        self.Min = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeActionParams(AbstractModel):
    """Parameters of the action with the `StatusCode` field as the rule engine condition

    """

    def __init__(self):
        r"""
        :param StatusCode: The status code.
        :type StatusCode: int
        :param Name: The parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name.
        :type Name: str
        :param Values: The parameter value.
        :type Values: list of str
        """
        self.StatusCode = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    """Rule engine condition parameters

    """

    def __init__(self):
        r"""
        :param Operator: Operator. Valid values:
<li>`equals`: Equals</li>
<li>`notEquals`: Does not equal</li>
<li>`exist`: Exists</li>
<li>`notexist`: Does not exist</li>
        :type Operator: str
        :param Target: Match type. Valid values:
<li>`filename`: File name</li>
<li>`extension`: File extension</li>
<li>`host`: Host</li>
<li>`full_url`: Full URL, which indicates the complete URL path under the current site and must contain the HTTP protocol, host, and path.</li>
<li>`url`: Partial URL under the current site</li><li>`client_country`: Country/Region of the client</li>
<li>`query_string`: Query string in the URL</li>
<li>`request_header`: HTTP request header</li>
        :type Target: str
        :param Values: The parameter value of the match type. It can be an empty string only when `Target=query string/request header` and `Operator=exist/notexist`.
<li>When `Target=extension`, enter the file extension, such as "jpg" and "txt".</li>
<li>When `Target=filename`, enter the file name, such as "foo" in "foo.jpg".</li>
<li>When `Target=all`, it indicates any site request.</li>
<li>When `Target=host`, enter the host under the current site, such as "www.maxx55.com".</li>
<li>When `Target=url`, enter the partial URL path under the current site, such as "/example".</li>
<li>When `Target=full_url`, enter the complete URL  under the current site. It must contain the HTTP protocol, host, and path, such as "https://www.maxx55.cn/example".</li>
<li>When `Target=client_country`, enter the ISO-3166 country/region code.</li>
<li>When `Target=query_string`, enter the value of the query string, such as "cn" and "1" in "lang=cn&version=1".</li>
<li>When `Target=request_header`, enter the HTTP request header value, such as "zh-CN,zh;q=0.9" in the "Accept-Language:zh-CN,zh;q=0.9" header.</li>
        :type Values: list of str
        :param IgnoreCase: Whether the parameter value is case insensitive. Default value: false.
        :type IgnoreCase: bool
        :param Name: The parameter name of the match type. This field is required only when `Target=query_string/request_header`.
<li>`query_string`: Name of the query string, such as "lang" and "version" in "lang=cn&version=1".</li>
<li>`request_header`: Name of the HTTP request header, such as "Accept-Language" in the "Accept-Language:zh-CN,zh;q=0.9" header.</li>
        :type Name: str
        :param IgnoreNameCase: 
        :type IgnoreNameCase: bool
        """
        self.Operator = None
        self.Target = None
        self.Values = None
        self.IgnoreCase = None
        self.Name = None
        self.IgnoreNameCase = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Target = params.get("Target")
        self.Values = params.get("Values")
        self.IgnoreCase = params.get("IgnoreCase")
        self.Name = params.get("Name")
        self.IgnoreNameCase = params.get("IgnoreNameCase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExtraParameter(AbstractModel):
    """Rule engine parameter details and special parameter types.

    """

    def __init__(self):
        r"""
        :param Id: Parameter name. Valid values:
<li>`Action`: Required parameter for HTTP header modification when `RewirteAction` is selected for `RuleAction`.</li>
<li>`StatusCode`: Required parameter for the status code feature when `CodeAction` is selected for `RuleAction`.</li>
        :type Id: str
        :param Type: Parameter value type.
<li>`CHOICE`: The parameter value can be selected only from `Values`.</li>
<li>`CUSTOM_NUM`: The parameter value is a custom integer.</li>
<li>`CUSTOM_STRING`: The parameter value is a custom string.</li>
        :type Type: str
        :param Choices: Valid values.
Note: If the value of `Id` is `StatusCode`, values in the array are all integer values. When entering a parameter value, enter the integer value of the string.
        :type Choices: list of str
        """
        self.Id = None
        self.Type = None
        self.Choices = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """Rule details of the rule engine

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: str
        :param RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        :param RulePriority: The rule priority. The greater the value, the higher the priority. The minimum value is `1`.
        :type RulePriority: int
        :param Tags: Tag of the rule.
        :type Tags: list of str
        """
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.RulePriority = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalActionParams(AbstractModel):
    """Common action parameter of a rule engine condition

    """

    def __init__(self):
        r"""
        :param Name: Parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name.
        :type Name: str
        :param Values: The parameter value.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteActionParams(AbstractModel):
    """Parameter of the action for the HTTP request/response header of a rule engine condition.

    """

    def __init__(self):
        r"""
        :param Action: Feature parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name, which has three values:
<li>add: Add the HTTP header.</li>
<li>set: Rewrite the HTTP header.</li>
<li>del: Delete the HTTP header.</li>
        :type Action: str
        :param Name: Parameter name
        :type Name: str
        :param Values: Parameter value
        :type Values: list of str
        """
        self.Action = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesProperties(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match.

    """

    def __init__(self):
        r"""
        :param Name: Parameter name.
        :type Name: str
        :param Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param Type: Parameter value type.
<li>`CHOICE`: The parameter value can be selected only from `ChoicesValue`.</li>
<li>`TOGGLE`: The parameter value is of switch type and can be selected from `ChoicesValue`.</li>
<li>`OBJECT`: The parameter value is of object type, and `ChoiceProperties` indicates the attributes associated with the object type.</li>
<li>`CUSTOM_NUM`: Custom integer</li>
<li>`CUSTOM_STRING`: Custom string.</li>Note: If `OBJECT` is selected, refer to [Example 2. Create a rule with parameters of OBJECT type](https://tcloud4api.woa.com/document/product/1657/79382?!preview&!document=1).
        :type Type: str
        :param Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param ChoiceProperties: Associated configuration parameters of this parameter, which are required for API call.
Note: This parameter will be an empty array if no special parameters are added as optional parameters.
        :type ChoiceProperties: list of RuleChoicePropertiesItem
        :param ExtraParameter: <li>NULL: No special parameters when `NormalAction` is selected for `RuleAction`.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self.Name = None
        self.Min = None
        self.ChoicesValue = None
        self.Type = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ChoiceProperties = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Min = params.get("Min")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Type = params.get("Type")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ChoiceProperties") is not None:
            self.ChoiceProperties = []
            for item in params.get("ChoiceProperties"):
                obj = RuleChoicePropertiesItem()
                obj._deserialize(item)
                self.ChoiceProperties.append(obj)
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesSettingAction(AbstractModel):
    """List of the settings of the rule engine that can be used for request match and their detailed information.

    """

    def __init__(self):
        r"""
        :param Action: Feature name. Valid values:
<li>Access URL rewrite (`AccessUrlRedirect`).</li>
<li>Origin-pull URL rewrite (`UpstreamUrlRedirect`).</li>
<li>Custom error page
(`ErrorPage`).</li>
<li>QUIC (`QUIC`).</li>
<li>WebSocket (`WebSocket`).</li>
<li>Video dragging (`VideoSeek`).</li>
<li>Token authentication (`Authentication`).</li>
<li>`CacheKey`: Custom cache key.</li>
<li>`Cache`: Node cache TTL.</li>
<li>`MaxAge`: Browser cache TTL.</li>
<li>`OfflineCache`: Offline cache.</li>
<li>`SmartRouting`: Smart acceleration.</li>
<li>`RangeOriginPull`: Range GETs.</li>
<li>`UpstreamHttp2`: HTTP/2 forwarding.</li>
<li>`HostHeader`: Host header rewrite.</li>
<li>`ForceRedirect`: Force HTTPS.</li>
<li>`OriginPullProtocol`: Origin-pull HTTPS.</li>
<li>`CachePrefresh`: Cache prefresh.</li>
<li>`Compression`: Smart compression.</li>
<li>`RequestHeader`: HTTP request header modification.</li>
<li>HTTP response header modification (`ResponseHeader`).</li>
<li>Status code cache TTL (`StatusCodeCache`).</li>
<li>`Hsts`.</li>
<li>`ClientIpHeader`.</li>
<li>`TlsVersion`.</li>
<li>`OcspStapling`.</li>
        :type Action: str
        :param Properties: Parameter information
        :type Properties: list of RulesProperties
        """
        self.Action = None
        self.Properties = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = RulesProperties()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecClientIp(AbstractModel):
    """Client IP information

    """

    def __init__(self):
        r"""
        :param ClientIp: IP of the client.
        :type ClientIp: str
        :param RequestMaxQps: Maximum QPS.
        :type RequestMaxQps: int
        :param RequestNum: Number of requests.
        :type RequestNum: int
        """
        self.ClientIp = None
        self.RequestMaxQps = None
        self.RequestNum = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RequestMaxQps = params.get("RequestMaxQps")
        self.RequestNum = params.get("RequestNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntry(AbstractModel):
    """Returned value of security data entry

    """

    def __init__(self):
        r"""
        :param Key: The query dimension value.
        :type Key: str
        :param Value: The details.
        :type Value: list of SecEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """The security data queried by metric

    """

    def __init__(self):
        r"""
        :param Metric: The metric name.
        :type Metric: str
        :param Detail: The time-series data details.
        :type Detail: list of TimingDataItem
        :param Max: The maximum value.
        :type Max: int
        :param Avg: The average value.
        :type Avg: float
        :param Sum: Sum
        :type Sum: float
        """
        self.Metric = None
        self.Detail = None
        self.Max = None
        self.Avg = None
        self.Sum = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecHitRuleInfo(AbstractModel):
    """The hit rule information

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        :param Action: Action. Values:
<li>`trans`: Allow;</li>
<li>`alg`: Algorithm challenge;</li>
<li>`drop`: Discard;</li>
<li>`ban`: Block the source IP;</li>
<li>`redirect`: Redirect;</li>
<li>`page`: Return to the specified page;</li>
<li>`monitor`: Observe.</li>
        :type Action: str
        :param HitTime: The hit time recorded in seconds using UNIX timestamp.
        :type HitTime: int
        :param RequestNum: The number of requests.
        :type RequestNum: int
        :param Description: The rule description.
        :type Description: str
        :param Domain: The subdomain name.
        :type Domain: str
        :param BotLabel: The bot tag. Values:
<li>`evil_bot`: Malicious bot</li>
<li>`suspect_bot`: Suspected bot</li>
<li>`good_bot`: Good bot</li>
<li>`normal`: Normal request</li>
<li>`none`: Uncategorized</li>
        :type BotLabel: str
        """
        self.RuleId = None
        self.RuleTypeName = None
        self.Action = None
        self.HitTime = None
        self.RequestNum = None
        self.Description = None
        self.Domain = None
        self.BotLabel = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleTypeName = params.get("RuleTypeName")
        self.Action = params.get("Action")
        self.HitTime = params.get("HitTime")
        self.RequestNum = params.get("RequestNum")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.BotLabel = params.get("BotLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecRuleRelatedInfo(AbstractModel):
    """CC/WAF/Bot security rule information

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param Action: Action. Values:
<li>`trans`: Allow;</li>
<li>`alg`: Algorithm challenge;</li>
<li>`drop`: Discard;</li>
<li>`ban`: Block the source IP;</li>
<li>`redirect`: Redirect;</li>
<li>`page`: Return to the specified page;</li>
<li>`monitor`: Observe.</li>
        :type Action: str
        :param RiskLevel: Risk level (only found in WAF logs). Values:
<li>`high risk`: High risk;</li>
<li>`middle risk`: Middle risk;</li>
<li>`low risk`: Low risk;</li>
<li>`unkonw`: Unknown.</li>
        :type RiskLevel: str
        :param RuleLevel: Rule level. Values:
<li>`normal`: Moderate.</li>
        :type RuleLevel: str
        :param Description: Rule description.
        :type Description: str
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        :param AttackContent: The attack content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        """
        self.RuleId = None
        self.Action = None
        self.RiskLevel = None
        self.RuleLevel = None
        self.Description = None
        self.RuleTypeName = None
        self.AttackContent = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Action = params.get("Action")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleLevel = params.get("RuleLevel")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.AttackContent = params.get("AttackContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """Security configuration

    """

    def __init__(self):
        r"""
        :param WafConfig: The settings of the managed rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WafConfig: :class:`tencentcloud.teo.v20220901.models.WafConfig`
        :param RateLimitConfig: The settings of the rate limiting rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220901.models.RateLimitConfig`
        :param AclConfig: The settings of the custom rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AclConfig: :class:`tencentcloud.teo.v20220901.models.AclConfig`
        :param BotConfig: The settings of the bot configuration. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BotConfig: :class:`tencentcloud.teo.v20220901.models.BotConfig`
        :param SwitchConfig: The switch setting of the layer-7 protection. If it is null, the setting that was last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SwitchConfig: :class:`tencentcloud.teo.v20220901.models.SwitchConfig`
        :param IpTableConfig: The settings of the basic access control rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpTableConfig: :class:`tencentcloud.teo.v20220901.models.IpTableConfig`
        :param ExceptConfig: The settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptConfig: :class:`tencentcloud.teo.v20220901.models.ExceptConfig`
        :param DropPageConfig: The settings of the custom block page. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DropPageConfig: :class:`tencentcloud.teo.v20220901.models.DropPageConfig`
        :param TemplateConfig: Security template settings
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TemplateConfig: :class:`tencentcloud.teo.v20220901.models.TemplateConfig`
        """
        self.WafConfig = None
        self.RateLimitConfig = None
        self.AclConfig = None
        self.BotConfig = None
        self.SwitchConfig = None
        self.IpTableConfig = None
        self.ExceptConfig = None
        self.DropPageConfig = None
        self.TemplateConfig = None


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self.WafConfig = WafConfig()
            self.WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self.RateLimitConfig = RateLimitConfig()
            self.RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        if params.get("BotConfig") is not None:
            self.BotConfig = BotConfig()
            self.BotConfig._deserialize(params.get("BotConfig"))
        if params.get("SwitchConfig") is not None:
            self.SwitchConfig = SwitchConfig()
            self.SwitchConfig._deserialize(params.get("SwitchConfig"))
        if params.get("IpTableConfig") is not None:
            self.IpTableConfig = IpTableConfig()
            self.IpTableConfig._deserialize(params.get("IpTableConfig"))
        if params.get("ExceptConfig") is not None:
            self.ExceptConfig = ExceptConfig()
            self.ExceptConfig._deserialize(params.get("ExceptConfig"))
        if params.get("DropPageConfig") is not None:
            self.DropPageConfig = DropPageConfig()
            self.DropPageConfig._deserialize(params.get("DropPageConfig"))
        if params.get("TemplateConfig") is not None:
            self.TemplateConfig = TemplateConfig()
            self.TemplateConfig._deserialize(params.get("TemplateConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityEntity(AbstractModel):
    """Protected resource

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Entity: The subdomain name/layer-4 proxy
        :type Entity: str
        :param EntityType: The type. Values:
<li>`domain`: Layer-7 subdomain name</li>
<li>`application`: Layer-4 proxy name</li>
        :type EntityType: str
        """
        self.ZoneId = None
        self.Entity = None
        self.EntityType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.EntityType = params.get("EntityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityType(AbstractModel):
    """The security type setting item.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the security type setting. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Type: Type of the certificate. Values:
<li>`default`: Default certificate</lil>
<li>`upload`: Specified certificate</li>
<li>`managed`: Tencent Cloud-managed certificate</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Time when the certificate is deployed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param SignAlgo: Signature algorithm.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SignAlgo: str
        :param CommonName: Domain name of the certificate.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CommonName: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.SignAlgo = None
        self.CommonName = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.SignAlgo = params.get("SignAlgo")
        self.CommonName = params.get("CommonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldArea(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param Type: The type of protected resources. Values:
<li>`domain`: Layer-7 subdomain name</li>
<li>`application`: Layer-4 proxy</li>
        :type Type: str
        :param EntityName: The layer-7 site name.
        :type EntityName: str
        :param DDoSHosts: The layer-7 subdomain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoSHosts: list of DDoSHost
        :param TcpNum: Number of layer-4 TCP forwarding rules
        :type TcpNum: int
        :param UdpNum: Number of layer-4 UDP forwarding rules
        :type UdpNum: int
        :param Entity: Name of the protected resource
        :type Entity: str
        """
        self.ZoneId = None
        self.PolicyId = None
        self.Type = None
        self.EntityName = None
        self.DDoSHosts = None
        self.TcpNum = None
        self.UdpNum = None
        self.Entity = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PolicyId = params.get("PolicyId")
        self.Type = params.get("Type")
        self.EntityName = params.get("EntityName")
        if params.get("DDoSHosts") is not None:
            self.DDoSHosts = []
            for item in params.get("DDoSHosts"):
                obj = DDoSHost()
                obj._deserialize(item)
                self.DDoSHosts.append(obj)
        self.TcpNum = params.get("TcpNum")
        self.UdpNum = params.get("UdpNum")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleDataRecord(AbstractModel):
    """The dimensional data record

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param TypeValue: Value of the metric under the query dimension.
        :type TypeValue: list of SingleTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = SingleTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleTypeValue(AbstractModel):
    """The dimensional data

    """

    def __init__(self):
        r"""
        :param MetricName: The metric name.
        :type MetricName: str
        :param DetailData: The metric value.
        :type DetailData: int
        """
        self.MetricName = None
        self.DetailData = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.DetailData = params.get("DetailData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCondition(AbstractModel):
    """Exception rule conditions, used to filter requests by specific fields

    """

    def __init__(self):
        r"""
        :param Type: The field type. Values:
<li>`header_fields`: HTTP request header</li>
<li>`cookie`: HTTP request cookie</li>
<li>`query_string`: Query string in the HTTP request URL</li>
<li>`uri`: HTTP request URI</li>
<li>`body_raw`: HTTP request body</li>
<li>`body_json`: JSON HTTP request body</li>
        :type Type: str
        :param Selector: The specific field. Values:
<li>`args`: Query parameter in the URI, such as "?name1=jack&age=12"</li>
<li>`path`: Partial path in the URI, such as "/path/to/resource.jpg"</li>
<li>`full`: Full path in the URI, such as "example.com/path/to/resource.jpg?name1=jack&age=12"</li>
<li>`upload_filename`: File path segment</li>
<li>`keys`: All keys</li>
<li>`values`: Values of all keys</li>
<li>`key_value`: Key and its value</li>
        :type Selector: str
        :param MatchFromType: The match method used to match the key. Values:
<li>`equal`: Exact match</li>
<li>`wildcard`: Wildcard match (only asterisks)</li>
        :type MatchFromType: str
        :param MatchFrom: The value that matches the key.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MatchFrom: list of str
        :param MatchContentType: The match method used to match the content.
<li>`equal`: Exact match</li>
<li>`wildcard`: Wildcard match (only asterisks)</li>
        :type MatchContentType: str
        :param MatchContent: The value that matches the content.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MatchContent: list of str
        """
        self.Type = None
        self.Selector = None
        self.MatchFromType = None
        self.MatchFrom = None
        self.MatchContentType = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Selector = params.get("Selector")
        self.MatchFromType = params.get("MatchFromType")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContentType = params.get("MatchContentType")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """Smart acceleration configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable smart acceleration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingConfig(AbstractModel):
    """The site test configuration

    """

    def __init__(self):
        r"""
        :param TaskType: The task type. Values:
<li>`1`: Page performance</li>
<li>`2`: File uploads</li>
<li>`3`: File downloads</li>
<li>`4`: Port performance</li>
<li>`5`: Network quality</li>
<li>`6`: Audio/Video experience</li>
        :type TaskType: int
        :param Url: The URL.
        :type Url: str
        :param UA: The user agent.
        :type UA: str
        :param Connectivity: The network type.
        :type Connectivity: str
        """
        self.TaskType = None
        self.Url = None
        self.UA = None
        self.Connectivity = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Url = params.get("Url")
        self.UA = params.get("UA")
        self.Connectivity = params.get("Connectivity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingDetailData(AbstractModel):
    """The site’s load speed across regions.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param DistrictStatistics: The site performance across regions.
        :type DistrictStatistics: list of DistrictStatistics
        """
        self.ZoneId = None
        self.ZoneName = None
        self.DistrictStatistics = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("DistrictStatistics") is not None:
            self.DistrictStatistics = []
            for item in params.get("DistrictStatistics"):
                obj = DistrictStatistics()
                obj._deserialize(item)
                self.DistrictStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingInfo(AbstractModel):
    """The site test information

    """

    def __init__(self):
        r"""
        :param StatusCode: The task status. Values:
<li>`200`: The task completed.</li>
<li>`100`: The task is running.</li>
<li>`503`: The task failed.</li>
        :type StatusCode: int
        :param TestId: ID of the site test task.
        :type TestId: str
        :param SpeedTestingConfig: The settings of the site test task.
        :type SpeedTestingConfig: :class:`tencentcloud.teo.v20220901.models.SpeedTestingConfig`
        :param SpeedTestingStatistics: The site test result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpeedTestingStatistics: :class:`tencentcloud.teo.v20220901.models.SpeedTestingStatistics`
        """
        self.StatusCode = None
        self.TestId = None
        self.SpeedTestingConfig = None
        self.SpeedTestingStatistics = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.TestId = params.get("TestId")
        if params.get("SpeedTestingConfig") is not None:
            self.SpeedTestingConfig = SpeedTestingConfig()
            self.SpeedTestingConfig._deserialize(params.get("SpeedTestingConfig"))
        if params.get("SpeedTestingStatistics") is not None:
            self.SpeedTestingStatistics = SpeedTestingStatistics()
            self.SpeedTestingStatistics._deserialize(params.get("SpeedTestingStatistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingMetricData(AbstractModel):
    """The site test metrics.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param OriginSpeedTestingInfo: The origin information.
        :type OriginSpeedTestingInfo: list of SpeedTestingInfo
        :param ProxySpeedTestingInfo: The EdgeOne information.
        :type ProxySpeedTestingInfo: list of SpeedTestingInfo
        :param SpeedTestingStatus: The site status.
        :type SpeedTestingStatus: :class:`tencentcloud.teo.v20220901.models.SpeedTestingStatus`
        :param OptimizeAction: The optimization suggestions.
        :type OptimizeAction: list of OptimizeAction
        :param ProxyLoadTime: The EdgeOne load time, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyLoadTime: int
        :param OriginLoadTime: The origin load time, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginLoadTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginSpeedTestingInfo = None
        self.ProxySpeedTestingInfo = None
        self.SpeedTestingStatus = None
        self.OptimizeAction = None
        self.ProxyLoadTime = None
        self.OriginLoadTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("OriginSpeedTestingInfo") is not None:
            self.OriginSpeedTestingInfo = []
            for item in params.get("OriginSpeedTestingInfo"):
                obj = SpeedTestingInfo()
                obj._deserialize(item)
                self.OriginSpeedTestingInfo.append(obj)
        if params.get("ProxySpeedTestingInfo") is not None:
            self.ProxySpeedTestingInfo = []
            for item in params.get("ProxySpeedTestingInfo"):
                obj = SpeedTestingInfo()
                obj._deserialize(item)
                self.ProxySpeedTestingInfo.append(obj)
        if params.get("SpeedTestingStatus") is not None:
            self.SpeedTestingStatus = SpeedTestingStatus()
            self.SpeedTestingStatus._deserialize(params.get("SpeedTestingStatus"))
        if params.get("OptimizeAction") is not None:
            self.OptimizeAction = []
            for item in params.get("OptimizeAction"):
                obj = OptimizeAction()
                obj._deserialize(item)
                self.OptimizeAction.append(obj)
        self.ProxyLoadTime = params.get("ProxyLoadTime")
        self.OriginLoadTime = params.get("OriginLoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingQuota(AbstractModel):
    """The quota limit on site tests.

    """

    def __init__(self):
        r"""
        :param TotalTestRuns: The total number of site tests.
        :type TotalTestRuns: int
        :param AvailableTestRuns: The number of available site tests.
        :type AvailableTestRuns: int
        """
        self.TotalTestRuns = None
        self.AvailableTestRuns = None


    def _deserialize(self, params):
        self.TotalTestRuns = params.get("TotalTestRuns")
        self.AvailableTestRuns = params.get("AvailableTestRuns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingStatistics(AbstractModel):
    """The site test result

    """

    def __init__(self):
        r"""
        :param FirstContentfulPaint: Last contentful paint, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstContentfulPaint: int
        :param FirstMeaningfulPaint: Full content load, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstMeaningfulPaint: int
        :param OverallDownloadSpeed: Average download speed, in KB/s.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OverallDownloadSpeed: float
        :param RenderTime: Rendering time, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenderTime: int
        :param DocumentFinishTime: DOM content loaded, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentFinishTime: int
        :param TcpConnectionTime: Average TCP connection, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TcpConnectionTime: int
        :param ResponseTime: Average backend response, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResponseTime: int
        :param FileDownloadTime: Average DOM content download, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileDownloadTime: int
        :param LoadTime: Load time, in milliseconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadTime: int
        """
        self.FirstContentfulPaint = None
        self.FirstMeaningfulPaint = None
        self.OverallDownloadSpeed = None
        self.RenderTime = None
        self.DocumentFinishTime = None
        self.TcpConnectionTime = None
        self.ResponseTime = None
        self.FileDownloadTime = None
        self.LoadTime = None


    def _deserialize(self, params):
        self.FirstContentfulPaint = params.get("FirstContentfulPaint")
        self.FirstMeaningfulPaint = params.get("FirstMeaningfulPaint")
        self.OverallDownloadSpeed = params.get("OverallDownloadSpeed")
        self.RenderTime = params.get("RenderTime")
        self.DocumentFinishTime = params.get("DocumentFinishTime")
        self.TcpConnectionTime = params.get("TcpConnectionTime")
        self.ResponseTime = params.get("ResponseTime")
        self.FileDownloadTime = params.get("FileDownloadTime")
        self.LoadTime = params.get("LoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingStatus(AbstractModel):
    """The test task status

    """

    def __init__(self):
        r"""
        :param Url: The URL.
        :type Url: str
        :param Tls: Whether the URL uses HTTPS.
        :type Tls: bool
        :param CreatedOn: Creation time of the task.
        :type CreatedOn: str
        :param StatusCode: The task status. Values:
<li>`200`: The task completed.</li>
<li>`100`: The task is running.</li>
<li>`503`: The task failed./li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusCode: int
        :param UA: The user agent.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UA: str
        :param Connectivity: The network environment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Connectivity: str
        :param Reachable: Whether the URL is reachable. Values:
<li>`true`: Yes</li>
<li>`false`: No</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reachable: bool
        :param TimedOut: Whether the URL connection timed out. Values:
<li>`true`: Yes</li>
<li>`false`: No</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimedOut: bool
        """
        self.Url = None
        self.Tls = None
        self.CreatedOn = None
        self.StatusCode = None
        self.UA = None
        self.Connectivity = None
        self.Reachable = None
        self.TimedOut = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Tls = params.get("Tls")
        self.CreatedOn = params.get("CreatedOn")
        self.StatusCode = params.get("StatusCode")
        self.UA = params.get("UA")
        self.Connectivity = params.get("Connectivity")
        self.Reachable = params.get("Reachable")
        self.TimedOut = params.get("TimedOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRule(AbstractModel):
    """Nested rule settings

    """

    def __init__(self):
        r"""
        :param Conditions: The condition that determines if a feature should run.
Note: If any condition in the array is met, the feature will run.
        :type Conditions: list of RuleAndConditions
        :param Actions: The feature to be executed.
        :type Actions: list of Action
        """
        self.Conditions = None
        self.Actions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRuleItem(AbstractModel):
    """Rule engine nested rule

    """

    def __init__(self):
        r"""
        :param Rules: Nested rule settings
        :type Rules: list of SubRule
        :param Tags: Tag of the rule.
        :type Tags: list of str
        """
        self.Rules = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = SubRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """Pricing query parameter

    """

    def __init__(self):
        r"""
        :param Key: The parameter key.
        :type Key: str
        :param Value: The parameter value.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    """Web security configuration switch

    """

    def __init__(self):
        r"""
        :param WebSwitch: Whether to enable web protection. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>It does not affect DDoS and bot configuration.
        :type WebSwitch: str
        """
        self.WebSwitch = None


    def _deserialize(self, params):
        self.WebSwitch = params.get("WebSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchLogTopicTaskRequest(AbstractModel):
    """SwitchLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID of the shipping task.
        :type TopicId: str
        :param IsOpen: Whether to enable the shipping task. Values:
<li>`true`: Enable the shipping task;</li>
<li>`false`: Disable the shipping task.</li>
        :type IsOpen: bool
        """
        self.TopicId = None
        self.IsOpen = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchLogTopicTaskResponse(AbstractModel):
    """SwitchLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag configuration

    """

    def __init__(self):
        r"""
        :param TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param Status: Status of the task.
        :type Status: str
        :param Target: Resource.
        :type Target: str
        :param Type: Type of the task.
        :type Type: str
        :param CreateTime: Creation time of the task.
        :type CreateTime: str
        :param UpdateTime: Completion time of the task.
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateConfig(AbstractModel):
    """Security template settings

    """

    def __init__(self):
        r"""
        :param TemplateId: The template ID.
        :type TemplateId: str
        :param TemplateName: The template name.
        :type TemplateName: str
        """
        self.TemplateId = None
        self.TemplateName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """Data items of the statistical curve

    """

    def __init__(self):
        r"""
        :param Timestamp: The query time recorded in seconds using UNIX timestamp.
        :type Timestamp: int
        :param Value: The value.
        :type Value: int
        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """The time-series data

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param TypeValue: Detailed time series data
        :type TypeValue: list of TimingTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """Detailed data of time series type

    """

    def __init__(self):
        r"""
        :param Sum: Sum.
        :type Sum: int
        :param Max: The maximum value.
        :type Max: int
        :param Avg: The average value.
        :type Avg: int
        :param MetricName: Metric name.
        :type MetricName: str
        :param Detail: Details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        """
        self.Sum = None
        self.Max = None
        self.Avg = None
        self.MetricName = None
        self.Detail = None


    def _deserialize(self, params):
        self.Sum = params.get("Sum")
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.MetricName = params.get("MetricName")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """The top-ranked data record

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param DetailData: Top data rankings
        :type DetailData: list of TopDetailData
        """
        self.TypeKey = None
        self.DetailData = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """The top-ranked data details

    """

    def __init__(self):
        r"""
        :param Key: The field name.
        :type Key: str
        :param Value: The field value.
        :type Value: int
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntry(AbstractModel):
    """The Top-ranked data

    """

    def __init__(self):
        r"""
        :param Key: The query dimension value.
        :type Key: str
        :param Value: The details.
        :type Value: list of TopEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = TopEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntryValue(AbstractModel):
    """The top-ranked data

    """

    def __init__(self):
        r"""
        :param Name: The item name.
        :type Name: str
        :param Count: The number of items.
        :type Count: int
        """
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """HTTP2 origin-pull configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable HTTP2 origin-pull. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """Custom name servers

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable custom name servers. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Servers: List of custom name servers
        :type Servers: list of str
        """
        self.Switch = None
        self.Servers = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """IP information of the custom name server

    """

    def __init__(self):
        r"""
        :param Name: Custom name of the name server
        :type Name: str
        :param IPv4: IPv4 address of the custom name server
        :type IPv4: str
        """
        self.Name = None
        self.IPv4 = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Waf(AbstractModel):
    """N/A

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WAF. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param PolicyId: ID of the policy
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafConfig(AbstractModel):
    """WAF configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WAF configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>The configuration can be modified even when it is disabled.
        :type Switch: str
        :param Level: The protection level. Values:
<li>`loose`: Loose</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`stricter`: Super strict</li>
<li>`custom`: Custom</li>
        :type Level: str
        :param Mode: The WAF global mode. Values:
<li>`block`: Block globally</li>
<li>`observe`: Observe globally</li>
        :type Mode: str
        :param WafRule: The settings of the managed rule. If it is null, the settings that were last configured will be used.
        :type WafRule: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param AiRule: The setting of the AI rule engine. If it is null, the setting that was last configured will be used.
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        """
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRule = None
        self.AiRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRule") is not None:
            self.WafRule = WafRule()
            self.WafRule._deserialize(params.get("WafRule"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafGroup(AbstractModel):
    """WAF managed rule group

    """

    def __init__(self):
        r"""
        :param Action: Action to be executed. Values:
<li>`block`: Block</li>
<li>`observe: Observe</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param Level: The protection level. Values:
<li>`loose`: Loose</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`stricter`: Super strict</li>
<li>`custom`: Custom</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: str
        :param TypeId: ID of the rule type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TypeId: int
        """
        self.Action = None
        self.Level = None
        self.TypeId = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Level = params.get("Level")
        self.TypeId = params.get("TypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafGroupDetail(AbstractModel):
    """Details of the managed rule group

    """

    def __init__(self):
        r"""
        :param RuleTypeId: ID of the rule type.
        :type RuleTypeId: int
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        :param RuleTypeDesc: Description of the rule type.
        :type RuleTypeDesc: str
        :param WafGroupRules: List of rules.
        :type WafGroupRules: list of WafGroupRule
        :param Level: The rule level.
        :type Level: str
        :param Action: The rule action.
        :type Action: str
        """
        self.RuleTypeId = None
        self.RuleTypeName = None
        self.RuleTypeDesc = None
        self.WafGroupRules = None
        self.Level = None
        self.Action = None


    def _deserialize(self, params):
        self.RuleTypeId = params.get("RuleTypeId")
        self.RuleTypeName = params.get("RuleTypeName")
        self.RuleTypeDesc = params.get("RuleTypeDesc")
        if params.get("WafGroupRules") is not None:
            self.WafGroupRules = []
            for item in params.get("WafGroupRules"):
                obj = WafGroupRule()
                obj._deserialize(item)
                self.WafGroupRules.append(obj)
        self.Level = params.get("Level")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafGroupInfo(AbstractModel):
    """The managed rule

    """

    def __init__(self):
        r"""
        :param WafGroupDetails: List of managed rule groups.
        :type WafGroupDetails: list of WafGroupDetail
        :param Level: The level of the managed rule group
<li>`loose`: Loose</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`stricter`: Super strict</li>
        :type Level: str
        :param Act: Reserved field.
        :type Act: str
        :param Mode: The mode. Values:
<li>`block`: Block</li>
<li>`observe`: Observer</li>
        :type Mode: str
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.WafGroupDetails = None
        self.Level = None
        self.Act = None
        self.Mode = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("WafGroupDetails") is not None:
            self.WafGroupDetails = []
            for item in params.get("WafGroupDetails"):
                obj = WafGroupDetail()
                obj._deserialize(item)
                self.WafGroupDetails.append(obj)
        self.Level = params.get("Level")
        self.Act = params.get("Act")
        self.Mode = params.get("Mode")
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafGroupRule(AbstractModel):
    """The managed rule details

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param Description: The rule description.
        :type Description: str
        :param RuleLevelDesc: The description of the rule level.
        :type RuleLevelDesc: str
        :param RuleTags: The rule tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleTags: list of str
        :param UpdateTime: The update time in the format of YYYY-MM-DD hh:mm:ss.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param Status: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>It can be left empty when you query a managed rule.
        :type Status: str
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        :param RuleTypeId: ID of the rule type.
        :type RuleTypeId: int
        :param RuleTypeDesc: Description of the rule type.
        :type RuleTypeDesc: str
        """
        self.RuleId = None
        self.Description = None
        self.RuleLevelDesc = None
        self.RuleTags = None
        self.UpdateTime = None
        self.Status = None
        self.RuleTypeName = None
        self.RuleTypeId = None
        self.RuleTypeDesc = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleLevelDesc = params.get("RuleLevelDesc")
        self.RuleTags = params.get("RuleTags")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.RuleTypeName = params.get("RuleTypeName")
        self.RuleTypeId = params.get("RuleTypeId")
        self.RuleTypeDesc = params.get("RuleTypeDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRule(AbstractModel):
    """WAF rule

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable managed rules. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param BlockRuleIDs: IDs of the managed rules in the Block mode. You can obtain more details from [DescribeSecurityGroupManagedRules](https://tcloud4api.woa.com/document/product/1657/80807?!preview&!document=1).
        :type BlockRuleIDs: list of int
        :param ObserveRuleIDs: IDs of the managed rules in the Observe mode. You can obtain more details from [DescribeSecurityGroupManagedRules](https://tcloud4api.woa.com/document/product/1657/80807?!preview&!document=1).
        :type ObserveRuleIDs: list of int
        """
        self.Switch = None
        self.BlockRuleIDs = None
        self.ObserveRuleIDs = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockRuleIDs = params.get("BlockRuleIDs")
        self.ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogs(AbstractModel):
    """Web attack log

    """

    def __init__(self):
        r"""
        :param EventId: The attack event ID.
        :type EventId: str
        :param AttackIp: The attacker IP.
        :type AttackIp: str
        :param Domain: The attacked subdomain name.
        :type Domain: str
        :param HttpLog: The HTTP log content.
        :type HttpLog: str
        :param SipCountryCode: The country code of the attacker IP, which is defined in ISO-3166 alpha-2. For the list of country codes, see [ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json).
        :type SipCountryCode: str
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        :param RequestUri: The request address.
        :type RequestUri: str
        :param AttackContent: The attack content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param RuleDetailList: The security rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param ReqMethod: The request type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReqMethod: str
        """
        self.EventId = None
        self.AttackIp = None
        self.Domain = None
        self.HttpLog = None
        self.SipCountryCode = None
        self.AttackTime = None
        self.RequestUri = None
        self.AttackContent = None
        self.RuleDetailList = None
        self.ReqMethod = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AttackIp = params.get("AttackIp")
        self.Domain = params.get("Domain")
        self.HttpLog = params.get("HttpLog")
        self.SipCountryCode = params.get("SipCountryCode")
        self.AttackTime = params.get("AttackTime")
        self.RequestUri = params.get("RequestUri")
        self.AttackContent = params.get("AttackContent")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.ReqMethod = params.get("ReqMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WebSocket connection timeout. Values:
<li>`on`: The field "Timeout" can be configured.</li>
<li>`off`: The field "Timeout" is fixed to 15 seconds.</li>
        :type Switch: str
        :param Timeout: The timeout period in seconds. Maximum value: 120.
        :type Timeout: int
        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """Site information

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param NameServers: The list of name servers assigned by Tencent Cloud.
        :type NameServers: list of str
        :param Status: The site status. Values:
<li>`active`: The name server is switched.</li>
<li>`pending`: The name server is not switched.</li>
<li>`moved`: The name server is moved.</li>
<li>`deactivated`: The site is blocked.</li>
        :type Status: str
        :param Type: The site access method. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>
        :type Type: str
        :param Paused: Whether the site is disabled.
        :type Paused: bool
        :param CnameSpeedUp: Whether CNAME acceleration is enabled. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type CnameSpeedUp: str
        :param CnameStatus: CNAME record access status. Values:
<li>`finished`: The site is verified.</li>
<li>`pending`: The site is being verified.</li>
        :type CnameStatus: str
        :param Tags: The list of resource tags.
        :type Tags: list of Tag
        :param Resources: The list of billable resources.
        :type Resources: list of Resource
        :param CreatedOn: The creation time of the site.
        :type CreatedOn: str
        :param ModifiedOn: The modification date of the site.
        :type ModifiedOn: str
        :param Area: The site access region. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param VanityNameServers: The custom name server information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param VanityNameServersIps: The custom name server IP information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        :param ActiveStatus: Status of the proxy. Values:
<li>`active`: Enabled</li>
<li>`inactive`: Not activated</li>
<li>`paused`: Disabled</li>
        :type ActiveStatus: str
        :param AliasZoneName: The site alias. It can be up to 20 characters consisting of digits, letters, hyphens (-) and underscores (_).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AliasZoneName: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Resources = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Area = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.ActiveStatus = None
        self.AliasZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Area = params.get("Area")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.ActiveStatus = params.get("ActiveStatus")
        self.AliasZoneName = params.get("AliasZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """The site configuration.

    """

    def __init__(self):
        r"""
        :param ZoneName: Name of the site
        :type ZoneName: str
        :param Area: Site acceleration region. Values:
<li>`mainland`: Acceleration in the Chinese mainland.</li>
<li>`overseas`: Acceleration outside the Chinese mainland.</li>
        :type Area: str
        :param CacheKey: Node cache key configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Quic: The QUIC access configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: The POST transport configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: Smart compression configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param CacheConfig: Cache expiration time configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: Origin server configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: Smart acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param MaxAge: Browser cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: The offline cache configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param WebSocket: WebSocket configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: Cache prefresh configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: IPv6 access configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param Https: HTTPS acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param ClientIpCountry: Whether to carry the location information of the client IP during origin-pull.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneName = None
        self.Area = None
        self.CacheKey = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.CacheConfig = None
        self.Origin = None
        self.SmartRouting = None
        self.MaxAge = None
        self.OfflineCache = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.Https = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Area = params.get("Area")
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        