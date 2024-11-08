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
        :param _MatchFrom: Field to match
        :type MatchFrom: str
        :param _MatchParam: String to match
        :type MatchParam: str
        :param _Operator: Relation between the field and content
        :type Operator: str
        :param _MatchContent: Content to match
        :type MatchContent: str
        """
        self._MatchFrom = None
        self._MatchParam = None
        self._Operator = None
        self._MatchContent = None

    @property
    def MatchFrom(self):
        """Field to match
        :rtype: str
        """
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchParam(self):
        """String to match
        :rtype: str
        """
        return self._MatchParam

    @MatchParam.setter
    def MatchParam(self, MatchParam):
        self._MatchParam = MatchParam

    @property
    def Operator(self):
        """Relation between the field and content
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def MatchContent(self):
        """Content to match
        :rtype: str
        """
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._MatchFrom = params.get("MatchFrom")
        self._MatchParam = params.get("MatchParam")
        self._Operator = params.get("Operator")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ACLUserRule(AbstractModel):
    """Custom ACL rule

    """

    def __init__(self):
        r"""
        :param _RuleName: Name of the rule
        :type RuleName: str
        :param _Action: Action
        :type Action: str
        :param _RuleStatus: Status of the rule
        :type RuleStatus: str
        :param _Conditions: ACL rule
        :type Conditions: list of ACLCondition
        :param _RulePriority: Priority of the rule
        :type RulePriority: int
        :param _RuleID: ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param _UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param _PunishTime: IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param _PunishTimeUnit: IP blocking time unit
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTimeUnit: str
        :param _Name: Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Name: str
        :param _PageId: ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageId: int
        :param _RedirectUrl: Redirection URL, which must be a subdomain name of the site
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectUrl: str
        :param _ResponseCode: Return code configured on the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseCode: int
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._Conditions = None
        self._RulePriority = None
        self._RuleID = None
        self._UpdateTime = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._Name = None
        self._PageId = None
        self._RedirectUrl = None
        self._ResponseCode = None

    @property
    def RuleName(self):
        """Name of the rule
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        """Action
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        """Status of the rule
        :rtype: str
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def Conditions(self):
        """ACL rule
        :rtype: list of ACLCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def RulePriority(self):
        """Priority of the rule
        :rtype: int
        """
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        """ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        """Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PunishTime(self):
        """IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        """IP blocking time unit
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def Name(self):
        """Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageId(self):
        """ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def RedirectUrl(self):
        """Redirection URL, which must be a subdomain name of the site
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def ResponseCode(self):
        """Return code configured on the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._Name = params.get("Name")
        self._PageId = params.get("PageId")
        self._RedirectUrl = params.get("RedirectUrl")
        self._ResponseCode = params.get("ResponseCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfig(AbstractModel):
    """ACL configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
        :type Switch: str
        :param _UserRules: ACL user rule
        :type UserRules: list of ACLUserRule
        """
        self._Switch = None
        self._UserRules = None

    @property
    def Switch(self):
        """Switch
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def UserRules(self):
        """ACL user rule
        :rtype: list of ACLUserRule
        """
        return self._UserRules

    @UserRules.setter
    def UserRules(self, UserRules):
        self._UserRules = UserRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self._UserRules = []
            for item in params.get("UserRules"):
                obj = ACLUserRule()
                obj._deserialize(item)
                self._UserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRule(AbstractModel):
    """AI rule engine

    """

    def __init__(self):
        r"""
        :param _Mode: `smart_status_close`: Disable; `smart_status_open`: Block;
`smart_status_observe`: Observe.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        """`smart_status_close`: Disable; `smart_status_open`: Block;
`smart_status_observe`: Observe.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxy(AbstractModel):
    """Application proxy instance

    """

    def __init__(self):
        r"""
        :param _ProxyId: ID of the proxy
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyId: str
        :param _ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param _PlatType: Scheduling mode:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param _SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param _AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param _ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param _SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param _Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        :param _Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param _ScheduleValue: Scheduling information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ScheduleValue: list of str
        :param _UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param _ZoneId: Site ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneId: str
        :param _ZoneName: Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneName: str
        :param _SessionPersistTime: Session persistence duration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SessionPersistTime: int
        :param _ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyType: str
        :param _HostId: When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name;
`HostId` indicates a unique ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostId: str
        """
        self._ProxyId = None
        self._ProxyName = None
        self._PlatType = None
        self._SecurityType = None
        self._AccelerateType = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._Rule = None
        self._Status = None
        self._ScheduleValue = None
        self._UpdateTime = None
        self._ZoneId = None
        self._ZoneName = None
        self._SessionPersistTime = None
        self._ProxyType = None
        self._HostId = None

    @property
    def ProxyId(self):
        """ID of the proxy
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        """Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def PlatType(self):
        """Scheduling mode:
`ip`: Anycast IP
`domain`: CNAME
        :rtype: str
        """
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def SecurityType(self):
        """`0`: Disable security protection; `1`: Enable security protection.
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        """`0`: Disable acceleration; `1`: Enable acceleration.
        :rtype: int
        """
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def ForwardClientIp(self):
        """This field is moved to `Rule.ForwardClientIp`.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """This field is moved to `Rule.SessionPersist`.
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def Rule(self):
        """Rule list
        :rtype: list of ApplicationProxyRule
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Status(self):
        """Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScheduleValue(self):
        """Scheduling information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._ScheduleValue

    @ScheduleValue.setter
    def ScheduleValue(self, ScheduleValue):
        self._ScheduleValue = ScheduleValue

    @property
    def UpdateTime(self):
        """Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ZoneId(self):
        """Site ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def SessionPersistTime(self):
        """Session persistence duration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        """Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def HostId(self):
        """When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name;
`HostId` indicates a unique ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._PlatType = params.get("PlatType")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        self._Status = params.get("Status")
        self._ScheduleValue = params.get("ScheduleValue")
        self._UpdateTime = params.get("UpdateTime")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """Application proxy rule

    """

    def __init__(self):
        r"""
        :param _Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param _Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param _OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param _OriginValue: Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param _RuleId: Rule ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleId: str
        :param _Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
        :type Status: str
        :param _ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param _SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._RuleId = None
        self._Status = None
        self._ForwardClientIp = None
        self._SessionPersist = None

    @property
    def Proto(self):
        """Protocol. Valid values: `TCP` and `UDP`.
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        """Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :rtype: list of str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        """Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        """Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :rtype: list of str
        """
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def RuleId(self):
        """Rule ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        """Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ForwardClientIp(self):
        """Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """Specifies whether to enable session persistence
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist


    def _deserialize(self, params):
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotConfig(AbstractModel):
    """Bot security configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable bot security configuration
        :type Switch: str
        :param _ManagedRule: Preset rules
        :type ManagedRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param _UaBotRule: Not supported currently
        :type UaBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param _IspBotRule: Not supported currently
        :type IspBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param _PortraitRule: User portrait rules
        :type PortraitRule: :class:`tencentcloud.teo.v20220106.models.BotPortraitRule`
        :param _IntelligenceRule: Bot intelligence rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220106.models.IntelligenceRule`
        """
        self._Switch = None
        self._ManagedRule = None
        self._UaBotRule = None
        self._IspBotRule = None
        self._PortraitRule = None
        self._IntelligenceRule = None

    @property
    def Switch(self):
        """Whether to enable bot security configuration
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ManagedRule(self):
        """Preset rules
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        """
        return self._ManagedRule

    @ManagedRule.setter
    def ManagedRule(self, ManagedRule):
        self._ManagedRule = ManagedRule

    @property
    def UaBotRule(self):
        """Not supported currently
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        """
        return self._UaBotRule

    @UaBotRule.setter
    def UaBotRule(self, UaBotRule):
        self._UaBotRule = UaBotRule

    @property
    def IspBotRule(self):
        """Not supported currently
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        """
        return self._IspBotRule

    @IspBotRule.setter
    def IspBotRule(self, IspBotRule):
        self._IspBotRule = IspBotRule

    @property
    def PortraitRule(self):
        """User portrait rules
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotPortraitRule`
        """
        return self._PortraitRule

    @PortraitRule.setter
    def PortraitRule(self, PortraitRule):
        self._PortraitRule = PortraitRule

    @property
    def IntelligenceRule(self):
        """Bot intelligence rules
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.IntelligenceRule`
        """
        return self._IntelligenceRule

    @IntelligenceRule.setter
    def IntelligenceRule(self, IntelligenceRule):
        self._IntelligenceRule = IntelligenceRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("ManagedRule") is not None:
            self._ManagedRule = BotManagedRule()
            self._ManagedRule._deserialize(params.get("ManagedRule"))
        if params.get("UaBotRule") is not None:
            self._UaBotRule = BotManagedRule()
            self._UaBotRule._deserialize(params.get("UaBotRule"))
        if params.get("IspBotRule") is not None:
            self._IspBotRule = BotManagedRule()
            self._IspBotRule._deserialize(params.get("IspBotRule"))
        if params.get("PortraitRule") is not None:
            self._PortraitRule = BotPortraitRule()
            self._PortraitRule._deserialize(params.get("PortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self._IntelligenceRule = IntelligenceRule()
            self._IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLog(AbstractModel):
    """Bot attack log

    """

    def __init__(self):
        r"""
        :param _AttackTime: Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        :param _AttackIp: Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackIp: str
        :param _Domain: Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param _AttackType: Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param _RequestMethod: Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestMethod: str
        :param _AttackContent: Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param _RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param _RuleId: Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param _SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param _EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param _DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param _HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param _Ua: user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ua: str
        :param _DetectionMethod: Detection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetectionMethod: str
        :param _Confidence: Confidence
Note: This field may return null, indicating that no valid values can be obtained.
        :type Confidence: str
        :param _Maliciousness: Maliciousness
Note: This field may return null, indicating that no valid values can be obtained.
        :type Maliciousness: str
        """
        self._AttackTime = None
        self._AttackIp = None
        self._Domain = None
        self._RequestUri = None
        self._AttackType = None
        self._RequestMethod = None
        self._AttackContent = None
        self._RiskLevel = None
        self._RuleId = None
        self._SipCountryCode = None
        self._EventId = None
        self._DisposalMethod = None
        self._HttpLog = None
        self._Ua = None
        self._DetectionMethod = None
        self._Confidence = None
        self._Maliciousness = None

    @property
    def AttackTime(self):
        """Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime

    @property
    def AttackIp(self):
        """Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackIp

    @AttackIp.setter
    def AttackIp(self, AttackIp):
        self._AttackIp = AttackIp

    @property
    def Domain(self):
        """Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestUri(self):
        """Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestUri

    @RequestUri.setter
    def RequestUri(self, RequestUri):
        self._RequestUri = RequestUri

    @property
    def AttackType(self):
        """Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def RequestMethod(self):
        """Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestMethod

    @RequestMethod.setter
    def RequestMethod(self, RequestMethod):
        self._RequestMethod = RequestMethod

    @property
    def AttackContent(self):
        """Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackContent

    @AttackContent.setter
    def AttackContent(self, AttackContent):
        self._AttackContent = AttackContent

    @property
    def RiskLevel(self):
        """Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RuleId(self):
        """Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def SipCountryCode(self):
        """IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SipCountryCode

    @SipCountryCode.setter
    def SipCountryCode(self, SipCountryCode):
        self._SipCountryCode = SipCountryCode

    @property
    def EventId(self):
        """Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DisposalMethod(self):
        """Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DisposalMethod

    @DisposalMethod.setter
    def DisposalMethod(self, DisposalMethod):
        self._DisposalMethod = DisposalMethod

    @property
    def HttpLog(self):
        """http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HttpLog

    @HttpLog.setter
    def HttpLog(self, HttpLog):
        self._HttpLog = HttpLog

    @property
    def Ua(self):
        """user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ua

    @Ua.setter
    def Ua(self, Ua):
        self._Ua = Ua

    @property
    def DetectionMethod(self):
        """Detection method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DetectionMethod

    @DetectionMethod.setter
    def DetectionMethod(self, DetectionMethod):
        self._DetectionMethod = DetectionMethod

    @property
    def Confidence(self):
        """Confidence
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Maliciousness(self):
        """Maliciousness
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Maliciousness

    @Maliciousness.setter
    def Maliciousness(self, Maliciousness):
        self._Maliciousness = Maliciousness


    def _deserialize(self, params):
        self._AttackTime = params.get("AttackTime")
        self._AttackIp = params.get("AttackIp")
        self._Domain = params.get("Domain")
        self._RequestUri = params.get("RequestUri")
        self._AttackType = params.get("AttackType")
        self._RequestMethod = params.get("RequestMethod")
        self._AttackContent = params.get("AttackContent")
        self._RiskLevel = params.get("RiskLevel")
        self._RuleId = params.get("RuleId")
        self._SipCountryCode = params.get("SipCountryCode")
        self._EventId = params.get("EventId")
        self._DisposalMethod = params.get("DisposalMethod")
        self._HttpLog = params.get("HttpLog")
        self._Ua = params.get("Ua")
        self._DetectionMethod = params.get("DetectionMethod")
        self._Confidence = params.get("Confidence")
        self._Maliciousness = params.get("Maliciousness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLogData(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param _List: Data set of bot attack logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of BotLog
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data set of bot attack logs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BotLog
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = BotLog()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot managed rules

    """

    def __init__(self):
        r"""
        :param _ManagedIds: ID of the rule to be enabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ManagedIds: list of int
        :param _RuleID: ID of the rule being applied
        :type RuleID: int
        :param _Action: Action of the rule. Values: `drop`; `trans`; `monitor`; `alg`.
        :type Action: str
        :param _PunishTime: The amount of time the IP is blocked
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param _PunishTimeUnit: Unit of IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTimeUnit: str
        :param _Name: Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Name: str
        :param _PageId: ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageId: int
        :param _RedirectUrl: Redirection URL, which must be a subdomain name of your site encoded by URLEncode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectUrl: str
        :param _ResponseCode: Response code returned after redirection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseCode: int
        :param _TransManagedIds: ID of the rule that is set to allow requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TransManagedIds: list of int
        :param _AlgManagedIds: ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlgManagedIds: list of int
        :param _CapManagedIds: ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CapManagedIds: list of int
        :param _MonManagedIds: ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MonManagedIds: list of int
        :param _DropManagedIds: ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DropManagedIds: list of int
        """
        self._ManagedIds = None
        self._RuleID = None
        self._Action = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._Name = None
        self._PageId = None
        self._RedirectUrl = None
        self._ResponseCode = None
        self._TransManagedIds = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None

    @property
    def ManagedIds(self):
        """ID of the rule to be enabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._ManagedIds

    @ManagedIds.setter
    def ManagedIds(self, ManagedIds):
        self._ManagedIds = ManagedIds

    @property
    def RuleID(self):
        """ID of the rule being applied
        :rtype: int
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Action(self):
        """Action of the rule. Values: `drop`; `trans`; `monitor`; `alg`.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        """The amount of time the IP is blocked
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        """Unit of IP blocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def Name(self):
        """Name of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageId(self):
        """ID of the custom block page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def RedirectUrl(self):
        """Redirection URL, which must be a subdomain name of your site encoded by URLEncode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def ResponseCode(self):
        """Response code returned after redirection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def TransManagedIds(self):
        """ID of the rule that is set to allow requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._TransManagedIds

    @TransManagedIds.setter
    def TransManagedIds(self, TransManagedIds):
        self._TransManagedIds = TransManagedIds

    @property
    def AlgManagedIds(self):
        """ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        """ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        """ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        """ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds


    def _deserialize(self, params):
        self._ManagedIds = params.get("ManagedIds")
        self._RuleID = params.get("RuleID")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._Name = params.get("Name")
        self._PageId = params.get("PageId")
        self._RedirectUrl = params.get("RedirectUrl")
        self._ResponseCode = params.get("ResponseCode")
        self._TransManagedIds = params.get("TransManagedIds")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRuleDetail(AbstractModel):
    """Bot managed rule details

    """

    def __init__(self):
        r"""
        :param _RuleId: ID of the rule
        :type RuleId: int
        :param _Description: Rule description
        :type Description: str
        :param _RuleTypeName: Rule type
        :type RuleTypeName: str
        :param _Status: Whether the rule is enabled
        :type Status: str
        """
        self._RuleId = None
        self._Description = None
        self._RuleTypeName = None
        self._Status = None

    @property
    def RuleId(self):
        """ID of the rule
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Description(self):
        """Rule description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleTypeName(self):
        """Rule type
        :rtype: str
        """
        return self._RuleTypeName

    @RuleTypeName.setter
    def RuleTypeName(self, RuleTypeName):
        self._RuleTypeName = RuleTypeName

    @property
    def Status(self):
        """Whether the rule is enabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Description = params.get("Description")
        self._RuleTypeName = params.get("RuleTypeName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPortraitRule(AbstractModel):
    """Bot user portrait rules

    """

    def __init__(self):
        r"""
        :param _RuleID: ID of the rule being applied
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param _AlgManagedIds: ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlgManagedIds: list of int
        :param _CapManagedIds: ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CapManagedIds: list of int
        :param _MonManagedIds: ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MonManagedIds: list of int
        :param _DropManagedIds: ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DropManagedIds: list of int
        :param _Switch: Feature switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._RuleID = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None
        self._Switch = None

    @property
    def RuleID(self):
        """ID of the rule being applied
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def AlgManagedIds(self):
        """ID of the rule that is set to verify requests by JavaScript challenge
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        """ID of the rule that is set to verify requests by CAPTCHA
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        """ID of the rule that is set to observe requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        """ID of the rule that is set to block requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds

    @property
    def Switch(self):
        """Feature switch
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEvent(AbstractModel):
    """CC block event

    """

    def __init__(self):
        r"""
        :param _ClientIp: Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIp: str
        :param _InterceptNum: Number of blocks per minute
Note: This field may return null, indicating that no valid values can be obtained.
        :type InterceptNum: int
        :param _InterceptTime: Block time in rate-limiting policy per minute in seconds
        :type InterceptTime: int
        """
        self._ClientIp = None
        self._InterceptNum = None
        self._InterceptTime = None

    @property
    def ClientIp(self):
        """Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def InterceptNum(self):
        """Number of blocks per minute
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InterceptNum

    @InterceptNum.setter
    def InterceptNum(self, InterceptNum):
        self._InterceptNum = InterceptNum

    @property
    def InterceptTime(self):
        """Block time in rate-limiting policy per minute in seconds
        :rtype: int
        """
        return self._InterceptTime

    @InterceptTime.setter
    def InterceptTime(self, InterceptTime):
        self._InterceptTime = InterceptTime


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._InterceptNum = params.get("InterceptNum")
        self._InterceptTime = params.get("InterceptTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEventData(AbstractModel):
    """CC block event data

    """

    def __init__(self):
        r"""
        :param _List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CCInterceptEvent
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CCInterceptEvent
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CCInterceptEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLog(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param _AttackTime: Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        :param _AttackSip: Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackSip: str
        :param _AttackDomain: Attack domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackDomain: str
        :param _RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param _HitCount: Number of hits
Note: This field may return null, indicating that no valid values can be obtained.
        :type HitCount: int
        :param _SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param _EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param _DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param _HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param _RuleId: Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param _RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        """
        self._AttackTime = None
        self._AttackSip = None
        self._AttackDomain = None
        self._RequestUri = None
        self._HitCount = None
        self._SipCountryCode = None
        self._EventId = None
        self._DisposalMethod = None
        self._HttpLog = None
        self._RuleId = None
        self._RiskLevel = None

    @property
    def AttackTime(self):
        """Attack time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime

    @property
    def AttackSip(self):
        """Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackSip

    @AttackSip.setter
    def AttackSip(self, AttackSip):
        self._AttackSip = AttackSip

    @property
    def AttackDomain(self):
        """Attack domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackDomain

    @AttackDomain.setter
    def AttackDomain(self, AttackDomain):
        self._AttackDomain = AttackDomain

    @property
    def RequestUri(self):
        """Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestUri

    @RequestUri.setter
    def RequestUri(self, RequestUri):
        self._RequestUri = RequestUri

    @property
    def HitCount(self):
        """Number of hits
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HitCount

    @HitCount.setter
    def HitCount(self, HitCount):
        self._HitCount = HitCount

    @property
    def SipCountryCode(self):
        """IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SipCountryCode

    @SipCountryCode.setter
    def SipCountryCode(self, SipCountryCode):
        self._SipCountryCode = SipCountryCode

    @property
    def EventId(self):
        """Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DisposalMethod(self):
        """Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DisposalMethod

    @DisposalMethod.setter
    def DisposalMethod(self, DisposalMethod):
        self._DisposalMethod = DisposalMethod

    @property
    def HttpLog(self):
        """http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HttpLog

    @HttpLog.setter
    def HttpLog(self, HttpLog):
        self._HttpLog = HttpLog

    @property
    def RuleId(self):
        """Rule number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RiskLevel(self):
        """Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel


    def _deserialize(self, params):
        self._AttackTime = params.get("AttackTime")
        self._AttackSip = params.get("AttackSip")
        self._AttackDomain = params.get("AttackDomain")
        self._RequestUri = params.get("RequestUri")
        self._HitCount = params.get("HitCount")
        self._SipCountryCode = params.get("SipCountryCode")
        self._EventId = params.get("EventId")
        self._DisposalMethod = params.get("DisposalMethod")
        self._HttpLog = params.get("HttpLog")
        self._RuleId = params.get("RuleId")
        self._RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLogData(AbstractModel):
    """Block log in rate-limiting policy

    """

    def __init__(self):
        r"""
        :param _List: Data set of CC block logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of CCLog
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data set of CC block logs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CCLog
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CCLog()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration

    """

    def __init__(self):
        r"""
        :param _Cache: Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param _NoCache: No-cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param _FollowOrigin: Follows the origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        self._Cache = None
        self._NoCache = None
        self._FollowOrigin = None

    @property
    def Cache(self):
        """Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def NoCache(self):
        """No-cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        """
        return self._NoCache

    @NoCache.setter
    def NoCache(self, NoCache):
        self._NoCache = NoCache

    @property
    def FollowOrigin(self):
        """Follows the origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = CacheConfigCache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self._NoCache = CacheConfigNoCache()
            self._NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self._FollowOrigin = CacheConfigFollowOrigin()
            self._FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param _Switch: Cache configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param _CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTime: int
        :param _IgnoreCacheControl: Specifies whether to enable force cache
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCacheControl: str
        """
        self._Switch = None
        self._CacheTime = None
        self._IgnoreCacheControl = None

    @property
    def Switch(self):
        """Cache configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheTime(self):
        """Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def IgnoreCacheControl(self):
        """Specifies whether to enable force cache
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CacheTime = params.get("CacheTime")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """Follows the origin server configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Specifies whether to follow the origin server configuration
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Specifies whether to follow the origin server configuration
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """Do not cache the configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to cache the configuration
`on`: Do not cache
`off`: Cache
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to cache the configuration
`on`: Do not cache
`off`: Cache
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """Cache key configuration

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: Specifies whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String)
`off`: Disable full-path cache (i.e., enable Ignore Query String)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullUrlCache: str
        :param _IgnoreCase: Specifies whether the cache key is case sensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCase: str
        :param _QueryString: Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220106.models.QueryString`
        """
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None

    @property
    def FullUrlCache(self):
        """Specifies whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String)
