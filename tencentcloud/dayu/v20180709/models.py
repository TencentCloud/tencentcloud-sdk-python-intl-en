# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class BaradData(AbstractModel):
    """Data returned by Barad

    """

    def __init__(self):
        """
        :param MetricName: Metric name (connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;)
        :type MetricName: str
        :param Data: Value array
        :type Data: list of float
        :param Count: Value array size
        :type Count: int
        """
        self.MetricName = None
        self.Data = None
        self.Count = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Data = params.get("Data")
        self.Count = params.get("Count")


class BoundIpInfo(AbstractModel):
    """IP object bound to Anti-DDoS Pro

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param BizType: Bound product type. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param DeviceType: Subtype under product type. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param InstanceId: Resource instance ID of IP. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`; if it is a hosted IP without corresponding resource instance ID, enter "none";
        :type InstanceId: str
        """
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")


class CCAlarmThreshold(AbstractModel):
    """CC alarm threshold

    """

    def __init__(self):
        """
        :param AlarmThreshold: CC alarm threshold
        :type AlarmThreshold: int
        """
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")


class CCEventRecord(AbstractModel):
    """CC attack event record

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Vip: Resource IP
        :type Vip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param ReqQps: Total requests peak (QPS)
        :type ReqQps: int
        :param DropQps: Attack peak (QPS)
        :type DropQps: int
        :param AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]
        :type AttackStatus: int
        :param ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param DomainList: Domain name list
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainList: str
        :param UriList: URI list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UriList: str
        :param AttackipList: Attack source list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttackipList: str
        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.ReqQps = None
        self.DropQps = None
        self.AttackStatus = None
        self.ResourceName = None
        self.DomainList = None
        self.UriList = None
        self.AttackipList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReqQps = params.get("ReqQps")
        self.DropQps = params.get("DropQps")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.DomainList = params.get("DomainList")
        self.UriList = params.get("UriList")
        self.AttackipList = params.get("AttackipList")


class CCFrequencyRule(AbstractModel):
    """Access frequency control rule for CC protection

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: ID of the access frequency control rule for CC protection
        :type CCFrequencyRuleId: str
        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        """
        self.CCFrequencyRuleId = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")


class CCPolicy(AbstractModel):
    """Custom CC protection rule

    """

    def __init__(self):
        """
        :param Name: Policy name
        :type Name: str
        :param Smode: Matching mode. Valid values: [matching (matching mode), speedlimit (speed limiting mode)]
        :type Smode: str
        :param SetId: Policy ID
        :type SetId: str
        :param Frequency: Number of requests allowed per minute
        :type Frequency: int
        :param ExeMode: Executed policy mode. Valid values: [alg (verification code), drop (blocking)]
        :type ExeMode: str
        :param Switch: Specifies whether the policy is activated
        :type Switch: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param RuleList: Rule list
        :type RuleList: list of CCRule
        :param IpList: IP list. If this field is to be left empty, please pass in an empty instead of null;
        :type IpList: list of str
        :param Protocol: CC protection type. Valid values: [http, https]
        :type Protocol: str
        :param RuleId: ID of the forwarding rule corresponding to the HTTPS CC protection domain name
        :type RuleId: str
        :param Domain: HTTPS CC protection domain name
        :type Domain: str
        """
        self.Name = None
        self.Smode = None
        self.SetId = None
        self.Frequency = None
        self.ExeMode = None
        self.Switch = None
        self.CreateTime = None
        self.RuleList = None
        self.IpList = None
        self.Protocol = None
        self.RuleId = None
        self.Domain = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Smode = params.get("Smode")
        self.SetId = params.get("SetId")
        self.Frequency = params.get("Frequency")
        self.ExeMode = params.get("ExeMode")
        self.Switch = params.get("Switch")
        self.CreateTime = params.get("CreateTime")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = CCRule()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.Domain = params.get("Domain")


class CCRule(AbstractModel):
    """The custom CC protection policy in key-value format

    """

    def __init__(self):
        """
        :param Skey: Key of the policy. Valid values: `host`, `cgi`, `ua`, `referer`
        :type Skey: str
        :param Operator: Rule condition. Valid values: `include`, `not_include`, `equal`
        :type Operator: str
        :param Value: Value of the policy. Length limit: 31 bytes
        :type Value: str
        """
        self.Skey = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")


class CCRuleConfig(AbstractModel):
    """Custom layer-7 CC policy

    """

    def __init__(self):
        """
        :param Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param Action: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Action: str
        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        """
        self.Period = None
        self.ReqNumber = None
        self.Action = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Action = params.get("Action")
        self.ExeDuration = params.get("ExeDuration")


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`basic`: Anti-DDoS Basic)
        :type Business: str
        :param Method: `get`: read alarm threshold, `set`: set alarm threshold
        :type Method: str
        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is required if `Method` is `set`;
        :type AlarmType: int
        :param AlarmThreshold: Alarm threshold. It is required if `Method` is `set`. If it is set to 0, it means to clear the alarm threshold configuration;
        :type AlarmThreshold: int
        """
        self.Business = None
        self.Method = None
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param AlarmThreshold: If there is an alarm threshold configuration, the returned alarm threshold will be greater than 0; otherwise, the returned alarm threshold will be 0;
        :type AlarmThreshold: int
        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is valid if `AlarmThreshold` is above 0;
        :type AlarmType: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AlarmThreshold = None
        self.AlarmType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.AlarmType = params.get("AlarmType")
        self.RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param BoundDevList: Array of IPs to be bound to the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP. If there are no IPs to bind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;
        :type BoundDevList: list of BoundIpInfo
        :param UnBoundDevList: Array of IPs to be unbound from Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP; if there are no IPs to unbind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;
        :type UnBoundDevList: list of BoundIpInfo
        :param CopyPolicy: [Disused]
        :type CopyPolicy: str
        """
        self.Business = None
        self.Id = None
        self.BoundDevList = None
        self.UnBoundDevList = None
        self.CopyPolicy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self.BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self.UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.UnBoundDevList.append(obj)
        self.CopyPolicy = params.get("CopyPolicy")


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateCCFrequencyRulesRequest(AbstractModel):
    """CreateCCFrequencyRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API
        :type RuleId: str
        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: Access frequency control rule ID for CC protection
        :type CCFrequencyRuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CCFrequencyRuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.RequestId = params.get("RequestId")


class CreateCCSelfDefinePolicyRequest(AbstractModel):
    """CreateCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Policy: Details of the CC protection policy
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self.Business = None
        self.Id = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyCaseRequest(AbstractModel):
    """CreateDDoSPolicyCase request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param CaseName: Policy scenario name string. Length limit: 64
        :type CaseName: str
        :param PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]
        :type PlatformTypes: list of str
        :param AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]
        :type AppType: str
        :param AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]
        :type AppProtocols: list of str
        :param TcpSportStart: TCP start port. Value range: (0, 65535]
        :type TcpSportStart: str
        :param TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port.
        :type TcpSportEnd: str
        :param UdpSportStart: UDP start port. Value range: (0, 65535]
        :type UdpSportStart: str
        :param UdpSportEnd: UDP end port. Value range: (0, 65535). It must be greater than or equal to the UDP start port.
        :type UdpSportEnd: str
        :param HasAbroad: Whether there are customers outside China. Valid values: [no, yes]
        :type HasAbroad: str
        :param HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]
        :type HasInitiateTcp: str
        :param HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]
        :type HasInitiateUdp: str
        :param PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]
        :type PeerTcpPort: str
        :param PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]
        :type PeerUdpPort: str
        :param TcpFootprint: Fixed feature code of TCP payload. Max string length: 512
        :type TcpFootprint: str
        :param UdpFootprint: Fixed feature code of UDP payload. Max string length: 512
        :type UdpFootprint: str
        :param WebApiUrl: Web application API URL
        :type WebApiUrl: list of str
        :param MinTcpPackageLen: Minimum length of TCP packet. Value range: (0, 1500)
        :type MinTcpPackageLen: str
        :param MaxTcpPackageLen: Maximum length of TCP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP packet
        :type MaxTcpPackageLen: str
        :param MinUdpPackageLen: Minimum length of UDP packet. Value range: (0, 1500)
        :type MinUdpPackageLen: str
        :param MaxUdpPackageLen: Maximum length of UDP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP packet
        :type MaxUdpPackageLen: str
        :param HasVPN: Whether there are applications using VPN. Valid values: [no, yes]
        :type HasVPN: str
        :param TcpPortList: TCP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.
        :type TcpPortList: str
        :param UdpPortList: UDP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.
        :type UdpPortList: str
        """
        self.Business = None
        self.CaseName = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CaseName = params.get("CaseName")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param SceneId: Policy scenario ID
        :type SceneId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SceneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyRequest(AbstractModel):
    """CreateDDoSPolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param DropOptions: Protocol disablement, which must be entered, and the array length must be 1
        :type DropOptions: list of DDoSPolicyDropOption
        :param Name: Policy name
        :type Name: str
        :param PortLimits: Ports to be closed. If no ports are to be closed, enter an empty array
        :type PortLimits: list of DDoSPolicyPortLimit
        :param IpAllowDenys: IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist
        :type IpAllowDenys: list of IpBlackWhite
        :param PacketFilters: Packet filter. Enter an empty array if there are no packets to filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param WaterPrint: Watermarking policy parameters. Enter an empty array if the watermarking feature is not enabled. Only one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)
        :type WaterPrint: list of WaterPrintPolicy
        """
        self.Business = None
        self.DropOptions = None
        self.Name = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        self.Name = params.get("Name")
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateInstanceNameRequest(AbstractModel):
    """CreateInstanceName request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Name: Instance name. Length limit: 32 characters
        :type Name: str
        """
        self.Business = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Name = params.get("Name")


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4HealthConfigRequest(AbstractModel):
    """CreateL4HealthConfig request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param HealthConfig: Layer-4 health check configuration array
        :type HealthConfig: list of L4HealthConfig
        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4RulesRequest(AbstractModel):
    """CreateL4Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Rules: Rule list
        :type Rules: list of L4RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7CCRuleRequest(AbstractModel):
    """CreateL7CCRule request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Method: Operation. Valid values: [query (query), add (add), del (delete)]
        :type Method: str
        :param RuleId: Layer-7 forwarding rule ID, such as rule-0000001
        :type RuleId: str
        :param RuleConfig: Custom layer-7 CC protection rule. If the `Method` is `query`, this field can be left empty; if the `Method` is `add` or `del`, it is required, and the array length can only be 1;
        :type RuleConfig: list of CCRuleConfig
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.RuleId = None
        self.RuleConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.RuleId = params.get("RuleId")
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule response structure.

    """

    def __init__(self):
        """
        :param RuleConfig: Custom layer-7 CC protection rule parameters. If custom CC protection rule is not enabled, an empty array will be returned.
        :type RuleConfig: list of CCRuleConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)
        self.RequestId = params.get("RequestId")


