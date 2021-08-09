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
        """
        :param MetricName: Metric name (connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;)\n        :type MetricName: str\n        :param Data: Value array\n        :type Data: list of float\n        :param Count: Value array size\n        :type Count: int\n        """
        self.MetricName = None
        self.Data = None
        self.Count = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """IP object bound to Anti-DDoS Pro

    """

    def __init__(self):
        """
        :param Ip: IP address\n        :type Ip: str\n        :param BizType: Category of product that can be bound. Valid values: public (CVM and CLB), bm (BM), eni (ENI), vpngw (VPN gateway), natgw (NAT gateway), waf (WAF), fpc (financial products), gaap (GAAP), and other (Hosted IP).\n        :type BizType: str\n        :param DeviceType: Subtype under product type. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]\n        :type DeviceType: str\n        :param InstanceId: Resource instance ID of IP. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`; if it is a hosted IP without corresponding resource instance ID, enter "none";\n        :type InstanceId: str\n        """
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCAlarmThreshold(AbstractModel):
    """CC alarm threshold

    """

    def __init__(self):
        """
        :param AlarmThreshold: CC alarm threshold\n        :type AlarmThreshold: int\n        """
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCEventRecord(AbstractModel):
    """CC attack event record

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Vip: Resource IP\n        :type Vip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param ReqQps: Total requests peak (QPS)\n        :type ReqQps: int\n        :param DropQps: Attack peak (QPS)\n        :type DropQps: int\n        :param AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]\n        :type AttackStatus: int\n        :param ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceName: str\n        :param DomainList: Domain name list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomainList: str\n        :param UriList: URI list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UriList: str\n        :param AttackipList: Attack source list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AttackipList: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCFrequencyRule(AbstractModel):
    """Access frequency control rule for CC protection

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: ID of the access frequency control rule for CC protection\n        :type CCFrequencyRuleId: str\n        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;\n        :type Uri: str\n        :param UserAgent: `User-Agent` string. Length limit: 80\n        :type UserAgent: str\n        :param Cookie: Cookie string. Length limit: 40\n        :type Cookie: str\n        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]\n        :type Mode: str\n        :param Period: Reference period in seconds. Valid values: [10, 30, 60]\n        :type Period: int\n        :param ReqNumber: Number of access requests. Value range: [1-10000]\n        :type ReqNumber: int\n        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]\n        :type Act: str\n        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]\n        :type ExeDuration: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPolicy(AbstractModel):
    """Custom CC protection rule

    """

    def __init__(self):
        """
        :param Name: Policy name\n        :type Name: str\n        :param Smode: Matching mode. Valid values: [matching (matching mode), speedlimit (speed limiting mode)]\n        :type Smode: str\n        :param SetId: Policy ID\n        :type SetId: str\n        :param Frequency: Number of requests allowed per minute\n        :type Frequency: int\n        :param ExeMode: Executed policy mode. Valid values: [alg (verification code), drop (blocking)]\n        :type ExeMode: str\n        :param Switch: Specifies whether the policy is activated\n        :type Switch: int\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param RuleList: Rule list\n        :type RuleList: list of CCRule\n        :param IpList: IP list. If this field is to be left empty, please pass in an empty instead of null;\n        :type IpList: list of str\n        :param Protocol: CC protection type. Valid values: [http, https]\n        :type Protocol: str\n        :param RuleId: ID of the forwarding rule corresponding to the HTTPS CC protection domain name\n        :type RuleId: str\n        :param Domain: HTTPS CC protection domain name\n        :type Domain: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRule(AbstractModel):
    """The custom CC protection policy in key-value format

    """

    def __init__(self):
        """
        :param Skey: Key of the policy. Valid values: `host`, `cgi`, `ua`, `referer`\n        :type Skey: str\n        :param Operator: Rule condition. Valid values: `include`, `not_include`, `equal`\n        :type Operator: str\n        :param Value: Value of the policy. Length limit: 31 bytes\n        :type Value: str\n        """
        self.Skey = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleConfig(AbstractModel):
    """Custom layer-7 CC policy

    """

    def __init__(self):
        """
        :param Period: Reference period in seconds. Valid values: [10, 30, 60]\n        :type Period: int\n        :param ReqNumber: Number of access requests. Value range: [1-10000]\n        :type ReqNumber: int\n        :param Action: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]\n        :type Action: str\n        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]\n        :type ExeDuration: int\n        """
        self.Period = None
        self.ReqNumber = None
        self.Action = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Action = params.get("Action")
        self.ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`basic`: Anti-DDoS Basic)\n        :type Business: str\n        :param Method: `get`: read alarm threshold, `set`: set alarm threshold\n        :type Method: str\n        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is required if `Method` is `set`;\n        :type AlarmType: int\n        :param AlarmThreshold: Alarm threshold. It is required if `Method` is `set`. If it is set to 0, it means to clear the alarm threshold configuration;\n        :type AlarmThreshold: int\n        """
        self.Business = None
        self.Method = None
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param AlarmThreshold: If there is an alarm threshold configuration, the returned alarm threshold will be greater than 0; otherwise, the returned alarm threshold will be 0;\n        :type AlarmThreshold: int\n        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic. This field is valid if `AlarmThreshold` is above 0;\n        :type AlarmType: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param BoundDevList: Array of IPs to be bound to the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP. If there are no IPs to bind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;\n        :type BoundDevList: list of BoundIpInfo\n        :param UnBoundDevList: Array of IPs to be unbound from Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, this array can contain only one IP; if there are no IPs to unbind, it can be empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty;\n        :type UnBoundDevList: list of BoundIpInfo\n        :param CopyPolicy: [Disused]\n        :type CopyPolicy: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API\n        :type RuleId: str\n        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]\n        :type Mode: str\n        :param Period: Reference period in seconds. Valid values: [10, 30, 60]\n        :type Period: int\n        :param ReqNumber: Number of access requests. Value range: [1-10000]\n        :type ReqNumber: int\n        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]\n        :type Act: str\n        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]\n        :type ExeDuration: int\n        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;\n        :type Uri: str\n        :param UserAgent: `User-Agent` string. Length limit: 80\n        :type UserAgent: str\n        :param Cookie: Cookie string. Length limit: 40\n        :type Cookie: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: Access frequency control rule ID for CC protection\n        :type CCFrequencyRuleId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Policy: Details of the CC protection policy\n        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`\n        """
        self.Business = None
        self.Id = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param CaseName: Policy scenario name string. Length limit: 64\n        :type CaseName: str\n        :param PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]\n        :type PlatformTypes: list of str\n        :param AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]\n        :type AppType: str\n        :param AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]\n        :type AppProtocols: list of str\n        :param TcpSportStart: TCP start port. Value range: (0, 65535]\n        :type TcpSportStart: str\n        :param TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port.\n        :type TcpSportEnd: str\n        :param UdpSportStart: UDP start port. Value range: (0, 65535]\n        :type UdpSportStart: str\n        :param UdpSportEnd: UDP end port. Value range: (0, 65535). It must be greater than or equal to the UDP start port.\n        :type UdpSportEnd: str\n        :param HasAbroad: Whether there are customers outside China. Valid values: [no, yes]\n        :type HasAbroad: str\n        :param HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]\n        :type HasInitiateTcp: str\n        :param HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]\n        :type HasInitiateUdp: str\n        :param PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]\n        :type PeerTcpPort: str\n        :param PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]\n        :type PeerUdpPort: str\n        :param TcpFootprint: Fixed feature code of TCP payload. Max string length: 512\n        :type TcpFootprint: str\n        :param UdpFootprint: Fixed feature code of UDP payload. Max string length: 512\n        :type UdpFootprint: str\n        :param WebApiUrl: Web application API URL\n        :type WebApiUrl: list of str\n        :param MinTcpPackageLen: Minimum length of TCP packet. Value range: (0, 1500)\n        :type MinTcpPackageLen: str\n        :param MaxTcpPackageLen: Maximum length of TCP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP packet\n        :type MaxTcpPackageLen: str\n        :param MinUdpPackageLen: Minimum length of UDP packet. Value range: (0, 1500)\n        :type MinUdpPackageLen: str\n        :param MaxUdpPackageLen: Maximum length of UDP packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP packet\n        :type MaxUdpPackageLen: str\n        :param HasVPN: Whether there are applications using VPN. Valid values: [no, yes]\n        :type HasVPN: str\n        :param TcpPortList: TCP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.\n        :type TcpPortList: str\n        :param UdpPortList: UDP port list. You can enter a single port, or a port range. Format: 80,443,700-800,53,1000-3000.\n        :type UdpPortList: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param SceneId: Policy scenario ID\n        :type SceneId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param DropOptions: Protocol disablement, which must be entered, and the array length must be 1\n        :type DropOptions: list of DDoSPolicyDropOption\n        :param Name: Policy name\n        :type Name: str\n        :param PortLimits: Ports to be closed. If no ports are to be closed, enter an empty array\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param IpAllowDenys: Request source IP blocklist/allowlist, which should be an empty array if there are no blocked or allowed IPs.\n        :type IpAllowDenys: list of IpBlackWhite\n        :param PacketFilters: Packet filter. Enter an empty array if there are no packets to filter\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param WaterPrint: Watermarking policy parameters. Enter an empty array if the watermarking feature is not enabled. Only one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)\n        :type WaterPrint: list of WaterPrintPolicy\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Name: Instance name. Length limit: 32 characters\n        :type Name: str\n        """
        self.Business = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param HealthConfig: Layer-4 health check configuration array\n        :type HealthConfig: list of L4HealthConfig\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Rules: Rule list\n        :type Rules: list of L4RuleEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Method: Operation. Valid values: [query (query), add (add), del (delete)]\n        :type Method: str\n        :param RuleId: Layer-7 forwarding rule ID, such as rule-0000001\n        :type RuleId: str\n        :param RuleConfig: Custom layer-7 CC protection rule. If the `Method` is `query`, this field can be left empty; if the `Method` is `add` or `del`, it is required, and the array length can only be 1;\n        :type RuleConfig: list of CCRuleConfig\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule response structure.

    """

    def __init__(self):
        """
        :param RuleConfig: Custom layer-7 CC protection rule parameters. If custom CC protection rule is not enabled, an empty array will be returned.\n        :type RuleConfig: list of CCRuleConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param HealthConfig: Layer-7 health check configuration array\n        :type HealthConfig: list of L7HealthConfig\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: The resource instance ID, such as the ID of an Anti-DDoS Advanced instance or the ID of an Anti-DDoS Ultimate instance.\n        :type Id: str\n        :param RuleId: Rule ID\n        :type RuleId: str\n        :param CertType: Certificate type, which is required if the protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]\n        :type CertType: int\n        :param SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID.\n        :type SSLId: str\n        :param Cert: [Disused] If the certificate is an external certificate, this field must be entered with the certificate content. \n        :type Cert: str\n        :param PrivateKey: [Disused] If the certificate is an external certificate, this field must be entered with the certificate key. \n        :type PrivateKey: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Rules: Rule list\n        :type Rules: list of L7RuleEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Rules: Rule list\n        :type Rules: list of L7RuleEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesUploadRequest(AbstractModel):
    """CreateNewL7RulesUpload request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).\n        :type Business: str\n        :param IdList: Resource ID list.\n        :type IdList: list of str\n        :param VipList: Resource IP address list.\n        :type VipList: list of str\n        :param Rules: Rule list.\n        :type Rules: list of L7RuleEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesUploadResponse(AbstractModel):
    """CreateNewL7RulesUpload response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Ip: IP\n        :type Ip: str\n        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)\n        :type ActionType: str\n        """
        self.Ip = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp response structure.

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)\n        :type ActionType: str\n        :param UnblockTime: Unblocked time (estimated)\n        :type UnblockTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AlarmType: Alarm threshold type. 1: inbound traffic, 2: cleansed traffic\n        :type AlarmType: int\n        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)\n        :type AlarmThreshold: int\n        """
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceRecord(AbstractModel):
    """Attack source information

    """

    def __init__(self):
        """
        :param SrcIp: Attack source IP\n        :type SrcIp: str\n        :param Province: Province (valid for Mainland China)\n        :type Province: str\n        :param Nation: Country/region\n        :type Nation: str\n        :param PacketSum: Total number of attack packets\n        :type PacketSum: int\n        :param PacketLen: Total attack traffic\n        :type PacketLen: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSEventRecord(AbstractModel):
    """DDoS attack event record

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Vip: Resource IP\n        :type Vip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param Mbps: Maximum attack bandwidth\n        :type Mbps: int\n        :param Pps: Maximum attack packet rate\n        :type Pps: int\n        :param AttackType: Attack type\n        :type AttackType: str\n        :param BlockFlag: Whether the IP is blocked. Valid values: [1 (yes), 0 (no), 2 (invalid value)]\n        :type BlockFlag: int\n        :param OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes (yes), no (no), empty string (unknown value)]\n        :type OverLoad: str\n        :param AttackStatus: Attack status. Valid values: [0 (ongoing), 1 (ended)]\n        :type AttackStatus: int\n        :param ResourceName: Resource name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceName: str\n        :param EventId: Attack event ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EventId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyDropOption(AbstractModel):
    """Disabled protocol in advanced DDoS policy

    """

    def __init__(self):
        """
        :param DropTcp: Blocks all TCP traffic. Valid values: [0,1]\n        :type DropTcp: int\n        :param DropUdp: Blocks all UDP traffic. Valid values: [0,1]\n        :type DropUdp: int\n        :param DropIcmp: Blocks all ICMP traffic. Valid values: [0,1]\n        :type DropIcmp: int\n        :param DropOther: Blocks traffic of other protocols. Valid values: [0,1]\n        :type DropOther: int\n        :param DropAbroad: Rejects traffic from outside Mainland China. Valid values: [0,1]\n        :type DropAbroad: int\n        :param CheckSyncConn: Null session protection. Valid values: [0,1]\n        :type CheckSyncConn: int\n        :param SdNewLimit: New connection suppression based on source IP and destination IP. Value range: [0,4294967295]\n        :type SdNewLimit: int\n        :param DstNewLimit: New connection suppression based on destination IP. Value range: [0,4294967295]\n        :type DstNewLimit: int\n        :param SdConnLimit: Concurrent connection suppression based on source IP and destination IP. Value range: [0,4294967295]\n        :type SdConnLimit: int\n        :param DstConnLimit: Concurrent connection suppression based on destination IP. Value range: [0,4294967295]\n        :type DstConnLimit: int\n        :param BadConnThreshold: Threshold for triggering connection suppression. Value range: [0,4294967295]\n        :type BadConnThreshold: int\n        :param NullConnEnable: Exceptional connection detection condition: null session protection status. Valid values: [0,1]\n        :type NullConnEnable: int\n        :param ConnTimeout: Exceptional connection detection condition: connection timeout. Valid values: [0,65535]\n        :type ConnTimeout: int\n        :param SynRate: Exceptional connection detection condition: percentage of SYN out of ACK. Valid values: [0,100]\n        :type SynRate: int\n        :param SynLimit: Exceptional connection detection condition: SYN threshold. Valid values: [0,100]\n        :type SynLimit: int\n        :param DTcpMbpsLimit: TCP speed limit. Value range: [0,4294967295]\n        :type DTcpMbpsLimit: int\n        :param DUdpMbpsLimit: UDP speed limit. Value range: [0,4294967295]\n        :type DUdpMbpsLimit: int\n        :param DIcmpMbpsLimit: ICMP speed limit. Value range: [0,4294967295]\n        :type DIcmpMbpsLimit: int\n        :param DOtherMbpsLimit: Other protocol speed limit. Value range: [0,4294967295]\n        :type DOtherMbpsLimit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPacketFilter(AbstractModel):
    """Packet filter in advanced DDoS policy

    """

    def __init__(self):
        """
        :param Protocol: Protocol. Valid values: [tcp, udp, icmp, all]\n        :type Protocol: str\n        :param SportStart: Start source port. Value range: [0,65535]\n        :type SportStart: int\n        :param SportEnd: End source port. Value range: [0,65535]\n        :type SportEnd: int\n        :param DportStart: Start destination port. Value range: [0,65535]\n        :type DportStart: int\n        :param DportEnd: End destination port. Value range: [0,65535]\n        :type DportEnd: int\n        :param PktlenMin: Minimum packet length. Value range: [0,1500]\n        :type PktlenMin: int\n        :param PktlenMax: Maximum packet length. Value range: [0,1500]\n        :type PktlenMax: int\n        :param MatchBegin: Whether to detect the payload. Valid values: [
begin_l3 (IP header)
begin_l4 (TCP header)
begin_l5 (payload)
no_match (no check)
]\n        :type MatchBegin: str\n        :param MatchType: Whether it is a regular expression. Valid values: [sunday (keyword), pcre (regular expression)]\n        :type MatchType: str\n        :param Str: Keyword or regular expression\n        :type Str: str\n        :param Depth: Detection depth. Value range: [0,1500]\n        :type Depth: int\n        :param Offset: Detection offset. Value range: [0,1500]\n        :type Offset: int\n        :param IsNot: Whether to include. Valid values: [0 (no), 1 (yes)]\n        :type IsNot: int\n        :param Action: Policy action. Valid values: [drop, drop_black, drop_rst, drop_black_rst, transmit]\n        :type Action: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPortLimit(AbstractModel):
    """Disabled port in advanced DDoS policy

    """

    def __init__(self):
        """
        :param Protocol: Protocol. Valid values: [tcp, udp, all]\n        :type Protocol: str\n        :param DPortStart: Start destination port. Value range: [0,65535]\n        :type DPortStart: int\n        :param DPortEnd: End destination port, which must be greater than or equal to the start destination port. Value range: [0,65535]\n        :type DPortEnd: int\n        :param SPortStart: Start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SPortStart: int\n        :param SPortEnd: End source port, which must be greater than or equal to the start source port. Value range: [0,65535]
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SPortEnd: int\n        :param Action: Action to be executed. Valid values: [drop (discard) , transmit (forward)]
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Action: str\n        :param Kind: Type of port to be disabled. Valid values: [0 (destination port range), 1 (source port range), 2 (destination port range and source port range)]
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Kind: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosPolicy(AbstractModel):
    """Advanced DDoS policy

    """

    def __init__(self):
        """
        :param Resources: Resource bound to policy\n        :type Resources: list of ResourceIp\n        :param DropOptions: Disabled protocol\n        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`\n        :param PortLimits: Disabled port\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param PacketFilters: Packet filter\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param IpBlackWhiteLists: IP blocklist/allowlist\n        :type IpBlackWhiteLists: list of IpBlackWhite\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param PolicyName: Policy name\n        :type PolicyName: str\n        :param CreateTime: Policy creation time\n        :type CreateTime: str\n        :param WaterPrint: Watermarking policy parameter. There can be only one policy. If there are no policies, the array is empty\n        :type WaterPrint: list of WaterPrintPolicy\n        :param WaterKey: Watermark key. There can be up to two keys. If there are no policies, the array is empty\n        :type WaterKey: list of WaterPrintKey\n        :param BoundResources: Resource instance bound to policy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BoundResources: list of str\n        :param SceneId: Policy scenario
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SceneId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param CCFrequencyRuleId: Access frequency control rule ID for CC protection\n        :type CCFrequencyRuleId: str\n        """
        self.Business = None
        self.CCFrequencyRuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param SetId: Policy ID\n        :type SetId: str\n        """
        self.Business = None
        self.Id = None
        self.SetId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param SceneId: Policy scenario ID\n        :type SceneId: str\n        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        """
        self.Business = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID list\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID list\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Filter: Search value, which can only be resource ID or user `UIN`\n        :type Filter: str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records\n        :type TotalCount: int\n        :param Data: Record array\n        :type Data: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt response structure.

    """

    def __init__(self):
        """
        :param Count: Maximum number of layer-7 rules that can be added for Anti-DDoS Advanced\n        :type Count: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param MetricName: Metric name. Valid values:
connum: number of active TCP connections;
new_conn: number of new TCP connections;
inactive_conn: number of inactive connections;
intraffic: inbound traffic;
outtraffic: outbound traffic;
alltraffic: sum of inbound and outbound traffic;
inpkg: inbound packet rate;
outpkg: outbound packet rate;\n        :type MetricName: str\n        :param Period: Statistical time granularity in seconds (300: 5-minute, 3600: hourly, 86400: daily)\n        :type Period: int\n        :param StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5\n        :type StartTime: str\n        :param EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5\n        :type EndTime: str\n        :param Statistics: Statistical method. Valid values:
max: maximum value;
min: minimum value;
avg: average;\n        :type Statistics: str\n        :param ProtocolPort: Protocol port array\n        :type ProtocolPort: list of ProtocolPort\n        :param Ip: Resource instance IP, which is required only if `Business` is `net` (Anti-DDoS Ultimate), because an Anti-DDoS Ultimate instance has multiple IPs;\n        :type Ip: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData response structure.

    """

    def __init__(self):
        """
        :param DataList: Returned metric value\n        :type DataList: list of BaradData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BasicIp: Queried IP address, such as 1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk\n        :type BasicRegion: str\n        :param BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).\n        :type BasicBizType: str\n        :param BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).\n        :type BasicDeviceType: str\n        :param BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)\n        :type BasicIpInstance: str\n        :param BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)\n        :type BasicIspCode: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold response structure.

    """

    def __init__(self):
        """
        :param CCEnable: CC status (0: disabled, 1: enabled)\n        :type CCEnable: int\n        :param CCThreshold: CC protection threshold\n        :type CCThreshold: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BasicIp: Queried IP address, such as 1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: IP region. Valid values: region abbreviations such as gz, bj, sh, and hk\n        :type BasicRegion: str\n        :param BasicBizType: Zone type. Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).\n        :type BasicBizType: str\n        :param BasicDeviceType: Device type. Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).\n        :type BasicDeviceType: str\n        :param BasicCheckFlag: Validity check. Valid value: 1\n        :type BasicCheckFlag: int\n        :param BasicIpInstance: IPInstance Nat gateway, which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)\n        :type BasicIpInstance: str\n        :param BasicIspCode: ISP line, which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)\n        :type BasicIspCode: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold response structure.

    """

    def __init__(self):
        """
        :param Threshold: Blackhole blocking value\n        :type Threshold: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)\n        :type Business: str\n        :param Id: Resource ID\n        :type Id: str\n        :param Period: Statistical period in seconds. Valid values: 300, 1800, 3600, 21600, and 86400.\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Statistics: Statistical mode, which only supports sum.\n        :type Statistics: str\n        :param ProtoInfo: Protocol and port list, which is valid when the statistical dimension is the number of connections. Valid protocols: TCP, UDP, HTTP, and HTTPS.\n        :type ProtoInfo: list of ProtocolPort\n        :param Domain: Specific domain name query\n        :type Domain: str\n        """
        self.Business = None
        self.Id = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.ProtoInfo = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        if params.get("ProtoInfo") is not None:
            self.ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtoInfo.append(obj)
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizHttpStatusResponse(AbstractModel):
    """DescribeBizHttpStatus response structure.

    """

    def __init__(self):
        """
        :param HttpStatusMap: Statistics on the HTTP status codes of business traffic\n        :type HttpStatusMap: :class:`tencentcloud.dayu.v20180709.models.HttpStatusMap`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.HttpStatusMap = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HttpStatusMap") is not None:
            self.HttpStatusMap = HttpStatusMap()
            self.HttpStatusMap._deserialize(params.get("HttpStatusMap"))
        self.RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RsId: Anti-DDoS instance ID\n        :type RsId: str\n        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param CCAlarmThreshold: CC alarm threshold\n        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param IpList: Resource instance IP. When `business` is not `basic`, if `IpList` is not empty, `Id` must not be empty;\n        :type IpList: list of str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `shield`: Chess Shield; `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param IpList: Instance IP list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpList: list of str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Data: CC attack event list\n        :type Data: list of CCEventRecord\n        :param Total: Total number of records\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API). If a value is entered, it means to get the access frequency control rule of the forwarding rule;\n        :type RuleId: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param CCFrequencyRuleList: Access frequency control rule list\n        :type CCFrequencyRuleList: list of CCFrequencyRule\n        :param CCFrequencyRuleStatus: Access frequency control rule status. Valid values: [on, off];\n        :type CCFrequencyRuleStatus: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Type: Blocklist or allowlist. Valid values: [white (allowlist), black (blocklist)]
Note: this array can only have one value. It cannot get the blocklist and allowlist at the same time\n        :type Type: list of str\n        :param Limit: Pagination parameter\n        :type Limit: int\n        :param Offset: Pagination parameter\n        :type Offset: int\n        :param Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];\n        :type Protocol: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny response structure.

    """

    def __init__(self):
        """
        :param Data: This field has been replaced by `RecordList` and should not be used\n        :type Data: list of KeyValue\n        :param Total: Number of records\n        :type Total: int\n        :param RecordList: Returned Blocklist/allowlist record,
If "Key":"ip", "Value": IP;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection protocol (HTTP or HTTPS);\n        :type RecordList: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro, `bgp-multip`: Anti-DDoS Pro (multi-IP)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Limit: Number of entries pulled\n        :type Limit: int\n        :param Offset: Offset\n        :type Offset: int\n        """
        self.Business = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of custom rules\n        :type Total: int\n        :param Policys: Policy list\n        :type Policys: list of CCPolicy\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)\n        :type Id: str\n        :param Domain: (Optional) Domain name\n        :type Domain: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param MetricName: Metric. Valid values: [inqps (total requests peak), dropqps (attack requests peak)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Data: Value array\n        :type Data: list of int non-negative\n        :param Count: Number of values\n        :type Count: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Type: Blocklist or allowlist. Valid value: [white (allowlist)]. Currently, only allowlist is supported.
Note: this array can only have one value which can only be `white`\n        :type Type: list of str\n        :param Limit: Pagination parameter\n        :type Limit: int\n        :param Offset: Pagination parameter\n        :type Offset: int\n        :param Protocol: HTTP or HTTPS CC protection, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)];\n        :type Protocol: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow response structure.

    """

    def __init__(self):
        """
        :param Data: This field has been replaced by `RecordList` and should not be used\n        :type Data: list of KeyValue\n        :param Total: Total number of records\n        :type Total: int\n        :param RecordList: Returned Blocklist/allowlist record,
