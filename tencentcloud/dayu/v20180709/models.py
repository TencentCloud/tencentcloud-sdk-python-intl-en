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


class BaradData(AbstractModel):
    """Data returned by Barad

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name (connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;)
        :type MetricName: str
        :param _Data: Value array
        :type Data: list of float
        :param _Count: Value array size
        :type Count: int
        """
        self._MetricName = None
        self._Data = None
        self._Count = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """IP object bound to Anti-DDoS Pro

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _BizType: Category of product that can be bound. Valid values: public (CVM and CLB), bm (BM), eni (ENI), vpngw (VPN gateway), natgw (NAT gateway), waf (WAF), fpc (financial products), gaap (GAAP), and other (Hosted IP).
        :type BizType: str
        :param _DeviceType: Subtype under product type. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param _InstanceId: Resource instance ID of IP. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`; if it is a hosted IP without corresponding resource instance ID, enter "none";
        :type InstanceId: str
        """
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCAlarmThreshold(AbstractModel):
    """CC alarm threshold

    """

    def __init__(self):
        r"""
        :param _AlarmThreshold: CC alarm threshold
        :type AlarmThreshold: int
        """
        self._AlarmThreshold = None

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCEventRecord(AbstractModel):
    """CC attack event record

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Vip: Resource IP
        :type Vip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _ReqQps: Total requests peak (QPS)
        :type ReqQps: int
        :param _DropQps: Attack peak (QPS)
        :type DropQps: int
        :param _AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]
        :type AttackStatus: int
        :param _ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param _DomainList: Domain name list
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainList: str
        :param _UriList: URI list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UriList: str
        :param _AttackipList: Attack source list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttackipList: str
        """
        self._Business = None
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._ReqQps = None
        self._DropQps = None
        self._AttackStatus = None
        self._ResourceName = None
        self._DomainList = None
        self._UriList = None
        self._AttackipList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReqQps(self):
        return self._ReqQps

    @ReqQps.setter
    def ReqQps(self, ReqQps):
        self._ReqQps = ReqQps

    @property
    def DropQps(self):
        return self._DropQps

    @DropQps.setter
    def DropQps(self, DropQps):
        self._DropQps = DropQps

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def UriList(self):
        return self._UriList

    @UriList.setter
    def UriList(self, UriList):
        self._UriList = UriList

    @property
    def AttackipList(self):
        return self._AttackipList

    @AttackipList.setter
    def AttackipList(self, AttackipList):
        self._AttackipList = AttackipList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReqQps = params.get("ReqQps")
        self._DropQps = params.get("DropQps")
        self._AttackStatus = params.get("AttackStatus")
        self._ResourceName = params.get("ResourceName")
        self._DomainList = params.get("DomainList")
        self._UriList = params.get("UriList")
        self._AttackipList = params.get("AttackipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCFrequencyRule(AbstractModel):
    """Access frequency control rule for CC protection

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleId: ID of the access frequency control rule for CC protection
        :type CCFrequencyRuleId: str
        :param _Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param _UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param _Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        :param _Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param _Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param _ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param _Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param _ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        """
        self._CCFrequencyRuleId = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration


    def _deserialize(self, params):
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPolicy(AbstractModel):
    """Custom CC protection rule

    """

    def __init__(self):
        r"""
        :param _Name: Policy name
        :type Name: str
        :param _Smode: Matching mode. Valid values: [matching (matching mode), speedlimit (speed limiting mode)]
        :type Smode: str
        :param _SetId: Policy ID
        :type SetId: str
        :param _Frequency: Number of requests allowed per minute
        :type Frequency: int
        :param _ExeMode: Executed policy mode. Valid values: [alg (verification code), drop (blocking)]
        :type ExeMode: str
        :param _Switch: Specifies whether the policy is activated
        :type Switch: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _RuleList: Rule list
        :type RuleList: list of CCRule
        :param _IpList: IP list. If this field is to be left empty, please pass in an empty instead of null;
        :type IpList: list of str
        :param _Protocol: CC protection type. Valid values: [http, https]
        :type Protocol: str
        :param _RuleId: ID of the forwarding rule corresponding to the HTTPS CC protection domain name
        :type RuleId: str
        :param _Domain: HTTPS CC protection domain name
        :type Domain: str
        """
        self._Name = None
        self._Smode = None
        self._SetId = None
        self._Frequency = None
        self._ExeMode = None
        self._Switch = None
        self._CreateTime = None
        self._RuleList = None
        self._IpList = None
        self._Protocol = None
        self._RuleId = None
        self._Domain = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Smode(self):
        return self._Smode

    @Smode.setter
    def Smode(self, Smode):
        self._Smode = Smode

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def ExeMode(self):
        return self._ExeMode

    @ExeMode.setter
    def ExeMode(self, ExeMode):
        self._ExeMode = ExeMode

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Smode = params.get("Smode")
        self._SetId = params.get("SetId")
        self._Frequency = params.get("Frequency")
        self._ExeMode = params.get("ExeMode")
        self._Switch = params.get("Switch")
        self._CreateTime = params.get("CreateTime")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = CCRule()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._IpList = params.get("IpList")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRule(AbstractModel):
    """The custom CC protection policy in key-value format

    """

    def __init__(self):
        r"""
        :param _Skey: Key of the policy. Valid values: `host`, `cgi`, `ua`, `referer`
        :type Skey: str
        :param _Operator: Rule condition. Valid values: `include`, `not_include`, `equal`
        :type Operator: str
        :param _Value: Value of the policy. Length limit: 31 bytes
        :type Value: str
        """
        self._Skey = None
        self._Operator = None
        self._Value = None

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Skey = params.get("Skey")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleConfig(AbstractModel):
    """Custom layer-7 CC policy

    """

    def __init__(self):
        r"""
        :param _Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param _ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param _Action: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Action: str
        :param _ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        """
        self._Period = None
        self._ReqNumber = None
        self._Action = None
        self._ExeDuration = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Action = params.get("Action")
        self._ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`basic`: Anti-DDoS Basic)
        :type Business: str
        :param _Method: `get`: read alarm threshold, `set`: set alarm threshold
        :type Method: str
        :param _AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is required if `Method` is `set`;
        :type AlarmType: int
        :param _AlarmThreshold: Alarm threshold. It is required if `Method` is `set`. If it is set to 0, it means to clear the alarm threshold configuration;
        :type AlarmThreshold: int
        """
        self._Business = None
        self._Method = None
        self._AlarmType = None
        self._AlarmThreshold = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Method = params.get("Method")
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmThreshold: If there is an alarm threshold configuration, the returned alarm threshold will be greater than 0; otherwise, the returned alarm threshold will be 0;
        :type AlarmThreshold: int
        :param _AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is valid if `AlarmThreshold` is above 0;
        :type AlarmType: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmThreshold = None
        self._AlarmType = None
        self._RequestId = None

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._AlarmType = params.get("AlarmType")
        self._RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _BoundDevList: Array of IPs to be bound to the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP. If there are no IPs to bind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;
        :type BoundDevList: list of BoundIpInfo
        :param _UnBoundDevList: Array of IPs to be unbound from Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP; if there are no IPs to unbind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;
        :type UnBoundDevList: list of BoundIpInfo
        :param _CopyPolicy: [Disused]
        :type CopyPolicy: str
        """
        self._Business = None
        self._Id = None
        self._BoundDevList = None
        self._UnBoundDevList = None
        self._CopyPolicy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BoundDevList(self):
        return self._BoundDevList

    @BoundDevList.setter
    def BoundDevList(self, BoundDevList):
        self._BoundDevList = BoundDevList

    @property
    def UnBoundDevList(self):
        return self._UnBoundDevList

    @UnBoundDevList.setter
    def UnBoundDevList(self, UnBoundDevList):
        self._UnBoundDevList = UnBoundDevList

    @property
    def CopyPolicy(self):
        return self._CopyPolicy

    @CopyPolicy.setter
    def CopyPolicy(self, CopyPolicy):
        self._CopyPolicy = CopyPolicy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self._BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self._UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._UnBoundDevList.append(obj)
        self._CopyPolicy = params.get("CopyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateCCFrequencyRulesRequest(AbstractModel):
    """CreateCCFrequencyRules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API
        :type RuleId: str
        :param _Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param _Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param _ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param _Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param _ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        :param _Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param _UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param _Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules response structure.

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleId: Access frequency control rule ID for CC protection
        :type CCFrequencyRuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CCFrequencyRuleId = None
        self._RequestId = None

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._RequestId = params.get("RequestId")


class CreateCCSelfDefinePolicyRequest(AbstractModel):
    """CreateCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Policy: Details of the CC protection policy
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self._Business = None
        self._Id = None
        self._Policy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Policy") is not None:
            self._Policy = CCPolicy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateDDoSPolicyCaseRequest(AbstractModel):
    """CreateDDoSPolicyCase request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _CaseName: Policy scenario name string. Length limit: 64
        :type CaseName: str
        :param _PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]
        :type PlatformTypes: list of str
        :param _AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]
        :type AppType: str
        :param _AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]
        :type AppProtocols: list of str
        :param _TcpSportStart: TCP start port. Value range: (0, 65535]
        :type TcpSportStart: str
        :param _TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port.
        :type TcpSportEnd: str
        :param _UdpSportStart: UDP start port. Value range: (0, 65535]
        :type UdpSportStart: str
        :param _UdpSportEnd: UDP end port. Value range: (0, 65535). It must be greater than or equal to the UDP start port.
        :type UdpSportEnd: str
        :param _HasAbroad: Whether there are customers outside China. Valid values: [no, yes]
        :type HasAbroad: str
        :param _HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]
        :type HasInitiateTcp: str
        :param _HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]
        :type HasInitiateUdp: str
        :param _PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]
        :type PeerTcpPort: str
        :param _PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]
        :type PeerUdpPort: str
        :param _TcpFootprint: Fixed feature code of TCP payload. Max string length: 512
        :type TcpFootprint: str
        :param _UdpFootprint: Fixed feature code of UDP payload. Max string length: 512
        :type UdpFootprint: str
        :param _WebApiUrl: Web application API URL
        :type WebApiUrl: list of str
        :param _MinTcpPackageLen: Minimum length of TCP packet. Value range: (0, 1500)
        :type MinTcpPackageLen: str
        :param _MaxTcpPackageLen: Maximum length of TCP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP packet
        :type MaxTcpPackageLen: str
        :param _MinUdpPackageLen: Minimum length of UDP packet. Value range: (0, 1500)
        :type MinUdpPackageLen: str
        :param _MaxUdpPackageLen: Maximum length of UDP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP packet
        :type MaxUdpPackageLen: str
        :param _HasVPN: Whether there are applications using VPN. Valid values: [no, yes]
        :type HasVPN: str
        :param _TcpPortList: TCP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.
        :type TcpPortList: str
        :param _UdpPortList: UDP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.
        :type UdpPortList: str
        """
        self._Business = None
        self._CaseName = None
        self._PlatformTypes = None
        self._AppType = None
        self._AppProtocols = None
        self._TcpSportStart = None
        self._TcpSportEnd = None
        self._UdpSportStart = None
        self._UdpSportEnd = None
        self._HasAbroad = None
        self._HasInitiateTcp = None
        self._HasInitiateUdp = None
        self._PeerTcpPort = None
        self._PeerUdpPort = None
        self._TcpFootprint = None
        self._UdpFootprint = None
        self._WebApiUrl = None
        self._MinTcpPackageLen = None
        self._MaxTcpPackageLen = None
        self._MinUdpPackageLen = None
        self._MaxUdpPackageLen = None
        self._HasVPN = None
        self._TcpPortList = None
        self._UdpPortList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CaseName(self):
        return self._CaseName

    @CaseName.setter
    def CaseName(self, CaseName):
        self._CaseName = CaseName

    @property
    def PlatformTypes(self):
        return self._PlatformTypes

    @PlatformTypes.setter
    def PlatformTypes(self, PlatformTypes):
        self._PlatformTypes = PlatformTypes

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppProtocols(self):
        return self._AppProtocols

    @AppProtocols.setter
    def AppProtocols(self, AppProtocols):
        self._AppProtocols = AppProtocols

    @property
    def TcpSportStart(self):
        return self._TcpSportStart

    @TcpSportStart.setter
    def TcpSportStart(self, TcpSportStart):
        self._TcpSportStart = TcpSportStart

    @property
    def TcpSportEnd(self):
        return self._TcpSportEnd

    @TcpSportEnd.setter
    def TcpSportEnd(self, TcpSportEnd):
        self._TcpSportEnd = TcpSportEnd

    @property
    def UdpSportStart(self):
        return self._UdpSportStart

    @UdpSportStart.setter
    def UdpSportStart(self, UdpSportStart):
        self._UdpSportStart = UdpSportStart

    @property
    def UdpSportEnd(self):
        return self._UdpSportEnd

    @UdpSportEnd.setter
    def UdpSportEnd(self, UdpSportEnd):
        self._UdpSportEnd = UdpSportEnd

    @property
    def HasAbroad(self):
        return self._HasAbroad

    @HasAbroad.setter
    def HasAbroad(self, HasAbroad):
        self._HasAbroad = HasAbroad

    @property
    def HasInitiateTcp(self):
        return self._HasInitiateTcp

    @HasInitiateTcp.setter
    def HasInitiateTcp(self, HasInitiateTcp):
        self._HasInitiateTcp = HasInitiateTcp

    @property
    def HasInitiateUdp(self):
        return self._HasInitiateUdp

    @HasInitiateUdp.setter
    def HasInitiateUdp(self, HasInitiateUdp):
        self._HasInitiateUdp = HasInitiateUdp

    @property
    def PeerTcpPort(self):
        return self._PeerTcpPort

    @PeerTcpPort.setter
    def PeerTcpPort(self, PeerTcpPort):
        self._PeerTcpPort = PeerTcpPort

    @property
    def PeerUdpPort(self):
        return self._PeerUdpPort

    @PeerUdpPort.setter
    def PeerUdpPort(self, PeerUdpPort):
        self._PeerUdpPort = PeerUdpPort

    @property
    def TcpFootprint(self):
        return self._TcpFootprint

    @TcpFootprint.setter
    def TcpFootprint(self, TcpFootprint):
        self._TcpFootprint = TcpFootprint

    @property
    def UdpFootprint(self):
        return self._UdpFootprint

    @UdpFootprint.setter
    def UdpFootprint(self, UdpFootprint):
        self._UdpFootprint = UdpFootprint

    @property
    def WebApiUrl(self):
        return self._WebApiUrl

    @WebApiUrl.setter
    def WebApiUrl(self, WebApiUrl):
        self._WebApiUrl = WebApiUrl

    @property
    def MinTcpPackageLen(self):
        return self._MinTcpPackageLen

    @MinTcpPackageLen.setter
    def MinTcpPackageLen(self, MinTcpPackageLen):
        self._MinTcpPackageLen = MinTcpPackageLen

    @property
    def MaxTcpPackageLen(self):
        return self._MaxTcpPackageLen

    @MaxTcpPackageLen.setter
    def MaxTcpPackageLen(self, MaxTcpPackageLen):
        self._MaxTcpPackageLen = MaxTcpPackageLen

    @property
    def MinUdpPackageLen(self):
        return self._MinUdpPackageLen

    @MinUdpPackageLen.setter
    def MinUdpPackageLen(self, MinUdpPackageLen):
        self._MinUdpPackageLen = MinUdpPackageLen

    @property
    def MaxUdpPackageLen(self):
        return self._MaxUdpPackageLen

    @MaxUdpPackageLen.setter
    def MaxUdpPackageLen(self, MaxUdpPackageLen):
        self._MaxUdpPackageLen = MaxUdpPackageLen

    @property
    def HasVPN(self):
        return self._HasVPN

    @HasVPN.setter
    def HasVPN(self, HasVPN):
        self._HasVPN = HasVPN

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CaseName = params.get("CaseName")
        self._PlatformTypes = params.get("PlatformTypes")
        self._AppType = params.get("AppType")
        self._AppProtocols = params.get("AppProtocols")
        self._TcpSportStart = params.get("TcpSportStart")
        self._TcpSportEnd = params.get("TcpSportEnd")
        self._UdpSportStart = params.get("UdpSportStart")
        self._UdpSportEnd = params.get("UdpSportEnd")
        self._HasAbroad = params.get("HasAbroad")
        self._HasInitiateTcp = params.get("HasInitiateTcp")
        self._HasInitiateUdp = params.get("HasInitiateUdp")
        self._PeerTcpPort = params.get("PeerTcpPort")
        self._PeerUdpPort = params.get("PeerUdpPort")
        self._TcpFootprint = params.get("TcpFootprint")
        self._UdpFootprint = params.get("UdpFootprint")
        self._WebApiUrl = params.get("WebApiUrl")
        self._MinTcpPackageLen = params.get("MinTcpPackageLen")
        self._MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self._MinUdpPackageLen = params.get("MinUdpPackageLen")
        self._MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self._HasVPN = params.get("HasVPN")
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase response structure.

    """

    def __init__(self):
        r"""
        :param _SceneId: Policy scenario ID
        :type SceneId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SceneId = None
        self._RequestId = None

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._RequestId = params.get("RequestId")


class CreateDDoSPolicyRequest(AbstractModel):
    """CreateDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _DropOptions: Protocol disablement, which must be entered, and the array length must be 1
        :type DropOptions: list of DDoSPolicyDropOption
        :param _Name: Policy name
        :type Name: str
        :param _PortLimits: Ports to be closed. If no ports are to be closed, enter an empty array
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _IpAllowDenys: Request source IP blocklist/allowlist, which should be an empty array if there are no blocked or allowed IPs.
        :type IpAllowDenys: list of IpBlackWhite
        :param _PacketFilters: Packet filter. Enter an empty array if there are no packets to filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _WaterPrint: Watermarking policy parameters. Enter an empty array if the watermarking feature is not enabled. Only one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)
        :type WaterPrint: list of WaterPrintPolicy
        """
        self._Business = None
        self._DropOptions = None
        self._Name = None
        self._PortLimits = None
        self._IpAllowDenys = None
        self._PacketFilters = None
        self._WaterPrint = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def IpAllowDenys(self):
        return self._IpAllowDenys

    @IpAllowDenys.setter
    def IpAllowDenys(self, IpAllowDenys):
        self._IpAllowDenys = IpAllowDenys

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint


    def _deserialize(self, params):
        self._Business = params.get("Business")
        if params.get("DropOptions") is not None:
            self._DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self._DropOptions.append(obj)
        self._Name = params.get("Name")
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self._IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateInstanceNameRequest(AbstractModel):
    """CreateInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Name: Instance name. Length limit: 32 characters
        :type Name: str
        """
        self._Business = None
        self._Id = None
        self._Name = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL4HealthConfigRequest(AbstractModel):
    """CreateL4HealthConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _HealthConfig: Layer-4 health check configuration array
        :type HealthConfig: list of L4HealthConfig
        """
        self._Business = None
        self._Id = None
        self._HealthConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL4RulesRequest(AbstractModel):
    """CreateL4Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Rules: Rule list
        :type Rules: list of L4RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7CCRuleRequest(AbstractModel):
    """CreateL7CCRule request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Method: Operation. Valid values: [query (query), add (add), del (delete)]
        :type Method: str
        :param _RuleId: Layer-7 forwarding rule ID, such as rule-0000001
        :type RuleId: str
        :param _RuleConfig: Custom layer-7 CC protection rule. If the `Method` is `query`, this field can be left empty; if the `Method` is `add` or `del`, it is required, and the array length can only be 1;
        :type RuleConfig: list of CCRuleConfig
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._RuleId = None
        self._RuleConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleConfig(self):
        return self._RuleConfig

    @RuleConfig.setter
    def RuleConfig(self, RuleConfig):
        self._RuleConfig = RuleConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._RuleId = params.get("RuleId")
        if params.get("RuleConfig") is not None:
            self._RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self._RuleConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleConfig: Custom layer-7 CC protection rule parameters. If custom CC protection rule is not enabled, an empty array will be returned.
        :type RuleConfig: list of CCRuleConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleConfig = None
        self._RequestId = None

    @property
    def RuleConfig(self):
        return self._RuleConfig

    @RuleConfig.setter
    def RuleConfig(self, RuleConfig):
        self._RuleConfig = RuleConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleConfig") is not None:
            self._RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self._RuleConfig.append(obj)
        self._RequestId = params.get("RequestId")


class CreateL7HealthConfigRequest(AbstractModel):
    """CreateL7HealthConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _HealthConfig: Layer-7 health check configuration array
        :type HealthConfig: list of L7HealthConfig
        """
        self._Business = None
        self._Id = None
        self._HealthConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RuleCertRequest(AbstractModel):
    """CreateL7RuleCert request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: The resource instance ID, such as the ID of an Anti-DDoS Advanced instance or the ID of an Anti-DDoS Ultimate instance.
        :type Id: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _CertType: Certificate type, which is required if the protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]
        :type CertType: int
        :param _SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID.
        :type SSLId: str
        :param _Cert: [Disused] If the certificate is an external certificate, this field must be entered with the certificate content. 
        :type Cert: str
        :param _PrivateKey: [Disused] If the certificate is an external certificate, this field must be entered with the certificate key. 
        :type PrivateKey: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Rules: Rule list
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RulesUploadRequest(AbstractModel):
    """CreateL7RulesUpload request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Rules: Rule list
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateNetReturnRequest(AbstractModel):
    """CreateNetReturn request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateNewL7RulesUploadRequest(AbstractModel):
    """CreateNewL7RulesUpload request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param _IdList: Resource ID list.
        :type IdList: list of str
        :param _VipList: Resource IP address list.
        :type VipList: list of str
        :param _Rules: Rule list.
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._IdList = None
        self._VipList = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesUploadResponse(AbstractModel):
    """CreateNewL7RulesUpload response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateUnblockIpRequest(AbstractModel):
    """CreateUnblockIp request structure.

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self._Ip = None
        self._ActionType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp response structure.

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        :param _UnblockTime: Unblocked time (estimated)
        :type UnblockTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ip = None
        self._ActionType = None
        self._UnblockTime = None
        self._RequestId = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def UnblockTime(self):
        return self._UnblockTime

    @UnblockTime.setter
    def UnblockTime(self, UnblockTime):
        self._UnblockTime = UnblockTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActionType = params.get("ActionType")
        self._UnblockTime = params.get("UnblockTime")
        self._RequestId = params.get("RequestId")


class DDoSAlarmThreshold(AbstractModel):
    """DDoS alarm threshold

    """

    def __init__(self):
        r"""
        :param _AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic
        :type AlarmType: int
        :param _AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)
        :type AlarmThreshold: int
        """
        self._AlarmType = None
        self._AlarmThreshold = None

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceRecord(AbstractModel):
    """Attack source information

    """

    def __init__(self):
        r"""
        :param _SrcIp: Attack source IP
        :type SrcIp: str
        :param _Province: Province (valid for Mainland China)
        :type Province: str
        :param _Nation: Country/region
        :type Nation: str
        :param _PacketSum: Total number of attack packets
        :type PacketSum: int
        :param _PacketLen: Total attack traffic
        :type PacketLen: int
        """
        self._SrcIp = None
        self._Province = None
        self._Nation = None
        self._PacketSum = None
        self._PacketLen = None

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def PacketSum(self):
        return self._PacketSum

    @PacketSum.setter
    def PacketSum(self, PacketSum):
        self._PacketSum = PacketSum

    @property
    def PacketLen(self):
        return self._PacketLen

    @PacketLen.setter
    def PacketLen(self, PacketLen):
        self._PacketLen = PacketLen


    def _deserialize(self, params):
        self._SrcIp = params.get("SrcIp")
        self._Province = params.get("Province")
        self._Nation = params.get("Nation")
        self._PacketSum = params.get("PacketSum")
        self._PacketLen = params.get("PacketLen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSEventRecord(AbstractModel):
    """DDoS attack event record

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Vip: Resource IP
        :type Vip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _Mbps: Maximum attack bandwidth
        :type Mbps: int
        :param _Pps: Maximum attack packet rate
        :type Pps: int
        :param _AttackType: Attack type
        :type AttackType: str
        :param _BlockFlag: Whether the IP is blocked. Valid values: [1 (yes), 0 (no), 2 (invalid value)]
        :type BlockFlag: int
        :param _OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes (yes), no (no), empty string (unknown value)]
        :type OverLoad: str
        :param _AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]
        :type AttackStatus: int
        :param _ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param _EventId: Attack event ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        """
        self._Business = None
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._Mbps = None
        self._Pps = None
        self._AttackType = None
        self._BlockFlag = None
        self._OverLoad = None
        self._AttackStatus = None
        self._ResourceName = None
        self._EventId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def BlockFlag(self):
        return self._BlockFlag

    @BlockFlag.setter
    def BlockFlag(self, BlockFlag):
        self._BlockFlag = BlockFlag

    @property
    def OverLoad(self):
        return self._OverLoad

    @OverLoad.setter
    def OverLoad(self, OverLoad):
        self._OverLoad = OverLoad

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._AttackType = params.get("AttackType")
        self._BlockFlag = params.get("BlockFlag")
        self._OverLoad = params.get("OverLoad")
        self._AttackStatus = params.get("AttackStatus")
        self._ResourceName = params.get("ResourceName")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyDropOption(AbstractModel):
    """Disabled protocol in advanced DDoS policy

    """

    def __init__(self):
        r"""
        :param _DropTcp: Blocks all TCP traffic. Valid values: [0,1]
        :type DropTcp: int
        :param _DropUdp: Blocks all UDP traffic. Valid values: [0,1]
        :type DropUdp: int
        :param _DropIcmp: Blocks all ICMP traffic. Valid values: [0,1]
        :type DropIcmp: int
        :param _DropOther: Blocks traffic of other protocols. Valid values: [0,1]
        :type DropOther: int
        :param _DropAbroad: Rejects traffic from outside Mainland China. Valid values: [0,1]
        :type DropAbroad: int
        :param _CheckSyncConn: Null session protection. Valid values: [0,1]
        :type CheckSyncConn: int
        :param _SdNewLimit: New connection suppression based on source IP and destination IP. Value range: [0,4294967295]
        :type SdNewLimit: int
        :param _DstNewLimit: New connection suppression based on destination IP. Value range: [0,4294967295]
        :type DstNewLimit: int
        :param _SdConnLimit: Concurrent connection suppression based on source IP and destination IP. Value range: [0,4294967295]
        :type SdConnLimit: int
        :param _DstConnLimit: Concurrent connection suppression based on destination IP. Value range: [0,4294967295]
        :type DstConnLimit: int
        :param _BadConnThreshold: Threshold for triggering connection suppression. Value range: [0,4294967295]
        :type BadConnThreshold: int
        :param _NullConnEnable: Exceptional connection detection condition: null session protection status. Valid values: [0,1]
        :type NullConnEnable: int
        :param _ConnTimeout: Exceptional connection detection condition: connection timeout. Valid values: [0,65535]
        :type ConnTimeout: int
        :param _SynRate: Exceptional connection detection condition: percentage of SYN out of ACK. Valid values: [0,100]
        :type SynRate: int
        :param _SynLimit: Exceptional connection detection condition: SYN threshold. Valid values: [0,100]
        :type SynLimit: int
        :param _DTcpMbpsLimit: TCP speed limit. Value range: [0,4294967295]
        :type DTcpMbpsLimit: int
        :param _DUdpMbpsLimit: UDP speed limit. Value range: [0,4294967295]
        :type DUdpMbpsLimit: int
        :param _DIcmpMbpsLimit: ICMP speed limit. Value range: [0,4294967295]
        :type DIcmpMbpsLimit: int
        :param _DOtherMbpsLimit: Other protocol speed limit. Value range: [0,4294967295]
        :type DOtherMbpsLimit: int
        """
        self._DropTcp = None
        self._DropUdp = None
        self._DropIcmp = None
        self._DropOther = None
        self._DropAbroad = None
        self._CheckSyncConn = None
        self._SdNewLimit = None
        self._DstNewLimit = None
        self._SdConnLimit = None
        self._DstConnLimit = None
        self._BadConnThreshold = None
        self._NullConnEnable = None
        self._ConnTimeout = None
        self._SynRate = None
        self._SynLimit = None
        self._DTcpMbpsLimit = None
        self._DUdpMbpsLimit = None
        self._DIcmpMbpsLimit = None
        self._DOtherMbpsLimit = None

    @property
    def DropTcp(self):
        return self._DropTcp

    @DropTcp.setter
    def DropTcp(self, DropTcp):
        self._DropTcp = DropTcp

    @property
    def DropUdp(self):
        return self._DropUdp

    @DropUdp.setter
    def DropUdp(self, DropUdp):
        self._DropUdp = DropUdp

    @property
    def DropIcmp(self):
        return self._DropIcmp

    @DropIcmp.setter
    def DropIcmp(self, DropIcmp):
        self._DropIcmp = DropIcmp

    @property
    def DropOther(self):
        return self._DropOther

    @DropOther.setter
    def DropOther(self, DropOther):
        self._DropOther = DropOther

    @property
    def DropAbroad(self):
        return self._DropAbroad

    @DropAbroad.setter
    def DropAbroad(self, DropAbroad):
        self._DropAbroad = DropAbroad

    @property
    def CheckSyncConn(self):
        return self._CheckSyncConn

    @CheckSyncConn.setter
    def CheckSyncConn(self, CheckSyncConn):
        self._CheckSyncConn = CheckSyncConn

    @property
    def SdNewLimit(self):
        return self._SdNewLimit

    @SdNewLimit.setter
    def SdNewLimit(self, SdNewLimit):
        self._SdNewLimit = SdNewLimit

    @property
    def DstNewLimit(self):
        return self._DstNewLimit

    @DstNewLimit.setter
    def DstNewLimit(self, DstNewLimit):
        self._DstNewLimit = DstNewLimit

    @property
    def SdConnLimit(self):
        return self._SdConnLimit

    @SdConnLimit.setter
    def SdConnLimit(self, SdConnLimit):
        self._SdConnLimit = SdConnLimit

    @property
    def DstConnLimit(self):
        return self._DstConnLimit

    @DstConnLimit.setter
    def DstConnLimit(self, DstConnLimit):
        self._DstConnLimit = DstConnLimit

    @property
    def BadConnThreshold(self):
        return self._BadConnThreshold

    @BadConnThreshold.setter
    def BadConnThreshold(self, BadConnThreshold):
        self._BadConnThreshold = BadConnThreshold

    @property
    def NullConnEnable(self):
        return self._NullConnEnable

    @NullConnEnable.setter
    def NullConnEnable(self, NullConnEnable):
        self._NullConnEnable = NullConnEnable

    @property
    def ConnTimeout(self):
        return self._ConnTimeout

    @ConnTimeout.setter
    def ConnTimeout(self, ConnTimeout):
        self._ConnTimeout = ConnTimeout

    @property
    def SynRate(self):
        return self._SynRate

    @SynRate.setter
    def SynRate(self, SynRate):
        self._SynRate = SynRate

    @property
    def SynLimit(self):
        return self._SynLimit

    @SynLimit.setter
    def SynLimit(self, SynLimit):
        self._SynLimit = SynLimit

    @property
    def DTcpMbpsLimit(self):
        return self._DTcpMbpsLimit

    @DTcpMbpsLimit.setter
    def DTcpMbpsLimit(self, DTcpMbpsLimit):
        self._DTcpMbpsLimit = DTcpMbpsLimit

    @property
    def DUdpMbpsLimit(self):
        return self._DUdpMbpsLimit

    @DUdpMbpsLimit.setter
    def DUdpMbpsLimit(self, DUdpMbpsLimit):
        self._DUdpMbpsLimit = DUdpMbpsLimit

    @property
    def DIcmpMbpsLimit(self):
        return self._DIcmpMbpsLimit

    @DIcmpMbpsLimit.setter
    def DIcmpMbpsLimit(self, DIcmpMbpsLimit):
        self._DIcmpMbpsLimit = DIcmpMbpsLimit

    @property
    def DOtherMbpsLimit(self):
        return self._DOtherMbpsLimit

    @DOtherMbpsLimit.setter
    def DOtherMbpsLimit(self, DOtherMbpsLimit):
        self._DOtherMbpsLimit = DOtherMbpsLimit


    def _deserialize(self, params):
        self._DropTcp = params.get("DropTcp")
        self._DropUdp = params.get("DropUdp")
        self._DropIcmp = params.get("DropIcmp")
        self._DropOther = params.get("DropOther")
        self._DropAbroad = params.get("DropAbroad")
        self._CheckSyncConn = params.get("CheckSyncConn")
        self._SdNewLimit = params.get("SdNewLimit")
        self._DstNewLimit = params.get("DstNewLimit")
        self._SdConnLimit = params.get("SdConnLimit")
        self._DstConnLimit = params.get("DstConnLimit")
        self._BadConnThreshold = params.get("BadConnThreshold")
        self._NullConnEnable = params.get("NullConnEnable")
        self._ConnTimeout = params.get("ConnTimeout")
        self._SynRate = params.get("SynRate")
        self._SynLimit = params.get("SynLimit")
        self._DTcpMbpsLimit = params.get("DTcpMbpsLimit")
        self._DUdpMbpsLimit = params.get("DUdpMbpsLimit")
        self._DIcmpMbpsLimit = params.get("DIcmpMbpsLimit")
        self._DOtherMbpsLimit = params.get("DOtherMbpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPacketFilter(AbstractModel):
    """Packet filter in advanced DDoS policy

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol. Valid values: [tcp, udp, icmp, all]
        :type Protocol: str
        :param _SportStart: Start source port. Value range: [0,65535]
        :type SportStart: int
        :param _SportEnd: End source port. Value range: [0,65535]
        :type SportEnd: int
        :param _DportStart: Start destination port. Value range: [0,65535]
        :type DportStart: int
        :param _DportEnd: End destination port. Value range: [0,65535]
        :type DportEnd: int
        :param _PktlenMin: Minimum packet length. Value range: [0,1500]
        :type PktlenMin: int
        :param _PktlenMax: Maximum packet length. Value range: [0,1500]
        :type PktlenMax: int
        :param _MatchBegin: Whether to detect the payload. Valid values: [
begin_l3 (IP header)
begin_l4 (TCP header)
begin_l5 (payload)
no_match (no check)
]
        :type MatchBegin: str
        :param _MatchType: Whether it is a regular expression. Valid values: [sunday (keyword), pcre (regular expression)]
        :type MatchType: str
        :param _Str: Keyword or regular expression
        :type Str: str
        :param _Depth: Detection depth. Value range: [0,1500]
        :type Depth: int
        :param _Offset: Detection offset. Value range: [0,1500]
        :type Offset: int
        :param _IsNot: Whether to include. Valid values: [0 (no), 1 (yes)]
        :type IsNot: int
        :param _Action: Policy action. Valid values: [drop, drop_black, drop_rst, drop_black_rst, transmit]
        :type Action: str
        """
        self._Protocol = None
        self._SportStart = None
        self._SportEnd = None
        self._DportStart = None
        self._DportEnd = None
        self._PktlenMin = None
        self._PktlenMax = None
        self._MatchBegin = None
        self._MatchType = None
        self._Str = None
        self._Depth = None
        self._Offset = None
        self._IsNot = None
        self._Action = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SportStart(self):
        return self._SportStart

    @SportStart.setter
    def SportStart(self, SportStart):
        self._SportStart = SportStart

    @property
    def SportEnd(self):
        return self._SportEnd

    @SportEnd.setter
    def SportEnd(self, SportEnd):
        self._SportEnd = SportEnd

    @property
    def DportStart(self):
        return self._DportStart

    @DportStart.setter
    def DportStart(self, DportStart):
        self._DportStart = DportStart

    @property
    def DportEnd(self):
        return self._DportEnd

    @DportEnd.setter
    def DportEnd(self, DportEnd):
        self._DportEnd = DportEnd

    @property
    def PktlenMin(self):
        return self._PktlenMin

    @PktlenMin.setter
    def PktlenMin(self, PktlenMin):
        self._PktlenMin = PktlenMin

    @property
    def PktlenMax(self):
        return self._PktlenMax

    @PktlenMax.setter
    def PktlenMax(self, PktlenMax):
        self._PktlenMax = PktlenMax

    @property
    def MatchBegin(self):
        return self._MatchBegin

    @MatchBegin.setter
    def MatchBegin(self, MatchBegin):
        self._MatchBegin = MatchBegin

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def Str(self):
        return self._Str

    @Str.setter
    def Str(self, Str):
        self._Str = Str

    @property
    def Depth(self):
        return self._Depth

    @Depth.setter
    def Depth(self, Depth):
        self._Depth = Depth

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def IsNot(self):
        return self._IsNot

    @IsNot.setter
    def IsNot(self, IsNot):
        self._IsNot = IsNot

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._SportStart = params.get("SportStart")
        self._SportEnd = params.get("SportEnd")
        self._DportStart = params.get("DportStart")
        self._DportEnd = params.get("DportEnd")
        self._PktlenMin = params.get("PktlenMin")
        self._PktlenMax = params.get("PktlenMax")
        self._MatchBegin = params.get("MatchBegin")
        self._MatchType = params.get("MatchType")
        self._Str = params.get("Str")
        self._Depth = params.get("Depth")
        self._Offset = params.get("Offset")
        self._IsNot = params.get("IsNot")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPortLimit(AbstractModel):
    """Disabled port in advanced DDoS policy

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol. Valid values: [tcp, udp, all]
        :type Protocol: str
        :param _DPortStart: Start destination port. Value range: [0,65535]
        :type DPortStart: int
        :param _DPortEnd: End destination port, which must be greater than or equal to the start destination port. Value range: [0,65535]
        :type DPortEnd: int
        :param _SPortStart: Start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.
        :type SPortStart: int
        :param _SPortEnd: End source port, which must be greater than or equal to the start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.
        :type SPortEnd: int
        :param _Action: Action to be executed. Valid values: [drop (discard) , transmit (forward)]
Note: this field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param _Kind: Type of port to be disabled. Valid values: [0 (destination port range), 1 (source port range), 2 (destination port range and source port range)]
Note: this field may return null, indicating that no valid values can be obtained.
        :type Kind: int
        """
        self._Protocol = None
        self._DPortStart = None
        self._DPortEnd = None
        self._SPortStart = None
        self._SPortEnd = None
        self._Action = None
        self._Kind = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DPortStart(self):
        return self._DPortStart

    @DPortStart.setter
    def DPortStart(self, DPortStart):
        self._DPortStart = DPortStart

    @property
    def DPortEnd(self):
        return self._DPortEnd

    @DPortEnd.setter
    def DPortEnd(self, DPortEnd):
        self._DPortEnd = DPortEnd

    @property
    def SPortStart(self):
        return self._SPortStart

    @SPortStart.setter
    def SPortStart(self, SPortStart):
        self._SPortStart = SPortStart

    @property
    def SPortEnd(self):
        return self._SPortEnd

    @SPortEnd.setter
    def SPortEnd(self, SPortEnd):
        self._SPortEnd = SPortEnd

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._DPortStart = params.get("DPortStart")
        self._DPortEnd = params.get("DPortEnd")
        self._SPortStart = params.get("SPortStart")
        self._SPortEnd = params.get("SPortEnd")
        self._Action = params.get("Action")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosPolicy(AbstractModel):
    """Advanced DDoS policy

    """

    def __init__(self):
        r"""
        :param _Resources: Resource bound to policy
        :type Resources: list of ResourceIp
        :param _DropOptions: Disabled protocol
        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`
        :param _PortLimits: Disabled port
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _PacketFilters: Packet filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _IpBlackWhiteLists: IP blocklist/allowlist
        :type IpBlackWhiteLists: list of IpBlackWhite
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _CreateTime: Policy creation time
        :type CreateTime: str
        :param _WaterPrint: Watermarking policy parameter. There can be only one policy. If there are no policies, the array is empty
        :type WaterPrint: list of WaterPrintPolicy
        :param _WaterKey: Watermark key. There can be up to two keys. If there are no policies, the array is empty
        :type WaterKey: list of WaterPrintKey
        :param _BoundResources: Resource instance bound to policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type BoundResources: list of str
        :param _SceneId: Policy scenario
Note: this field may return null, indicating that no valid values can be obtained.
        :type SceneId: str
        """
        self._Resources = None
        self._DropOptions = None
        self._PortLimits = None
        self._PacketFilters = None
        self._IpBlackWhiteLists = None
        self._PolicyId = None
        self._PolicyName = None
        self._CreateTime = None
        self._WaterPrint = None
        self._WaterKey = None
        self._BoundResources = None
        self._SceneId = None

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def IpBlackWhiteLists(self):
        return self._IpBlackWhiteLists

    @IpBlackWhiteLists.setter
    def IpBlackWhiteLists(self, IpBlackWhiteLists):
        self._IpBlackWhiteLists = IpBlackWhiteLists

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint

    @property
    def WaterKey(self):
        return self._WaterKey

    @WaterKey.setter
    def WaterKey(self, WaterKey):
        self._WaterKey = WaterKey

    @property
    def BoundResources(self):
        return self._BoundResources

    @BoundResources.setter
    def BoundResources(self, BoundResources):
        self._BoundResources = BoundResources

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceIp()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("DropOptions") is not None:
            self._DropOptions = DDoSPolicyDropOption()
            self._DropOptions._deserialize(params.get("DropOptions"))
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("IpBlackWhiteLists") is not None:
            self._IpBlackWhiteLists = []
            for item in params.get("IpBlackWhiteLists"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpBlackWhiteLists.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._CreateTime = params.get("CreateTime")
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
        if params.get("WaterKey") is not None:
            self._WaterKey = []
            for item in params.get("WaterKey"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._WaterKey.append(obj)
        self._BoundResources = params.get("BoundResources")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _CCFrequencyRuleId: Access frequency control rule ID for CC protection
        :type CCFrequencyRuleId: str
        """
        self._Business = None
        self._CCFrequencyRuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteCCSelfDefinePolicyRequest(AbstractModel):
    """DeleteCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _SetId: Policy ID
        :type SetId: str
        """
        self._Business = None
        self._Id = None
        self._SetId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteDDoSPolicyCaseRequest(AbstractModel):
    """DeleteDDoSPolicyCase request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _SceneId: Policy scenario ID
        :type SceneId: str
        """
        self._Business = None
        self._SceneId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteDDoSPolicyRequest(AbstractModel):
    """DeleteDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        """
        self._Business = None
        self._PolicyId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteL4RulesRequest(AbstractModel):
    """DeleteL4Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID list
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID list
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DescribeActionLogRequest(AbstractModel):
    """DescribeActionLog request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Filter: Search value, which can only be resource ID or user `UIN`
        :type Filter: str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Business = None
        self._Filter = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Business = params.get("Business")
        self._Filter = params.get("Filter")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _Data: Record array
        :type Data: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBGPIPL7RuleMaxCntRequest(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Maximum number of layer-7 rules that can be added for Anti-DDoS Advanced
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeBaradDataRequest(AbstractModel):
    """DescribeBaradData request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _MetricName: Metric name. Valid values:
connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;
        :type MetricName: str
        :param _Period: Statistical time granularity in seconds (300: 5-minute, 3600: hourly, 86400: daily)
        :type Period: int
        :param _StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5
        :type StartTime: str
        :param _EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5
        :type EndTime: str
        :param _Statistics: Statistical method. Valid values:
max: maximum value;
min: minimum value;
avg: average;
        :type Statistics: str
        :param _ProtocolPort: Protocol port array
        :type ProtocolPort: list of ProtocolPort
        :param _Ip: Resource instance IP, which is required only if `Business` is `net` (Anti-DDoS Ultimate), because an Anti-DDoS Ultimate instance has multiple IPs;
        :type Ip: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Statistics = None
        self._ProtocolPort = None
        self._Ip = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def ProtocolPort(self):
        return self._ProtocolPort

    @ProtocolPort.setter
    def ProtocolPort(self, ProtocolPort):
        self._ProtocolPort = ProtocolPort

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Statistics = params.get("Statistics")
        if params.get("ProtocolPort") is not None:
            self._ProtocolPort = []
            for item in params.get("ProtocolPort"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtocolPort.append(obj)
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData response structure.

    """

    def __init__(self):
        r"""
        :param _DataList: Returned metric value
        :type DataList: list of BaradData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataList = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = BaradData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBasicCCThresholdRequest(AbstractModel):
    """DescribeBasicCCThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _BasicIp: Queried IP address, such as 1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param _BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param _BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param _BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param _BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        """
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicIpInstance = None
        self._BasicIspCode = None

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode


    def _deserialize(self, params):
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _CCEnable: CC status (0: disabled, 1: enabled)
        :type CCEnable: int
        :param _CCThreshold: CC protection threshold
        :type CCThreshold: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CCEnable = None
        self._CCThreshold = None
        self._RequestId = None

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._RequestId = params.get("RequestId")


class DescribeBasicDeviceThresholdRequest(AbstractModel):
    """DescribeBasicDeviceThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _BasicIp: Queried IP address, such as 1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param _BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param _BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param _BasicCheckFlag: Validity check. Valid value: 1
        :type BasicCheckFlag: int
        :param _BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param _BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        """
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicCheckFlag = None
        self._BasicIpInstance = None
        self._BasicIspCode = None

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicCheckFlag(self):
        return self._BasicCheckFlag

    @BasicCheckFlag.setter
    def BasicCheckFlag(self, BasicCheckFlag):
        self._BasicCheckFlag = BasicCheckFlag

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode


    def _deserialize(self, params):
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicCheckFlag = params.get("BasicCheckFlag")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _Threshold: Blackhole blocking value
        :type Threshold: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Threshold = None
        self._RequestId = None

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _Id: Resource ID
        :type Id: str
        :param _Period: Statistical period in seconds. Valid values: 300, 1800, 3600, 21600, and 86400.
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Statistics: Statistical mode, which only supports sum.
        :type Statistics: str
        :param _ProtoInfo: Protocol and port list, which is valid when the statistical dimension is the number of connections. Valid protocols: TCP, UDP, HTTP, and HTTPS.
        :type ProtoInfo: list of ProtocolPort
        :param _Domain: Specific domain name query
        :type Domain: str
        """
        self._Business = None
        self._Id = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Statistics = None
        self._ProtoInfo = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def ProtoInfo(self):
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Statistics = params.get("Statistics")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizHttpStatusResponse(AbstractModel):
    """DescribeBizHttpStatus response structure.

    """

    def __init__(self):
        r"""
        :param _HttpStatusMap: Statistics on the HTTP status codes of business traffic
        :type HttpStatusMap: :class:`tencentcloud.dayu.v20180709.models.HttpStatusMap`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HttpStatusMap = None
        self._RequestId = None

    @property
    def HttpStatusMap(self):
        return self._HttpStatusMap

    @HttpStatusMap.setter
    def HttpStatusMap(self, HttpStatusMap):
        self._HttpStatusMap = HttpStatusMap

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HttpStatusMap") is not None:
            self._HttpStatusMap = HttpStatusMap()
            self._HttpStatusMap._deserialize(params.get("HttpStatusMap"))
        self._RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RsId: Anti-DDoS instance ID
        :type RsId: str
        """
        self._Business = None
        self._RsId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _CCAlarmThreshold: CC alarm threshold
        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CCAlarmThreshold = None
        self._RequestId = None

    @property
    def CCAlarmThreshold(self):
        return self._CCAlarmThreshold

    @CCAlarmThreshold.setter
    def CCAlarmThreshold(self, CCAlarmThreshold):
        self._CCAlarmThreshold = CCAlarmThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCAlarmThreshold") is not None:
            self._CCAlarmThreshold = CCAlarmThreshold()
            self._CCAlarmThreshold._deserialize(params.get("CCAlarmThreshold"))
        self._RequestId = params.get("RequestId")


class DescribeCCEvListRequest(AbstractModel):
    """DescribeCCEvList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _IpList: Resource instance IP. When `business` is not `basic`, if `IpList` is not empty, `Id` must not be empty;
        :type IpList: list of str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._IpList = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `shield`: Chess Shield; `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _IpList: Instance IP list
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpList: list of str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Data: CC attack event list
        :type Data: list of CCEventRecord
        :param _Total: Total number of records
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._IpList = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CCEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCCFrequencyRulesRequest(AbstractModel):
    """DescribeCCFrequencyRules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API). If a value is entered, it means to get the access frequency control rule of the forwarding rule;
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules response structure.

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleList: Access frequency control rule list
        :type CCFrequencyRuleList: list of CCFrequencyRule
        :param _CCFrequencyRuleStatus: Access frequency control rule status. Valid values: [on, off];
        :type CCFrequencyRuleStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CCFrequencyRuleList = None
        self._CCFrequencyRuleStatus = None
        self._RequestId = None

    @property
    def CCFrequencyRuleList(self):
        return self._CCFrequencyRuleList

    @CCFrequencyRuleList.setter
    def CCFrequencyRuleList(self, CCFrequencyRuleList):
        self._CCFrequencyRuleList = CCFrequencyRuleList

    @property
    def CCFrequencyRuleStatus(self):
        return self._CCFrequencyRuleStatus

    @CCFrequencyRuleStatus.setter
    def CCFrequencyRuleStatus(self, CCFrequencyRuleStatus):
        self._CCFrequencyRuleStatus = CCFrequencyRuleStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCFrequencyRuleList") is not None:
            self._CCFrequencyRuleList = []
            for item in params.get("CCFrequencyRuleList"):
                obj = CCFrequencyRule()
                obj._deserialize(item)
                self._CCFrequencyRuleList.append(obj)
        self._CCFrequencyRuleStatus = params.get("CCFrequencyRuleStatus")
        self._RequestId = params.get("RequestId")


class DescribeCCIpAllowDenyRequest(AbstractModel):
    """DescribeCCIpAllowDeny request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Type: Blocklist or allowlist. Valid values: [white (allowlist), black (blocklist)]
Note: this array can only have one value. It cannot get the blocklist and allowlist at the same time
        :type Type: list of str
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];
        :type Protocol: str
        """
        self._Business = None
        self._Id = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny response structure.

    """

    def __init__(self):
        r"""
        :param _Data: This field has been replaced by `RecordList` and should not be used
        :type Data: list of KeyValue
        :param _Total: Number of records
        :type Total: int
        :param _RecordList: Returned Blocklist/allowlist record,
If "Key":"ip", "Value": IP;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection protocol (HTTP or HTTPS);
        :type RecordList: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RecordList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCSelfDefinePolicyRequest(AbstractModel):
    """DescribeCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro, `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Limit: Number of entries pulled
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of custom rules
        :type Total: int
        :param _Policys: Policy list
        :type Policys: list of CCPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Policys = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Policys(self):
        return self._Policys

    @Policys.setter
    def Policys(self, Policys):
        self._Policys = Policys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Policys") is not None:
            self._Policys = []
            for item in params.get("Policys"):
                obj = CCPolicy()
                obj._deserialize(item)
                self._Policys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        :param _Domain: (Optional) Domain name
        :type Domain: str
        """
        self._Business = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Data: Value array
        :type Data: list of int non-negative
        :param _Count: Number of values
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeCCUrlAllowRequest(AbstractModel):
    """DescribeCCUrlAllow request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Type: Blocklist or allowlist. Valid value: [white (allowlist)]. Currently, only allowlist is supported.
Note: this array can only have one value which can only be `white`
        :type Type: list of str
        :param _Limit: Pagination parameter
        :type Limit: int
        :param _Offset: Pagination parameter
        :type Offset: int
        :param _Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];
        :type Protocol: str
        """
        self._Business = None
        self._Id = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: This field has been replaced by `RecordList` and should not be used
        :type Data: list of KeyValue
        :param _Total: Total number of records
        :type Total: int
        :param _RecordList: Returned Blocklist/allowlist record,
If "Key":"url", "Value": URL;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection type (HTTP protection or HTTPS domain name protection);
        :type RecordList: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RecordList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAlarmThresholdRequest(AbstractModel):
    """DescribeDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RsId: Anti-DDoS instance ID
        :type RsId: str
        """
        self._Business = None
        self._RsId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _DDoSAlarmThreshold: DDoS alarm threshold
        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DDoSAlarmThreshold = None
        self._RequestId = None

    @property
    def DDoSAlarmThreshold(self):
        return self._DDoSAlarmThreshold

    @DDoSAlarmThreshold.setter
    def DDoSAlarmThreshold(self, DDoSAlarmThreshold):
        self._DDoSAlarmThreshold = DDoSAlarmThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DDoSAlarmThreshold") is not None:
            self._DDoSAlarmThreshold = DDoSAlarmThreshold()
            self._DDoSAlarmThreshold._deserialize(params.get("DDoSAlarmThreshold"))
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackIPRegionMapRequest(AbstractModel):
    """DescribeDDoSAttackIPRegionMap request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time. Maximum statistics time range: half a year;
        :type EndTime: str
        :param _IpList: IP attack source of specified resource, which is optional
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap response structure.

    """

    def __init__(self):
        r"""
        :param _NationCount: Global region distribution data
        :type NationCount: list of KeyValueRecord
        :param _ProvinceCount: Chinese province distribution data
        :type ProvinceCount: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NationCount = None
        self._ProvinceCount = None
        self._RequestId = None

    @property
    def NationCount(self):
        return self._NationCount

    @NationCount.setter
    def NationCount(self, NationCount):
        self._NationCount = NationCount

    @property
    def ProvinceCount(self):
        return self._ProvinceCount

    @ProvinceCount.setter
    def ProvinceCount(self, ProvinceCount):
        self._ProvinceCount = ProvinceCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NationCount") is not None:
            self._NationCount = []
            for item in params.get("NationCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._NationCount.append(obj)
        if params.get("ProvinceCount") is not None:
            self._ProvinceCount = []
            for item in params.get("ProvinceCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ProvinceCount.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceRequest(AbstractModel):
    """DescribeDDoSAttackSource request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param _IpList: IP attack source of specified resource, which is optional
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of attack sources
        :type Total: int
        :param _AttackSourceList: Attack source list
        :type AttackSourceList: list of DDoSAttackSourceRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._AttackSourceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AttackSourceList(self):
        return self._AttackSourceList

    @AttackSourceList.setter
    def AttackSourceList(self, AttackSourceList):
        self._AttackSourceList = AttackSourceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AttackSourceList") is not None:
            self._AttackSourceList = []
            for item in params.get("AttackSourceList"):
                obj = DDoSAttackSourceRecord()
                obj._deserialize(item)
                self._AttackSourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSCountRequest(AbstractModel):
    """DescribeDDoSCount request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        :param _Data: `Key-Value` array. Valid values of `Key`:
If `MetricName` is `traffic`:
If `key` is `TcpKBSum`, it indicates the traffic of TCP packets in KB.
If `key` is `UdpKBSum`, it indicates the traffic of UDP packets in KB.
If `key` is `IcmpKBSum`, it indicates the traffic of ICMP packets in KB.
If `key` is `OtherKBSum`, it indicates the traffic of other packets in KB.

If `MetricName` is `pkg`:
If `key` is `TcpPacketSum`, it indicates the number of TCP packets.
If `key` is `UdpPacketSum`, it indicates the number of UDP packets.
If `key` is `IcmpPacketSum`, it indicates the number of ICMP packets.
If `key` is `OtherPacketSum`, it indicates the number of other packets.

If `MetricName` is `classnum`:
The value of `key` indicates the attack event type. When the `key` is `UNKNOWNFLOOD`, it indicates  unknown attack events.
        :type Data: list of KeyValue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSDefendStatusRequest(AbstractModel):
    """DescribeDDoSDefendStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Instance ID, which is required only if `Business` is not `basic`.
        :type Id: str
        :param _Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param _BizType: Type of products bound to the anti-DDoS instance, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (Bare metal products), eni (elastic network interface), vpngw (VPN Gateway), natgw (NAT Gateway), waf (Web Application Firewall), fpc (Finance products), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param _DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param _InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param _IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
"bj":     North China (Beijing)
"cd":     Southwest China (Chengdu)
"cq":     Southwest China (Chongqing)
"gz":     South China (Guangzhou)
"gzopen": South China (Guangzhou Open)
"hk":     Hong Kong (China)
"kr":     Southeast Asia (Seoul)
"sh":     East China (Shanghai)
"shjr":   East China (Shanghai Finance)
"szjr":   South China (Shenzhen Finance)
"sg":     Southeast Asia (Singapore)
"th":     Southeast Asia (Thailand)
"de":     Europe (Germany)
"usw":    West US (Silicon Valley)
"ca":     North America (Toronto)
"jp":     Japan
"hzec":   Hangzhou
"in":     India
"use":    East US (Virginia)
"ru":     Russia
"tpe":    Taiwan (China)
"nj":     Nanjing
        :type IPRegion: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus response structure.

    """

    def __init__(self):
        r"""
        :param _DefendStatus: Protection status. 0: disabled, 1: enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type DefendStatus: int
        :param _UndefendExpire: Expiration time of temporary protection disablement. This field is empty if the protection is in enabled status;
Note: this field may return null, indicating that no valid values can be obtained.
        :type UndefendExpire: str
        :param _ShowFlag: Console feature display field. 1: displays console features, 0: hides console features
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShowFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DefendStatus = None
        self._UndefendExpire = None
        self._ShowFlag = None
        self._RequestId = None

    @property
    def DefendStatus(self):
        return self._DefendStatus

    @DefendStatus.setter
    def DefendStatus(self, DefendStatus):
        self._DefendStatus = DefendStatus

    @property
    def UndefendExpire(self):
        return self._UndefendExpire

    @UndefendExpire.setter
    def UndefendExpire(self, UndefendExpire):
        self._UndefendExpire = UndefendExpire

    @property
    def ShowFlag(self):
        return self._ShowFlag

    @ShowFlag.setter
    def ShowFlag(self, ShowFlag):
        self._ShowFlag = ShowFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DefendStatus = params.get("DefendStatus")
        self._UndefendExpire = params.get("UndefendExpire")
        self._ShowFlag = params.get("ShowFlag")
        self._RequestId = params.get("RequestId")


class DescribeDDoSEvInfoRequest(AbstractModel):
    """DescribeDDoSEvInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _TcpPacketSum: Number of TCP attack packets
        :type TcpPacketSum: int
        :param _TcpKBSum: Traffic of TCP attacks in KB
        :type TcpKBSum: int
        :param _UdpPacketSum: Number of UDP attack packets
        :type UdpPacketSum: int
        :param _UdpKBSum: Traffic of UDP attacks in KB
        :type UdpKBSum: int
        :param _IcmpPacketSum: Number of ICMP attack packets
        :type IcmpPacketSum: int
        :param _IcmpKBSum: Traffic of ICMP attacks in KB
        :type IcmpKBSum: int
        :param _OtherPacketSum: Number of other attack packets
        :type OtherPacketSum: int
        :param _OtherKBSum: Traffic of other attacks in KB
        :type OtherKBSum: int
        :param _TotalTraffic: Total attack traffic in KB
        :type TotalTraffic: int
        :param _Mbps: Attack traffic bandwidth peak
        :type Mbps: int
        :param _Pps: Attack packet rate peak
        :type Pps: int
        :param _PcapUrl: PCAP file download link
        :type PcapUrl: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._TcpPacketSum = None
        self._TcpKBSum = None
        self._UdpPacketSum = None
        self._UdpKBSum = None
        self._IcmpPacketSum = None
        self._IcmpKBSum = None
        self._OtherPacketSum = None
        self._OtherKBSum = None
        self._TotalTraffic = None
        self._Mbps = None
        self._Pps = None
        self._PcapUrl = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TcpPacketSum(self):
        return self._TcpPacketSum

    @TcpPacketSum.setter
    def TcpPacketSum(self, TcpPacketSum):
        self._TcpPacketSum = TcpPacketSum

    @property
    def TcpKBSum(self):
        return self._TcpKBSum

    @TcpKBSum.setter
    def TcpKBSum(self, TcpKBSum):
        self._TcpKBSum = TcpKBSum

    @property
    def UdpPacketSum(self):
        return self._UdpPacketSum

    @UdpPacketSum.setter
    def UdpPacketSum(self, UdpPacketSum):
        self._UdpPacketSum = UdpPacketSum

    @property
    def UdpKBSum(self):
        return self._UdpKBSum

    @UdpKBSum.setter
    def UdpKBSum(self, UdpKBSum):
        self._UdpKBSum = UdpKBSum

    @property
    def IcmpPacketSum(self):
        return self._IcmpPacketSum

    @IcmpPacketSum.setter
    def IcmpPacketSum(self, IcmpPacketSum):
        self._IcmpPacketSum = IcmpPacketSum

    @property
    def IcmpKBSum(self):
        return self._IcmpKBSum

    @IcmpKBSum.setter
    def IcmpKBSum(self, IcmpKBSum):
        self._IcmpKBSum = IcmpKBSum

    @property
    def OtherPacketSum(self):
        return self._OtherPacketSum

    @OtherPacketSum.setter
    def OtherPacketSum(self, OtherPacketSum):
        self._OtherPacketSum = OtherPacketSum

    @property
    def OtherKBSum(self):
        return self._OtherKBSum

    @OtherKBSum.setter
    def OtherKBSum(self, OtherKBSum):
        self._OtherKBSum = OtherKBSum

    @property
    def TotalTraffic(self):
        return self._TotalTraffic

    @TotalTraffic.setter
    def TotalTraffic(self, TotalTraffic):
        self._TotalTraffic = TotalTraffic

    @property
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def PcapUrl(self):
        return self._PcapUrl

    @PcapUrl.setter
    def PcapUrl(self, PcapUrl):
        self._PcapUrl = PcapUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TcpPacketSum = params.get("TcpPacketSum")
        self._TcpKBSum = params.get("TcpKBSum")
        self._UdpPacketSum = params.get("UdpPacketSum")
        self._UdpKBSum = params.get("UdpKBSum")
        self._IcmpPacketSum = params.get("IcmpPacketSum")
        self._IcmpKBSum = params.get("IcmpKBSum")
        self._OtherPacketSum = params.get("OtherPacketSum")
        self._OtherKBSum = params.get("OtherKBSum")
        self._TotalTraffic = params.get("TotalTraffic")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._PcapUrl = params.get("PcapUrl")
        self._RequestId = params.get("RequestId")


class DescribeDDoSEvListRequest(AbstractModel):
    """DescribeDDoSEvList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        :param _IpList: Resource IP
        :type IpList: list of str
        :param _OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes, no]. If an empty string is entered, it means no filtering
        :type OverLoad: str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._IpList = None
        self._OverLoad = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def OverLoad(self):
        return self._OverLoad

    @OverLoad.setter
    def OverLoad(self, OverLoad):
        self._OverLoad = OverLoad

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._OverLoad = params.get("OverLoad")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _IpList: Resource IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpList: list of str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Data: DDoS attack event list
        :type Data: list of DDoSEventRecord
        :param _Total: Total number of records
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._IpList = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDDoSIpLogRequest(AbstractModel):
    """DescribeDDoSIpLog request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content
        :type Data: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetCountRequest(AbstractModel):
    """DescribeDDoSNetCount request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        :param _Data: `Key-Value` array. Valid values of `Key`:
If `MetricName` is `traffic`:
If `key` is `TcpKBSum`, it indicates the traffic of TCP packets in KB.
If `key` is `UdpKBSum`, it indicates the traffic of UDP packets in KB.
If `key` is `IcmpKBSum`, it indicates the traffic of ICMP packets in KB.
If `key` is `OtherKBSum`, it indicates the traffic of other packets in KB.

If `MetricName` is `pkg`:
If `key` is `TcpPacketSum`, it indicates the number of TCP packets.
If `key` is `UdpPacketSum`, it indicates the number of UDP packets.
If `key` is `IcmpPacketSum`, it indicates the number of ICMP packets.
If `key` is `OtherPacketSum`, it indicates the number of other packets.

If `MetricName` is `classnum`:
The value of `key` indicates the attack event type. When the `key` is `UNKNOWNFLOOD`, it indicates  unknown attack events.
        :type Data: list of KeyValue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetEvInfoRequest(AbstractModel):
    """DescribeDDoSNetEvInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _TcpPacketSum: Number of TCP attack packets
        :type TcpPacketSum: int
        :param _TcpKBSum: Traffic of TCP attacks in KB
        :type TcpKBSum: int
        :param _UdpPacketSum: Number of UDP attack packets
        :type UdpPacketSum: int
        :param _UdpKBSum: Traffic of UDP attacks in KB
        :type UdpKBSum: int
        :param _IcmpPacketSum: Number of ICMP attack packets
        :type IcmpPacketSum: int
        :param _IcmpKBSum: Traffic of ICMP attacks in KB
        :type IcmpKBSum: int
        :param _OtherPacketSum: Number of other attack packets
        :type OtherPacketSum: int
        :param _OtherKBSum: Traffic of other attacks in KB
        :type OtherKBSum: int
        :param _TotalTraffic: Total attack traffic in KB
        :type TotalTraffic: int
        :param _Mbps: Attack traffic bandwidth peak
        :type Mbps: int
        :param _Pps: Attack packet rate peak
        :type Pps: int
        :param _PcapUrl: PCAP file download link
        :type PcapUrl: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._TcpPacketSum = None
        self._TcpKBSum = None
        self._UdpPacketSum = None
        self._UdpKBSum = None
        self._IcmpPacketSum = None
        self._IcmpKBSum = None
        self._OtherPacketSum = None
        self._OtherKBSum = None
        self._TotalTraffic = None
        self._Mbps = None
        self._Pps = None
        self._PcapUrl = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TcpPacketSum(self):
        return self._TcpPacketSum

    @TcpPacketSum.setter
    def TcpPacketSum(self, TcpPacketSum):
        self._TcpPacketSum = TcpPacketSum

    @property
    def TcpKBSum(self):
        return self._TcpKBSum

    @TcpKBSum.setter
    def TcpKBSum(self, TcpKBSum):
        self._TcpKBSum = TcpKBSum

    @property
    def UdpPacketSum(self):
        return self._UdpPacketSum

    @UdpPacketSum.setter
    def UdpPacketSum(self, UdpPacketSum):
        self._UdpPacketSum = UdpPacketSum

    @property
    def UdpKBSum(self):
        return self._UdpKBSum

    @UdpKBSum.setter
    def UdpKBSum(self, UdpKBSum):
        self._UdpKBSum = UdpKBSum

    @property
    def IcmpPacketSum(self):
        return self._IcmpPacketSum

    @IcmpPacketSum.setter
    def IcmpPacketSum(self, IcmpPacketSum):
        self._IcmpPacketSum = IcmpPacketSum

    @property
    def IcmpKBSum(self):
        return self._IcmpKBSum

    @IcmpKBSum.setter
    def IcmpKBSum(self, IcmpKBSum):
        self._IcmpKBSum = IcmpKBSum

    @property
    def OtherPacketSum(self):
        return self._OtherPacketSum

    @OtherPacketSum.setter
    def OtherPacketSum(self, OtherPacketSum):
        self._OtherPacketSum = OtherPacketSum

    @property
    def OtherKBSum(self):
        return self._OtherKBSum

    @OtherKBSum.setter
    def OtherKBSum(self, OtherKBSum):
        self._OtherKBSum = OtherKBSum

    @property
    def TotalTraffic(self):
        return self._TotalTraffic

    @TotalTraffic.setter
    def TotalTraffic(self, TotalTraffic):
        self._TotalTraffic = TotalTraffic

    @property
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def PcapUrl(self):
        return self._PcapUrl

    @PcapUrl.setter
    def PcapUrl(self, PcapUrl):
        self._PcapUrl = PcapUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TcpPacketSum = params.get("TcpPacketSum")
        self._TcpKBSum = params.get("TcpKBSum")
        self._UdpPacketSum = params.get("UdpPacketSum")
        self._UdpKBSum = params.get("UdpKBSum")
        self._IcmpPacketSum = params.get("IcmpPacketSum")
        self._IcmpKBSum = params.get("IcmpKBSum")
        self._OtherPacketSum = params.get("OtherPacketSum")
        self._OtherKBSum = params.get("OtherKBSum")
        self._TotalTraffic = params.get("TotalTraffic")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._PcapUrl = params.get("PcapUrl")
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetEvListRequest(AbstractModel):
    """DescribeDDoSNetEvList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Data: DDoS attack event list
        :type Data: list of DDoSEventRecord
        :param _Total: Total number of records
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetIpLogRequest(AbstractModel):
    """DescribeDDoSNetIpLog request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Attack start time
        :type StartTime: str
        :param _EndTime: Attack end time
        :type EndTime: str
        :param _Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content
        :type Data: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetTrendRequest(AbstractModel):
    """DescribeDDoSNetTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Data: Value array
        :type Data: list of int non-negative
        :param _Count: Number of values
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Resource ID, which is optional. If a value is entered, it indicates the advanced DDoS policy bound to the resource
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
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
        :param _DDosPolicyList: Advanced DDoS policy list
        :type DDosPolicyList: list of DDosPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DDosPolicyList = None
        self._RequestId = None

    @property
    def DDosPolicyList(self):
        return self._DDosPolicyList

    @DDosPolicyList.setter
    def DDosPolicyList(self, DDosPolicyList):
        self._DDosPolicyList = DDosPolicyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DDosPolicyList") is not None:
            self._DDosPolicyList = []
            for item in params.get("DDosPolicyList"):
                obj = DDosPolicy()
                obj._deserialize(item)
                self._DDosPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Anti-DDoS instance IP
        :type Ip: str
        :param _MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend response structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Ip: Resource IP
        :type Ip: str
        :param _MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param _Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param _StartTime: Statistics start time
        :type StartTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _Data: Value array. The unit for attack traffic bandwidth is Mbps, and that for the packet rate is pps.
        :type Data: list of int non-negative
        :param _Count: Number of values
        :type Count: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeDDoSUsedStatisRequest(AbstractModel):
    """DescribeDDoSUsedStatis request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        """
        self._Business = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Field value as follows:
Days: number of days of Anti-DDoS resource use
Attacks: number of DDoS attacks
        :type Data: list of KeyValue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIPProductInfoRequest(AbstractModel):
    """DescribeIPProductInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)
        :type Business: str
        :param _IpList: IP list
        :type IpList: list of str
        """
        self._Business = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Tencent Cloud product information list. If nothing is found, an empty array will be returned. Valid values:
If `Key` is ProductName, `value` indicates the name of a Tencent Cloud product instance;
If `Key` is `ProductInstanceId`, `value` indicates the ID of a Tencent Cloud product instance;
If `Key` is `ProductType`, `value` indicates the Tencent Cloud product type (cvm: CVM, clb: CLB);
If `Key` is `IP`, `value` indicates the IP of a Tencent Cloud product instance;
        :type Data: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInsurePacksRequest(AbstractModel):
    """DescribeInsurePacks request structure.

    """

    def __init__(self):
        r"""
        :param _IdList: Guarantee package ID, which is optional. If you need to get the guarantee package with a specified ID (such as insure-000000xe), please use this field
        :type IdList: list of str
        """
        self._IdList = None

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks response structure.

    """

    def __init__(self):
        r"""
        :param _InsurePacks: Guarantee package list
        :type InsurePacks: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InsurePacks = None
        self._RequestId = None

    @property
    def InsurePacks(self):
        return self._InsurePacks

    @InsurePacks.setter
    def InsurePacks(self, InsurePacks):
        self._InsurePacks = InsurePacks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InsurePacks") is not None:
            self._InsurePacks = []
            for item in params.get("InsurePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._InsurePacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList request structure.

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList response structure.

    """

    def __init__(self):
        r"""
        :param _List: Blocked IP list
        :type List: list of IpBlockData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpUnBlockListRequest(AbstractModel):
    """DescribeIpUnBlockList request structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time
        :type BeginTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Ip: IP (if this field is not empty, IP filtering will be performed)
        :type Ip: str
        :param _Paging: Pagination parameter (paginated query will be performed if this field is not empty). This field will be disused in the future. Please use the `Limit` and `Offset` fields instead;
        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Ip = None
        self._Paging = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Paging(self):
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList response structure.

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time
        :type BeginTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _List: IP unblocking record
        :type List: list of IpUnBlockData
        :param _Total: Total number of records
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = IpUnBlockData()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeL4HealthConfigRequest(AbstractModel):
    """DescribeL4HealthConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig response structure.

    """

    def __init__(self):
        r"""
        :param _HealthConfig: Layer-4 health check configuration array
        :type HealthConfig: list of L4HealthConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthConfig = None
        self._RequestId = None

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4RulesErrHealthRequest(AbstractModel):
    """DescribeL4RulesErrHealth request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of exceptional rules
        :type Total: int
        :param _ErrHealths: Exceptional rule list. Returned value description: `Key` is the rule ID, while `Value` is the exceptional IP. Multiple IPs are separated by ","
        :type ErrHealths: list of KeyValue
        :param _ExtErrHealths: Exceptional rule list (which provides more error-related information). Returned value description:
If `key` is `RuleId`, `Value` indicates the rule ID;
If `key` is `Protocol`, `Value` indicates the forwarding protocol of a rule;
If `key` is `VirtualPort`, `Value` indicates the forwarding port of a rule;
If `Key` is `ErrMessage`, `Value` indicates the exception message for health check;
Exception message for health check in the format of `"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6"`. Multiple error messages for the source IP should be separated by `,`,
SourceIp: real server IP, SourcePort: real server port, AbnormalStatTime: exception time, AbnormalReason: cause of exception, Interval: check frequency, CheckNum: number of checks, FailNum: number of failures;
        :type ExtErrHealths: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ErrHealths = None
        self._ExtErrHealths = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ErrHealths(self):
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

    @property
    def ExtErrHealths(self):
        return self._ExtErrHealths

    @ExtErrHealths.setter
    def ExtErrHealths(self, ExtErrHealths):
        self._ExtErrHealths = ExtErrHealths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        if params.get("ExtErrHealths") is not None:
            self._ExtErrHealths = []
            for item in params.get("ExtErrHealths"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ExtErrHealths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7HealthConfigRequest(AbstractModel):
    """DescribeL7HealthConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig response structure.

    """

    def __init__(self):
        r"""
        :param _HealthConfig: Layer-7 health check configuration array
        :type HealthConfig: list of L7HealthConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthConfig = None
        self._RequestId = None

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePackIndexRequest(AbstractModel):
    """DescribePackIndex request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        """
        self._Business = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackIndexResponse(AbstractModel):
    """DescribePackIndex response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Field value as follows:
TotalPackCount: number of resources
AttackPackCount: number of resources being cleansed
BlockPackCount: number of blocked resources
ExpiredPackCount: number of expired resources
ExpireingPackCount: number of expiring resources
IsolatePackCount: number of isolated resources
        :type Data: list of KeyValue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePcapRequest(AbstractModel):
    """DescribePcap request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _StartTime: Attack event start time in the format of "2018-08-28 07:00:00"
        :type StartTime: str
        :param _EndTime: Attack event end time in the format of "2018-08-28 07:02:00"
        :type EndTime: str
        :param _Ip: Resource IP, which is required only if `Business` is `net`;
        :type Ip: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Ip = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePcapResponse(AbstractModel):
    """DescribePcap response structure.

    """

    def __init__(self):
        r"""
        :param _PcapUrlList: PCAP packet download link list, which is an empty array if there are no PCAP packets;
        :type PcapUrlList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PcapUrlList = None
        self._RequestId = None

    @property
    def PcapUrlList(self):
        return self._PcapUrlList

    @PcapUrlList.setter
    def PcapUrlList(self, PcapUrlList):
        self._PcapUrlList = PcapUrlList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PcapUrlList = params.get("PcapUrlList")
        self._RequestId = params.get("RequestId")


class DescribePolicyCaseRequest(AbstractModel):
    """DescribePolicyCase request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _SceneId: Policy scenario ID
        :type SceneId: str
        """
        self._Business = None
        self._SceneId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase response structure.

    """

    def __init__(self):
        r"""
        :param _CaseList: Policy scenario list
        :type CaseList: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CaseList = None
        self._RequestId = None

    @property
    def CaseList(self):
        return self._CaseList

    @CaseList.setter
    def CaseList(self, CaseList):
        self._CaseList = CaseList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CaseList") is not None:
            self._CaseList = []
            for item in params.get("CaseList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._CaseList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResIpListRequest(AbstractModel):
    """DescribeResIpList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _IdList: Resource ID. If this field is left empty, it means to get all resources IP of the current user
        :type IdList: list of str
        """
        self._Business = None
        self._IdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList response structure.

    """

    def __init__(self):
        r"""
        :param _Resource: Resource IP list
        :type Resource: list of ResourceIp
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Resource = None
        self._RequestId = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self._Resource = []
            for item in params.get("Resource"):
                obj = ResourceIp()
                obj._deserialize(item)
                self._Resource.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RegionList: Region code search, which is optional. If no regions are to be specified, enter an empty array. If a region is to be specified, enter a region code, such as ["gz", "sh"]
        :type RegionList: list of str
        :param _Line: Line search. This field can be optionally entered only when getting the list of Anti-DDoS Advanced resources. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. Please enter an empty array when getting other products;
        :type Line: list of int non-negative
        :param _IdList: Resource ID search, which is optional. If this field is not an empty array, it means to get the resource list of a specified resource;
        :type IdList: list of str
        :param _Name: Resource name search, which is optional. If this field is not an empty string, it means to search for resources by name;
        :type Name: str
        :param _IpList: IP query list, which is optional. Resources will be queried by IP if the list is not empty.
        :type IpList: list of str
        :param _Status: Resource status search list, which is optional. Valid values: [0 (running), 1 (cleansing), 2 (blocking)]. No status search will be performed if an empty array is entered;
        :type Status: list of int non-negative
        :param _Expire: Expiring resource search, which is optional. Valid values: [0 (no search), 1 (search for expiring resources)]
        :type Expire: int
        :param _OderBy: Sort by field, which is optional
        :type OderBy: list of OrderBy
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param _CName: CNAME of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;
        :type CName: str
        :param _Domain: Domain name of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;
        :type Domain: str
        """
        self._Business = None
        self._RegionList = None
        self._Line = None
        self._IdList = None
        self._Name = None
        self._IpList = None
        self._Status = None
        self._Expire = None
        self._OderBy = None
        self._Limit = None
        self._Offset = None
        self._CName = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def OderBy(self):
        return self._OderBy

    @OderBy.setter
    def OderBy(self, OderBy):
        self._OderBy = OderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CName(self):
        return self._CName

    @CName.setter
    def CName(self, CName):
        self._CName = CName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RegionList = params.get("RegionList")
        self._Line = params.get("Line")
        self._IdList = params.get("IdList")
        self._Name = params.get("Name")
        self._IpList = params.get("IpList")
        self._Status = params.get("Status")
        self._Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self._OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OderBy.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CName = params.get("CName")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of records
        :type Total: int
        :param _ServicePacks: Resource record list. The description of key values is as follows:
"Key": "CreateTime" (Instance purchase time)
"Key": "Region" (Instance region)
"Key": "BoundIP" (IP bound to the single-IP instance)
"Key": "Id" (Instance ID)
"Key": "CCEnabled" (CC protection switch status of the instance)
"Key": "DDoSThreshold" (Anti-DDoS cleansing threshold of the instance)	
"Key": "BoundStatus" (IP binding status of the single-IP/multi-IP instance; binding or bound)
"Key": "Type" (Disused field)
"Key": "ElasticLimit" (Elastic protection value of the instance)
"Key": "DDoSAI" (Anti-DDoS AI protection switch of the instance)
"Key": "OverloadCount" (The number of attacks exceeding the elastic protection value to the instance)
"Key": "Status" (Instance status; idle: running; attacking: under attacks; blocking: being blocked; isolate: being isolated)
"Key": "Lbid" (Disused field)
"Key": "ShowFlag" (Disused field)
"Key": "Expire" (Instance expiry time)
"Key": "CCThreshold" (CC protection trigger value of the instance)
"Key": "AutoRenewFlag" (Whether the instance is on auto-renewal)
"Key": "IspCode" (Line of the single-IP/multi-IP instance; 0: China Telecom; 1: China Unicom; 2: China Mobile; 5: BGP)
"Key": "PackType" (Package type)
"Key": "PackId" (Package ID)
"Key": "Name" (Instance name)
"Key": "Locked" (Disused field)
"Key": "IpDDoSLevel" (Protection level of the instance; low: loose; middle: normal; high: strict)
"Key": "DefendStatus" (DDoS protection status of the instance; enabled or temporarily disabled)
"Key": "UndefendExpire" (End time of the temporary disabling on DDoS protection for the instance)
"Key": "Tgw" (Whether it is a new instance)
"Key": "Bandwidth" (Base protection value of the Anti-DDoS Pro/Advanced instance)
"Key": "DdosMax" (Base protection value of the Anti-DDoS Ultimate instance)
"Key": "GFBandwidth" (Base business application bandwidth of the Anti-DDoS Advanced instance)
"Key": "ServiceBandwidth" (Base business application bandwidth of the Anti-DDoS Ultimate instance)
        :type ServicePacks: list of KeyValueRecord
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ServicePacks = None
        self._Business = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ServicePacks(self):
        return self._ServicePacks

    @ServicePacks.setter
    def ServicePacks(self, ServicePacks):
        self._ServicePacks = ServicePacks

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self._ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ServicePacks.append(obj)
        self._Business = params.get("Business")
        self._RequestId = params.get("RequestId")


class DescribeRuleSetsRequest(AbstractModel):
    """DescribeRuleSets request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _IdList: Resource ID list
        :type IdList: list of str
        """
        self._Business = None
        self._IdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets response structure.

    """

    def __init__(self):
        r"""
        :param _L4RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules
        :type L4RuleSets: list of KeyValueRecord
        :param _L7RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules
        :type L7RuleSets: list of KeyValueRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._L4RuleSets = None
        self._L7RuleSets = None
        self._RequestId = None

    @property
    def L4RuleSets(self):
        return self._L4RuleSets

    @L4RuleSets.setter
    def L4RuleSets(self, L4RuleSets):
        self._L4RuleSets = L4RuleSets

    @property
    def L7RuleSets(self):
        return self._L7RuleSets

    @L7RuleSets.setter
    def L7RuleSets(self, L7RuleSets):
        self._L7RuleSets = L7RuleSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("L4RuleSets") is not None:
            self._L4RuleSets = []
            for item in params.get("L4RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._L4RuleSets.append(obj)
        if params.get("L7RuleSets") is not None:
            self._L7RuleSets = []
            for item in params.get("L7RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._L7RuleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSchedulingDomainListRequest(AbstractModel):
    """DescribeSchedulingDomainList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of items in a page. Returned results are not paged if you enter '0'.
        :type Limit: int
        :param _Offset: Starting offset of the page. Value: (number of pages - 1) * items per page
        :type Offset: int
        :param _Domain: (Optional) Filter by specific domain name
        :type Domain: str
        """
        self._Limit = None
        self._Offset = None
        self._Domain = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of scheduling domain names
        :type Total: int
        :param _DomainList: List of scheduling domain names
        :type DomainList: list of SchedulingDomain
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._DomainList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomain()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecIndexRequest(AbstractModel):
    """DescribeSecIndex request structure.

    """


class DescribeSecIndexResponse(AbstractModel):
    """DescribeSecIndex response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Field value as follows:
AttackIpCount: number of attacked IPs
AttackCount: number of attacks
BlockCount: number of blockings
MaxMbps: attack bandwidth peak in Mbps
IpNum: IP statistics
        :type Data: list of KeyValue
        :param _BeginDate: Start time of the current month
        :type BeginDate: str
        :param _EndDate: End time of the current month
        :type EndDate: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._BeginDate = None
        self._EndDate = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._RequestId = params.get("RequestId")


class DescribeSourceIpSegmentRequest(AbstractModel):
    """DescribeSourceIpSegment request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Intermediate IP range. Multiple values are separated by ";"
        :type Data: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTransmitStatisRequest(AbstractModel):
    """DescribeTransmitStatis request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _MetricName: Metric name. Valid values:
traffic: traffic bandwidth;
pkg: packet rate;
        :type MetricName: str
        :param _Period: Statistical time granularity (300: 5-minute, 3600: hourly, 86400: daily)
        :type Period: int
        :param _StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5
        :type StartTime: str
        :param _EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5
        :type EndTime: str
        :param _IpList: Resource IP, which is required and only supports one IP if `Business` is `bgp-multip`. If this field is left empty, all IPs of a resource instance will be counted by default. If the resource instance has multiple IPs (such as Anti-DDoS Ultimate), the statistical method is summation;
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis response structure.

    """

    def __init__(self):
        r"""
        :param _InDataList: If `MetricName` is `traffic`, this field indicates the inbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the inbound packet rate in pps;
        :type InDataList: list of float
        :param _OutDataList: If `MetricName` is `traffic`, this field indicates the outbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the outbound packet rate in pps;
        :type OutDataList: list of float
        :param _MetricName: Metric name:
traffic: traffic bandwidth;
pkg: packet rate;
        :type MetricName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InDataList = None
        self._OutDataList = None
        self._MetricName = None
        self._RequestId = None

    @property
    def InDataList(self):
        return self._InDataList

    @InDataList.setter
    def InDataList(self, InDataList):
        self._InDataList = InDataList

    @property
    def OutDataList(self):
        return self._OutDataList

    @OutDataList.setter
    def OutDataList(self, OutDataList):
        self._OutDataList = OutDataList

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InDataList = params.get("InDataList")
        self._OutDataList = params.get("OutDataList")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeUnBlockStatisRequest(AbstractModel):
    """DescribeUnBlockStatis request structure.

    """


class DescribeUnBlockStatisResponse(AbstractModel):
    """DescribeUnBlockStatis response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of unblocking chances
        :type Total: int
        :param _Used: Number of used chances
        :type Used: int
        :param _BeginTime: Statistics start time
        :type BeginTime: str
        :param _EndTime: Statistics end time
        :type EndTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._BeginTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribleL4RulesRequest(AbstractModel):
    """DescribleL4Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained
        :type RuleIdList: list of str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Forwarding rule list
        :type Rules: list of L4RuleEntry
        :param _Total: Total number of rules
        :type Total: int
        :param _Healths: Health check configuration list
        :type Healths: list of L4RuleHealth
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribleL7RulesRequest(AbstractModel):
    """DescribleL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained
        :type RuleIdList: list of str
        :param _Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param _Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param _Domain: Domain name search, which is optional. Enter it if you need to search for domain names
        :type Domain: str
        :param _ProtocolList: Forwarding protocol search, which is optional. Valid values: [http, https, http/https]
        :type ProtocolList: list of str
        :param _StatusList: Status search, which is optional. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]
        :type StatusList: list of int non-negative
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None
        self._Limit = None
        self._Offset = None
        self._Domain = None
        self._ProtocolList = None
        self._StatusList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtocolList(self):
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        self._ProtocolList = params.get("ProtocolList")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Forwarding rule list
        :type Rules: list of L7RuleEntry
        :param _Total: Total number of rules
        :type Total: int
        :param _Healths: Health check configuration list
        :type Healths: list of L7RuleHealth
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribleRegionCountRequest(AbstractModel):
    """DescribleRegionCount request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param _LineList: Line search. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. This field is valid only for Anti-DDoS Advanced and should be ignored for other product
        :type LineList: list of int non-negative
        """
        self._Business = None
        self._LineList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount response structure.

    """

    def __init__(self):
        r"""
        :param _RegionList: Number of resource instances in region
        :type RegionList: list of RegionInstanceCount
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInstanceCount()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class HttpStatusMap(AbstractModel):
    """Aggregated data on the HTTP status codes of business traffic

    """

    def __init__(self):
        r"""
        :param _Http2xx: HTTP 2xx Status code
        :type Http2xx: list of float
        :param _Http3xx: HTTP 3xx Status code
        :type Http3xx: list of float
        :param _Http404: HTTP 404 Status code
        :type Http404: list of float
        :param _Http4xx: HTTP 4xx Status code
        :type Http4xx: list of float
        :param _Http5xx: HTTP 5xx Status code
        :type Http5xx: list of float
        :param _SourceHttp2xx: HTTP 2xx Forwarding status code
        :type SourceHttp2xx: list of float
        :param _SourceHttp3xx: HTTP 3xx Forwarding status code
        :type SourceHttp3xx: list of float
        :param _SourceHttp404: HTTP 404 Forwarding status code
        :type SourceHttp404: list of float
        :param _SourceHttp4xx: HTTP 4xx Forwarding status code
        :type SourceHttp4xx: list of float
        :param _SourceHttp5xx: HTTP 5xx Forwarding status code
        :type SourceHttp5xx: list of float
        """
        self._Http2xx = None
        self._Http3xx = None
        self._Http404 = None
        self._Http4xx = None
        self._Http5xx = None
        self._SourceHttp2xx = None
        self._SourceHttp3xx = None
        self._SourceHttp404 = None
        self._SourceHttp4xx = None
        self._SourceHttp5xx = None

    @property
    def Http2xx(self):
        return self._Http2xx

    @Http2xx.setter
    def Http2xx(self, Http2xx):
        self._Http2xx = Http2xx

    @property
    def Http3xx(self):
        return self._Http3xx

    @Http3xx.setter
    def Http3xx(self, Http3xx):
        self._Http3xx = Http3xx

    @property
    def Http404(self):
        return self._Http404

    @Http404.setter
    def Http404(self, Http404):
        self._Http404 = Http404

    @property
    def Http4xx(self):
        return self._Http4xx

    @Http4xx.setter
    def Http4xx(self, Http4xx):
        self._Http4xx = Http4xx

    @property
    def Http5xx(self):
        return self._Http5xx

    @Http5xx.setter
    def Http5xx(self, Http5xx):
        self._Http5xx = Http5xx

    @property
    def SourceHttp2xx(self):
        return self._SourceHttp2xx

    @SourceHttp2xx.setter
    def SourceHttp2xx(self, SourceHttp2xx):
        self._SourceHttp2xx = SourceHttp2xx

    @property
    def SourceHttp3xx(self):
        return self._SourceHttp3xx

    @SourceHttp3xx.setter
    def SourceHttp3xx(self, SourceHttp3xx):
        self._SourceHttp3xx = SourceHttp3xx

    @property
    def SourceHttp404(self):
        return self._SourceHttp404

    @SourceHttp404.setter
    def SourceHttp404(self, SourceHttp404):
        self._SourceHttp404 = SourceHttp404

    @property
    def SourceHttp4xx(self):
        return self._SourceHttp4xx

    @SourceHttp4xx.setter
    def SourceHttp4xx(self, SourceHttp4xx):
        self._SourceHttp4xx = SourceHttp4xx

    @property
    def SourceHttp5xx(self):
        return self._SourceHttp5xx

    @SourceHttp5xx.setter
    def SourceHttp5xx(self, SourceHttp5xx):
        self._SourceHttp5xx = SourceHttp5xx


    def _deserialize(self, params):
        self._Http2xx = params.get("Http2xx")
        self._Http3xx = params.get("Http3xx")
        self._Http404 = params.get("Http404")
        self._Http4xx = params.get("Http4xx")
        self._Http5xx = params.get("Http5xx")
        self._SourceHttp2xx = params.get("SourceHttp2xx")
        self._SourceHttp3xx = params.get("SourceHttp3xx")
        self._SourceHttp404 = params.get("SourceHttp404")
        self._SourceHttp4xx = params.get("SourceHttp4xx")
        self._SourceHttp5xx = params.get("SourceHttp5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlackWhite(AbstractModel):
    """IP blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _Type: Blocklist/allowlist type. Valid values: [black, white]
        :type Type: str
        """
        self._Ip = None
        self._Type = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """IP blocking record

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _Status: Status (Blocked: blocked, UnBlocking: unblocking, UnBlockFailed: unblocking failed)
        :type Status: str
        :param _BlockTime: Blocked time
        :type BlockTime: str
        :param _UnBlockTime: Unblocked time (estimated)
        :type UnBlockTime: str
        :param _ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self._Ip = None
        self._Status = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def UnBlockTime(self):
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpUnBlockData(AbstractModel):
    """IP unblocking record

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _BlockTime: Blocked time
        :type BlockTime: str
        :param _UnBlockTime: Unblocked time (actual)
        :type UnBlockTime: str
        :param _ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self._Ip = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def UnBlockTime(self):
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """Field value in K-V format

    """

    def __init__(self):
        r"""
        :param _Key: Field name
        :type Key: str
        :param _Value: Field value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class KeyValueRecord(AbstractModel):
    """`KeyValue` record

    """

    def __init__(self):
        r"""
        :param _Record: Key-Value array of a record
        :type Record: list of KeyValue
        """
        self._Record = None

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Record.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4HealthConfig(AbstractModel):
    """Layer-4 health check configuration

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: [TCP, UDP]
        :type Protocol: str
        :param _VirtualPort: Forwarding port
        :type VirtualPort: int
        :param _Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param _TimeOut: Response timeout period in seconds
        :type TimeOut: int
        :param _Interval: Detection interval in seconds
        :type Interval: int
        :param _KickNum: Unhealthy threshold in times.
        :type KickNum: int
        :param _AliveNum: Healthy threshold in times.
        :type AliveNum: int
        :param _KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        """
        self._Protocol = None
        self._VirtualPort = None
        self._Enable = None
        self._TimeOut = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._KeepTime = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VirtualPort = params.get("VirtualPort")
        self._Enable = params.get("Enable")
        self._TimeOut = params.get("TimeOut")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleEntry(AbstractModel):
    """Layer-4 rule

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: [TCP, UDP]
        :type Protocol: str
        :param _VirtualPort: Forwarding port
        :type VirtualPort: int
        :param _SourcePort: Real server port
        :type SourcePort: int
        :param _SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]
        :type SourceType: int
        :param _KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        :param _SourceList: Forward list
        :type SourceList: list of L4RuleSource
        :param _LbType: Load balancing method. Valid values: [1 (weighted round robin), 2 (source IP hash)]
        :type LbType: int
        :param _KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)];
        :type KeepEnable: int
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleName: Rule description
        :type RuleName: str
        :param _RemoveSwitch: Watermark removal status. Valid values: [0 (disabled), 1 (enabled)]
        :type RemoveSwitch: int
        """
        self._Protocol = None
        self._VirtualPort = None
        self._SourcePort = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._RuleName = None
        self._RemoveSwitch = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SourcePort(self):
        return self._SourcePort

    @SourcePort.setter
    def SourcePort(self, SourcePort):
        self._SourcePort = SourcePort

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RemoveSwitch(self):
        return self._RemoveSwitch

    @RemoveSwitch.setter
    def RemoveSwitch(self, RemoveSwitch):
        self._RemoveSwitch = RemoveSwitch


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VirtualPort = params.get("VirtualPort")
        self._SourcePort = params.get("SourcePort")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RemoveSwitch = params.get("RemoveSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleHealth(AbstractModel):
    """Rule health check parameter

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param _TimeOut: Response timeout period in seconds
        :type TimeOut: int
        :param _Interval: Detection interval in seconds, which must be greater than the response timeout period
        :type Interval: int
        :param _KickNum: Unhealthy threshold in times
        :type KickNum: int
        :param _AliveNum: Healthy threshold in times.
        :type AliveNum: int
        """
        self._RuleId = None
        self._Enable = None
        self._TimeOut = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Enable = params.get("Enable")
        self._TimeOut = params.get("TimeOut")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleSource(AbstractModel):
    """Layer-4 forwarding rule list

    """

    def __init__(self):
        r"""
        :param _Source: Intermediate IP or domain name
        :type Source: str
        :param _Weight: Weight value. Value range: [0,100]
        :type Weight: int
        """
        self._Source = None
        self._Weight = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7HealthConfig(AbstractModel):
    """Layer-7 health check configuration

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: [http, https, http/https]
        :type Protocol: str
        :param _Domain: Forwarding domain name
        :type Domain: str
        :param _Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param _Interval: Detection interval in seconds
        :type Interval: int
        :param _KickNum: Number of exceptions in times
        :type KickNum: int
        :param _AliveNum: Number of health checks in times
        :type AliveNum: int
        :param _Method: Health check detection method. Valid values: HEAD, GET. Default VALUE: HEAD
        :type Method: str
        :param _StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up
        :type StatusCode: int
        :param _Url: URL of checked directory. Default value: /
        :type Url: str
        """
        self._Protocol = None
        self._Domain = None
        self._Enable = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._Method = None
        self._StatusCode = None
        self._Url = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """Layer-7 rule

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: [http, https]
        :type Protocol: str
        :param _Domain: Forwarding domain name
        :type Domain: str
        :param _SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]
        :type SourceType: int
        :param _KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        :param _SourceList: Forward list
        :type SourceList: list of L4RuleSource
        :param _LbType: Load balancing method. Valid value: [1 (weighted round robin)]
        :type LbType: int
        :param _KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]
        :type KeepEnable: int
        :param _RuleId: Rule ID, which is optional when adding a new rule but required when modifying or deleting a rule;
        :type RuleId: str
        :param _CertType: Certificate source, which is required if the forwarding protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]. If the forwarding protocol is HTTP, 0 can be entered for this field
        :type CertType: int
        :param _SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID
        :type SSLId: str
        :param _Cert: If the certificate is an external certificate, this field must be entered with the certificate content. (As external certificates are no longer supported, this field has been disused and does not need to be entered)
        :type Cert: str
        :param _PrivateKey: If the certificate is an external certificate, this field must be entered with the certificate key. (As external certificates are no longer supported, this field has been disused and does not need to be entered)
        :type PrivateKey: str
        :param _RuleName: Rule description
        :type RuleName: str
        :param _Status: Rule status. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]
        :type Status: int
        :param _CCStatus: CC protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type CCStatus: int
        :param _CCEnable: HTTPS CC protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type CCEnable: int
        :param _CCThreshold: HTTPS CC protection threshold
        :type CCThreshold: int
        :param _CCLevel: HTTPS CC protection level
        :type CCLevel: str
        :param _HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.
        :type HttpsToHttpEnable: int
        :param _VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPort: int
        """
        self._Protocol = None
        self._Domain = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._RuleName = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CCStatus(self):
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCLevel(self):
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def HttpsToHttpEnable(self):
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """Layer-7 rule health check parameter

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param _Interval: Detection interval in seconds
        :type Interval: int
        :param _KickNum: Unhealthy threshold in times.
        :type KickNum: int
        :param _AliveNum: Healthy threshold in times.
        :type AliveNum: int
        :param _Method: HTTP request method. Valid values: [HEAD, GET]
        :type Method: str
        :param _StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up
        :type StatusCode: int
        :param _Url: URL of checked directory. Default value: /
        :type Url: str
        :param _Status: Configuration status. 0: normal, 1: configuring, 2: configuration failed
        :type Status: int
        """
        self._RuleId = None
        self._Enable = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._Method = None
        self._StatusCode = None
        self._Url = None
        self._Status = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RsId: Anti-DDoS instance ID
        :type RsId: str
        :param _AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value). It is set to 1000 on the backend by default
        :type AlarmThreshold: int
        :param _IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs
        :type IpList: list of str
        """
        self._Business = None
        self._RsId = None
        self._AlarmThreshold = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesRequest(AbstractModel):
    """ModifyCCFrequencyRules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _CCFrequencyRuleId: CC access frequency control rule ID
        :type CCFrequencyRuleId: str
        :param _Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param _Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param _ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param _Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param _ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        :param _Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param _UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param _Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        """
        self._Business = None
        self._CCFrequencyRuleId = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesStatusRequest(AbstractModel):
    """ModifyCCFrequencyRulesStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API
        :type RuleId: str
        :param _Method: Enables or disable. Valid values: ["on", "off"]
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCHostProtectionRequest(AbstractModel):
    """ModifyCCHostProtection request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Method: Enables/disables CC domain name protection. Valid values: [open (enable), close (disable)]
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCIpAllowDenyRequest(AbstractModel):
    """ModifyCCIpAllowDeny request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Method: add: add, delete: delete
        :type Method: str
        :param _Type: Blocklist/allowlist type. Valid values: [white (allowlist), black (blocklist)]
        :type Type: str
        :param _IpList: Blocklisted/whitelisted IP array
        :type IpList: list of str
        :param _Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;
        :type Protocol: str
        :param _Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;
        :type Domain: str
        :param _RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API),
If `Method` is `delete`, this field can be left empty;
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._Type = None
        self._IpList = None
        self._Protocol = None
        self._Domain = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._Type = params.get("Type")
        self._IpList = params.get("IpList")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCLevelRequest(AbstractModel):
    """ModifyCCLevel request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Level: CC protection level. Valid values: [default (normal), loose (loose), strict (strict)];
        :type Level: str
        :param _Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;
        :type Protocol: str
        :param _RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API);
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Level = None
        self._Protocol = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCPolicySwitchRequest(AbstractModel):
    """ModifyCCPolicySwitch request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _SetId: Policy ID
        :type SetId: str
        :param _Switch: Status
        :type Switch: int
        """
        self._Business = None
        self._Id = None
        self._SetId = None
        self._Switch = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCSelfDefinePolicyRequest(AbstractModel):
    """ModifyCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _SetId: Policy ID
        :type SetId: str
        :param _Policy: Details of the CC protection policy
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self._Business = None
        self._Id = None
        self._SetId = None
        self._Policy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        if params.get("Policy") is not None:
            self._Policy = CCPolicy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCThresholdRequest(AbstractModel):
    """ModifyCCThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Threshold: CC protection threshold. Valid values: (0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
If `Business` is Anti-DDoS Advanced or Anti-DDoS Ultimate, its maximum CC protection threshold is subject to the base protection bandwidth in the following way:
  Base bandwidth: maximum CC protection threshold
  10:  20000,
  20:  40000,
  30:  70000,
  40:  100000,
  50:  150000,
  60:  200000,
  80:  250000,
  100: 300000,
        :type Threshold: int
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;
        :type Protocol: str
        :param _RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API);
Required if `Protocol` is `https`;
        :type RuleId: str
        :param _BasicIp: Queried IP address (only provided by Anti-DDoS Basic), such as 1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: IP region (only provided for Anti-DDoS Basic). Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param _BasicBizType: Zone type (only provided for Anti-DDoS Basic). Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param _BasicDeviceType: Device type (only provided for Anti-DDoS Basic). Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param _BasicIpInstance: IPInstance Nat gateway (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param _BasicIspCode: ISP line (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        :param _Domain: This optional field must be specified when HTTPS protocol is used.
        :type Domain: str
        """
        self._Business = None
        self._Threshold = None
        self._Id = None
        self._Protocol = None
        self._RuleId = None
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicIpInstance = None
        self._BasicIspCode = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Threshold = params.get("Threshold")
        self._Id = params.get("Id")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCUrlAllowRequest(AbstractModel):
    """ModifyCCUrlAllow request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Method: add: add, delete: delete
        :type Method: str
        :param _Type: Blocklist/allowlist type. Valid value: [white (allowlist)]
        :type Type: str
        :param _UrlList: URL array. URL format:
http://domain name/cgi
https://domain name/cgi
        :type UrlList: list of str
        :param _Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;
        :type Protocol: str
        :param _Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;
        :type Domain: str
        :param _RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only when adding a rule and `Protocol` is `https`;
If `Method` is `delete`, this field can be left empty;
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._Type = None
        self._UrlList = None
        self._Protocol = None
        self._Domain = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UrlList(self):
        return self._UrlList

    @UrlList.setter
    def UrlList(self, UrlList):
        self._UrlList = UrlList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._Type = params.get("Type")
        self._UrlList = params.get("UrlList")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSAIStatusRequest(AbstractModel):
    """ModifyDDoSAIStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Method: get (read AI protection status), set (modify AI protection status);
        :type Method: str
        :param _DDoSAI: AI protection status, which is required if `Method` is `set`. Valid values: [on, off].
        :type DDoSAI: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._DDoSAI = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus response structure.

    """

    def __init__(self):
        r"""
        :param _DDoSAI: AI protection status. Valid values: [on, off]
        :type DDoSAI: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DDoSAI = None
        self._Id = None
        self._RequestId = None

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DDoSAI = params.get("DDoSAI")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ModifyDDoSAlarmThresholdRequest(AbstractModel):
    """ModifyDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _RsId: Anti-DDoS instance ID
        :type RsId: str
        :param _AlarmType: Alarm threshold type. 0: not set, 1: inbound traffic, 2: cleansed traffic
        :type AlarmType: int
        :param _AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)
        :type AlarmThreshold: int
        :param _IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs
        :type IpList: list of str
        """
        self._Business = None
        self._RsId = None
        self._AlarmType = None
        self._AlarmThreshold = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSDefendStatusRequest(AbstractModel):
    """ModifyDDoSDefendStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Status: Protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type Status: int
        :param _Hour: Disablement duration in hours. Valid values: [0, 1, 2, 3, 4, 5, 6]. If `Status` is `0` (indicating to disable), `Hour` must be greater than 0;
        :type Hour: int
        :param _Id: Resource ID, which is required if `Business` is not Anti-DDoS Basic;
        :type Id: str
        :param _Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param _BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param _DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param _InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param _IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
"bj":     North China (Beijing)
"cd":     Southwest China (Chengdu)
"cq":     Southwest China (Chongqing)
"gz":     South China (Guangzhou)
"gzopen": South China (Guangzhou Open)
"hk":     Hong Kong (China)
"kr":     Southeast Asia (Seoul)
"sh":     East China (Shanghai)
"shjr":   East China (Shanghai Finance)
"szjr":   South China (Shenzhen Finance)
"sg":     Southeast Asia (Singapore)
"th":     Southeast Asia (Thailand)
"de":     Europe (Germany)
"usw":    West US (Silicon Valley)
"ca":     North America (Toronto)
"jp":     Japan
"hzec":   Hangzhou
"in":     India
"use":    East US (Virginia)
"ru":     Russia
"tpe":    Taiwan (China)
"nj":     Nanjing
        :type IPRegion: str
        """
        self._Business = None
        self._Status = None
        self._Hour = None
        self._Id = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Status = params.get("Status")
        self._Hour = params.get("Hour")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Method: get (read protection level), set (modify protection level);
        :type Method: str
        :param _DDoSLevel: Protection level, which is required if `Method` is `set`. Valid values: [low,middle,high]
        :type DDoSLevel: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._DDoSLevel = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _DDoSLevel: Protection level. Valid values: [low,middle,high]
        :type DDoSLevel: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._DDoSLevel = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DDoSLevel = params.get("DDoSLevel")
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyCaseRequest(AbstractModel):
    """ModifyDDoSPolicyCase request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _SceneId: Policy scenario ID
        :type SceneId: str
        :param _PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]
        :type PlatformTypes: list of str
        :param _AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]
        :type AppType: str
        :param _AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]
        :type AppProtocols: list of str
        :param _TcpSportStart: TCP start port. Value range: (0, 65535]
        :type TcpSportStart: str
        :param _TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port
        :type TcpSportEnd: str
        :param _UdpSportStart: UDP start port. Value range: (0, 65535]
        :type UdpSportStart: str
        :param _UdpSportEnd: End UDP business port. Value range: (0, 65535). It must be greater than or equal to the start UDP business port
        :type UdpSportEnd: str
        :param _HasAbroad: Whether there are customers outside Mainland China. Valid values: [no, yes]
        :type HasAbroad: str
        :param _HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]
        :type HasInitiateTcp: str
        :param _HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]
        :type HasInitiateUdp: str
        :param _PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]
        :type PeerTcpPort: str
        :param _PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]
        :type PeerUdpPort: str
        :param _TcpFootprint: Fixed feature code of TCP payload. String length limit: 512
        :type TcpFootprint: str
        :param _UdpFootprint: Fixed feature code of UDP payload. String length limit: 512
        :type UdpFootprint: str
        :param _WebApiUrl: Web business API URL
        :type WebApiUrl: list of str
        :param _MinTcpPackageLen: Minimum length of TCP business packet. Value range: (0, 1500)
        :type MinTcpPackageLen: str
        :param _MaxTcpPackageLen: Maximum length of TCP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP business packet
        :type MaxTcpPackageLen: str
        :param _MinUdpPackageLen: Minimum length of UDP business packet. Value range: (0, 1500)
        :type MinUdpPackageLen: str
        :param _MaxUdpPackageLen: Maximum length of UDP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP business packet
        :type MaxUdpPackageLen: str
        :param _HasVPN: Whether there are VPN businesses. Valid values: [no, yes]
        :type HasVPN: str
        :param _TcpPortList: TCP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param _UdpPortList: UDP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self._Business = None
        self._SceneId = None
        self._PlatformTypes = None
        self._AppType = None
        self._AppProtocols = None
        self._TcpSportStart = None
        self._TcpSportEnd = None
        self._UdpSportStart = None
        self._UdpSportEnd = None
        self._HasAbroad = None
        self._HasInitiateTcp = None
        self._HasInitiateUdp = None
        self._PeerTcpPort = None
        self._PeerUdpPort = None
        self._TcpFootprint = None
        self._UdpFootprint = None
        self._WebApiUrl = None
        self._MinTcpPackageLen = None
        self._MaxTcpPackageLen = None
        self._MinUdpPackageLen = None
        self._MaxUdpPackageLen = None
        self._HasVPN = None
        self._TcpPortList = None
        self._UdpPortList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def PlatformTypes(self):
        return self._PlatformTypes

    @PlatformTypes.setter
    def PlatformTypes(self, PlatformTypes):
        self._PlatformTypes = PlatformTypes

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppProtocols(self):
        return self._AppProtocols

    @AppProtocols.setter
    def AppProtocols(self, AppProtocols):
        self._AppProtocols = AppProtocols

    @property
    def TcpSportStart(self):
        return self._TcpSportStart

    @TcpSportStart.setter
    def TcpSportStart(self, TcpSportStart):
        self._TcpSportStart = TcpSportStart

    @property
    def TcpSportEnd(self):
        return self._TcpSportEnd

    @TcpSportEnd.setter
    def TcpSportEnd(self, TcpSportEnd):
        self._TcpSportEnd = TcpSportEnd

    @property
    def UdpSportStart(self):
        return self._UdpSportStart

    @UdpSportStart.setter
    def UdpSportStart(self, UdpSportStart):
        self._UdpSportStart = UdpSportStart

    @property
    def UdpSportEnd(self):
        return self._UdpSportEnd

    @UdpSportEnd.setter
    def UdpSportEnd(self, UdpSportEnd):
        self._UdpSportEnd = UdpSportEnd

    @property
    def HasAbroad(self):
        return self._HasAbroad

    @HasAbroad.setter
    def HasAbroad(self, HasAbroad):
        self._HasAbroad = HasAbroad

    @property
    def HasInitiateTcp(self):
        return self._HasInitiateTcp

    @HasInitiateTcp.setter
    def HasInitiateTcp(self, HasInitiateTcp):
        self._HasInitiateTcp = HasInitiateTcp

    @property
    def HasInitiateUdp(self):
        return self._HasInitiateUdp

    @HasInitiateUdp.setter
    def HasInitiateUdp(self, HasInitiateUdp):
        self._HasInitiateUdp = HasInitiateUdp

    @property
    def PeerTcpPort(self):
        return self._PeerTcpPort

    @PeerTcpPort.setter
    def PeerTcpPort(self, PeerTcpPort):
        self._PeerTcpPort = PeerTcpPort

    @property
    def PeerUdpPort(self):
        return self._PeerUdpPort

    @PeerUdpPort.setter
    def PeerUdpPort(self, PeerUdpPort):
        self._PeerUdpPort = PeerUdpPort

    @property
    def TcpFootprint(self):
        return self._TcpFootprint

    @TcpFootprint.setter
    def TcpFootprint(self, TcpFootprint):
        self._TcpFootprint = TcpFootprint

    @property
    def UdpFootprint(self):
        return self._UdpFootprint

    @UdpFootprint.setter
    def UdpFootprint(self, UdpFootprint):
        self._UdpFootprint = UdpFootprint

    @property
    def WebApiUrl(self):
        return self._WebApiUrl

    @WebApiUrl.setter
    def WebApiUrl(self, WebApiUrl):
        self._WebApiUrl = WebApiUrl

    @property
    def MinTcpPackageLen(self):
        return self._MinTcpPackageLen

    @MinTcpPackageLen.setter
    def MinTcpPackageLen(self, MinTcpPackageLen):
        self._MinTcpPackageLen = MinTcpPackageLen

    @property
    def MaxTcpPackageLen(self):
        return self._MaxTcpPackageLen

    @MaxTcpPackageLen.setter
    def MaxTcpPackageLen(self, MaxTcpPackageLen):
        self._MaxTcpPackageLen = MaxTcpPackageLen

    @property
    def MinUdpPackageLen(self):
        return self._MinUdpPackageLen

    @MinUdpPackageLen.setter
    def MinUdpPackageLen(self, MinUdpPackageLen):
        self._MinUdpPackageLen = MinUdpPackageLen

    @property
    def MaxUdpPackageLen(self):
        return self._MaxUdpPackageLen

    @MaxUdpPackageLen.setter
    def MaxUdpPackageLen(self, MaxUdpPackageLen):
        self._MaxUdpPackageLen = MaxUdpPackageLen

    @property
    def HasVPN(self):
        return self._HasVPN

    @HasVPN.setter
    def HasVPN(self, HasVPN):
        self._HasVPN = HasVPN

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        self._PlatformTypes = params.get("PlatformTypes")
        self._AppType = params.get("AppType")
        self._AppProtocols = params.get("AppProtocols")
        self._TcpSportStart = params.get("TcpSportStart")
        self._TcpSportEnd = params.get("TcpSportEnd")
        self._UdpSportStart = params.get("UdpSportStart")
        self._UdpSportEnd = params.get("UdpSportEnd")
        self._HasAbroad = params.get("HasAbroad")
        self._HasInitiateTcp = params.get("HasInitiateTcp")
        self._HasInitiateUdp = params.get("HasInitiateUdp")
        self._PeerTcpPort = params.get("PeerTcpPort")
        self._PeerUdpPort = params.get("PeerUdpPort")
        self._TcpFootprint = params.get("TcpFootprint")
        self._UdpFootprint = params.get("UdpFootprint")
        self._WebApiUrl = params.get("WebApiUrl")
        self._MinTcpPackageLen = params.get("MinTcpPackageLen")
        self._MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self._MinUdpPackageLen = params.get("MinUdpPackageLen")
        self._MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self._HasVPN = params.get("HasVPN")
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyNameRequest(AbstractModel):
    """ModifyDDoSPolicyName request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _Name: Policy name
        :type Name: str
        """
        self._Business = None
        self._PolicyId = None
        self._Name = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _DropOptions: Protocol disablement, which must be entered, and the array length must be 1
        :type DropOptions: list of DDoSPolicyDropOption
        :param _PortLimits: Port disablement. If no ports are to be disabled, enter an empty array
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _IpAllowDenys: IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist
        :type IpAllowDenys: list of IpBlackWhite
        :param _PacketFilters: Packet filter. Enter an empty array if there are no packets to filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _WaterPrint: Watermarking policy parameter. Enter an empty array if the watermarking feature is not enabled. At most one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)
        :type WaterPrint: list of WaterPrintPolicy
        """
        self._Business = None
        self._PolicyId = None
        self._DropOptions = None
        self._PortLimits = None
        self._IpAllowDenys = None
        self._PacketFilters = None
        self._WaterPrint = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def IpAllowDenys(self):
        return self._IpAllowDenys

    @IpAllowDenys.setter
    def IpAllowDenys(self, IpAllowDenys):
        self._IpAllowDenys = IpAllowDenys

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        if params.get("DropOptions") is not None:
            self._DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self._DropOptions.append(obj)
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self._IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
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
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSSwitchRequest(AbstractModel):
    """ModifyDDoSSwitch request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Method: `get`: read DDoS protection status, `set`: modify DDoS protection status
        :type Method: str
        :param _Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param _BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param _DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param _InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param _IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
"bj":     North China (Beijing)
"cd":     Southwest China (Chengdu)
"cq":     Southwest China (Chongqing)
"gz":     South China (Guangzhou)
"gzopen": South China (Guangzhou Open)
"hk":     Hong Kong (China)
"kr":     Southeast Asia (Seoul)
"sh":     East China (Shanghai)
"shjr":   East China (Shanghai Finance)
"szjr":   South China (Shenzhen Finance)
"sg":     Southeast Asia (Singapore)
"th":     Southeast Asia (Thailand)
"de":     Europe (Germany)
"usw":    West US (Silicon Valley)
"ca":     North America (Toronto)
"jp":     Japan
"hzec":   Hangzhou
"in":     India
"use":    East US (Virginia)
"ru":     Russia
"tpe":    Taiwan (China)
"nj":     Nanjing
        :type IPRegion: str
        :param _Status: Protection status value, which is optional. Valid values: [0 (disabled), 1 (enabled)]. If `Method` is `get`, this field can be left empty;
        :type Status: int
        """
        self._Business = None
        self._Method = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None
        self._Status = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Method = params.get("Method")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Current protection status value. Valid values: [0 (disabled), 1 (enabled)]
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Threshold: DDoS cleansing threshold. Valid values: [0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
If the value is set to 0, the default value will be used;
        :type Threshold: int
        """
        self._Business = None
        self._Id = None
        self._Threshold = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSWaterKeyRequest(AbstractModel):
    """ModifyDDoSWaterKey request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _Method: Key operation. Valid values: [add (add), delete (delete), open (open), close (close), get (get key)]
        :type Method: str
        :param _KeyId: Key ID, which can be left empty or 0 when adding a key but is required for other operations
        :type KeyId: int
        """
        self._Business = None
        self._PolicyId = None
        self._Method = None
        self._KeyId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        self._Method = params.get("Method")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyList: Watermark key list
        :type KeyList: list of WaterPrintKey
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyList = None
        self._RequestId = None

    @property
    def KeyList(self):
        return self._KeyList

    @KeyList.setter
    def KeyList(self, KeyList):
        self._KeyList = KeyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self._KeyList = []
            for item in params.get("KeyList"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._KeyList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyElasticLimitRequest(AbstractModel):
    """ModifyElasticLimit request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Limit: Elastic protection threshold. Valid values: [0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]
        :type Limit: int
        """
        self._Business = None
        self._Id = None
        self._Limit = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4HealthRequest(AbstractModel):
    """ModifyL4Health request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Healths: Health check parameter array
        :type Healths: list of L4RuleHealth
        """
        self._Business = None
        self._Id = None
        self._Healths = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4KeepTimeRequest(AbstractModel):
    """ModifyL4KeepTime request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]
        :type KeepEnable: int
        :param _KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._KeepEnable = None
        self._KeepTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._KeepEnable = params.get("KeepEnable")
        self._KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4RulesRequest(AbstractModel):
    """ModifyL4Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Rule: Rule
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L4RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL7RulesRequest(AbstractModel):
    """ModifyL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Rule: Rule
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L7RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyNetReturnSwitchRequest(AbstractModel):
    """ModifyNetReturnSwitch request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _Status: Switch status. 0: disabled, 1: enabled
        :type Status: int
        :param _Hour: Switch duration in hours. Valid values: [0,1,2,3,4,5,6;]. If `status` is 1, this field is required and must be greater than 0
        :type Hour: int
        """
        self._Business = None
        self._Id = None
        self._Status = None
        self._Hour = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Hour = params.get("Hour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param _Id: Anti-DDoS instance ID.
        :type Id: str
        :param _Rule: Domain name forwarding rule.
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.NewL7RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = NewL7RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyNewL4RuleRequest(AbstractModel):
    """ModifyNewL4Rule request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param _Id: Anti-DDoS instance ID.
        :type Id: str
        :param _Rule: Forwarding rule.
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L4RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewL4RuleResponse(AbstractModel):
    """ModifyNewL4Rule response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyResBindDDoSPolicyRequest(AbstractModel):
    """ModifyResBindDDoSPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _Method: bind: bind policy; unbind: unbind policy
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._PolicyId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._PolicyId = params.get("PolicyId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyResourceRenewFlagRequest(AbstractModel):
    """ModifyResourceRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `shield`: Chess Shield, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `insurance`: guarantee package, `staticpack`: non-BGP package
        :type Business: str
        :param _Id: Resource ID
        :type Id: str
        :param _RenewFlag: Auto-renewal flag (0: manual renewal, 1: auto-renewal, 2: no renewal upon expiration)
        :type RenewFlag: int
        """
        self._Business = None
        self._Id = None
        self._RenewFlag = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class NewL7RuleEntry(AbstractModel):
    """Layer-7 rule.

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: `http` and `https`.
        :type Protocol: str
        :param _Domain: Forwarding domain name.
        :type Domain: str
        :param _SourceType: Forwarding method. Valid values: `1` (by domain name); `2` (by IP).
        :type SourceType: int
        :param _KeepTime: Session persistence duration, in seconds.
        :type KeepTime: int
        :param _SourceList: List of sources
        :type SourceList: list of L4RuleSource
        :param _LbType: Load balancing method. Valid value: `1` (weighed polling).
        :type LbType: int
        :param _KeepEnable: Whether session persistence is enabled. Valid values: `0` (disabled) and `1` (enabled).
        :type KeepEnable: int
        :param _RuleId: Rule ID. This field is not required for adding a rule, but is required for modifying or deleting a rule.
        :type RuleId: str
        :param _CertType: Certificate source. When the forwarding protocol is HTTPS, this field must be set to `2` (Tencent Cloud managed certificate), and for HTTP protocol, it can be set to `0`.
        :type CertType: int
        :param _SSLId: When the certificate source is Tencent Cloud managed certificate, this field must be set to the ID of the managed certificate.
        :type SSLId: str
        :param _Cert: [Disused] When the certificate is an external certificate, the certificate content should be provided here. 
        :type Cert: str
        :param _PrivateKey: [Disused] When the certificate is an external certificate, the certificate key should be provided here. 
        :type PrivateKey: str
        :param _RuleName: Rule description.
        :type RuleName: str
        :param _Status: Rule status. Valid values: `0` (the rule was successfully configured), `1` (configuring the rule), `2` (rule configuration failed), `3` (deleting the rule), `5` (failed to delete rule), `6` (rule awaiting configuration), `7` (rule awaiting deletion), and `8` (rule awaiting certificate configuration).
        :type Status: int
        :param _CCStatus: CC protection status. Valid values: `0` (disabled) and `1` (enabled).
        :type CCStatus: int
        :param _CCEnable: CC protection status based on HTTPS. Valid values: `0` (disabled) and `1` (enabled).
        :type CCEnable: int
        :param _CCThreshold: CC protection threshold based on HTTPS.
        :type CCThreshold: int
        :param _CCLevel: CC protection level based on HTTPS.
        :type CCLevel: str
        :param _Region: Region code.
        :type Region: int
        :param _Id: Anti-DDoS instance ID.
        :type Id: str
        :param _Ip: Anti-DDoS instance IP address.
        :type Ip: str
        :param _ModifyTime: Modification time.
        :type ModifyTime: str
        :param _HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.
        :type HttpsToHttpEnable: int
        :param _VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPort: int
        """
        self._Protocol = None
        self._Domain = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._RuleName = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._Region = None
        self._Id = None
        self._Ip = None
        self._ModifyTime = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CCStatus(self):
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCLevel(self):
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def HttpsToHttpEnable(self):
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._ModifyTime = params.get("ModifyTime")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    """Sort by field

    """

    def __init__(self):
        r"""
        :param _Field: Sort by field name. Valid values: [
bandwidth (bandwidth),
overloadCount (number of times of exceeding peak value)
]
        :type Field: str
        :param _Order: Sorting order. Valid values: [asc (ascending), desc (descending)]
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """Pagination index

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position
        :type Offset: int
        :param _Limit: Quantity
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """Protocol and port parameters

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol (TCP, UDP)
        :type Protocol: str
        :param _Port: Port
        :type Port: int
        """
        self._Protocol = None
        self._Port = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstanceCount(AbstractModel):
    """Number of resource instances in region

    """

    def __init__(self):
        r"""
        :param _Region: Region code
        :type Region: str
        :param _RegionV3: Region code (new specification)
        :type RegionV3: str
        :param _Count: Number of resource instances
        :type Count: int
        """
        self._Region = None
        self._RegionV3 = None
        self._Count = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionV3(self):
        return self._RegionV3

    @RegionV3.setter
    def RegionV3(self, RegionV3):
        self._RegionV3 = RegionV3

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionV3 = params.get("RegionV3")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIp(AbstractModel):
    """Resource IP array

    """

    def __init__(self):
        r"""
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _IpList: Resource IP array
        :type IpList: list of str
        """
        self._Id = None
        self._IpList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomain(AbstractModel):
    """Scheduling domain name information

    """

    def __init__(self):
        r"""
        :param _Domain: Scheduling domain name
        :type Domain: str
        :param _BGPIpList: List of BGP IPs
        :type BGPIpList: list of str
        :param _CTCCIpList: List of CTCC IPs
        :type CTCCIpList: list of str
        :param _CUCCIpList: List of CUCC IPs
        :type CUCCIpList: list of str
        :param _CMCCIpList: List of CMCC IPs
        :type CMCCIpList: list of str
        :param _OverseaIpList: List of IPs outside Mainland China
        :type OverseaIpList: list of str
        :param _Method: Scheduling method. It only supports `priority` now.
        :type Method: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _TTL: 
        :type TTL: int
        :param _Status: Status
        :type Status: int
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._Domain = None
        self._BGPIpList = None
        self._CTCCIpList = None
        self._CUCCIpList = None
        self._CMCCIpList = None
        self._OverseaIpList = None
        self._Method = None
        self._CreateTime = None
        self._TTL = None
        self._Status = None
        self._ModifyTime = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def BGPIpList(self):
        return self._BGPIpList

    @BGPIpList.setter
    def BGPIpList(self, BGPIpList):
        self._BGPIpList = BGPIpList

    @property
    def CTCCIpList(self):
        return self._CTCCIpList

    @CTCCIpList.setter
    def CTCCIpList(self, CTCCIpList):
        self._CTCCIpList = CTCCIpList

    @property
    def CUCCIpList(self):
        return self._CUCCIpList

    @CUCCIpList.setter
    def CUCCIpList(self, CUCCIpList):
        self._CUCCIpList = CUCCIpList

    @property
    def CMCCIpList(self):
        return self._CMCCIpList

    @CMCCIpList.setter
    def CMCCIpList(self, CMCCIpList):
        self._CMCCIpList = CMCCIpList

    @property
    def OverseaIpList(self):
        return self._OverseaIpList

    @OverseaIpList.setter
    def OverseaIpList(self, OverseaIpList):
        self._OverseaIpList = OverseaIpList

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._BGPIpList = params.get("BGPIpList")
        self._CTCCIpList = params.get("CTCCIpList")
        self._CUCCIpList = params.get("CUCCIpList")
        self._CMCCIpList = params.get("CMCCIpList")
        self._OverseaIpList = params.get("OverseaIpList")
        self._Method = params.get("Method")
        self._CreateTime = params.get("CreateTime")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """Operation return code, which is only used to return success

    """

    def __init__(self):
        r"""
        :param _Code: Success/error code
        :type Code: str
        :param _Message: Description
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """Watermark key

    """

    def __init__(self):
        r"""
        :param _KeyId: Watermark key ID
        :type KeyId: str
        :param _KeyContent: Watermark key value
        :type KeyContent: str
        :param _KeyVersion: Watermark key version number
        :type KeyVersion: str
        :param _OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]
        :type OpenStatus: int
        :param _CreateTime: Key generation time
        :type CreateTime: str
        """
        self._KeyId = None
        self._KeyContent = None
        self._KeyVersion = None
        self._OpenStatus = None
        self._CreateTime = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyContent(self):
        return self._KeyContent

    @KeyContent.setter
    def KeyContent(self, KeyContent):
        self._KeyContent = KeyContent

    @property
    def KeyVersion(self):
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyContent = params.get("KeyContent")
        self._KeyVersion = params.get("KeyVersion")
        self._OpenStatus = params.get("OpenStatus")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintPolicy(AbstractModel):
    """Watermarking policy parameter

    """

    def __init__(self):
        r"""
        :param _TcpPortList: TCP port range, such as ["2000-3000","3500-4000"]
        :type TcpPortList: list of str
        :param _UdpPortList: UDP port range, such as ["2000-3000","3500-4000"]
        :type UdpPortList: list of str
        :param _Offset: Watermark offset. Value range: [0, 100)
        :type Offset: int
        :param _RemoveSwitch: Whether to automatically remove. Valid values: [0 (no), 1 (yes)]
        :type RemoveSwitch: int
        :param _OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]
        :type OpenStatus: int
        """
        self._TcpPortList = None
        self._UdpPortList = None
        self._Offset = None
        self._RemoveSwitch = None
        self._OpenStatus = None

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RemoveSwitch(self):
        return self._RemoveSwitch

    @RemoveSwitch.setter
    def RemoveSwitch(self, RemoveSwitch):
        self._RemoveSwitch = RemoveSwitch

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus


    def _deserialize(self, params):
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        self._Offset = params.get("Offset")
        self._RemoveSwitch = params.get("RemoveSwitch")
        self._OpenStatus = params.get("OpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        