class CreateL7HealthConfigRequest(AbstractModel):
    """CreateL7HealthConfig request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param HealthConfig: Layer-7 health check configuration array
        :type HealthConfig: list of L7HealthConfig
        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RuleCertRequest(AbstractModel):
    """CreateL7RuleCert request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: The resource instance ID, such as the ID of an Anti-DDoS Advanced instance or the ID of an Anti-DDoS Ultimate instance.
        :type Id: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param CertType: Certificate type, which is required if the protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]
        :type CertType: int
        :param SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID.
        :type SSLId: str
        :param Cert: [Disused] If the certificate is an external certificate, this field must be entered with the certificate content. 
        :type Cert: str
        :param PrivateKey: [Disused] If the certificate is an external certificate, this field must be entered with the certificate key. 
        :type PrivateKey: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Rules: Rule list
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesUploadRequest(AbstractModel):
    """CreateL7RulesUpload request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Rules: Rule list
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNetReturnRequest(AbstractModel):
    """CreateNetReturn request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesUploadRequest(AbstractModel):
    """CreateNewL7RulesUpload request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param IdList: Resource ID list.
        :type IdList: list of str
        :param VipList: Resource IP address list.
        :type VipList: list of str
        :param Rules: Rule list.
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateNewL7RulesUploadResponse(AbstractModel):
    """CreateNewL7RulesUpload response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateUnblockIpRequest(AbstractModel):
    """CreateUnblockIp request structure.

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self.Ip = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp response structure.

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        :param UnblockTime: Unblocked time (estimated)
        :type UnblockTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ip = None
        self.ActionType = None
        self.UnblockTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")
        self.UnblockTime = params.get("UnblockTime")
        self.RequestId = params.get("RequestId")


class DDoSAlarmThreshold(AbstractModel):
    """DDoS alarm threshold

    """

    def __init__(self):
        """
        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic
        :type AlarmType: int
        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)
        :type AlarmThreshold: int
        """
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")


class DDoSAttackSourceRecord(AbstractModel):
    """Attack source information

    """

    def __init__(self):
        """
        :param SrcIp: Attack source IP
        :type SrcIp: str
        :param Province: Province (valid for Mainland China)
        :type Province: str
        :param Nation: Country/region
        :type Nation: str
        :param PacketSum: Total number of attack packets
        :type PacketSum: int
        :param PacketLen: Total attack traffic
        :type PacketLen: int
        """
        self.SrcIp = None
        self.Province = None
        self.Nation = None
        self.PacketSum = None
        self.PacketLen = None


    def _deserialize(self, params):
        self.SrcIp = params.get("SrcIp")
        self.Province = params.get("Province")
        self.Nation = params.get("Nation")
        self.PacketSum = params.get("PacketSum")
        self.PacketLen = params.get("PacketLen")


class DDoSEventRecord(AbstractModel):
    """DDoS attack event record

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Vip: Resource IP
        :type Vip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param Mbps: Maximum attack bandwidth
        :type Mbps: int
        :param Pps: Maximum attack packet rate
        :type Pps: int
        :param AttackType: Attack type
        :type AttackType: str
        :param BlockFlag: Whether the IP is blocked. Valid values: [1 (yes), 0 (no), 2 (invalid value)]
        :type BlockFlag: int
        :param OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes (yes), no (no), empty string (unknown value)]
        :type OverLoad: str
        :param AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]
        :type AttackStatus: int
        :param ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param EventId: Attack event ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventId: str
        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.Mbps = None
        self.Pps = None
        self.AttackType = None
        self.BlockFlag = None
        self.OverLoad = None
        self.AttackStatus = None
        self.ResourceName = None
        self.EventId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.AttackType = params.get("AttackType")
        self.BlockFlag = params.get("BlockFlag")
        self.OverLoad = params.get("OverLoad")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.EventId = params.get("EventId")


class DDoSPolicyDropOption(AbstractModel):
    """Disabled protocol in advanced DDoS policy

    """

    def __init__(self):
        """
        :param DropTcp: Blocks all TCP traffic. Valid values: [0,1]
        :type DropTcp: int
        :param DropUdp: Blocks all UDP traffic. Valid values: [0,1]
        :type DropUdp: int
        :param DropIcmp: Blocks all ICMP traffic. Valid values: [0,1]
        :type DropIcmp: int
        :param DropOther: Blocks traffic of other protocols. Valid values: [0,1]
        :type DropOther: int
        :param DropAbroad: Rejects traffic from outside Mainland China. Valid values: [0,1]
        :type DropAbroad: int
        :param CheckSyncConn: Null session protection. Valid values: [0,1]
        :type CheckSyncConn: int
        :param SdNewLimit: New connection suppression based on source IP and destination IP. Value range: [0,4294967295]
        :type SdNewLimit: int
        :param DstNewLimit: New connection suppression based on destination IP. Value range: [0,4294967295]
        :type DstNewLimit: int
        :param SdConnLimit: Concurrent connection suppression based on source IP and destination IP. Value range: [0,4294967295]
        :type SdConnLimit: int
        :param DstConnLimit: Concurrent connection suppression based on destination IP. Value range: [0,4294967295]
        :type DstConnLimit: int
        :param BadConnThreshold: Threshold for triggering connection suppression. Value range: [0,4294967295]
        :type BadConnThreshold: int
        :param NullConnEnable: Exceptional connection detection condition: null session protection status. Valid values: [0,1]
        :type NullConnEnable: int
        :param ConnTimeout: Exceptional connection detection condition: connection timeout. Valid values: [0,65535]
        :type ConnTimeout: int
        :param SynRate: Exceptional connection detection condition: percentage of SYN out of ACK. Valid values: [0,100]
        :type SynRate: int
        :param SynLimit: Exceptional connection detection condition: SYN threshold. Valid values: [0,100]
        :type SynLimit: int
        :param DTcpMbpsLimit: TCP speed limit. Value range: [0,4294967295]
        :type DTcpMbpsLimit: int
        :param DUdpMbpsLimit: UDP speed limit. Value range: [0,4294967295]
        :type DUdpMbpsLimit: int
        :param DIcmpMbpsLimit: ICMP speed limit. Value range: [0,4294967295]
        :type DIcmpMbpsLimit: int
        :param DOtherMbpsLimit: Other protocol speed limit. Value range: [0,4294967295]
        :type DOtherMbpsLimit: int
        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.DropAbroad = None
        self.CheckSyncConn = None
        self.SdNewLimit = None
        self.DstNewLimit = None
        self.SdConnLimit = None
        self.DstConnLimit = None
        self.BadConnThreshold = None
        self.NullConnEnable = None
        self.ConnTimeout = None
        self.SynRate = None
        self.SynLimit = None
        self.DTcpMbpsLimit = None
        self.DUdpMbpsLimit = None
        self.DIcmpMbpsLimit = None
        self.DOtherMbpsLimit = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.DropAbroad = params.get("DropAbroad")
        self.CheckSyncConn = params.get("CheckSyncConn")
        self.SdNewLimit = params.get("SdNewLimit")
        self.DstNewLimit = params.get("DstNewLimit")
        self.SdConnLimit = params.get("SdConnLimit")
        self.DstConnLimit = params.get("DstConnLimit")
        self.BadConnThreshold = params.get("BadConnThreshold")
        self.NullConnEnable = params.get("NullConnEnable")
        self.ConnTimeout = params.get("ConnTimeout")
        self.SynRate = params.get("SynRate")
        self.SynLimit = params.get("SynLimit")
        self.DTcpMbpsLimit = params.get("DTcpMbpsLimit")
        self.DUdpMbpsLimit = params.get("DUdpMbpsLimit")
        self.DIcmpMbpsLimit = params.get("DIcmpMbpsLimit")
        self.DOtherMbpsLimit = params.get("DOtherMbpsLimit")


class DDoSPolicyPacketFilter(AbstractModel):
    """Packet filter in advanced DDoS policy

    """

    def __init__(self):
        """
        :param Protocol: Protocol. Valid values: [tcp, udp, icmp, all]
        :type Protocol: str
        :param SportStart: Start source port. Value range: [0,65535]
        :type SportStart: int
        :param SportEnd: End source port. Value range: [0,65535]
        :type SportEnd: int
        :param DportStart: Start destination port. Value range: [0,65535]
        :type DportStart: int
        :param DportEnd: End destination port. Value range: [0,65535]
        :type DportEnd: int
        :param PktlenMin: Minimum packet length. Value range: [0,1500]
        :type PktlenMin: int
        :param PktlenMax: Maximum packet length. Value range: [0,1500]
        :type PktlenMax: int
        :param MatchBegin: Whether to detect the payload. Valid values: [
begin_l3 (IP header)
begin_l4 (TCP header)
begin_l5 (payload)
no_match (no check)
]
        :type MatchBegin: str
        :param MatchType: Whether it is a regular expression. Valid values: [sunday (keyword), pcre (regular expression)]
        :type MatchType: str
        :param Str: Keyword or regular expression
        :type Str: str
        :param Depth: Detection depth. Value range: [0,1500]
        :type Depth: int
        :param Offset: Detection offset. Value range: [0,1500]
        :type Offset: int
        :param IsNot: Whether to include. Valid values: [0 (no), 1 (yes)]
        :type IsNot: int
        :param Action: Policy action. Valid values: [drop, drop_black, drop_rst, drop_black_rst, transmit]
        :type Action: str
        """
        self.Protocol = None
        self.SportStart = None
        self.SportEnd = None
        self.DportStart = None
        self.DportEnd = None
        self.PktlenMin = None
        self.PktlenMax = None
        self.MatchBegin = None
        self.MatchType = None
        self.Str = None
        self.Depth = None
        self.Offset = None
        self.IsNot = None
        self.Action = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PktlenMin = params.get("PktlenMin")
        self.PktlenMax = params.get("PktlenMax")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchType = params.get("MatchType")
        self.Str = params.get("Str")
        self.Depth = params.get("Depth")
        self.Offset = params.get("Offset")
        self.IsNot = params.get("IsNot")
        self.Action = params.get("Action")


class DDoSPolicyPortLimit(AbstractModel):
    """Disabled port in advanced DDoS policy

    """

    def __init__(self):
        """
        :param Protocol: Protocol. Valid values: [tcp, udp, all]
        :type Protocol: str
        :param DPortStart: Start destination port. Value range: [0,65535]
        :type DPortStart: int
        :param DPortEnd: End destination port, which must be greater than or equal to the start destination port. Value range: [0,65535]
        :type DPortEnd: int
        :param SPortStart: Start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.
        :type SPortStart: int
        :param SPortEnd: End source port, which must be greater than or equal to the start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.
        :type SPortEnd: int
        :param Action: Action to be executed. Valid values: [drop (discard) , transmit (forward)]