`off`: Disable full-path cache (i.e., enable Ignore Query String)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        """Specifies whether the cache key is case sensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        """Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.QueryString`
        """
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = QueryString()
            self._QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """Cache prefresh

    """

    def __init__(self):
        r"""
        :param _Switch: Configuration switch
        :type Switch: str
        :param _Percent: Cache prefresh percentage. Values: 1-99
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        """
        self._Switch = None
        self._Percent = None

    @property
    def Switch(self):
        """Configuration switch
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Percent(self):
        """Cache prefresh percentage. Values: 1-99
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertFilter(AbstractModel):
    """Query filter to search for certificates

    """

    def __init__(self):
        r"""
        :param _Name: Filters by the field name. Values:
 - `host`: Domain name
 - `certId`: Certificate ID
 - `certAlias`: Certificate alias
 - `certType: default`: Default certificate; `upload`: External certificate; `managed`: Tencent Cloud certificate.
        :type Name: str
        :param _Values: Filters by the field value
        :type Values: list of str
        :param _Fuzzy: Specifies whether to enable fuzzy query, which only supports the `host` field.
If it is enabled, the length of `Value` must be 1.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        """Filters by the field name. Values:
 - `host`: Domain name
 - `certId`: Certificate ID
 - `certAlias`: Certificate alias
 - `certType: default`: Default certificate; `upload`: External certificate; `managed`: Tencent Cloud certificate.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filters by the field value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        """Specifies whether to enable fuzzy query, which only supports the `host` field.
If it is enabled, the length of `Value` must be 1.
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertSort(AbstractModel):
    """Sorting conditions for query results.

    """

    def __init__(self):
        r"""
        :param _Key: Fields that can be sorted. Values:
`createTime`: Domain name creation time
`certExpireTime`: Certificate expiration time
`certDeployTime`: Certificate deployment time
        :type Key: str
        :param _Sequence: Sorting order. Valid values: `asc` and `desc` (default).
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        """Fields that can be sorted. Values:
`createTime`: Domain name creation time
`certExpireTime`: Certificate expiration time
`certDeployTime`: Certificate deployment time
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
        """Sorting order. Valid values: `asc` and `desc` (default).
        :rtype: str
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _Certificate: Certificate
        :type Certificate: str
        :param _PrivateKey: Private key
        :type PrivateKey: str
        """
        self._Certificate = None
        self._PrivateKey = None

    @property
    def Certificate(self):
        """Certificate
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def PrivateKey(self):
        """Private key
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._Certificate = params.get("Certificate")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateResponse(AbstractModel):
    """CheckCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ClientIp(AbstractModel):
    """Client IP header

    """

    def __init__(self):
        r"""
        :param _Switch: Specifies whether to enable client IP header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param _HeaderName: Name of the origin-pull client IP request header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeaderName: str
        """
        self._Switch = None
        self._HeaderName = None

    @property
    def Switch(self):
        """Specifies whether to enable client IP header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderName(self):
        """Name of the origin-pull client IP request header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CnameStatus(AbstractModel):
    """CNAME status

    """

    def __init__(self):
        r"""
        :param _Name: Record name
        :type Name: str
        :param _Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param _Status: Status
`active`: Activated
`moved`: Not activated
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self._Name = None
        self._Cname = None
        self._Status = None

    @property
    def Name(self):
        """Record name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cname(self):
        """CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        """Status
`active`: Activated
`moved`: Not activated
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Smart compression
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to enable Smart compression
`on`: Enable
`off`: Disable
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param _PlatType: Scheduling mode. Values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param _SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param _AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param _ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param _SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param _Rule: Rule details
        :type Rule: list of ApplicationProxyRule
        :param _SessionPersistTime: Session persistence duration. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param _ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        """
        self._ZoneId = None
        self._ZoneName = None
        self._ProxyName = None
        self._PlatType = None
        self._SecurityType = None
        self._AccelerateType = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._Rule = None
        self._SessionPersistTime = None
        self._ProxyType = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ProxyName(self):
        """Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def PlatType(self):
        """Scheduling mode. Values:
`ip`: Anycast IP
`domain`: CNAME
        :rtype: str
        """
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def SecurityType(self):
        """`0`: Disable security protection; `1`: Enable security protection.
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        """`0`: Disable acceleration; `1`: Enable acceleration.
        :rtype: int
        """
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def ForwardClientIp(self):
        """This field is moved to `Rule.ForwardClientIp`.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """This field is moved to `Rule.SessionPersist`.
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def Rule(self):
        """Rule details
        :rtype: list of ApplicationProxyRule
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def SessionPersistTime(self):
        """Session persistence duration. Value range: 30-3600 (in seconds).
        :rtype: int
        """
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        """Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :rtype: str
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ProxyName = params.get("ProxyName")
        self._PlatType = params.get("PlatType")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Layer-4 application proxy ID
        :type ProxyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """Layer-4 application proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        :param _Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param _Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param _OriginType: Origin type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param _OriginValue: Origin information:
When `OriginType=custom`, it can include one or more origins in either of the following formats:
IP:Port
Domain name:Port
When `OriginType=origins`, it is an origin group ID.
        :type OriginValue: list of str
        :param _ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param _SessionPersist: Specifies whether to enable session persistence 
        :type SessionPersist: bool
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Proto(self):
        """Protocol. Valid values: `TCP` and `UDP`.
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        """Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :rtype: list of str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        """Origin type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        """Origin information:
When `OriginType=custom`, it can include one or more origins in either of the following formats:
IP:Port
Domain name:Port
When `OriginType=origins`, it is an origin group ID.
        :rtype: list of str
        """
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        """Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """Specifies whether to enable session persistence 
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateApplicationProxyRulesRequest(AbstractModel):
    """CreateApplicationProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        :param _Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Rule = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Rule(self):
        """Rule list
        :rtype: list of ApplicationProxyRule
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRulesResponse(AbstractModel):
    """CreateApplicationProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Array of rule IDs
        :type RuleId: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """Array of rule IDs
        :rtype: list of str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateCustomErrorPageRequest(AbstractModel):
    """CreateCustomErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Entity: Subdomain name of the site
        :type Entity: str
        :param _Name: Name of the file specified to be returned
        :type Name: str
        :param _Content: Content of the custom page
        :type Content: str
        """
        self._ZoneId = None
        self._Entity = None
        self._Name = None
        self._Content = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Subdomain name of the site
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Name(self):
        """Name of the file specified to be returned
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Content of the custom page
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomErrorPageResponse(AbstractModel):
    """CreateCustomErrorPage response structure.

    """

    def __init__(self):
        r"""
        :param _PageId: ID of the custom page
        :type PageId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PageId = None
        self._RequestId = None

    @property
    def PageId(self):
        """ID of the custom page
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Type: Record type
        :type Type: str
        :param _Name: Record name
        :type Name: str
        :param _Content: Record content
        :type Content: str
        :param _Mode: Proxy mode. Valid values: `dns_only`, `cdn_only`, and `secure_cdn`.
        :type Mode: str
        :param _Ttl: 
        :type Ttl: int
        :param _Priority: Priority
        :type Priority: int
        """
        self._ZoneId = None
        self._Type = None
        self._Name = None
        self._Content = None
        self._Mode = None
        self._Ttl = None
        self._Priority = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        """Record type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Record name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Record content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Mode(self):
        """Proxy mode. Valid values: `dns_only`, `cdn_only`, and `secure_cdn`.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Ttl(self):
        """
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Priority(self):
        """Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Mode = params.get("Mode")
        self._Ttl = params.get("Ttl")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDnsRecordResponse(AbstractModel):
    """CreateDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: str
        :param _Type: Record type
        :type Type: str
        :param _Name: Record name
        :type Name: str
        :param _Content: Record content
        :type Content: str
        :param _Ttl: 
        :type Ttl: int
        :param _Priority: Priority
        :type Priority: int
        :param _Mode: Proxy mode
        :type Mode: str
        :param _Status: Resolution status. Valid values:
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param _Locked: Whether the DNS record is locked
        :type Locked: bool
        :param _CreatedOn: Creation time
        :type CreatedOn: str
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Type = None
        self._Name = None
        self._Content = None
        self._Ttl = None
        self._Priority = None
        self._Mode = None
        self._Status = None
        self._Locked = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._ZoneId = None
        self._ZoneName = None
        self._Cname = None
        self._RequestId = None

    @property
    def Id(self):
        """Record ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """Record type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Record name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Record content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ttl(self):
        """
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Priority(self):
        """Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Mode(self):
        """Proxy mode
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        """Resolution status. Valid values:
`active`: Activated
`pending`: Not activated
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Locked(self):
        """Whether the DNS record is locked
        :rtype: bool
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def CreatedOn(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Cname(self):
        """CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Ttl = params.get("Ttl")
        self._Priority = params.get("Priority")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._Locked = params.get("Locked")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._Cname = params.get("Cname")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Host: Subdomain name
        :type Host: str
        :param _Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param _OriginId: ID of the origin group used
        :type OriginId: list of str
        :param _TTL: Indicates DNS TTL time when `Type=dns_only` 
        :type TTL: int
        """
        self._ZoneId = None
        self._Host = None
        self._Type = None
        self._OriginId = None
        self._TTL = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Host(self):
        """Subdomain name
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Type(self):
        """Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OriginId(self):
        """ID of the origin group used
        :rtype: list of str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def TTL(self):
        """Indicates DNS TTL time when `Type=dns_only` 
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Host = params.get("Host")
        self._Type = params.get("Type")
        self._OriginId = params.get("OriginId")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancingResponse(AbstractModel):
    """CreateLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancingId = None
        self._RequestId = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _OriginName: Name of the origin group
        :type OriginName: str
        :param _Type: Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :type Type: str
        :param _Record: Origin records
        :type Record: list of OriginRecord
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _OriginType: Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :type OriginType: str
        """
        self._OriginName = None
        self._Type = None
        self._Record = None
        self._ZoneId = None
        self._OriginType = None

    @property
    def OriginName(self):
        """Name of the origin group
        :rtype: str
        """
        return self._OriginName

    @OriginName.setter
    def OriginName(self, OriginName):
        self._OriginName = OriginName

    @property
    def Type(self):
        """Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Record(self):
        """Origin records
        :rtype: list of OriginRecord
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OriginType(self):
        """Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType


    def _deserialize(self, params):
        self._OriginName = params.get("OriginName")
        self._Type = params.get("Type")
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Record.append(obj)
        self._ZoneId = params.get("ZoneId")
        self._OriginType = params.get("OriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOriginGroupResponse(AbstractModel):
    """CreateOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: ID of the newly added origin group
        :type OriginId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginId = None
        self._RequestId = None

    @property
    def OriginId(self):
        """ID of the newly added origin group
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param _EncodeUrl: Specifies whether to encode the URL
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        :param _Headers: HTTP header information
        :type Headers: list of Header
        """
        self._ZoneId = None
        self._Targets = None
        self._EncodeUrl = None
        self._Headers = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Targets(self):
        """List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :rtype: list of str
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        """Specifies whether to encode the URL
Note that if it’s enabled, the purging is based on the converted URLs.
        :rtype: bool
        """
        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        self._EncodeUrl = EncodeUrl

    @property
    def Headers(self):
        """HTTP header information
        :rtype: list of Header
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _FailedList: List of failed tasks
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedList: list of FailReason
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        """List of failed tasks
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of FailReason
        """
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Type: Type of the purging task. Values:
- `purge_url`: Purge by the URL
- `purge_prefix`: Purge by the prefix
- `purge_host`: Purge by the Hostname
- `purge_all`: Purge all cached contents
        :type Type: str
        :param _Targets: Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Hostnames are purged, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Prefixes are purged, such as http://www.example.com/example.
3. When `Type = purge_url`:
URLs are purged, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`: All types of resources are purged.
`Targets` is not a required field.
        :type Targets: list of str
        :param _EncodeUrl: Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        """
        self._ZoneId = None
        self._Type = None
        self._Targets = None
        self._EncodeUrl = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        """Type of the purging task. Values:
- `purge_url`: Purge by the URL
- `purge_prefix`: Purge by the prefix
- `purge_host`: Purge by the Hostname
- `purge_all`: Purge all cached contents
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Targets(self):
        """Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Hostnames are purged, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Prefixes are purged, such as http://www.example.com/example.
3. When `Type = purge_url`:
URLs are purged, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`: All types of resources are purged.
`Targets` is not a required field.
        :rtype: list of str
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        """Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :rtype: bool
        """
        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        self._EncodeUrl = EncodeUrl


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _FailedList: List of failed tasks and reasons
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedList: list of FailReason
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        """List of failed tasks and reasons
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of FailReason
        """
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _Type: Access mode. Valid values:
- `full` (default): Access via NS
- `partial`: Access via CNAME
        :type Type: str
        :param _JumpStart: Specifies whether to skip resolution record scanning
        :type JumpStart: bool
        :param _Tags: Resource tag
        :type Tags: list of Tag
        """
        self._Name = None
        self._Type = None
        self._JumpStart = None
        self._Tags = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Access mode. Valid values:
- `full` (default): Access via NS
- `partial`: Access via CNAME
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def JumpStart(self):
        """Specifies whether to skip resolution record scanning
        :rtype: bool
        """
        return self._JumpStart

    @JumpStart.setter
    def JumpStart(self, JumpStart):
        self._JumpStart = JumpStart

    @property
    def Tags(self):
        """Resource tag
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._JumpStart = params.get("JumpStart")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneResponse(AbstractModel):
    """CreateZone response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _Type: Specifies how the site is connected to EdgeOne.
        :type Type: str
        :param _Status: Site status