If "Key":"url", "Value": URL;
If "Key":"domain", "Value": domain name.
If "Key":"type", "Value" can be `white` (allowlist) or `black` (blocklist).
If "Key":"protocol", "Value": CC protection type (HTTP protection or HTTPS domain name protection);\n        :type RecordList: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RsId: Anti-DDoS instance ID\n        :type RsId: str\n        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param DDoSAlarmThreshold: DDoS alarm threshold\n        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time. Maximum statistics time range: half a year;\n        :type EndTime: str\n        :param IpList: IP attack source of specified resource, which is optional\n        :type IpList: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap response structure.

    """

    def __init__(self):
        """
        :param NationCount: Global region distribution data\n        :type NationCount: list of KeyValueRecord\n        :param ProvinceCount: Chinese province distribution data\n        :type ProvinceCount: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        :param IpList: IP attack source of specified resource, which is optional\n        :type IpList: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of attack sources\n        :type Total: int\n        :param AttackSourceList: Attack source list\n        :type AttackSourceList: list of DDoSAttackSourceRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]\n        :type MetricName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]\n        :type MetricName: str\n        :param Data: `Key-Value` array. Valid values of `Key`:
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
The value of `key` indicates the attack event type. When the `key` is `UNKNOWNFLOOD`, it indicates  unknown attack events.\n        :type Data: list of KeyValue\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Instance ID, which is required only if `Business` is not `basic`.\n        :type Id: str\n        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;\n        :type Ip: str\n        :param BizType: Type of products bound to the anti-DDoS instance, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (Bare metal products), eni (elastic network interface), vpngw (VPN Gateway), natgw (NAT Gateway), waf (Web Application Firewall), fpc (Finance products), gaap (GAAP), other (hosted IP)]\n        :type BizType: str\n        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]\n        :type DeviceType: str\n        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;\n        :type InstanceId: str\n        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
"nj":     Nanjing\n        :type IPRegion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus response structure.

    """

    def __init__(self):
        """
        :param DefendStatus: Protection status. 0: disabled, 1: enabled
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DefendStatus: int\n        :param UndefendExpire: Expiration time of temporary protection disablement. This field is empty if the protection is in enabled status;
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UndefendExpire: str\n        :param ShowFlag: Console feature display field. 1: displays console features, 0: hides console features
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ShowFlag: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param TcpPacketSum: Number of TCP attack packets\n        :type TcpPacketSum: int\n        :param TcpKBSum: Traffic of TCP attacks in KB\n        :type TcpKBSum: int\n        :param UdpPacketSum: Number of UDP attack packets\n        :type UdpPacketSum: int\n        :param UdpKBSum: Traffic of UDP attacks in KB\n        :type UdpKBSum: int\n        :param IcmpPacketSum: Number of ICMP attack packets\n        :type IcmpPacketSum: int\n        :param IcmpKBSum: Traffic of ICMP attacks in KB\n        :type IcmpKBSum: int\n        :param OtherPacketSum: Number of other attack packets\n        :type OtherPacketSum: int\n        :param OtherKBSum: Traffic of other attacks in KB\n        :type OtherKBSum: int\n        :param TotalTraffic: Total attack traffic in KB\n        :type TotalTraffic: int\n        :param Mbps: Attack traffic bandwidth peak\n        :type Mbps: int\n        :param Pps: Attack packet rate peak\n        :type Pps: int\n        :param PcapUrl: PCAP file download link\n        :type PcapUrl: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)\n        :type Id: str\n        :param IpList: Resource IP\n        :type IpList: list of str\n        :param OverLoad: Whether the elastic protection bandwidth is exceeded. Valid values: [yes, no]. If an empty string is entered, it means no filtering\n        :type OverLoad: str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param IpList: Resource IP
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpList: list of str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Data: DDoS attack event list\n        :type Data: list of DDoSEventRecord\n        :param Total: Total number of records\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content\n        :type Data: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]\n        :type MetricName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param MetricName: Metric. Valid values: [traffic (attack protocol traffic in KB), pkg (number of attack protocol packets), classnum (number of attack events)]\n        :type MetricName: str\n        :param Data: `Key-Value` array. Valid values of `Key`:
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
The value of `key` indicates the attack event type. When the `key` is `UNKNOWNFLOOD`, it indicates  unknown attack events.\n        :type Data: list of KeyValue\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param TcpPacketSum: Number of TCP attack packets\n        :type TcpPacketSum: int\n        :param TcpKBSum: Traffic of TCP attacks in KB\n        :type TcpKBSum: int\n        :param UdpPacketSum: Number of UDP attack packets\n        :type UdpPacketSum: int\n        :param UdpKBSum: Traffic of UDP attacks in KB\n        :type UdpKBSum: int\n        :param IcmpPacketSum: Number of ICMP attack packets\n        :type IcmpPacketSum: int\n        :param IcmpKBSum: Traffic of ICMP attacks in KB\n        :type IcmpKBSum: int\n        :param OtherPacketSum: Number of other attack packets\n        :type OtherPacketSum: int\n        :param OtherKBSum: Traffic of other attacks in KB\n        :type OtherKBSum: int\n        :param TotalTraffic: Total attack traffic in KB\n        :type TotalTraffic: int\n        :param Mbps: Attack traffic bandwidth peak\n        :type Mbps: int\n        :param Pps: Attack packet rate peak\n        :type Pps: int\n        :param PcapUrl: PCAP file download link\n        :type PcapUrl: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Data: DDoS attack event list\n        :type Data: list of DDoSEventRecord\n        :param Total: Total number of records\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Attack start time\n        :type StartTime: str\n        :param EndTime: Attack end time\n        :type EndTime: str\n        :param Data: IP attack log, which is a `KeyValue` array. Valid values of `Key-Value`:
If `Key` is `LogTime`, `Value` indicates the IP log time
If `Key` is `LogMessage`, `Value` indicates the IP log content\n        :type Data: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Data: Value array\n        :type Data: list of int non-negative\n        :param Count: Number of values\n        :type Count: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Resource ID, which is optional. If a value is entered, it indicates the advanced DDoS policy bound to the resource\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
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
        """
        :param DDosPolicyList: Advanced DDoS policy list\n        :type DDosPolicyList: list of DDosPolicy\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Ip: Anti-DDoS instance IP\n        :type Ip: str\n        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Id: Resource instance ID. If `Business` is `basic`, this field is not required (because Anti-DDoS Basic has no resource instance)\n        :type Id: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend response structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Id: Anti-DDoS instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Id: str\n        :param Ip: Resource IP\n        :type Ip: str\n        :param MetricName: Metric. Valid values: [bps (attack traffic bandwidth), pps (attack packet rate)]\n        :type MetricName: str\n        :param Period: Statistical granularity. Valid values: [300 (5-minute), 3600 (hourly), 86400 (daily)]\n        :type Period: int\n        :param StartTime: Statistics start time\n        :type StartTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param Data: Value array. The unit for attack traffic bandwidth is Mbps, and that for the packet rate is pps.\n        :type Data: list of int non-negative\n        :param Count: Number of values\n        :type Count: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)\n        :type Business: str\n        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis response structure.

    """

    def __init__(self):
        """
        :param Data: Field value as follows:
Days: number of days of Anti-DDoS resource use
Attacks: number of DDoS attacks\n        :type Data: list of KeyValue\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)\n        :type Business: str\n        :param IpList: IP list\n        :type IpList: list of str\n        """
        self.Business = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo response structure.

    """

    def __init__(self):
        """
        :param Data: Tencent Cloud product information list. If nothing is found, an empty array will be returned. Valid values:
If `Key` is ProductName, `value` indicates the name of a Tencent Cloud product instance;
If `Key` is `ProductInstanceId`, `value` indicates the ID of a Tencent Cloud product instance;
If `Key` is `ProductType`, `value` indicates the Tencent Cloud product type (cvm: CVM, clb: CLB);
If `Key` is `IP`, `value` indicates the IP of a Tencent Cloud product instance;\n        :type Data: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param IdList: Guarantee package ID, which is optional. If you need to get the guarantee package with a specified ID (such as insure-000000xe), please use this field\n        :type IdList: list of str\n        """
        self.IdList = None


    def _deserialize(self, params):
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks response structure.

    """

    def __init__(self):
        """
        :param InsurePacks: Guarantee package list\n        :type InsurePacks: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param List: Blocked IP list\n        :type List: list of IpBlockData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BeginTime: Start time\n        :type BeginTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Ip: IP (if this field is not empty, IP filtering will be performed)\n        :type Ip: str\n        :param Paging: Pagination parameter (paginated query will be performed if this field is not empty). This field will be disused in the future. Please use the `Limit` and `Offset` fields instead;\n        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList response structure.

    """

    def __init__(self):
        """
        :param BeginTime: Start time\n        :type BeginTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param List: IP unblocking record\n        :type List: list of IpUnBlockData\n        :param Total: Total number of records\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig response structure.

    """

    def __init__(self):
        """
        :param HealthConfig: Layer-4 health check configuration array\n        :type HealthConfig: list of L4HealthConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of exceptional rules\n        :type Total: int\n        :param ErrHealths: Exceptional rule list. Returned value description: `Key` is the rule ID, while `Value` is the exceptional IP. Multiple IPs are separated by ","\n        :type ErrHealths: list of KeyValue\n        :param ExtErrHealths: Exceptional rule list (which provides more error-related information). Returned value description:
If `key` is `RuleId`, `Value` indicates the rule ID;
If `key` is `Protocol`, `Value` indicates the forwarding protocol of a rule;
If `key` is `VirtualPort`, `Value` indicates the forwarding port of a rule;
If `Key` is `ErrMessage`, `Value` indicates the exception message for health check;
Exception message for health check in the format of `"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6"`. Multiple error messages for the source IP should be separated by `,`,
SourceIp: real server IP, SourcePort: real server port, AbnormalStatTime: exception time, AbnormalReason: cause of exception, Interval: check frequency, CheckNum: number of checks, FailNum: number of failures;\n        :type ExtErrHealths: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID array. To export the health check configurations of all rules, leave this field empty or enter an empty array;\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig response structure.

    """

    def __init__(self):
        """
        :param HealthConfig: Layer-7 health check configuration array\n        :type HealthConfig: list of L7HealthConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
IsolatePackCount: number of isolated resources\n        :type Data: list of KeyValue\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param StartTime: Attack event start time in the format of "2018-08-28 07:00:00"\n        :type StartTime: str\n        :param EndTime: Attack event end time in the format of "2018-08-28 07:02:00"\n        :type EndTime: str\n        :param Ip: Resource IP, which is required only if `Business` is `net`;\n        :type Ip: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePcapResponse(AbstractModel):
    """DescribePcap response structure.

    """

    def __init__(self):
        """
        :param PcapUrlList: PCAP packet download link list, which is an empty array if there are no PCAP packets;\n        :type PcapUrlList: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param SceneId: Policy scenario ID\n        :type SceneId: str\n        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase response structure.

    """

    def __init__(self):
        """
        :param CaseList: Policy scenario list\n        :type CaseList: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param IdList: Resource ID. If this field is left empty, it means to get all resources IP of the current user\n        :type IdList: list of str\n        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList response structure.

    """

    def __init__(self):
        """
        :param Resource: Resource IP list\n        :type Resource: list of ResourceIp\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RegionList: Region code search, which is optional. If no regions are to be specified, enter an empty array. If a region is to be specified, enter a region code, such as ["gz", "sh"]\n        :type RegionList: list of str\n        :param Line: Line search. This field can be optionally entered only when getting the list of Anti-DDoS Advanced resources. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. Please enter an empty array when getting other products;\n        :type Line: list of int non-negative\n        :param IdList: Resource ID search, which is optional. If this field is not an empty array, it means to get the resource list of a specified resource;\n        :type IdList: list of str\n        :param Name: Resource name search, which is optional. If this field is not an empty string, it means to search for resources by name;\n        :type Name: str\n        :param IpList: IP query list, which is optional. Resources will be queried by IP if the list is not empty.\n        :type IpList: list of str\n        :param Status: Resource status search list, which is optional. Valid values: [0 (running), 1 (cleansing), 2 (blocking)]. No status search will be performed if an empty array is entered;\n        :type Status: list of int non-negative\n        :param Expire: Expiring resource search, which is optional. Valid values: [0 (no search), 1 (search for expiring resources)]\n        :type Expire: int\n        :param OderBy: Sort by field, which is optional\n        :type OderBy: list of OrderBy\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        :param CName: CNAME of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;\n        :type CName: str\n        :param Domain: Domain name of Anti-DDoS Ultimate resource, which is optional and only valid for the Anti-DDoS Ultimate resource list;\n        :type Domain: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of records\n        :type Total: int\n        :param ServicePacks: Resource record list. The description of key values is as follows:
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
"Key": "ServiceBandwidth" (Base business application bandwidth of the Anti-DDoS Ultimate instance)\n        :type ServicePacks: list of KeyValueRecord\n        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param IdList: Resource ID list\n        :type IdList: list of str\n        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets response structure.

    """

    def __init__(self):
        """
        :param L4RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules\n        :type L4RuleSets: list of KeyValueRecord\n        :param L7RuleSets: Rule record array. Valid values:
If `Key` is "Id", `Value` indicates the resource ID
If `Key` is "RuleIdList", `Value` indicates the resource rule ID. Multiple rule IDs are separated by ","
If `Key` is "RuleNameList", `Value` indicates the resource rule name. Multiple rule names are separated by ","
If `Key` is "RuleNum", `Value` indicates the number of resource rules\n        :type L7RuleSets: list of KeyValueRecord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Limit: Number of items in a page. Returned results are not paged if you enter '0'.\n        :type Limit: int\n        :param Offset: Starting offset of the page. Value: (number of pages - 1) * items per page\n        :type Offset: int\n        :param Domain: (Optional) Filter by specific domain name\n        :type Domain: str\n        """
        self.Limit = None
        self.Offset = None
        self.Domain = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of scheduling domain names\n        :type Total: int\n        :param DomainList: List of scheduling domain names\n        :type DomainList: list of SchedulingDomain\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
IpNum: IP statistics\n        :type Data: list of KeyValue\n        :param BeginDate: Start time of the current month\n        :type BeginDate: str\n        :param EndDate: End time of the current month\n        :type EndDate: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment response structure.

    """

    def __init__(self):
        """
        :param Data: Intermediate IP range. Multiple values are separated by ";"\n        :type Data: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param MetricName: Metric name. Valid values:
traffic: traffic bandwidth;
pkg: packet rate;\n        :type MetricName: str\n        :param Period: Statistical time granularity (300: 5-minute, 3600: hourly, 86400: daily)\n        :type Period: int\n        :param StartTime: Statistics start time. The second part is kept at 0, and the minute part is a multiple of 5\n        :type StartTime: str\n        :param EndTime: Statistics end time. The second part is kept at 0, and the minute part is a multiple of 5\n        :type EndTime: str\n        :param IpList: Resource IP, which is required and only supports one IP if `Business` is `bgp-multip`. If this field is left empty, all IPs of a resource instance will be counted by default. If the resource instance has multiple IPs (such as Anti-DDoS Ultimate), the statistical method is summation;\n        :type IpList: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis response structure.

    """

    def __init__(self):
        """
        :param InDataList: If `MetricName` is `traffic`, this field indicates the inbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the inbound packet rate in pps;\n        :type InDataList: list of float\n        :param OutDataList: If `MetricName` is `traffic`, this field indicates the outbound traffic bandwidth in bps;
If `MetricName` is `pkg`, this field indicates the outbound packet rate in pps;\n        :type OutDataList: list of float\n        :param MetricName: Metric name:
traffic: traffic bandwidth;
pkg: packet rate;\n        :type MetricName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Total: Total number of unblocking chances\n        :type Total: int\n        :param Used: Number of used chances\n        :type Used: int\n        :param BeginTime: Statistics start time\n        :type BeginTime: str\n        :param EndTime: Statistics end time\n        :type EndTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained\n        :type RuleIdList: list of str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules response structure.

    """

    def __init__(self):
        """
        :param Rules: Forwarding rule list\n        :type Rules: list of L4RuleEntry\n        :param Total: Total number of rules\n        :type Total: int\n        :param Healths: Health check configuration list\n        :type Healths: list of L4RuleHealth\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleIdList: Rule ID, which is optional. If this field is entered, the specified rule will be obtained\n        :type RuleIdList: list of str\n        :param Limit: Number of entries per page. A value of 0 means no pagination\n        :type Limit: int\n        :param Offset: Page start offset, whose value is (page number - 1) * number of entries per page\n        :type Offset: int\n        :param Domain: Domain name search, which is optional. Enter it if you need to search for domain names\n        :type Domain: str\n        :param ProtocolList: Forwarding protocol search, which is optional. Valid values: [http, https, http/https]\n        :type ProtocolList: list of str\n        :param StatusList: Status search, which is optional. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]\n        :type StatusList: list of int non-negative\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules response structure.

    """

    def __init__(self):
        """
        :param Rules: Forwarding rule list\n        :type Rules: list of L7RuleEntry\n        :param Total: Total number of rules\n        :type Total: int\n        :param Healths: Health check configuration list\n        :type Healths: list of L7RuleHealth\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP)\n        :type Business: str\n        :param LineList: Line search. Valid values: [1 (BGP line), 2 (Nanjing Telecom), 3 (Nanjing Unicom), 99 (third-party partner line)]. This field is valid only for Anti-DDoS Advanced and should be ignored for other product\n        :type LineList: list of int non-negative\n        """
        self.Business = None
        self.LineList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount response structure.

    """

    def __init__(self):
        """
        :param RegionList: Number of resource instances in region\n        :type RegionList: list of RegionInstanceCount\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class HttpStatusMap(AbstractModel):
    """Aggregated data on the HTTP status codes of business traffic

    """

    def __init__(self):
        """
        :param Http2xx: HTTP 2xx Status code\n        :type Http2xx: list of float\n        :param Http3xx: HTTP 3xx Status code\n        :type Http3xx: list of float\n        :param Http404: HTTP 404 Status code\n        :type Http404: list of float\n        :param Http4xx: HTTP 4xx Status code\n        :type Http4xx: list of float\n        :param Http5xx: HTTP 5xx Status code\n        :type Http5xx: list of float\n        :param SourceHttp2xx: HTTP 2xx Forwarding status code\n        :type SourceHttp2xx: list of float\n        :param SourceHttp3xx: HTTP 3xx Forwarding status code\n        :type SourceHttp3xx: list of float\n        :param SourceHttp404: HTTP 404 Forwarding status code\n        :type SourceHttp404: list of float\n        :param SourceHttp4xx: HTTP 4xx Forwarding status code\n        :type SourceHttp4xx: list of float\n        :param SourceHttp5xx: HTTP 5xx Forwarding status code\n        :type SourceHttp5xx: list of float\n        """
        self.Http2xx = None
        self.Http3xx = None
        self.Http404 = None
        self.Http4xx = None
        self.Http5xx = None
        self.SourceHttp2xx = None
        self.SourceHttp3xx = None
        self.SourceHttp404 = None
        self.SourceHttp4xx = None
        self.SourceHttp5xx = None


    def _deserialize(self, params):
        self.Http2xx = params.get("Http2xx")
        self.Http3xx = params.get("Http3xx")
        self.Http404 = params.get("Http404")
        self.Http4xx = params.get("Http4xx")
        self.Http5xx = params.get("Http5xx")
        self.SourceHttp2xx = params.get("SourceHttp2xx")
        self.SourceHttp3xx = params.get("SourceHttp3xx")
        self.SourceHttp404 = params.get("SourceHttp404")
        self.SourceHttp4xx = params.get("SourceHttp4xx")
        self.SourceHttp5xx = params.get("SourceHttp5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlackWhite(AbstractModel):
    """IP blocklist/allowlist

    """

    def __init__(self):
        """
        :param Ip: IP address\n        :type Ip: str\n        :param Type: Blocklist/allowlist type. Valid values: [black, white]\n        :type Type: str\n        """
        self.Ip = None
        self.Type = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """IP blocking record

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param Status: Status (Blocked: blocked, UnBlocking: unblocking, UnBlockFailed: unblocking failed)\n        :type Status: str\n        :param BlockTime: Blocked time\n        :type BlockTime: str\n        :param UnBlockTime: Unblocked time (estimated)\n        :type UnBlockTime: str\n        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)\n        :type ActionType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpUnBlockData(AbstractModel):
    """IP unblocking record

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param BlockTime: Blocked time\n        :type BlockTime: str\n        :param UnBlockTime: Unblocked time (actual)\n        :type UnBlockTime: str\n        :param ActionType: Type of the unblocking action (`user`: self-service unblocking, `auto`: automatic unblocking, `update`: unblocking by service upgrading, `bind`: unblocking by binding Anti-DDoS Pro instance)\n        :type ActionType: str\n        """
        self.Ip = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """Field value in K-V format

    """

    def __init__(self):
        """
        :param Key: Field name\n        :type Key: str\n        :param Value: Field value\n        :type Value: str\n        """
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
        


class KeyValueRecord(AbstractModel):
    """`KeyValue` record

    """

    def __init__(self):
        """
        :param Record: Key-Value array of a record\n        :type Record: list of KeyValue\n        """
        self.Record = None


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Record.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4HealthConfig(AbstractModel):
    """Layer-4 health check configuration

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [TCP, UDP]\n        :type Protocol: str\n        :param VirtualPort: Forwarding port\n        :type VirtualPort: int\n        :param Enable: 1: enabled, 0: disabled\n        :type Enable: int\n        :param TimeOut: Response timeout period in seconds\n        :type TimeOut: int\n        :param Interval: Detection interval in seconds\n        :type Interval: int\n        :param KickNum: Unhealthy threshold in times.\n        :type KickNum: int\n        :param AliveNum: Healthy threshold in times.\n        :type AliveNum: int\n        :param KeepTime: Session persistence duration in seconds\n        :type KeepTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleEntry(AbstractModel):
    """Layer-4 rule

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [TCP, UDP]\n        :type Protocol: str\n        :param VirtualPort: Forwarding port\n        :type VirtualPort: int\n        :param SourcePort: Real server port\n        :type SourcePort: int\n        :param SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]\n        :type SourceType: int\n        :param KeepTime: Session persistence duration in seconds\n        :type KeepTime: int\n        :param SourceList: Forward list\n        :type SourceList: list of L4RuleSource\n        :param LbType: Load balancing method. Valid values: [1 (weighted round robin), 2 (source IP hash)]\n        :type LbType: int\n        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)];\n        :type KeepEnable: int\n        :param RuleId: Rule ID\n        :type RuleId: str\n        :param RuleName: Rule description\n        :type RuleName: str\n        :param RemoveSwitch: Watermark removal status. Valid values: [0 (disabled), 1 (enabled)]\n        :type RemoveSwitch: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleHealth(AbstractModel):
    """Rule health check parameter

    """

    def __init__(self):
        """
        :param RuleId: Rule ID\n        :type RuleId: str\n        :param Enable: 1: enabled, 0: disabled\n        :type Enable: int\n        :param TimeOut: Response timeout period in seconds\n        :type TimeOut: int\n        :param Interval: Detection interval in seconds, which must be greater than the response timeout period\n        :type Interval: int\n        :param KickNum: Unhealthy threshold in times\n        :type KickNum: int\n        :param AliveNum: Healthy threshold in times.\n        :type AliveNum: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleSource(AbstractModel):
    """Layer-4 forwarding rule list

    """

    def __init__(self):
        """
        :param Source: Intermediate IP or domain name\n        :type Source: str\n        :param Weight: Weight value. Value range: [0,100]\n        :type Weight: int\n        """
        self.Source = None
        self.Weight = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7HealthConfig(AbstractModel):
    """Layer-7 health check configuration

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [http, https, http/https]\n        :type Protocol: str\n        :param Domain: Forwarding domain name\n        :type Domain: str\n        :param Enable: 1: enabled, 0: disabled\n        :type Enable: int\n        :param Interval: Detection interval in seconds\n        :type Interval: int\n        :param KickNum: Number of exceptions in times\n        :type KickNum: int\n        :param AliveNum: Number of health checks in times\n        :type AliveNum: int\n        :param Method: Health check detection method. Valid values: HEAD, GET. Default VALUE: HEAD\n        :type Method: str\n        :param StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up\n        :type StatusCode: int\n        :param Url: URL of checked directory. Default value: /\n        :type Url: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """Layer-7 rule

    """

    def __init__(self):
        """
        :param Protocol: Forwarding protocol. Valid values: [http, https]\n        :type Protocol: str\n        :param Domain: Forwarding domain name\n        :type Domain: str\n        :param SourceType: Forwarding method. Valid values: [1 (forwarding via domain name), 2 (forwarding via IP)]\n        :type SourceType: int\n        :param KeepTime: Session persistence duration in seconds\n        :type KeepTime: int\n        :param SourceList: Forward list\n        :type SourceList: list of L4RuleSource\n        :param LbType: Load balancing method. Valid value: [1 (weighted round robin)]\n        :type LbType: int\n        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]\n        :type KeepEnable: int\n        :param RuleId: Rule ID, which is optional when adding a new rule but required when modifying or deleting a rule;\n        :type RuleId: str\n        :param CertType: Certificate source, which is required if the forwarding protocol is HTTPS. Valid value: [2 (Tencent Cloud-hosted certificate)]. If the forwarding protocol is HTTP, 0 can be entered for this field\n        :type CertType: int\n        :param SSLId: If the certificate is a Tencent Cloud-hosted certificate, this field must be entered with the hosted certificate ID\n        :type SSLId: str\n        :param Cert: If the certificate is an external certificate, this field must be entered with the certificate content. (As external certificates are no longer supported, this field has been disused and does not need to be entered)\n        :type Cert: str\n        :param PrivateKey: If the certificate is an external certificate, this field must be entered with the certificate key. (As external certificates are no longer supported, this field has been disused and does not need to be entered)\n        :type PrivateKey: str\n        :param RuleName: Rule description\n        :type RuleName: str\n        :param Status: Rule status. Valid values: [0 (successfully configured rule), 1 (rule configuration taking effect), 2 (rule configuration failed), 3 (rule deletion taking effect), 5 (rule deletion failed), 6 (rule waiting for configuration), 7 (rule waiting for deletion), 8 (rule waiting for certificate configuration)]\n        :type Status: int\n        :param CCStatus: CC protection status. Valid values: [0 (disabled), 1 (enabled)]\n        :type CCStatus: int\n        :param CCEnable: HTTPS CC protection status. Valid values: [0 (disabled), 1 (enabled)]\n        :type CCEnable: int\n        :param CCThreshold: HTTPS CC protection threshold\n        :type CCThreshold: int\n        :param CCLevel: HTTPS CC protection level\n        :type CCLevel: str\n        :param HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.\n        :type HttpsToHttpEnable: int\n        :param VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VirtualPort: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """Layer-7 rule health check parameter

    """

    def __init__(self):
        """
        :param RuleId: Rule ID\n        :type RuleId: str\n        :param Enable: 1: enabled, 0: disabled\n        :type Enable: int\n        :param Interval: Detection interval in seconds\n        :type Interval: int\n        :param KickNum: Unhealthy threshold in times.\n        :type KickNum: int\n        :param AliveNum: Healthy threshold in times.\n        :type AliveNum: int\n        :param Method: HTTP request method. Valid values: [HEAD, GET]\n        :type Method: str\n        :param StatusCode: Healthy status code during health check. xx = 1, 2xx = 2, 3xx = 4, 4xx = 8, 5xx = 16. Multiple status code values are added up\n        :type StatusCode: int\n        :param Url: URL of checked directory. Default value: /\n        :type Url: str\n        :param Status: Configuration status. 0: normal, 1: configuring, 2: configuration failed\n        :type Status: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RsId: Anti-DDoS instance ID\n        :type RsId: str\n        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value). It is set to 1000 on the backend by default\n        :type AlarmThreshold: int\n        :param IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs\n        :type IpList: list of str\n        """
        self.Business = None
        self.RsId = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param CCFrequencyRuleId: CC access frequency control rule ID\n        :type CCFrequencyRuleId: str\n        :param Mode: Matching rule. Valid values: ["include" (prefix match), "equal" (exact match)]\n        :type Mode: str\n        :param Period: Reference period in seconds. Valid values: [10, 30, 60]\n        :type Period: int\n        :param ReqNumber: Number of access requests. Value range: [1-10000]\n        :type ReqNumber: int\n        :param Act: Action take. Valid values: ["alg" (CAPTCHA), "drop" (blocking)]\n        :type Act: str\n        :param ExeDuration: Execution duration in seconds. Valid range: [1-900]\n        :type ExeDuration: int\n        :param Uri: URI string, which must start with `/`, such as `/abc/a.php`. Length limit: 31. If URI is `/`, only prefix match can be selected as the matching mode;\n        :type Uri: str\n        :param UserAgent: `User-Agent` string. Length limit: 80\n        :type UserAgent: str\n        :param Cookie: Cookie string. Length limit: 40\n        :type Cookie: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleId: Layer-7 forwarding rule ID, which can be obtained through the `DescribleL7Rules` API\n        :type RuleId: str\n        :param Method: Enables or disable. Valid values: ["on", "off"]\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleId: Rule ID\n        :type RuleId: str\n        :param Method: Enables/disables CC domain name protection. Valid values: [open (enable), close (disable)]\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Method: add: add, delete: delete\n        :type Method: str\n        :param Type: Blocklist/allowlist type. Valid values: [white (allowlist), black (blocklist)]\n        :type Type: str\n        :param IpList: Blocklisted/whitelisted IP array\n        :type IpList: list of str\n        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;\n        :type Protocol: str\n        :param Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;\n        :type Domain: str\n        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API),