Note: this field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param Kind: Type of port to be disabled. Valid values: [0 (destination port range), 1 (source port range), 2 (destination port range and source port range)]
Note: this field may return null, indicating that no valid values can be obtained.
        :type Kind: int
        """
        self.Protocol = None
        self.DPortStart = None
        self.DPortEnd = None
        self.SPortStart = None
        self.SPortEnd = None
        self.Action = None
        self.Kind = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.DPortStart = params.get("DPortStart")
        self.DPortEnd = params.get("DPortEnd")
        self.SPortStart = params.get("SPortStart")
        self.SPortEnd = params.get("SPortEnd")
        self.Action = params.get("Action")
        self.Kind = params.get("Kind")


class DDosPolicy(AbstractModel):
    """Advanced DDoS policy

    """

    def __init__(self):
        """
        :param Resources: Resource bound to policy
        :type Resources: list of ResourceIp
        :param DropOptions: Disabled protocol
        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`
        :param PortLimits: Disabled port
        :type PortLimits: list of DDoSPolicyPortLimit
        :param PacketFilters: Packet filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param IpBlackWhiteLists: IP blocklist/allowlist
        :type IpBlackWhiteLists: list of IpBlackWhite
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param PolicyName: Policy name
        :type PolicyName: str
        :param CreateTime: Policy creation time
        :type CreateTime: str
        :param WaterPrint: Watermarking policy parameter. There can be only one policy. If there are no policies, the array is empty
        :type WaterPrint: list of WaterPrintPolicy
        :param WaterKey: Watermark key. There can be up to two keys. If there are no policies, the array is empty
        :type WaterKey: list of WaterPrintKey
        :param BoundResources: Resource instance bound to policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type BoundResources: list of str
        :param SceneId: Policy scenario
Note: this field may return null, indicating that no valid values can be obtained.
        :type SceneId: str
        """
        self.Resources = None
        self.DropOptions = None
        self.PortLimits = None
        self.PacketFilters = None
        self.IpBlackWhiteLists = None
        self.PolicyId = None
        self.PolicyName = None
        self.CreateTime = None
        self.WaterPrint = None
        self.WaterKey = None
        self.BoundResources = None
        self.SceneId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("DropOptions") is not None:
            self.DropOptions = DDoSPolicyDropOption()
            self.DropOptions._deserialize(params.get("DropOptions"))
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("IpBlackWhiteLists") is not None:
            self.IpBlackWhiteLists = []
            for item in params.get("IpBlackWhiteLists"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpBlackWhiteLists.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.CreateTime = params.get("CreateTime")
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)
        if params.get("WaterKey") is not None:
            self.WaterKey = []
            for item in params.get("WaterKey"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.WaterKey.append(obj)
        self.BoundResources = params.get("BoundResources")
        self.SceneId = params.get("SceneId")


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param CCFrequencyRuleId: Access frequency control rule ID for CC protection
        :type CCFrequencyRuleId: str
        """
        self.Business = None
        self.CCFrequencyRuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteCCSelfDefinePolicyRequest(AbstractModel):
    """DeleteCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param SetId: Policy ID
        :type SetId: str
        """
        self.Business = None
        self.Id = None
        self.SetId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyCaseRequest(AbstractModel):
    """DeleteDDoSPolicyCase request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param SceneId: Policy scenario ID
        :type SceneId: str
        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyRequest(AbstractModel):
    """DeleteDDoSPolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param PolicyId: Policy ID
        :type PolicyId: str
        """
        self.Business = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL4RulesRequest(AbstractModel):
    """DeleteL4Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID list
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID list
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DescribeActionLogRequest(AbstractModel):
    """DescribeActionLog request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Filter: Search value, which can only be resource ID or user `UIN`
        :type Filter: str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Business = None
        self.Filter = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Business = params.get("Business")
        self.Filter = params.get("Filter")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param Data: Record array
        :type Data: list of KeyValueRecord
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
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBGPIPL7RuleMaxCntRequest(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt response structure.

    """

    def __init__(self):
        """
        :param Count: Maximum number of layer-7 rules that can be added for Anti-DDoS Advanced
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeBaradDataRequest(AbstractModel):
    """DescribeBaradData request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param MetricName: Metric name. Valid values:
connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;
        :type MetricName: str
        :param Period: Statistical time granularity in seconds (300: 5-minute, 3600: hourly, 86400: daily)
        :type Period: int
        :param StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5
        :type StartTime: str
        :param EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5
        :type EndTime: str
        :param Statistics: Statistical method. Valid values:
max: maximum value;
min: minimum value;
avg: average;
        :type Statistics: str
        :param ProtocolPort: Protocol port array
        :type ProtocolPort: list of ProtocolPort
        :param Ip: Resource instance IP, which is required only if `Business` is `net` (Anti-DDoS Ultimate), because an Anti-DDoS Ultimate instance has multiple IPs;
        :type Ip: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.ProtocolPort = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        if params.get("ProtocolPort") is not None:
            self.ProtocolPort = []
            for item in params.get("ProtocolPort"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPort.append(obj)
        self.Ip = params.get("Ip")


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData response structure.

    """

    def __init__(self):
        """
        :param DataList: Returned metric value
        :type DataList: list of BaradData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = BaradData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBasicCCThresholdRequest(AbstractModel):
    """DescribeBasicCCThreshold request structure.

    """

    def __init__(self):
        """
        :param BasicIp: Queried IP address, such as 1.1.1.1
        :type BasicIp: str
        :param BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold response structure.

    """

    def __init__(self):
        """
        :param CCEnable: CC status (0: disabled, 1: enabled)
        :type CCEnable: int
        :param CCThreshold: CC protection threshold
        :type CCThreshold: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CCEnable = None
        self.CCThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.RequestId = params.get("RequestId")


class DescribeBasicDeviceThresholdRequest(AbstractModel):
    """DescribeBasicDeviceThreshold request structure.

    """

    def __init__(self):
        """
        :param BasicIp: Queried IP address, such as 1.1.1.1
        :type BasicIp: str
        :param BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param BasicCheckFlag: Validity check. Valid value: 1
        :type BasicCheckFlag: int
        :param BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicCheckFlag = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicCheckFlag = params.get("BasicCheckFlag")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold response structure.

    """

    def __init__(self):
        """
        :param Threshold: Blackhole blocking value
        :type Threshold: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RsId: Anti-DDoS instance ID
        :type RsId: str
        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param CCAlarmThreshold: CC alarm threshold
        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CCAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCAlarmThreshold") is not None:
            self.CCAlarmThreshold = CCAlarmThreshold()
            self.CCAlarmThreshold._deserialize(params.get("CCAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeCCEvListRequest(AbstractModel):
    """DescribeCCEvList request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param IpList: Resource instance IP. When `business` is not `basic`, if `IpList` is not empty, `Id` must not be empty;
        :type IpList: list of str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `shield`: Chess Shield; `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param IpList: Instance IP list
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpList: list of str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Data: CC attack event list
        :type Data: list of CCEventRecord
        :param Total: Total number of records
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CCEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCCFrequencyRulesRequest(AbstractModel):
    """DescribeCCFrequencyRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API). If a value is entered, it means to get the access frequency control rule of the forwarding rule;
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param CCFrequencyRuleList: Access frequency control rule list
        :type CCFrequencyRuleList: list of CCFrequencyRule
        :param CCFrequencyRuleStatus: Access frequency control rule status. Valid values: [on, off];
        :type CCFrequencyRuleStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CCFrequencyRuleList = None
        self.CCFrequencyRuleStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCFrequencyRuleList") is not None:
            self.CCFrequencyRuleList = []
            for item in params.get("CCFrequencyRuleList"):
                obj = CCFrequencyRule()
                obj._deserialize(item)
                self.CCFrequencyRuleList.append(obj)
        self.CCFrequencyRuleStatus = params.get("CCFrequencyRuleStatus")
        self.RequestId = params.get("RequestId")


class DescribeCCIpAllowDenyRequest(AbstractModel):
    """DescribeCCIpAllowDeny request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Type: Blocklist or allowlist. Valid values: [white (allowlist), black (blocklist)]
Note: this array can only have one value. It cannot get the blocklist and allowlist at the same time
        :type Type: list of str
        :param Limit: Pagination parameter
        :type Limit: int
        :param Offset: Pagination parameter
        :type Offset: int
        :param Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];
        :type Protocol: str
        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny response structure.

    """

    def __init__(self):
        """
        :param Data: This field has been replaced by `RecordList` and should not be used
        :type Data: list of KeyValue
        :param Total: Number of records
        :type Total: int
        :param RecordList: Returned Blocklist/allowlist record,
If "Key":"ip", "Value": IP;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection protocol (HTTP or HTTPS);
        :type RecordList: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCSelfDefinePolicyRequest(AbstractModel):
    """DescribeCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro, `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Limit: Number of entries pulled
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of custom rules
        :type Total: int
        :param Policys: Policy list
        :type Policys: list of CCPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Policys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Policys") is not None:
            self.Policys = []
            for item in params.get("Policys"):
                obj = CCPolicy()
                obj._deserialize(item)
                self.Policys.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Ip: Resource IP
        :type Ip: str
        :param MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        :param Domain: (Optional) Domain name
        :type Domain: str
        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param Data: Value array
        :type Data: list of int non-negative
        :param Count: Number of values
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeCCUrlAllowRequest(AbstractModel):
    """DescribeCCUrlAllow request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Type: Blocklist or allowlist. Valid value: [white (allowlist)]. Currently, only allowlist is supported.
Note: this array can only have one value which can only be `white`
        :type Type: list of str
        :param Limit: Pagination parameter
        :type Limit: int
        :param Offset: Pagination parameter
        :type Offset: int
        :param Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];
        :type Protocol: str
        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow response structure.

    """

    def __init__(self):
        """
        :param Data: This field has been replaced by `RecordList` and should not be used
        :type Data: list of KeyValue
        :param Total: Total number of records
        :type Total: int
        :param RecordList: Returned Blocklist/allowlist record,