- `pending`: The name server is not switched.
- `active`: The name server is switched to another assigned.
- `moved`: Move the NS out of Tencent Cloud
        :type Status: str
        :param _OriginalNameServers: List of name servers
        :type OriginalNameServers: list of str
        :param _NameServers: List of name servers assigned to users
        :type NameServers: list of str
        :param _CreatedOn: Site creation date
        :type CreatedOn: str
        :param _ModifiedOn: Site update time
        :type ModifiedOn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Status = None
        self._OriginalNameServers = None
        self._NameServers = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Specifies how the site is connected to EdgeOne.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """Site status
- `pending`: The name server is not switched.
- `active`: The name server is switched to another assigned.
- `moved`: Move the NS out of Tencent Cloud
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalNameServers(self):
        """List of name servers
        :rtype: list of str
        """
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def NameServers(self):
        """List of name servers assigned to users
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def CreatedOn(self):
        """Site creation date
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Site update time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._NameServers = params.get("NameServers")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._RequestId = params.get("RequestId")


class DDoSAcl(AbstractModel):
    """DDoS port filtering configuration

    """

    def __init__(self):
        r"""
        :param _DportEnd: Destination port used as the end port
        :type DportEnd: int
        :param _DportStart: Destination port used as the start port
        :type DportStart: int
        :param _SportEnd: Source port used as the end port
        :type SportEnd: int
        :param _SportStart: Source port used as the start port
        :type SportStart: int
        :param _Protocol: Protocol. Values: `tcp`, `udp`, and `all`.
        :type Protocol: str
        :param _Action: Action. Values: `drop` (Drop the request); `transmit` (Allow the request); `forward` (Continue to offer protection).
        :type Action: str
        :param _Default: Whether it is a system configuration. Values: `0` (manual configuration); `1` (system configuration).
        :type Default: int
        """
        self._DportEnd = None
        self._DportStart = None
        self._SportEnd = None
        self._SportStart = None
        self._Protocol = None
        self._Action = None
        self._Default = None

    @property
    def DportEnd(self):
        """Destination port used as the end port
        :rtype: int
        """
        return self._DportEnd

    @DportEnd.setter
    def DportEnd(self, DportEnd):
        self._DportEnd = DportEnd

    @property
    def DportStart(self):
        """Destination port used as the start port
        :rtype: int
        """
        return self._DportStart

    @DportStart.setter
    def DportStart(self, DportStart):
        self._DportStart = DportStart

    @property
    def SportEnd(self):
        """Source port used as the end port
        :rtype: int
        """
        return self._SportEnd

    @SportEnd.setter
    def SportEnd(self, SportEnd):
        self._SportEnd = SportEnd

    @property
    def SportStart(self):
        """Source port used as the start port
        :rtype: int
        """
        return self._SportStart

    @SportStart.setter
    def SportStart(self, SportStart):
        self._SportStart = SportStart

    @property
    def Protocol(self):
        """Protocol. Values: `tcp`, `udp`, and `all`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Action(self):
        """Action. Values: `drop` (Drop the request); `transmit` (Allow the request); `forward` (Continue to offer protection).
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Default(self):
        """Whether it is a system configuration. Values: `0` (manual configuration); `1` (system configuration).
        :rtype: int
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default


    def _deserialize(self, params):
        self._DportEnd = params.get("DportEnd")
        self._DportStart = params.get("DportStart")
        self._SportEnd = params.get("SportEnd")
        self._SportStart = params.get("SportStart")
        self._Protocol = params.get("Protocol")
        self._Action = params.get("Action")
        self._Default = params.get("Default")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAntiPly(AbstractModel):
    """DDoS protection against protocol and connection attacks

    """

    def __init__(self):
        r"""
        :param _DropTcp: Enables TCP protocol blocking. `on` (enable); `off` (disable).
        :type DropTcp: str
        :param _DropUdp: Enables UDP protocol blocking. `on` (enable); `off` (disable).
        :type DropUdp: str
        :param _DropIcmp: Enables ICMP protocol blocking. `on` (enable); `off` (disable).
        :type DropIcmp: str
        :param _DropOther: Enables blocking for other protocols. `on` (enable); `off` (disable).
        :type DropOther: str
        :param _SourceCreateLimit: Number of new connections the source port can establish. Value range: 0-4294967295.
        :type SourceCreateLimit: int
        :param _SourceConnectLimit: Number of concurrent connections the source port can establish. Value range: 0-4294967295.
        :type SourceConnectLimit: int
        :param _DestinationCreateLimit: Number of new connections the destination port can establish. Value range: 0-4294967295.
        :type DestinationCreateLimit: int
        :param _DestinationConnectLimit: Number of concurrent connections the destination port can establish. Value range: 0-4294967295.
        :type DestinationConnectLimit: int
        :param _AbnormalConnectNum: Number of abnormal connections allowed. Value range: 0-4294967295.
        :type AbnormalConnectNum: int
        :param _AbnormalSynRatio: Specifies the ratio of SYN exceptions to trigger alerts. Value range: 0-100
        :type AbnormalSynRatio: int
        :param _AbnormalSynNum: Specifies a max number of SYN packets that triggers alarms. Value range: 0-65535
        :type AbnormalSynNum: int
        :param _ConnectTimeout: Connection timeout period. Value range: 0-65535.
        :type ConnectTimeout: int
        :param _EmptyConnectProtect: Whether to enable null session protection. `0`: Disable; `1`: Enable.
        :type EmptyConnectProtect: str
        :param _UdpShard: Whether to enable UDP fragmentation. `off`: Disable; `on`: Enable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UdpShard: str
        """
        self._DropTcp = None
        self._DropUdp = None
        self._DropIcmp = None
        self._DropOther = None
        self._SourceCreateLimit = None
        self._SourceConnectLimit = None
        self._DestinationCreateLimit = None
        self._DestinationConnectLimit = None
        self._AbnormalConnectNum = None
        self._AbnormalSynRatio = None
        self._AbnormalSynNum = None
        self._ConnectTimeout = None
        self._EmptyConnectProtect = None
        self._UdpShard = None

    @property
    def DropTcp(self):
        """Enables TCP protocol blocking. `on` (enable); `off` (disable).
        :rtype: str
        """
        return self._DropTcp

    @DropTcp.setter
    def DropTcp(self, DropTcp):
        self._DropTcp = DropTcp

    @property
    def DropUdp(self):
        """Enables UDP protocol blocking. `on` (enable); `off` (disable).
        :rtype: str
        """
        return self._DropUdp

    @DropUdp.setter
    def DropUdp(self, DropUdp):
        self._DropUdp = DropUdp

    @property
    def DropIcmp(self):
        """Enables ICMP protocol blocking. `on` (enable); `off` (disable).
        :rtype: str
        """
        return self._DropIcmp

    @DropIcmp.setter
    def DropIcmp(self, DropIcmp):
        self._DropIcmp = DropIcmp

    @property
    def DropOther(self):
        """Enables blocking for other protocols. `on` (enable); `off` (disable).
        :rtype: str
        """
        return self._DropOther

    @DropOther.setter
    def DropOther(self, DropOther):
        self._DropOther = DropOther

    @property
    def SourceCreateLimit(self):
        """Number of new connections the source port can establish. Value range: 0-4294967295.
        :rtype: int
        """
        return self._SourceCreateLimit

    @SourceCreateLimit.setter
    def SourceCreateLimit(self, SourceCreateLimit):
        self._SourceCreateLimit = SourceCreateLimit

    @property
    def SourceConnectLimit(self):
        """Number of concurrent connections the source port can establish. Value range: 0-4294967295.
        :rtype: int
        """
        return self._SourceConnectLimit

    @SourceConnectLimit.setter
    def SourceConnectLimit(self, SourceConnectLimit):
        self._SourceConnectLimit = SourceConnectLimit

    @property
    def DestinationCreateLimit(self):
        """Number of new connections the destination port can establish. Value range: 0-4294967295.
        :rtype: int
        """
        return self._DestinationCreateLimit

    @DestinationCreateLimit.setter
    def DestinationCreateLimit(self, DestinationCreateLimit):
        self._DestinationCreateLimit = DestinationCreateLimit

    @property
    def DestinationConnectLimit(self):
        """Number of concurrent connections the destination port can establish. Value range: 0-4294967295.
        :rtype: int
        """
        return self._DestinationConnectLimit

    @DestinationConnectLimit.setter
    def DestinationConnectLimit(self, DestinationConnectLimit):
        self._DestinationConnectLimit = DestinationConnectLimit

    @property
    def AbnormalConnectNum(self):
        """Number of abnormal connections allowed. Value range: 0-4294967295.
        :rtype: int
        """
        return self._AbnormalConnectNum

    @AbnormalConnectNum.setter
    def AbnormalConnectNum(self, AbnormalConnectNum):
        self._AbnormalConnectNum = AbnormalConnectNum

    @property
    def AbnormalSynRatio(self):
        """Specifies the ratio of SYN exceptions to trigger alerts. Value range: 0-100
        :rtype: int
        """
        return self._AbnormalSynRatio

    @AbnormalSynRatio.setter
    def AbnormalSynRatio(self, AbnormalSynRatio):
        self._AbnormalSynRatio = AbnormalSynRatio

    @property
    def AbnormalSynNum(self):
        """Specifies a max number of SYN packets that triggers alarms. Value range: 0-65535
        :rtype: int
        """
        return self._AbnormalSynNum

    @AbnormalSynNum.setter
    def AbnormalSynNum(self, AbnormalSynNum):
        self._AbnormalSynNum = AbnormalSynNum

    @property
    def ConnectTimeout(self):
        """Connection timeout period. Value range: 0-65535.
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def EmptyConnectProtect(self):
        """Whether to enable null session protection. `0`: Disable; `1`: Enable.
        :rtype: str
        """
        return self._EmptyConnectProtect

    @EmptyConnectProtect.setter
    def EmptyConnectProtect(self, EmptyConnectProtect):
        self._EmptyConnectProtect = EmptyConnectProtect

    @property
    def UdpShard(self):
        """Whether to enable UDP fragmentation. `off`: Disable; `on`: Enable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UdpShard

    @UdpShard.setter
    def UdpShard(self, UdpShard):
        self._UdpShard = UdpShard


    def _deserialize(self, params):
        self._DropTcp = params.get("DropTcp")
        self._DropUdp = params.get("DropUdp")
        self._DropIcmp = params.get("DropIcmp")
        self._DropOther = params.get("DropOther")
        self._SourceCreateLimit = params.get("SourceCreateLimit")
        self._SourceConnectLimit = params.get("SourceConnectLimit")
        self._DestinationCreateLimit = params.get("DestinationCreateLimit")
        self._DestinationConnectLimit = params.get("DestinationConnectLimit")
        self._AbnormalConnectNum = params.get("AbnormalConnectNum")
        self._AbnormalSynRatio = params.get("AbnormalSynRatio")
        self._AbnormalSynNum = params.get("AbnormalSynNum")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._EmptyConnectProtect = params.get("EmptyConnectProtect")
        self._UdpShard = params.get("UdpShard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSApplication(AbstractModel):
    """DDoS protection for the application layer (layer 7)

    """

    def __init__(self):
        r"""
        :param _Host: Second-level domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Host: str
        :param _Status: Status of the domain name
`init`: NS to be switched
`offline`: Site acceleration not enabled with DNS
`process`: Deployment in progress
`online`: Normal
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param _AccelerateType: Site acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `SecurityType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccelerateType: str
        :param _SecurityType: Security acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `AccelerateType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SecurityType: str
        """
        self._Host = None
        self._Status = None
        self._AccelerateType = None
        self._SecurityType = None

    @property
    def Host(self):
        """Second-level domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Status(self):
        """Status of the domain name
`init`: NS to be switched
`offline`: Site acceleration not enabled with DNS
`process`: Deployment in progress
`online`: Normal
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccelerateType(self):
        """Site acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `SecurityType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def SecurityType(self):
        """Security acceleration switch. `on`: Enable site acceleration; `off`: Disable site acceleration. This field can be used together with `AccelerateType`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Status = params.get("Status")
        self._AccelerateType = params.get("AccelerateType")
        self._SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSConfig(AbstractModel):
    """DDoS configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Switch
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSFeaturesFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param _Action: Action. `drop`: Drop the request; `transmit`: Allow the request; `drop_block`: Drop the request and block it; `forward`: Continue to offer protection.
        :type Action: str
        :param _Depth: Sets how far from the first search position
        :type Depth: int
        :param _Depth2: Sets how far from the second search position
        :type Depth2: int
        :param _DportEnd: End of the destination port
        :type DportEnd: int
        :param _DportStart: Start of the destination port
        :type DportStart: int
        :param _IsNot: Whether to match string 1 that does not contain all the specified elements
        :type IsNot: int
        :param _IsNot2: Whether to match string 2 that does not contain all the specified elements
        :type IsNot2: int
        :param _MatchLogic: Logical operator that combines two conditions. Values: `none`, `and` and `or`. If there is only one condition, pass in `none` for this condition only.
        :type MatchLogic: str
        :param _MatchType: Matching method of the first condition. `pcre`: Regex match; `sunday`: String match.
        :type MatchType: str
        :param _MatchType2: Matching method of the second condition. `pcre`: Regex match; `sunday`: String match.
        :type MatchType2: str
        :param _Offset: Offset from the first search position
        :type Offset: int
        :param _Offset2: Offset from the second search position
        :type Offset2: int
        :param _PacketMax: Maximum packet length
        :type PacketMax: int
        :param _PacketMin: Minimum packet length
        :type PacketMin: int
        :param _Protocol: Protocol. Values: `tcp`, `udp`, `icmp` and `all`.
        :type Protocol: str
        :param _SportEnd: End of the source port
        :type SportEnd: int
        :param _SportStart: Start of the source port
        :type SportStart: int
        :param _Str: String in the first condition
        :type Str: str
        :param _Str2: String in the second condition
        :type Str2: str
        :param _MatchBegin: Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :type MatchBegin: str
        :param _MatchBegin2: Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :type MatchBegin2: str
        """
        self._Action = None
        self._Depth = None
        self._Depth2 = None
        self._DportEnd = None
        self._DportStart = None
        self._IsNot = None
        self._IsNot2 = None
        self._MatchLogic = None
        self._MatchType = None
        self._MatchType2 = None
        self._Offset = None
        self._Offset2 = None
        self._PacketMax = None
        self._PacketMin = None
        self._Protocol = None
        self._SportEnd = None
        self._SportStart = None
        self._Str = None
        self._Str2 = None
        self._MatchBegin = None
        self._MatchBegin2 = None

    @property
    def Action(self):
        """Action. `drop`: Drop the request; `transmit`: Allow the request; `drop_block`: Drop the request and block it; `forward`: Continue to offer protection.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Depth(self):
        """Sets how far from the first search position
        :rtype: int
        """
        return self._Depth

    @Depth.setter
    def Depth(self, Depth):
        self._Depth = Depth

    @property
    def Depth2(self):
        """Sets how far from the second search position
        :rtype: int
        """
        return self._Depth2

    @Depth2.setter
    def Depth2(self, Depth2):
        self._Depth2 = Depth2

    @property
    def DportEnd(self):
        """End of the destination port
        :rtype: int
        """
        return self._DportEnd

    @DportEnd.setter
    def DportEnd(self, DportEnd):
        self._DportEnd = DportEnd

    @property
    def DportStart(self):
        """Start of the destination port
        :rtype: int
        """
        return self._DportStart

    @DportStart.setter
    def DportStart(self, DportStart):
        self._DportStart = DportStart

    @property
    def IsNot(self):
        """Whether to match string 1 that does not contain all the specified elements
        :rtype: int
        """
        return self._IsNot

    @IsNot.setter
    def IsNot(self, IsNot):
        self._IsNot = IsNot

    @property
    def IsNot2(self):
        """Whether to match string 2 that does not contain all the specified elements
        :rtype: int
        """
        return self._IsNot2

    @IsNot2.setter
    def IsNot2(self, IsNot2):
        self._IsNot2 = IsNot2

    @property
    def MatchLogic(self):
        """Logical operator that combines two conditions. Values: `none`, `and` and `or`. If there is only one condition, pass in `none` for this condition only.
        :rtype: str
        """
        return self._MatchLogic

    @MatchLogic.setter
    def MatchLogic(self, MatchLogic):
        self._MatchLogic = MatchLogic

    @property
    def MatchType(self):
        """Matching method of the first condition. `pcre`: Regex match; `sunday`: String match.
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchType2(self):
        """Matching method of the second condition. `pcre`: Regex match; `sunday`: String match.
        :rtype: str
        """
        return self._MatchType2

    @MatchType2.setter
    def MatchType2(self, MatchType2):
        self._MatchType2 = MatchType2

    @property
    def Offset(self):
        """Offset from the first search position
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Offset2(self):
        """Offset from the second search position
        :rtype: int
        """
        return self._Offset2

    @Offset2.setter
    def Offset2(self, Offset2):
        self._Offset2 = Offset2

    @property
    def PacketMax(self):
        """Maximum packet length
        :rtype: int
        """
        return self._PacketMax

    @PacketMax.setter
    def PacketMax(self, PacketMax):
        self._PacketMax = PacketMax

    @property
    def PacketMin(self):
        """Minimum packet length
        :rtype: int
        """
        return self._PacketMin

    @PacketMin.setter
    def PacketMin(self, PacketMin):
        self._PacketMin = PacketMin

    @property
    def Protocol(self):
        """Protocol. Values: `tcp`, `udp`, `icmp` and `all`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SportEnd(self):
        """End of the source port
        :rtype: int
        """
        return self._SportEnd

    @SportEnd.setter
    def SportEnd(self, SportEnd):
        self._SportEnd = SportEnd

    @property
    def SportStart(self):
        """Start of the source port
        :rtype: int
        """
        return self._SportStart

    @SportStart.setter
    def SportStart(self, SportStart):
        self._SportStart = SportStart

    @property
    def Str(self):
        """String in the first condition
        :rtype: str
        """
        return self._Str

    @Str.setter
    def Str(self, Str):
        self._Str = Str

    @property
    def Str2(self):
        """String in the second condition
        :rtype: str
        """
        return self._Str2

    @Str2.setter
    def Str2(self, Str2):
        self._Str2 = Str2

    @property
    def MatchBegin(self):
        """Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :rtype: str
        """
        return self._MatchBegin

    @MatchBegin.setter
    def MatchBegin(self, MatchBegin):
        self._MatchBegin = MatchBegin

    @property
    def MatchBegin2(self):
        """Layer at which each match starts. Values: `begin_l5`, `no_match`, `begin_l3` and `begin_l4`.
        :rtype: str
        """
        return self._MatchBegin2

    @MatchBegin2.setter
    def MatchBegin2(self, MatchBegin2):
        self._MatchBegin2 = MatchBegin2


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Depth = params.get("Depth")
        self._Depth2 = params.get("Depth2")
        self._DportEnd = params.get("DportEnd")
        self._DportStart = params.get("DportStart")
        self._IsNot = params.get("IsNot")
        self._IsNot2 = params.get("IsNot2")
        self._MatchLogic = params.get("MatchLogic")
        self._MatchType = params.get("MatchType")
        self._MatchType2 = params.get("MatchType2")
        self._Offset = params.get("Offset")
        self._Offset2 = params.get("Offset2")
        self._PacketMax = params.get("PacketMax")
        self._PacketMin = params.get("PacketMin")
        self._Protocol = params.get("Protocol")
        self._SportEnd = params.get("SportEnd")
        self._SportStart = params.get("SportStart")
        self._Str = params.get("Str")
        self._Str2 = params.get("Str2")
        self._MatchBegin = params.get("MatchBegin")
        self._MatchBegin2 = params.get("MatchBegin2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIp(AbstractModel):
    """DDoS regional blocking

    """

    def __init__(self):
        r"""
        :param _RegionId: Region information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegionId: list of int
        :param _Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        """
        self._RegionId = None
        self._Switch = None

    @property
    def RegionId(self):
        """Region information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Switch(self):
        """Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSStatusInfo(AbstractModel):
    """DDoS protection level

    """

    def __init__(self):
        r"""
        :param _AiStatus: This field is not supported. Value: `off`.
        :type AiStatus: str
        :param _Appid: User appid
        :type Appid: str
        :param _PlyLevel: Protection level. Values: `low`, `middle`, and `high`.
        :type PlyLevel: str
        """
        self._AiStatus = None
        self._Appid = None
        self._PlyLevel = None

    @property
    def AiStatus(self):
        """This field is not supported. Value: `off`.
        :rtype: str
        """
        return self._AiStatus

    @AiStatus.setter
    def AiStatus(self, AiStatus):
        self._AiStatus = AiStatus

    @property
    def Appid(self):
        """User appid
        :rtype: str
        """
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def PlyLevel(self):
        """Protection level. Values: `low`, `middle`, and `high`.
        :rtype: str
        """
        return self._PlyLevel

    @PlyLevel.setter
    def PlyLevel(self, PlyLevel):
        self._PlyLevel = PlyLevel


    def _deserialize(self, params):
        self._AiStatus = params.get("AiStatus")
        self._Appid = params.get("Appid")
        self._PlyLevel = params.get("PlyLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUserAllowBlockIP(AbstractModel):
    """IP Allowlist/Blocklist for DDoS protection

    """

    def __init__(self):
        r"""
        :param _Ip: Start IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ip: str
        :param _Mask: Start mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mask: int
        :param _Type: IP type. `block`: IP blocklist; `allow`: IP allowlist.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _UpdateTime: Timestamp
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: int
        :param _Ip2: End IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ip2: str
        :param _Mask2: End mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mask2: int
        """
        self._Ip = None
        self._Mask = None
        self._Type = None
        self._UpdateTime = None
        self._Ip2 = None
        self._Mask2 = None

    @property
    def Ip(self):
        """Start IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mask(self):
        """Start mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Type(self):
        """IP type. `block`: IP blocklist; `allow`: IP allowlist.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdateTime(self):
        """Timestamp
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Ip2(self):
        """End IP address in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Ip2

    @Ip2.setter
    def Ip2(self, Ip2):
        self._Ip2 = Ip2

    @property
    def Mask2(self):
        """End mask in a specific range
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Mask2

    @Mask2.setter
    def Mask2(self, Mask2):
        self._Mask2 = Mask2


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Mask = params.get("Mask")
        self._Type = params.get("Type")
        self._UpdateTime = params.get("UpdateTime")
        self._Ip2 = params.get("Ip2")
        self._Mask2 = params.get("Mask2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEvent(AbstractModel):
    """DDoS attack event object

    """

    def __init__(self):
        r"""
        :param _PolicyId: DDoS policy group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param _AttackType: Attack type (corresponding to interaction event name)
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param _AttackStatus: Attack status
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackStatus: int
        :param _AttackMaxBandWidth: Maximum attack bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackMaxBandWidth: int
        :param _AttackPacketMaxRate: Peak attack packet rate
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackPacketMaxRate: int
        :param _AttackStartTime: Attack start time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackStartTime: int
        :param _AttackEndTime: Attack end time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackEndTime: int
        :param _EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param _ZoneId: Site ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        """
        self._PolicyId = None
        self._AttackType = None
        self._AttackStatus = None
        self._AttackMaxBandWidth = None
        self._AttackPacketMaxRate = None
        self._AttackStartTime = None
        self._AttackEndTime = None
        self._EventId = None
        self._ZoneId = None

    @property
    def PolicyId(self):
        """DDoS policy group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttackType(self):
        """Attack type (corresponding to interaction event name)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def AttackStatus(self):
        """Attack status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def AttackMaxBandWidth(self):
        """Maximum attack bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackMaxBandWidth

    @AttackMaxBandWidth.setter
    def AttackMaxBandWidth(self, AttackMaxBandWidth):
        self._AttackMaxBandWidth = AttackMaxBandWidth

    @property
    def AttackPacketMaxRate(self):
        """Peak attack packet rate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackPacketMaxRate

    @AttackPacketMaxRate.setter
    def AttackPacketMaxRate(self, AttackPacketMaxRate):
        self._AttackPacketMaxRate = AttackPacketMaxRate

    @property
    def AttackStartTime(self):
        """Attack start time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackStartTime

    @AttackStartTime.setter
    def AttackStartTime(self, AttackStartTime):
        self._AttackStartTime = AttackStartTime

    @property
    def AttackEndTime(self):
        """Attack end time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackEndTime

    @AttackEndTime.setter
    def AttackEndTime(self, AttackEndTime):
        self._AttackEndTime = AttackEndTime

    @property
    def EventId(self):
        """Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def ZoneId(self):
        """Site ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttackType = params.get("AttackType")
        self._AttackStatus = params.get("AttackStatus")
        self._AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self._AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self._AttackStartTime = params.get("AttackStartTime")
        self._AttackEndTime = params.get("AttackEndTime")
        self._EventId = params.get("EventId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventData(AbstractModel):
    """DDoS attack event data

    """

    def __init__(self):
        r"""
        :param _List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosAttackEvent
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DDosAttackEvent
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DDosAttackEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventDetailData(AbstractModel):
    """DDoS attack event details

    """

    def __init__(self):
        r"""
        :param _AttackStatus: Attack status
        :type AttackStatus: int
        :param _AttackType: Attack type
        :type AttackType: str
        :param _EndTime: End time
        :type EndTime: int
        :param _StartTime: Start time
        :type StartTime: int
        :param _MaxBandWidth: Maximum bandwidth
        :type MaxBandWidth: int
        :param _PacketMaxRate: Maximum packet rate
        :type PacketMaxRate: int
        :param _EventId: Event ID
        :type EventId: str
        :param _PolicyId: DDoS policy group ID
        :type PolicyId: int
        """
        self._AttackStatus = None
        self._AttackType = None
        self._EndTime = None
        self._StartTime = None
        self._MaxBandWidth = None
        self._PacketMaxRate = None
        self._EventId = None
        self._PolicyId = None

    @property
    def AttackStatus(self):
        """Attack status
        :rtype: int
        """
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def AttackType(self):
        """Attack type
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def MaxBandWidth(self):
        """Maximum bandwidth
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def PacketMaxRate(self):
        """Maximum packet rate
        :rtype: int
        """
        return self._PacketMaxRate

    @PacketMaxRate.setter
    def PacketMaxRate(self, PacketMaxRate):
        self._PacketMaxRate = PacketMaxRate

    @property
    def EventId(self):
        """Event ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def PolicyId(self):
        """DDoS policy group ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._AttackStatus = params.get("AttackStatus")
        self._AttackType = params.get("AttackType")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._PacketMaxRate = params.get("PacketMaxRate")
        self._EventId = params.get("EventId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackSourceEvent(AbstractModel):
    """DDoS attack event object

    """

    def __init__(self):
        r"""
        :param _AttackSourceIp: Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackSourceIp: str
        :param _AttackRegion: Country/Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackRegion: str
        :param _AttackFlow: Accumulative attack traffic
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackFlow: int
        :param _AttackPacketNum: Accumulative number of attack packets
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackPacketNum: int
        """
        self._AttackSourceIp = None
        self._AttackRegion = None
        self._AttackFlow = None
        self._AttackPacketNum = None

    @property
    def AttackSourceIp(self):
        """Attack source IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackSourceIp

    @AttackSourceIp.setter
    def AttackSourceIp(self, AttackSourceIp):
        self._AttackSourceIp = AttackSourceIp

    @property
    def AttackRegion(self):
        """Country/Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackRegion

    @AttackRegion.setter
    def AttackRegion(self, AttackRegion):
        self._AttackRegion = AttackRegion

    @property
    def AttackFlow(self):
        """Accumulative attack traffic
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackFlow

    @AttackFlow.setter
    def AttackFlow(self, AttackFlow):
        self._AttackFlow = AttackFlow

    @property
    def AttackPacketNum(self):
        """Accumulative number of attack packets
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackPacketNum

    @AttackPacketNum.setter
    def AttackPacketNum(self, AttackPacketNum):
        self._AttackPacketNum = AttackPacketNum


    def _deserialize(self, params):
        self._AttackSourceIp = params.get("AttackSourceIp")
        self._AttackRegion = params.get("AttackRegion")
        self._AttackFlow = params.get("AttackFlow")
        self._AttackPacketNum = params.get("AttackPacketNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackSourceEventData(AbstractModel):
    """DDoS attack source data

    """

    def __init__(self):
        r"""
        :param _List: DDoS attack source data set
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosAttackSourceEvent
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """DDoS attack source data set
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DDosAttackSourceEvent
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DDosAttackSourceEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosMajorAttackEvent(AbstractModel):
    """Major DDoS attack event

    """

    def __init__(self):
        r"""
        :param _PolicyId: DDoS policy group ID
        :type PolicyId: int
        :param _AttackMaxBandWidth: Maximum attack bandwidth
        :type AttackMaxBandWidth: int
        :param _AttackTime: Attack time in seconds
        :type AttackTime: int
        """
        self._PolicyId = None
        self._AttackMaxBandWidth = None
        self._AttackTime = None

    @property
    def PolicyId(self):
        """DDoS policy group ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttackMaxBandWidth(self):
        """Maximum attack bandwidth
        :rtype: int
        """
        return self._AttackMaxBandWidth

    @AttackMaxBandWidth.setter
    def AttackMaxBandWidth(self, AttackMaxBandWidth):
        self._AttackMaxBandWidth = AttackMaxBandWidth

    @property
    def AttackTime(self):
        """Attack time in seconds
        :rtype: int
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self._AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosMajorAttackEventData(AbstractModel):
    """Major attack object data

    """

    def __init__(self):
        r"""
        :param _List: `DDosMajorAttackEvent` DDoS attack event
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of DDosMajorAttackEvent
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """`DDosMajorAttackEvent` DDoS attack event
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DDosMajorAttackEvent
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DDosMajorAttackEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """Data items in a DNS request curve

    """

    def __init__(self):
        r"""
        :param _Time: Time
        :type Time: str
        :param _Value: Value
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: int
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """Time
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """Value
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosAcls(AbstractModel):
    """DDoS port filtering

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param _Acl: DDoS port filtering parameters
        :type Acl: list of DDoSAcl
        """
        self._Switch = None
        self._Acl = None

    @property
    def Switch(self):
        """Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Acl(self):
        """DDoS port filtering parameters
        :rtype: list of DDoSAcl
        """
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("Acl") is not None:
            self._Acl = []
            for item in params.get("Acl"):
                obj = DDoSAcl()
                obj._deserialize(item)
                self._Acl.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosAllowBlock(AbstractModel):
    """DDoS blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param _UserAllowBlockIp: Array of objects in blocklist/allowlist configuration
        :type UserAllowBlockIp: list of DDoSUserAllowBlockIP
        """
        self._Switch = None
        self._UserAllowBlockIp = None

    @property
    def Switch(self):
        """Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def UserAllowBlockIp(self):
        """Array of objects in blocklist/allowlist configuration
        :rtype: list of DDoSUserAllowBlockIP
        """
        return self._UserAllowBlockIp

    @UserAllowBlockIp.setter
    def UserAllowBlockIp(self, UserAllowBlockIp):
        self._UserAllowBlockIp = UserAllowBlockIp


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("UserAllowBlockIp") is not None:
            self._UserAllowBlockIp = []
            for item in params.get("UserAllowBlockIp"):
                obj = DDoSUserAllowBlockIP()
                obj._deserialize(item)
                self._UserAllowBlockIp.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosPacketFilter(AbstractModel):
    """DDoS feature filtering

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :type Switch: str
        :param _PacketFilter: Array of objects in feature filtering configuration
        :type PacketFilter: list of DDoSFeaturesFilter
        """
        self._Switch = None
        self._PacketFilter = None

    @property
    def Switch(self):
        """Whether to remove all settings when empty strings are passed in. Default value: `off` (remove)
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PacketFilter(self):
        """Array of objects in feature filtering configuration
        :rtype: list of DDoSFeaturesFilter
        """
        return self._PacketFilter

    @PacketFilter.setter
    def PacketFilter(self, PacketFilter):
        self._PacketFilter = PacketFilter


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("PacketFilter") is not None:
            self._PacketFilter = []
            for item in params.get("PacketFilter"):
                obj = DDoSFeaturesFilter()
                obj._deserialize(item)
                self._PacketFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosRule(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param _DdosStatusInfo: DDoS mitigation level
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosStatusInfo: :class:`tencentcloud.teo.v20220106.models.DDoSStatusInfo`
        :param _DdosGeoIp: DDoS regional blocking
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosGeoIp: :class:`tencentcloud.teo.v20220106.models.DDoSGeoIp`
        :param _DdosAllowBlock: DDoS blocklist/allowlist
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAllowBlock: :class:`tencentcloud.teo.v20220106.models.DdosAllowBlock`
        :param _DdosAntiPly: Protocol blocking and null session protection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAntiPly: :class:`tencentcloud.teo.v20220106.models.DDoSAntiPly`
        :param _DdosPacketFilter: DDoS feature filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosPacketFilter: :class:`tencentcloud.teo.v20220106.models.DdosPacketFilter`
        :param _DdosAcl: DDoS port filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosAcl: :class:`tencentcloud.teo.v20220106.models.DdosAcls`
        :param _Switch: DDoS mitigation switch. `on`: Enable; `off`: Disable.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param _UdpShardOpen: Whether to enable UDP fragmentation. `on`: Enable; `off`: Disable.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UdpShardOpen: str
        """
        self._DdosStatusInfo = None
        self._DdosGeoIp = None
        self._DdosAllowBlock = None
        self._DdosAntiPly = None
        self._DdosPacketFilter = None
        self._DdosAcl = None
        self._Switch = None
        self._UdpShardOpen = None

    @property
    def DdosStatusInfo(self):
        """DDoS mitigation level
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDoSStatusInfo`
        """
        return self._DdosStatusInfo

    @DdosStatusInfo.setter
    def DdosStatusInfo(self, DdosStatusInfo):
        self._DdosStatusInfo = DdosStatusInfo

    @property
    def DdosGeoIp(self):
        """DDoS regional blocking
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDoSGeoIp`
        """
        return self._DdosGeoIp

    @DdosGeoIp.setter
    def DdosGeoIp(self, DdosGeoIp):
        self._DdosGeoIp = DdosGeoIp

    @property
    def DdosAllowBlock(self):
        """DDoS blocklist/allowlist
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DdosAllowBlock`
        """
        return self._DdosAllowBlock

    @DdosAllowBlock.setter
    def DdosAllowBlock(self, DdosAllowBlock):
        self._DdosAllowBlock = DdosAllowBlock

    @property
    def DdosAntiPly(self):
        """Protocol blocking and null session protection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDoSAntiPly`
        """
        return self._DdosAntiPly

    @DdosAntiPly.setter
    def DdosAntiPly(self, DdosAntiPly):
        self._DdosAntiPly = DdosAntiPly

    @property
    def DdosPacketFilter(self):
        """DDoS feature filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DdosPacketFilter`
        """
        return self._DdosPacketFilter

    @DdosPacketFilter.setter
    def DdosPacketFilter(self, DdosPacketFilter):
        self._DdosPacketFilter = DdosPacketFilter

    @property
    def DdosAcl(self):
        """DDoS port filtering
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DdosAcls`
        """
        return self._DdosAcl

    @DdosAcl.setter
    def DdosAcl(self, DdosAcl):
        self._DdosAcl = DdosAcl

    @property
    def Switch(self):
        """DDoS mitigation switch. `on`: Enable; `off`: Disable.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def UdpShardOpen(self):
        """Whether to enable UDP fragmentation. `on`: Enable; `off`: Disable.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UdpShardOpen

    @UdpShardOpen.setter
    def UdpShardOpen(self, UdpShardOpen):
        self._UdpShardOpen = UdpShardOpen


    def _deserialize(self, params):
        if params.get("DdosStatusInfo") is not None:
            self._DdosStatusInfo = DDoSStatusInfo()
            self._DdosStatusInfo._deserialize(params.get("DdosStatusInfo"))
        if params.get("DdosGeoIp") is not None:
            self._DdosGeoIp = DDoSGeoIp()
            self._DdosGeoIp._deserialize(params.get("DdosGeoIp"))
        if params.get("DdosAllowBlock") is not None:
            self._DdosAllowBlock = DdosAllowBlock()
            self._DdosAllowBlock._deserialize(params.get("DdosAllowBlock"))
        if params.get("DdosAntiPly") is not None:
            self._DdosAntiPly = DDoSAntiPly()
            self._DdosAntiPly._deserialize(params.get("DdosAntiPly"))
        if params.get("DdosPacketFilter") is not None:
            self._DdosPacketFilter = DdosPacketFilter()
            self._DdosPacketFilter._deserialize(params.get("DdosPacketFilter"))
        if params.get("DdosAcl") is not None:
            self._DdosAcl = DdosAcls()
            self._DdosAcl._deserialize(params.get("DdosAcl"))
        self._Switch = params.get("Switch")
        self._UdpShardOpen = params.get("UdpShardOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param _CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param _Alias: Certificate alias
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param _Type: Certificate type. Valid values:
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param _EffectiveTime: Time when the certificate takes effect
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EffectiveTime: str
        :param _CommonName: Certificate common name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CommonName: str
        :param _SubjectAltName: Domain names added to the SAN certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubjectAltName: list of str
        :param _Status: Certificate status. Valid values:
`applying`: Application in progress
`failed`: Application failed
`processing`: Deploying certificate
`deployed`: Certificate deployed
`disabled`: Certificate disabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param _Message: Returns a message to display failure causes when `Status=failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Message: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._EffectiveTime = None
        self._CommonName = None
        self._SubjectAltName = None
        self._Status = None
        self._Message = None

    @property
    def CertId(self):
        """Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        """Certificate alias
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        """Certificate type. Valid values:
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        """Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EffectiveTime(self):
        """Time when the certificate takes effect
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def CommonName(self):
        """Certificate common name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName

    @property
    def SubjectAltName(self):
        """Domain names added to the SAN certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def Status(self):
        """Certificate status. Valid values:
`applying`: Application in progress
`failed`: Application failed
`processing`: Deploying certificate
`deployed`: Certificate deployed
`disabled`: Certificate disabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """Returns a message to display failure causes when `Status=failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._CommonName = params.get("CommonName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        """
        self._ZoneId = None
        self._ProxyId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Ids: Record ID
        :type Ids: list of str
        """
        self._ZoneId = None
        self._Ids = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Ids(self):
        """Record ID
        :rtype: list of str
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsResponse(AbstractModel):
    """DeleteDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Record ID
        :type Ids: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ids = None
        self._RequestId = None

    @property
    def Ids(self):
        """Record ID
        :rtype: list of str
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        """
        self._ZoneId = None
        self._LoadBalancingId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancingResponse(AbstractModel):
    """DeleteLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancingId = None
        self._RequestId = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._OriginId = None
        self._ZoneId = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOriginGroupResponse(AbstractModel):
    """DeleteOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginId = None
        self._RequestId = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class DescribeApplicationProxyDetailRequest(AbstractModel):
    """DescribeApplicationProxyDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Instance ID
        :type ProxyId: str
        """
        self._ZoneId = None
        self._ProxyId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Instance ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyDetailResponse(AbstractModel):
    """DescribeApplicationProxyDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Instance ID
        :type ProxyId: str
        :param _ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param _PlatType: Proxy mode. Valid values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param _SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param _AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param _ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param _SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param _Rule: List of rules
        :type Rule: list of ApplicationProxyRule
        :param _Status: Status. Valid values:
`online`: Enable
`offline`: Disable
`progress`: Deploying
        :type Status: str
        :param _ScheduleValue: Scheduling information
        :type ScheduleValue: list of str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _SessionPersistTime: Session persistence time
        :type SessionPersistTime: int
        :param _ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        :param _HostId: When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name, such as test.123.com
`HostId` indicates a unique ID of the domain name.
        :type HostId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._ProxyName = None
        self._PlatType = None
        self._SecurityType = None
        self._AccelerateType = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._Rule = None
        self._Status = None
        self._ScheduleValue = None
        self._UpdateTime = None
        self._ZoneId = None
        self._ZoneName = None
        self._SessionPersistTime = None
        self._ProxyType = None
        self._HostId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """Instance ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        """Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def PlatType(self):
        """Proxy mode. Valid values:
`ip`: Anycast IP
`domain`: CNAME
        :rtype: str
        """
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def SecurityType(self):
        """`0`: Disable security protection; `1`: Enable security protection.
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        """`0`: Disable acceleration; `1`: Enable acceleration.
        :rtype: int
        """
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def ForwardClientIp(self):
        """This field is moved to `Rule.ForwardClientIp`.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """This field is moved to `Rule.SessionPersist`.
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def Rule(self):
        """List of rules
        :rtype: list of ApplicationProxyRule
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Status(self):
        """Status. Valid values:
`online`: Enable
`offline`: Disable
`progress`: Deploying
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScheduleValue(self):
        """Scheduling information
        :rtype: list of str
        """
        return self._ScheduleValue

    @ScheduleValue.setter
    def ScheduleValue(self, ScheduleValue):
        self._ScheduleValue = ScheduleValue

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def SessionPersistTime(self):
        """Session persistence time
        :rtype: int
        """
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        """Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :rtype: str
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def HostId(self):
        """When `ProxyType=hostname`:
`ProxyName` indicates a specified domain name, such as test.123.com
`HostId` indicates a unique ID of the domain name.
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._PlatType = params.get("PlatType")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        self._Status = params.get("Status")
        self._ScheduleValue = params.get("ScheduleValue")
        self._UpdateTime = params.get("UpdateTime")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        self._HostId = params.get("HostId")
        self._RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _Limit: Pagination parameter
        :type Limit: int
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyResponse(AbstractModel):
    """DescribeApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of ApplicationProxy
        :param _TotalCount: Total number of records
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Quota: Disused
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quota: int
        :param _IpCount: When `PlatType` is `ip`, it indicates the number of proxies that schedule via Anycast IP.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IpCount: int
        :param _DomainCount: When `PlatType` is `domain`, it indicates the number of proxies that schedule via CNAME.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DomainCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._Quota = None
        self._IpCount = None
        self._DomainCount = None
        self._RequestId = None

    @property
    def Data(self):
        """List of data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of ApplicationProxy
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """Total number of records
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Quota(self):
        """Disused
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def IpCount(self):
        """When `PlatType` is `ip`, it indicates the number of proxies that schedule via Anycast IP.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IpCount

    @IpCount.setter
    def IpCount(self, IpCount):
        self._IpCount = IpCount

    @property
    def DomainCount(self):
        """When `PlatType` is `domain`, it indicates the number of proxies that schedule via CNAME.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Quota = params.get("Quota")
        self._IpCount = params.get("IpCount")
        self._DomainCount = params.get("DomainCount")
        self._RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items per page
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _Domains: Domain name set
        :type Domains: list of str
        :param _QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._ZoneIds = None
        self._Domains = None
        self._QueryCondition = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """Domain name set
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def QueryCondition(self):
        """Query condition
        :rtype: list of QueryCondition
        """
        return self._QueryCondition

    @QueryCondition.setter
    def QueryCondition(self, QueryCondition):
        self._QueryCondition = QueryCondition


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self._QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotLogResponse(AbstractModel):
    """DescribeBotLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Bot attack data
        :type Data: :class:`tencentcloud.teo.v20220106.models.BotLogData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Bot attack data
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotLogData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = BotLogData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeBotManagedRulesRequest(AbstractModel):
    """DescribeBotManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param _Page: Total number of pages
        :type Page: int
        :param _PerPage: Number of rules per page
        :type PerPage: int
        :param _RuleType: Rule type. Values: `idcid`, `sipbot` and `uabot`. All rules will be returned if this field is not specified.
        :type RuleType: str
        """
        self._ZoneId = None
        self._Entity = None
        self._Page = None
        self._PerPage = None
        self._RuleType = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Subdomain name/layer-4 proxy
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Page(self):
        """Total number of pages
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PerPage(self):
        """Number of rules per page
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def RuleType(self):
        """Rule type. Values: `idcid`, `sipbot` and `uabot`. All rules will be returned if this field is not specified.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        self._Page = params.get("Page")
        self._PerPage = params.get("PerPage")
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotManagedRulesResponse(AbstractModel):
    """DescribeBotManagedRules response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of bot managed rules returned
        :type Count: int
        :param _Rules: Bot managed rules
        :type Rules: list of BotManagedRuleDetail
        :param _Total: Total number of bot managed rules
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Rules = None
        self._Total = None
        self._RequestId = None

    @property
    def Count(self):
        """Number of bot managed rules returned
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Rules(self):
        """Bot managed rules
        :rtype: list of BotManagedRuleDetail
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        """Total number of bot managed rules
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = BotManagedRuleDetail()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCnameStatusRequest(AbstractModel):
    """DescribeCnameStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Names: List of domain names
        :type Names: list of str
        """
        self._ZoneId = None
        self._Names = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Names(self):
        """List of domain names
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCnameStatusResponse(AbstractModel):
    """DescribeCnameStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: List of CNAME statuses
        :type Status: list of CnameStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """List of CNAME statuses
        :rtype: list of CnameStatus
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self._Status = []
            for item in params.get("Status"):
                obj = CnameStatus()
                obj._deserialize(item)
                self._Status.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy group ID
        :type PolicyId: int
        :param _ZoneId: Top-level domain name (site)
        :type ZoneId: str
        """
        self._PolicyId = None
        self._ZoneId = None

    @property
    def PolicyId(self):
        """Policy group ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ZoneId(self):
        """Top-level domain name (site)
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDDosAttackDataRequest(AbstractModel):
    """DescribeDDosAttackData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param _ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param _PolicyIds: List of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _Port: Port number
        :type Port: int
        :param _ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param _AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._Port = None
        self._ProtocolType = None
        self._AttackType = None
        self._Interval = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """List of statistical metrics
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        """List of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        """List of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def Port(self):
        """Port number
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: tcp, udp, all
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AttackType(self):
        """Attack type. Valid values: flood, icmpFlood..., all
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._Port = params.get("Port")
        self._ProtocolType = params.get("ProtocolType")
        self._AttackType = params.get("AttackType")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackDataResponse(AbstractModel):
    """DescribeDDosAttackData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DDoS attack data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned data
        :type Msg: str
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS attack data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SecEntry
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned data
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeDDosAttackEventDetailRequest(AbstractModel):
    """DescribeDDosAttackEventDetail request structure.

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID
        :type EventId: str
        """
        self._EventId = None

    @property
    def EventId(self):
        """Event ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventDetailResponse(AbstractModel):
    """DescribeDDosAttackEventDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DDoS attack event details
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventDetailData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS attack event details
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventDetailData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DDosAttackEventDetailData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDDosAttackEventRequest(AbstractModel):
    """DescribeDDosAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        :param _IsShowDetail: Whether to show details. Valid values: Y (yes), N (no).
        :type IsShowDetail: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._PolicyIds = None
        self._ZoneIds = None
        self._ProtocolType = None
        self._IsShowDetail = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PolicyIds(self):
        """Set of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: {tcp,udp,all}
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def IsShowDetail(self):
        """Whether to show details. Valid values: Y (yes), N (no).
        :rtype: str
        """
        return self._IsShowDetail

    @IsShowDetail.setter
    def IsShowDetail(self, IsShowDetail):
        self._IsShowDetail = IsShowDetail


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._PolicyIds = params.get("PolicyIds")
        self._ZoneIds = params.get("ZoneIds")
        self._ProtocolType = params.get("ProtocolType")
        self._IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventResponse(AbstractModel):
    """DescribeDDosAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DDoS attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS attack event data
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DDosAttackEventData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDDosAttackSourceEventRequest(AbstractModel):
    """DescribeDDosAttackSourceEvent request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._PolicyIds = None
        self._ZoneIds = None
        self._ProtocolType = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PolicyIds(self):
        """Set of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: {tcp,udp,all}
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._PolicyIds = params.get("PolicyIds")
        self._ZoneIds = params.get("ZoneIds")
        self._ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackSourceEventResponse(AbstractModel):
    """DescribeDDosAttackSourceEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DDoS attack source data
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackSourceEventData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS attack source data
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDosAttackSourceEventData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DDosAttackSourceEventData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDDosAttackTopDataRequest(AbstractModel):
    """DescribeDDosAttackTopData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricName: Filter metric
        :type MetricName: str
        :param _Limit: Number of the top data entries to query. 0: queries all data entries.
        :type Limit: int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _Port: Port number
        :type Port: int
        :param _ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param _AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Limit = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._Port = None
        self._ProtocolType = None
        self._AttackType = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """Filter metric
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Limit(self):
        """Number of the top data entries to query. 0: queries all data entries.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        """Set of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def Port(self):
        """Port number
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: tcp, udp, all
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AttackType(self):
        """Attack type. Valid values: flood, icmpFlood..., all
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Limit = params.get("Limit")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._Port = params.get("Port")
        self._ProtocolType = params.get("ProtocolType")
        self._AttackType = params.get("AttackType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackTopDataResponse(AbstractModel):
    """DescribeDDosAttackTopData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Top N data
        :type Data: list of TopNEntry
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Top N data
        :rtype: list of TopNEntry
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDDosMajorAttackEventRequest(AbstractModel):
    """DescribeDDosMajorAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _ProtocolType: Protocol type. Valid values: {tcp,udp,all}
        :type ProtocolType: str
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._PolicyIds = None
        self._ProtocolType = None
        self._ZoneIds = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PolicyIds(self):
        """Set of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: {tcp,udp,all}
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._PolicyIds = params.get("PolicyIds")
        self._ProtocolType = params.get("ProtocolType")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosMajorAttackEventResponse(AbstractModel):
    """DescribeDDosMajorAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Major DDoS attack event
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosMajorAttackEventData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Major DDoS attack event
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDosMajorAttackEventData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DDosMajorAttackEventData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of certificates
        :type TotalCount: int
        :param _CertInfo: List of default certificates
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of DefaultServerCertInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CertInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of certificates
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CertInfo(self):
        """List of default certificates
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of DefaultServerCertInfo
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CertInfo") is not None:
            self._CertInfo = []
            for item in params.get("CertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self._CertInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Filters: Filter parameters
        :type Filters: list of DnsDataFilter
        :param _Interval: Time granularity. The default value is `min`. The server can adapt to the time granularity specified.
Valid values:
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Interval = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """Filter parameters
        :rtype: list of DnsDataFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        """Time granularity. The default value is `min`. The server can adapt to the time granularity specified.
Valid values:
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DnsDataFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsDataResponse(AbstractModel):
    """DescribeDnsData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DNS request data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of DataItem
        :param _Interval: Interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """DNS request data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of DataItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        """Interval
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query filter
        :type Filters: list of DnsRecordFilter
        :param _Order: Sorts the order
        :type Order: str
        :param _Direction: Valid values: `asc`, and `desc`.
        :type Direction: str
        :param _Match: Valid values: `all`, and `any`.
        :type Match: str
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._Filters = None
        self._Order = None
        self._Direction = None
        self._Match = None
        self._Limit = None
        self._Offset = None
        self._ZoneId = None

    @property
    def Filters(self):
        """Query filter
        :rtype: list of DnsRecordFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        """Sorts the order
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Direction(self):
        """Valid values: `asc`, and `desc`.
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Match(self):
        """Valid values: `all`, and `any`.
        :rtype: str
        """
        return self._Match

    @Match.setter
    def Match(self, Match):
        self._Match = Match

    @property
    def Limit(self):
        """Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset for paginated queries. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DnsRecordFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Direction = params.get("Direction")
        self._Match = params.get("Match")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsRecordsResponse(AbstractModel):
    """DescribeDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param _Records: List of DNS records
        :type Records: list of DnsRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Records = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Used for paginated query by total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Records(self):
        """List of DNS records
        :rtype: list of DnsRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = DnsRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnssecResponse(AbstractModel):
    """DescribeDnssec response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _Status: DNSSEC status. Valid values:
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param _Dnssec: 
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._Dnssec = None
        self._ModifiedOn = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """DNSSEC status. Valid values:
- `enabled`: Enabled
- `disabled`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Dnssec(self):
        """
        :rtype: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        """
        return self._Dnssec

    @Dnssec.setter
    def Dnssec(self, Dnssec):
        self._Dnssec = Dnssec

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self._Dnssec = DnssecInfo()
            self._Dnssec._deserialize(params.get("Dnssec"))
        self._ModifiedOn = params.get("ModifiedOn")
        self._RequestId = params.get("RequestId")


class DescribeHostsCertificateRequest(AbstractModel):
    """DescribeHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Query filter
        :type Filters: list of CertFilter
        :param _Sort: Sorting order
        :type Sort: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sort = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        """Offset for paginated queries. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Query filter
        :rtype: list of CertFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        """Sorting order
        :rtype: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CertFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = CertSort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsCertificateResponse(AbstractModel):
    """DescribeHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param _Hosts: List of certificate configurations for domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hosts: list of HostCertSetting
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Hosts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Used for paginated query by total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Hosts(self):
        """List of certificate configurations for domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of HostCertSetting
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self._Hosts = []
            for item in params.get("Hosts"):
                obj = HostCertSetting()
                obj._deserialize(item)
                self._Hosts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Hosts: Specifies a domain name for the query
        :type Hosts: list of str
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Hosts = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        """Offset for paginated queries. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Hosts(self):
        """Specifies a domain name for the query
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Hosts = params.get("Hosts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting response structure.

    """

    def __init__(self):
        r"""
        :param _Hosts: List of domain names
        :type Hosts: list of DetailHost
        :param _TotalNumber: Number of domain names
        :type TotalNumber: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Hosts = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def Hosts(self):
        """List of domain names
        :rtype: list of DetailHost
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def TotalNumber(self):
        """Number of domain names
        :rtype: int
        """
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Hosts") is not None:
            self._Hosts = []
            for item in params.get("Hosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self._Hosts.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeIdentificationRequest(AbstractModel):
    """DescribeIdentification request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationResponse(AbstractModel):
    """DescribeIdentification response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _Status: Verification status. Valid values:
- `pending`: Verifying
- `finished`: The site is verified.
        :type Status: str
        :param _Subdomain: 
        :type Subdomain: str
        :param _RecordType: Record type
        :type RecordType: str
        :param _RecordValue: Record value
        :type RecordValue: str
        :param _OriginalNameServers: NS records of the domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Status = None
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None
        self._OriginalNameServers = None
        self._RequestId = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """Verification status. Valid values:
- `pending`: Verifying
- `finished`: The site is verified.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Subdomain(self):
        """
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        """Record type
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        """Record value
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def OriginalNameServers(self):
        """NS records of the domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancingDetailRequest(AbstractModel):
    """DescribeLoadBalancingDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        """
        self._ZoneId = None
        self._LoadBalancingId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingDetailResponse(AbstractModel):
    """DescribeLoadBalancingDetail response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param _Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param _TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param _OriginId: ID of the origin group used
        :type OriginId: list of str
        :param _Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Status: Status of the task
        :type Status: str
        :param _Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancingId = None
        self._ZoneId = None
        self._Host = None
        self._Type = None
        self._TTL = None
        self._OriginId = None
        self._Origin = None
        self._UpdateTime = None
        self._Status = None
        self._Cname = None
        self._RequestId = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Host(self):
        """Subdomain name. You can use @ to represent the root domain.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Type(self):
        """Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TTL(self):
        """Indicates DNS TTL time when `Type=dns_only`
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def OriginId(self):
        """ID of the origin group used
        :rtype: list of str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Origin(self):
        """Information of the origin server used
        :rtype: list of OriginGroup
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Status of the task
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        """Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._ZoneId = params.get("ZoneId")
        self._Host = params.get("Host")
        self._Type = params.get("Type")
        self._TTL = params.get("TTL")
        self._OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self._Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self._Origin.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Host: Ignore query string parameter
        :type Host: str
        :param _Fuzzy: Specifies whether the `Host` parameter supports fuzzy match
        :type Fuzzy: bool
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Host = None
        self._Fuzzy = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Host(self):
        """Ignore query string parameter
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Fuzzy(self):
        """Specifies whether the `Host` parameter supports fuzzy match
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Host = params.get("Host")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingResponse(AbstractModel):
    """DescribeLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _Data: CLB information
        :type Data: list of LoadBalancing
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """CLB information
        :rtype: list of LoadBalancing
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LoadBalancing()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginGroupDetailRequest(AbstractModel):
    """DescribeOriginGroupDetail request structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._OriginId = None
        self._ZoneId = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupDetailResponse(AbstractModel):
    """DescribeOriginGroupDetail response structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _OriginName: Origin group name
        :type OriginName: str
        :param _Type: Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in OriginRecord.
`weight`: Origin-pull by the weight specified by `Weight` in OriginRecord.
        :type Type: str
        :param _Record: Record
        :type Record: list of OriginRecord
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _OriginType: Origin type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginType: str
        :param _ApplicationProxyUsed: Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationProxyUsed: bool
        :param _LoadBalancingUsed: Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsed: bool
        :param _LoadBalancingUsedType: Proxy mode of the load balancing task associated with the origin group.
`none`: Not used for load balancing.
`dns_only`: Used for DNS-only load balancing.
`proxied`: Used for proxied load balancing.
`both`: Used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsedType: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginId = None
        self._OriginName = None
        self._Type = None
        self._Record = None
        self._UpdateTime = None
        self._ZoneId = None
        self._ZoneName = None
        self._OriginType = None
        self._ApplicationProxyUsed = None
        self._LoadBalancingUsed = None
        self._LoadBalancingUsedType = None
        self._RequestId = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def OriginName(self):
        """Origin group name
        :rtype: str
        """
        return self._OriginName

    @OriginName.setter
    def OriginName(self, OriginName):
        self._OriginName = OriginName

    @property
    def Type(self):
        """Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in OriginRecord.
`weight`: Origin-pull by the weight specified by `Weight` in OriginRecord.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Record(self):
        """Record
        :rtype: list of OriginRecord
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def OriginType(self):
        """Origin type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ApplicationProxyUsed(self):
        """Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ApplicationProxyUsed

    @ApplicationProxyUsed.setter
    def ApplicationProxyUsed(self, ApplicationProxyUsed):
        self._ApplicationProxyUsed = ApplicationProxyUsed

    @property
    def LoadBalancingUsed(self):
        """Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._LoadBalancingUsed

    @LoadBalancingUsed.setter
    def LoadBalancingUsed(self, LoadBalancingUsed):
        self._LoadBalancingUsed = LoadBalancingUsed

    @property
    def LoadBalancingUsedType(self):
        """Proxy mode of the load balancing task associated with the origin group.
`none`: Not used for load balancing.
`dns_only`: Used for DNS-only load balancing.
`proxied`: Used for proxied load balancing.
`both`: Used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancingUsedType

    @LoadBalancingUsedType.setter
    def LoadBalancingUsedType(self, LoadBalancingUsedType):
        self._LoadBalancingUsedType = LoadBalancingUsedType

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._OriginName = params.get("OriginName")
        self._Type = params.get("Type")
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Record.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._OriginType = params.get("OriginType")
        self._ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self._LoadBalancingUsed = params.get("LoadBalancingUsed")
        self._LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        self._RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Filters: Filter parameters
        :type Filters: list of OriginFilter
        :param _ZoneId: Site ID
If it’s not specified, all origin groups will be obtained.
        :type ZoneId: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ZoneId = None

    @property
    def Offset(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter parameters
        :rtype: list of OriginFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ZoneId(self):
        """Site ID
If it’s not specified, all origin groups will be obtained.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = OriginFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupResponse(AbstractModel):
    """DescribeOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Origin group information
        :type Data: list of OriginGroup
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """Origin group information
        :rtype: list of OriginGroup
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OriginGroup()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param _EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param _MetricNames: Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :type MetricNames: list of str
        :param _Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param _ZoneIds: List of `ZoneId` values. This parameter takes effect only when querying in the zone/domain dimension.
        :type ZoneIds: list of str
        :param _Domains: List of `Domain` values. This parameter takes effect only when querying in the domain dimension.
        :type Domains: list of str
        :param _Protocol: Protocol type. Valid values: {http,http2,https,all}
        :type Protocol: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Interval = None
        self._ZoneIds = None
        self._Domains = None
        self._Protocol = None

    @property
    def StartTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Interval(self):
        """Time interval. Valid values: {min, 5min, hour, day, week}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ZoneIds(self):
        """List of `ZoneId` values. This parameter takes effect only when querying in the zone/domain dimension.
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """List of `Domain` values. This parameter takes effect only when querying in the domain dimension.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Protocol(self):
        """Protocol type. Valid values: {http,http2,https,all}
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Interval = params.get("Interval")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data response structure.

    """

    def __init__(self):
        r"""
        :param _Type: Query dimension
        :type Type: str
        :param _Interval: Time interval
        :type Interval: str
        :param _Data: Detailed data
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Type = None
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Type(self):
        """Query dimension
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        """Time interval
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """Detailed data
        :rtype: list of TimingDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _StartTime: Start time of the query
        :type StartTime: str
        :param _EndTime: End time of the query
        :type EndTime: str
        :param _Offset: Offset of the query
        :type Offset: int
        :param _Limit: Maximum number of results returned
        :type Limit: int
        :param _Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Domains: List of domain names queried
        :type Domains: list of str
        :param _Target: Resources queried
        :type Target: str
        """
        self._JobId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Statuses = None
        self._ZoneId = None
        self._Domains = None
        self._Target = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StartTime(self):
        """Start time of the query
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the query
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Offset of the query
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of results returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Statuses(self):
        """Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domains(self):
        """List of domain names queried
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Target(self):
        """Resources queried
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Statuses = params.get("Statuses")
        self._ZoneId = params.get("ZoneId")
        self._Domains = params.get("Domains")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param _Tasks: List of tasks returned
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total entries that match the specified query condition
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """List of tasks returned
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _Type: Type of the purging task
        :type Type: str
        :param _StartTime: Start time of the query
        :type StartTime: str
        :param _EndTime: End time of the query
        :type EndTime: str
        :param _Offset: Offset of the query
        :type Offset: int
        :param _Limit: Maximum number of results returned
        :type Limit: int
        :param _Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Domains: List of domain names queried
        :type Domains: list of str
        :param _Target: Queries content
        :type Target: str
        """
        self._JobId = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Statuses = None
        self._ZoneId = None
        self._Domains = None
        self._Target = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Type(self):
        """Type of the purging task
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        """Start time of the query
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the query
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Offset of the query
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of results returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Statuses(self):
        """Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domains(self):
        """List of domain names queried
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Target(self):
        """Queries content
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Statuses = params.get("Statuses")
        self._ZoneId = params.get("ZoneId")
        self._Domains = params.get("Domains")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param _Tasks: List of tasks returned
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total entries that match the specified query condition
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """List of tasks returned
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyListRequest(AbstractModel):
    """DescribeSecurityPolicyList request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyListResponse(AbstractModel):
    """DescribeSecurityPolicyList response structure.

    """

    def __init__(self):
        r"""
        :param _Entities: List of protected resources
        :type Entities: list of SecurityEntity
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Entities = None
        self._RequestId = None

    @property
    def Entities(self):
        """List of protected resources
        :rtype: list of SecurityEntity
        """
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Entities") is not None:
            self._Entities = []
            for item in params.get("Entities"):
                obj = SecurityEntity()
                obj._deserialize(item)
                self._Entities.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesIdRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: List of rule IDs
        :type RuleId: list of int
        """
        self._RuleId = None

    @property
    def RuleId(self):
        """List of rule IDs
        :rtype: list of int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesIdResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of returned items
        :type Total: int
        :param _Rules: Managed rule
        :type Rules: list of ManagedRule
        :param _Count: Total number of returned items
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Rules = None
        self._Count = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of returned items
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Rules(self):
        """Managed rule
        :rtype: list of ManagedRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Count(self):
        """Total number of returned items
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param _Page: Total number of pages
        :type Page: int
        :param _PerPage: Number of rules per page
        :type PerPage: int
        """
        self._ZoneId = None
        self._Entity = None
        self._Page = None
        self._PerPage = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Subdomain name/layer-4 proxy
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Page(self):
        """Total number of pages
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PerPage(self):
        """Number of rules per page
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        self._Page = params.get("Page")
        self._PerPage = params.get("PerPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRules response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of rules returned
        :type Count: int
        :param _Rules: Managed rule
        :type Rules: list of ManagedRule
        :param _Total: Total number of rules
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Rules = None
        self._Total = None
        self._RequestId = None

    @property
    def Count(self):
        """Number of rules returned
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Rules(self):
        """Managed rule
        :rtype: list of ManagedRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        """Total number of rules
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyRegionsRequest(AbstractModel):
    """DescribeSecurityPolicyRegions request structure.

    """


class DescribeSecurityPolicyRegionsResponse(AbstractModel):
    """DescribeSecurityPolicyRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number of regions
        :type Count: int
        :param _GeoIp: Region information
        :type GeoIp: list of GeoIp
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._GeoIp = None
        self._RequestId = None

    @property
    def Count(self):
        """Total number of regions
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def GeoIp(self):
        """Region information
        :rtype: list of GeoIp
        """
        return self._GeoIp

    @GeoIp.setter
    def GeoIp(self, GeoIp):
        self._GeoIp = GeoIp

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("GeoIp") is not None:
            self._GeoIp = []
            for item in params.get("GeoIp"):
                obj = GeoIp()
                obj._deserialize(item)
                self._GeoIp.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyRequest(AbstractModel):
    """DescribeSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Second-level domain name
        :type Entity: str
        """
        self._ZoneId = None
        self._Entity = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Second-level domain name
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyResponse(AbstractModel):
    """DescribeSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AppId: User ID
        :type AppId: int
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Second-level domain name
        :type Entity: str
        :param _Config: Security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppId = None
        self._ZoneId = None
        self._Entity = None
        self._Config = None
        self._RequestId = None

    @property
    def AppId(self):
        """User ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Second-level domain name
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Config(self):
        """Security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        if params.get("Config") is not None:
            self._Config = SecurityConfig()
            self._Config._deserialize(params.get("Config"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityPortraitRulesRequest(AbstractModel):
    """DescribeSecurityPortraitRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Subdomain name/Application name
        :type Entity: str
        """
        self._ZoneId = None
        self._Entity = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Subdomain name/Application name
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPortraitRulesResponse(AbstractModel):
    """DescribeSecurityPortraitRules response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of rules returned in this request
        :type Count: int
        :param _Rules: Bot user profiling rule
        :type Rules: list of PortraitManagedRuleDetail
        :param _Total: Total number of rules
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Rules = None
        self._Total = None
        self._RequestId = None

    @property
    def Count(self):
        """Number of rules returned in this request
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Rules(self):
        """Bot user profiling rule
        :rtype: list of PortraitManagedRuleDetail
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        """Total number of rules
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PortraitManagedRuleDetail()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param _EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param _MetricNames: Supported metrics for data query:
`l4Flow_connections`: Access connections
`l4Flow_flux`: Access traffic
`l4Flow_inFlux`: Inbound traffic
`l4Flow_outFlux`: Outbound traffic
        :type MetricNames: list of str
        :param _ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param _InstanceIds: This field has been disused. Use `ProxyIds` instead.
        :type InstanceIds: list of str
        :param _Protocol: This field is not supported currently.
        :type Protocol: str
        :param _Interval: Time interval. Valid values: {min, 5min, hour, day}
        :type Interval: str
        :param _RuleId: This field is not supported currently. Use `Filter` instead.
        :type RuleId: str
        :param _Filters: Supported filters: `proxyd`, `ruleId`
        :type Filters: list of Filter
        :param _ProxyIds: List of layer-4 proxies
        :type ProxyIds: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._InstanceIds = None
        self._Protocol = None
        self._Interval = None
        self._RuleId = None
        self._Filters = None
        self._ProxyIds = None

    @property
    def StartTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """Supported metrics for data query:
`l4Flow_connections`: Access connections
`l4Flow_flux`: Access traffic
`l4Flow_inFlux`: Inbound traffic
`l4Flow_outFlux`: Outbound traffic
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        """List of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceIds(self):
        """This field has been disused. Use `ProxyIds` instead.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Protocol(self):
        """This field is not supported currently.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Interval(self):
        """Time interval. Valid values: {min, 5min, hour, day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RuleId(self):
        """This field is not supported currently. Use `Filter` instead.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Filters(self):
        """Supported filters: `proxyd`, `ruleId`
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProxyIds(self):
        """List of layer-4 proxies
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceIds = params.get("InstanceIds")
        self._Protocol = params.get("Protocol")
        self._Interval = params.get("Interval")
        self._RuleId = params.get("RuleId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data response structure.

    """

    def __init__(self):
        r"""
        :param _Type: Query dimension
        :type Type: str
        :param _Interval: Time interval
        :type Interval: str
        :param _Data: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Type = None
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Type(self):
        """Query dimension
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        """Time interval
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param _EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param _MetricNames: Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :type MetricNames: list of str
        :param _Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param _ZoneIds: Array of `ZoneId` values
        :type ZoneIds: list of str
        :param _Filters: Filter
        :type Filters: list of Filter
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Interval = None
        self._ZoneIds = None
        self._Filters = None

    @property
    def StartTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """Supported metrics for data query:
`l7Flow_outFlux`: Access traffic
`l7Flow_request`: Access requests
`l7Flow_outBandwidth`: Access bandwidth
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Interval(self):
        """Time interval. Valid values: {min, 5min, hour, day, week}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ZoneIds(self):
        """Array of `ZoneId` values
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        """Filter
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Interval = params.get("Interval")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _Type: Query dimension
        :type Type: str
        :param _Interval: Time interval
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Type = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """Query dimension
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        """Time interval
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query (client time in RFC 3339)
        :type StartTime: str
        :param _EndTime: Start time of the query (client time in RFC 3339)
        :type EndTime: str
        :param _MetricNames: Supported metrics for data query:
`l7Cache_outFlux`: Access traffic
`l7Cache_request`: Access requests
        :type MetricNames: list of str
        :param _Interval: Time interval. Values: {min, 5min, hour, day, week}
        :type Interval: str
        :param _ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param _Filters: Filter condition:
{Key: "cacheType", Value: ["hit"], Operator: "equals"}: Filter by data responded from EdgeOne
{Key: "cacheType", Value: ["miss", "dynamic"], Operator: "equals"}: Filter by data responded from the origin server
        :type Filters: list of Filter
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Interval = None
        self._ZoneIds = None
        self._Filters = None

    @property
    def StartTime(self):
        """Start time of the query (client time in RFC 3339)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Start time of the query (client time in RFC 3339)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """Supported metrics for data query:
`l7Cache_outFlux`: Access traffic
`l7Cache_request`: Access requests
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Interval(self):
        """Time interval. Values: {min, 5min, hour, day, week}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ZoneIds(self):
        """List of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        """Filter condition:
{Key: "cacheType", Value: ["hit"], Operator: "equals"}: Filter by data responded from EdgeOne
{Key: "cacheType", Value: ["miss", "dynamic"], Operator: "equals"}: Filter by data responded from the origin server
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Interval = params.get("Interval")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _Type: Metric specified for data query
        :type Type: str
        :param _Interval: Time interval
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Type = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """Details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """Metric specified for data query
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        """Time interval
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Client time in RFC 3339 format
        :type StartTime: str
        :param _EndTime: Client time in RFC 3339 format
        :type EndTime: str
        :param _MetricName: Time series-type access traffic metric
        :type MetricName: str
        :param _Limit: Top N. 0 indicates to return the full data.
        :type Limit: int
        :param _Interval: Time interval. Valid values: {min, 5min, hour, day, week}
        :type Interval: str
        :param _ZoneIds: Array of `ZoneId` values
        :type ZoneIds: list of str
        :param _Filters: Filter
        :type Filters: list of Filter
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Limit = None
        self._Interval = None
        self._ZoneIds = None
        self._Filters = None

    @property
    def StartTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Client time in RFC 3339 format
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """Time series-type access traffic metric
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Limit(self):
        """Top N. 0 indicates to return the full data.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Interval(self):
        """Time interval. Valid values: {min, 5min, hour, day, week}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ZoneIds(self):
        """Array of `ZoneId` values
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        """Filter
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Limit = params.get("Limit")
        self._Interval = params.get("Interval")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Top detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param _Type: Query dimension
        :type Type: str
        :param _MetricName: Query metric
        :type MetricName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Type = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Data(self):
        """Top detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TopDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """Query dimension
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MetricName(self):
        """Query metric
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query (client time in RFC 3339)
        :type StartTime: str
        :param _EndTime: End time of the query (client time in RFC 3339)
        :type EndTime: str
        :param _MetricName: Metric for time-series data query
        :type MetricName: str
        :param _Limit: Specifies the number of data records to return. If `0` is passed in, all data is returned.
        :type Limit: int
        :param _Interval: Time interval. Values: {min, 5min, hour, day, week}. This field is optional.
        :type Interval: str
        :param _ZoneIds: Array of site IDs
        :type ZoneIds: list of str
        :param _Filters: Filter condition
        :type Filters: list of Filter
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Limit = None
        self._Interval = None
        self._ZoneIds = None
        self._Filters = None

    @property
    def StartTime(self):
        """Start time of the query (client time in RFC 3339)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the query (client time in RFC 3339)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """Metric for time-series data query
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Limit(self):
        """Specifies the number of data records to return. If `0` is passed in, all data is returned.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Interval(self):
        """Time interval. Values: {min, 5min, hour, day, week}. This field is optional.
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ZoneIds(self):
        """Array of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        """Filter condition
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Limit = params.get("Limit")
        self._Interval = params.get("Interval")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Top-ranked data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param _Type: Dimension specified for data query
        :type Type: str
        :param _MetricName: Metric specified for data query
        :type MetricName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Type = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Data(self):
        """Top-ranked data details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TopDataRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """Dimension specified for data query
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MetricName(self):
        """Metric specified for data query
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeWebManagedRulesAttackEventsRequest(AbstractModel):
    """DescribeWebManagedRulesAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _PolicyIds: List of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _Domains: List of subdomain names
        :type Domains: list of str
        :param _IsShowDetail: Whether to show details. Valid values: Y (yes), N (no).
        :type IsShowDetail: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._PolicyIds = None
        self._ZoneIds = None
        self._Domains = None
        self._IsShowDetail = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PolicyIds(self):
        """List of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """List of subdomain names
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def IsShowDetail(self):
        """Whether to show details. Valid values: Y (yes), N (no).
        :rtype: str
        """
        return self._IsShowDetail

    @IsShowDetail.setter
    def IsShowDetail(self, IsShowDetail):
        self._IsShowDetail = IsShowDetail


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._PolicyIds = params.get("PolicyIds")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesAttackEventsResponse(AbstractModel):
    """DescribeWebManagedRulesAttackEvents response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Web attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebEventData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned data
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Web attack event data
        :rtype: :class:`tencentcloud.teo.v20220106.models.WebEventData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned data
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WebEventData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param _ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param _Domains: List of subdomain names
        :type Domains: list of str
        :param _ProtocolType: Protocol type
        :type ProtocolType: str
        :param _AttackType: "webshell" : WebShell detection prevention
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
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Domains = None
        self._ProtocolType = None
        self._AttackType = None
        self._Interval = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """List of statistical metrics
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        """List of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """List of subdomain names
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ProtocolType(self):
        """Protocol type
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AttackType(self):
        """"webshell" : WebShell detection prevention
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
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._ProtocolType = params.get("ProtocolType")
        self._AttackType = params.get("AttackType")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesDataResponse(AbstractModel):
    """DescribeWebManagedRulesData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Web attack log entity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """Web attack log entity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SecEntry
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items per page
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _Domains: Domain name set
        :type Domains: list of str
        :param _QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._ZoneIds = None
        self._Domains = None
        self._QueryCondition = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """Domain name set
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def QueryCondition(self):
        """Query condition
        :rtype: list of QueryCondition
        """
        return self._QueryCondition

    @QueryCondition.setter
    def QueryCondition(self, QueryCondition):
        self._QueryCondition = QueryCondition


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self._QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesLogResponse(AbstractModel):
    """DescribeWebManagedRulesLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Web attack log data
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebLogData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Web attack log data
        :rtype: :class:`tencentcloud.teo.v20220106.models.WebLogData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WebLogData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeWebManagedRulesTopDataRequest(AbstractModel):
    """DescribeWebManagedRulesTopData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricName: Filter metric
        :type MetricName: str
        :param _Limit: Number of the top data entries to query. 0: queries all data entries.
        :type Limit: int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _PolicyIds: Set of DDoS policy group IDs
        :type PolicyIds: list of int
        :param _Port: Port number
        :type Port: int
        :param _ProtocolType: Protocol type. Valid values: tcp, udp, all
        :type ProtocolType: str
        :param _AttackType: Attack type. Valid values: flood, icmpFlood..., all
        :type AttackType: str
        :param _Domains: Domain name set
        :type Domains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Limit = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._Port = None
        self._ProtocolType = None
        self._AttackType = None
        self._Domains = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """Filter metric
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Limit(self):
        """Number of the top data entries to query. 0: queries all data entries.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        """Set of DDoS policy group IDs
        :rtype: list of int
        """
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def Port(self):
        """Port number
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProtocolType(self):
        """Protocol type. Valid values: tcp, udp, all
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AttackType(self):
        """Attack type. Valid values: flood, icmpFlood..., all
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Domains(self):
        """Domain name set
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Limit = params.get("Limit")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._Port = params.get("Port")
        self._ProtocolType = params.get("ProtocolType")
        self._AttackType = params.get("AttackType")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesTopDataResponse(AbstractModel):
    """DescribeWebManagedRulesTopData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Top N data
        :type Data: list of TopNEntry
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Top N data
        :rtype: list of TopNEntry
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeWebProtectionAttackEventsRequest(AbstractModel):
    """DescribeWebProtectionAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _Domains: Domain name
        :type Domains: list of str
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._Domains = None
        self._ZoneIds = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Domains(self):
        """Domain name
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Domains = params.get("Domains")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionAttackEventsResponse(AbstractModel):
    """DescribeWebProtectionAttackEvents response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DDoS attack event data
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCInterceptEventData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS attack event data
        :rtype: :class:`tencentcloud.teo.v20220106.models.CCInterceptEventData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CCInterceptEventData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricNames: List of statistical metrics
        :type MetricNames: list of str
        :param _ZoneIds: List of site IDs
        :type ZoneIds: list of str
        :param _Domains: List of subdomain names
        :type Domains: list of str
        :param _ProtocolType: Protocol type
        :type ProtocolType: str
        :param _AttackType: "webshell" : WebShell detection prevention
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
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Domains = None
        self._ProtocolType = None
        self._AttackType = None
        self._Interval = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """List of statistical metrics
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        """List of site IDs
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """List of subdomain names
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ProtocolType(self):
        """Protocol type
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AttackType(self):
        """"webshell" : WebShell detection prevention
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
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._ProtocolType = params.get("ProtocolType")
        self._AttackType = params.get("AttackType")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionDataResponse(AbstractModel):
    """DescribeWebProtectionData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Message
        :type Msg: str
        :param _Interval: Query time granularity. Valid values: {min,5min,hour,day}
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """Data details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SecEntry
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Interval(self):
        """Query time granularity. Valid values: {min,5min,hour,day}
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeWebProtectionLogRequest(AbstractModel):
    """DescribeWebProtectionLog request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _PageSize: Number of items per page
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _ZoneIds: Site set
        :type ZoneIds: list of str
        :param _Domains: Domain name set
        :type Domains: list of str
        :param _QueryCondition: Query condition
        :type QueryCondition: list of QueryCondition
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._ZoneIds = None
        self._Domains = None
        self._QueryCondition = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of items per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def ZoneIds(self):
        """Site set
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        """Domain name set
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def QueryCondition(self):
        """Query condition
        :rtype: list of QueryCondition
        """
        return self._QueryCondition

    @QueryCondition.setter
    def QueryCondition(self, QueryCondition):
        self._QueryCondition = QueryCondition


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self._QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionLogResponse(AbstractModel):
    """DescribeWebProtectionLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Block data in rate-limiting policy
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCLogData`
        :param _Status: Status. 1: failed; 0: succeeded
        :type Status: int
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._Msg = None
        self._RequestId = None

    @property
    def Data(self):
        """Block data in rate-limiting policy
        :rtype: :class:`tencentcloud.teo.v20220106.models.CCLogData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """Status. 1: failed; 0: succeeded
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Msg(self):
        """Returned message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CCLogData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeZoneDDoSPolicyRequest(AbstractModel):
    """DescribeZoneDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site (top-level domain name)
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        """ID of the site (top-level domain name)
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDDoSPolicyResponse(AbstractModel):
    """DescribeZoneDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AppId: User APPID
        :type AppId: int
        :param _ShieldAreas: DDoS mitigation configuration
        :type ShieldAreas: list of ShieldArea
        :param _Domains: Includes the details of all subdomain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domains: list of DDoSApplication
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppId = None
        self._ShieldAreas = None
        self._Domains = None
        self._RequestId = None

    @property
    def AppId(self):
        """User APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ShieldAreas(self):
        """DDoS mitigation configuration
        :rtype: list of ShieldArea
        """
        return self._ShieldAreas

    @ShieldAreas.setter
    def ShieldAreas(self, ShieldAreas):
        self._ShieldAreas = ShieldAreas

    @property
    def Domains(self):
        """Includes the details of all subdomain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of DDoSApplication
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("ShieldAreas") is not None:
            self._ShieldAreas = []
            for item in params.get("ShieldAreas"):
                obj = ShieldArea()
                obj._deserialize(item)
                self._ShieldAreas.append(obj)
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneDetailsRequest(AbstractModel):
    """DescribeZoneDetails request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDetailsResponse(AbstractModel):
    """DescribeZoneDetails response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _OriginalNameServers: List of name servers used
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param _NameServers: List of name servers assigned to users by Tencent Cloud
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NameServers: list of str
        :param _Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param _Type: Specifies how the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param _Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param _CnameSpeedUp: Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
        :type CnameSpeedUp: str
        :param _CnameStatus: Ownership verification status of the site when it accesses via CNAME.
- `finished`: The site is verified.
- `pending`: The site is waiting for verification.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param _Tags: Resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Area: 
        :type Area: str
        :param _Resources: Billable resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resources: list of Resource
        :param _ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param _CreatedOn: Site creation date
        :type CreatedOn: str
        :param _VanityNameServers: User-defined name server information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param _VanityNameServersIps: User-defined name server IP information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._OriginalNameServers = None
        self._NameServers = None
        self._Status = None
        self._Type = None
        self._Paused = None
        self._CnameSpeedUp = None
        self._CnameStatus = None
        self._Tags = None
        self._Area = None
        self._Resources = None
        self._ModifiedOn = None
        self._CreatedOn = None
        self._VanityNameServers = None
        self._VanityNameServersIps = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginalNameServers(self):
        """List of name servers used
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def NameServers(self):
        """List of name servers assigned to users by Tencent Cloud
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def Status(self):
        """Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """Specifies how the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Paused(self):
        """Indicates whether the site is disabled
        :rtype: bool
        """
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def CnameSpeedUp(self):
        """Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
        :rtype: str
        """
        return self._CnameSpeedUp

    @CnameSpeedUp.setter
    def CnameSpeedUp(self, CnameSpeedUp):
        self._CnameSpeedUp = CnameSpeedUp

    @property
    def CnameStatus(self):
        """Ownership verification status of the site when it accesses via CNAME.
- `finished`: The site is verified.
- `pending`: The site is waiting for verification.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def Tags(self):
        """Resource tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Area(self):
        """
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Resources(self):
        """Billable resource
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Resource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ModifiedOn(self):
        """Site modification date
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def CreatedOn(self):
        """Site creation date
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def VanityNameServers(self):
        """User-defined name server information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers

    @property
    def VanityNameServersIps(self):
        """User-defined name server IP information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of VanityNameServersIps
        """
        return self._VanityNameServersIps

    @VanityNameServersIps.setter
    def VanityNameServersIps(self, VanityNameServersIps):
        self._VanityNameServersIps = VanityNameServersIps

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._NameServers = params.get("NameServers")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Paused = params.get("Paused")
        self._CnameSpeedUp = params.get("CnameSpeedUp")
        self._CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Area = params.get("Area")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._ModifiedOn = params.get("ModifiedOn")
        self._CreatedOn = params.get("CreatedOn")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self._VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self._VanityNameServersIps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param _Cache: Cache expiration time configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param _CacheKey: Node cache key configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param _MaxAge: Browser cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param _OfflineCache: Offline cache
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param _Quic: QUIC access
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param _PostMaxSize: POST transport configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param _Compression: Smart compression configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param _UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param _ForceRedirect: Force HTTPS redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param _Https: HTTPS acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param _Origin: Origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param _SmartRouting: Dynamic acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Zone: Domain name of the site
        :type Zone: str
        :param _WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param _ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param _CachePrefresh: Cache prefresh configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Cache = None
        self._CacheKey = None
        self._MaxAge = None
        self._OfflineCache = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._Https = None
        self._Origin = None
        self._SmartRouting = None
        self._ZoneId = None
        self._Zone = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None
        self._RequestId = None

    @property
    def Cache(self):
        """Cache expiration time configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        """Node cache key configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def MaxAge(self):
        """Browser cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        """Offline cache
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        """
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        """QUIC access
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.Quic`
        """
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        """POST transport configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        """
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        """Smart compression configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        """HTTP2 origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        """
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        """Force HTTPS redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        """HTTPS acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Origin(self):
        """Origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        """Dynamic acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        """
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        """Domain name of the site
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def WebSocket(self):
        """WebSocket configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        """Origin-pull client IP header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        """
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        """Cache prefresh configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = CacheConfig()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIp()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination parameter, which specifies the offset.
        :type Offset: int
        :param _Limit: Pagination parameter, which specifies the number of sites returned in each page.
        :type Limit: int
        :param _Filters: Query condition filter, which supports complex type.
        :type Filters: list of ZoneFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """Pagination parameter, which specifies the offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter, which specifies the number of sites returned in each page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Query condition filter, which supports complex type.
        :rtype: list of ZoneFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ZoneFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of sites that match the specified conditions
        :type TotalCount: int
        :param _Zones: Details of sites
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zones: list of Zone
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Zones = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of sites that match the specified conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Zones(self):
        """Details of sites
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of Zone
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """Domain name configuration information

    """

    def __init__(self):
        r"""
        :param _AppId: Tencent Cloud account ID
        :type AppId: int
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Status: Acceleration service status
`process`: Deploying
`online`: Enabled
`offline`: Disabled
        :type Status: str
        :param _Host: Domain name
        :type Host: str
        """
        self._AppId = None
        self._ZoneId = None
        self._Status = None
        self._Host = None

    @property
    def AppId(self):
        """Tencent Cloud account ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        """Acceleration service status
`process`: Deploying
`online`: Enabled
`offline`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Host(self):
        """Domain name
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsDataFilter(AbstractModel):
    """Ignore query string parameters for DNS data

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name. Valid values:
`zone`: Site name
`host`: Domain name
`type`: DNS resolution type
`code`: DNS response code
`area`: Region of the resolution server
        :type Name: str
        :param _Value: Parameter value
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
        :param _Values: Parameter value
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
        self._Name = None
        self._Value = None
        self._Values = None

    @property
    def Name(self):
        """Parameter name. Valid values:
`zone`: Site name
`host`: Domain name
`type`: DNS resolution type
`code`: DNS response code
`area`: Region of the resolution server
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Parameter value
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
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Values(self):
        """Parameter value
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
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecord(AbstractModel):
    """DNS record

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: str
        :param _Type: Record type
        :type Type: str
        :param _Name: Host record
        :type Name: str
        :param _Content: Record value
        :type Content: str
        :param _Mode: Proxy mode
        :type Mode: str
        :param _Ttl: TTL value
        :type Ttl: int
        :param _Priority: Priority
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Priority: int
        :param _CreatedOn: Creation time
        :type CreatedOn: str
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _Locked: Domain name lock
        :type Locked: bool
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _Status: Resolution status
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param _Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param _DomainStatus: Which service is enabled for the domain name.
- `lb`: Load balancing
- `security`: Security acceleration
- `l4`: L4 proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainStatus: list of str
        """
        self._Id = None
        self._Type = None
        self._Name = None
        self._Content = None
        self._Mode = None
        self._Ttl = None
        self._Priority = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._Locked = None
        self._ZoneId = None
        self._ZoneName = None
        self._Status = None
        self._Cname = None
        self._DomainStatus = None

    @property
    def Id(self):
        """Record ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """Record type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Host record
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Record value
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Mode(self):
        """Proxy mode
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Ttl(self):
        """TTL value
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Priority(self):
        """Priority
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CreatedOn(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def Locked(self):
        """Domain name lock
        :rtype: bool
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Status(self):
        """Resolution status
`active`: Activated
`pending`: Not activated
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        """CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def DomainStatus(self):
        """Which service is enabled for the domain name.
- `lb`: Load balancing
- `security`: Security acceleration
- `l4`: L4 proxy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Mode = params.get("Mode")
        self._Ttl = params.get("Ttl")
        self._Priority = params.get("Priority")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._Locked = params.get("Locked")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        self._DomainStatus = params.get("DomainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecordFilter(AbstractModel):
    """Query filter to search for DNS records

    """

    def __init__(self):
        r"""
        :param _Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :type Name: str
        :param _Values: Filters by the field value
        :type Values: list of str
        :param _Fuzzy: Specifies whether to enable fuzzy query. It’s only available when the filter name is `name`. If it’s enabled, the length of `Values` must be 1.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        """Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filters by the field value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        """Specifies whether to enable fuzzy query. It’s only available when the filter name is `name`. If it’s enabled, the length of `Values` must be 1.
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnssecInfo(AbstractModel):
    """DNSSEC information

    """

    def __init__(self):
        r"""
        :param _Flags: Flag
        :type Flags: int
        :param _Algorithm: Encryption algorithm
        :type Algorithm: str
        :param _KeyType: Encryption type
        :type KeyType: str
        :param _DigestType: Digest type
        :type DigestType: str
        :param _DigestAlgorithm: Digest algorithm
        :type DigestAlgorithm: str
        :param _Digest: Digest message
        :type Digest: str
        :param _DS: DS record value
        :type DS: str
        :param _KeyTag: Key tag
        :type KeyTag: int
        :param _PublicKey: Public key
        :type PublicKey: str
        """
        self._Flags = None
        self._Algorithm = None
        self._KeyType = None
        self._DigestType = None
        self._DigestAlgorithm = None
        self._Digest = None
        self._DS = None
        self._KeyTag = None
        self._PublicKey = None

    @property
    def Flags(self):
        """Flag
        :rtype: int
        """
        return self._Flags

    @Flags.setter
    def Flags(self, Flags):
        self._Flags = Flags

    @property
    def Algorithm(self):
        """Encryption algorithm
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def KeyType(self):
        """Encryption type
        :rtype: str
        """
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def DigestType(self):
        """Digest type
        :rtype: str
        """
        return self._DigestType

    @DigestType.setter
    def DigestType(self, DigestType):
        self._DigestType = DigestType

    @property
    def DigestAlgorithm(self):
        """Digest algorithm
        :rtype: str
        """
        return self._DigestAlgorithm

    @DigestAlgorithm.setter
    def DigestAlgorithm(self, DigestAlgorithm):
        self._DigestAlgorithm = DigestAlgorithm

    @property
    def Digest(self):
        """Digest message
        :rtype: str
        """
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def DS(self):
        """DS record value
        :rtype: str
        """
        return self._DS

    @DS.setter
    def DS(self, DS):
        self._DS = DS

    @property
    def KeyTag(self):
        """Key tag
        :rtype: int
        """
        return self._KeyTag

    @KeyTag.setter
    def KeyTag(self, KeyTag):
        self._KeyTag = KeyTag

    @property
    def PublicKey(self):
        """Public key
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey


    def _deserialize(self, params):
        self._Flags = params.get("Flags")
        self._Algorithm = params.get("Algorithm")
        self._KeyType = params.get("KeyType")
        self._DigestType = params.get("DigestType")
        self._DigestAlgorithm = params.get("DigestAlgorithm")
        self._Digest = params.get("Digest")
        self._DS = params.get("DS")
        self._KeyTag = params.get("KeyTag")
        self._PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time. It must conform to the RFC3339 standard.
        :type StartTime: str
        :param _EndTime: End time. It must conform to the RFC3339 standard.
        :type EndTime: str
        :param _PageSize: Number of entries per page
        :type PageSize: int
        :param _PageNo: Current page
        :type PageNo: int
        :param _Zones: Array of site names
        :type Zones: list of str
        :param _Domains: Array of subdomain names
        :type Domains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageSize = None
        self._PageNo = None
        self._Zones = None
        self._Domains = None

    @property
    def StartTime(self):
        """Start time. It must conform to the RFC3339 standard.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time. It must conform to the RFC3339 standard.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageSize(self):
        """Number of entries per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Current page
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Zones(self):
        """Array of site names
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Domains(self):
        """Array of subdomain names
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Zones = params.get("Zones")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Layer-7 offline log data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of L7OfflineLog
        :param _PageSize: Page size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageSize: int
        :param _PageNo: Page number
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageNo: int
        :param _Pages: Total number of pages
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of entries
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalSize: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._PageSize = None
        self._PageNo = None
        self._Pages = None
        self._TotalSize = None
        self._RequestId = None

    @property
    def Data(self):
        """Layer-7 offline log data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of L7OfflineLog
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PageSize(self):
        """Page size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        """Page number
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of entries
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        self._RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param _Reason: Failure reason
        :type Reason: str
        :param _Targets: List of resources failed to be processed. 
 
        :type Targets: list of str
        """
        self._Reason = None
        self._Targets = None

    @property
    def Reason(self):
        """Failure reason
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Targets(self):
        """List of resources failed to be processed. 
 
        :rtype: list of str
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param _Key: Filter dimension
        :type Key: str
        :param _Operator: Operator
        :type Operator: str
        :param _Value: Filter dimension value
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        """Filter dimension
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        """Operator
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        """Filter dimension value
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Force redirect configuration switch
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RedirectStatusCode: Redirection status code
301
302
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        """Force redirect configuration switch
`on`: Enable
`off`: Disable
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectStatusCode(self):
        """Redirection status code
301
302
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeoIp(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: int
        :param _Country: Country name
        :type Country: str
        :param _Continent: Continent name
        :type Continent: str
        :param _CountryEn: Country name in English
        :type CountryEn: str
        :param _ContinentEn: Continent name in English
        :type ContinentEn: str
        """
        self._RegionId = None
        self._Country = None
        self._Continent = None
        self._CountryEn = None
        self._ContinentEn = None

    @property
    def RegionId(self):
        """Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Country(self):
        """Country name
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Continent(self):
        """Continent name
        :rtype: str
        """
        return self._Continent

    @Continent.setter
    def Continent(self, Continent):
        self._Continent = Continent

    @property
    def CountryEn(self):
        """Country name in English
        :rtype: str
        """
        return self._CountryEn

    @CountryEn.setter
    def CountryEn(self, CountryEn):
        self._CountryEn = CountryEn

    @property
    def ContinentEn(self):
        """Continent name in English
        :rtype: str
        """
        return self._ContinentEn

    @ContinentEn.setter
    def ContinentEn(self, ContinentEn):
        self._ContinentEn = ContinentEn


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Country = params.get("Country")
        self._Continent = params.get("Continent")
        self._CountryEn = params.get("CountryEn")
        self._ContinentEn = params.get("ContinentEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """HTTP header, used as input for the CreatePrefetchTask API

    """

    def __init__(self):
        r"""
        :param _Name: HTTP header name
        :type Name: str
        :param _Value: HTTP header value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """HTTP header name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """HTTP header value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertSetting(AbstractModel):
    """Certificate configurations for domain names

    """

    def __init__(self):
        r"""
        :param _Host: Domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Host: str
        :param _CertInfo: Server certificate configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of ServerCertInfo
        """
        self._Host = None
        self._CertInfo = None

    @property
    def Host(self):
        """Domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def CertInfo(self):
        """Server certificate configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of ServerCertInfo
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo


    def _deserialize(self, params):
        self._Host = params.get("Host")
        if params.get("CertInfo") is not None:
            self._CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Specifies whether to enable. Valid values: `on` and `off`.
        :type Switch: str
        :param _MaxAge: `MaxAge` value.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: int
        :param _IncludeSubDomains: Specifies whether to include subdomain names. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IncludeSubDomains: str
        :param _Preload: Specifies whether to preload. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Preload: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None
        self._Preload = None

    @property
    def Switch(self):
        """Specifies whether to enable. Valid values: `on` and `off`.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        """`MaxAge` value.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        """Specifies whether to include subdomain names. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains

    @property
    def Preload(self):
        """Specifies whether to preload. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Preload

    @Preload.setter
    def Preload(self, Preload):
        self._Preload = Preload


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        self._Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Http2: HTTP2 configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Http2: str
        :param _OcspStapling: OCSP configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OcspStapling: str
        :param _TlsVersion: TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TlsVersion: list of str
        :param _Hsts: HSTS Configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        self._Http2 = None
        self._OcspStapling = None
        self._TlsVersion = None
        self._Hsts = None

    @property
    def Http2(self):
        """HTTP2 configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        """OCSP configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def TlsVersion(self):
        """TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Hsts(self):
        """HSTS Configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts


    def _deserialize(self, params):
        self._Http2 = params.get("Http2")
        self._OcspStapling = params.get("OcspStapling")
        self._TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self._Hsts = Hsts()
            self._Hsts._deserialize(params.get("Hsts"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _Subdomain: 
        :type Subdomain: str
        :param _RecordType: Record type
        :type RecordType: str
        :param _RecordValue: Record value
        :type RecordValue: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None
        self._RequestId = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Subdomain(self):
        """
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        """Record type
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        """Record value
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._RequestId = params.get("RequestId")


class ImportDnsRecordsRequest(AbstractModel):
    """ImportDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _File: File content
        :type File: str
        """
        self._ZoneId = None
        self._File = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def File(self):
        """File content
        :rtype: str
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportDnsRecordsResponse(AbstractModel):
    """ImportDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Record ID
        :type Ids: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ids = None
        self._RequestId = None

    @property
    def Ids(self):
        """Record ID
        :rtype: list of str
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        self._RequestId = params.get("RequestId")


class IntelligenceRule(AbstractModel):
    """Bot intelligence rules

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Items: Items in a bot intelligence rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of IntelligenceRuleItem
        """
        self._Switch = None
        self._Items = None

    @property
    def Switch(self):
        """Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Items(self):
        """Items in a bot intelligence rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of IntelligenceRuleItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRuleItem(AbstractModel):
    """Bot intelligence rule items

    """

    def __init__(self):
        r"""
        :param _Label: Malicious bot, which is used to tag bad bots
Note: This field may return null, indicating that no valid values can be obtained.
        :type Label: str
        :param _Action: Action
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        """
        self._Label = None
        self._Action = None

    @property
    def Label(self):
        """Malicious bot, which is used to tag bad bots
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Action(self):
        """Action
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableConfig(AbstractModel):
    """IP/Region blocklist/allowlist configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Rules: []
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of IpTableRule
        """
        self._Switch = None
        self._Rules = None

    @property
    def Switch(self):
        """Switch
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Rules(self):
        """[]
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of IpTableRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableRule(AbstractModel):
    """IP blocklist/allowlist rule details

    """

    def __init__(self):
        r"""
        :param _Action: Action: `drop` (block), `trans` (allow), `monitor` (observe)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param _MatchFrom: Matches by IP or region. Values: `ip` and `area`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MatchFrom: str
        :param _MatchContent: Matching content
Note: This field may return null, indicating that no valid values can be obtained.
        :type MatchContent: str
        :param _RuleID: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleID: int
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._Action = None
        self._MatchFrom = None
        self._MatchContent = None
        self._RuleID = None
        self._UpdateTime = None

    @property
    def Action(self):
        """Action: `drop` (block), `trans` (allow), `monitor` (observe)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MatchFrom(self):
        """Matches by IP or region. Values: `ip` and `area`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchContent(self):
        """Matching content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent

    @property
    def RuleID(self):
        """Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        """Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._MatchFrom = params.get("MatchFrom")
        self._MatchContent = params.get("MatchContent")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """Layer-7 offline log details

    """

    def __init__(self):
        r"""
        :param _LogTime: Start time of the log packaging
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogTime: int
        :param _Domain: Subdomain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domain: str
        :param _Size: Log size, in bytes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Size: int
        :param _Url: Download address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Url: str
        :param _LogPacketName: Log package name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogPacketName: str
        """
        self._LogTime = None
        self._Domain = None
        self._Size = None
        self._Url = None
        self._LogPacketName = None

    @property
    def LogTime(self):
        """Start time of the log packaging
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def Domain(self):
        """Subdomain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Size(self):
        """Log size, in bytes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Url(self):
        """Download address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LogPacketName(self):
        """Log package name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._LogPacketName

    @LogPacketName.setter
    def LogPacketName(self, LogPacketName):
        self._LogPacketName = LogPacketName


    def _deserialize(self, params):
        self._LogTime = params.get("LogTime")
        self._Domain = params.get("Domain")
        self._Size = params.get("Size")
        self._Url = params.get("Url")
        self._LogPacketName = params.get("LogPacketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancing(AbstractModel):
    """CLB information

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param _Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param _TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param _OriginId: ID of the origin group used
        :type OriginId: list of str
        :param _Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Status: Status
        :type Status: str
        :param _Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        """
        self._LoadBalancingId = None
        self._ZoneId = None
        self._Host = None
        self._Type = None
        self._TTL = None
        self._OriginId = None
        self._Origin = None
        self._UpdateTime = None
        self._Status = None
        self._Cname = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Host(self):
        """Subdomain name. You can use @ to represent the root domain.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Type(self):
        """Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TTL(self):
        """Indicates DNS TTL time when `Type=dns_only`
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def OriginId(self):
        """ID of the origin group used
        :rtype: list of str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Origin(self):
        """Information of the origin server used
        :rtype: list of OriginGroup
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        """Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._ZoneId = params.get("ZoneId")
        self._Host = params.get("Host")
        self._Type = params.get("Type")
        self._TTL = params.get("TTL")
        self._OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self._Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self._Origin.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagedRule(AbstractModel):
    """Managed rule

    """

    def __init__(self):
        r"""
        :param _RuleId: ID of the rule
        :type RuleId: int
        :param _Description: Rule description
        :type Description: str
        :param _RuleTypeName: Rule type
        :type RuleTypeName: str
        :param _RuleLevelDesc: Rule level
        :type RuleLevelDesc: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Status: Rule status: `block`, `allow`
        :type Status: str
        :param _RuleTags: Tag of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTags: list of str
        :param _RuleTypeDesc: Description of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTypeDesc: str
        :param _RuleTypeId: ID of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTypeId: int
        """
        self._RuleId = None
        self._Description = None
        self._RuleTypeName = None
        self._RuleLevelDesc = None
        self._UpdateTime = None
        self._Status = None
        self._RuleTags = None
        self._RuleTypeDesc = None
        self._RuleTypeId = None

    @property
    def RuleId(self):
        """ID of the rule
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Description(self):
        """Rule description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleTypeName(self):
        """Rule type
        :rtype: str
        """
        return self._RuleTypeName

    @RuleTypeName.setter
    def RuleTypeName(self, RuleTypeName):
        self._RuleTypeName = RuleTypeName

    @property
    def RuleLevelDesc(self):
        """Rule level
        :rtype: str
        """
        return self._RuleLevelDesc

    @RuleLevelDesc.setter
    def RuleLevelDesc(self, RuleLevelDesc):
        self._RuleLevelDesc = RuleLevelDesc

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Rule status: `block`, `allow`
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleTags(self):
        """Tag of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._RuleTags

    @RuleTags.setter
    def RuleTags(self, RuleTags):
        self._RuleTags = RuleTags

    @property
    def RuleTypeDesc(self):
        """Description of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuleTypeDesc

    @RuleTypeDesc.setter
    def RuleTypeDesc(self, RuleTypeDesc):
        self._RuleTypeDesc = RuleTypeDesc

    @property
    def RuleTypeId(self):
        """ID of the rule type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RuleTypeId

    @RuleTypeId.setter
    def RuleTypeId(self, RuleTypeId):
        self._RuleTypeId = RuleTypeId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Description = params.get("Description")
        self._RuleTypeName = params.get("RuleTypeName")
        self._RuleLevelDesc = params.get("RuleLevelDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._RuleTags = params.get("RuleTags")
        self._RuleTypeDesc = params.get("RuleTypeDesc")
        self._RuleTypeId = params.get("RuleTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration.

    """

    def __init__(self):
        r"""
        :param _MaxAgeTime: Specifies the max age of the cache (in seconds). The maximum value is 365 days.
Note: the value `0` means not to cache.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAgeTime: int
        :param _FollowOrigin: Specifies whether to follow the max cache age of the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: str
        """
        self._MaxAgeTime = None
        self._FollowOrigin = None

    @property
    def MaxAgeTime(self):
        """Specifies the max age of the cache (in seconds). The maximum value is 365 days.
Note: the value `0` means not to cache.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxAgeTime

    @MaxAgeTime.setter
    def MaxAgeTime(self, MaxAgeTime):
        self._MaxAgeTime = MaxAgeTime

    @property
    def FollowOrigin(self):
        """Specifies whether to follow the max cache age of the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        self._MaxAgeTime = params.get("MaxAgeTime")
        self._FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: ID of the proxy
        :type ProxyId: str
        :param _ProxyName: Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :type ProxyName: str
        :param _ForwardClientIp: This parameter is disused.
        :type ForwardClientIp: str
        :param _SessionPersist: This parameter is disused.
        :type SessionPersist: bool
        :param _SessionPersistTime: Session persistence time. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param _ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :type ProxyType: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._ProxyName = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._ProxyType = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """ID of the proxy
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        """Name of the proxy:
Domain name or subdomain name when `ProxyType=hostname`
Instance name when `ProxyType=instance`
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ForwardClientIp(self):
        """This parameter is disused.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """This parameter is disused.
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        """Session persistence time. Value range: 30-3600 (in seconds).
        :rtype: int
        """
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        """Specifies how a layer-4 proxy is created.
`hostname`: Create by subdomain name
`instance`: Create by instance
        :rtype: str
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: ID of the proxy
        :type ProxyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """ID of the proxy
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: Proxy ID
        :type ProxyId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param _Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param _OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :type OriginType: str
        :param _OriginValue: Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param _ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA.
`PPV1`: Pass the client IP via Proxy Protocol V1.
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param _SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """Proxy ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Proto(self):
        """Protocol. Valid values: `TCP` and `UDP`.
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        """Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :rtype: list of str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        """Origin server type. Valid values:
`custom`: Specified origins
`origins`: Origin group
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        """Origin server information:
When `OriginType=custom`, it indicates one or more origin servers. Example:
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

When `OriginType=origins`, it indicates an origin group ID. Example:
OriginValue=["origin-xxx"]
        :rtype: list of str
        """
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        """Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA.
`PPV1`: Pass the client IP via Proxy Protocol V1.
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
        :rtype: str
        """
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        """Specifies whether to enable session persistence
        :rtype: bool
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: ID of the proxy
        :type ProxyId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Status: Status
`offline`: Disabled
`online`: Enabled
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._Status = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """ID of the proxy
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        """Status
`offline`: Disabled
`online`: Enabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ProxyId: ID of the proxy
        :type ProxyId: str
        :param _Status: Status
`offline`: Disabled
`online`: Enabled
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Status = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        """ID of the proxy
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        """Status
`offline`: Disabled
`online`: Enabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: ID of the proxy
        :type ProxyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """ID of the proxy
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyHostRequest(AbstractModel):
    """ModifyDDoSPolicyHost request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Host: Second-level domain name
        :type Host: str
        :param _AccelerateType: Whether to enable content acceleration. Values: `on` (enable content acceleration), and `off` (disable content acceleration). It can be used together with `SecurityType`.
        :type AccelerateType: str
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _SecurityType: Whether to enable security protection. Values: `on` (enable security protection) and `off` (disable security protection). It can be used together with `AccelerateType`.
        :type SecurityType: str
        """
        self._ZoneId = None
        self._Host = None
        self._AccelerateType = None
        self._PolicyId = None
        self._SecurityType = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Host(self):
        """Second-level domain name
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def AccelerateType(self):
        """Whether to enable content acceleration. Values: `on` (enable content acceleration), and `off` (disable content acceleration). It can be used together with `SecurityType`.
        :rtype: str
        """
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def PolicyId(self):
        """Policy ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def SecurityType(self):
        """Whether to enable security protection. Values: `on` (enable security protection) and `off` (disable security protection). It can be used together with `AccelerateType`.
        :rtype: str
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Host = params.get("Host")
        self._AccelerateType = params.get("AccelerateType")
        self._PolicyId = params.get("PolicyId")
        self._SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyHostResponse(AbstractModel):
    """ModifyDDoSPolicyHost response structure.

    """

    def __init__(self):
        r"""
        :param _Host: Subdomain name
        :type Host: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Host = None
        self._RequestId = None

    @property
    def Host(self):
        """Subdomain name
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: ID of the policy group
        :type PolicyId: int
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _DdosRule: Detailed DDoS mitigation configuration
        :type DdosRule: :class:`tencentcloud.teo.v20220106.models.DdosRule`
        """
        self._PolicyId = None
        self._ZoneId = None
        self._DdosRule = None

    @property
    def PolicyId(self):
        """ID of the policy group
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DdosRule(self):
        """Detailed DDoS mitigation configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.DdosRule`
        """
        return self._DdosRule

    @DdosRule.setter
    def DdosRule(self, DdosRule):
        self._DdosRule = DdosRule


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._ZoneId = params.get("ZoneId")
        if params.get("DdosRule") is not None:
            self._DdosRule = DdosRule()
            self._DdosRule._deserialize(params.get("DdosRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: ID of the policy group
        :type PolicyId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """ID of the policy group
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _CertId: Certificate ID
        :type CertId: str
        :param _Status: Certificate status
`deployed`: The certificate is deployed.
`disabled`: The certificate is disabled.
If the deployment fails, you can pass in `Status = deployed` again.
        :type Status: str
        """
        self._ZoneId = None
        self._CertId = None
        self._Status = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CertId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """Certificate status
`deployed`: The certificate is deployed.
`disabled`: The certificate is disabled.
If the deployment fails, you can pass in `Status = deployed` again.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateResponse(AbstractModel):
    """ModifyDefaultCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDnsRecordRequest(AbstractModel):
    """ModifyDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Type: Record type
        :type Type: str
        :param _Name: Record name
        :type Name: str
        :param _Content: Record content
        :type Content: str
        :param _Ttl: 
        :type Ttl: int
        :param _Priority: Priority
        :type Priority: int
        :param _Mode: Proxy mode
        :type Mode: str
        """
        self._Id = None
        self._ZoneId = None
        self._Type = None
        self._Name = None
        self._Content = None
        self._Ttl = None
        self._Priority = None
        self._Mode = None

    @property
    def Id(self):
        """Record ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        """Record type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Record name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Record content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ttl(self):
        """
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Priority(self):
        """Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Mode(self):
        """Proxy mode
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Ttl = params.get("Ttl")
        self._Priority = params.get("Priority")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnsRecordResponse(AbstractModel):
    """ModifyDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: str
        :param _Type: Record type
        :type Type: str
        :param _Name: Record name
        :type Name: str
        :param _Content: Record content
        :type Content: str
        :param _Ttl: 
        :type Ttl: int
        :param _Priority: Priority
        :type Priority: int
        :param _Mode: Proxy mode
        :type Mode: str
        :param _Status: Resolution status
        :type Status: str
        :param _Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param _Locked: Whether the DNS record is locked
        :type Locked: bool
        :param _CreatedOn: Creation time
        :type CreatedOn: str
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Type = None
        self._Name = None
        self._Content = None
        self._Ttl = None
        self._Priority = None
        self._Mode = None
        self._Status = None
        self._Cname = None
        self._Locked = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._ZoneId = None
        self._ZoneName = None
        self._RequestId = None

    @property
    def Id(self):
        """Record ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """Record type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Record name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Record content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ttl(self):
        """
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Priority(self):
        """Priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Mode(self):
        """Proxy mode
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        """Resolution status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        """CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Locked(self):
        """Whether the DNS record is locked
        :rtype: bool
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def CreatedOn(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Ttl = params.get("Ttl")
        self._Priority = params.get("Priority")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        self._Locked = params.get("Locked")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Status: DNSSEC status
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self._Id = None
        self._Status = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """DNSSEC status
- `enabled`: Enabled
- `disabled`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnssecResponse(AbstractModel):
    """ModifyDnssec response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _Status: DNSSEC status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param _Dnssec: DNSSEC information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._Dnssec = None
        self._ModifiedOn = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """DNSSEC status.
- `enabled`: Enabled
- `disabled`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Dnssec(self):
        """DNSSEC information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        """
        return self._Dnssec

    @Dnssec.setter
    def Dnssec(self, Dnssec):
        self._Dnssec = Dnssec

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self._Dnssec = DnssecInfo()
            self._Dnssec._deserialize(params.get("Dnssec"))
        self._ModifiedOn = params.get("ModifiedOn")
        self._RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Hosts: Domain name that the certificate will be attached to
        :type Hosts: list of str
        :param _CertInfo: Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :type CertInfo: list of ServerCertInfo
        """
        self._ZoneId = None
        self._Hosts = None
        self._CertInfo = None

    @property
    def ZoneId(self):
        """ID of the site
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Hosts(self):
        """Domain name that the certificate will be attached to
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def CertInfo(self):
        """Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :rtype: list of ServerCertInfo
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Hosts = params.get("Hosts")
        if params.get("CertInfo") is not None:
            self._CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancingRequest(AbstractModel):
    """ModifyLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _Type: Proxy mode.
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param _OriginId: ID of the origin group used
        :type OriginId: list of str
        :param _TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        """
        self._ZoneId = None
        self._LoadBalancingId = None
        self._Type = None
        self._OriginId = None
        self._TTL = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def Type(self):
        """Proxy mode.
`dns_only`: Only DNS
`proxied`: Enable proxy
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OriginId(self):
        """ID of the origin group used
        :rtype: list of str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def TTL(self):
        """Indicates DNS TTL time when `Type=dns_only`
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._Type = params.get("Type")
        self._OriginId = params.get("OriginId")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingResponse(AbstractModel):
    """ModifyLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancingId = None
        self._RequestId = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _Status: Status.
`online`: Enabled
`offline`: Disabled
        :type Status: str
        """
        self._ZoneId = None
        self._LoadBalancingId = None
        self._Status = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def Status(self):
        """Status.
`online`: Enabled
`offline`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingStatusResponse(AbstractModel):
    """ModifyLoadBalancingStatus response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancingId = None
        self._RequestId = None

    @property
    def LoadBalancingId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancingId

    @LoadBalancingId.setter
    def LoadBalancingId(self, LoadBalancingId):
        self._LoadBalancingId = LoadBalancingId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancingId = params.get("LoadBalancingId")
        self._RequestId = params.get("RequestId")


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: ID of the origin group
        :type OriginId: str
        :param _OriginName: Name of the origin group
        :type OriginName: str
        :param _Type: Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :type Type: str
        :param _Record: Origin record
        :type Record: list of OriginRecord
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _OriginType: Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :type OriginType: str
        """
        self._OriginId = None
        self._OriginName = None
        self._Type = None
        self._Record = None
        self._ZoneId = None
        self._OriginType = None

    @property
    def OriginId(self):
        """ID of the origin group
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def OriginName(self):
        """Name of the origin group
        :rtype: str
        """
        return self._OriginName

    @OriginName.setter
    def OriginName(self, OriginName):
        self._OriginName = OriginName

    @property
    def Type(self):
        """Origin-pull configuration type. This field is required when `OriginType=self`.
`area`: Origin-pull by region
`weight`: Origin-pull by weight
When `OriginType=third_party/cos`, it can be left empty.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Record(self):
        """Origin record
        :rtype: list of OriginRecord
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OriginType(self):
        """Origin type
`self`: Customer origin
`third_party`: Third-party origin
`cos`: Tencent Cloud COS origin
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._OriginName = params.get("OriginName")
        self._Type = params.get("Type")
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Record.append(obj)
        self._ZoneId = params.get("ZoneId")
        self._OriginType = params.get("OriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOriginGroupResponse(AbstractModel):
    """ModifyOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginId = None
        self._RequestId = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Subdomain name/layer-4 proxy
        :type Entity: str
        :param _Config: Security configuration
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        """
        self._ZoneId = None
        self._Entity = None
        self._Config = None

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Subdomain name/layer-4 proxy
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Config(self):
        """Security configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        if params.get("Config") is not None:
            self._Config = SecurityConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self._Id = None
        self._Status = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCnameSpeedUpResponse(AbstractModel):
    """ModifyZoneCnameSpeedUp response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param _ModifiedOn: Update time
        :type ModifiedOn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._ModifiedOn = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifiedOn(self):
        """Update time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ModifiedOn = params.get("ModifiedOn")
        self._RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID, which is used to identify the site.
        :type Id: str
        :param _Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param _VanityNameServers: Custom site information
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        self._Id = None
        self._Type = None
        self._VanityNameServers = None

    @property
    def Id(self):
        """Site ID, which is used to identify the site.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VanityNameServers(self):
        """Custom site information
        :rtype: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _OriginalNameServers: Name server used by the site
        :type OriginalNameServers: list of str
        :param _Status: Site status.
- `pending`: The name server is not connected.
- `active`: The name server is connected.
- `moved`: The name server is moved.
        :type Status: str
        :param _Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param _NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param _CreatedOn: Creation time
        :type CreatedOn: str
        :param _ModifiedOn: Modification time
        :type ModifiedOn: str
        :param _CnameStatus: CNAME access status.
- `finished`: Ownership of the site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._OriginalNameServers = None
        self._Status = None
        self._Type = None
        self._NameServers = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._CnameStatus = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginalNameServers(self):
        """Name server used by the site
        :rtype: list of str
        """
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def Status(self):
        """Site status.
- `pending`: The name server is not connected.
- `active`: The name server is connected.
- `moved`: The name server is moved.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NameServers(self):
        """List of name servers assigned by Tencent Cloud
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def CreatedOn(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Modification time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def CnameStatus(self):
        """CNAME access status.
- `finished`: Ownership of the site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._NameServers = params.get("NameServers")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._CnameStatus = params.get("CnameStatus")
        self._RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site to be modified
        :type ZoneId: str
        :param _Cache: Cache expiration time
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param _CacheKey: Node cache key
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param _MaxAge: Browser cache configuration
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param _OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param _Quic: QUIC access
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param _PostMaxSize: Maximum size of files transferred over POST request
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param _Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param _UpstreamHttp2: HTTP2 origin-pull configuration
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param _ForceRedirect: Force HTTPS redirect configuration
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param _Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param _Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param _SmartRouting: Smart acceleration configuration
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param _WebSocket: WebSocket configuration
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param _ClientIpHeader: Origin-pull client IP header configuration
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param _CachePrefresh: Cache prefresh configuration
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        self._ZoneId = None
        self._Cache = None
        self._CacheKey = None
        self._MaxAge = None
        self._OfflineCache = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._Https = None
        self._Origin = None
        self._SmartRouting = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None

    @property
    def ZoneId(self):
        """ID of the site to be modified
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Cache(self):
        """Cache expiration time
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        """Node cache key
        :rtype: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def MaxAge(self):
        """Browser cache configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        """Offline cache
        :rtype: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        """
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        """QUIC access
        :rtype: :class:`tencentcloud.teo.v20220106.models.Quic`
        """
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        """Maximum size of files transferred over POST request
        :rtype: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        """
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        """Smart compression configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        """HTTP2 origin-pull configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        """
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        """Force HTTPS redirect configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        """HTTPS acceleration configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Origin(self):
        """Origin server configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        """Smart acceleration configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        """
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def WebSocket(self):
        """WebSocket configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        """Origin-pull client IP header configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        """
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        """Cache prefresh configuration
        :rtype: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Cache") is not None:
            self._Cache = CacheConfig()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIp()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._RequestId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        """
        self._Id = None
        self._Paused = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Paused(self):
        """Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :rtype: bool
        """
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        :param _ModifiedOn: Update time
        :type ModifiedOn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._Name = None
        self._Paused = None
        self._ModifiedOn = None
        self._RequestId = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Paused(self):
        """Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :rtype: bool
        """
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def ModifiedOn(self):
        """Update time
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Paused = params.get("Paused")
        self._ModifiedOn = params.get("ModifiedOn")
        self._RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """Configuration of offline cache

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable offline cache. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to enable offline cache. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """Origin server configuration

    """

    def __init__(self):
        r"""
        :param _OriginPullProtocol: Origin-pull protocol.
`http`: Switch HTTPS requests to HTTP
`follow`: Follow the protocol of the request.
`https`: Switch HTTP requests to HTTPS. This only supports port 443 on the origin server.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        """
        self._OriginPullProtocol = None

    @property
    def OriginPullProtocol(self):
        """Origin-pull protocol.
`http`: Switch HTTPS requests to HTTP
`follow`: Follow the protocol of the request.
`https`: Switch HTTP requests to HTTPS. This only supports port 443 on the origin server.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol


    def _deserialize(self, params):
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCheckOriginStatus(AbstractModel):
    """Origin health status

    """

    def __init__(self):
        r"""
        :param _Status: `healthy`: Healthy; `unhealthy`: Unhealthy; `process`: Checking origin.
        :type Status: str
        :param _Host: List of unhealthy origin groups when `Status = unhealthy`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: list of str
        """
        self._Status = None
        self._Host = None

    @property
    def Status(self):
        """`healthy`: Healthy; `unhealthy`: Unhealthy; `process`: Checking origin.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Host(self):
        """List of unhealthy origin groups when `Status = unhealthy`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginFilter(AbstractModel):
    """The filter parameter to query origin groups

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered. Supported field: name
        :type Name: str
        :param _Value: Value of the field
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Field to be filtered. Supported field: name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Value of the field
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """Origin group information

    """

    def __init__(self):
        r"""
        :param _OriginId: Origin group ID
        :type OriginId: str
        :param _OriginName: Origin group name
        :type OriginName: str
        :param _Type: Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in `OriginRecord`.
`weight`: Origin-pull by the weight specified by `Weight` in `OriginRecord`.
        :type Type: str
        :param _Record: Record
        :type Record: list of OriginRecord
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _ZoneName: Site name
        :type ZoneName: str
        :param _OriginType: Origin server type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginType: str
        :param _ApplicationProxyUsed: Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationProxyUsed: bool
        :param _LoadBalancingUsed: Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsed: bool
        :param _Status: Origin status 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: :class:`tencentcloud.teo.v20220106.models.OriginCheckOriginStatus`
        :param _LoadBalancingUsedType: Proxy mode of the load balancing task associated with the origin group.
`none`: This origin group is not used for load balancing.
`dns_only`: Used for DNS-only load balancing 
`proxied`: Used for proxied load balancing
`both`: It’s used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancingUsedType: str
        """
        self._OriginId = None
        self._OriginName = None
        self._Type = None
        self._Record = None
        self._UpdateTime = None
        self._ZoneId = None
        self._ZoneName = None
        self._OriginType = None
        self._ApplicationProxyUsed = None
        self._LoadBalancingUsed = None
        self._Status = None
        self._LoadBalancingUsedType = None

    @property
    def OriginId(self):
        """Origin group ID
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def OriginName(self):
        """Origin group name
        :rtype: str
        """
        return self._OriginName

    @OriginName.setter
    def OriginName(self, OriginName):
        self._OriginName = OriginName

    @property
    def Type(self):
        """Origin-pull configuration type
`area`: Origin-pull by the client IP’s region specified by `Area` in `OriginRecord`.
`weight`: Origin-pull by the weight specified by `Weight` in `OriginRecord`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Record(self):
        """Record
        :rtype: list of OriginRecord
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """Site name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def OriginType(self):
        """Origin server type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ApplicationProxyUsed(self):
        """Whether the origin group uses layer-4 proxy.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ApplicationProxyUsed

    @ApplicationProxyUsed.setter
    def ApplicationProxyUsed(self, ApplicationProxyUsed):
        self._ApplicationProxyUsed = ApplicationProxyUsed

    @property
    def LoadBalancingUsed(self):
        """Whether the origin group is used for load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._LoadBalancingUsed

    @LoadBalancingUsed.setter
    def LoadBalancingUsed(self, LoadBalancingUsed):
        self._LoadBalancingUsed = LoadBalancingUsed

    @property
    def Status(self):
        """Origin status 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.OriginCheckOriginStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancingUsedType(self):
        """Proxy mode of the load balancing task associated with the origin group.
`none`: This origin group is not used for load balancing.
`dns_only`: Used for DNS-only load balancing 
`proxied`: Used for proxied load balancing
`both`: It’s used for both DNS-only and proxied load balancing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancingUsedType

    @LoadBalancingUsedType.setter
    def LoadBalancingUsedType(self, LoadBalancingUsedType):
        self._LoadBalancingUsedType = LoadBalancingUsedType


    def _deserialize(self, params):
        self._OriginId = params.get("OriginId")
        self._OriginName = params.get("OriginName")
        self._Type = params.get("Type")
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Record.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._OriginType = params.get("OriginType")
        self._ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self._LoadBalancingUsed = params.get("LoadBalancingUsed")
        if params.get("Status") is not None:
            self._Status = OriginCheckOriginStatus()
            self._Status._deserialize(params.get("Status"))
        self._LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """Origin group record

    """

    def __init__(self):
        r"""
        :param _Record: Record value
        :type Record: str
        :param _Area: A specific region when `Type=area`.
The default region when `Type` is not specified.
        :type Area: list of str
        :param _Weight: A specific weight when `Type=weight`.
The value range is [1-100].
The total weight of multiple origins in an origin group should be 100.
        :type Weight: int
        :param _Port: Port
        :type Port: int
        :param _RecordId: Record ID
        :type RecordId: str
        :param _Private: Specifies whether to run private origin authentication.
It is valid only when `OriginType=third_part`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Private: bool
        :param _PrivateParameter: Private origin parameter.
It is valid only when `Private=true`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PrivateParameter: list of OriginRecordPrivateParameter
        :param _Proto: 
        :type Proto: str
        """
        self._Record = None
        self._Area = None
        self._Weight = None
        self._Port = None
        self._RecordId = None
        self._Private = None
        self._PrivateParameter = None
        self._Proto = None

    @property
    def Record(self):
        """Record value
        :rtype: str
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Area(self):
        """A specific region when `Type=area`.
The default region when `Type` is not specified.
        :rtype: list of str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Weight(self):
        """A specific weight when `Type=weight`.
The value range is [1-100].
The total weight of multiple origins in an origin group should be 100.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        """Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RecordId(self):
        """Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Private(self):
        """Specifies whether to run private origin authentication.
It is valid only when `OriginType=third_part`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Private

    @Private.setter
    def Private(self, Private):
        self._Private = Private

    @property
    def PrivateParameter(self):
        """Private origin parameter.
It is valid only when `Private=true`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of OriginRecordPrivateParameter
        """
        return self._PrivateParameter

    @PrivateParameter.setter
    def PrivateParameter(self, PrivateParameter):
        self._PrivateParameter = PrivateParameter

    @property
    def Proto(self):
        """
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto


    def _deserialize(self, params):
        self._Record = params.get("Record")
        self._Area = params.get("Area")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        self._RecordId = params.get("RecordId")
        self._Private = params.get("Private")
        if params.get("PrivateParameter") is not None:
            self._PrivateParameter = []
            for item in params.get("PrivateParameter"):
                obj = OriginRecordPrivateParameter()
                obj._deserialize(item)
                self._PrivateParameter.append(obj)
        self._Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecordPrivateParameter(AbstractModel):
    """Private origin authentication parameter

    """

    def __init__(self):
        r"""
        :param _Name: Name of the private origin authentication parameter.
`AccessKeyId`: Access key ID
`SecretAccessKey`: Secret access key
        :type Name: str
        :param _Value: Value of the private origin authentication parameter
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Name of the private origin authentication parameter.
`AccessKeyId`: Access key ID
`SecretAccessKey`: Secret access key
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Value of the private origin authentication parameter
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortraitManagedRuleDetail(AbstractModel):
    """User profiling rule details

    """

    def __init__(self):
        r"""
        :param _RuleId: Unique rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param _Description: Rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _RuleTypeName: Rule type name: botdb (user profile)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleTypeName: str
        :param _ClassificationId: Rule feature category ID (scanner, bot behavior, etc.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClassificationId: int
        :param _Status: Current rule action status (block, alg, etc.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._RuleId = None
        self._Description = None
        self._RuleTypeName = None
        self._ClassificationId = None
        self._Status = None

    @property
    def RuleId(self):
        """Unique rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Description(self):
        """Rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleTypeName(self):
        """Rule type name: botdb (user profile)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RuleTypeName

    @RuleTypeName.setter
    def RuleTypeName(self, RuleTypeName):
        self._RuleTypeName = RuleTypeName

    @property
    def ClassificationId(self):
        """Rule feature category ID (scanner, bot behavior, etc.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ClassificationId

    @ClassificationId.setter
    def ClassificationId(self, ClassificationId):
        self._ClassificationId = ClassificationId

    @property
    def Status(self):
        """Current rule action status (block, alg, etc.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Description = params.get("Description")
        self._RuleTypeName = params.get("RuleTypeName")
        self._ClassificationId = params.get("ClassificationId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param _Switch: Specifies whether to enable custom setting of the maximum file size. 
`off`: Disable. In this case, the max size defaults to 32 MB.
`on`: Enable. You can set a custom max size.
        :type Switch: str
        :param _MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxSize: int
        """
        self._Switch = None
        self._MaxSize = None

    @property
    def Switch(self):
        """Specifies whether to enable custom setting of the maximum file size. 
`off`: Disable. In this case, the max size defaults to 32 MB.
`on`: Enable. You can set a custom max size.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxSize(self):
        """Maximum size. Value range: 1-500 MB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """Query condition

    """

    def __init__(self):
        r"""
        :param _Key: Dimension
        :type Key: str
        :param _Operator: Operator
        :type Operator: str
        :param _Value: Dimension value
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        """Dimension
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        """Operator
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        """Dimension value
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """Request parameter contained in `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to use `QueryString` as part of `CacheKey`. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param _Action: `includeCustom`: Include the specified query strings.
`excludeCustom`: Exclude the specified query strings.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param _Value: Array of query strings used/excluded
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: list of str
        """
        self._Switch = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        """Whether to use `QueryString` as part of `CacheKey`. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        """`includeCustom`: Include the specified query strings.
`excludeCustom`: Exclude the specified query strings.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        """Array of query strings used/excluded
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable QUIC
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to enable QUIC
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """Rate limit configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
        :type Switch: str
        :param _UserRules: Rate limit rule
        :type UserRules: list of RateLimitUserRule
        :param _Template: Default template
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Template: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplate`
        :param _Intelligence: Client filtering
Note: This field may return null, indicating that no valid values can be obtained.
        :type Intelligence: :class:`tencentcloud.teo.v20220106.models.RateLimitIntelligence`
        """
        self._Switch = None
        self._UserRules = None
        self._Template = None
        self._Intelligence = None

    @property
    def Switch(self):
        """Switch
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def UserRules(self):
        """Rate limit rule
        :rtype: list of RateLimitUserRule
        """
        return self._UserRules

    @UserRules.setter
    def UserRules(self, UserRules):
        self._UserRules = UserRules

    @property
    def Template(self):
        """Default template
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplate`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Intelligence(self):
        """Client filtering
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.RateLimitIntelligence`
        """
        return self._Intelligence

    @Intelligence.setter
    def Intelligence(self, Intelligence):
        self._Intelligence = Intelligence


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self._UserRules = []
            for item in params.get("UserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self._UserRules.append(obj)
        if params.get("Template") is not None:
            self._Template = RateLimitTemplate()
            self._Template._deserialize(params.get("Template"))
        if params.get("Intelligence") is not None:
            self._Intelligence = RateLimitIntelligence()
            self._Intelligence._deserialize(params.get("Intelligence"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligence(AbstractModel):
    """Client filtering

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable this feature
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Action: Action. Values: `monitor` (observe), `alg` (JS/Managed challenge)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        """
        self._Switch = None
        self._Action = None

    @property
    def Switch(self):
        """Whether to enable this feature
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        """Action. Values: `monitor` (observe), `alg` (JS/Managed challenge)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplate(AbstractModel):
    """Rate limit template

    """

    def __init__(self):
        r"""
        :param _Mode: Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _Detail: Template details
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Detail: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplateDetail`
        """
        self._Mode = None
        self._Detail = None

    @property
    def Mode(self):
        """Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Detail(self):
        """Template details
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplateDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("Detail") is not None:
            self._Detail = RateLimitTemplateDetail()
            self._Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """Rate limit template configuration

    """

    def __init__(self):
        r"""
        :param _Mode: Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _ID: Unique ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ID: int
        :param _Action: Action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param _PunishTime: Time it takes to perform the action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PunishTime: int
        :param _Threshold: Request rate threshold
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Threshold: int
        :param _Period: Statistical period
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Period: int
        """
        self._Mode = None
        self._ID = None
        self._Action = None
        self._PunishTime = None
        self._Threshold = None
        self._Period = None

    @property
    def Mode(self):
        """Template name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ID(self):
        """Unique ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Action(self):
        """Action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        """Time it takes to perform the action
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def Threshold(self):
        """Request rate threshold
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        """Statistical period
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._ID = params.get("ID")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitUserRule(AbstractModel):
    """Rate limit rule

    """

    def __init__(self):
        r"""
        :param _Threshold: Rate threshold
        :type Threshold: int
        :param _Period: Data collection time
        :type Period: int
        :param _RuleName: Name of the rule
        :type RuleName: str
        :param _Action: Action: `monitor` (Observe), `drop` (Block)
        :type Action: str
        :param _PunishTime: Time it takes to perform the action
        :type PunishTime: int
        :param _PunishTimeUnit: Time unit: second
        :type PunishTimeUnit: str
        :param _RuleStatus: Status of the rule
        :type RuleStatus: str
        :param _Conditions: Rule
        :type Conditions: list of ACLCondition
        :param _RulePriority: Priority of the rule
        :type RulePriority: int
        :param _RuleID: ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleID: int
        :param _FreqFields: Word filter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FreqFields: list of str
        :param _UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        """
        self._Threshold = None
        self._Period = None
        self._RuleName = None
        self._Action = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._RuleStatus = None
        self._Conditions = None
        self._RulePriority = None
        self._RuleID = None
        self._FreqFields = None
        self._UpdateTime = None

    @property
    def Threshold(self):
        """Rate threshold
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        """Data collection time
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RuleName(self):
        """Name of the rule
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        """Action: `monitor` (Observe), `drop` (Block)
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        """Time it takes to perform the action
        :rtype: int
        """
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        """Time unit: second
        :rtype: str
        """
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def RuleStatus(self):
        """Status of the rule
        :rtype: str
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def Conditions(self):
        """Rule
        :rtype: list of ACLCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def RulePriority(self):
        """Priority of the rule
        :rtype: int
        """
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        """ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def FreqFields(self):
        """Word filter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._FreqFields

    @FreqFields.setter
    def FreqFields(self, FreqFields):
        self._FreqFields = FreqFields

    @property
    def UpdateTime(self):
        """Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._FreqFields = params.get("FreqFields")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._RequestId = None

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Billable resource

    """

    def __init__(self):
        r"""
        :param _Id: Resource ID
        :type Id: str
        :param _PayMode: Billing mode
`0`: Pay-as-you-go
        :type PayMode: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _EnableTime: Effective time
        :type EnableTime: str
        :param _ExpireTime: Expiration time
        :type ExpireTime: str
        :param _Status: Status of the plan
        :type Status: str
        :param _Sv: Pricing query parameter
        :type Sv: list of Sv
        :param _AutoRenewFlag: Specifies whether to enable auto-renewal
`0`: Default
`1`: Enable auto-renewal
`2`: Disable auto-renewal
        :type AutoRenewFlag: int
        :param _PlanId: ID of the plan
        :type PlanId: str
        :param _Area: 
        :type Area: str
        """
        self._Id = None
        self._PayMode = None
        self._CreateTime = None
        self._EnableTime = None
        self._ExpireTime = None
        self._Status = None
        self._Sv = None
        self._AutoRenewFlag = None
        self._PlanId = None
        self._Area = None

    @property
    def Id(self):
        """Resource ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PayMode(self):
        """Billing mode
`0`: Pay-as-you-go
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        """Effective time
        :rtype: str
        """
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ExpireTime(self):
        """Expiration time
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        """Status of the plan
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Sv(self):
        """Pricing query parameter
        :rtype: list of Sv
        """
        return self._Sv

    @Sv.setter
    def Sv(self, Sv):
        self._Sv = Sv

    @property
    def AutoRenewFlag(self):
        """Specifies whether to enable auto-renewal
`0`: Default
`1`: Enable auto-renewal
`2`: Disable auto-renewal
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PlanId(self):
        """ID of the plan
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Area(self):
        """
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        if params.get("Sv") is not None:
            self._Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self._Sv.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PlanId = params.get("PlanId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDnsRecordsRequest(AbstractModel):
    """ScanDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        """Site ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDnsRecordsResponse(AbstractModel):
    """ScanDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Scan status
- `doing`: Scanning
- `done`: Scanned
        :type Status: str
        :param _RecordsAdded: Number of DNS records added after scanning
        :type RecordsAdded: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RecordsAdded = None
        self._RequestId = None

    @property
    def Status(self):
        """Scan status
- `doing`: Scanning
- `done`: Scanned
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RecordsAdded(self):
        """Number of DNS records added after scanning
        :rtype: int
        """
        return self._RecordsAdded

    @RecordsAdded.setter
    def RecordsAdded(self, RecordsAdded):
        self._RecordsAdded = RecordsAdded

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RecordsAdded = params.get("RecordsAdded")
        self._RequestId = params.get("RequestId")


class SecEntry(AbstractModel):
    """Returned value of security data entry

    """

    def __init__(self):
        r"""
        :param _Key: Entry key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Entry value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: list of SecEntryValue
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Entry key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Entry value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SecEntryValue
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """Corresponding value of security data entry

    """

    def __init__(self):
        r"""
        :param _Metric: Metric name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metric: str
        :param _Detail: Metric data details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        :param _Max: Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: int
        :param _Avg: Average
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avg: float
        :param _Sum: Sum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sum: float
        """
        self._Metric = None
        self._Detail = None
        self._Max = None
        self._Avg = None
        self._Sum = None

    @property
    def Metric(self):
        """Metric name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Detail(self):
        """Metric data details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingDataItem
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Max(self):
        """Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        """Average
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def Sum(self):
        """Sum
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """Security configuration

    """

    def __init__(self):
        r"""
        :param _WafConfig: WAF configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WafConfig: :class:`tencentcloud.teo.v20220106.models.WafConfig`
        :param _RateLimitConfig: Rate limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220106.models.RateLimitConfig`
        :param _DdosConfig: DDoS mitigation configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DdosConfig: :class:`tencentcloud.teo.v20220106.models.DDoSConfig`
        :param _AclConfig: ACL configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AclConfig: :class:`tencentcloud.teo.v20220106.models.AclConfig`
        :param _BotConfig: Bot configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BotConfig: :class:`tencentcloud.teo.v20220106.models.BotConfig`
        :param _SwitchConfig: Switch that controls all web security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SwitchConfig: :class:`tencentcloud.teo.v20220106.models.SwitchConfig`
        :param _IpTableConfig: IP blocklist/allowlist
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpTableConfig: :class:`tencentcloud.teo.v20220106.models.IpTableConfig`
        """
        self._WafConfig = None
        self._RateLimitConfig = None
        self._DdosConfig = None
        self._AclConfig = None
        self._BotConfig = None
        self._SwitchConfig = None
        self._IpTableConfig = None

    @property
    def WafConfig(self):
        """WAF configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.WafConfig`
        """
        return self._WafConfig

    @WafConfig.setter
    def WafConfig(self, WafConfig):
        self._WafConfig = WafConfig

    @property
    def RateLimitConfig(self):
        """Rate limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.RateLimitConfig`
        """
        return self._RateLimitConfig

    @RateLimitConfig.setter
    def RateLimitConfig(self, RateLimitConfig):
        self._RateLimitConfig = RateLimitConfig

    @property
    def DdosConfig(self):
        """DDoS mitigation configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.DDoSConfig`
        """
        return self._DdosConfig

    @DdosConfig.setter
    def DdosConfig(self, DdosConfig):
        self._DdosConfig = DdosConfig

    @property
    def AclConfig(self):
        """ACL configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.AclConfig`
        """
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig

    @property
    def BotConfig(self):
        """Bot configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.BotConfig`
        """
        return self._BotConfig

    @BotConfig.setter
    def BotConfig(self, BotConfig):
        self._BotConfig = BotConfig

    @property
    def SwitchConfig(self):
        """Switch that controls all web security configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.SwitchConfig`
        """
        return self._SwitchConfig

    @SwitchConfig.setter
    def SwitchConfig(self, SwitchConfig):
        self._SwitchConfig = SwitchConfig

    @property
    def IpTableConfig(self):
        """IP blocklist/allowlist
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.IpTableConfig`
        """
        return self._IpTableConfig

    @IpTableConfig.setter
    def IpTableConfig(self, IpTableConfig):
        self._IpTableConfig = IpTableConfig


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self._WafConfig = WafConfig()
            self._WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self._RateLimitConfig = RateLimitConfig()
            self._RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("DdosConfig") is not None:
            self._DdosConfig = DDoSConfig()
            self._DdosConfig._deserialize(params.get("DdosConfig"))
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        if params.get("BotConfig") is not None:
            self._BotConfig = BotConfig()
            self._BotConfig._deserialize(params.get("BotConfig"))
        if params.get("SwitchConfig") is not None:
            self._SwitchConfig = SwitchConfig()
            self._SwitchConfig._deserialize(params.get("SwitchConfig"))
        if params.get("IpTableConfig") is not None:
            self._IpTableConfig = IpTableConfig()
            self._IpTableConfig._deserialize(params.get("IpTableConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityEntity(AbstractModel):
    """Protected resource

    """

    def __init__(self):
        r"""
        :param _AppId: User APPID
        :type AppId: int
        :param _ZoneId: Top-level domain name
        :type ZoneId: str
        :param _Entity: Second-level domain name
        :type Entity: str
        :param _EntityType: Type of protected resource. Values: `domain` and `application`.
        :type EntityType: str
        """
        self._AppId = None
        self._ZoneId = None
        self._Entity = None
        self._EntityType = None

    @property
    def AppId(self):
        """User APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ZoneId(self):
        """Top-level domain name
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entity(self):
        """Second-level domain name
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def EntityType(self):
        """Type of protected resource. Values: `domain` and `application`.
        :rtype: str
        """
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ZoneId = params.get("ZoneId")
        self._Entity = params.get("Entity")
        self._EntityType = params.get("EntityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param _CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param _Alias: Alias of the certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param _Type: Certificate type.
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Certificate deployment time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DeployTime: str
        :param _Status: Certificate deployment status.
`processing`: Deploying
`deployed`: Deployed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._DeployTime = None
        self._Status = None

    @property
    def CertId(self):
        """Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        """Alias of the certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        """Certificate type.
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        """Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        """Certificate deployment time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Status(self):
        """Certificate deployment status.
`processing`: Deploying
`deployed`: Deployed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldArea(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site (top-level domain name)
        :type ZoneId: str
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _Type: Type of protected resource. Values: `domain` and `application`.
        :type Type: str
        :param _EntityName: Layer-4 proxy name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EntityName: str
        :param _Application: Layer-7 domain name parameters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Application: list of DDoSApplication
        :param _TcpNum: Number of layer-4 TCP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TcpNum: int
        :param _UdpNum: Number of layer-4 UDP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UdpNum: int
        :param _Entity: Name of the protected resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Entity: str
        :param _Share: Whether the shared resource is used. Values: `true` (yes) and `false` (no). The proxy mode cannot be switched when the shared resource is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Share: bool
        """
        self._ZoneId = None
        self._PolicyId = None
        self._Type = None
        self._EntityName = None
        self._Application = None
        self._TcpNum = None
        self._UdpNum = None
        self._Entity = None
        self._Share = None

    @property
    def ZoneId(self):
        """ID of the site (top-level domain name)
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PolicyId(self):
        """Policy ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Type(self):
        """Type of protected resource. Values: `domain` and `application`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EntityName(self):
        """Layer-4 proxy name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._EntityName

    @EntityName.setter
    def EntityName(self, EntityName):
        self._EntityName = EntityName

    @property
    def Application(self):
        """Layer-7 domain name parameters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of DDoSApplication
        """
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

    @property
    def TcpNum(self):
        """Number of layer-4 TCP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._TcpNum

    @TcpNum.setter
    def TcpNum(self, TcpNum):
        self._TcpNum = TcpNum

    @property
    def UdpNum(self):
        """Number of layer-4 UDP forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._UdpNum

    @UdpNum.setter
    def UdpNum(self, UdpNum):
        self._UdpNum = UdpNum

    @property
    def Entity(self):
        """Name of the protected resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Share(self):
        """Whether the shared resource is used. Values: `true` (yes) and `false` (no). The proxy mode cannot be switched when the shared resource is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Share

    @Share.setter
    def Share(self, Share):
        self._Share = Share


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PolicyId = params.get("PolicyId")
        self._Type = params.get("Type")
        self._EntityName = params.get("EntityName")
        if params.get("Application") is not None:
            self._Application = []
            for item in params.get("Application"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self._Application.append(obj)
        self._TcpNum = params.get("TcpNum")
        self._UdpNum = params.get("UdpNum")
        self._Entity = params.get("Entity")
        self._Share = params.get("Share")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """Smart acceleration configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable smart acceleration
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to enable smart acceleration
`on`: Enable
`off`: Disable
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """Pricing query parameter

    """

    def __init__(self):
        r"""
        :param _Key: Parameter key
        :type Key: str
        :param _Value: Parameter value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Parameter key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Parameter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    """Web security configuration switch

    """

    def __init__(self):
        r"""
        :param _WebSwitch: Switch that controls all web security configuration: basic web protection, custom rules, and rate limiting
        :type WebSwitch: str
        """
        self._WebSwitch = None

    @property
    def WebSwitch(self):
        """Switch that controls all web security configuration: basic web protection, custom rules, and rate limiting
        :rtype: str
        """
        return self._WebSwitch

    @WebSwitch.setter
    def WebSwitch(self, WebSwitch):
        self._WebSwitch = WebSwitch


    def _deserialize(self, params):
        self._WebSwitch = params.get("WebSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag configuration

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _Status: Status of the task
        :type Status: str
        :param _Target: Resource
        :type Target: str
        :param _Type: Task type
        :type Type: str
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _UpdateTime: Task completion time
        :type UpdateTime: str
        """
        self._JobId = None
        self._Status = None
        self._Target = None
        self._Type = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Status(self):
        """Status of the task
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Target(self):
        """Resource
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Type(self):
        """Task type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        """Task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Task completion time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Status = params.get("Status")
        self._Target = params.get("Target")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """Data items of the statistical curve

    """

    def __init__(self):
        r"""
        :param _Timestamp: Second-level timestamp
Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _Value: Value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: int
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        """Second-level timestamp
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        """Value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """Time series data of L7 data analysis

    """

    def __init__(self):
        r"""
        :param _TypeKey: Query dimension value
        :type TypeKey: str
        :param _TypeValue: Detailed time series data
Note: This field may return null, indicating that no valid values can be obtained.
        :type TypeValue: list of TimingTypeValue
        """
        self._TypeKey = None
        self._TypeValue = None

    @property
    def TypeKey(self):
        """Query dimension value
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def TypeValue(self):
        """Detailed time series data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingTypeValue
        """
        return self._TypeValue

    @TypeValue.setter
    def TypeValue(self, TypeValue):
        self._TypeValue = TypeValue


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self._TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self._TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """Detailed data of time series type

    """

    def __init__(self):
        r"""
        :param _Sum: Sum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sum: int
        :param _Max: Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: int
        :param _Avg: Average
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avg: int
        :param _MetricName: Metric name
        :type MetricName: str
        :param _DetailData: This field will be disused soon. Use the `Detail` field instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailData: list of int
        :param _Detail: Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        """
        self._Sum = None
        self._Max = None
        self._Avg = None
        self._MetricName = None
        self._DetailData = None
        self._Detail = None

    @property
    def Sum(self):
        """Sum
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum

    @property
    def Max(self):
        """Maximum
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        """Average
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def MetricName(self):
        """Metric name
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def DetailData(self):
        """This field will be disused soon. Use the `Detail` field instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData

    @property
    def Detail(self):
        """Detailed data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TimingDataItem
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Sum = params.get("Sum")
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._MetricName = params.get("MetricName")
        self._DetailData = params.get("DetailData")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """Top data of layer-7 data analysis

    """

    def __init__(self):
        r"""
        :param _TypeKey: Query dimension value
        :type TypeKey: str
        :param _DetailData: Top data rankings
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailData: list of TopDetailData
        """
        self._TypeKey = None
        self._DetailData = None

    @property
    def TypeKey(self):
        """Query dimension value
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def DetailData(self):
        """Top data rankings
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TopDetailData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """The structure used to sort the top data

    """

    def __init__(self):
        r"""
        :param _Key: Field name
        :type Key: str
        :param _Value: Field value
        :type Value: int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Field name
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Field value
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopNEntry(AbstractModel):
    """TopN entry

    """

    def __init__(self):
        r"""
        :param _Key: Entry key
        :type Key: str
        :param _Value: Top N data
        :type Value: list of TopNEntryValue
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Entry key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Top N data
        :rtype: list of TopNEntryValue
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = TopNEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopNEntryValue(AbstractModel):
    """Top N data entry

    """

    def __init__(self):
        r"""
        :param _Name: Entry name
        :type Name: str
        :param _Count: Quantity
        :type Count: int
        """
        self._Name = None
        self._Count = None

    @property
    def Name(self):
        """Entry name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        """Quantity
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """HTTP2 origin-pull configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HTTP2 origin-pull
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Whether to enable HTTP2 origin-pull
`on`: Enable
`off`: Disable
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """Custom name servers

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the custom name server
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _Servers: List of custom name servers
        :type Servers: list of str
        """
        self._Switch = None
        self._Servers = None

    @property
    def Switch(self):
        """Whether to enable the custom name server
`on`: Enable
`off`: Disable
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Servers(self):
        """List of custom name servers
        :rtype: list of str
        """
        return self._Servers

    @Servers.setter
    def Servers(self, Servers):
        self._Servers = Servers


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """IP of the custom name server

    """

    def __init__(self):
        r"""
        :param _Name: Name of the custom name server
        :type Name: str
        :param _IPv4: IPv4 address of the custom name server
        :type IPv4: str
        """
        self._Name = None
        self._IPv4 = None

    @property
    def Name(self):
        """Name of the custom name server
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IPv4(self):
        """IPv4 address of the custom name server
        :rtype: str
        """
        return self._IPv4

    @IPv4.setter
    def IPv4(self, IPv4):
        self._IPv4 = IPv4


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafConfig(AbstractModel):
    """WAF configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch
        :type Switch: str
        :param _Level: Protection level: `loose`, `normal`, `strict`, `stricter`, `custom`
        :type Level: str
        :param _Mode: Mode: `block`, `observe`, `close`
        :type Mode: str
        :param _WafRules: WAF rule allowlist/blocklist
        :type WafRules: :class:`tencentcloud.teo.v20220106.models.WafRule`
        :param _AiRule: AI rule engine
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AiRule: :class:`tencentcloud.teo.v20220106.models.AiRule`
        """
        self._Switch = None
        self._Level = None
        self._Mode = None
        self._WafRules = None
        self._AiRule = None

    @property
    def Switch(self):
        """Switch
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Level(self):
        """Protection level: `loose`, `normal`, `strict`, `stricter`, `custom`
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Mode(self):
        """Mode: `block`, `observe`, `close`
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def WafRules(self):
        """WAF rule allowlist/blocklist
        :rtype: :class:`tencentcloud.teo.v20220106.models.WafRule`
        """
        return self._WafRules

    @WafRules.setter
    def WafRules(self, WafRules):
        self._WafRules = WafRules

    @property
    def AiRule(self):
        """AI rule engine
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.teo.v20220106.models.AiRule`
        """
        return self._AiRule

    @AiRule.setter
    def AiRule(self, AiRule):
        self._AiRule = AiRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Level = params.get("Level")
        self._Mode = params.get("Mode")
        if params.get("WafRules") is not None:
            self._WafRules = WafRule()
            self._WafRules._deserialize(params.get("WafRules"))
        if params.get("AiRule") is not None:
            self._AiRule = AiRule()
            self._AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRule(AbstractModel):
    """WAF rule

    """

    def __init__(self):
        r"""
        :param _BlockRuleIDs: Blocklist
        :type BlockRuleIDs: list of int
        :param _Switch: Whether the WAF rule is enabled or disabled
        :type Switch: str
        :param _ObserveRuleIDs: Observe mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ObserveRuleIDs: list of int
        """
        self._BlockRuleIDs = None
        self._Switch = None
        self._ObserveRuleIDs = None

    @property
    def BlockRuleIDs(self):
        """Blocklist
        :rtype: list of int
        """
        return self._BlockRuleIDs

    @BlockRuleIDs.setter
    def BlockRuleIDs(self, BlockRuleIDs):
        self._BlockRuleIDs = BlockRuleIDs

    @property
    def Switch(self):
        """Whether the WAF rule is enabled or disabled
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ObserveRuleIDs(self):
        """Observe mode
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of int
        """
        return self._ObserveRuleIDs

    @ObserveRuleIDs.setter
    def ObserveRuleIDs(self, ObserveRuleIDs):
        self._ObserveRuleIDs = ObserveRuleIDs


    def _deserialize(self, params):
        self._BlockRuleIDs = params.get("BlockRuleIDs")
        self._Switch = params.get("Switch")
        self._ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebAttackEvent(AbstractModel):
    """Web block event

    """

    def __init__(self):
        r"""
        :param _ClientIp: Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIp: str
        :param _AttackUrl: Attack URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackUrl: str
        :param _AttackTime: Attack time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        """
        self._ClientIp = None
        self._AttackUrl = None
        self._AttackTime = None

    @property
    def ClientIp(self):
        """Client IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def AttackUrl(self):
        """Attack URL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackUrl

    @AttackUrl.setter
    def AttackUrl(self, AttackUrl):
        self._AttackUrl = AttackUrl

    @property
    def AttackTime(self):
        """Attack time in seconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._AttackUrl = params.get("AttackUrl")
        self._AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebEventData(AbstractModel):
    """Web event data

    """

    def __init__(self):
        r"""
        :param _List: Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of WebAttackEvent
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data set of attack events
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of WebAttackEvent
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = WebAttackEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogData(AbstractModel):
    """Web attack log data

    """

    def __init__(self):
        r"""
        :param _List: Data
Note: This field may return null, indicating that no valid values can be obtained.
        :type List: list of WebLogs
        :param _PageNo: Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: int
        :param _PageSize: Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _Pages: Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pages: int
        :param _TotalSize: Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._List = None
        self._PageNo = None
        self._PageSize = None
        self._Pages = None
        self._TotalSize = None

    @property
    def List(self):
        """Data
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of WebLogs
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def PageNo(self):
        """Current page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Number of items per page
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Pages(self):
        """Total number of pages
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def TotalSize(self):
        """Total number of items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = WebLogs()
                obj._deserialize(item)
                self._List.append(obj)
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Pages = params.get("Pages")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogs(AbstractModel):
    """Web attack log

    """

    def __init__(self):
        r"""
        :param _AttackContent: Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param _AttackIp: Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackIp: str
        :param _AttackType: Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param _Domain: Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Msuuid: uuid
Note: This field may return null, indicating that no valid values can be obtained.
        :type Msuuid: str
        :param _RequestMethod: Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestMethod: str
        :param _RequestUri: Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUri: str
        :param _RiskLevel: Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param _RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param _SipCountryCode: IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :type SipCountryCode: str
        :param _EventId: Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        :param _DisposalMethod: Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param _HttpLog: http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param _Ua: user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ua: str
        :param _AttackTime: Attack time. For consistency considerations, the original parameter `time` was renamed `AttackTime`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackTime: int
        """
        self._AttackContent = None
        self._AttackIp = None
        self._AttackType = None
        self._Domain = None
        self._Msuuid = None
        self._RequestMethod = None
        self._RequestUri = None
        self._RiskLevel = None
        self._RuleId = None
        self._SipCountryCode = None
        self._EventId = None
        self._DisposalMethod = None
        self._HttpLog = None
        self._Ua = None
        self._AttackTime = None

    @property
    def AttackContent(self):
        """Attack content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackContent

    @AttackContent.setter
    def AttackContent(self, AttackContent):
        self._AttackContent = AttackContent

    @property
    def AttackIp(self):
        """Attack IP
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackIp

    @AttackIp.setter
    def AttackIp(self, AttackIp):
        self._AttackIp = AttackIp

    @property
    def AttackType(self):
        """Attack type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Domain(self):
        """Domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Msuuid(self):
        """uuid
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msuuid

    @Msuuid.setter
    def Msuuid(self, Msuuid):
        self._Msuuid = Msuuid

    @property
    def RequestMethod(self):
        """Request method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestMethod

    @RequestMethod.setter
    def RequestMethod(self, RequestMethod):
        self._RequestMethod = RequestMethod

    @property
    def RequestUri(self):
        """Request URI
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestUri

    @RequestUri.setter
    def RequestUri(self, RequestUri):
        self._RequestUri = RequestUri

    @property
    def RiskLevel(self):
        """Risk grade
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RuleId(self):
        """Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def SipCountryCode(self):
        """IP country/region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SipCountryCode

    @SipCountryCode.setter
    def SipCountryCode(self, SipCountryCode):
        self._SipCountryCode = SipCountryCode

    @property
    def EventId(self):
        """Event ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DisposalMethod(self):
        """Processing method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DisposalMethod

    @DisposalMethod.setter
    def DisposalMethod(self, DisposalMethod):
        self._DisposalMethod = DisposalMethod

    @property
    def HttpLog(self):
        """http_log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HttpLog

    @HttpLog.setter
    def HttpLog(self, HttpLog):
        self._HttpLog = HttpLog

    @property
    def Ua(self):
        """user agent
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ua

    @Ua.setter
    def Ua(self, Ua):
        self._Ua = Ua

    @property
    def AttackTime(self):
        """Attack time. For consistency considerations, the original parameter `time` was renamed `AttackTime`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime


    def _deserialize(self, params):
        self._AttackContent = params.get("AttackContent")
        self._AttackIp = params.get("AttackIp")
        self._AttackType = params.get("AttackType")
        self._Domain = params.get("Domain")
        self._Msuuid = params.get("Msuuid")
        self._RequestMethod = params.get("RequestMethod")
        self._RequestUri = params.get("RequestUri")
        self._RiskLevel = params.get("RiskLevel")
        self._RuleId = params.get("RuleId")
        self._SipCountryCode = params.get("SipCountryCode")
        self._EventId = params.get("EventId")
        self._DisposalMethod = params.get("DisposalMethod")
        self._HttpLog = params.get("HttpLog")
        self._Ua = params.get("Ua")
        self._AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable custom WebSocket timeout setting. When it’s `off`: it means to keep the default WebSocket connection timeout period, which is 15 seconds. To change the timeout period, please set it to `on`.
        :type Switch: str
        :param _Timeout: Sets timeout period in seconds. Maximum value: 120
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        """Whether to enable custom WebSocket timeout setting. When it’s `off`: it means to keep the default WebSocket connection timeout period, which is 15 seconds. To change the timeout period, please set it to `on`.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        """Sets timeout period in seconds. Maximum value: 120
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """Site information

    """

    def __init__(self):
        r"""
        :param _Id: Site ID
        :type Id: str
        :param _Name: Site name
        :type Name: str
        :param _OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param _NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param _Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param _Type: How the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param _Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param _CnameSpeedUp: Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
Note: This field may return null, indicating that no valid values can be obtained.
        :type CnameSpeedUp: str
        :param _CnameStatus: Ownership verification status of the site when it is connected to EdgeOne via CNAME.
- `finished`: The site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param _Tags: Resource tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        :param _Resources: Billable resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Resources: list of Resource
        :param _CreatedOn: Site creation date
        :type CreatedOn: str
        :param _ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param _Area: 
        :type Area: str
        """
        self._Id = None
        self._Name = None
        self._OriginalNameServers = None
        self._NameServers = None
        self._Status = None
        self._Type = None
        self._Paused = None
        self._CnameSpeedUp = None
        self._CnameStatus = None
        self._Tags = None
        self._Resources = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._Area = None

    @property
    def Id(self):
        """Site ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Site name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginalNameServers(self):
        """List of name servers used by the site
        :rtype: list of str
        """
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def NameServers(self):
        """List of name servers assigned by Tencent Cloud
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def Status(self):
        """Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """How the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Paused(self):
        """Indicates whether the site is disabled
        :rtype: bool
        """
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def CnameSpeedUp(self):
        """Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CnameSpeedUp

    @CnameSpeedUp.setter
    def CnameSpeedUp(self, CnameSpeedUp):
        self._CnameSpeedUp = CnameSpeedUp

    @property
    def CnameStatus(self):
        """Ownership verification status of the site when it is connected to EdgeOne via CNAME.
- `finished`: The site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def Tags(self):
        """Resource tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Resources(self):
        """Billable resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of Resource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def CreatedOn(self):
        """Site creation date
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        """Site modification date
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def Area(self):
        """
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._NameServers = params.get("NameServers")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Paused = params.get("Paused")
        self._CnameSpeedUp = params.get("CnameSpeedUp")
        self._CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """Site query filter

    """

    def __init__(self):
        r"""
        :param _Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
- `tagKey`: Tag key.
- `tagValue`: Tag value.
        :type Name: str
        :param _Values: Filters by the field value
        :type Values: list of str
        :param _Fuzzy: Specifies whether to enable fuzzy query. It’s only available when filter name is `name`. If it’s enabled, the length of `Values` must be 1.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        """Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
- `tagKey`: Tag key.
- `tagValue`: Tag value.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filters by the field value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        """Specifies whether to enable fuzzy query. It’s only available when filter name is `name`. If it’s enabled, the length of `Values` must be 1.
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        