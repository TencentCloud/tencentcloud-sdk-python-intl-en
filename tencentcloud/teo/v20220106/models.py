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


class ACLCondition(AbstractModel):
    """Condition that makes up an access control rule

    """

    def __init__(self):
        r"""
        :param MatchFrom: Field to match
        :type MatchFrom: str
        :param MatchParam: String to match
        :type MatchParam: str
        :param Operator: Relation between the field and content
        :type Operator: str
        :param MatchContent: Content to match
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
        


class ACLUserRule(AbstractModel):
    """Custom ACL rule

    """

    def __init__(self):
        r"""
        :param RuleName: Name of the rule
        :type RuleName: str
        :param Action: Action
        :type Action: str
        :param RuleStatus: Status of the rule
        :type RuleStatus: str
        :param Conditions: ACL rule
        :type Conditions: list of ACLCondition
        :param RulePriority: Priority of the rule
        :type RulePriority: int
        :param RuleID: ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param PunishTime: IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param PunishTimeUnit: IP blocking time unit
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTimeUnit: str
        :param Name: Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Name: str
        :param PageId: ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageId: int
        :param RedirectUrl: Redirection URL, which must be a subdomain name of the site
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectUrl: str
        :param ResponseCode: Return code configured on the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseCode: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.Conditions = None
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
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
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
        


class AclConfig(AbstractModel):
    """ACL configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch
        :type Switch: str
        :param UserRules: ACL user rule
        :type UserRules: list of ACLUserRule
        """
        self.Switch = None
        self.UserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self.UserRules = []
            for item in params.get("UserRules"):
                obj = ACLUserRule()
                obj._deserialize(item)
                self.UserRules.append(obj)
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
        :param Mode: `smart_status_close`: Disable; `smart_status_open`: Block;
`smart_status_observe`: Observe.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class ApplicationProxy(AbstractModel):
    """Application proxy instance

    """

    def __init__(self):
        r"""
        :param ProxyId: ID of the proxy
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyId: str
        :param ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param PlatType: Scheduling mode:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        :param Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param ScheduleValue: Scheduling information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ScheduleValue: list of str
        :param UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param ZoneId: Site ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneId: str
        :param ZoneName: Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneName: str
        :param SessionPersistTime: Session persistence duration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyType: str
        :param HostId: When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name;
`HostId` indicates a unique ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
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
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param OriginValue: Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param RuleId: Rule ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleId: str
        :param Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
        :type Status: str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotConfig(AbstractModel):
    """Bot security configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable bot security configuration
        :type Switch: str
        :param ManagedRule: Preset rules
        :type ManagedRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param UaBotRule: Not supported currently
        :type UaBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param IspBotRule: Not supported currently
        :type IspBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param PortraitRule: User portrait rules
        :type PortraitRule: :class:`tencentcloud.teo.v20220106.models.BotPortraitRule`
        :param IntelligenceRule: Bot intelligence rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220106.models.IntelligenceRule`
        """
        self.Switch = None
        self.ManagedRule = None
        self.UaBotRule = None
        self.IspBotRule = None
        self.PortraitRule = None
        self.IntelligenceRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ManagedRule") is not None:
            self.ManagedRule = BotManagedRule()
            self.ManagedRule._deserialize(params.get("ManagedRule"))
        if params.get("UaBotRule") is not None:
            self.UaBotRule = BotManagedRule()
            self.UaBotRule._deserialize(params.get("UaBotRule"))
        if params.get("IspBotRule") is not None:
            self.IspBotRule = BotManagedRule()
            self.IspBotRule._deserialize(params.get("IspBotRule"))
        if params.get("PortraitRule") is not None:
            self.PortraitRule = BotPortraitRule()
            self.PortraitRule._deserialize(params.get("PortraitRule"))
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
        :param AttackTime: Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        :param AttackIp: Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackIp: str
        :param Domain: Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param AttackType: Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param RequestMethod: Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestMethod: str
        :param AttackContent: Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param RuleId: Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param Ua: user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ua: str
        :param DetectionMethod: Detection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetectionMethod: str
        :param Confidence: Confidence
Note: This field may return null, indicating that no valid values can be obtained.
        :type Confidence: str
        :param Maliciousness: Maliciousness
Note: This field may return null, indicating that no valid values can be obtained.
        :type Maliciousness: str
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLogData(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param List: Data set of bot attack logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of BotLog
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BotLog()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot managed rules

    """

    def __init__(self):
        r"""
        :param ManagedIds: ID of the rule to be enabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ManagedIds: list of int
        :param RuleID: ID of the rule being applied
        :type RuleID: int
        :param Action: Action of the rule. Values: `drop`; `trans`; `monitor`; `alg`.
        :type Action: str
        :param PunishTime: The amount of time the IP is blocked
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param PunishTimeUnit: Unit of IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTimeUnit: str
        :param Name: Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Name: str
        :param PageId: ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageId: int
        :param RedirectUrl: Redirection URL, which must be a subdomain name of your site encoded by URLEncode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectUrl: str
        :param ResponseCode: Response code returned after redirection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseCode: int
        :param TransManagedIds: ID of the rule that is set to allow requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TransManagedIds: list of int
        :param AlgManagedIds: ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlgManagedIds: list of int
        :param CapManagedIds: ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CapManagedIds: list of int
        :param MonManagedIds: ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MonManagedIds: list of int
        :param DropManagedIds: ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DropManagedIds: list of int
        """
        self.ManagedIds = None
        self.RuleID = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.Name = None
        self.PageId = None
        self.RedirectUrl = None
        self.ResponseCode = None
        self.TransManagedIds = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.ManagedIds = params.get("ManagedIds")
        self.RuleID = params.get("RuleID")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.Name = params.get("Name")
        self.PageId = params.get("PageId")
        self.RedirectUrl = params.get("RedirectUrl")
        self.ResponseCode = params.get("ResponseCode")
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
        :param RuleId: ID of the rule
        :type RuleId: int
        :param Description: Rule description
        :type Description: str
        :param RuleTypeName: Rule type
        :type RuleTypeName: str
        :param Status: Whether the rule is enabled
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
        :param RuleID: ID of the rule being applied
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param AlgManagedIds: ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlgManagedIds: list of int
        :param CapManagedIds: ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CapManagedIds: list of int
        :param MonManagedIds: ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MonManagedIds: list of int
        :param DropManagedIds: ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DropManagedIds: list of int
        :param Switch: Feature switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.RuleID = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None
        self.Switch = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        self.Switch = params.get("Switch")
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
        :param ClientIp: Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIp: str
        :param InterceptNum: Number of blocks per minute
Note: This field may return null, indicating that no valid values can be obtained.
        :type InterceptNum: int
        :param InterceptTime: Block time in rate-limiting policy per minute in seconds
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
        


class CCInterceptEventData(AbstractModel):
    """CC block event data

    """

    def __init__(self):
        r"""
        :param List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CCInterceptEvent
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CCInterceptEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLog(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param AttackTime: Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        :param AttackSip: Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackSip: str
        :param AttackDomain: Attack domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackDomain: str
        :param RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param HitCount: Number of hits
Note: This field may return null, indicating that no valid values can be obtained.
        :type HitCount: int
        :param SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param RuleId: Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        """
        self.AttackTime = None
        self.AttackSip = None
        self.AttackDomain = None
        self.RequestUri = None
        self.HitCount = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.RuleId = None
        self.RiskLevel = None


    def _deserialize(self, params):
        self.AttackTime = params.get("AttackTime")
        self.AttackSip = params.get("AttackSip")
        self.AttackDomain = params.get("AttackDomain")
        self.RequestUri = params.get("RequestUri")
        self.HitCount = params.get("HitCount")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.RuleId = params.get("RuleId")
        self.RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLogData(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param List: Data set of CC block logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CCLog
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CCLog()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration

    """

    def __init__(self):
        r"""
        :param Cache: Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param NoCache: No-cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param FollowOrigin: Follows the origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param Switch: Cache configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTime: int
        :param IgnoreCacheControl: Specifies whether to enable force cache
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CacheConfigFollowOrigin(AbstractModel):
    """Follows the origin server configuration

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to follow the origin server configuration
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CacheConfigNoCache(AbstractModel):
    """Do not cache the configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to cache the configuration
`on`: Do not cache
`off`: Cache
Note: This field may return `null`, indicating that no valid values can be obtained.
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
        


class CacheKey(AbstractModel):
    """Cache key configuration

    """

    def __init__(self):
        r"""
        :param FullUrlCache: Specifies whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String)
`off`: Disable full-path cache (i.e., enable Ignore Query String)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullUrlCache: str
        :param IgnoreCase: Specifies whether the cache key is case sensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220106.models.QueryString`
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
        :param Switch: Configuration switch
        :type Switch: str
        :param Percent: Cache prefresh percentage. Values: 1-99
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
        


class CertFilter(AbstractModel):
    """Query filter to search for certificates

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Values:
 - `host`: Domain name
 - `certId`: Certificate ID
 - `certAlias`: Certificate alias
 - `certType: default`: Default certificate; `upload`: External certificate; `managed`: Tencent Cloud certificate.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query, which only supports the `host` field.
If it is enabled, the length of `Value` must be 1.
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
        


class CertSort(AbstractModel):
    """Sorting conditions for query results.

    """

    def __init__(self):
        r"""
        :param Key: Fields that can be sorted. Values:
`createTime`: Domain name creation time
`certExpireTime`: Certificate expiration time
`certDeployTime`: Certificate deployment time
        :type Key: str
        :param Sequence: Sorting order. Valid values: `asc` and `desc` (default).
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
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
        :param Certificate: Certificate
        :type Certificate: str
        :param PrivateKey: Private key
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


class ClientIp(AbstractModel):
    """Client IP header

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to enable client IP header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param HeaderName: Name of the origin-pull client IP request header
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CnameStatus(AbstractModel):
    """CNAME status

    """

    def __init__(self):
        r"""
        :param Name: Record name
        :type Name: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param Status: Status
`active`: Activated
`moved`: Not activated
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self.Name = None
        self.Cname = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable Smart compression