If "Key":"url", "Value": URL;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection type (HTTP protection or HTTPS domain name protection);
        :type RecordList: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAlarmThresholdRequest(AbstractModel):
    """DescribeDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RsId: Anti-DDoS instance ID
        :type RsId: str
        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param DDoSAlarmThreshold: DDoS alarm threshold
        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DDoSAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDoSAlarmThreshold") is not None:
            self.DDoSAlarmThreshold = DDoSAlarmThreshold()
            self.DDoSAlarmThreshold._deserialize(params.get("DDoSAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackIPRegionMapRequest(AbstractModel):
    """DescribeDDoSAttackIPRegionMap request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time. Maximum statistics time range: half a year;
        :type EndTime: str
        :param IpList: IP attack source of specified resource, which is optional
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap response structure.

    """

    def __init__(self):
        """
        :param NationCount: Global region distribution data
        :type NationCount: list of KeyValueRecord
        :param ProvinceCount: Chinese province distribution data
        :type ProvinceCount: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NationCount = None
        self.ProvinceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NationCount") is not None:
            self.NationCount = []
            for item in params.get("NationCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.NationCount.append(obj)
        if params.get("ProvinceCount") is not None:
            self.ProvinceCount = []
            for item in params.get("ProvinceCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ProvinceCount.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceRequest(AbstractModel):
    """DescribeDDoSAttackSource request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param IpList: IP attack source of specified resource, which is optional
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.IpList = params.get("IpList")


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of attack sources
        :type Total: int
        :param AttackSourceList: Attack source list
        :type AttackSourceList: list of DDoSAttackSourceRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.AttackSourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AttackSourceList") is not None:
            self.AttackSourceList = []
            for item in params.get("AttackSourceList"):
                obj = DDoSAttackSourceRecord()
                obj._deserialize(item)
                self.AttackSourceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSCountRequest(AbstractModel):
    """DescribeDDoSCount request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        :param Data: `Key-Value` array. Valid values of `Key`:
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSDefendStatusRequest(AbstractModel):
    """DescribeDDoSDefendStatus request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Instance ID, which is required only if `Business` is not `basic`.
        :type Id: str
        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param BizType: Type of products bound to the anti-DDoS instance, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (Bare metal products), eni (elastic network interface), vpngw (VPN Gateway), natgw (NAT Gateway), waf (Web Application Firewall), fpc (Finance products), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
        self.Business = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus response structure.

    """

    def __init__(self):
        """
        :param DefendStatus: Protection status. 0: disabled, 1: enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type DefendStatus: int
        :param UndefendExpire: Expiration time of temporary protection disablement. This field is empty if the protection is in enabled status;
Note: this field may return null, indicating that no valid values can be obtained.
        :type UndefendExpire: str
        :param ShowFlag: Console feature display field. 1: displays console features, 0: hides console features
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShowFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DefendStatus = None
        self.UndefendExpire = None
        self.ShowFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DefendStatus = params.get("DefendStatus")
        self.UndefendExpire = params.get("UndefendExpire")
        self.ShowFlag = params.get("ShowFlag")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvInfoRequest(AbstractModel):
    """DescribeDDoSEvInfo request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param TcpPacketSum: Number of TCP attack packets
        :type TcpPacketSum: int
        :param TcpKBSum: Traffic of TCP attacks in KB
        :type TcpKBSum: int
        :param UdpPacketSum: Number of UDP attack packets
        :type UdpPacketSum: int
        :param UdpKBSum: Traffic of UDP attacks in KB
        :type UdpKBSum: int
        :param IcmpPacketSum: Number of ICMP attack packets
        :type IcmpPacketSum: int
        :param IcmpKBSum: Traffic of ICMP attacks in KB
        :type IcmpKBSum: int
        :param OtherPacketSum: Number of other attack packets
        :type OtherPacketSum: int
        :param OtherKBSum: Traffic of other attacks in KB
        :type OtherKBSum: int
        :param TotalTraffic: Total attack traffic in KB
        :type TotalTraffic: int
        :param Mbps: Attack traffic bandwidth peak
        :type Mbps: int
        :param Pps: Attack packet rate peak
        :type Pps: int
        :param PcapUrl: PCAP file download link
        :type PcapUrl: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvListRequest(AbstractModel):
    """DescribeDDoSEvList request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        :param IpList: Resource IP
        :type IpList: list of str
        :param OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes, no]. If an empty string is entered, it means no filtering
        :type OverLoad: str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.OverLoad = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.OverLoad = params.get("OverLoad")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param IpList: Resource IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpList: list of str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Data: DDoS attack event list
        :type Data: list of DDoSEventRecord
        :param Total: Total number of records
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSIpLogRequest(AbstractModel):
    """DescribeDDoSIpLog request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content
        :type Data: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetCountRequest(AbstractModel):
    """DescribeDDoSNetCount request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]
        :type MetricName: str
        :param Data: `Key-Value` array. Valid values of `Key`:
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvInfoRequest(AbstractModel):
    """DescribeDDoSNetEvInfo request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param TcpPacketSum: Number of TCP attack packets
        :type TcpPacketSum: int
        :param TcpKBSum: Traffic of TCP attacks in KB
        :type TcpKBSum: int
        :param UdpPacketSum: Number of UDP attack packets
        :type UdpPacketSum: int
        :param UdpKBSum: Traffic of UDP attacks in KB
        :type UdpKBSum: int
        :param IcmpPacketSum: Number of ICMP attack packets
        :type IcmpPacketSum: int
        :param IcmpKBSum: Traffic of ICMP attacks in KB
        :type IcmpKBSum: int
        :param OtherPacketSum: Number of other attack packets
        :type OtherPacketSum: int
        :param OtherKBSum: Traffic of other attacks in KB
        :type OtherKBSum: int
        :param TotalTraffic: Total attack traffic in KB
        :type TotalTraffic: int
        :param Mbps: Attack traffic bandwidth peak
        :type Mbps: int
        :param Pps: Attack packet rate peak
        :type Pps: int
        :param PcapUrl: PCAP file download link
        :type PcapUrl: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvListRequest(AbstractModel):
    """DescribeDDoSNetEvList request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Data: DDoS attack event list
        :type Data: list of DDoSEventRecord
        :param Total: Total number of records
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetIpLogRequest(AbstractModel):
    """DescribeDDoSNetIpLog request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Attack start time
        :type StartTime: str
        :param EndTime: Attack end time
        :type EndTime: str
        :param Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content
        :type Data: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetTrendRequest(AbstractModel):
    """DescribeDDoSNetTrend request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param Data: Value array
        :type Data: list of int non-negative
        :param Count: Number of values
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Resource ID, which is optional. If a value is entered, it indicates the advanced DDoS policy bound to the resource
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param DDosPolicyList: Advanced DDoS policy list
        :type DDosPolicyList: list of DDosPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DDosPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDosPolicyList") is not None:
            self.DDosPolicyList = []
            for item in params.get("DDosPolicyList"):
                obj = DDosPolicy()
                obj._deserialize(item)
                self.DDosPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Ip: Anti-DDoS instance IP
        :type Ip: str
        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)
        :type Id: str
        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param Ip: Resource IP
        :type Ip: str
        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]
        :type MetricName: str
        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]
        :type Period: int
        :param StartTime: Statistics start time
        :type StartTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param Data: Value array. The unit for attack traffic bandwidth is Mbps, and that for the packet rate is pps.
        :type Data: list of int non-negative
        :param Count: Number of values
        :type Count: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSUsedStatisRequest(AbstractModel):
    """DescribeDDoSUsedStatis request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis response structure.

    """

    def __init__(self):
        """
        :param Data: Field value as follows:
Days: number of days of Anti-DDoS resource use
Attacks: number of DDoS attacks
        :type Data: list of KeyValue
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIPProductInfoRequest(AbstractModel):
    """DescribeIPProductInfo request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)
        :type Business: str
        :param IpList: IP list
        :type IpList: list of str
        """
        self.Business = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IpList = params.get("IpList")


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo response structure.

    """

    def __init__(self):
        """
        :param Data: Tencent Cloud product information list. If nothing is found, an empty array will be returned. Valid values:
If `Key` is ProductName, `value` indicates the name of a Tencent Cloud product instance;
If `Key` is `ProductInstanceId`, `value` indicates the ID of a Tencent Cloud product instance;
If `Key` is `ProductType`, `value` indicates the Tencent Cloud product type (cvm: CVM, clb: CLB);
If `Key` is `IP`, `value` indicates the IP of a Tencent Cloud product instance;
        :type Data: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInsurePacksRequest(AbstractModel):
    """DescribeInsurePacks request structure.

    """

    def __init__(self):
        """
        :param IdList: Guarantee package ID, which is optional. If you need to get the guarantee package with a specified ID (such as insure-000000xe), please use this field
        :type IdList: list of str
        """
        self.IdList = None


    def _deserialize(self, params):
        self.IdList = params.get("IdList")


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks response structure.

    """

    def __init__(self):
        """
        :param InsurePacks: Guarantee package list
        :type InsurePacks: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InsurePacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InsurePacks") is not None:
            self.InsurePacks = []
            for item in params.get("InsurePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.InsurePacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList request structure.

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList response structure.

    """

    def __init__(self):
        """
        :param List: Blocked IP list
        :type List: list of IpBlockData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpUnBlockListRequest(AbstractModel):
    """DescribeIpUnBlockList request structure.

    """

    def __init__(self):
        """
        :param BeginTime: Start time
        :type BeginTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Ip: IP (if this field is not empty, IP filtering will be performed)
        :type Ip: str
        :param Paging: Pagination parameter (paginated query will be performed if this field is not empty). This field will be disused in the future. Please use the `Limit` and `Offset` fields instead;
        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.BeginTime = None
        self.EndTime = None
        self.Ip = None
        self.Paging = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        if params.get("Paging") is not None:
            self.Paging = Paging()
            self.Paging._deserialize(params.get("Paging"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList response structure.

    """

    def __init__(self):
        """
        :param BeginTime: Start time
        :type BeginTime: str
        :param EndTime: End time
        :type EndTime: str
        :param List: IP unblocking record
        :type List: list of IpUnBlockData
        :param Total: Total number of records
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpUnBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeL4HealthConfigRequest(AbstractModel):
    """DescribeL4HealthConfig request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig response structure.

    """

    def __init__(self):
        """
        :param HealthConfig: Layer-4 health check configuration array
        :type HealthConfig: list of L4HealthConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4RulesErrHealthRequest(AbstractModel):
    """DescribeL4RulesErrHealth request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of exceptional rules
        :type Total: int
        :param ErrHealths: Exceptional rule list. Returned value description: `Key` is the rule ID, while `Value` is the exceptional IP. Multiple IPs are separated by ","
        :type ErrHealths: list of KeyValue
        :param ExtErrHealths: Exceptional rule list (which provides more error-related information). Returned value description:
If `key` is `RuleId`, `Value` indicates the rule ID;
If `key` is `Protocol`, `Value` indicates the forwarding protocol of a rule;
If `key` is `VirtualPort`, `Value` indicates the forwarding port of a rule;
If `Key` is `ErrMessage`, `Value` indicates the exception message for health check;
Exception message for health check in the format of `"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6"`. Multiple error messages for the source IP should be separated by `,`,
SourceIp: real server IP, SourcePort: real server port, AbnormalStatTime: exception time, AbnormalReason: cause of exception, Interval: check frequency, CheckNum: number of checks, FailNum: number of failures;
        :type ExtErrHealths: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.ErrHealths = None
        self.ExtErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        if params.get("ExtErrHealths") is not None:
            self.ExtErrHealths = []
            for item in params.get("ExtErrHealths"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ExtErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7HealthConfigRequest(AbstractModel):
    """DescribeL7HealthConfig request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig response structure.

    """

    def __init__(self):
        """
        :param HealthConfig: Layer-7 health check configuration array
        :type HealthConfig: list of L7HealthConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackIndexRequest(AbstractModel):
    """DescribePackIndex request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")


class DescribePackIndexResponse(AbstractModel):
    """DescribePackIndex response structure.

    """

    def __init__(self):
        """
        :param Data: Field value as follows:
TotalPackCount: number of resources
AttackPackCount: number of resources being cleansed
BlockPackCount: number of blocked resources
ExpiredPackCount: number of expired resources
ExpireingPackCount: number of expiring resources
IsolatePackCount: number of isolated resources
        :type Data: list of KeyValue
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePcapRequest(AbstractModel):
    """DescribePcap request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param StartTime: Attack event start time in the format of "2018-08-28 07:00:00"
        :type StartTime: str
        :param EndTime: Attack event end time in the format of "2018-08-28 07:02:00"
        :type EndTime: str
        :param Ip: Resource IP, which is required only if `Business` is `net`;
        :type Ip: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")


class DescribePcapResponse(AbstractModel):
    """DescribePcap response structure.

    """

    def __init__(self):
        """
        :param PcapUrlList: PCAP packet download link list, which is an empty array if there are no PCAP packets;
        :type PcapUrlList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PcapUrlList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PcapUrlList = params.get("PcapUrlList")
        self.RequestId = params.get("RequestId")


class DescribePolicyCaseRequest(AbstractModel):
    """DescribePolicyCase request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param SceneId: Policy scenario ID
        :type SceneId: str
        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase response structure.

    """

    def __init__(self):
        """
        :param CaseList: Policy scenario list
        :type CaseList: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CaseList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CaseList") is not None:
            self.CaseList = []
            for item in params.get("CaseList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.CaseList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResIpListRequest(AbstractModel):
    """DescribeResIpList request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param IdList: Resource ID. If this field is left empty, it means to get all resources IP of the current user
        :type IdList: list of str
        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList response structure.

    """

    def __init__(self):
        """
        :param Resource: Resource IP list
        :type Resource: list of ResourceIp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Resource = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self.Resource = []
            for item in params.get("Resource"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resource.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RegionList: Region code search, which is optional. If no regions are to be specified, enter an empty array. If a region is to be specified, enter a region code, such as ["gz", "sh"]
        :type RegionList: list of str
        :param Line: Line search. This field can be optionally entered only when getting the list of Anti-DDoS Advanced resources. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. Please enter an empty array when getting other products;
        :type Line: list of int non-negative
        :param IdList: Resource ID search, which is optional. If this field is not an empty array, it means to get the resource list of a specified resource;
        :type IdList: list of str
        :param Name: Resource name search, which is optional. If this field is not an empty string, it means to search for resources by name;
        :type Name: str
        :param IpList: IP search list, which is optional. If this field is not empty, it means to search for resources by IP;
        :type IpList: list of str
        :param Status: Resource status search list, which is optional. Valid values: [0 (running), 1 (cleansing), 2 (blocking)]. No status search will be performed if an empty array is entered;
        :type Status: list of int non-negative
        :param Expire: Expiring resource search, which is optional. Valid values: [0 (no search), 1 (search for expiring resources)]
        :type Expire: int
        :param OderBy: Sort by field, which is optional
        :type OderBy: list of OrderBy
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param CName: CNAME of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;
        :type CName: str
        :param Domain: Domain name of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;
        :type Domain: str
        """
        self.Business = None
        self.RegionList = None
        self.Line = None
        self.IdList = None
        self.Name = None
        self.IpList = None
        self.Status = None
        self.Expire = None
        self.OderBy = None
        self.Limit = None
        self.Offset = None
        self.CName = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RegionList = params.get("RegionList")
        self.Line = params.get("Line")
        self.IdList = params.get("IdList")
        self.Name = params.get("Name")
        self.IpList = params.get("IpList")
        self.Status = params.get("Status")
        self.Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self.OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self.OderBy.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CName = params.get("CName")
        self.Domain = params.get("Domain")


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of records
        :type Total: int
        :param ServicePacks: Resource record list. Valid values of `key`:
"Key": "CreateTime" - resource instance purchase time
"Key": "Region" - resource instance region
"Key": "BoundIP" - IP bound to single IP instance
"Key": "Id" - resource instance ID
"Key": "CCEnabled" - CC protection status of resource instance
"Key": "DDoSThreshold" - DDoS cleansing threshold of resource instance	
"Key": "BoundStatus" - IP binding status of single IP instance or multi-IP instance (binding or bound)
"Key": "Type" - this field has been disused
"Key": "ElasticLimit" - elastic protection value of resource instance
"Key": "DDoSAI" - DDoS AI protection status of resource instance
"Key": "Bandwidth" - base protection value of resource instance
"Key": "OverloadCount" - number of attacks to the resource instance that exceed the elastic protection value
"Key": "Status" - resource instance status (idle: running, attacking: attacking, blocking: blocking, isolate: isolating)
"Key": "Lbid" - this field has been disused
"Key": "ShowFlag" - this field has been disused
"Key": "Expire" - resource instance expiration time
"Key": "CCThreshold" - CC protection triggering threshold of resource instance
"Key": "AutoRenewFlag" - auto-renewal flag of resource instance
"Key": "IspCode" - line of single IP instance or multi-IP instance (0: China Telecom, 1: China Unicom, 2: China Mobile, 5: BGP)
"Key": "PackType" - package type
"Key": "PackId" - package ID
"Key": "Name" - resource instance name
"Key": "Locked" - this field has been disused
"Key": "IpDDoSLevel" - protection level of resource instance (low: loose, middle: normal, high: strict)
"Key": "DefendStatus" - DDoS protection status of resource (enabled or temporarily disabled)
"Key": "UndefendExpire" - end time of temporary disablement of DDoS protection for resource instance
"Key": "Tgw" - whether the resource instance is a new resource
        :type ServicePacks: list of KeyValueRecord
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.ServicePacks = None
        self.Business = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self.ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ServicePacks.append(obj)
        self.Business = params.get("Business")
        self.RequestId = params.get("RequestId")


class DescribeRuleSetsRequest(AbstractModel):
    """DescribeRuleSets request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param IdList: Resource ID list
        :type IdList: list of str
        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets response structure.

    """

    def __init__(self):
        """
        :param L4RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules
        :type L4RuleSets: list of KeyValueRecord
        :param L7RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules
        :type L7RuleSets: list of KeyValueRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.L4RuleSets = None
        self.L7RuleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("L4RuleSets") is not None:
            self.L4RuleSets = []
            for item in params.get("L4RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L4RuleSets.append(obj)
        if params.get("L7RuleSets") is not None:
            self.L7RuleSets = []
            for item in params.get("L7RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L7RuleSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSchedulingDomainListRequest(AbstractModel):
    """DescribeSchedulingDomainList request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of items in a page. Returned results are not paged if you enter '0'.
        :type Limit: int
        :param Offset: Starting offset of the page. Value: (number of pages - 1) * items per page
        :type Offset: int
        :param Domain: (Optional) Filter by specific domain name
        :type Domain: str
        """
        self.Limit = None
        self.Offset = None
        self.Domain = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of scheduling domain names
        :type Total: int
        :param DomainList: List of scheduling domain names
        :type DomainList: list of SchedulingDomain
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomain()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecIndexRequest(AbstractModel):
    """DescribeSecIndex request structure.

    """


class DescribeSecIndexResponse(AbstractModel):
    """DescribeSecIndex response structure.

    """

    def __init__(self):
        """
        :param Data: Field value as follows:
AttackIpCount: number of attacked IPs
AttackCount: number of attacks
BlockCount: number of blockings
MaxMbps: attack bandwidth peak in Mbps
IpNum: IP statistics
        :type Data: list of KeyValue
        :param BeginDate: Start time of the current month
        :type BeginDate: str
        :param EndDate: End time of the current month
        :type EndDate: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.BeginDate = None
        self.EndDate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.RequestId = params.get("RequestId")


class DescribeSourceIpSegmentRequest(AbstractModel):
    """DescribeSourceIpSegment request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment response structure.

    """

    def __init__(self):
        """
        :param Data: Intermediate IP range. Multiple values are separated by ";"
        :type Data: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTransmitStatisRequest(AbstractModel):
    """DescribeTransmitStatis request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param MetricName: Metric name. Valid values:
traffic: traffic bandwidth;
pkg: packet rate;
        :type MetricName: str
        :param Period: Statistical time granularity (300: 5-minute, 3600: hourly, 86400: daily)
        :type Period: int
        :param StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5
        :type StartTime: str
        :param EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5
        :type EndTime: str
        :param IpList: Resource IP, which is required and only supports one IP if `Business` is `bgp-multip`. If this field is left empty, all IPs of a resource instance will be counted by default. If the resource instance has multiple IPs (such as Anti-DDoS Ultimate), the statistical method is summation;
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis response structure.

    """

    def __init__(self):
        """
        :param InDataList: If `MetricName` is `traffic`, this field indicates the inbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the inbound packet rate in pps;
        :type InDataList: list of float
        :param OutDataList: If `MetricName` is `traffic`, this field indicates the outbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the outbound packet rate in pps;
        :type OutDataList: list of float
        :param MetricName: Metric name:
traffic: traffic bandwidth;
pkg: packet rate;
        :type MetricName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InDataList = None
        self.OutDataList = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InDataList = params.get("InDataList")
        self.OutDataList = params.get("OutDataList")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeUnBlockStatisRequest(AbstractModel):
    """DescribeUnBlockStatis request structure.

    """


class DescribeUnBlockStatisResponse(AbstractModel):
    """DescribeUnBlockStatis response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of unblocking chances
        :type Total: int
        :param Used: Number of used chances
        :type Used: int
        :param BeginTime: Statistics start time
        :type BeginTime: str
        :param EndTime: Statistics end time
        :type EndTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Used = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribleL4RulesRequest(AbstractModel):
    """DescribleL4Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained
        :type RuleIdList: list of str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules response structure.

    """

    def __init__(self):
        """
        :param Rules: Forwarding rule list
        :type Rules: list of L4RuleEntry
        :param Total: Total number of rules
        :type Total: int
        :param Healths: Health check configuration list
        :type Healths: list of L4RuleHealth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleL7RulesRequest(AbstractModel):
    """DescribleL7Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained
        :type RuleIdList: list of str
        :param Limit: Number of entries per page. A value of 0 means no pagination
        :type Limit: int
        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page
        :type Offset: int
        :param Domain: Domain name search, which is optional. Enter it if you need to search for domain names
        :type Domain: str
        :param ProtocolList: Forwarding protocol search, which is optional. Valid values: [http, https, http/https]
        :type ProtocolList: list of str
        :param StatusList: Status search, which is optional. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]
        :type StatusList: list of int non-negative
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None
        self.Domain = None
        self.ProtocolList = None
        self.StatusList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        self.ProtocolList = params.get("ProtocolList")
        self.StatusList = params.get("StatusList")


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules response structure.

    """

    def __init__(self):
        """
        :param Rules: Forwarding rule list
        :type Rules: list of L7RuleEntry
        :param Total: Total number of rules
        :type Total: int
        :param Healths: Health check configuration list
        :type Healths: list of L7RuleHealth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleRegionCountRequest(AbstractModel):
    """DescribleRegionCount request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)
        :type Business: str
        :param LineList: Line search. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. This field is valid only for Anti-DDoS Advanced and should be ignored for other product
        :type LineList: list of int non-negative
        """
        self.Business = None
        self.LineList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.LineList = params.get("LineList")


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount response structure.

    """

    def __init__(self):
        """
        :param RegionList: Number of resource instances in region
        :type RegionList: list of RegionInstanceCount
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInstanceCount()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class IpBlackWhite(AbstractModel):
    """IP blocklist/allowlist

    """

    def __init__(self):
        """
        :param Ip: IP address
        :type Ip: str
        :param Type: Blocklist/allowlist type. Valid values: [black, white]
        :type Type: str
        """
        self.Ip = None
        self.Type = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")


class IpBlockData(AbstractModel):
    """IP blocking record

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param Status: Status (Blocked: blocked, UnBlocking: unblocking, UnBlockFailed: unblocking failed)
        :type Status: str
        :param BlockTime: Blocked time
        :type BlockTime: str
        :param UnBlockTime: Unblocked time (estimated)
        :type UnBlockTime: str
        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self.Ip = None
        self.Status = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Status = params.get("Status")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")


class IpUnBlockData(AbstractModel):
    """IP unblocking record

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param BlockTime: Blocked time
        :type BlockTime: str
        :param UnBlockTime: Unblocked time (actual)
        :type UnBlockTime: str
        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)
        :type ActionType: str
        """
        self.Ip = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")


class KeyValue(AbstractModel):
    """Field value in K-V format

    """

    def __init__(self):
        """
        :param Key: Field name
        :type Key: str
        :param Value: Field value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class KeyValueRecord(AbstractModel):
    """`KeyValue` record

    """

    def __init__(self):
        """
        :param Record: Key-Value array of a record
        :type Record: list of KeyValue
        """
        self.Record = None


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Record.append(obj)


class L4HealthConfig(AbstractModel):
    """Layer-4 health check configuration

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [TCP, UDP]
        :type Protocol: str
        :param VirtualPort: Forwarding port
        :type VirtualPort: int
        :param Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param TimeOut: Response timeout period in seconds
        :type TimeOut: int
        :param Interval: Detection interval in seconds
        :type Interval: int
        :param KickNum: Unhealthy threshold in times.
        :type KickNum: int
        :param AliveNum: Healthy threshold in times.
        :type AliveNum: int
        :param KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        """
        self.Protocol = None
        self.VirtualPort = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.KeepTime = params.get("KeepTime")


class L4RuleEntry(AbstractModel):
    """Layer-4 rule

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [TCP, UDP]
        :type Protocol: str
        :param VirtualPort: Forwarding port
        :type VirtualPort: int
        :param SourcePort: Real server port
        :type SourcePort: int
        :param SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]
        :type SourceType: int
        :param KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        :param SourceList: Forward list
        :type SourceList: list of L4RuleSource
        :param LbType: Load balancing method. Valid values: [1 (weighted round robin), 2 (source IP hash)]
        :type LbType: int
        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)];
        :type KeepEnable: int
        :param RuleId: Rule ID
        :type RuleId: str
        :param RuleName: Rule description
        :type RuleName: str
        :param RemoveSwitch: Watermark removal status. Valid values: [0 (disabled), 1 (enabled)]
        :type RemoveSwitch: int
        """
        self.Protocol = None
        self.VirtualPort = None
        self.SourcePort = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.RuleName = None
        self.RemoveSwitch = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.SourcePort = params.get("SourcePort")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RemoveSwitch = params.get("RemoveSwitch")


class L4RuleHealth(AbstractModel):
    """Rule health check parameter

    """

    def __init__(self):
        """
        :param RuleId: Rule ID
        :type RuleId: str
        :param Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param TimeOut: Response timeout period in seconds
        :type TimeOut: int
        :param Interval: Detection interval in seconds, which must be greater than the response timeout period
        :type Interval: int
        :param KickNum: Unhealthy threshold in times
        :type KickNum: int
        :param AliveNum: Healthy threshold in times.
        :type AliveNum: int
        """
        self.RuleId = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")


class L4RuleSource(AbstractModel):
    """Layer-4 forwarding rule list

    """

    def __init__(self):
        """
        :param Source: Intermediate IP or domain name
        :type Source: str
        :param Weight: Weight value. Value range: [0,100]
        :type Weight: int
        """
        self.Source = None
        self.Weight = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Weight = params.get("Weight")


class L7HealthConfig(AbstractModel):
    """Layer-7 health check configuration

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [http, https, http/https]
        :type Protocol: str
        :param Domain: Forwarding domain name
        :type Domain: str
        :param Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param Interval: Detection interval in seconds
        :type Interval: int
        :param KickNum: Number of exceptions in times
        :type KickNum: int
        :param AliveNum: Number of health checks in times
        :type AliveNum: int
        :param Method: Health check detection method. Valid values: HEAD, GET. Default VALUE: HEAD
        :type Method: str
        :param StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up
        :type StatusCode: int
        :param Url: URL of checked directory. Default value: /
        :type Url: str
        """
        self.Protocol = None
        self.Domain = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")


class L7RuleEntry(AbstractModel):
    """Layer-7 rule

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [http, https]
        :type Protocol: str
        :param Domain: Forwarding domain name
        :type Domain: str
        :param SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]
        :type SourceType: int
        :param KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        :param SourceList: Forward list
        :type SourceList: list of L4RuleSource
        :param LbType: Load balancing method. Valid value: [1 (weighted round robin)]
        :type LbType: int
        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]
        :type KeepEnable: int
        :param RuleId: Rule ID, which is optional when adding a new rule but required when modifying or deleting a rule;
        :type RuleId: str
        :param CertType: Certificate source, which is required if the forwarding protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]. If the forwarding protocol is HTTP, 0 can be entered for this field
        :type CertType: int
        :param SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID
        :type SSLId: str
        :param Cert: If the certificate is an external certificate, this field must be entered with the certificate content. (As external certificates are no longer supported, this field has been disused and does not need to be entered)
        :type Cert: str
        :param PrivateKey: If the certificate is an external certificate, this field must be entered with the certificate key. (As external certificates are no longer supported, this field has been disused and does not need to be entered)
        :type PrivateKey: str
        :param RuleName: Rule description
        :type RuleName: str
        :param Status: Rule status. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]
        :type Status: int
        :param CCStatus: CC protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type CCStatus: int
        :param CCEnable: HTTPS CC protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type CCEnable: int
        :param CCThreshold: HTTPS CC protection threshold
        :type CCThreshold: int
        :param CCLevel: HTTPS CC protection level
        :type CCLevel: str
        :param HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.
        :type HttpsToHttpEnable: int
        :param VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPort: int
        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.HttpsToHttpEnable = None
        self.VirtualPort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.VirtualPort = params.get("VirtualPort")


class L7RuleHealth(AbstractModel):
    """Layer-7 rule health check parameter

    """

    def __init__(self):
        """
        :param RuleId: Rule ID
        :type RuleId: str
        :param Enable: 1: enabled, 0: disabled
        :type Enable: int
        :param Interval: Detection interval in seconds
        :type Interval: int
        :param KickNum: Unhealthy threshold in times.
        :type KickNum: int
        :param AliveNum: Healthy threshold in times.
        :type AliveNum: int
        :param Method: HTTP request method. Valid values: [HEAD, GET]
        :type Method: str
        :param StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up
        :type StatusCode: int
        :param Url: URL of checked directory. Default value: /
        :type Url: str
        :param Status: Configuration status. 0: normal, 1: configuring, 2: configuration failed
        :type Status: int
        """
        self.RuleId = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RsId: Anti-DDoS instance ID
        :type RsId: str
        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value). It is set to 1000 on the backend by default
        :type AlarmThreshold: int
        :param IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs
        :type IpList: list of str
        """
        self.Business = None
        self.RsId = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesRequest(AbstractModel):
    """ModifyCCFrequencyRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param CCFrequencyRuleId: CC access frequency control rule ID
        :type CCFrequencyRuleId: str
        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]
        :type Mode: str
        :param Period: Reference period in seconds. Valid values: [10, 30, 60]
        :type Period: int
        :param ReqNumber: Number of access requests. Value range: [1-10000]
        :type ReqNumber: int
        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]
        :type Act: str
        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]
        :type ExeDuration: int
        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;
        :type Uri: str
        :param UserAgent: `User-Agent` string. Length limit: 80
        :type UserAgent: str
        :param Cookie: Cookie string. Length limit: 40
        :type Cookie: str
        """
        self.Business = None
        self.CCFrequencyRuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesStatusRequest(AbstractModel):
    """ModifyCCFrequencyRulesStatus request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API
        :type RuleId: str
        :param Method: Enables or disable. Valid values: ["on", "off"]
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCHostProtectionRequest(AbstractModel):
    """ModifyCCHostProtection request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Method: Enables/disables CC domain name protection. Valid values: [open (enable), close (disable)]
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCIpAllowDenyRequest(AbstractModel):
    """ModifyCCIpAllowDeny request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Method: add: add, delete: delete
        :type Method: str
        :param Type: Blocklist/allowlist type. Valid values: [white (allowlist), black (blocklist)]
        :type Type: str
        :param IpList: Blocklisted/whitelisted IP array
        :type IpList: list of str
        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;
        :type Protocol: str
        :param Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;
        :type Domain: str
        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API),
If `Method` is `delete`, this field can be left empty;
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.IpList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCLevelRequest(AbstractModel):
    """ModifyCCLevel request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Level: CC protection level. Valid values: [default (normal), loose (loose), strict (strict)];
        :type Level: str
        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;
        :type Protocol: str
        :param RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API);
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Level = None
        self.Protocol = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Level = params.get("Level")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCPolicySwitchRequest(AbstractModel):
    """ModifyCCPolicySwitch request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param SetId: Policy ID
        :type SetId: str
        :param Switch: Status
        :type Switch: int
        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Switch = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        self.Switch = params.get("Switch")


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCSelfDefinePolicyRequest(AbstractModel):
    """ModifyCCSelfDefinePolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param SetId: Policy ID
        :type SetId: str
        :param Policy: Details of the CC protection policy
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCThresholdRequest(AbstractModel):
    """ModifyCCThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic
        :type Business: str
        :param Threshold: CC protection threshold. Valid values: (0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
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
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;
        :type Protocol: str
        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API);
Required if `Protocol` is `https`;
        :type RuleId: str
        :param BasicIp: Queried IP address (only provided by Anti-DDoS Basic), such as 1.1.1.1
        :type BasicIp: str
        :param BasicRegion: IP region (only provided for Anti-DDoS Basic). Valid values: region abbreviations such as gz, bj, sh, and hk
        :type BasicRegion: str
        :param BasicBizType: Zone type (only provided for Anti-DDoS Basic). Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).
        :type BasicBizType: str
        :param BasicDeviceType: Device type (only provided for Anti-DDoS Basic). Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).
        :type BasicDeviceType: str
        :param BasicIpInstance: IPInstance Nat gateway (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)
        :type BasicIpInstance: str
        :param BasicIspCode: ISP line (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)
        :type BasicIspCode: int
        :param Domain: This optional field must be specified when HTTPS protocol is used.
        :type Domain: str
        """
        self.Business = None
        self.Threshold = None
        self.Id = None
        self.Protocol = None
        self.RuleId = None
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Threshold = params.get("Threshold")
        self.Id = params.get("Id")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")
        self.Domain = params.get("Domain")


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCUrlAllowRequest(AbstractModel):
    """ModifyCCUrlAllow request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Method: add: add, delete: delete
        :type Method: str
        :param Type: Blocklist/allowlist type. Valid value: [white (allowlist)]
        :type Type: str
        :param UrlList: URL array. URL format:
http://domain name/cgi
https://domain name/cgi
        :type UrlList: list of str
        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;
        :type Protocol: str
        :param Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;
        :type Domain: str
        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only when adding a rule and `Protocol` is `https`;
If `Method` is `delete`, this field can be left empty;
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.UrlList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.UrlList = params.get("UrlList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSAIStatusRequest(AbstractModel):
    """ModifyDDoSAIStatus request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Method: get (read AI protection status), set (modify AI protection status);
        :type Method: str
        :param DDoSAI: AI protection status, which is required if `Method` is `set`. Valid values: [on, off].
        :type DDoSAI: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSAI = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSAI = params.get("DDoSAI")


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus response structure.

    """

    def __init__(self):
        """
        :param DDoSAI: AI protection status. Valid values: [on, off]
        :type DDoSAI: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DDoSAI = None
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DDoSAI = params.get("DDoSAI")
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class ModifyDDoSAlarmThresholdRequest(AbstractModel):
    """ModifyDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)
        :type Business: str
        :param RsId: Anti-DDoS instance ID
        :type RsId: str
        :param AlarmType: Alarm threshold type. 0: not set, 1: inbound traffic, 2: cleansed traffic
        :type AlarmType: int
        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)
        :type AlarmThreshold: int
        :param IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs
        :type IpList: list of str
        """
        self.Business = None
        self.RsId = None
        self.AlarmType = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSDefendStatusRequest(AbstractModel):
    """ModifyDDoSDefendStatus request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic
        :type Business: str
        :param Status: Protection status. Valid values: [0 (disabled), 1 (enabled)]
        :type Status: int
        :param Hour: Disablement duration in hours. Valid values: [0, 1, 2, 3, 4, 5, 6]. If `Status` is `0` (indicating to disable), `Hour` must be greater than 0;
        :type Hour: int
        :param Id: Resource ID, which is required if `Business` is not Anti-DDoS Basic;
        :type Id: str
        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
        self.Business = None
        self.Status = None
        self.Hour = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Method: get (read protection level), set (modify protection level);
        :type Method: str
        :param DDoSLevel: Protection level, which is required if `Method` is `set`. Valid values: [low,middle,high]
        :type DDoSLevel: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSLevel = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSLevel = params.get("DDoSLevel")


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel response structure.

    """

    def __init__(self):
        """
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param DDoSLevel: Protection level. Valid values: [low,middle,high]
        :type DDoSLevel: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.DDoSLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DDoSLevel = params.get("DDoSLevel")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyCaseRequest(AbstractModel):
    """ModifyDDoSPolicyCase request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param SceneId: Policy scenario ID
        :type SceneId: str
        :param PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]
        :type PlatformTypes: list of str
        :param AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]
        :type AppType: str
        :param AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]
        :type AppProtocols: list of str
        :param TcpSportStart: TCP start port. Value range: (0, 65535]
        :type TcpSportStart: str
        :param TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port
        :type TcpSportEnd: str
        :param UdpSportStart: UDP start port. Value range: (0, 65535]
        :type UdpSportStart: str
        :param UdpSportEnd: End UDP business port. Value range: (0, 65535). It must be greater than or equal to the start UDP business port
        :type UdpSportEnd: str
        :param HasAbroad: Whether there are customers outside Mainland China. Valid values: [no, yes]
        :type HasAbroad: str
        :param HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]
        :type HasInitiateTcp: str
        :param HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]
        :type HasInitiateUdp: str
        :param PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]
        :type PeerTcpPort: str
        :param PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]
        :type PeerUdpPort: str
        :param TcpFootprint: Fixed feature code of TCP payload. String length limit: 512
        :type TcpFootprint: str
        :param UdpFootprint: Fixed feature code of UDP payload. String length limit: 512
        :type UdpFootprint: str
        :param WebApiUrl: Web business API URL
        :type WebApiUrl: list of str
        :param MinTcpPackageLen: Minimum length of TCP business packet. Value range: (0, 1500)
        :type MinTcpPackageLen: str
        :param MaxTcpPackageLen: Maximum length of TCP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP business packet
        :type MaxTcpPackageLen: str
        :param MinUdpPackageLen: Minimum length of UDP business packet. Value range: (0, 1500)
        :type MinUdpPackageLen: str
        :param MaxUdpPackageLen: Maximum length of UDP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP business packet
        :type MaxUdpPackageLen: str
        :param HasVPN: Whether there are VPN businesses. Valid values: [no, yes]
        :type HasVPN: str
        :param TcpPortList: TCP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param UdpPortList: UDP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self.Business = None
        self.SceneId = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyNameRequest(AbstractModel):
    """ModifyDDoSPolicyName request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param Name: Policy name
        :type Name: str
        """
        self.Business = None
        self.PolicyId = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Name = params.get("Name")


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param DropOptions: Protocol disablement, which must be entered, and the array length must be 1
        :type DropOptions: list of DDoSPolicyDropOption
        :param PortLimits: Port disablement. If no ports are to be disabled, enter an empty array
        :type PortLimits: list of DDoSPolicyPortLimit
        :param IpAllowDenys: IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist
        :type IpAllowDenys: list of IpBlackWhite
        :param PacketFilters: Packet filter. Enter an empty array if there are no packets to filter
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param WaterPrint: Watermarking policy parameter. Enter an empty array if the watermarking feature is not enabled. At most one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)
        :type WaterPrint: list of WaterPrintPolicy
        """
        self.Business = None
        self.PolicyId = None
        self.DropOptions = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSSwitchRequest(AbstractModel):
    """ModifyDDoSSwitch request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic
        :type Business: str
        :param Method: `get`: read DDoS protection status, `set`: modify DDoS protection status
        :type Method: str
        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;
        :type Ip: str
        :param BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]
        :type BizType: str
        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]
        :type DeviceType: str
        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;
        :type InstanceId: str
        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
        :param Status: Protection status value, which is optional. Valid values: [0 (disabled), 1 (enabled)]. If `Method` is `get`, this field can be left empty;
        :type Status: int
        """
        self.Business = None
        self.Method = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")
        self.Status = params.get("Status")


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch response structure.

    """

    def __init__(self):
        """
        :param Status: Current protection status value. Valid values: [0 (disabled), 1 (enabled)]
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Threshold: DDoS cleansing threshold. Valid values: [0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
If the value is set to 0, the default value will be used;
        :type Threshold: int
        """
        self.Business = None
        self.Id = None
        self.Threshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Threshold = params.get("Threshold")


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSWaterKeyRequest(AbstractModel):
    """ModifyDDoSWaterKey request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param Method: Key operation. Valid values: [add (add), delete (delete), open (open), close (close), get (get key)]
        :type Method: str
        :param KeyId: Key ID, which can be left empty or 0 when adding a key but is required for other operations
        :type KeyId: int
        """
        self.Business = None
        self.PolicyId = None
        self.Method = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        self.KeyId = params.get("KeyId")


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey response structure.

    """

    def __init__(self):
        """
        :param KeyList: Watermark key list
        :type KeyList: list of WaterPrintKey
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyElasticLimitRequest(AbstractModel):
    """ModifyElasticLimit request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Limit: Elastic protection threshold. Valid values: [0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]
        :type Limit: int
        """
        self.Business = None
        self.Id = None
        self.Limit = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4HealthRequest(AbstractModel):
    """ModifyL4Health request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Healths: Health check parameter array
        :type Healths: list of L4RuleHealth
        """
        self.Business = None
        self.Id = None
        self.Healths = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4KeepTimeRequest(AbstractModel):
    """ModifyL4KeepTime request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]
        :type KeepEnable: int
        :param KeepTime: Session persistence duration in seconds
        :type KeepTime: int
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.KeepEnable = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.KeepEnable = params.get("KeepEnable")
        self.KeepTime = params.get("KeepTime")


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4RulesRequest(AbstractModel):
    """ModifyL4Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL7RulesRequest(AbstractModel):
    """ModifyL7Rules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNetReturnSwitchRequest(AbstractModel):
    """ModifyNetReturnSwitch request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param Status: Switch status. 0: disabled, 1: enabled
        :type Status: int
        :param Hour: Switch duration in hours. Valid values: [0,1,2,3,4,5,6;]. If `status` is 1, this field is required and must be greater than 0
        :type Hour: int
        """
        self.Business = None
        self.Id = None
        self.Status = None
        self.Hour = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param Id: Anti-DDoS instance ID.
        :type Id: str
        :param Rule: Domain name forwarding rule.
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.NewL7RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = NewL7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNewL4RuleRequest(AbstractModel):
    """ModifyNewL4Rule request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).
        :type Business: str
        :param Id: Anti-DDoS instance ID.
        :type Id: str
        :param Rule: Forwarding rule.
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyNewL4RuleResponse(AbstractModel):
    """ModifyNewL4Rule response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyResBindDDoSPolicyRequest(AbstractModel):
    """ModifyResBindDDoSPolicy request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate
        :type Business: str
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param PolicyId: Policy ID
        :type PolicyId: str
        :param Method: bind: bind policy; unbind: unbind policy
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.PolicyId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyResourceRenewFlagRequest(AbstractModel):
    """ModifyResourceRenewFlag request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `shield`: Chess Shield, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `insurance`: guarantee package, `staticpack`: non-BGP package
        :type Business: str
        :param Id: Resource ID
        :type Id: str
        :param RenewFlag: Auto-renewal flag (0: manual renewal, 1: auto-renewal, 2: no renewal upon expiration)
        :type RenewFlag: int
        """
        self.Business = None
        self.Id = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RenewFlag = params.get("RenewFlag")


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag response structure.

    """

    def __init__(self):
        """
        :param Success: Success code
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class NewL7RuleEntry(AbstractModel):
    """Layer-7 rule.

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: `http` and `https`.
        :type Protocol: str
        :param Domain: Forwarding domain name.
        :type Domain: str
        :param SourceType: Forwarding method. Valid values: `1` (by domain name); `2` (by IP).
        :type SourceType: int
        :param KeepTime: Session persistence duration, in seconds.
        :type KeepTime: int
        :param SourceList: List of sources
        :type SourceList: list of L4RuleSource
        :param LbType: Load balancing method. Valid value: `1` (weighed polling).
        :type LbType: int
        :param KeepEnable: Whether session persistence is enabled. Valid values: `0` (disabled) and `1` (enabled).
        :type KeepEnable: int
        :param RuleId: Rule ID. This field is not required for adding a rule, but is required for modifying or deleting a rule.
        :type RuleId: str
        :param CertType: Certificate source. When the forwarding protocol is HTTPS, this field must be set to `2` (Tencent Cloud managed certificate), and for HTTP protocol, it can be set to `0`.
        :type CertType: int
        :param SSLId: When the certificate source is Tencent Cloud managed certificate, this field must be set to the ID of the managed certificate.
        :type SSLId: str
        :param Cert: [Disused] When the certificate is an external certificate, the certificate content should be provided here. 
        :type Cert: str
        :param PrivateKey: [Disused] When the certificate is an external certificate, the certificate key should be provided here. 
        :type PrivateKey: str
        :param RuleName: Rule description.
        :type RuleName: str
        :param Status: Rule status. Valid values: `0` (the rule was successfully configured), `1` (configuring the rule), `2` (rule configuration failed), `3` (deleting the rule), `5` (failed to delete rule), `6` (rule awaiting configuration), `7` (rule awaiting deletion), and `8` (rule awaiting certificate configuration).
        :type Status: int
        :param CCStatus: CC protection status. Valid values: `0` (disabled) and `1` (enabled).
        :type CCStatus: int
        :param CCEnable: CC protection status based on HTTPS. Valid values: `0` (disabled) and `1` (enabled).
        :type CCEnable: int
        :param CCThreshold: CC protection threshold based on HTTPS.
        :type CCThreshold: int
        :param CCLevel: CC protection level based on HTTPS.
        :type CCLevel: str
        :param Region: Region code.
        :type Region: int
        :param Id: Anti-DDoS instance ID.
        :type Id: str
        :param Ip: Anti-DDoS instance IP address.
        :type Ip: str
        :param ModifyTime: Modification time.
        :type ModifyTime: str
        :param HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.
        :type HttpsToHttpEnable: int
        :param VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPort: int
        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.Region = None
        self.Id = None
        self.Ip = None
        self.ModifyTime = None
        self.HttpsToHttpEnable = None
        self.VirtualPort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.ModifyTime = params.get("ModifyTime")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.VirtualPort = params.get("VirtualPort")


class OrderBy(AbstractModel):
    """Sort by field

    """

    def __init__(self):
        """
        :param Field: Sort by field name. Valid values: [
bandwidth (bandwidth),
overloadCount (number of times of exceeding peak value)
]
        :type Field: str
        :param Order: Sorting order. Valid values: [asc (ascending), desc (descending)]
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class Paging(AbstractModel):
    """Pagination index

    """

    def __init__(self):
        """
        :param Offset: Starting position
        :type Offset: int
        :param Limit: Quantity
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ProtocolPort(AbstractModel):
    """Protocol and port parameters

    """

    def __init__(self):
        """
        :param Protocol: Protocol (TCP, UDP)
        :type Protocol: str
        :param Port: Port
        :type Port: int
        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class RegionInstanceCount(AbstractModel):
    """Number of resource instances in region

    """

    def __init__(self):
        """
        :param Region: Region code
        :type Region: str
        :param RegionV3: Region code (new specification)
        :type RegionV3: str
        :param Count: Number of resource instances
        :type Count: int
        """
        self.Region = None
        self.RegionV3 = None
        self.Count = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionV3 = params.get("RegionV3")
        self.Count = params.get("Count")