If `Method` is `delete`, this field can be left empty;\n        :type RuleId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Level: CC protection level. Valid values: [default (normal), loose (loose), strict (strict)];\n        :type Level: str\n        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;\n        :type Protocol: str\n        :param RuleId: Layer-7 forwarding rule ID (which can be obtained from the layer-7 forwarding rule API);\n        :type RuleId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param SetId: Policy ID\n        :type SetId: str\n        :param Switch: Status\n        :type Switch: int\n        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Switch = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param SetId: Policy ID\n        :type SetId: str\n        :param Policy: Details of the CC protection policy\n        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Threshold: CC protection threshold. Valid values: (0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
If `Business` is Anti-DDoS Advanced or Anti-DDoS Ultimate, its maximum CC protection threshold is subject to the base protection bandwidth in the following way:
  Base bandwidth: maximum CC protection threshold
  10:  20000,
  20:  40000,
  30:  70000,
  40:  100000,
  50:  150000,
  60:  200000,
  80:  250000,
  100: 300000,\n        :type Threshold: int\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `RuleId` field is required;\n        :type Protocol: str\n        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API);
Required if `Protocol` is `https`;\n        :type RuleId: str\n        :param BasicIp: Queried IP address (only provided by Anti-DDoS Basic), such as 1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: IP region (only provided for Anti-DDoS Basic). Valid values: region abbreviations such as gz, bj, sh, and hk\n        :type BasicRegion: str\n        :param BasicBizType: Zone type (only provided for Anti-DDoS Basic). Valid values: public (public cloud zone), bm (BM zone), nat (NAT server zone), channel (internet channel).\n        :type BasicBizType: str\n        :param BasicDeviceType: Device type (only provided for Anti-DDoS Basic). Valid values: cvm (CVM), clb (public CLB), lb (BM CLB), nat (NAT server), channel (internet channel).\n        :type BasicDeviceType: str\n        :param BasicIpInstance: IPInstance Nat gateway (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter is required, which can be obtained through the NAT resource query API)\n        :type BasicIpInstance: str\n        :param BasicIspCode: ISP line (only provided for Anti-DDoS Basic), which is optional. (If the device type to be queried is a NAT server, this parameter should be 5)\n        :type BasicIspCode: int\n        :param Domain: This optional field must be specified when HTTPS protocol is used.\n        :type Domain: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Method: add: add, delete: delete\n        :type Method: str\n        :param Type: Blocklist/allowlist type. Valid value: [white (allowlist)]\n        :type Type: str\n        :param UrlList: URL array. URL format:
http://domain name/cgi
https://domain name/cgi\n        :type UrlList: list of str\n        :param Protocol: CC protection type, which is optional. Valid values: [http (HTTP CC protection), https (HTTPS CC protection)]; if this field is left empty, HTTPS CC protection will be used by default; if `https` is entered, the `Domain` and `RuleId` fields are required;\n        :type Protocol: str\n        :param Domain: HTTPS layer-7 forwarding rule domain name (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only if `Protocol` is `https`;\n        :type Domain: str\n        :param RuleId: HTTPS layer-7 forwarding rule ID (which is optional and can be obtained from the layer-7 forwarding rule API). This field is required only when adding a rule and `Protocol` is `https`;
If `Method` is `delete`, this field can be left empty;\n        :type RuleId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Method: get (read AI protection status), set (modify AI protection status);\n        :type Method: str\n        :param DDoSAI: AI protection status, which is required if `Method` is `set`. Valid values: [on, off].\n        :type DDoSAI: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSAI = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus response structure.

    """

    def __init__(self):
        """
        :param DDoSAI: AI protection status. Valid values: [on, off]\n        :type DDoSAI: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`shield`: Chess Shield, `bgpip`: Anti-DDoS Advanced, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param RsId: Anti-DDoS instance ID\n        :type RsId: str\n        :param AlarmType: Alarm threshold type. 0: not set, 1: inbound traffic, 2: cleansed traffic\n        :type AlarmType: int\n        :param AlarmThreshold: Alarm threshold, which should be greater than 0 (currently scheduled value)\n        :type AlarmThreshold: int\n        :param IpList: List of IPs associated with resource. If no Anti-DDoS Pro instance is bound, pass in an empty array. For Anti-DDoS Ultimate, pass in multiple IPs\n        :type IpList: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Status: Protection status. Valid values: [0 (disabled), 1 (enabled)]\n        :type Status: int\n        :param Hour: Disablement duration in hours. Valid values: [0, 1, 2, 3, 4, 5, 6]. If `Status` is `0` (indicating to disable), `Hour` must be greater than 0;\n        :type Hour: int\n        :param Id: Resource ID, which is required if `Business` is not Anti-DDoS Basic;\n        :type Id: str\n        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;\n        :type Ip: str\n        :param BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]\n        :type BizType: str\n        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]\n        :type DeviceType: str\n        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;\n        :type InstanceId: str\n        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