`on`: Enable
`off`: Disable
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
        


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param PlatType: Scheduling mode. Values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: Rule details
        :type Rule: list of ApplicationProxyRule
        :param SessionPersistTime: Session persistence duration. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
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
        :param ProxyId: Layer-4 application proxy ID
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
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param OriginValue: Origin information:
When `OriginType=custom`, it can include one or more origins in either of the following formats:
IP:Port
Domain name:Port
When `OriginType=origins`, it is an origin group ID.
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence 
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
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


class CreateApplicationProxyRulesRequest(AbstractModel):
    """CreateApplicationProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Rule = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRulesResponse(AbstractModel):
    """CreateApplicationProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Array of rule IDs
        :type RuleId: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateCustomErrorPageRequest(AbstractModel):
    """CreateCustomErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Entity: Subdomain name of the site
        :type Entity: str
        :param Name: Name of the file specified to be returned
        :type Name: str
        :param Content: Content of the custom page
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
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Mode: Proxy mode. Valid values: `dns_only`, `cdn_only`, and `secure_cdn`.
        :type Mode: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        :param Status: Resolution status. Valid values:
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param Locked: Whether the DNS record is locked
        :type Locked: bool
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param TTL: Indicates DNS TTL time when `Type=dns_only` 
        :type TTL: int
        """
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
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
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param OriginName: Name of the origin group
        :type OriginName: str
        :param Type: Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :type Type: str
        :param Record: Origin records
        :type Record: list of OriginRecord
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param OriginType: Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :type OriginType: str
        """
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.ZoneId = None
        self.OriginType = None


    def _deserialize(self, params):
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
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
        :param OriginId: ID of the newly added origin group
        :type OriginId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to encode the URL
Note that if it’s enabled, the purging is based on the converted URLs.
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
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Type: Type of the purging task. Values:
- `purge_url`: Purge by the URL
- `purge_prefix`: Purge by the prefix
- `purge_host`: Purge by the Hostname
- `purge_all`: Purge all cached contents
        :type Type: str
        :param Targets: Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Hostnames are purged, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Prefixes are purged, such as http://www.example.com/example.
3. When `Type = purge_url`:
URLs are purged, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`: All types of resources are purged.
`Targets` is not a required field.
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
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks and reasons
Note: This field may return `null`, indicating that no valid value can be obtained.
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


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param Type: Access mode. Valid values:
- `full` (default): Access via NS
- `partial`: Access via CNAME
        :type Type: str
        :param JumpStart: Specifies whether to skip resolution record scanning
        :type JumpStart: bool
        :param Tags: Resource tag
        :type Tags: list of Tag
        """
        self.Name = None
        self.Type = None
        self.JumpStart = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Type: Specifies how the site is connected to EdgeOne.
        :type Type: str
        :param Status: Site status
- `pending`: The name server is not switched.
- `active`: The name server is switched to another assigned.
- `moved`: Move the NS out of Tencent Cloud
        :type Status: str
        :param OriginalNameServers: List of name servers
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned to users
        :type NameServers: list of str
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Status = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DDoSAcl(AbstractModel):
    """DDoS port filtering configuration

    """

    def __init__(self):
        r"""
        :param DportEnd: Destination port used as the end port
        :type DportEnd: int
        :param DportStart: Destination port used as the start port
        :type DportStart: int
        :param SportEnd: Source port used as the end port
        :type SportEnd: int
        :param SportStart: Source port used as the start port
        :type SportStart: int
        :param Protocol: Protocol. Values: `tcp`, `udp`, and `all`.
        :type Protocol: str
        :param Action: Action. Values: `drop` (Drop the request); `transmit` (Allow the request); `forward` (Continue to offer protection).
        :type Action: str
        :param Default: Whether it is a system configuration. Values: `0` (manual configuration); `1` (system configuration).
        :type Default: int
        """
        self.DportEnd = None
        self.DportStart = None
        self.SportEnd = None
        self.SportStart = None
        self.Protocol = None
        self.Action = None
        self.Default = None


    def _deserialize(self, params):
        self.DportEnd = params.get("DportEnd")
        self.DportStart = params.get("DportStart")
        self.SportEnd = params.get("SportEnd")
        self.SportStart = params.get("SportStart")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        self.Default = params.get("Default")
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
        :param DropTcp: Enables TCP protocol blocking. `on` (enable); `off` (disable).
        :type DropTcp: str
        :param DropUdp: Enables UDP protocol blocking. `on` (enable); `off` (disable).
        :type DropUdp: str
        :param DropIcmp: Enables ICMP protocol blocking. `on` (enable); `off` (disable).
        :type DropIcmp: str
        :param DropOther: Enables blocking for other protocols. `on` (enable); `off` (disable).
        :type DropOther: str
        :param SourceCreateLimit: Number of new connections the source port can establish. Value range: 0-4294967295.
        :type SourceCreateLimit: int
        :param SourceConnectLimit: Number of concurrent connections the source port can establish. Value range: 0-4294967295.
        :type SourceConnectLimit: int
        :param DestinationCreateLimit: Number of new connections the destination port can establish. Value range: 0-4294967295.
        :type DestinationCreateLimit: int
        :param DestinationConnectLimit: Number of concurrent connections the destination port can establish. Value range: 0-4294967295.
        :type DestinationConnectLimit: int
        :param AbnormalConnectNum: Number of abnormal connections allowed. Value range: 0-4294967295.
        :type AbnormalConnectNum: int
        :param AbnormalSynRatio: Specifies the ratio of SYN exceptions to trigger alerts. Value range: 0-100
        :type AbnormalSynRatio: int
        :param AbnormalSynNum: Specifies a max number of SYN packets that triggers alarms. Value range: 0-65535
        :type AbnormalSynNum: int
        :param ConnectTimeout: Connection timeout period. Value range: 0-65535.
        :type ConnectTimeout: int
        :param EmptyConnectProtect: Whether to enable null session protection. `0`: Disable; `1`: Enable.
        :type EmptyConnectProtect: str
        :param UdpShard: Whether to enable UDP fragmentation. `off`: Disable; `on`: Enable.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class DDoSApplication(AbstractModel):
    """DDoS protection for the application layer (layer 7)

    """

    def __init__(self):
        r"""
        :param Host: Second-level domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Host: str
        :param Status: Status of the domain name
`init`: NS to be switched
`offline`: Site acceleration not enabled with DNS
`process`: Deployment in progress
`online`: Normal
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param AccelerateType: Site acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `SecurityType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccelerateType: str
        :param SecurityType: Security acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `AccelerateType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class DDoSConfig(AbstractModel):
    """DDoS configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch
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
        


class DDoSFeaturesFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param Action: Action. `drop`: Drop the request; `transmit`: Allow the request; `drop_block`: Drop the request and block it; `forward`: Continue to offer protection.
        :type Action: str
        :param Depth: Sets how far from the first search position
        :type Depth: int
        :param Depth2: Sets how far from the second search position
        :type Depth2: int
        :param DportEnd: End of the destination port
        :type DportEnd: int
        :param DportStart: Start of the destination port
        :type DportStart: int
        :param IsNot: Whether to match string 1 that does not contain all the specified elements
        :type IsNot: int
        :param IsNot2: Whether to match string 2 that does not contain all the specified elements
        :type IsNot2: int
        :param MatchLogic: Logical operator that combines two conditions. Values: `none`, `and` and `or`. If there is only one condition, pass in `none` for this condition only.
        :type MatchLogic: str
        :param MatchType: Matching method of the first condition. `pcre`: Regex match; `sunday`: String match.
        :type MatchType: str
        :param MatchType2: Matching method of the second condition. `pcre`: Regex match; `sunday`: String match.
        :type MatchType2: str
        :param Offset: Offset from the first search position
        :type Offset: int
        :param Offset2: Offset from the second search position
        :type Offset2: int
        :param PacketMax: Maximum packet length
        :type PacketMax: int
        :param PacketMin: Minimum packet length
        :type PacketMin: int
        :param Protocol: Protocol. Values: `tcp`, `udp`, `icmp` and `all`.
        :type Protocol: str
        :param SportEnd: End of the source port
        :type SportEnd: int
        :param SportStart: Start of the source port
        :type SportStart: int
        :param Str: String in the first condition
        :type Str: str
        :param Str2: String in the second condition
        :type Str2: str
        :param MatchBegin: Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :type MatchBegin: str
        :param MatchBegin2: Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :type MatchBegin2: str
        """
        self.Action = None
        self.Depth = None
        self.Depth2 = None
        self.DportEnd = None
        self.DportStart = None
        self.IsNot = None
        self.IsNot2 = None
        self.MatchLogic = None
        self.MatchType = None
        self.MatchType2 = None
        self.Offset = None
        self.Offset2 = None
        self.PacketMax = None
        self.PacketMin = None
        self.Protocol = None
        self.SportEnd = None
        self.SportStart = None
        self.Str = None
        self.Str2 = None
        self.MatchBegin = None
        self.MatchBegin2 = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Depth = params.get("Depth")
        self.Depth2 = params.get("Depth2")
        self.DportEnd = params.get("DportEnd")
        self.DportStart = params.get("DportStart")
        self.IsNot = params.get("IsNot")
        self.IsNot2 = params.get("IsNot2")
        self.MatchLogic = params.get("MatchLogic")
        self.MatchType = params.get("MatchType")
        self.MatchType2 = params.get("MatchType2")
        self.Offset = params.get("Offset")
        self.Offset2 = params.get("Offset2")
        self.PacketMax = params.get("PacketMax")
        self.PacketMin = params.get("PacketMin")
        self.Protocol = params.get("Protocol")
        self.SportEnd = params.get("SportEnd")
        self.SportStart = params.get("SportStart")
        self.Str = params.get("Str")
        self.Str2 = params.get("Str2")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchBegin2 = params.get("MatchBegin2")
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
        :param RegionId: Region information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegionId: list of int
        :param Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        """
        self.RegionId = None
        self.Switch = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Switch = params.get("Switch")
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
        :param AiStatus: This field is not supported. Value: `off`.
        :type AiStatus: str
        :param Appid: User appid
        :type Appid: str
        :param PlyLevel: Protection level. Values: `low`, `middle`, and `high`.
        :type PlyLevel: str
        """
        self.AiStatus = None
        self.Appid = None
        self.PlyLevel = None


    def _deserialize(self, params):
        self.AiStatus = params.get("AiStatus")
        self.Appid = params.get("Appid")
        self.PlyLevel = params.get("PlyLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUserAllowBlockIP(AbstractModel):
    """IP Allowlist/Blocklist for DDoS protection

    """

    def __init__(self):
        r"""
        :param Ip: Start IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ip: str
        :param Mask: Start mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mask: int
        :param Type: IP type. `block`: IP blocklist; `allow`: IP allowlist.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param UpdateTime: Timestamp
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: int
        :param Ip2: End IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ip2: str
        :param Mask2: End mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mask2: int
        """
        self.Ip = None
        self.Mask = None
        self.Type = None
        self.UpdateTime = None
        self.Ip2 = None
        self.Mask2 = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Mask = params.get("Mask")
        self.Type = params.get("Type")
        self.UpdateTime = params.get("UpdateTime")
        self.Ip2 = params.get("Ip2")
        self.Mask2 = params.get("Mask2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEvent(AbstractModel):
    """DDoS attack event object

    """

    def __init__(self):
        r"""
        :param PolicyId: DDoS policy group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param AttackType: Attack type (corresponding to interaction event name)
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param AttackStatus: Attack status
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackStatus: int
        :param AttackMaxBandWidth: Maximum attack bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackMaxBandWidth: int
        :param AttackPacketMaxRate: Peak attack packet rate
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackPacketMaxRate: int
        :param AttackStartTime: Attack start time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackStartTime: int
        :param AttackEndTime: Attack end time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackEndTime: int
        :param EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param ZoneId: Site ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        """
        self.PolicyId = None
        self.AttackType = None
        self.AttackStatus = None
        self.AttackMaxBandWidth = None
        self.AttackPacketMaxRate = None
        self.AttackStartTime = None
        self.AttackEndTime = None
        self.EventId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self.AttackStartTime = params.get("AttackStartTime")
        self.AttackEndTime = params.get("AttackEndTime")
        self.EventId = params.get("EventId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventData(AbstractModel):
    """DDoS attack event data

    """

    def __init__(self):
        r"""
        :param List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosAttackEvent
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventDetailData(AbstractModel):
    """DDoS attack event details

    """

    def __init__(self):
        r"""
        :param AttackStatus: Attack status
        :type AttackStatus: int
        :param AttackType: Attack type
        :type AttackType: str
        :param EndTime: End time
        :type EndTime: int
        :param StartTime: Start time
        :type StartTime: int
        :param MaxBandWidth: Maximum bandwidth
        :type MaxBandWidth: int
        :param PacketMaxRate: Maximum packet rate
        :type PacketMaxRate: int
        :param EventId: Event ID
        :type EventId: str
        :param PolicyId: DDoS policy group ID
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
        


class DDosAttackSourceEvent(AbstractModel):
    """DDoS attack event object

    """

    def __init__(self):
        r"""
        :param AttackSourceIp: Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackSourceIp: str
        :param AttackRegion: Country/Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackRegion: str
        :param AttackFlow: Accumulative attack traffic
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackFlow: int
        :param AttackPacketNum: Accumulative number of attack packets
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class DDosAttackSourceEventData(AbstractModel):
    """DDoS attack source data

    """

    def __init__(self):
        r"""
        :param List: DDoS attack source data set
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosAttackSourceEvent
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosAttackSourceEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosMajorAttackEvent(AbstractModel):
    """Major DDoS attack event

    """

    def __init__(self):
        r"""
        :param PolicyId: DDoS policy group ID
        :type PolicyId: int
        :param AttackMaxBandWidth: Maximum attack bandwidth
        :type AttackMaxBandWidth: int
        :param AttackTime: Attack time in seconds
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
        