class ResourceIp(AbstractModel):
    """Resource IP array

    """

    def __init__(self):
        """
        :param Id: Anti-DDoS instance ID
        :type Id: str
        :param IpList: Resource IP array
        :type IpList: list of str
        """
        self.Id = None
        self.IpList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")


class SchedulingDomain(AbstractModel):
    """Scheduling domain name information

    """

    def __init__(self):
        """
        :param Domain: Scheduling domain name
        :type Domain: str
        :param BGPIpList: List of BGP IPs
        :type BGPIpList: list of str
        :param CTCCIpList: List of CTCC IPs
        :type CTCCIpList: list of str
        :param CUCCIpList: List of CUCC IPs
        :type CUCCIpList: list of str
        :param CMCCIpList: List of CMCC IPs
        :type CMCCIpList: list of str
        :param OverseaIpList: List of IPs outside Mainland China
        :type OverseaIpList: list of str
        :param Method: Scheduling method. It only supports `priority` now.
        :type Method: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param TTL: 
        :type TTL: int
        :param Status: Status
        :type Status: int
        :param ModifyTime: Modification time
        :type ModifyTime: str
        """
        self.Domain = None
        self.BGPIpList = None
        self.CTCCIpList = None
        self.CUCCIpList = None
        self.CMCCIpList = None
        self.OverseaIpList = None
        self.Method = None
        self.CreateTime = None
        self.TTL = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.BGPIpList = params.get("BGPIpList")
        self.CTCCIpList = params.get("CTCCIpList")
        self.CUCCIpList = params.get("CUCCIpList")
        self.CMCCIpList = params.get("CMCCIpList")
        self.OverseaIpList = params.get("OverseaIpList")
        self.Method = params.get("Method")
        self.CreateTime = params.get("CreateTime")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")