"nj":     Nanjing\n        :type IPRegion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Method: get (read protection level), set (modify protection level);\n        :type Method: str\n        :param DDoSLevel: Protection level, which is required if `Method` is `set`. Valid values: [low,middle,high]\n        :type DDoSLevel: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSLevel = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel response structure.

    """

    def __init__(self):
        """
        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param DDoSLevel: Protection level. Valid values: [low,middle,high]\n        :type DDoSLevel: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param SceneId: Policy scenario ID\n        :type SceneId: str\n        :param PlatformTypes: Development platform. Valid values: [PC (PC client), MOBILE (mobile device), TV (TV), SERVER (server)]\n        :type PlatformTypes: list of str\n        :param AppType: Category. Valid values: [WEB (website), GAME (game), APP (application), OTHER (other)]\n        :type AppType: str\n        :param AppProtocols: Application protocol. Valid values: [tcp (TCP protocol), udp (UDP protocol), icmp (ICMP protocol), all (other protocols)]\n        :type AppProtocols: list of str\n        :param TcpSportStart: TCP start port. Value range: (0, 65535]\n        :type TcpSportStart: str\n        :param TcpSportEnd: TCP end port. Value range: (0, 65535). It must be greater than or equal to the TCP start port\n        :type TcpSportEnd: str\n        :param UdpSportStart: UDP start port. Value range: (0, 65535]\n        :type UdpSportStart: str\n        :param UdpSportEnd: End UDP business port. Value range: (0, 65535). It must be greater than or equal to the start UDP business port\n        :type UdpSportEnd: str\n        :param HasAbroad: Whether there are customers outside Mainland China. Valid values: [no, yes]\n        :type HasAbroad: str\n        :param HasInitiateTcp: Whether to actively initiate outbound TCP requests. Valid values: [no, yes]\n        :type HasInitiateTcp: str\n        :param HasInitiateUdp: Whether to actively initiate outbound UDP requests. Valid values: [no, yes]\n        :type HasInitiateUdp: str\n        :param PeerTcpPort: Port that actively initiates TCP requests. Value range: (0, 65535]\n        :type PeerTcpPort: str\n        :param PeerUdpPort: Port that actively initiates UDP requests. Value range: (0, 65535]\n        :type PeerUdpPort: str\n        :param TcpFootprint: Fixed feature code of TCP payload. String length limit: 512\n        :type TcpFootprint: str\n        :param UdpFootprint: Fixed feature code of UDP payload. String length limit: 512\n        :type UdpFootprint: str\n        :param WebApiUrl: Web business API URL\n        :type WebApiUrl: list of str\n        :param MinTcpPackageLen: Minimum length of TCP business packet. Value range: (0, 1500)\n        :type MinTcpPackageLen: str\n        :param MaxTcpPackageLen: Maximum length of TCP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of TCP business packet\n        :type MaxTcpPackageLen: str\n        :param MinUdpPackageLen: Minimum length of UDP business packet. Value range: (0, 1500)\n        :type MinUdpPackageLen: str\n        :param MaxUdpPackageLen: Maximum length of UDP business packet. Value range: (0, 1500). It must be greater than or equal to the minimum length of UDP business packet\n        :type MaxUdpPackageLen: str\n        :param HasVPN: Whether there are VPN businesses. Valid values: [no, yes]\n        :type HasVPN: str\n        :param TcpPortList: TCP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000\n        :type TcpPortList: str\n        :param UdpPortList: UDP business port list. Individual ports and port ranges are supported, which should be in string type, such as 80,443,700-800,53,1000-3000\n        :type UdpPortList: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param Name: Policy name\n        :type Name: str\n        """
        self.Business = None
        self.PolicyId = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param DropOptions: Protocol disablement, which must be entered, and the array length must be 1\n        :type DropOptions: list of DDoSPolicyDropOption\n        :param PortLimits: Port disablement. If no ports are to be disabled, enter an empty array\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param IpAllowDenys: IP blocklist/allowlist. Enter an empty array if there is no IP blocklist/allowlist\n        :type IpAllowDenys: list of IpBlackWhite\n        :param PacketFilters: Packet filter. Enter an empty array if there are no packets to filter\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param WaterPrint: Watermarking policy parameter. Enter an empty array if the watermarking feature is not enabled. At most one watermarking policy can be passed in (that is, the size of the array cannot exceed 1)\n        :type WaterPrint: list of WaterPrintPolicy\n        """
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
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `basic`: Anti-DDoS Basic\n        :type Business: str\n        :param Method: `get`: read DDoS protection status, `set`: modify DDoS protection status\n        :type Method: str\n        :param Ip: Anti-DDoS Basic IP, which is required only if `Business` is Anti-DDoS Basic;\n        :type Ip: str\n        :param BizType: Product type of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [public (CVM), bm (BM), eni (ENI), vpngw (VPN Gateway), natgw (NAT Gateway), waf (WAF), fpc (finance product), gaap (GAAP), other (hosted IP)]\n        :type BizType: str\n        :param DeviceType: Product subtype of IP, which is required only if `Business` is Anti-DDoS Basic. Valid values: [cvm (CVM), lb (CLB), eni (ENI), vpngw (VPN), natgw (NAT), waf (WAF), fpc (finance), gaap (GAAP), other (hosted IP), eip (BM EIP)]\n        :type DeviceType: str\n        :param InstanceId: Resource instance ID of IP, which is required only if `Business` is Anti-DDoS Basic. This field is required when binding a new IP. For example, if it is an ENI IP, enter `ID(eni-*)` of the ENI for `InstanceId`;\n        :type InstanceId: str\n        :param IPRegion: This field is required only if `Business` is Anti-DDoS Basic, indicating the IP region. Valid values:
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
"nj":     Nanjing\n        :type IPRegion: str\n        :param Status: Protection status value, which is optional. Valid values: [0 (disabled), 1 (enabled)]. If `Method` is `get`, this field can be left empty;\n        :type Status: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch response structure.

    """

    def __init__(self):
        """
        :param Status: Current protection status value. Valid values: [0 (disabled), 1 (enabled)]\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Threshold: DDoS cleansing threshold. Valid values: [0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
If the value is set to 0, the default value will be used;\n        :type Threshold: int\n        """
        self.Business = None
        self.Id = None
        self.Threshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param Method: Key operation. Valid values: [add (add), delete (delete), open (open), close (close), get (get key)]\n        :type Method: str\n        :param KeyId: Key ID, which can be left empty or 0 when adding a key but is required for other operations\n        :type KeyId: int\n        """
        self.Business = None
        self.PolicyId = None
        self.Method = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey response structure.

    """

    def __init__(self):
        """
        :param KeyList: Watermark key list\n        :type KeyList: list of WaterPrintKey\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Limit: Elastic protection threshold. Valid values: [0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]\n        :type Limit: int\n        """
        self.Business = None
        self.Id = None
        self.Limit = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Healths: Health check parameter array\n        :type Healths: list of L4RuleHealth\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param RuleId: Rule ID\n        :type RuleId: str\n        :param KeepEnable: Session persistence status. Valid values: [0 (disabled), 1 (enabled)]\n        :type KeepEnable: int\n        :param KeepTime: Session persistence duration in seconds\n        :type KeepTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Rule: Rule\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Rule: Rule\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`net`: Anti-DDoS Ultimate)\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param Status: Switch status. 0: disabled, 1: enabled\n        :type Status: int\n        :param Hour: Switch duration in hours. Valid values: [0,1,2,3,4,5,6;]. If `status` is 1, this field is required and must be greater than 0\n        :type Hour: int\n        """
        self.Business = None
        self.Id = None
        self.Status = None
        self.Hour = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules request structure.

    """

    def __init__(self):
        """
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).\n        :type Business: str\n        :param Id: Anti-DDoS instance ID.\n        :type Id: str\n        :param Rule: Domain name forwarding rule.\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.NewL7RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = NewL7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced).\n        :type Business: str\n        :param Id: Anti-DDoS instance ID.\n        :type Id: str\n        :param Rule: Forwarding rule.\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewL4RuleResponse(AbstractModel):
    """ModifyNewL4Rule response structure.

    """

    def __init__(self):
        """
        :param Success: Success code.\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (single IP); `bgp-multip`: Anti-DDoS Pro (multi-IP), `net`: Anti-DDoS Ultimate\n        :type Business: str\n        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param PolicyId: Policy ID\n        :type PolicyId: str\n        :param Method: bind: bind policy; unbind: unbind policy\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.PolicyId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced, `net`: Anti-DDoS Ultimate, `shield`: Chess Shield, `bgp`: Anti-DDoS Pro (single IP), `bgp-multip`: Anti-DDoS Pro (multi-IP), `insurance`: guarantee package, `staticpack`: non-BGP package\n        :type Business: str\n        :param Id: Resource ID\n        :type Id: str\n        :param RenewFlag: Auto-renewal flag (0: manual renewal, 1: auto-renewal, 2: no renewal upon expiration)\n        :type RenewFlag: int\n        """
        self.Business = None
        self.Id = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag response structure.

    """

    def __init__(self):
        """
        :param Success: Success code\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Protocol: Forwarding protocol. Valid values: `http` and `https`.\n        :type Protocol: str\n        :param Domain: Forwarding domain name.\n        :type Domain: str\n        :param SourceType: Forwarding method. Valid values: `1` (by domain name); `2` (by IP).\n        :type SourceType: int\n        :param KeepTime: Session persistence duration, in seconds.\n        :type KeepTime: int\n        :param SourceList: List of sources\n        :type SourceList: list of L4RuleSource\n        :param LbType: Load balancing method. Valid value: `1` (weighed polling).\n        :type LbType: int\n        :param KeepEnable: Whether session persistence is enabled. Valid values: `0` (disabled) and `1` (enabled).\n        :type KeepEnable: int\n        :param RuleId: Rule ID. This field is not required for adding a rule, but is required for modifying or deleting a rule.\n        :type RuleId: str\n        :param CertType: Certificate source. When the forwarding protocol is HTTPS, this field must be set to `2` (Tencent Cloud managed certificate), and for HTTP protocol, it can be set to `0`.\n        :type CertType: int\n        :param SSLId: When the certificate source is Tencent Cloud managed certificate, this field must be set to the ID of the managed certificate.\n        :type SSLId: str\n        :param Cert: [Disused] When the certificate is an external certificate, the certificate content should be provided here. \n        :type Cert: str\n        :param PrivateKey: [Disused] When the certificate is an external certificate, the certificate key should be provided here. \n        :type PrivateKey: str\n        :param RuleName: Rule description.\n        :type RuleName: str\n        :param Status: Rule status. Valid values: `0` (the rule was successfully configured), `1` (configuring the rule), `2` (rule configuration failed), `3` (deleting the rule), `5` (failed to delete rule), `6` (rule awaiting configuration), `7` (rule awaiting deletion), and `8` (rule awaiting certificate configuration).\n        :type Status: int\n        :param CCStatus: CC protection status. Valid values: `0` (disabled) and `1` (enabled).\n        :type CCStatus: int\n        :param CCEnable: CC protection status based on HTTPS. Valid values: `0` (disabled) and `1` (enabled).\n        :type CCEnable: int\n        :param CCThreshold: CC protection threshold based on HTTPS.\n        :type CCThreshold: int\n        :param CCLevel: CC protection level based on HTTPS.\n        :type CCLevel: str\n        :param Region: Region code.\n        :type Region: int\n        :param Id: Anti-DDoS instance ID.\n        :type Id: str\n        :param Ip: Anti-DDoS instance IP address.\n        :type Ip: str\n        :param ModifyTime: Modification time.\n        :type ModifyTime: str\n        :param HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). The default value is disabled.\n        :type HttpsToHttpEnable: int\n        :param VirtualPort: Access port number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VirtualPort: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    """Sort by field

    """

    def __init__(self):
        """
        :param Field: Sort by field name. Valid values: [
bandwidth (bandwidth),
overloadCount (number of times of exceeding peak value)
]\n        :type Field: str\n        :param Order: Sorting order. Valid values: [asc (ascending), desc (descending)]\n        :type Order: str\n        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """Pagination index

    """

    def __init__(self):
        """
        :param Offset: Starting position\n        :type Offset: int\n        :param Limit: Quantity\n        :type Limit: int\n        """
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
        


class ProtocolPort(AbstractModel):
    """Protocol and port parameters

    """

    def __init__(self):
        """
        :param Protocol: Protocol (TCP, UDP)\n        :type Protocol: str\n        :param Port: Port\n        :type Port: int\n        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstanceCount(AbstractModel):
    """Number of resource instances in region

    """

    def __init__(self):
        """
        :param Region: Region code\n        :type Region: str\n        :param RegionV3: Region code (new specification)\n        :type RegionV3: str\n        :param Count: Number of resource instances\n        :type Count: int\n        """
        self.Region = None
        self.RegionV3 = None
        self.Count = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionV3 = params.get("RegionV3")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIp(AbstractModel):
    """Resource IP array

    """

    def __init__(self):
        """
        :param Id: Anti-DDoS instance ID\n        :type Id: str\n        :param IpList: Resource IP array\n        :type IpList: list of str\n        """
        self.Id = None
        self.IpList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomain(AbstractModel):
    """Scheduling domain name information

    """

    def __init__(self):
        """
        :param Domain: Scheduling domain name\n        :type Domain: str\n        :param BGPIpList: List of BGP IPs\n        :type BGPIpList: list of str\n        :param CTCCIpList: List of CTCC IPs\n        :type CTCCIpList: list of str\n        :param CUCCIpList: List of CUCC IPs\n        :type CUCCIpList: list of str\n        :param CMCCIpList: List of CMCC IPs\n        :type CMCCIpList: list of str\n        :param OverseaIpList: List of IPs outside Mainland China\n        :type OverseaIpList: list of str\n        :param Method: Scheduling method. It only supports `priority` now.\n        :type Method: str\n        :param CreateTime: The creation time.\n        :type CreateTime: str\n        :param TTL: \n        :type TTL: int\n        :param Status: Status\n        :type Status: int\n        :param ModifyTime: Modification time\n        :type ModifyTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """Operation return code, which is only used to return success

    """

    def __init__(self):
        """
        :param Code: Success/error code\n        :type Code: str\n        :param Message: Description\n        :type Message: str\n        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """Watermark key

    """

    def __init__(self):
        """
        :param KeyId: Watermark key ID\n        :type KeyId: str\n        :param KeyContent: Watermark key value\n        :type KeyContent: str\n        :param KeyVersion: Watermark key version number\n        :type KeyVersion: str\n        :param OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]\n        :type OpenStatus: int\n        :param CreateTime: Key generation time\n        :type CreateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintPolicy(AbstractModel):
    """Watermarking policy parameter

    """

    def __init__(self):
        """
        :param TcpPortList: TCP port range, such as ["2000-3000","3500-4000"]\n        :type TcpPortList: list of str\n        :param UdpPortList: UDP port range, such as ["2000-3000","3500-4000"]\n        :type UdpPortList: list of str\n        :param Offset: Watermark offset. Value range: [0, 100)\n        :type Offset: int\n        :param RemoveSwitch: Whether to automatically remove. Valid values: [0 (no), 1 (yes)]\n        :type RemoveSwitch: int\n        :param OpenStatus: Whether it is enabled. Valid values: [0 (no), 1 (yes)]\n        :type OpenStatus: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        