class DDosMajorAttackEventData(AbstractModel):
    """Major attack object data

    """

    def __init__(self):
        r"""
        :param List: `DDosMajorAttackEvent` DDoS attack event
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosMajorAttackEvent
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosMajorAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """Data items in a DNS request curve

    """

    def __init__(self):
        r"""
        :param Time: Time
        :type Time: str
        :param Value: Value
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class DdosAcls(AbstractModel):
    """DDoS port filtering

    """

    def __init__(self):
        r"""
        :param Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param Acl: DDoS port filtering parameters
        :type Acl: list of DDoSAcl
        """
        self.Switch = None
        self.Acl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Acl") is not None:
            self.Acl = []
            for item in params.get("Acl"):
                obj = DDoSAcl()
                obj._deserialize(item)
                self.Acl.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosAllowBlock(AbstractModel):
    """DDoS blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param UserAllowBlockIp: Array of objects in blocklist/allowlist configuration
        :type UserAllowBlockIp: list of DDoSUserAllowBlockIP
        """
        self.Switch = None
        self.UserAllowBlockIp = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserAllowBlockIp") is not None:
            self.UserAllowBlockIp = []
            for item in params.get("UserAllowBlockIp"):
                obj = DDoSUserAllowBlockIP()
                obj._deserialize(item)
                self.UserAllowBlockIp.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosPacketFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param PacketFilter: Array of objects in feature filtering configuration
        :type PacketFilter: list of DDoSFeaturesFilter
        """
        self.Switch = None
        self.PacketFilter = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PacketFilter") is not None:
            self.PacketFilter = []
            for item in params.get("PacketFilter"):
                obj = DDoSFeaturesFilter()
                obj._deserialize(item)
                self.PacketFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosRule(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param DdosStatusInfo: DDoS mitigation level
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosStatusInfo: :class:`tencentcloud.teo.v20220106.models.DDoSStatusInfo`
        :param DdosGeoIp: DDoS regional blocking
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosGeoIp: :class:`tencentcloud.teo.v20220106.models.DDoSGeoIp`
        :param DdosAllowBlock: DDoS blocklist/allowlist
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAllowBlock: :class:`tencentcloud.teo.v20220106.models.DdosAllowBlock`
        :param DdosAntiPly: Protocol blocking and null session protection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAntiPly: :class:`tencentcloud.teo.v20220106.models.DDoSAntiPly`
        :param DdosPacketFilter: DDoS feature filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosPacketFilter: :class:`tencentcloud.teo.v20220106.models.DdosPacketFilter`
        :param DdosAcl: DDoS port filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAcl: :class:`tencentcloud.teo.v20220106.models.DdosAcls`
        :param Switch: DDoS mitigation switch. `on`: Enable; `off`: Disable.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param UdpShardOpen: Whether to enable UDP fragmentation. `on`: Enable; `off`: Disable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UdpShardOpen: str
        """
        self.DdosStatusInfo = None
        self.DdosGeoIp = None
        self.DdosAllowBlock = None
        self.DdosAntiPly = None
        self.DdosPacketFilter = None
        self.DdosAcl = None
        self.Switch = None
        self.UdpShardOpen = None


    def _deserialize(self, params):
        if params.get("DdosStatusInfo") is not None:
            self.DdosStatusInfo = DDoSStatusInfo()
            self.DdosStatusInfo._deserialize(params.get("DdosStatusInfo"))
        if params.get("DdosGeoIp") is not None:
            self.DdosGeoIp = DDoSGeoIp()
            self.DdosGeoIp._deserialize(params.get("DdosGeoIp"))
        if params.get("DdosAllowBlock") is not None:
            self.DdosAllowBlock = DdosAllowBlock()
            self.DdosAllowBlock._deserialize(params.get("DdosAllowBlock"))
        if params.get("DdosAntiPly") is not None:
            self.DdosAntiPly = DDoSAntiPly()
            self.DdosAntiPly._deserialize(params.get("DdosAntiPly"))
        if params.get("DdosPacketFilter") is not None:
            self.DdosPacketFilter = DdosPacketFilter()
            self.DdosPacketFilter._deserialize(params.get("DdosPacketFilter"))
        if params.get("DdosAcl") is not None:
            self.DdosAcl = DdosAcls()
            self.DdosAcl._deserialize(params.get("DdosAcl"))
        self.Switch = params.get("Switch")
        self.UdpShardOpen = params.get("UdpShardOpen")
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
        :param CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param Alias: Certificate alias
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param Type: Certificate type. Valid values:
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param EffectiveTime: Time when the certificate takes effect
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EffectiveTime: str
        :param CommonName: Certificate common name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CommonName: str
        :param SubjectAltName: Domain names added to the SAN certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubjectAltName: list of str
        :param Status: Certificate status. Valid values:
`applying`: Application in progress
`failed`: Application failed
`processing`: Deploying certificate
`deployed`: Certificate deployed
`disabled`: Certificate disabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param Message: Returns a message to display failure causes when `Status=failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Message: str
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
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
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RuleId: Rule ID
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


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Ids: Record ID
        :type Ids: list of str
        """
        self.ZoneId = None
        self.Ids = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Ids = params.get("Ids")
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
        :param Ids: Record ID
        :type Ids: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
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
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param OriginId: Origin group ID
        :type OriginId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        """
        self.OriginId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.ZoneId = params.get("ZoneId")
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
        :param OriginId: Origin group ID
        :type OriginId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyDetailRequest(AbstractModel):
    """DescribeApplicationProxyDetail request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Instance ID
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
        


class DescribeApplicationProxyDetailResponse(AbstractModel):
    """DescribeApplicationProxyDetail response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Instance ID
        :type ProxyId: str
        :param ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param PlatType: Proxy mode. Valid values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: List of rules
        :type Rule: list of ApplicationProxyRule
        :param Status: Status. Valid values:
`online`: Enable
`offline`: Disable
`progress`: Deploying
        :type Status: str
        :param ScheduleValue: Scheduling information
        :type ScheduleValue: list of str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param SessionPersistTime: Session persistence time
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        :param HostId: When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name, such as test.123.com
`HostId` indicates a unique ID of the domain name.
        :type HostId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Pagination parameter
        :type Offset: int
        :param Limit: Pagination parameter
        :type Limit: int
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyResponse(AbstractModel):
    """DescribeApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of ApplicationProxy
        :param TotalCount: Total number of records
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Quota: Disused
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quota: int
        :param IpCount: When `PlatType` is `ip`, it indicates the number of proxies that schedule via Anycast IP.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IpCount: int
        :param DomainCount: When `PlatType` is `domain`, it indicates the number of proxies that schedule via CNAME.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DomainCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.Quota = None
        self.IpCount = None
        self.DomainCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.Quota = params.get("Quota")
        self.IpCount = params.get("IpCount")
        self.DomainCount = params.get("DomainCount")
        self.RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param Domains: Domain name set
        :type Domains: list of str
        :param QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
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
        :param Data: Bot attack data
        :type Data: :class:`tencentcloud.teo.v20220106.models.BotLogData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BotLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeBotManagedRulesRequest(AbstractModel):
    """DescribeBotManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param Page: Total number of pages
        :type Page: int
        :param PerPage: Number of rules per page
        :type PerPage: int
        :param RuleType: Rule type. Values: `idcid`, `sipbot` and `uabot`. All rules will be returned if this field is not specified.
        :type RuleType: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Page = None
        self.PerPage = None
        self.RuleType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Page = params.get("Page")
        self.PerPage = params.get("PerPage")
        self.RuleType = params.get("RuleType")
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
        :param Count: Number of bot managed rules returned
        :type Count: int
        :param Rules: Bot managed rules
        :type Rules: list of BotManagedRuleDetail
        :param Total: Total number of bot managed rules
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = BotManagedRuleDetail()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCnameStatusRequest(AbstractModel):
    """DescribeCnameStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Names: List of domain names
        :type Names: list of str
        """
        self.ZoneId = None
        self.Names = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCnameStatusResponse(AbstractModel):
    """DescribeCnameStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: List of CNAME statuses
        :type Status: list of CnameStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self.Status = []
            for item in params.get("Status"):
                obj = CnameStatus()
                obj._deserialize(item)
                self.Status.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy group ID
        :type PolicyId: int
        :param ZoneId: Top-level domain name (site)
        :type ZoneId: str
        """
        self.PolicyId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackDataRequest(AbstractModel):
    """DescribeDDosAttackData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param PolicyIds: List of DDoS policy group IDs
        :type PolicyIds: list of int
        :param Port: Port number
        :type Port: int
        :param ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackDataResponse(AbstractModel):
    """DescribeDDosAttackData response structure.

    """

    def __init__(self):
        r"""
        :param Data: DDoS attack data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned data
        :type Msg: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackEventDetailRequest(AbstractModel):
    """DescribeDDosAttackEventDetail request structure.

    """

    def __init__(self):
        r"""
        :param EventId: Event ID
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventDetailResponse(AbstractModel):
    """DescribeDDosAttackEventDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: DDoS attack event details
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventDetailData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackEventDetailData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackEventRequest(AbstractModel):
    """DescribeDDosAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        :param IsShowDetail: Whether to show details. Valid values: Y (yes), N (no).
        :type IsShowDetail: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None
        self.IsShowDetail = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        self.IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventResponse(AbstractModel):
    """DescribeDDosAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: DDoS attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackSourceEventRequest(AbstractModel):
    """DescribeDDosAttackSourceEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackSourceEventResponse(AbstractModel):
    """DescribeDDosAttackSourceEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: DDoS attack source data
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackSourceEventData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackSourceEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackTopDataRequest(AbstractModel):
    """DescribeDDosAttackTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MetricName: Filter metric
        :type MetricName: str
        :param Limit: Number of the top data entries to query. 0: queries all data entries.
        :type Limit: int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param Port: Port number
        :type Port: int
        :param ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackTopDataResponse(AbstractModel):
    """DescribeDDosAttackTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Top N data
        :type Data: list of TopNEntry
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosMajorAttackEventRequest(AbstractModel):
    """DescribeDDosMajorAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosMajorAttackEventResponse(AbstractModel):
    """DescribeDDosMajorAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: Major DDoS attack event
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosMajorAttackEventData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosMajorAttackEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of certificates
        :type TotalCount: int
        :param CertInfo: List of default certificates
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of DefaultServerCertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Filters: Filter parameters
        :type Filters: list of DnsDataFilter
        :param Interval: Time granularity. The default value is `min`. The server can adapt to the time granularity specified.
Valid values:
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
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
                obj = DnsDataFilter()
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
        :param Data: DNS request data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of DataItem
        :param Interval: Interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Query filter
        :type Filters: list of DnsRecordFilter
        :param Order: Sorts the order
        :type Order: str
        :param Direction: Valid values: `asc`, and `desc`.
        :type Direction: str
        :param Match: Valid values: `all`, and `any`.
        :type Match: str
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param ZoneId: Site ID
        :type ZoneId: str
        """
        self.Filters = None
        self.Order = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsRecordFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ZoneId = params.get("ZoneId")
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
        :param TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param Records: List of DNS records
        :type Records: list of DnsRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: DNSSEC status. Valid values:
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param Dnssec: 
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsCertificateRequest(AbstractModel):
    """DescribeHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query filter
        :type Filters: list of CertFilter
        :param Sort: Sorting order
        :type Sort: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = CertFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = CertSort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsCertificateResponse(AbstractModel):
    """DescribeHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param Hosts: List of certificate configurations for domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hosts: list of HostCertSetting
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Hosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = HostCertSetting()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Hosts: Specifies a domain name for the query
        :type Hosts: list of str
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Hosts = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Hosts = params.get("Hosts")
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
        :param Hosts: List of domain names
        :type Hosts: list of DetailHost
        :param TotalNumber: Number of domain names
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Hosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationRequest(AbstractModel):
    """DescribeIdentification request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationResponse(AbstractModel):
    """DescribeIdentification response structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param Status: Verification status. Valid values:
- `pending`: Verifying
- `finished`: The site is verified.
        :type Status: str
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: Record type
        :type RecordType: str
        :param RecordValue: Record value
        :type RecordValue: str
        :param OriginalNameServers: NS records of the domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Status = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.OriginalNameServers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingDetailRequest(AbstractModel):
    """DescribeLoadBalancingDetail request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
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
        


class DescribeLoadBalancingDetailResponse(AbstractModel):
    """DescribeLoadBalancingDetail response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Status of the task
        :type Status: str
        :param Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Pagination parameter
        :type Offset: int
        :param Limit: Pagination parameter
        :type Limit: int
        :param Host: Ignore query string parameter
        :type Host: str
        :param Fuzzy: Specifies whether the `Host` parameter supports fuzzy match
        :type Fuzzy: bool
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Host = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Host = params.get("Host")
        self.Fuzzy = params.get("Fuzzy")
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
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param Data: CLB information
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


