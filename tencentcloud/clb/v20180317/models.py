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


class AssociateTargetGroupsRequest(AbstractModel):
    """AssociateTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param Associations: Association array
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """Rule associated with target group

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: ID of associated CLB instance
        :type LoadBalancerId: str
        :param ListenerId: ID of associated listener
        :type ListenerId: str
        :param LocationId: ID of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocationId: str
        :param Protocol: Protocol type of associated listener, such as HTTP or TCP
        :type Protocol: str
        :param Port: Port of associated listener
        :type Port: int
        :param Domain: Domain name of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Url: URL of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param ListenerName: Listener name
        :type ListenerName: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Protocol = None
        self.Port = None
        self.Domain = None
        self.Url = None
        self.LoadBalancerName = None
        self.ListenerName = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.ListenerName = params.get("ListenerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: `HTTPS:443` listener ID
        :type ListenerId: str
        :param Domains: The domain name to be redirected under the listener `HTTPS:443`. If it is left empty, all domain names under the listener `HTTPS:443` will be configured with redirects.
        :type Domains: list of str
        :param RewriteCodes: Redirection status code. Valid values: 301, 302, and 307.
        :type RewriteCodes: list of int
        :param TakeUrls: Whether the matched URL is carried in redirection.
        :type TakeUrls: list of bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domains = None
        self.RewriteCodes = None
        self.TakeUrls = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")
        self.RewriteCodes = params.get("RewriteCodes")
        self.TakeUrls = params.get("TakeUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """Details of a real server bound to a listener

    """

    def __init__(self):
        r"""
        :param Type: Real server type. Valid values: CVM, ENI.
        :type Type: str
        :param InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API
        :type InstanceId: str
        :param Port: Listening port of a real server
        :type Port: int
        :param Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param RegisteredTime: Bound time of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param EniId: Unique ENI ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        """
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicTargetGroupInfo(AbstractModel):
    """Basic information of a target group bound to a forwarding rule or a listener

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupName: Target group name
        :type TargetGroupName: str
        """
        self.TargetGroupId = None
        self.TargetGroupName = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Targets: Unbinding targets
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param FailListenerIdSet: IDs of the listeners failed to unbind
        :type FailListenerIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ModifyList: List of weights to be modified in batches
        :type ModifyList: list of RsWeightRule
        """
        self.LoadBalancerId = None
        self.ModifyList = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Targets: Binding target
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param FailListenerIdSet: IDs of the listeners failed to bind. If this is blank, all listeners are bound successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """Batch binding type

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID.
        :type ListenerId: str
        :param Port: The port to Bind
        :type Port: int
        :param InstanceId: CVM instance ID. The primary IP of the primary ENI will be bound.
        :type InstanceId: str
        :param EniIp: It is required for binding an IP. It supports an ENI IP or any other private IP. To bind an ENI IP, the ENI should be bound to a CVM instance before being bound to a CLB instance.
Note: either `InstanceId` or `EniIp` must be passed in, which is required for binding a dual-stack IPv6 CVM instance.
        :type EniIp: str
        :param Weight: Weight of the CVM instance. Value range: [0, 100]. If it is not specified for binding the instance, 10 will be used by default.
        :type Weight: int
        :param LocationId: Layer-7 rule ID.
        :type LocationId: str
        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None
        self.LocationId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        self.LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDetailItem(AbstractModel):
    """Binding details including listener name, protocol, url and vport

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: Specifies the ID of CLB to be bound
        :type LoadBalancerId: str
        :param ListenerId: Specifies the ID of listener to be bound
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Domain: Specifies the domain name to be bound
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        :param LocationId: Sets the bound rule.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LocationId: str
        :param ListenerName: Listener name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param Protocol: Listener protocol.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        :param Vport: Listener port.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vport: int
        :param Url: URL of the location.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Url: str
        :param UconfigId: Configuration ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UconfigId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.LocationId = None
        self.ListenerName = None
        self.Protocol = None
        self.Vport = None
        self.Url = None
        self.UconfigId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.LocationId = params.get("LocationId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Vport = params.get("Vport")
        self.Url = params.get("Url")
        self.UconfigId = params.get("UconfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockedIP(AbstractModel):
    """IP added to blocklist 12306

    """

    def __init__(self):
        r"""
        :param IP: Blacklisted IP
        :type IP: str
        :param CreateTime: Blacklisted time
        :type CreateTime: str
        :param ExpireTime: Expiration time
        :type ExpireTime: str
        """
        self.IP = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """Certificate ID and list of CLB instances associated with it

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID
        :type CertId: str
        :param LoadBalancers: List of CLB instances associated with certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancer
        """
        self.CertId = None
        self.LoadBalancers = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInput(AbstractModel):
    """Certificate information

    """

    def __init__(self):
        r"""
        :param SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)
        :type SSLMode: str
        :param CertId: ID of a server certificate. If you leave this parameter empty, you must upload the certificate, including CertContent, CertKey, and CertName.
        :type CertId: str
        :param CertCaId: ID of a client certificate. When the listener adopts mutual authentication (i.e., SSLMode = mutual), if you leave this parameter empty, you must upload the client certificate, including CertCaContent and CertCaName.
        :type CertCaId: str
        :param CertName: Name of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertName: str
        :param CertKey: Key of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertKey: str
        :param CertContent: Content of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertContent: str
        :param CertCaName: Name of the uploaded client CA certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.
        :type CertCaName: str
        :param CertCaContent: Content of the uploaded client certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.
        :type CertCaContent: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.CertName = None
        self.CertKey = None
        self.CertContent = None
        self.CertCaName = None
        self.CertCaContent = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.CertName = params.get("CertName")
        self.CertKey = params.get("CertKey")
        self.CertContent = params.get("CertContent")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateOutput(AbstractModel):
    """Certificate information

    """

    def __init__(self):
        r"""
        :param SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)
        :type SSLMode: str
        :param CertId: Server certificate ID.
        :type CertId: str
        :param CertCaId: Client certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertCaId: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalHealth(AbstractModel):
    """Real server health status of a classic CLB

    """

    def __init__(self):
        r"""
        :param IP: Private IP of a real server
        :type IP: str
        :param Port: Real server port
        :type Port: int
        :param ListenerPort: CLB listener port
        :type ListenerPort: int
        :param Protocol: Forwarding protocol
        :type Protocol: str
        :param HealthStatus: Health check result. Value range: 1 (healthy), 0 (unhealthy)
        :type HealthStatus: int
        """
        self.IP = None
        self.Port = None
        self.ListenerPort = None
        self.Protocol = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.ListenerPort = params.get("ListenerPort")
        self.Protocol = params.get("Protocol")
        self.HealthStatus = params.get("HealthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalListener(AbstractModel):
    """Classic CLB listener information

    """

    def __init__(self):
        r"""
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param ListenerPort: CLB listener port
        :type ListenerPort: int
        :param InstancePort: Backend forwarding port of a listener
        :type InstancePort: int
        :param ListenerName: Listener name
        :type ListenerName: str
        :param Protocol: Listener protocol type
        :type Protocol: str
        :param SessionExpire: Session persistence time
        :type SessionExpire: int
        :param HealthSwitch: Whether health check is enabled. 1: enabled; 0: disabled.
        :type HealthSwitch: int
        :param TimeOut: Response timeout period
        :type TimeOut: int
        :param IntervalTime: Check interval
        :type IntervalTime: int
        :param HealthNum: Health threshold
        :type HealthNum: int
        :param UnhealthNum: Unhealthy threshold
        :type UnhealthNum: int
        :param HttpHash: A request balancing method for HTTP and HTTPS listeners of a public network classic CLB. wrr means weighted round robin, while ip_hash means consistent hashing based on source IPs of access requests.
        :type HttpHash: str
        :param HttpCode: Health check return code for HTTP and HTTPS listeners of a public network classic CLB. For more information, see the explanation of the field in the listener creating API.
        :type HttpCode: int
        :param HttpCheckPath: Health check path for HTTP and HTTPS listeners of a public network classic CLB
        :type HttpCheckPath: str
        :param SSLMode: Authentication method for an HTTPS listener of a public network classic CLB
        :type SSLMode: str
        :param CertId: Server certificate ID for an HTTPS listener of a public network classic CLB
        :type CertId: str
        :param CertCaId: Client certificate ID for an HTTPS listener of a public network classic CLB
        :type CertCaId: str
        :param Status: Listener status. Value range: 0 (creating), 1 (running)
        :type Status: int
        """
        self.ListenerId = None
        self.ListenerPort = None
        self.InstancePort = None
        self.ListenerName = None
        self.Protocol = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpHash = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerPort = params.get("ListenerPort")
        self.InstancePort = params.get("InstancePort")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpHash = params.get("HttpHash")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalLoadBalancerInfo(AbstractModel):
    """CLB information

    """

    def __init__(self):
        r"""
        :param InstanceId: Real server ID
        :type InstanceId: str
        :param LoadBalancerIds: List of CLB instance IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        """
        self.InstanceId = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTarget(AbstractModel):
    """Real server information of a classic CLB

    """

    def __init__(self):
        r"""
        :param Type: Real server type. Value range: CVM, ENI (coming soon)
        :type Type: str
        :param InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API
        :type InstanceId: str
        :param Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param RunFlag: Real server status
1: failed; 2: running; 3: creating; 4: shut down; 5: returned; 6: returning; 7: restarting; 8: starting; 9: shutting down; 10: resetting password; 11: formatting; 12: making image; 13: setting bandwidth; 14: reinstalling system; 19: upgrading; 21: hot migrating
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunFlag: int
        """
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RunFlag = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RunFlag = params.get("RunFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTargetInfo(AbstractModel):
    """Backend information of a classic CLB

    """

    def __init__(self):
        r"""
        :param InstanceId: Real server ID
        :type InstanceId: str
        :param Weight: Weight. Value range: [0, 100]
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterItem(AbstractModel):
    """Dedicated cluster information

    """

    def __init__(self):
        r"""
        :param ClusterId: Unique cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param Zone: Cluster AZ, such as ap-guangzhou-1
Note: this field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigListItem(AbstractModel):
    """Configuration content

    """

    def __init__(self):
        r"""
        :param UconfigId: Configuration ID.
        :type UconfigId: str
        :param ConfigType: Configuration type.
        :type ConfigType: str
        :param ConfigName: Configuration name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ConfigName: str
        :param ConfigContent: Configuration content.
        :type ConfigContent: str
        :param CreateTimestamp: Creates configuration time.
        :type CreateTimestamp: str
        :param UpdateTimestamp: Modifies configuration time.
        :type UpdateTimestamp: str
        """
        self.UconfigId = None
        self.ConfigType = None
        self.ConfigName = None
        self.ConfigContent = None
        self.CreateTimestamp = None
        self.UpdateTimestamp = None


    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        self.ConfigType = params.get("ConfigType")
        self.ConfigName = params.get("ConfigName")
        self.ConfigContent = params.get("ConfigContent")
        self.CreateTimestamp = params.get("CreateTimestamp")
        self.UpdateTimestamp = params.get("UpdateTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetRequest(AbstractModel):
    """CreateClsLogSet request structure.

    """

    def __init__(self):
        r"""
        :param Period: Logset retention period in days; max value: 90
        :type Period: int
        :param LogsetName: Logset name, which must be unique among all CLS logsets; default value: clb_logset
        :type LogsetName: str
        :param LogsetType: Logset type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).
        :type LogsetType: str
        """
        self.Period = None
        self.LogsetName = None
        self.LogsetType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.LogsetName = params.get("LogsetName")
        self.LogsetType = params.get("LogsetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetResponse(AbstractModel):
    """CreateClsLogSet response structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID.
        :type LogsetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Ports: Specifies for which ports to create listeners. Each port corresponds to a new listener.
        :type Ports: list of int
        :param Protocol: Listener protocol: TCP, UDP, HTTP, HTTPS, or TCP_SSL (which is currently in beta test. If you want to use it, please submit a ticket for application).
        :type Protocol: str
        :param ListenerNames: List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.
        :type ListenerNames: list of str
        :param HealthCheck: Health check parameter, which is applicable only to TCP, UDP, and TCP_SSL listeners.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: Certificate information. This parameter is applicable only to TCP_SSL listeners and HTTPS listeners with the SNI feature not enabled.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param Scheduler: Forwarding method of a listener. Value range: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR. This parameter is applicable only to TCP/UDP/TCP_SSL listeners.
        :type Scheduler: str
        :param SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners
        :type SniSwitch: int
        :param TargetType: Target real server type. `NODE`: binding a general node; `TARGETGROUP`: binding a target group.
        :type TargetType: str
        :param SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.
        :type SessionType: str
        :param KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners. Valid values: 0 (disable; default value) and 1 (enable).
        :type KeepaliveEnable: int
        :param EndPort: This parameter is used to specify the end port and is required when creating a port range listener. Only one member can be passed in when inputting the `Ports` parameter, which is used to specify the start port. If you want to try the port range feature, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).
        :type EndPort: int
        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
        :type DeregisterTargetRst: bool
        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.Certificate = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SniSwitch = None
        self.TargetType = None
        self.SessionType = None
        self.KeepaliveEnable = None
        self.EndPort = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.TargetType = params.get("TargetType")
        self.SessionType = params.get("SessionType")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.EndPort = params.get("EndPort")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param ListenerIds: Array of unique IDs of the created listeners
        :type ListenerIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param Forward: CLB instance type. Valid value: 1 (generic CLB instance).
        :type Forward: int
        :param LoadBalancerName: CLB instance name, which takes effect only when only one instance is to be created in the request. It can consist 1 to 60 letters, digits, hyphens (-), or underscores (_).
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.
        :type LoadBalancerName: str
        :param VpcId: Network ID of the target CLB real server, such as `vpc-12345678`, which can be obtained through the [DescribeVpcEx](https://intl.cloud.tencent.com/document/product/215/1372?from_cn_redirect=1) API. If this parameter is not specified, it will default to `DefaultVPC`. This parameter is required for creating a CLB instance.
        :type VpcId: str
        :param SubnetId: A subnet ID must be specified when you purchase a private network CLB instance in a VPC, and the VIP of this instance will be generated in this subnet. This parameter is required for creating a CLB instance.
        :type SubnetId: str
        :param ProjectId: Project ID of the CLB instance, which can be obtained through the [DescribeProject](https://intl.cloud.tencent.com/document/product/378/4400?from_cn_redirect=1) API. If this parameter is not specified, it will default to the default project.
        :type ProjectId: int
        :param AddressIPVersion: IP version. Valid values: `IPV4` (default), `IPV6` (IPV6 NAT64 version) or `IPv6FullChain` (IPv6 version). This parameter is only for public network CLB instances.
        :type AddressIPVersion: str
        :param Number: Number of CLBs to be created. Default value: 1.
        :type Number: int
        :param MasterZoneId: Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1, which is applicable only to public network CLB.
Note: A primary AZ carries traffic, while a secondary AZ does not carry traffic by default and will be used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. The list of primary AZs in a specific region can be queried through the DescribeMasterZones API.
        :type MasterZoneId: str
        :param ZoneId: Specifies an AZ ID for creating a CLB instance, such as `ap-guangzhou-1`, which is applicable only to public network CLB instances.
        :type ZoneId: str
        :param InternetAccessible: CLB network billing mode. This parameter is applicable only to public network CLB instances.
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param VipIsp: This parameter is applicable only to public network CLB instances. Valid values: CMCC (China Mobile), CTCC (China Telecom), CUCC (China Unicom). If this parameter is not specified, BGP will be used by default. ISPs supported in a region can be queried with the `DescribeSingleIsp` API. If an ISP is specified, only bill-by-bandwidth-package (BANDWIDTH_PACKAGE) can be used as the network billing mode.
        :type VipIsp: str
        :param Tags: Tags a CLB instance when purchasing it.
        :type Tags: list of TagInfo
        :param Vip: Specifies a VIP for the CLB instance.
<ul><li>`VpcId` is optional for creating shared clusters of public network CLB instances. For IPv6 CLB instance type, `SubnetId` is required; for IPv4 and IPv6 NAT64 types, it can be left empty.</li>
<li>`VpcId` is optional for creating shared clusters of public network CLB instances. For IPv6 CLB instance type, `SubnetId` is required; for IPv4 and IPv6 NAT64 types, it can be left empty.
</li></ul>
        :type Vip: str
        :param BandwidthPackageId: Bandwidth package ID. If this parameter is specified, the network billing mode (`InternetAccessible.InternetChargeType`) will only support bill-by-bandwidth package (`BANDWIDTH_PACKAGE`).
        :type BandwidthPackageId: str
        :param ExclusiveCluster: Exclusive cluster information. This parameter is required for creating exclusive clusters of CLB instances.
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param SlaType: 
        :type SlaType: str
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param SnatPro: Whether Binding IPs of other VPCs feature switch
        :type SnatPro: bool
        :param SnatIps: Creates `SnatIp` when the binding IPs of other VPCs feature is enabled
        :type SnatIps: list of SnatIp
        :param ClusterTag: Tag for the STGW exclusive cluster.
        :type ClusterTag: str
        :param SlaveZoneId: Sets the secondary AZ ID for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`, which is applicable only to public network CLB instances.
Note: A secondary AZ will load traffic if the primary AZ has failures. The API `DescribeMasterZones` is used to query the primary and secondary AZ list of a region.
        :type SlaveZoneId: str
        :param EipAddressId: Unique ID of an EIP, which can only be used when binding the EIP of a private network CLB instance. E.g., `eip-11112222`.
        :type EipAddressId: str
        """
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AddressIPVersion = None
        self.Number = None
        self.MasterZoneId = None
        self.ZoneId = None
        self.InternetAccessible = None
        self.VipIsp = None
        self.Tags = None
        self.Vip = None
        self.BandwidthPackageId = None
        self.ExclusiveCluster = None
        self.SlaType = None
        self.ClientToken = None
        self.SnatPro = None
        self.SnatIps = None
        self.ClusterTag = None
        self.SlaveZoneId = None
        self.EipAddressId = None


    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Number = params.get("Number")
        self.MasterZoneId = params.get("MasterZoneId")
        self.ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Vip = params.get("Vip")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.SlaType = params.get("SlaType")
        self.ClientToken = params.get("ClientToken")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.ClusterTag = params.get("ClusterTag")
        self.SlaveZoneId = params.get("SlaveZoneId")
        self.EipAddressId = params.get("EipAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: Array of unique CLB instance IDs.
        :type LoadBalancerIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.
        :type LoadBalancerId: str
        :param SnatIps: Information of the SNAT IP to be added. You can apply for a specified IP or apply for an automatically assigned IP by specifying a subnet.
        :type SnatIps: list of SnatIp
        """
        self.LoadBalancerId = None
        self.SnatIps = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: Listener ID
        :type ListenerId: str
        :param Rules: Information of the new forwarding rule
        :type Rules: list of RuleInput
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Rules = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self.Rules.append(obj)
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
        :param LocationIds: Array of unique IDs of created forwarding rules
        :type LocationIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LocationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocationIds = params.get("LocationIds")
        self.RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupName: Target group name (up to 50 characters)
        :type TargetGroupName: str
        :param VpcId: `vpcid` attribute of a target group. If this parameter is left empty, the default VPC will be used.
        :type VpcId: str
        :param Port: Default port of a target group, which can be used for subsequently added servers.
        :type Port: int
        :param TargetGroupInstances: Real server bound to a target group
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupName = None
        self.VpcId = None
        self.Port = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupName = params.get("TargetGroupName")
        self.VpcId = params.get("VpcId")
        self.Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: ID generated after target group creation
        :type TargetGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TargetGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Log topic name
        :type TopicName: str
        :param PartitionCount: The number of topic partitions, which changes as partitions are split or merged. Each log topic can have up to 50 partitions. If this parameter is not passed in, 1 partition will be created by default and up to 10 partitions are allowed to be created.
        :type PartitionCount: int
        :param TopicType: Log type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).
        :type TopicType: str
        """
        self.TopicName = None
        self.PartitionCount = None
        self.TopicType = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        self.TopicType = params.get("TopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: ID of the listener to be deleted
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerIds: Array of listener IDs to delete (20 IDs at most). If this parameter is left empty, all listeners of the CLB instance will be deleted.
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: Array of IDs of the CLB instances to be deleted. Array length limit: 20.
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.
        :type LoadBalancerId: str
        :param Ips: Array of the SNAT IP addresses to be deleted
        :type Ips: list of str
        """
        self.LoadBalancerId = None
        self.Ips = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param SourceListenerId: Source listener ID
        :type SourceListenerId: str
        :param TargetListenerId: Target listener ID
        :type TargetListenerId: str
        :param RewriteInfos: Redirection relationship between forwarding rules
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param LocationIds: Array of IDs of the forwarding rules to be deleted
        :type LocationIds: list of str
        :param Domain: Domain name of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified.
        :type Domain: str
        :param Url: Forwarding path of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified.
        :type Url: str
        :param NewDefaultServerDomain: A listener must be configured with a default domain name. If you need to delete the default domain name, you can specify another one as the new default domain name.
        :type NewDefaultServerDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationIds = None
        self.Domain = None
        self.Url = None
        self.NewDefaultServerDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationIds = params.get("LocationIds")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupIds: Target group ID array
        :type TargetGroupIds: list of str
        """
        self.TargetGroupIds = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupInstances: Information of server to be unbound
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param InstanceIds: List of real server IDs
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID in the format of "lb-12345678"
        :type LoadBalancerId: str
        :param ListenerId: Listener ID in the format of "lbl-12345678"
        :type ListenerId: str
        :param Targets: List of real servers to be unbound. Array length limit: 20.
        :type Targets: list of Target
        :param LocationId: Forwarding rule ID in the format of "loc-12345678". When unbinding a server from a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param Offset: Data offset. Default value: 0.
        :type Offset: int
        :param Limit: Maximum number of IPs to be returned. Default value: 100,000.
        :type Limit: int
        """
        self.LoadBalancerId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList response structure.

    """

    def __init__(self):
        r"""
        :param BlockedIPCount: Number of returned IPs
        :type BlockedIPCount: int
        :param ClientIPField: Field for getting real client IP
        :type ClientIPField: str
        :param BlockedIPList: List of IPs added to blocklist 12360
        :type BlockedIPList: list of BlockedIP
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BlockedIPCount = None
        self.ClientIPField = None
        self.BlockedIPList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockedIPCount = params.get("BlockedIPCount")
        self.ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self.BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self.BlockedIPList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Async task ID returned by the `ModifyBlockIPList` API
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask response structure.

    """

    def __init__(self):
        r"""
        :param Status: 1: running; 2: failed; 6: succeeded
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of real server IDs
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerInfoList: CLB information list
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancerInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self.LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self.LoadBalancerInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus response structure.

    """

    def __init__(self):
        r"""
        :param HealthList: List of real server health statuses
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HealthList: list of ClassicalHealth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HealthList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self.HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self.HealthList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerIds: List of CLB listener IDs
        :type ListenerIds: list of str
        :param Protocol: CLB listening protocol. Valid values: TCP, UDP, HTTP, and HTTPS.
        :type Protocol: str
        :param ListenerPort: CLB listening port. Value range: 1 - 65535.
        :type ListenerPort: int
        :param Status: Listener status. Valid values: 0 (creating) and 1 (running).
        :type Status: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.ListenerPort = None
        self.Status = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.ListenerPort = params.get("ListenerPort")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners response structure.

    """

    def __init__(self):
        r"""
        :param Listeners: Listener list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Listeners: list of ClassicalListener
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets response structure.

    """

    def __init__(self):
        r"""
        :param Targets: Real server list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Targets: list of ClassicalTarget
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClsLogSetRequest(AbstractModel):
    """DescribeClsLogSet request structure.

    """


class DescribeClsLogSetResponse(AbstractModel):
    """DescribeClsLogSet response structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param HealthLogsetId: Health check logset ID
        :type HealthLogsetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogsetId = None
        self.HealthLogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.HealthLogsetId = params.get("HealthLogsetId")
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigAssociateListRequest(AbstractModel):
    """DescribeCustomizedConfigAssociateList request structure.

    """

    def __init__(self):
        r"""
        :param UconfigId: Configuration ID.
        :type UconfigId: str
        :param Offset: Start position of the binding list. Default: 0.
        :type Offset: int
        :param Limit: Number of binding lists to pull. Default: 20.
        :type Limit: int
        :param Domain: Searches for the domain name.
        :type Domain: str
        """
        self.UconfigId = None
        self.Offset = None
        self.Limit = None
        self.Domain = None


    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizedConfigAssociateListResponse(AbstractModel):
    """DescribeCustomizedConfigAssociateList response structure.

    """

    def __init__(self):
        r"""
        :param BindList: List of bound resources
        :type BindList: list of BindDetailItem
        :param TotalCount: Total number of bound resources
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BindList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BindList") is not None:
            self.BindList = []
            for item in params.get("BindList"):
                obj = BindDetailItem()
                obj._deserialize(item)
                self.BindList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigListRequest(AbstractModel):
    """DescribeCustomizedConfigList request structure.

    """

    def __init__(self):
        r"""
        :param ConfigType: Configuration type. Valid values: `CLB` (CLB-specific configs), `SERVER` (domain name-specific configs), and `LOCATION` (forwarding rule-specific configs).
        :type ConfigType: str
        :param Offset: Pagination offset. Default: 0.
        :type Offset: int
        :param Limit: Number of results per page. Default: 20.
        :type Limit: int
        :param ConfigName: Specifies the name of configs to query. Fuzzy match is supported.
        :type ConfigName: str
        :param UconfigIds: Configuration ID.
        :type UconfigIds: list of str
        :param Filters: The filters are:
<li> loadbalancer-id - String - Required: no - (filter) CLB instance ID, such as "lb-12345678". </li>
<li> vip - String - Required: no - (filter) CLB instance VIP, such as "1.1.1.1" and "2204::22:3". </li>
        :type Filters: list of Filter
        """
        self.ConfigType = None
        self.Offset = None
        self.Limit = None
        self.ConfigName = None
        self.UconfigIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.ConfigType = params.get("ConfigType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigName = params.get("ConfigName")
        self.UconfigIds = params.get("UconfigIds")
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
        


class DescribeCustomizedConfigListResponse(AbstractModel):
    """DescribeCustomizedConfigList response structure.

    """

    def __init__(self):
        r"""
        :param ConfigList: Configuration list.
        :type ConfigList: list of ConfigListItem
        :param TotalCount: Number of configurations.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConfigList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConfigListItem()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param ListenerIds: Array of CLB listener IDs to query (100 IDs at most).
        :type ListenerIds: list of str
        :param Protocol: Type of the listener protocols to be queried. Valid values: TCP, UDP, HTTP, HTTPS, and TCP_SSL.
        :type Protocol: str
        :param Port: Port of the listeners to be queried
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param Listeners: Listener list
        :type Listeners: list of Listener
        :param TotalCount: Total number of listeners (with filters of port, protocol, and listener ID applied).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId request structure.

    """

    def __init__(self):
        r"""
        :param CertIds: Server or client certificate ID
        :type CertIds: list of str
        """
        self.CertIds = None


    def _deserialize(self, params):
        self.CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId response structure.

    """

    def __init__(self):
        r"""
        :param CertSet: Certificate ID and list of CLB instances associated with it
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self.CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self.CertSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerTrafficRequest(AbstractModel):
    """DescribeLoadBalancerTraffic request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerRegion: CLB instance region. If this parameter is not passed in, CLB instances in all regions will be returned.
        :type LoadBalancerRegion: str
        """
        self.LoadBalancerRegion = None


    def _deserialize(self, params):
        self.LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerTrafficResponse(AbstractModel):
    """DescribeLoadBalancerTraffic response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerTraffic: Information of CLB instances sorted by outbound bandwidth from highest to lowest
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerTraffic: list of LoadBalancerTraffic
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancerTraffic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerTraffic") is not None:
            self.LoadBalancerTraffic = []
            for item in params.get("LoadBalancerTraffic"):
                obj = LoadBalancerTraffic()
                obj._deserialize(item)
                self.LoadBalancerTraffic.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersDetailRequest(AbstractModel):
    """DescribeLoadBalancersDetail request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of CLB instance lists returned. Default value: 20; maximum value: 100.
        :type Limit: int
        :param Offset: Starting offset of the CLB instance list returned. Default value: 0.
        :type Offset: int
        :param Fields: List of fields to be returned. The `LoadBalancerId` and `LoadBalancerName` are returned by default.
        :type Fields: list of str
        :param TargetType: Target type. Valid values: NODE and GROUP. If the list of fields contains `TargetId`, `TargetAddress`, `TargetPort`, `TargetWeight` and other fields, `Target` of the target group or non-target group must be exported.
        :type TargetType: str
        :param Filters: Filter condition of querying lists describing CLB instance details:
<li> loadbalancer-id - String - Required: no - (Filter condition) CLB instance ID, such as "lb-12345678". </li>
<li> project-id - String - Required: no - (Filter condition) Project ID, such as "0" and "123".</li>
<li> network - String - Required: no - (Filter condition) Network type of the CLB instance, such as "Public" and "Private".</li>
<li> vip - String - Required: no - (Filter condition) CLB instance VIP, such as "1.1.1.1" and "2204::22:3". </li>
<li> target-ip - String - Required: no - (Filter condition) Private IP of the target real servers, such as"1.1.1.1" and "2203::214:4".</li>
<li> vpcid - String - Required: no - (Filter condition) Identifier of the VPC instance to which the CLB instance belongs, such as "vpc-12345678".</li>
<li> zone - String - Required: no - (Filter condition) Availability zone where the CLB instance resides, such as "ap-guangzhou-1".</li>
<li> tag-key - String - Required: no - (Filter condition) Tag key of the CLB instance, such as "name".</li>
<li> tag:* - String - Required: no - (Filter condition) CLB instance tag, followed by tag key after the colon ':'. For example, use {"Name": "tag:name","Values": ["zhangsan", "lisi"]} to filter the tag key “name” with the tag value “zhangsan” and “lisi”.</li>
<li> fuzzy-search - String - Required: no - (Filter condition) Fuzzy search for CLB instance VIP and CLB instance name, such as "1.1".</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Fields = None
        self.TargetType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Fields = params.get("Fields")
        self.TargetType = params.get("TargetType")
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
        


class DescribeLoadBalancersDetailResponse(AbstractModel):
    """DescribeLoadBalancersDetail response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of lists describing CLB instance details.
        :type TotalCount: int
        :param LoadBalancerDetailSet: List of CLB instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerDetailSet: list of LoadBalancerDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerDetailSet") is not None:
            self.LoadBalancerDetailSet = []
            for item in params.get("LoadBalancerDetailSet"):
                obj = LoadBalancerDetail()
                obj._deserialize(item)
                self.LoadBalancerDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: CLB instance ID
        :type LoadBalancerIds: list of str
        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param Forward: CLB instance type. 1: generic CLB instance; 0: classic CLB instance
        :type Forward: int
        :param LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param Domain: Domain name assigned to a CLB instance by Tencent Cloud. This parameter is meaningful only for the public network classic CLB.
        :type Domain: str
        :param LoadBalancerVips: VIP address of a CLB instance (there can be multiple addresses)
        :type LoadBalancerVips: list of str
        :param BackendPublicIps: Public IP of the real server bound to a CLB.
        :type BackendPublicIps: list of str
        :param BackendPrivateIps: Private IP of the real server bound to a CLB.
        :type BackendPrivateIps: list of str
        :param Offset: Data offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param OrderBy: Sort by parameter. Value range: LoadBalancerName, CreateTime, Domain, LoadBalancerType.
        :type OrderBy: str
        :param OrderType: 1: reverse; 0: sequential. Default value: reverse by creation time |
        :type OrderType: int
        :param SearchKey: Search field which fuzzy matches name, domain name, or VIP.
        :type SearchKey: str
        :param ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API.
        :type ProjectId: int
        :param WithRs: Whether a CLB instance is bound to a real server. 0: no; 1: yes; -1: query all.
        :type WithRs: int
        :param VpcId: VPC where a CLB instance resides, such as vpc-bhqkbhdx.
Basic network does not support queries by VpcId.
        :type VpcId: str
        :param SecurityGroup: Security group ID, e.g., `sg-m1cc****`.
        :type SecurityGroup: str
        :param MasterZone: Primary AZ ID, e.g., `100001` (Guangzhou Zone 1).
        :type MasterZone: str
        :param Filters: Each request can have up to 10 `Filters` and 100 `Filter.Values`. Detailed filter conditions:
<li> internet-charge-type - Type: String - Required: No - Filter by CLB network billing mode, including `TRAFFIC_POSTPAID_BY_HOUR`</li>
        :type Filters: list of Filter
        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.BackendPublicIps = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchKey = None
        self.ProjectId = None
        self.WithRs = None
        self.VpcId = None
        self.SecurityGroup = None
        self.MasterZone = None
        self.Filters = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPublicIps = params.get("BackendPublicIps")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchKey = params.get("SearchKey")
        self.ProjectId = params.get("ProjectId")
        self.WithRs = params.get("WithRs")
        self.VpcId = params.get("VpcId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.MasterZone = params.get("MasterZone")
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
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of CLB instances that meet the filter criteria. This value is independent of the Limit in the input parameter.
        :type TotalCount: int
        :param LoadBalancerSet: Array of returned CLB instances.
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    """DescribeQuota request structure.

    """


class DescribeQuotaResponse(AbstractModel):
    """DescribeQuota response structure.

    """

    def __init__(self):
        r"""
        :param QuotaSet: Quota list
        :type QuotaSet: list of Quota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param SourceListenerIds: Array of CLB listener IDs
        :type SourceListenerIds: list of str
        :param SourceLocationIds: Array of CLB forwarding rule IDs
        :type SourceLocationIds: list of str
        """
        self.LoadBalancerId = None
        self.SourceListenerIds = None
        self.SourceLocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerIds = params.get("SourceListenerIds")
        self.SourceLocationIds = params.get("SourceLocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite response structure.

    """

    def __init__(self):
        r"""
        :param RewriteSet: Array of redirection forwarding rules. If there are no redirection rules, an empty array will be returned.
        :type RewriteSet: list of RuleOutput
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RewriteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self.RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.RewriteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter. Currently, only filtering by `TargetGroupId`, `BindIP`, or `InstanceId` is supported.
        :type Filters: list of Filter
        :param Limit: Number of displayed results. Default value: 20
        :type Limit: int
        :param Offset: Display offset. Default value: 0
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of results in current query
        :type TotalCount: int
        :param TargetGroupInstanceSet: Information of the bound server
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param RealCount: Actual statistics, which are not affected by `Limit`, `Offset`, and `CAM`.
        :type RealCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupInstanceSet = None
        self.RealCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self.TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self.TargetGroupInstanceSet.append(obj)
        self.RealCount = params.get("RealCount")
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupIds: Target group ID array
        :type TargetGroupIds: list of str
        :param Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`. Target group ID will be used first.
        :type Filters: list of Filter
        :param Offset: Starting display offset
        :type Offset: int
        :param Limit: Limit of the number of displayed results. Default value: 20.
        :type Limit: int
        """
        self.TargetGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
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
        


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of displayed results
        :type TotalCount: int
        :param TargetGroupSet: Information set of displayed target groups
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupIds: Target group ID, which is exclusive of `Filters`.
        :type TargetGroupIds: list of str
        :param Limit: Limit of the number of displayed results. Default value: 20.
        :type Limit: int
        :param Offset: Starting display offset
        :type Offset: int
        :param Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`.
        :type Filters: list of Filter
        """
        self.TargetGroupIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of displayed results
        :type TotalCount: int
        :param TargetGroupSet: Information set of displayed target groups
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: List of IDs of CLB instances to be queried
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancers: CLB instance list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancerHealth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param ListenerIds: List of listener IDs (20 IDs at most).
        :type ListenerIds: list of str
        :param Protocol: Listener protocol type
        :type Protocol: str
        :param Port: Listener port
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets response structure.

    """

    def __init__(self):
        r"""
        :param Listeners: Information of real servers bound to the listener
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerBackend
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Request ID, i.e., the RequestId parameter returned by the API.
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Current status of a task. Value range: 0 (succeeded), 1 (failed), 2 (in progress).
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param Associations: Array of rules to be unbound
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExclusiveCluster(AbstractModel):
    """Dedicated cluster

    """

    def __init__(self):
        r"""
        :param L4Clusters: Layer-4 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.
        :type L4Clusters: list of ClusterItem
        :param L7Clusters: Layer-7 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.
        :type L7Clusters: list of ClusterItem
        :param ClassicalCluster: vpcgw cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`
        """
        self.L4Clusters = None
        self.L7Clusters = None
        self.ClassicalCluster = None


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self.L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self.L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self.ClassicalCluster = ClusterItem()
            self.ClassicalCluster._deserialize(params.get("ClassicalCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfo(AbstractModel):
    """Reserved field which can be ignored generally.

    """

    def __init__(self):
        r"""
        :param ZhiTong: Whether to enable VIP direct connection
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZhiTong: bool
        :param TgwGroupName: TgwGroup name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TgwGroupName: str
        """
        self.ZhiTong = None
        self.TgwGroupName = None


    def _deserialize(self, params):
        self.ZhiTong = params.get("ZhiTong")
        self.TgwGroupName = params.get("TgwGroupName")
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
        :param Name: Filter name
        :type Name: str
        :param Values: Filter value array
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
        


class HealthCheck(AbstractModel):
    """Health check information.
    Note: Custom check parameters are currently supported only in certain beta test regions.

    """

    def __init__(self):
        r"""
        :param HealthSwitch: Whether to enable health check. 1: enable; 0: disable.
        :type HealthSwitch: int
        :param TimeOut: Health check response timeout period in seconds (applicable only to layer-4 listeners). Value range: 2-60. Default value: 2. This parameter should be less than the check interval.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeOut: int
        :param IntervalTime: Health check interval in seconds. Value range: 5-300. Default value: 5.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntervalTime: int
        :param HealthNum: Health threshold. Default value: 3, indicating that if a forward is found healthy three consecutive times, it is considered to be normal. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthNum: int
        :param UnHealthNum: Unhealthy threshold. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it is considered to be exceptional. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnHealthNum: int
        :param HttpCode: Health check status code (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: 1-31. Default value: 31.
1 means that the return value of 1xx after detection means healthy, 2 for returning 2xx for healthy, 4 for returning 3xx for healthy, 8 for returning 4xx for healthy, and 16 for returning 5xx for healthy. If you want multiple return codes to represent healthy, sum up the corresponding values. Note: The HTTP health check mode of TCP listeners only supports specifying one kind of health check status code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCode: int
        :param HttpCheckPath: Health check path (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners).
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCheckPath: str
        :param HttpCheckDomain: Health check domain name (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners).
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCheckDomain: str
        :param HttpCheckMethod: Health check method (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: HEAD, GET. Default value: HEAD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCheckMethod: str
        :param CheckPort: Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, it is recommended to leave it empty. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckPort: int
        :param ContextType: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the input format of the health check. Value range: HEX, TEXT. If the value is HEX, the characters of SendContext and RecvContext can only be selected from 0123456789ABCDEF and the length must be an even number. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContextType: str
        :param SendContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the content of the request sent by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SendContext: str
        :param RecvContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the result returned by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecvContext: str
        :param CheckType: Health check protocol (a custom check parameter). Value range: TCP, HTTP, CUSTOM (applicable only to TCP/UDP listeners, where UDP listeners only support CUSTOM. If custom health check is used, this parameter is required).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckType: str
        :param HttpVersion: Health check protocol (a custom check parameter), which is required if the value of CheckType is HTTP. This parameter represents the HTTP version of the real server. Value range: HTTP/1.0, HTTP/1.1. (Applicable only to TCP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpVersion: str
        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthNum = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.HttpCheckMethod = None
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None
        self.HttpVersion = None


    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthNum = params.get("UnHealthNum")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckMethod = params.get("HttpCheckMethod")
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        self.HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """Network billing mode based on maximum outbound bandwidth

    """

    def __init__(self):
        r"""
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR: hourly pay-as-you-go by traffic; BANDWIDTH_POSTPAID_BY_HOUR: hourly pay-as-you-go by bandwidth;
BANDWIDTH_PACKAGE: billed by bandwidth package (currently, this method is supported only if the ISP is specified)
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: Maximum outbound bandwidth in Mbps, which applies only to public network CLB. Value range: 0-65,535. Default value: 10.
        :type InternetMaxBandwidthOut: int
        :param BandwidthpkgSubType: Bandwidth package type, such as SINGLEISP
Note: This field may return null, indicating that no valid values can be obtained.
        :type BandwidthpkgSubType: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.BandwidthpkgSubType = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.BandwidthpkgSubType = params.get("BandwidthpkgSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBChargePrepaid(AbstractModel):
    """Monthly subscription configuration of a CLB instance

    """

    def __init__(self):
        r"""
        :param RenewFlag: Renewal type. AUTO_RENEW: automatic renewal; MANUAL_RENEW: manual renewal
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: str
        :param Period: Cycle, indicating the number of months (reserved field)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Period: int
        """
        self.RenewFlag = None
        self.Period = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """Listener information

    """

    def __init__(self):
        r"""
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Protocol: Listener protocol
        :type Protocol: str
        :param Port: Listener port
        :type Port: int
        :param Certificate: Information of certificates bound to the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param HealthCheck: Health check information of the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: Request scheduling method
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scheduler: str
        :param SessionExpireTime: Session persistence time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionExpireTime: int
        :param SniSwitch: Whether to enable the SNI feature (this parameter is only meaningful for HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SniSwitch: int
        :param Rules: All forwarding rules under a listener (this parameter is meaningful only for HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleOutput
        :param ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param CreateTime: Listener creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param EndPort: End port of a port range
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        :param TargetType: Real server type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetType: str
        :param TargetGroup: Basic information of a bound target group. This field will be returned when a target group is bound to a listener.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionType: str
        :param KeepaliveEnable: Whether a persistent connection is enabled (1: enabled; 0: disabled). This parameter can only be configured in HTTP/HTTPS listeners.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KeepaliveEnable: int
        :param Toa: Only the NAT64 CLB TCP listeners are supported.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Toa: bool
        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeregisterTargetRst: bool
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Certificate = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.SniSwitch = None
        self.Rules = None
        self.ListenerName = None
        self.CreateTime = None
        self.EndPort = None
        self.TargetType = None
        self.TargetGroup = None
        self.SessionType = None
        self.KeepaliveEnable = None
        self.Toa = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ListenerName = params.get("ListenerName")
        self.CreateTime = params.get("CreateTime")
        self.EndPort = params.get("EndPort")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.SessionType = params.get("SessionType")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.Toa = params.get("Toa")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """Details of real servers bound to a listener

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID
        :type ListenerId: str
        :param Protocol: Listener protocol
        :type Protocol: str
        :param Port: Listener port
        :type Port: int
        :param Rules: Information of rules under a listener (applicable only to HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleTargets
        :param Targets: List of real servers bound to a listener (applicable only to TCP/UDP/TCP_SSL listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        :param EndPort: Ending port in port range if port range is supported; 0 if port range is not supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None
        self.EndPort = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """Health check information of the listener

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID
        :type ListenerId: str
        :param ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param Protocol: Listener protocol
        :type Protocol: str
        :param Port: Listener port
        :type Port: int
        :param Rules: List of forwarding rules of the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleHealth
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """CLB instance information

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param Forward: CLB type identifier. Value range: 1 (CLB); 0 (classic CLB).
        :type Forward: int
        :param Domain: CLB instance domain name. This field is provided only to public network classic CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param LoadBalancerVips: List of VIPs of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerVips: list of str
        :param Status: CLB instance status, including:
0: creating; 1: running.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param CreateTime: CLB instance creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param StatusTime: Last status change time of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusTime: str
        :param ProjectId: ID of the project to which a CLB instance belongs. 0: default project.
        :type ProjectId: int
        :param VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param OpenBgp: Protective CLB identifier. Value range: 1 (protective), 0 (non-protective).
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpenBgp: int
        :param Snat: SNAT is enabled for all private network classic CLB created before December 2016.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Snat: bool
        :param Isolation: 0: not isolated; 1: isolated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Isolation: int
        :param Log: Log information. Only the public network CLB that have HTTP or HTTPS listeners can generate logs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Log: str
        :param SubnetId: Subnet where a CLB instance resides (meaningful only for private network VPC CLB)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param Tags: CLB instance tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param SecureGroups: Security group of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecureGroups: list of str
        :param TargetRegionInfo: Basic information of a backend server bound to a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param AnycastZone: Anycast CLB publishing region. For non-anycast CLB, this field returns an empty string.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AnycastZone: str
        :param AddressIPVersion: IP version. Valid values: ipv4, ipv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPVersion: str
        :param NumericalVpcId: VPC ID in a numeric form
Note: This field may return null, indicating that no valid values can be obtained.
        :type NumericalVpcId: int
        :param VipIsp: ISP to which a CLB IP address belongs
Note: This field may return null, indicating that no valid values can be obtained.
        :type VipIsp: str
        :param MasterZone: Primary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`
        :param BackupZoneSet: Secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupZoneSet: list of ZoneInfo
        :param IsolatedTime: CLB instance isolation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param ExpireTime: CLB instance expiration time, which takes effect only for prepaid instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param ChargeType: Billing mode of CLB instance. Valid values: PREPAID (monthly subscription), POSTPAID_BY_HOUR (pay as you go).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param NetworkAttributes: CLB instance network attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param PrepaidAttributes: Prepaid billing attributes of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param LogSetId: Logset ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetId: str
        :param LogTopicId: Log topic ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogTopicId: str
        :param AddressIPv6: IPv6 address of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param ExtraInfo: Reserved field which can be ignored generally.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param IsDDos: Whether an Anti-DDoS Pro instance can be bound
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDDos: bool
        :param ConfigId: Custom configuration ID at the CLB instance level
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigId: str
        :param LoadBalancerPassToTarget: Whether a real server opens the traffic from a CLB instance to the internet
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: bool
        :param ExclusiveCluster: Private network dedicated cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param IPv6Mode: This field is meaningful only when the IP address version is `ipv6`. Valid values: IPv6Nat64, IPv6FullChain
Note: this field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param SnatPro: Whether to enable SnatPro.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SnatPro: bool
        :param SnatIps: `SnatIp` list after SnatPro load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SnatIps: list of SnatIp
        :param SlaType: Performance guarantee specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type SlaType: str
        :param IsBlock: Whether VIP is blocked
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsBlock: bool
        :param IsBlockTime: Time blocked or unblocked
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsBlockTime: str
        :param LocalBgp: Whether the IP type is the local BGP
        :type LocalBgp: bool
        :param ClusterTag: Dedicated layer-7 tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterTag: str
        :param MixIpTarget: If the layer-7 listener of an IPv6FullChain CLB instance is enabled, the CLB instance can be bound with an IPv4 and an IPv6 CVM instance simultaneously.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MixIpTarget: bool
        :param Zones: Availability zone of a VPC-based private network CLB instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param NfvInfo: Whether it is an NFV CLB instance. No returned information: no; l7nfv: yes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NfvInfo: str
        :param HealthLogSetId: Health check logset ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type HealthLogSetId: str
        :param HealthLogTopicId: Health check log topic ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type HealthLogTopicId: str
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Forward = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.ProjectId = None
        self.VpcId = None
        self.OpenBgp = None
        self.Snat = None
        self.Isolation = None
        self.Log = None
        self.SubnetId = None
        self.Tags = None
        self.SecureGroups = None
        self.TargetRegionInfo = None
        self.AnycastZone = None
        self.AddressIPVersion = None
        self.NumericalVpcId = None
        self.VipIsp = None
        self.MasterZone = None
        self.BackupZoneSet = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.LogSetId = None
        self.LogTopicId = None
        self.AddressIPv6 = None
        self.ExtraInfo = None
        self.IsDDos = None
        self.ConfigId = None
        self.LoadBalancerPassToTarget = None
        self.ExclusiveCluster = None
        self.IPv6Mode = None
        self.SnatPro = None
        self.SnatIps = None
        self.SlaType = None
        self.IsBlock = None
        self.IsBlockTime = None
        self.LocalBgp = None
        self.ClusterTag = None
        self.MixIpTarget = None
        self.Zones = None
        self.NfvInfo = None
        self.HealthLogSetId = None
        self.HealthLogTopicId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.OpenBgp = params.get("OpenBgp")
        self.Snat = params.get("Snat")
        self.Isolation = params.get("Isolation")
        self.Log = params.get("Log")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self.AnycastZone = params.get("AnycastZone")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.NumericalVpcId = params.get("NumericalVpcId")
        self.VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self.MasterZone = ZoneInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self.BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.BackupZoneSet.append(obj)
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.IsDDos = params.get("IsDDos")
        self.ConfigId = params.get("ConfigId")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.IPv6Mode = params.get("IPv6Mode")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.SlaType = params.get("SlaType")
        self.IsBlock = params.get("IsBlock")
        self.IsBlockTime = params.get("IsBlockTime")
        self.LocalBgp = params.get("LocalBgp")
        self.ClusterTag = params.get("ClusterTag")
        self.MixIpTarget = params.get("MixIpTarget")
        self.Zones = params.get("Zones")
        self.NfvInfo = params.get("NfvInfo")
        self.HealthLogSetId = params.get("HealthLogSetId")
        self.HealthLogTopicId = params.get("HealthLogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    """CLB instance details

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param LoadBalancerType: CLB instance network type:
Public: public network; Private: private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param Status: CLB instance status, including:
0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param Address: CLB instance VIP.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param AddressIPv6: IPv6 VIP address of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param AddressIPVersion: IP version of the CLB instance. Valid values: IPv4, IPv6.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPVersion: str
        :param IPv6Mode: IPv6 address type of the CLB instance. Valid values: IPv6Nat64, IPv6FullChain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param Zone: Availability zone where the CLB instance resides.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param AddressIsp: ISP to which the CLB IP address belongs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIsp: str
        :param VpcId: ID of the VPC instance to which the CLB instance belongs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param ProjectId: ID of the project to which the CLB instance belongs. 0: default project.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param CreateTime: CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param ChargeType: CLB instance billing mode.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param NetworkAttributes: CLB instance network attribute.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param PrepaidAttributes: Pay-as-you-go attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param ExtraInfo: Reserved field, which can be ignored generally.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param ConfigId: Custom configuration ID at the CLB instance level.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConfigId: str
        :param Tags: CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param ListenerId: CLB listener ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Protocol: Listener protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param Port: Listener port.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param LocationId: Forwarding rule ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocationId: str
        :param Domain: Domain name of the forwarding rule.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Url: Forwarding rule path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param TargetId: ID of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetId: str
        :param TargetAddress: Address of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetAddress: str
        :param TargetPort: Listening port of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetPort: int
        :param TargetWeight: Forwarding weight of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetWeight: int
        :param Isolation: 0: not isolated; 1: isolated.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Isolation: int
        :param SecurityGroup: List of the security groups bound to the CLB instance.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroup: list of str
        :param LoadBalancerPassToTarget: Whether the CLB instance is billed by IP.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: int
        :param TargetHealth: Health status of the target real server.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetHealth: str
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Status = None
        self.Address = None
        self.AddressIPv6 = None
        self.AddressIPVersion = None
        self.IPv6Mode = None
        self.Zone = None
        self.AddressIsp = None
        self.VpcId = None
        self.ProjectId = None
        self.CreateTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.ExtraInfo = None
        self.ConfigId = None
        self.Tags = None
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.TargetId = None
        self.TargetAddress = None
        self.TargetPort = None
        self.TargetWeight = None
        self.Isolation = None
        self.SecurityGroup = None
        self.LoadBalancerPassToTarget = None
        self.TargetHealth = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Status = params.get("Status")
        self.Address = params.get("Address")
        self.AddressIPv6 = params.get("AddressIPv6")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.IPv6Mode = params.get("IPv6Mode")
        self.Zone = params.get("Zone")
        self.AddressIsp = params.get("AddressIsp")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.ConfigId = params.get("ConfigId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.TargetId = params.get("TargetId")
        self.TargetAddress = params.get("TargetAddress")
        self.TargetPort = params.get("TargetPort")
        self.TargetWeight = params.get("TargetWeight")
        self.Isolation = params.get("Isolation")
        self.SecurityGroup = params.get("SecurityGroup")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self.TargetHealth = params.get("TargetHealth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """CLB instance health check status

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param Listeners: List of listeners
Note: This field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerHealth
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerTraffic(AbstractModel):
    """CLB instance traffic data

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param Region: CLB instance region
        :type Region: str
        :param Vip: CLB instance VIP
        :type Vip: str
        :param OutBandwidth: Maximum outbound bandwidth in Mbps
        :type OutBandwidth: float
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Region = None
        self.Vip = None
        self.OutBandwidth = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Region = params.get("Region")
        self.Vip = params.get("Vip")
        self.OutBandwidth = params.get("OutBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param SourceListenerId: Source listener ID
        :type SourceListenerId: str
        :param TargetListenerId: Target listener ID
        :type TargetListenerId: str
        :param RewriteInfos: Redirection relationship between forwarding rules
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: CLB instance ID
        :type LoadBalancerIds: list of str
        :param Type: Operation type. Valid values:
<li> add_customized_field (sets header initially to enable the blocklist feature)</li>
<li> set_customized_field (modifies header)</li>
<li> del_customized_field (deletes header)</li>
<li> add_blocked (adds IPs to blocklist)</li>
<li> del_blocked (deletes IPs from blocklist)</li>
<li> flush_blocked (clears blocklist)</li>
        :type Type: str
        :param ClientIPField: Header field that stores real client IPs
        :type ClientIPField: str
        :param BlockIPList: List of blocked IPs. The array can contain up to 200,000 entries in one operation.
        :type BlockIPList: list of str
        :param ExpireTime: Expiration time in seconds. Default value: 3600
        :type ExpireTime: int
        :param AddStrategy: IP adding policy. Valid value: fifo (if a blocklist is full, new IPs added to the blocklist will adopt the first-in first-out policy)
        :type AddStrategy: str
        """
        self.LoadBalancerIds = None
        self.Type = None
        self.ClientIPField = None
        self.BlockIPList = None
        self.ExpireTime = None
        self.AddStrategy = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.Type = params.get("Type")
        self.ClientIPField = params.get("ClientIPField")
        self.BlockIPList = params.get("BlockIPList")
        self.ExpireTime = params.get("ExpireTime")
        self.AddStrategy = params.get("AddStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList response structure.

    """

    def __init__(self):
        r"""
        :param JodId: Async task ID
        :type JodId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JodId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JodId = params.get("JodId")
        self.RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Domain: Domain name, which must be under a created forwarding rule.
        :type Domain: str
        :param NewDomain: New domain name
        :type NewDomain: str
        :param Certificate: Domain name certificate information. Note: This is only applicable to SNI-enabled listeners.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.
        :type Http2: bool
        :param DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.
        :type DefaultServer: bool
        :param NewDefaultServerDomain: A listener must be configured with a default domain name. If you need to disable the default domain name, you must specify another one as the new default domain name.
        :type NewDefaultServerDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None
        self.Certificate = None
        self.Http2 = None
        self.DefaultServer = None
        self.NewDefaultServerDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Http2 = params.get("Http2")
        self.DefaultServer = params.get("DefaultServer")
        self.NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Domain: Legacy domain name under a listener.
        :type Domain: str
        :param NewDomain: New domain name. 	Length limit: 1-120. There are three usage formats: non-regular expression, wildcard, and regular expression. A non-regular expression can only contain letters, digits, "-", and ".". In a wildcard, "*" can only be at the beginning or the end. A regular expressions must begin with a "~".
        :type NewDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param ListenerName: New listener name
        :type ListenerName: str
        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param HealthCheck: Health check parameter, which is applicable only to TCP, UDP, and TCP_SSL listeners.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: Certificate information. This parameter is applicable only to HTTPS and TCP_SSL listeners.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: Forwarding method of a listener. Value range: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        :param SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners. Note: The SNI feature can be enabled but cannot be disabled once enabled.
        :type SniSwitch: int
        :param KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners.
        :type KeepaliveEnable: int
        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
        :type DeregisterTargetRst: bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.SniSwitch = None
        self.KeepaliveEnable = None
        self.DeregisterTargetRst = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.KeepaliveEnable = params.get("KeepaliveEnable")
        self.DeregisterTargetRst = params.get("DeregisterTargetRst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: Unique CLB ID
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param TargetRegionInfo: Region information of the real server bound to a CLB.
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param InternetChargeInfo: Network billing parameter
        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param LoadBalancerPassToTarget: Whether the target opens traffic from CLB to the internet. If yes (true), only security groups on CLB will be verified; if no (false), security groups on both CLB and backend instance need to be verified.
        :type LoadBalancerPassToTarget: bool
        :param SnatPro: Whether to enable SnatPro
        :type SnatPro: bool
        :param DeleteProtect: Specifies whether to enable deletion protection.
        :type DeleteProtect: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None
        self.SnatPro = None
        self.DeleteProtect = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = InternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self.SnatPro = params.get("SnatPro")
        self.DeleteProtect = params.get("DeleteProtect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param DealName: This parameter can be used to query whether CLB billing mode switch is successful.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param LocationId: ID of the forwarding rule to be modified.
        :type LocationId: str
        :param Url: New forwarding path of the forwarding rule. This parameter is not required if the URL does not need to be modified.
        :type Url: str
        :param HealthCheck: Health check information
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.
        :type Scheduler: str
        :param SessionExpireTime: Session persistence time
        :type SessionExpireTime: int
        :param ForwardType: Forwarding protocol between CLB instance and real server. Default value: HTTP. Valid values: HTTP, HTTPS, and TRPC.
        :type ForwardType: str
        :param TrpcCallee: TRPC callee server route, which is required when `ForwardType` is "TRPC".
        :type TrpcCallee: str
        :param TrpcFunc: TRPC calling service API, which is required when `ForwardType` is "TRPC".
        :type TrpcFunc: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ForwardType = None
        self.TrpcCallee = None
        self.TrpcFunc = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.ForwardType = params.get("ForwardType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupName: New name of target group
        :type TargetGroupName: str
        :param Port: New default port of target group
        :type Port: int
        """
        self.TargetGroupId = None
        self.TargetGroupName = None
        self.Port = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupInstances: Array of servers for which to modify ports
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupInstances: Array of servers for which to modify weights
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Targets: List of real servers for which to modify the ports
        :type Targets: list of Target
        :param NewPort: New port of the real server bound to a listener or forwarding rule
        :type NewPort: int
        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        :param Targets: List of real servers for which to modify the weights
        :type Targets: list of Target
        :param Weight: New forwarding weight of a real server. Value range: 0-100. Default value: 10. If the Targets.Weight parameter is set, this parameter will not take effect.
        :type Weight: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """Quota description. All quotas are in the current region.

    """

    def __init__(self):
        r"""
        :param QuotaId: Quota name. Valid values:
<li> TOTAL_OPEN_CLB_QUOTA: quota of public network CLB instances in the current region</li>
<li> TOTAL_INTERNAL_CLB_QUOTA: quota of private network CLB instances in the current region</li>
<li> TOTAL_LISTENER_QUOTA: quota of listeners under one CLB instance</li>
<li> TOTAL_LISTENER_RULE_QUOTA: quota of forwarding rules under one listener</li>
<li> TOTAL_TARGET_BIND_QUOTA: quota of CVM instances can be bound under one forwarding rule</li>
        :type QuotaId: str
        :param QuotaCurrent: Currently used quantity. If it is `null`, it is meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type QuotaCurrent: int
        :param QuotaLimit: Quota limit.
        :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param TargetGroupInstances: Server instance array
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Targets: List of real servers to be bound. Array length limit: 20.
        :type Targets: list of Target
        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param Domain: Target forwarding rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param Url: Target forwarding rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Targets: Real server information
        :type Targets: list of ClassicalTargetInfo
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param OldCertificateId: ID of the certificate to be replaced, which can be a server certificate or a client certificate.
        :type OldCertificateId: str
        :param Certificate: Information such as the content of the new certificate
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        """
        self.OldCertificateId = None
        self.Certificate = None


    def _deserialize(self, params):
        self.OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RewriteLocationMap(AbstractModel):
    """Redirection relationship between forwarding rules

    """

    def __init__(self):
        r"""
        :param SourceLocationId: Source forwarding rule ID
        :type SourceLocationId: str
        :param TargetLocationId: Forwarding rule ID of a redirect target
        :type TargetLocationId: str
        :param RewriteCode: Redirection status code. Valid values: 301, 302, and 307.
        :type RewriteCode: int
        :param TakeUrl: Whether the matched URL is carried in redirection. It is required when configuring `RewriteCode`.
        :type TakeUrl: bool
        :param SourceDomain: Original domain name of redirection, which must be the corresponding domain name of `SourceLocationId`. It is required when configuring `RewriteCode`.
        :type SourceDomain: str
        """
        self.SourceLocationId = None
        self.TargetLocationId = None
        self.RewriteCode = None
        self.TakeUrl = None
        self.SourceDomain = None


    def _deserialize(self, params):
        self.SourceLocationId = params.get("SourceLocationId")
        self.TargetLocationId = params.get("TargetLocationId")
        self.RewriteCode = params.get("RewriteCode")
        self.TakeUrl = params.get("TakeUrl")
        self.SourceDomain = params.get("SourceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteTarget(AbstractModel):
    """Redirect target information

    """

    def __init__(self):
        r"""
        :param TargetListenerId: Listener ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetListenerId: str
        :param TargetLocationId: Forwarding rule ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetLocationId: str
        :param RewriteCode: Redirection status code
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RewriteCode: int
        :param TakeUrl: Whether the matched URL is carried in redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TakeUrl: bool
        :param RewriteType: Redirection type. Manual: manual redirection; Auto: automatic redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RewriteType: str
        """
        self.TargetListenerId = None
        self.TargetLocationId = None
        self.RewriteCode = None
        self.TakeUrl = None
        self.RewriteType = None


    def _deserialize(self, params):
        self.TargetListenerId = params.get("TargetListenerId")
        self.TargetLocationId = params.get("TargetLocationId")
        self.RewriteCode = params.get("RewriteCode")
        self.TakeUrl = params.get("TakeUrl")
        self.RewriteType = params.get("RewriteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsWeightRule(AbstractModel):
    """Modifies the data type of a node weight

    """

    def __init__(self):
        r"""
        :param ListenerId: CLB listener ID.
        :type ListenerId: str
        :param Targets: List of real servers whose weights to modify.
        :type Targets: list of Target
        :param LocationId: Forwarding rule ID, which is required only for layer-7 rules.
        :type LocationId: str
        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified
        :type Domain: str
        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified
        :type Url: str
        :param Weight: The new forwarding weight of the real server. Value range: [0, 100]. This parameter takes lower precedence than `Weight` in [`Targets`](https://intl.cloud.tencent.com/document/api/214/30694?from_cn_redirect=1#Target), which means that this parameter only takes effect when the `Weight` in `RsWeightRule` is left empty.
        :type Weight: int
        """
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """Health check status of a forwarding rule

    """

    def __init__(self):
        r"""
        :param LocationId: Forwarding rule ID
        :type LocationId: str
        :param Domain: Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Url: Forwarding rule Url
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param Targets: Health status of the real server bound to this rule
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Targets: list of TargetHealth
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInput(AbstractModel):
    """HTTP/HTTPS forwarding rule (input)

    """

    def __init__(self):
        r"""
        :param Domain: Domain name of the forwarding rule. Length: 1-80.
        :type Domain: str
        :param Url: Forwarding rule path. Length: 1-200.
        :type Url: str
        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. Setting it to 0 indicates that session persistence is disabled.
        :type SessionExpireTime: int
        :param HealthCheck: Health check information. For more information, please see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1)
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: Certificate information
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.
        :type Scheduler: str
        :param ForwardType: Forwarding protocol between the CLB instance and real server. Currently, HTTP/HTTPS/TRPC are supported.
        :type ForwardType: str
        :param DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.
        :type DefaultServer: bool
        :param Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.
        :type Http2: bool
        :param TargetType: Target real server type. NODE: binding a general node; TARGETGROUP: binding a target group.
        :type TargetType: str
        :param TrpcCallee: TRPC callee server route, which is required when `ForwardType` is `TRPC`.
        :type TrpcCallee: str
        :param TrpcFunc: TRPC calling service API, which is required when `ForwardType` is `TRPC`.
        :type TrpcFunc: str
        :param Quic: Whether to enable QUIC. Note: QUIC can be enabled only for HTTPS domain names
        :type Quic: bool
        """
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ForwardType = None
        self.DefaultServer = None
        self.Http2 = None
        self.TargetType = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.Quic = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ForwardType = params.get("ForwardType")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.TargetType = params.get("TargetType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.Quic = params.get("Quic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleOutput(AbstractModel):
    """HTTP/HTTPS listener forwarding rule (output)

    """

    def __init__(self):
        r"""
        :param LocationId: Forwarding rule ID
        :type LocationId: str
        :param Domain: Domain name of the forwarding rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Url: Forwarding rule path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param SessionExpireTime: Session persistence time
        :type SessionExpireTime: int
        :param HealthCheck: Health check information
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: Certificate information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param Scheduler: Request forwarding method of the rule
        :type Scheduler: str
        :param ListenerId: ID of the listener to which the forwarding rule belongs
        :type ListenerId: str
        :param RewriteTarget: Redirect target information of a forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`
        :param HttpGzip: Whether to enable gzip
        :type HttpGzip: bool
        :param BeAutoCreated: Whether the forwarding rule is automatically created
        :type BeAutoCreated: bool
        :param DefaultServer: Whether to use as the default domain name
        :type DefaultServer: bool
        :param Http2: Whether to enable Http2
        :type Http2: bool
        :param ForwardType: Forwarding protocol between CLB and real server
        :type ForwardType: str
        :param CreateTime: Forwarding rule creation time
        :type CreateTime: str
        :param TargetType: Real server type
        :type TargetType: str
        :param TargetGroup: Basic information of a bound target group. This field will be returned if a target group is bound to a rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param WafDomainId: WAF instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type WafDomainId: str
        :param TrpcCallee: TRPC callee server route, which is valid when `ForwardType` is `TRPC`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TrpcCallee: str
        :param TrpcFunc: TRPC calling service API, which is valid when `ForwardType` is `TRPC`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TrpcFunc: str
        :param QuicStatus: QUIC status
Note: this field may return null, indicating that no valid values can be obtained.
        :type QuicStatus: str
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ListenerId = None
        self.RewriteTarget = None
        self.HttpGzip = None
        self.BeAutoCreated = None
        self.DefaultServer = None
        self.Http2 = None
        self.ForwardType = None
        self.CreateTime = None
        self.TargetType = None
        self.TargetGroup = None
        self.WafDomainId = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.QuicStatus = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self.RewriteTarget = RewriteTarget()
            self.RewriteTarget._deserialize(params.get("RewriteTarget"))
        self.HttpGzip = params.get("HttpGzip")
        self.BeAutoCreated = params.get("BeAutoCreated")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.ForwardType = params.get("ForwardType")
        self.CreateTime = params.get("CreateTime")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.WafDomainId = params.get("WafDomainId")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.QuicStatus = params.get("QuicStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTargets(AbstractModel):
    """Information of the real server bound to a forwarding rule under an HTTP/HTTPS listener

    """

    def __init__(self):
        r"""
        :param LocationId: Forwarding rule ID
        :type LocationId: str
        :param Domain: Domain name of the forwarding rule
        :type Domain: str
        :param Url: Forwarding rule path.
        :type Url: str
        :param Targets: Real server information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param LogSetId: CLS logset ID
        :type LogSetId: str
        :param LogTopicId: CLS log topic ID
        :type LogTopicId: str
        :param LogType: Log type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).
        :type LogType: str
        """
        self.LoadBalancerId = None
        self.LogSetId = None
        self.LogTopicId = None
        self.LogType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param SecurityGroups: Array of security group IDs. One CLB instance can be bound to up to 50 security groups. If you want to unbind all security groups, you do not need to pass in this parameter, or you can pass in an empty array.
        :type SecurityGroups: list of str
        """
        self.LoadBalancerId = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroup: Security group ID, such as sg-12345678
        :type SecurityGroup: str
        :param OperationType: ADD: bind a security group;
DEL: unbind a security group
        :type OperationType: str
        :param LoadBalancerIds: Array of CLB instance IDs
        :type LoadBalancerIds: list of str
        """
        self.SecurityGroup = None
        self.OperationType = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnatIp(AbstractModel):
    """`SnatIp` information structure

    """

    def __init__(self):
        r"""
        :param SubnetId: Unique VPC subnet ID, such as `subnet-12345678`.
        :type SubnetId: str
        :param Ip: IP address, such as 192.168.0.1
        :type Ip: str
        """
        self.SubnetId = None
        self.Ip = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """CLB tag information

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
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
        


class Target(AbstractModel):
    """Redirect target, i.e., the real server bound to a CLB

    """

    def __init__(self):
        r"""
        :param Port: Listening port of a real server
Note: this parameter is required when binding a CVM or ENI.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param Type: Real server type. Value range: CVM (Cloud Virtual Machine), ENI (Elastic Network Interface). This parameter does not take effect currently as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param InstanceId: Unique ID of a CVM instance, which is required when binding a CVM instance. It can be obtained from the `InstanceId` field in the response of the `DescribeInstances` API. It indicates binding the primary IP of the primary ENI.
Note: either `InstanceId` or `EniIp` must be passed in.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Weight: The new forwarding weight of the real server. Value range: [0, 100]. Default: 10. This parameter takes priority over `Weight` in [`RsWeightRule`](https://intl.cloud.tencent.com/document/api/214/30694?from_cn_redirect=1#RsWeightRule). If it’s left empty, the value of `Weight` in `RsWeightRule` will be used.
        :type Weight: int
        :param EniIp: It is required when binding an IP. ENI IPs and other private IPs are supported. To bind an ENI IP, the ENI should be bound to a CVM instance before being bound to a CLB instance.
Note: either `InstanceId` or `EniIp` must be passed in. It is required when binding a dual-stack IPv6 CVM instance.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EniIp: str
        """
        self.Port = None
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupAssociation(AbstractModel):
    """Association between rule and target group

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: Listener ID
        :type ListenerId: str
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param LocationId: Forwarding rule ID
        :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetGroupId = None
        self.LocationId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.TargetGroupId = params.get("TargetGroupId")
        self.LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupBackend(AbstractModel):
    """Real server bound to a target group

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param Type: Real server type. Valid values: CVM, ENI (coming soon)
        :type Type: str
        :param InstanceId: Unique real server ID
        :type InstanceId: str
        :param Port: Listening port of real server
        :type Port: int
        :param Weight: Forwarding weight of real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param PublicIpAddresses: Public IP of real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: Private IP of real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param InstanceName: Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param RegisteredTime: Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param EniId: Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        :param ZoneId: AZ ID of the real server
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ZoneId: int
        """
        self.TargetGroupId = None
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInfo(AbstractModel):
    """Target group information

    """

    def __init__(self):
        r"""
        :param TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param VpcId: `vpcid` of target group
        :type VpcId: str
        :param TargetGroupName: Target group name
        :type TargetGroupName: str
        :param Port: Default port of target group
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param CreatedTime: Target group creation time
        :type CreatedTime: str
        :param UpdatedTime: Target group modification time
        :type UpdatedTime: str
        :param AssociatedRule: Array of associated rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedRule: list of AssociationItem
        """
        self.TargetGroupId = None
        self.VpcId = None
        self.TargetGroupName = None
        self.Port = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.AssociatedRule = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.VpcId = params.get("VpcId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self.AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self.AssociatedRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInstance(AbstractModel):
    """Target group instance

    """

    def __init__(self):
        r"""
        :param BindIP: Private IP of target group instance
        :type BindIP: str
        :param Port: Port of target group instance
        :type Port: int
        :param Weight: Weight of target group instance
        :type Weight: int
        :param NewPort: New port of target group instance
        :type NewPort: int
        """
        self.BindIP = None
        self.Port = None
        self.Weight = None
        self.NewPort = None


    def _deserialize(self, params):
        self.BindIP = params.get("BindIP")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """Describes the health information of a target

    """

    def __init__(self):
        r"""
        :param IP: Private IP of the target
        :type IP: str
        :param Port: Port bound to the target
        :type Port: int
        :param HealthStatus: Current health status. true: healthy; false: unhealthy.
        :type HealthStatus: bool
        :param TargetId: Instance ID of the target, such as ins-12345678
        :type TargetId: str
        :param HealthStatusDetial: Detailed information of the current health status. Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status.
        :type HealthStatusDetial: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetial = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetial = params.get("HealthStatusDetial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetRegionInfo(AbstractModel):
    """Information of the real server bound to a CLB instance, including region and network to which it belongs.

    """

    def __init__(self):
        r"""
        :param Region: Region of the target, such as ap-guangzhou
        :type Region: str
        :param VpcId: Network of the target, which is in the format of vpc-abcd1234 for VPC or 0 for basic network
        :type VpcId: str
        """
        self.Region = None
        self.VpcId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """AZ information

    """

    def __init__(self):
        r"""
        :param ZoneId: Unique AZ ID in a numeric form, such as 100001
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param Zone: Unique AZ ID in a string form, such as ap-guangzhou-1
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param ZoneName: AZ name, such as Guangzhou Zone 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param ZoneRegion: AZ region, e.g., ap-guangzhou.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ZoneRegion: str
        :param LocalZone: Whether the AZ is the `LocalZone`, e.g., false.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LocalZone: bool
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None
        self.ZoneRegion = None
        self.LocalZone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneRegion = params.get("ZoneRegion")
        self.LocalZone = params.get("LocalZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        