class SuccessCode(AbstractModel):
    """Operation return code, which is only used to return success

    """

    def __init__(self):
        """
        :param Code: Success/error code
        :type Code: str
        :param Message: Description
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class WaterPrintKey(AbstractModel):
    """Watermark key

    """

    def __init__(self):
        """
        :param KeyId: Watermark key ID
        :type KeyId: str
        :param KeyContent: Watermark key value
        :type KeyContent: str
        :param KeyVersion: Watermark key version number
        :type KeyVersion: str
        :param OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]
        :type OpenStatus: int
        :param CreateTime: Key generation time
        :type CreateTime: str
        """
        self.KeyId = None
        self.KeyContent = None
        self.KeyVersion = None
        self.OpenStatus = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyContent = params.get("KeyContent")
        self.KeyVersion = params.get("KeyVersion")
        self.OpenStatus = params.get("OpenStatus")
        self.CreateTime = params.get("CreateTime")


class WaterPrintPolicy(AbstractModel):
    """Watermarking policy parameter

    """

    def __init__(self):
        """
        :param TcpPortList: TCP port range, such as ["2000-3000","3500-4000"]
        :type TcpPortList: list of str
        :param UdpPortList: UDP port range, such as ["2000-3000","3500-4000"]
        :type UdpPortList: list of str
        :param Offset: Watermark offset. Value range: [0, 100)
        :type Offset: int
        :param RemoveSwitch: Whether to automatically remove. Valid values: [0 (no), 1 (yes)]
        :type RemoveSwitch: int
        :param OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]
        :type OpenStatus: int
        """
        self.TcpPortList = None
        self.UdpPortList = None
        self.Offset = None
        self.RemoveSwitch = None
        self.OpenStatus = None


    def _deserialize(self, params):
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")
        self.Offset = params.get("Offset")
        self.RemoveSwitch = params.get("RemoveSwitch")
        self.OpenStatus = params.get("OpenStatus")