class DescribeOriginGroupDetailRequest(AbstractModel):
    """DescribeOriginGroupDetail request structure.

    """

    def __init__(self):
        r"""
        :param OriginId: Origin group ID
        :type OriginId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        """
        self.OriginId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupDetailResponse(AbstractModel):
    """DescribeOriginGroupDetail response structure.

    """

    def __init__(self):
        r"""
        :param OriginId: Origin group ID
        :type OriginId: str
        :param OriginName: Origin group name
        :type OriginName: str
        :param Type: Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in OriginRecord.
`weight`: Origin-pull by the weight specified by `Weight` in OriginRecord.
        :type Type: str
        :param Record: Record
        :type Record: list of OriginRecord
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param OriginType: Origin type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginType: str
        :param ApplicationProxyUsed: Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsed: bool
        :param LoadBalancingUsedType: Proxy mode of the load balancing task associated with the origin group.
`none`: Not used for load balancing.
`dns_only`: Used for DNS-only load balancing.
`proxied`: Used for proxied load balancing.
`both`: Used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsedType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None
        self.LoadBalancingUsedType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        self.LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        self.RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination parameter
        :type Offset: int
        :param Limit: Pagination parameter
        :type Limit: int
        :param Filters: Filter parameters
        :type Filters: list of OriginFilter
        :param ZoneId: Site ID
If it’s not specified, all origin groups will be obtained.
        :type ZoneId: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = OriginFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ZoneId = params.get("ZoneId")
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
        :param Data: Origin group information
        :type Data: list of OriginGroup
        :param TotalCount: Total number of records
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
                obj = OriginGroup()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param MetricNames: Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :type MetricNames: list of str
        :param Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: List of `ZoneId` values. This parameter takes effect only when querying in the zone/domain dimension.
        :type ZoneIds: list of str
        :param Domains: List of `Domain` values. This parameter takes effect only when querying in the domain dimension.
        :type Domains: list of str
        :param Protocol: Protocol type. Valid values: {http,http2,https,all}
        :type Protocol: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
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
        :param Type: Query dimension
        :type Type: str
        :param Interval: Time interval
        :type Interval: str
        :param Data: Detailed data
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Type = None
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
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
        :param JobId: Task ID
        :type JobId: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Resources queried
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
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
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
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
        :param JobId: Task ID
        :type JobId: str
        :param Type: Type of the purging task
        :type Type: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Queries content
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
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
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
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


class DescribeSecurityPolicyListRequest(AbstractModel):
    """DescribeSecurityPolicyList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
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
        :param Entities: List of protected resources
        :type Entities: list of SecurityEntity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Entities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Entities") is not None:
            self.Entities = []
            for item in params.get("Entities"):
                obj = SecurityEntity()
                obj._deserialize(item)
                self.Entities.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesIdRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId request structure.

    """

    def __init__(self):
        r"""
        :param RuleId: List of rule IDs
        :type RuleId: list of int
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesIdResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number of returned items
        :type Total: int
        :param Rules: Managed rule
        :type Rules: list of ManagedRule
        :param Count: Total number of returned items
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Rules = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param Page: Total number of pages
        :type Page: int
        :param PerPage: Number of rules per page
        :type PerPage: int
        """
        self.ZoneId = None
        self.Entity = None
        self.Page = None
        self.PerPage = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Page = params.get("Page")
        self.PerPage = params.get("PerPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRules response structure.

    """

    def __init__(self):
        r"""
        :param Count: Number of rules returned
        :type Count: int
        :param Rules: Managed rule
        :type Rules: list of ManagedRule
        :param Total: Total number of rules
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRegionsRequest(AbstractModel):
    """DescribeSecurityPolicyRegions request structure.

    """


class DescribeSecurityPolicyRegionsResponse(AbstractModel):
    """DescribeSecurityPolicyRegions response structure.

    """

    def __init__(self):
        r"""
        :param Count: Total number of regions
        :type Count: int
        :param GeoIp: Region information
        :type GeoIp: list of GeoIp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.GeoIp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("GeoIp") is not None:
            self.GeoIp = []
            for item in params.get("GeoIp"):
                obj = GeoIp()
                obj._deserialize(item)
                self.GeoIp.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRequest(AbstractModel):
    """DescribeSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Second-level domain name
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
        


class DescribeSecurityPolicyResponse(AbstractModel):
    """DescribeSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param AppId: User ID
        :type AppId: int
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Second-level domain name
        :type Entity: str
        :param Config: Security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Entity = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        if params.get("Config") is not None:
            self.Config = SecurityConfig()
            self.Config._deserialize(params.get("Config"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityPortraitRulesRequest(AbstractModel):
    """DescribeSecurityPortraitRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Subdomain name/Application name
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
        


class DescribeSecurityPortraitRulesResponse(AbstractModel):
    """DescribeSecurityPortraitRules response structure.

    """

    def __init__(self):
        r"""
        :param Count: Number of rules returned in this request
        :type Count: int
        :param Rules: Bot user profiling rule
        :type Rules: list of PortraitManagedRuleDetail
        :param Total: Total number of rules
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PortraitManagedRuleDetail()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param MetricNames: Supported metrics for data query:
`l4Flow_connections`: Access connections
`l4Flow_flux`: Access traffic
`l4Flow_inFlux`: Inbound traffic
`l4Flow_outFlux`: Outbound traffic
        :type MetricNames: list of str
        :param ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param InstanceIds: This field has been disused. Use `ProxyIds` instead.
        :type InstanceIds: list of str
        :param Protocol: This field is not supported currently.
        :type Protocol: str
        :param Interval: Time interval. Valid values: {min, 5min, hour, day}
        :type Interval: str
        :param RuleId: This field is not supported currently. Use `Filter` instead.
        :type RuleId: str
        :param Filters: Supported filters: `proxyd`, `ruleId`
        :type Filters: list of Filter
        :param ProxyIds: List of layer-4 proxies
        :type ProxyIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.InstanceIds = None
        self.Protocol = None
        self.Interval = None
        self.RuleId = None
        self.Filters = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.InstanceIds = params.get("InstanceIds")
        self.Protocol = params.get("Protocol")
        self.Interval = params.get("Interval")
        self.RuleId = params.get("RuleId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProxyIds = params.get("ProxyIds")
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
        :param Type: Query dimension
        :type Type: str
        :param Interval: Time interval
        :type Interval: str
        :param Data: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Type = None
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
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
        :param StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param MetricNames: Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :type MetricNames: list of str
        :param Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: Array of `ZoneId` values
        :type ZoneIds: list of str
        :param Filters: Filter
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
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
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param Type: Query dimension
        :type Type: str
        :param Interval: Time interval
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the query (client time in RFC 3339)
        :type StartTime: str
        :param EndTime: Start time of the query (client time in RFC 3339)
        :type EndTime: str
        :param MetricNames: Supported metrics for data query:
`l7Cache_outFlux`: Access traffic
`l7Cache_request`: Access requests
        :type MetricNames: list of str
        :param Interval: Time interval. Values: {min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param Filters: Filter condition:
{Key: "cacheType", Value: ["hit"], Operator: "equals"}: Filter by data responded from EdgeOne
{Key: "cacheType", Value: ["miss", "dynamic"], Operator: "equals"}: Filter by data responded from the origin server
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
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
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param Type: Metric specified for data query
        :type Type: str
        :param Interval: Time interval
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param MetricName: Time series-type access traffic metric
        :type MetricName: str
        :param Limit: Top N. 0 indicates to return the full data.
        :type Limit: int
        :param Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: Array of `ZoneId` values
        :type ZoneIds: list of str
        :param Filters: Filter
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
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
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Top detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param Type: Query dimension
        :type Type: str
        :param MetricName: Query metric
        :type MetricName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the query (client time in RFC 3339)
        :type StartTime: str
        :param EndTime: End time of the query (client time in RFC 3339)
        :type EndTime: str
        :param MetricName: Metric for time-series data query
        :type MetricName: str
        :param Limit: Specifies the number of data records to return. If `0` is passed in, all data is returned.
        :type Limit: int
        :param Interval: Time interval. Values: {min, 5min, hour, day, week}. This field is optional.
        :type Interval: str
        :param ZoneIds: Array of site IDs
        :type ZoneIds: list of str
        :param Filters: Filter condition
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
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
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Top-ranked data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param Type: Dimension specified for data query
        :type Type: str
        :param MetricName: Metric specified for data query
        :type MetricName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesAttackEventsRequest(AbstractModel):
    """DescribeWebManagedRulesAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param PolicyIds: List of DDoS policy group IDs
        :type PolicyIds: list of int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param Domains: List of subdomain names
        :type Domains: list of str
        :param IsShowDetail: Whether to show details. Valid values: Y (yes), N (no).
        :type IsShowDetail: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Domains = None
        self.IsShowDetail = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesAttackEventsResponse(AbstractModel):
    """DescribeWebManagedRulesAttackEvents response structure.

    """

    def __init__(self):
        r"""
        :param Data: Web attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebEventData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned data
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WebEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param Domains: List of subdomain names
        :type Domains: list of str
        :param ProtocolType: Protocol type
        :type ProtocolType: str
        :param AttackType: "webshell" : WebShell detection prevention
"oa" : Common OA vulnerability prevention
"xss" : XSS attack prevention
"xxe" : XXE attack prevention
"webscan" : Scanner attack vulnerability prevention
"cms" : Common CMS vulnerability prevention
"upload" : Malicious file upload attack prevention
"sql" : SQL injection attack prevention
"cmd_inject": Command/Code injection attack prevention
"osc" : Open-source component vulnerability prevention
"file_read" : Arbitrary file read prevention
"ldap" : LDAP injection attack prevention
"other" : Other vulnerability prevention

"all":"All"
        :type AttackType: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
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
        :param Data: Web attack log entity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param Domains: Domain name set
        :type Domains: list of str
        :param QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
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
        :param Data: Web attack log data
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebLogData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WebLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesTopDataRequest(AbstractModel):
    """DescribeWebManagedRulesTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MetricName: Filter metric
        :type MetricName: str
        :param Limit: Number of the top data entries to query. 0: queries all data entries.
        :type Limit: int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param Port: Port number
        :type Port: int
        :param ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        :param Domains: Domain name set
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesTopDataResponse(AbstractModel):
    """DescribeWebManagedRulesTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Top N data
        :type Data: list of TopNEntry
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionAttackEventsRequest(AbstractModel):
    """DescribeWebProtectionAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param Domains: Domain name
        :type Domains: list of str
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Domains = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Domains = params.get("Domains")
        self.ZoneIds = params.get("ZoneIds")
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
        :param Data: DDoS attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCInterceptEventData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CCInterceptEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param Domains: List of subdomain names
        :type Domains: list of str
        :param ProtocolType: Protocol type
        :type ProtocolType: str
        :param AttackType: "webshell" : WebShell detection prevention
"oa" : Common OA vulnerability prevention
"xss" : XSS attack prevention
"xxe" : XXE attack prevention
"webscan" : Scanner attack vulnerability prevention
"cms" : Common CMS vulnerability prevention
"upload" : Malicious file upload attack prevention
"sql" : SQL injection attack prevention
"cmd_inject": Command/Code injection attack prevention
"osc" : Open-source component vulnerability prevention
"file_read" : Arbitrary file read prevention
"ldap" : LDAP injection attack prevention
"other" : Other vulnerability prevention

"all":"All"
        :type AttackType: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
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
        :param Data: Data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Message
        :type Msg: str
        :param Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionLogRequest(AbstractModel):
    """DescribeWebProtectionLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param PageSize: Number of items per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param ZoneIds: Site set
        :type ZoneIds: list of str
        :param Domains: Domain name set
        :type Domains: list of str
        :param QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionLogResponse(AbstractModel):
    """DescribeWebProtectionLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: Block data in rate-limiting policy
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCLogData`
        :param Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CCLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeZoneDDoSPolicyRequest(AbstractModel):
    """DescribeZoneDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site (top-level domain name)
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
        :param AppId: User APPID
        :type AppId: int
        :param ShieldAreas: DDoS mitigation configuration
        :type ShieldAreas: list of ShieldArea
        :param Domains: Includes the details of all subdomain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domains: list of DDoSApplication
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AppId = None
        self.ShieldAreas = None
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        if params.get("ShieldAreas") is not None:
            self.ShieldAreas = []
            for item in params.get("ShieldAreas"):
                obj = ShieldArea()
                obj._deserialize(item)
                self.ShieldAreas.append(obj)
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneDetailsRequest(AbstractModel):
    """DescribeZoneDetails request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDetailsResponse(AbstractModel):
    """DescribeZoneDetails response structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: List of name servers used
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned to users by Tencent Cloud
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NameServers: list of str
        :param Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param CnameSpeedUp: Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
        :type CnameSpeedUp: str
        :param CnameStatus: Ownership verification status of the site when it accesses via CNAME.
- `finished`: The site is verified.
- `pending`: The site is waiting for verification.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param Tags: Resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param Area: 
        :type Area: str
        :param Resources: Billable resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resources: list of Resource
        :param ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param VanityNameServers: User-defined name server information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param VanityNameServersIps: User-defined name server IP information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Area = None
        self.Resources = None
        self.ModifiedOn = None
        self.CreatedOn = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
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
        self.Area = params.get("Area")
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.ModifiedOn = params.get("ModifiedOn")
        self.CreatedOn = params.get("CreatedOn")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        :param Cache: Cache expiration time configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: Node cache key configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: Browser cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: Offline cache
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: QUIC access
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST transport configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: Smart compression configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: HTTPS acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: Origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: Dynamic acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Zone: Domain name of the site
        :type Zone: str
        :param WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: Cache prefresh configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Cache = None
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
        self.ZoneId = None
        self.Zone = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
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
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination parameter, which specifies the offset.
        :type Offset: int
        :param Limit: Pagination parameter, which specifies the number of sites returned in each page.
        :type Limit: int
        :param Filters: Query condition filter, which supports complex type.
        :type Filters: list of ZoneFilter
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
                obj = ZoneFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: Number of sites that match the specified conditions
        :type TotalCount: int
        :param Zones: Details of sites
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param AppId: Tencent Cloud account ID
        :type AppId: int
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Status: Acceleration service status
`process`: Deploying
`online`: Enabled
`offline`: Disabled
        :type Status: str
        :param Host: Domain name
        :type Host: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsDataFilter(AbstractModel):
    """Ignore query string parameters for DNS data

    """

    def __init__(self):
        r"""
        :param Name: Parameter name. Valid values:
`zone`: Site name
`host`: Domain name
`type`: DNS resolution type
`code`: DNS response code
`area`: Region of the resolution server
        :type Name: str
        :param Value: Parameter value
When `Name=area`, valid values:
`Asia`
`Europe`
`Africa`
`Oceania`
`Americas`

When `Name=code`, valid values:
`NoError`: Successful response.
`NXDomain`: Non-existent domain in the request. It is only valid when the response is from the authoritative name server.
`NotImp`: Request type not supported.
`Refused`: The name server refuses to perform the requested operation for policy reasons.
        :type Value: str
        :param Values: Parameter value
When `Name=area`, valid values:
`Asia`
`Europe`
`Africa`
`Oceania`
`Americas`

When `Name=code`, valid values:
`NoError`: Successful response.
`NXDomain`: Non-existent domain in the request. It is only valid when the response is from the authoritative name server.
`NotImp`: Request type not supported.
`Refused`: The name server refuses to perform the requested operation for policy reasons.
        :type Values: list of str
        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Host record
        :type Name: str
        :param Content: Record value
        :type Content: str
        :param Mode: Proxy mode
        :type Mode: str
        :param Ttl: TTL value
        :type Ttl: int
        :param Priority: Priority
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Priority: int
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param Locked: Domain name lock
        :type Locked: bool
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param Status: Resolution status
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param DomainStatus: Which service is enabled for the domain name.
- `lb`: Load balancing
- `security`: Security acceleration
- `l4`: L4 proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainStatus: list of str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
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
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
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
        


class DnsRecordFilter(AbstractModel):
    """Query filter to search for DNS records

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query. It’s only available when the filter name is `name`. If it’s enabled, the length of `Values` must be 1.
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
        


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time. It must conform to the RFC3339 standard.
        :type StartTime: str
        :param EndTime: End time. It must conform to the RFC3339 standard.
        :type EndTime: str
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param Zones: Array of site names
        :type Zones: list of str
        :param Domains: Array of subdomain names
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Zones = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Zones = params.get("Zones")
        self.Domains = params.get("Domains")
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
        :param Data: Layer-7 offline log data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of L7OfflineLog
        :param PageSize: Page size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageSize: int
        :param PageNo: Page number
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageNo: int
        :param Pages: Total number of pages
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Pages: int
        :param TotalSize: Total number of entries
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.PageSize = None
        self.PageNo = None
        self.Pages = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param Reason: Failure reason
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
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param Key: Filter dimension
        :type Key: str
        :param Operator: Operator
        :type Operator: str
        :param Value: Filter dimension value
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
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param Switch: Force redirect configuration switch
`on`: Enable
`off`: Disable
        :type Switch: str
        :param RedirectStatusCode: Redirection status code
301
302
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Continent: Continent name
        :type Continent: str
        :param CountryEn: Country name in English
        :type CountryEn: str
        :param ContinentEn: Continent name in English
        :type ContinentEn: str
        """
        self.RegionId = None
        self.Country = None
        self.Continent = None
        self.CountryEn = None
        self.ContinentEn = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Country = params.get("Country")
        self.Continent = params.get("Continent")
        self.CountryEn = params.get("CountryEn")
        self.ContinentEn = params.get("ContinentEn")
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
        :param Name: HTTP header name
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
        


class HostCertSetting(AbstractModel):
    """Certificate configurations for domain names

    """

    def __init__(self):
        r"""
        :param Host: Domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Host: str
        :param CertInfo: Server certificate configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of ServerCertInfo
        """
        self.Host = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
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
        :param Switch: Specifies whether to enable. Valid values: `on` and `off`.
        :type Switch: str
        :param MaxAge: `MaxAge` value.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: int
        :param IncludeSubDomains: Specifies whether to include subdomain names. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IncludeSubDomains: str
        :param Preload: Specifies whether to preload. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Http2: HTTP2 configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Http2: str
        :param OcspStapling: OCSP configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OcspStapling: str
        :param TlsVersion: TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TlsVersion: list of str
        :param Hsts: HSTS Configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
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
        :param Name: Site name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
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
        :param Name: Site name
        :type Name: str
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: Record type
        :type RecordType: str
        :param RecordValue: Record value
        :type RecordValue: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.RequestId = params.get("RequestId")


class ImportDnsRecordsRequest(AbstractModel):
    """ImportDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param File: File content
        :type File: str
        """
        self.ZoneId = None
        self.File = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportDnsRecordsResponse(AbstractModel):
    """ImportDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param Ids: Record ID
        :type Ids: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class IntelligenceRule(AbstractModel):
    """Bot intelligence rules

    """

    def __init__(self):
        r"""
        :param Switch: Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Items: Items in a bot intelligence rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of IntelligenceRuleItem
        """
        self.Switch = None
        self.Items = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self.Items.append(obj)
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
        :param Label: Malicious bot, which is used to tag bad bots
Note: This field may return null, indicating that no valid values can be obtained.
        :type Label: str
        :param Action: Action
Note: This field may return null, indicating that no valid values can be obtained.
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
        :param Switch: Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Rules: []
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of IpTableRule
        """
        self.Switch = None
        self.Rules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self.Rules.append(obj)
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
        :param Action: Action: `drop` (block), `trans` (allow), `monitor` (observe)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param MatchFrom: Matches by IP or region. Values: `ip` and `area`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MatchFrom: str
        :param MatchContent: Matching content
Note: This field may return null, indicating that no valid values can be obtained.
        :type MatchContent: str
        :param RuleID: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleID: int
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Action = None
        self.MatchFrom = None
        self.MatchContent = None
        self.RuleID = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContent = params.get("MatchContent")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
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
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogTime: int
        :param Domain: Subdomain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domain: str
        :param Size: Log size, in bytes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Size: int
        :param Url: Download address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Url: str
        :param LogPacketName: Log package name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogPacketName: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
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
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Status
        :type Status: str
        :param Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagedRule(AbstractModel):
    """Managed rule

    """

    def __init__(self):
        r"""
        :param RuleId: ID of the rule
        :type RuleId: int
        :param Description: Rule description
        :type Description: str
        :param RuleTypeName: Rule type
        :type RuleTypeName: str
        :param RuleLevelDesc: Rule level
        :type RuleLevelDesc: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Rule status: `block`, `allow`
        :type Status: str
        :param RuleTags: Tag of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTags: list of str
        :param RuleTypeDesc: Description of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTypeDesc: str
        :param RuleTypeId: ID of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTypeId: int
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.RuleLevelDesc = None
        self.UpdateTime = None
        self.Status = None
        self.RuleTags = None
        self.RuleTypeDesc = None
        self.RuleTypeId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.RuleLevelDesc = params.get("RuleLevelDesc")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.RuleTags = params.get("RuleTags")
        self.RuleTypeDesc = params.get("RuleTypeDesc")
        self.RuleTypeId = params.get("RuleTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration.

    """

    def __init__(self):
        r"""
        :param MaxAgeTime: Specifies the max age of the cache (in seconds). The maximum value is 365 days.
Note: the value `0` means not to cache.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAgeTime: int
        :param FollowOrigin: Specifies whether to follow the max cache age of the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: str
        """
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: ID of the proxy
        :type ProxyId: str
        :param ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param ForwardClientIp: This parameter is disused.
        :type ForwardClientIp: str
        :param SessionPersist: This parameter is disused.
        :type SessionPersist: bool
        :param SessionPersistTime: Session persistence time. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
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
        :param ProxyId: ID of the proxy
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param OriginValue: Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA.
`PPV1`: Pass the client IP via Proxy Protocol V1.
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
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


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: ID of the proxy
        :type ProxyId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Status: Status
`offline`: Disabled
`online`: Enabled
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


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: ID of the proxy
        :type ProxyId: str
        :param Status: Status
`offline`: Disabled
`online`: Enabled
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
        :param ProxyId: ID of the proxy
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyHostRequest(AbstractModel):
    """ModifyDDoSPolicyHost request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Second-level domain name
        :type Host: str
        :param AccelerateType: Whether to enable content acceleration. Values: `on` (enable content acceleration), and `off` (disable content acceleration). It can be used together with `SecurityType`.
        :type AccelerateType: str
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param SecurityType: Whether to enable security protection. Values: `on` (enable security protection) and `off` (disable security protection). It can be used together with `AccelerateType`.
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
        :param Host: Subdomain name
        :type Host: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: ID of the policy group
        :type PolicyId: int
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param DdosRule: Detailed DDoS mitigation configuration
        :type DdosRule: :class:`tencentcloud.teo.v20220106.models.DdosRule`
        """
        self.PolicyId = None
        self.ZoneId = None
        self.DdosRule = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        if params.get("DdosRule") is not None:
            self.DdosRule = DdosRule()
            self.DdosRule._deserialize(params.get("DdosRule"))
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
        :param PolicyId: ID of the policy group
        :type PolicyId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param CertId: Certificate ID
        :type CertId: str
        :param Status: Certificate status
`deployed`: The certificate is deployed.
`disabled`: The certificate is disabled.
If the deployment fails, you can pass in `Status = deployed` again.
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
        :param Id: Record ID
        :type Id: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        """
        self.Id = None
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        :param Status: Resolution status
        :type Status: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param Locked: Whether the DNS record is locked
        :type Locked: bool
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Cname = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Status: DNSSEC status
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: DNSSEC status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param Dnssec: DNSSEC information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Hosts: Domain name that the certificate will be attached to
        :type Hosts: list of str
        :param CertInfo: Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :type CertInfo: list of ServerCertInfo
        """
        self.ZoneId = None
        self.Hosts = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
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
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param Type: Proxy mode.
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
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
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param Status: Status.
`online`: Enabled
`offline`: Disabled
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
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param OriginId: ID of the origin group
        :type OriginId: str
        :param OriginName: Name of the origin group
        :type OriginName: str
        :param Type: Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :type Type: str
        :param Record: Origin record
        :type Record: list of OriginRecord
        :param ZoneId: Site ID
        :type ZoneId: str
        :param OriginType: Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :type OriginType: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.ZoneId = None
        self.OriginType = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
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
        :param OriginId: Origin group ID
        :type OriginId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param Config: Security configuration
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        """
        self.ZoneId = None
        self.Entity = None
        self.Config = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        if params.get("Config") is not None:
            self.Config = SecurityConfig()
            self.Config._deserialize(params.get("Config"))
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


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param ModifiedOn: Update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID, which is used to identify the site.
        :type Id: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param VanityNameServers: Custom site information
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        self.Id = None
        self.Type = None
        self.VanityNameServers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: Name server used by the site
        :type OriginalNameServers: list of str
        :param Status: Site status.
- `pending`: The name server is not connected.
- `active`: The name server is connected.
- `moved`: The name server is moved.
        :type Status: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param CnameStatus: CNAME access status.
- `finished`: Ownership of the site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.Status = None
        self.Type = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site to be modified
        :type ZoneId: str
        :param Cache: Cache expiration time
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: Node cache key
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: Browser cache configuration
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: QUIC access
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: Maximum size of files transferred over POST request
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: Smart acceleration configuration
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param WebSocket: WebSocket configuration
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: Cache prefresh configuration
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        self.ZoneId = None
        self.Cache = None
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


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
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
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
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
        :param ZoneId: Site ID
        :type ZoneId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        """
        self.Id = None
        self.Paused = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        :param ModifiedOn: Update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Paused = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Paused = params.get("Paused")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """Configuration of offline cache

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable offline cache. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class Origin(AbstractModel):
    """Origin server configuration

    """

    def __init__(self):
        r"""
        :param OriginPullProtocol: Origin-pull protocol.
`http`: Switch HTTPS requests to HTTP
`follow`: Follow the protocol of the request.
`https`: Switch HTTP requests to HTTPS. This only supports port 443 on the origin server.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        """
        self.OriginPullProtocol = None


    def _deserialize(self, params):
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCheckOriginStatus(AbstractModel):
    """Origin health status

    """

    def __init__(self):
        r"""
        :param Status: `healthy`: Healthy; `unhealthy`: Unhealthy; `process`: Checking origin.
        :type Status: str
        :param Host: List of unhealthy origin groups when `Status = unhealthy`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: list of str
        """
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginFilter(AbstractModel):
    """The filter parameter to query origin groups

    """

    def __init__(self):
        r"""
        :param Name: Field to be filtered. Supported field: name
        :type Name: str
        :param Value: Value of the field
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
        


class OriginGroup(AbstractModel):
    """Origin group information

    """

    def __init__(self):
        r"""
        :param OriginId: Origin group ID
        :type OriginId: str
        :param OriginName: Origin group name
        :type OriginName: str
        :param Type: Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in `OriginRecord`.
`weight`: Origin-pull by the weight specified by `Weight` in `OriginRecord`.
        :type Type: str
        :param Record: Record
        :type Record: list of OriginRecord
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param OriginType: Origin server type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginType: str
        :param ApplicationProxyUsed: Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsed: bool
        :param Status: Origin status 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: :class:`tencentcloud.teo.v20220106.models.OriginCheckOriginStatus`
        :param LoadBalancingUsedType: Proxy mode of the load balancing task associated with the origin group.
`none`: This origin group is not used for load balancing.
`dns_only`: Used for DNS-only load balancing 
`proxied`: Used for proxied load balancing
`both`: It’s used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsedType: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None
        self.Status = None
        self.LoadBalancingUsedType = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        if params.get("Status") is not None:
            self.Status = OriginCheckOriginStatus()
            self.Status._deserialize(params.get("Status"))
        self.LoadBalancingUsedType = params.get("LoadBalancingUsedType")
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
        :param Record: Record value
        :type Record: str
        :param Area: A specific region when `Type=area`.
The default region when `Type` is not specified.
        :type Area: list of str
        :param Weight: A specific weight when `Type=weight`.
The value range is [1-100].
The total weight of multiple origins in an origin group should be 100.
        :type Weight: int
        :param Port: Port
        :type Port: int
        :param RecordId: Record ID
        :type RecordId: str
        :param Private: Specifies whether to run private origin authentication.
It is valid only when `OriginType=third_part`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Private: bool
        :param PrivateParameter: Private origin parameter.
It is valid only when `Private=true`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PrivateParameter: list of OriginRecordPrivateParameter
        :param Proto: 
        :type Proto: str
        """
        self.Record = None
        self.Area = None
        self.Weight = None
        self.Port = None
        self.RecordId = None
        self.Private = None
        self.PrivateParameter = None
        self.Proto = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.Area = params.get("Area")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.RecordId = params.get("RecordId")
        self.Private = params.get("Private")
        if params.get("PrivateParameter") is not None:
            self.PrivateParameter = []
            for item in params.get("PrivateParameter"):
                obj = OriginRecordPrivateParameter()
                obj._deserialize(item)
                self.PrivateParameter.append(obj)
        self.Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecordPrivateParameter(AbstractModel):
    """Private origin authentication parameter

    """

    def __init__(self):
        r"""
        :param Name: Name of the private origin authentication parameter.
`AccessKeyId`: Access key ID
`SecretAccessKey`: Secret access key
        :type Name: str
        :param Value: Value of the private origin authentication parameter
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
        :param ClassificationId: Rule feature category ID (scanner, bot behavior, etc.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClassificationId: int
        :param Status: Current rule action status (block, alg, etc.)
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
        :param Switch: Specifies whether to enable custom setting of the maximum file size. 
`off`: Disable. In this case, the max size defaults to 32 MB.
`on`: Enable. You can set a custom max size.
        :type Switch: str
        :param MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class QueryCondition(AbstractModel):
    """Query condition

    """

    def __init__(self):
        r"""
        :param Key: Dimension
        :type Key: str
        :param Operator: Operator
        :type Operator: str
        :param Value: Dimension value
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
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param Action: `includeCustom`: Include the specified query strings.
`excludeCustom`: Exclude the specified query strings.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param Value: Array of query strings used/excluded
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Switch: Whether to enable QUIC
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
        


class RateLimitConfig(AbstractModel):
    """Rate limit configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch
        :type Switch: str
        :param UserRules: Rate limit rule
        :type UserRules: list of RateLimitUserRule
        :param Template: Default template
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Template: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplate`
        :param Intelligence: Client filtering
Note: This field may return null, indicating that no valid values can be obtained.
        :type Intelligence: :class:`tencentcloud.teo.v20220106.models.RateLimitIntelligence`
        """
        self.Switch = None
        self.UserRules = None
        self.Template = None
        self.Intelligence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self.UserRules = []
            for item in params.get("UserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self.UserRules.append(obj)
        if params.get("Template") is not None:
            self.Template = RateLimitTemplate()
            self.Template._deserialize(params.get("Template"))
        if params.get("Intelligence") is not None:
            self.Intelligence = RateLimitIntelligence()
            self.Intelligence._deserialize(params.get("Intelligence"))
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
        :param Switch: Whether to enable this feature
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Action: Action. Values: `monitor` (observe), `alg` (JS/Managed challenge)
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class RateLimitTemplate(AbstractModel):
    """Rate limit template

    """

    def __init__(self):
        r"""
        :param Mode: Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param Detail: Template details
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Detail: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplateDetail`
        """
        self.Mode = None
        self.Detail = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("Detail") is not None:
            self.Detail = RateLimitTemplateDetail()
            self.Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """Rate limit template configuration

    """

    def __init__(self):
        r"""
        :param Mode: Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param ID: Unique ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ID: int
        :param Action: Action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param PunishTime: Time it takes to perform the action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param Threshold: Request rate threshold
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Threshold: int
        :param Period: Statistical period
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Threshold: Rate threshold
        :type Threshold: int
        :param Period: Data collection time
        :type Period: int
        :param RuleName: Name of the rule
        :type RuleName: str
        :param Action: Action: `monitor` (Observe), `drop` (Block)
        :type Action: str
        :param PunishTime: Time it takes to perform the action
        :type PunishTime: int
        :param PunishTimeUnit: Time unit: second
        :type PunishTimeUnit: str
        :param RuleStatus: Status of the rule
        :type RuleStatus: str
        :param Conditions: Rule
        :type Conditions: list of ACLCondition
        :param RulePriority: Priority of the rule
        :type RulePriority: int
        :param RuleID: ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param FreqFields: Word filter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FreqFields: list of str
        :param UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        """
        self.Threshold = None
        self.Period = None
        self.RuleName = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.RuleStatus = None
        self.Conditions = None
        self.RulePriority = None
        self.RuleID = None
        self.FreqFields = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.FreqFields = params.get("FreqFields")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
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
        :param Name: Site name
        :type Name: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Billable resource

    """

    def __init__(self):
        r"""
        :param Id: Resource ID
        :type Id: str
        :param PayMode: Billing mode
`0`: Pay-as-you-go
        :type PayMode: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param EnableTime: Effective time
        :type EnableTime: str
        :param ExpireTime: Expiration time
        :type ExpireTime: str
        :param Status: Status of the plan
        :type Status: str
        :param Sv: Pricing query parameter
        :type Sv: list of Sv
        :param AutoRenewFlag: Specifies whether to enable auto-renewal
`0`: Default
`1`: Enable auto-renewal
`2`: Disable auto-renewal
        :type AutoRenewFlag: int
        :param PlanId: ID of the plan
        :type PlanId: str
        :param Area: 
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
        


class ScanDnsRecordsRequest(AbstractModel):
    """ScanDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        


class ScanDnsRecordsResponse(AbstractModel):
    """ScanDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param Status: Scan status
- `doing`: Scanning
- `done`: Scanned
        :type Status: str
        :param RecordsAdded: Number of DNS records added after scanning
        :type RecordsAdded: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RecordsAdded = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RecordsAdded = params.get("RecordsAdded")
        self.RequestId = params.get("RequestId")


class SecEntry(AbstractModel):
    """Returned value of security data entry

    """

    def __init__(self):
        r"""
        :param Key: Entry key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Entry value
Note: This field may return null, indicating that no valid values can be obtained.
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
    """Corresponding value of security data entry

    """

    def __init__(self):
        r"""
        :param Metric: Metric name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param Detail: Metric data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        :param Max: Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: int
        :param Avg: Average
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avg: float
        :param Sum: Sum
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class SecurityConfig(AbstractModel):
    """Security configuration

    """

    def __init__(self):
        r"""
        :param WafConfig: WAF configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WafConfig: :class:`tencentcloud.teo.v20220106.models.WafConfig`
        :param RateLimitConfig: Rate limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220106.models.RateLimitConfig`
        :param DdosConfig: DDoS mitigation configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosConfig: :class:`tencentcloud.teo.v20220106.models.DDoSConfig`
        :param AclConfig: ACL configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AclConfig: :class:`tencentcloud.teo.v20220106.models.AclConfig`
        :param BotConfig: Bot configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BotConfig: :class:`tencentcloud.teo.v20220106.models.BotConfig`
        :param SwitchConfig: Switch that controls all web security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SwitchConfig: :class:`tencentcloud.teo.v20220106.models.SwitchConfig`
        :param IpTableConfig: IP blocklist/allowlist
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpTableConfig: :class:`tencentcloud.teo.v20220106.models.IpTableConfig`
        """
        self.WafConfig = None
        self.RateLimitConfig = None
        self.DdosConfig = None
        self.AclConfig = None
        self.BotConfig = None
        self.SwitchConfig = None
        self.IpTableConfig = None


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self.WafConfig = WafConfig()
            self.WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self.RateLimitConfig = RateLimitConfig()
            self.RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("DdosConfig") is not None:
            self.DdosConfig = DDoSConfig()
            self.DdosConfig._deserialize(params.get("DdosConfig"))
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
        :param AppId: User APPID
        :type AppId: int
        :param ZoneId: Top-level domain name
        :type ZoneId: str
        :param Entity: Second-level domain name
        :type Entity: str
        :param EntityType: Type of protected resource. Values: `domain` and `application`.
        :type EntityType: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Entity = None
        self.EntityType = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.EntityType = params.get("EntityType")
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
        :param CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param Type: Certificate type.
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate deployment time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DeployTime: str
        :param Status: Certificate deployment status.
`processing`: Deploying
`deployed`: Deployed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Status = params.get("Status")
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
        :param ZoneId: ID of the site (top-level domain name)
        :type ZoneId: str
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param Type: Type of protected resource. Values: `domain` and `application`.
        :type Type: str
        :param EntityName: Layer-4 proxy name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EntityName: str
        :param Application: Layer-7 domain name parameters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Application: list of DDoSApplication
        :param TcpNum: Number of layer-4 TCP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TcpNum: int
        :param UdpNum: Number of layer-4 UDP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UdpNum: int
        :param Entity: Name of the protected resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Entity: str
        :param Share: Whether the shared resource is used. Values: `true` (yes) and `false` (no). The proxy mode cannot be switched when the shared resource is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Share: bool
        """
        self.ZoneId = None
        self.PolicyId = None
        self.Type = None
        self.EntityName = None
        self.Application = None
        self.TcpNum = None
        self.UdpNum = None
        self.Entity = None
        self.Share = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PolicyId = params.get("PolicyId")
        self.Type = params.get("Type")
        self.EntityName = params.get("EntityName")
        if params.get("Application") is not None:
            self.Application = []
            for item in params.get("Application"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self.Application.append(obj)
        self.TcpNum = params.get("TcpNum")
        self.UdpNum = params.get("UdpNum")
        self.Entity = params.get("Entity")
        self.Share = params.get("Share")
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
        :param Switch: Whether to enable smart acceleration
`on`: Enable
`off`: Disable
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
        


class Sv(AbstractModel):
    """Pricing query parameter

    """

    def __init__(self):
        r"""
        :param Key: Parameter key
        :type Key: str
        :param Value: Parameter value
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
        :param WebSwitch: Switch that controls all web security configuration: basic web protection, custom rules, and rate limiting
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
        


class Tag(AbstractModel):
    """Tag configuration

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
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
        :param JobId: Task ID
        :type JobId: str
        :param Status: Status of the task
        :type Status: str
        :param Target: Resource
        :type Target: str
        :param Type: Task type
        :type Type: str
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param UpdateTime: Task completion time
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
        


class TimingDataItem(AbstractModel):
    """Data items of the statistical curve

    """

    def __init__(self):
        r"""
        :param Timestamp: Second-level timestamp
Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param Value: Value
Note: This field may return null, indicating that no valid values can be obtained.
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
    """Time series data of L7 data analysis

    """

    def __init__(self):
        r"""
        :param TypeKey: Query dimension value
        :type TypeKey: str
        :param TypeValue: Detailed time series data
Note: This field may return null, indicating that no valid values can be obtained.
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
        :param Sum: Sum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sum: int
        :param Max: Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: int
        :param Avg: Average
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avg: int
        :param MetricName: Metric name
        :type MetricName: str
        :param DetailData: This field will be disused soon. Use the `Detail` field instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailData: list of int
        :param Detail: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        """
        self.Sum = None
        self.Max = None
        self.Avg = None
        self.MetricName = None
        self.DetailData = None
        self.Detail = None


    def _deserialize(self, params):
        self.Sum = params.get("Sum")
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.MetricName = params.get("MetricName")
        self.DetailData = params.get("DetailData")
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
    """Top data of layer-7 data analysis

    """

    def __init__(self):
        r"""
        :param TypeKey: Query dimension value
        :type TypeKey: str
        :param DetailData: Top data rankings
Note: This field may return null, indicating that no valid values can be obtained.
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
    """The structure used to sort the top data

    """

    def __init__(self):
        r"""
        :param Key: Field name
        :type Key: str
        :param Value: Field value
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
        


class TopNEntry(AbstractModel):
    """TopN entry

    """

    def __init__(self):
        r"""
        :param Key: Entry key
        :type Key: str
        :param Value: Top N data
        :type Value: list of TopNEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = TopNEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopNEntryValue(AbstractModel):
    """Top N data entry

    """

    def __init__(self):
        r"""
        :param Name: Entry name
        :type Name: str
        :param Count: Quantity
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
        :param Switch: Whether to enable HTTP2 origin-pull
`on`: Enable
`off`: Disable
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
        :param Switch: Whether to enable the custom name server
`on`: Enable
`off`: Disable
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
    """IP of the custom name server

    """

    def __init__(self):
        r"""
        :param Name: Name of the custom name server
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
        


class WafConfig(AbstractModel):
    """WAF configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch
        :type Switch: str
        :param Level: Protection level: `loose`, `normal`, `strict`, `stricter`, `custom`
        :type Level: str
        :param Mode: Mode: `block`, `observe`, `close`
        :type Mode: str
        :param WafRules: WAF rule allowlist/blocklist
        :type WafRules: :class:`tencentcloud.teo.v20220106.models.WafRule`
        :param AiRule: AI rule engine
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AiRule: :class:`tencentcloud.teo.v20220106.models.AiRule`
        """
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRules = None
        self.AiRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRules") is not None:
            self.WafRules = WafRule()
            self.WafRules._deserialize(params.get("WafRules"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
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
        :param BlockRuleIDs: Blocklist
        :type BlockRuleIDs: list of int
        :param Switch: Whether the WAF rule is enabled or disabled
        :type Switch: str
        :param ObserveRuleIDs: Observe mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ObserveRuleIDs: list of int
        """
        self.BlockRuleIDs = None
        self.Switch = None
        self.ObserveRuleIDs = None


    def _deserialize(self, params):
        self.BlockRuleIDs = params.get("BlockRuleIDs")
        self.Switch = params.get("Switch")
        self.ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebAttackEvent(AbstractModel):
    """Web block event

    """

    def __init__(self):
        r"""
        :param ClientIp: Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIp: str
        :param AttackUrl: Attack URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackUrl: str
        :param AttackTime: Attack time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        """
        self.ClientIp = None
        self.AttackUrl = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.AttackUrl = params.get("AttackUrl")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebEventData(AbstractModel):
    """Web event data

    """

    def __init__(self):
        r"""
        :param List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of WebAttackEvent
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = WebAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogData(AbstractModel):
    """Web attack log data

    """

    def __init__(self):
        r"""
        :param List: Data
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of WebLogs
        :param PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = WebLogs()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
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
        :param AttackContent: Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param AttackIp: Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackIp: str
        :param AttackType: Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param Domain: Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Msuuid: uuid
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msuuid: str
        :param RequestMethod: Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestMethod: str
        :param RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param Ua: user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ua: str
        :param AttackTime: Attack time. For consistency considerations, the original parameter `time` was renamed `AttackTime`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        """
        self.AttackContent = None
        self.AttackIp = None
        self.AttackType = None
        self.Domain = None
        self.Msuuid = None
        self.RequestMethod = None
        self.RequestUri = None
        self.RiskLevel = None
        self.RuleId = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.Ua = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.AttackContent = params.get("AttackContent")
        self.AttackIp = params.get("AttackIp")
        self.AttackType = params.get("AttackType")
        self.Domain = params.get("Domain")
        self.Msuuid = params.get("Msuuid")
        self.RequestMethod = params.get("RequestMethod")
        self.RequestUri = params.get("RequestUri")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleId = params.get("RuleId")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.Ua = params.get("Ua")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable custom WebSocket timeout setting. When it’s `off`: it means to keep the default WebSocket connection timeout period, which is 15 seconds. To change the timeout period, please set it to `on`.
        :type Switch: str
        :param Timeout: Sets timeout period in seconds. Maximum value: 120
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param Type: How the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param CnameSpeedUp: Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
Note: This field may return null, indicating that no valid values can be obtained.
        :type CnameSpeedUp: str
        :param CnameStatus: Ownership verification status of the site when it is connected to EdgeOne via CNAME.
- `finished`: The site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param Tags: Resource tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        :param Resources: Billable resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Resources: list of Resource
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param Area: 
        :type Area: str
        """
        self.Id = None
        self.Name = None
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


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """Site query filter

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
- `tagKey`: Tag key.
- `tagValue`: Tag value.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query. It’s only available when filter name is `name`. If it’s enabled, the length of `Values` must be 1.
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
        