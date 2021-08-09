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
        """
        :param Associations: Association array\n        :type Associations: list of TargetGroupAssociation\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """Rule associated with target group

    """

    def __init__(self):
        """
        :param LoadBalancerId: ID of associated CLB instance\n        :type LoadBalancerId: str\n        :param ListenerId: ID of associated listener\n        :type ListenerId: str\n        :param LocationId: ID of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LocationId: str\n        :param Protocol: Protocol type of associated listener, such as HTTP or TCP\n        :type Protocol: str\n        :param Port: Port of associated listener\n        :type Port: int\n        :param Domain: Domain name of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Url: URL of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param LoadBalancerName: CLB instance name\n        :type LoadBalancerName: str\n        :param ListenerName: Listener name\n        :type ListenerName: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: `HTTPS:443` listener ID\n        :type ListenerId: str\n        :param Domains: The domain name to be redirected under the listener `HTTPS:443`. If it is left empty, all domain names under the listener `HTTPS:443` will be configured with redirects.\n        :type Domains: list of str\n        :param RewriteCodes: Redirection status code. Valid values: 301, 302, and 307.\n        :type RewriteCodes: list of int\n        :param TakeUrls: Whether the matched URL is carried in redirection.\n        :type TakeUrls: list of bool\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """Details of a real server bound to a listener

    """

    def __init__(self):
        """
        :param Type: Real server type. Valid values: CVM, ENI.\n        :type Type: str\n        :param InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API\n        :type InstanceId: str\n        :param Port: Listening port of a real server\n        :type Port: int\n        :param Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.\n        :type Weight: int\n        :param PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PublicIpAddresses: list of str\n        :param PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PrivateIpAddresses: list of str\n        :param InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InstanceName: str\n        :param RegisteredTime: Bound time of a real server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RegisteredTime: str\n        :param EniId: Unique ENI ID
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EniId: str\n        """
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
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupName: Target group name\n        :type TargetGroupName: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param Targets: Unbinding targets\n        :type Targets: list of BatchTarget\n        """
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
        """
        :param FailListenerIdSet: IDs of the listeners failed to unbind\n        :type FailListenerIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ModifyList: List of weights to be modified in batches\n        :type ModifyList: list of RsWeightRule\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param Targets: Binding target\n        :type Targets: list of BatchTarget\n        """
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
        """
        :param FailListenerIdSet: IDs of the listeners failed to bind. If this is blank, all listeners are bound successfully.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type FailListenerIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """Batch binding type

    """

    def __init__(self):
        """
        :param ListenerId: Listener ID\n        :type ListenerId: str\n        :param Port: Binding port\n        :type Port: int\n        :param InstanceId: CVM instance ID. Indicating binding the primary IP of the primary ENI.\n        :type InstanceId: str\n        :param EniIp: ENI IP or other private IP. This parameter is required for binding a dual-stack IPv6 CVM instance.\n        :type EniIp: str\n        :param Weight: CVM instance weight. Value range: [0, 100]. If it is not specified when binding the instance, 10 will be used by default.\n        :type Weight: int\n        :param LocationId: Layer-7 rule ID\n        :type LocationId: str\n        """
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
        


class BlockedIP(AbstractModel):
    """IP added to blocklist 12306

    """

    def __init__(self):
        """
        :param IP: Blacklisted IP\n        :type IP: str\n        :param CreateTime: Blacklisted time\n        :type CreateTime: str\n        :param ExpireTime: Expiration time\n        :type ExpireTime: str\n        """
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
        """
        :param CertId: Certificate ID\n        :type CertId: str\n        :param LoadBalancers: List of CLB instances associated with certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancers: list of LoadBalancer\n        """
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
        """
        :param SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)\n        :type SSLMode: str\n        :param CertId: ID of a server certificate. If you leave this parameter empty, you must upload the certificate, including CertContent, CertKey, and CertName.\n        :type CertId: str\n        :param CertCaId: ID of a client certificate. When the listener adopts mutual authentication (i.e., SSLMode = mutual), if you leave this parameter empty, you must upload the client certificate, including CertCaContent and CertCaName.\n        :type CertCaId: str\n        :param CertName: Name of the uploaded server certificate. If there is no CertId, this parameter is required.\n        :type CertName: str\n        :param CertKey: Key of the uploaded server certificate. If there is no CertId, this parameter is required.\n        :type CertKey: str\n        :param CertContent: Content of the uploaded server certificate. If there is no CertId, this parameter is required.\n        :type CertContent: str\n        :param CertCaName: Name of the uploaded client CA certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.\n        :type CertCaName: str\n        :param CertCaContent: Content of the uploaded client certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.\n        :type CertCaContent: str\n        """
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
        """
        :param SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)\n        :type SSLMode: str\n        :param CertId: Server certificate ID.\n        :type CertId: str\n        :param CertCaId: Client certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CertCaId: str\n        """
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
        """
        :param IP: Private IP of a real server\n        :type IP: str\n        :param Port: Real server port\n        :type Port: int\n        :param ListenerPort: CLB listener port\n        :type ListenerPort: int\n        :param Protocol: Forwarding protocol\n        :type Protocol: str\n        :param HealthStatus: Health check result. Value range: 1 (healthy), 0 (unhealthy)\n        :type HealthStatus: int\n        """
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
        """
        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param ListenerPort: CLB listener port\n        :type ListenerPort: int\n        :param InstancePort: Backend forwarding port of a listener\n        :type InstancePort: int\n        :param ListenerName: Listener name\n        :type ListenerName: str\n        :param Protocol: Listener protocol type\n        :type Protocol: str\n        :param SessionExpire: Session persistence time\n        :type SessionExpire: int\n        :param HealthSwitch: Whether health check is enabled. 1: enabled; 0: disabled.\n        :type HealthSwitch: int\n        :param TimeOut: Response timeout period\n        :type TimeOut: int\n        :param IntervalTime: Check interval\n        :type IntervalTime: int\n        :param HealthNum: Health threshold\n        :type HealthNum: int\n        :param UnhealthNum: Unhealthy threshold\n        :type UnhealthNum: int\n        :param HttpHash: A request balancing method for HTTP and HTTPS listeners of a public network classic CLB. wrr means weighted round robin, while ip_hash means consistent hashing based on source IPs of access requests.\n        :type HttpHash: str\n        :param HttpCode: Health check return code for HTTP and HTTPS listeners of a public network classic CLB. For more information, see the explanation of the field in the listener creating API.\n        :type HttpCode: int\n        :param HttpCheckPath: Health check path for HTTP and HTTPS listeners of a public network classic CLB\n        :type HttpCheckPath: str\n        :param SSLMode: Authentication method for an HTTPS listener of a public network classic CLB\n        :type SSLMode: str\n        :param CertId: Server certificate ID for an HTTPS listener of a public network classic CLB\n        :type CertId: str\n        :param CertCaId: Client certificate ID for an HTTPS listener of a public network classic CLB\n        :type CertCaId: str\n        :param Status: Listener status. Value range: 0 (creating), 1 (running)\n        :type Status: int\n        """
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
        """
        :param InstanceId: Real server ID\n        :type InstanceId: str\n        :param LoadBalancerIds: List of CLB instance IDs
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerIds: list of str\n        """
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
        """
        :param Type: Real server type. Value range: CVM, ENI (coming soon)\n        :type Type: str\n        :param InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API\n        :type InstanceId: str\n        :param Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.\n        :type Weight: int\n        :param PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PublicIpAddresses: list of str\n        :param PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PrivateIpAddresses: list of str\n        :param InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InstanceName: str\n        :param RunFlag: Real server status
1: failed; 2: running; 3: creating; 4: shut down; 5: returned; 6: returning; 7: restarting; 8: starting; 9: shutting down; 10: resetting password; 11: formatting; 12: making image; 13: setting bandwidth; 14: reinstalling system; 19: upgrading; 21: hot migrating
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RunFlag: int\n        """
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
        """
        :param InstanceId: Real server ID\n        :type InstanceId: str\n        :param Weight: Weight. Value range: [0, 100]\n        :type Weight: int\n        """
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
        """
        :param ClusterId: Unique cluster ID\n        :type ClusterId: str\n        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterName: str\n        :param Zone: Cluster AZ, such as ap-guangzhou-1
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Zone: str\n        """
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
        


class CreateClsLogSetRequest(AbstractModel):
    """CreateClsLogSet request structure.

    """

    def __init__(self):
        """
        :param Period: Logset retention period in days; max value: 90\n        :type Period: int\n        :param LogsetName: Logset name, which must be unique among all CLS logsets; default value: clb_logset\n        :type LogsetName: str\n        :param LogsetType: Logset type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).\n        :type LogsetType: str\n        """
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
        """
        :param LogsetId: Logset ID.\n        :type LogsetId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param Ports: Specifies for which ports to create listeners. Each port corresponds to a new listener.\n        :type Ports: list of int\n        :param Protocol: Listener protocol: TCP, UDP, HTTP, HTTPS, or TCP_SSL (which is currently in beta test. If you want to use it, please submit a ticket for application).\n        :type Protocol: str\n        :param ListenerNames: List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.\n        :type ListenerNames: list of str\n        :param HealthCheck: Health check parameter, which is applicable only to TCP, UDP, and TCP_SSL listeners.\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Certificate: Certificate information. This parameter is applicable only to TCP_SSL listeners and HTTPS listeners with the SNI feature not enabled.\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`\n        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.\n        :type SessionExpireTime: int\n        :param Scheduler: Forwarding method of a listener. Value range: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR. This parameter is applicable only to TCP/UDP/TCP_SSL listeners.\n        :type Scheduler: str\n        :param SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners\n        :type SniSwitch: int\n        :param TargetType: Target real server type. `NODE`: binding a general node; `TARGETGROUP`: binding a target group.\n        :type TargetType: str\n        :param SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.\n        :type SessionType: str\n        :param KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners. Valid values: 0 (disable; default value) and 1 (enable).\n        :type KeepaliveEnable: int\n        :param EndPort: This parameter is used to specify the end port and is required when creating a port range listener. Only one member can be passed in when inputting the `Ports` parameter, which is used to specify the start port. If you want to try the port range feature, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).\n        :type EndPort: int\n        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.\n        :type DeregisterTargetRst: bool\n        """
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
        """
        :param ListenerIds: Array of unique IDs of the created listeners\n        :type ListenerIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.\n        :type LoadBalancerType: str\n        :param Forward: CLB instance type. Valid value: 1 (generic CLB instance).\n        :type Forward: int\n        :param LoadBalancerName: CLB instance name, which takes effect only when only one instance is to be created in the request. It can consist 1 to 60 letters, digits, hyphens (-), or underscores (_).
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.\n        :type LoadBalancerName: str\n        :param VpcId: Network ID of the backend target server of CLB, which can be obtained through the DescribeVpcEx API. If this parameter is not passed in, it will default to a basic network ("0").\n        :type VpcId: str\n        :param SubnetId: A subnet ID must be specified when you purchase a private network CLB instance in a VPC, and the VIP of this instance will be generated in this subnet.\n        :type SubnetId: str\n        :param ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API. If this parameter is not passed in, the default project will be used.\n        :type ProjectId: int\n        :param AddressIPVersion: IP version. Valid values: IPv4, IPv6, IPv6FullChain. Default value: IPv4. This parameter is applicable only to public network CLB instances.\n        :type AddressIPVersion: str\n        :param Number: Number of CLBs to be created. Default value: 1.\n        :type Number: int\n        :param MasterZoneId: Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1, which is applicable only to public network CLB.
Note: A primary AZ carries traffic, while a secondary AZ does not carry traffic by default and will be used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. The list of primary AZs in a specific region can be queried through the DescribeMasterZones API.\n        :type MasterZoneId: str\n        :param ZoneId: Specifies an AZ ID for creating a CLB instance, such as `ap-guangzhou-1`, which is applicable only to public network CLB instances.\n        :type ZoneId: str\n        :param InternetAccessible: CLB network billing mode. This parameter is applicable only to public network CLB instances.\n        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`\n        :param VipIsp: This parameter is applicable only to public network CLB instances. Valid values: CMCC (China Mobile), CTCC (China Telecom), CUCC (China Unicom). If this parameter is not specified, BGP will be used by default. ISPs supported in a region can be queried with the `DescribeSingleIsp` API. If an ISP is specified, only bill-by-bandwidth-package (BANDWIDTH_PACKAGE) can be used as the network billing mode.\n        :type VipIsp: str\n        :param Tags: Tags a CLB instance when purchasing it\n        :type Tags: list of TagInfo\n        :param Vip: Applies for CLB instances for a specified VIP\n        :type Vip: str\n        :param BandwidthPackageId: Bandwidth package ID. If this parameter is specified, the network billing mode (`InternetAccessible.InternetChargeType`) will only support bill-by-bandwidth package (`BANDWIDTH_PACKAGE`).\n        :type BandwidthPackageId: str\n        :param ExclusiveCluster: Dedicated cluster information\n        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`\n        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\n        :type ClientToken: str\n        :param SnatPro: Whether Binding IPs of other VPCs feature switch\n        :type SnatPro: bool\n        :param SnatIps: Creates `SnatIp` when the binding IPs of other VPCs feature is enabled\n        :type SnatIps: list of SnatIp\n        :param ClusterTag: Tag for the STGW exclusive cluster.\n        :type ClusterTag: str\n        :param SlaveZoneId: Sets the secondary AZ ID for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`, which is applicable only to public network CLB instances.
Note: A secondary AZ will load traffic if the primary AZ has failures. The API `DescribeMasterZones` is used to query the primary and secondary AZ list of a region.\n        :type SlaveZoneId: str\n        :param EipAddressId: Unique ID of an EIP, which can only be used when binding the EIP of a private network CLB instance. E.g., `eip-11112222`.\n        :type EipAddressId: str\n        """
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
        """
        :param LoadBalancerIds: Array of unique CLB instance IDs.\n        :type LoadBalancerIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.\n        :type LoadBalancerId: str\n        :param SnatIps: Information of the SNAT IP to be added. You can apply for a specified IP or apply for an automatically assigned IP by specifying a subnet.\n        :type SnatIps: list of SnatIp\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: Listener ID\n        :type ListenerId: str\n        :param Rules: Information of the new forwarding rule\n        :type Rules: list of RuleInput\n        """
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
        """
        :param LocationIds: Array of unique IDs of created forwarding rules\n        :type LocationIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LocationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocationIds = params.get("LocationIds")
        self.RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup request structure.

    """

    def __init__(self):
        """
        :param TargetGroupName: Target group name (up to 50 characters)\n        :type TargetGroupName: str\n        :param VpcId: `vpcid` attribute of a target group. If this parameter is left empty, the default VPC will be used.\n        :type VpcId: str\n        :param Port: Default port of a target group, which can be used for subsequently added servers.\n        :type Port: int\n        :param TargetGroupInstances: Real server bound to a target group\n        :type TargetGroupInstances: list of TargetGroupInstance\n        """
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
        """
        :param TargetGroupId: ID generated after target group creation\n        :type TargetGroupId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TargetGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        """
        :param TopicName: Log topic name\n        :type TopicName: str\n        :param PartitionCount: The number of topic partitions, which changes as partitions are split or merged. Each log topic can have up to 50 partitions. If this parameter is not passed in, 1 partition will be created by default and up to 10 partitions are allowed to be created.\n        :type PartitionCount: int\n        :param TopicType: Log type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).\n        :type TopicType: str\n        """
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
        """
        :param TopicId: Log topic ID\n        :type TopicId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: ID of the listener to be deleted\n        :type ListenerId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerIds: Array of IDs of the listeners to be deleted. If this parameter is left empty, all listeners of the CLB instance will be deleted.\n        :type ListenerIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerIds: Array of IDs of the CLB instances to be deleted. Array length limit: 20.\n        :type LoadBalancerIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.\n        :type LoadBalancerId: str\n        :param Ips: Array of the SNAT IP addresses to be deleted\n        :type Ips: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param SourceListenerId: Source listener ID\n        :type SourceListenerId: str\n        :param TargetListenerId: Target listener ID\n        :type TargetListenerId: str\n        :param RewriteInfos: Redirection relationship between forwarding rules\n        :type RewriteInfos: list of RewriteLocationMap\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param LocationIds: Array of IDs of the forwarding rules to be deleted\n        :type LocationIds: list of str\n        :param Domain: Domain name of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified.\n        :type Domain: str\n        :param Url: Forwarding path of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified.\n        :type Url: str\n        :param NewDefaultServerDomain: A listener must be configured with a default domain name. If you need to delete the default domain name, you can specify another one as the new default domain name.\n        :type NewDefaultServerDomain: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups request structure.

    """

    def __init__(self):
        """
        :param TargetGroupIds: Target group ID array\n        :type TargetGroupIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances request structure.

    """

    def __init__(self):
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupInstances: Information of server to be unbound\n        :type TargetGroupInstances: list of TargetGroupInstance\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param InstanceIds: List of real server IDs\n        :type InstanceIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID in the format of "lb-12345678"\n        :type LoadBalancerId: str\n        :param ListenerId: Listener ID in the format of "lbl-12345678"\n        :type ListenerId: str\n        :param Targets: List of real servers to be unbound. Array length limit: 20.\n        :type Targets: list of Target\n        :param LocationId: Forwarding rule ID in the format of "loc-12345678". When unbinding a server from a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.\n        :type LocationId: str\n        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.\n        :type Domain: str\n        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.\n        :type Url: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID.\n        :type LoadBalancerId: str\n        :param Offset: Data offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Maximum number of IPs to be returned. Default value: 100,000.\n        :type Limit: int\n        """
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
        """
        :param BlockedIPCount: Number of returned IPs\n        :type BlockedIPCount: int\n        :param ClientIPField: Field for getting real client IP\n        :type ClientIPField: str\n        :param BlockedIPList: List of IPs added to blocklist 12360\n        :type BlockedIPList: list of BlockedIP\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TaskId: Async task ID returned by the `ModifyBlockIPList` API\n        :type TaskId: str\n        """
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
        """
        :param Status: 1: running; 2: failed; 6: succeeded\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of real server IDs\n        :type InstanceIds: list of str\n        """
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
        """
        :param LoadBalancerInfoList: CLB information list\n        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        """
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
        """
        :param HealthList: List of real server health statuses
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type HealthList: list of ClassicalHealth\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerIds: List of CLB listener IDs\n        :type ListenerIds: list of str\n        :param Protocol: CLB listening protocol. Valid values: TCP, UDP, HTTP, and HTTPS.\n        :type Protocol: str\n        :param ListenerPort: CLB listening port. Value range: 1 - 65535.\n        :type ListenerPort: int\n        :param Status: Listener status. Valid values: 0 (creating) and 1 (running).\n        :type Status: int\n        """
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
        """
        :param Listeners: Listener list
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Listeners: list of ClassicalListener\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        """
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
        """
        :param Targets: Real server list
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Targets: list of ClassicalTarget\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LogsetId: Logset ID\n        :type LogsetId: str\n        :param HealthLogsetId: Health check logset ID\n        :type HealthLogsetId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LogsetId = None
        self.HealthLogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.HealthLogsetId = params.get("HealthLogsetId")
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerIds: Array of IDs of the CLB listeners to be queried\n        :type ListenerIds: list of str\n        :param Protocol: Type of the listener protocols to be queried. Valid values: TCP, UDP, HTTP, HTTPS, and TCP_SSL.\n        :type Protocol: str\n        :param Port: Port of the listeners to be queried\n        :type Port: int\n        """
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
        """
        :param Listeners: Listener list\n        :type Listeners: list of Listener\n        :param TotalCount: Total number of listeners (with filters of port, protocol, and listener ID applied).
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertIds: Server or client certificate ID\n        :type CertIds: list of str\n        """
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
        """
        :param CertSet: Certificate ID and list of CLB instances associated with it\n        :type CertSet: list of CertIdRelatedWithLoadBalancers\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerRegion: CLB instance region. If this parameter is not passed in, CLB instances in all regions will be returned.\n        :type LoadBalancerRegion: str\n        """
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
        """
        :param LoadBalancerTraffic: Information of CLB instances sorted by outbound bandwidth from highest to lowest
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type LoadBalancerTraffic: list of LoadBalancerTraffic\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Limit: Number of CLB instance lists returned. Default value: 20; maximum value: 100.\n        :type Limit: int\n        :param Offset: Starting offset of the CLB instance list returned. Default value: 0.\n        :type Offset: int\n        :param Fields: List of fields to be returned. The `LoadBalancerId` and `LoadBalancerName` are returned by default.\n        :type Fields: list of str\n        :param TargetType: Target type. Valid values: NODE and GROUP. If the list of fields contains `TargetId`, `TargetAddress`, `TargetPort`, `TargetWeight` and other fields, `Target` of the target group or non-target group must be exported.\n        :type TargetType: str\n        :param Filters: Filter condition of querying lists describing CLB instance details:
<li> loadbalancer-id - String - Required: no - (Filter condition) CLB instance ID, such as "lb-12345678". </li>
<li> project-id - String - Required: no - (Filter condition) Project ID, such as "0" and "123".</li>
<li> network - String - Required: no - (Filter condition) Network type of the CLB instance, such as "Public" and "Private".</li>
<li> vip - String - Required: no - (Filter condition) CLB instance VIP, such as "1.1.1.1" and "2204::22:3". </li>
<li> target-ip - String - Required: no - (Filter condition) Private IP of the target real servers, such as"1.1.1.1" and "2203::214:4".</li>
<li> vpcid - String - Required: no - (Filter condition) Identifier of the VPC instance to which the CLB instance belongs, such as "vpc-12345678".</li>
<li> zone - String - Required: no - (Filter condition) Availability zone where the CLB instance resides, such as "ap-guangzhou-1".</li>
<li> tag-key - String - Required: no - (Filter condition) Tag key of the CLB instance, such as "name".</li>
<li> tag:* - String - Required: no - (Filter condition) CLB instance tag, followed by tag key after the colon ':'. For example, use {"Name": "tag:name","Values": ["zhangsan", "lisi"]} to filter the tag key “name” with the tag value “zhangsan” and “lisi”.</li>
<li> fuzzy-search - String - Required: no - (Filter condition) Fuzzy search for CLB instance VIP and CLB instance name, such as "1.1".</li>\n        :type Filters: list of Filter\n        """
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
        """
        :param TotalCount: Total number of lists describing CLB instance details.\n        :type TotalCount: int\n        :param LoadBalancerDetailSet: List of CLB instance details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerDetailSet: list of LoadBalancerDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerIds: CLB instance ID\n        :type LoadBalancerIds: list of str\n        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.\n        :type LoadBalancerType: str\n        :param Forward: CLB instance type. 1: generic CLB instance; 0: classic CLB instance\n        :type Forward: int\n        :param LoadBalancerName: CLB instance name.\n        :type LoadBalancerName: str\n        :param Domain: Domain name assigned to a CLB instance by Tencent Cloud. This parameter is meaningful only for the public network classic CLB.\n        :type Domain: str\n        :param LoadBalancerVips: VIP address of a CLB instance (there can be multiple addresses)\n        :type LoadBalancerVips: list of str\n        :param BackendPublicIps: Public IP of the real server bound to a CLB.\n        :type BackendPublicIps: list of str\n        :param BackendPrivateIps: Private IP of the real server bound to a CLB.\n        :type BackendPrivateIps: list of str\n        :param Offset: Data offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param OrderBy: Sort by parameter. Value range: LoadBalancerName, CreateTime, Domain, LoadBalancerType.\n        :type OrderBy: str\n        :param OrderType: 1: reverse; 0: sequential. Default value: reverse by creation time |\n        :type OrderType: int\n        :param SearchKey: Search field which fuzzy matches name, domain name, or VIP.\n        :type SearchKey: str\n        :param ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API.\n        :type ProjectId: int\n        :param WithRs: Whether a CLB instance is bound to a real server. 0: no; 1: yes; -1: query all.\n        :type WithRs: int\n        :param VpcId: VPC where a CLB instance resides, such as vpc-bhqkbhdx.
Basic network does not support queries by VpcId.\n        :type VpcId: str\n        :param SecurityGroup: Security group ID, e.g., `sg-m1cc****`.\n        :type SecurityGroup: str\n        :param MasterZone: Primary AZ ID, e.g., `100001` (Guangzhou Zone 1).\n        :type MasterZone: str\n        :param Filters: Each request can have up to 10 `Filters` and 100 `Filter.Values`. Detailed filter conditions:
<li> internet-charge-type - Type: String - Required: No - Filter by CLB network billing mode, including `TRAFFIC_POSTPAID_BY_HOUR`</li>\n        :type Filters: list of Filter\n        """
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
        """
        :param TotalCount: Total number of CLB instances that meet the filter criteria. This value is independent of the Limit in the input parameter.\n        :type TotalCount: int\n        :param LoadBalancerSet: Array of returned CLB instances.\n        :type LoadBalancerSet: list of LoadBalancer\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param QuotaSet: Quota list\n        :type QuotaSet: list of Quota\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param SourceListenerIds: Array of CLB listener IDs\n        :type SourceListenerIds: list of str\n        :param SourceLocationIds: Array of CLB forwarding rule IDs\n        :type SourceLocationIds: list of str\n        """
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
        """
        :param RewriteSet: Array of redirection forwarding rules. If there are no redirection rules, an empty array will be returned.\n        :type RewriteSet: list of RuleOutput\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Filters: Filter. Currently, only filtering by `TargetGroupId`, `BindIP`, or `InstanceId` is supported.\n        :type Filters: list of Filter\n        :param Limit: Number of displayed results. Default value: 20\n        :type Limit: int\n        :param Offset: Display offset. Default value: 0\n        :type Offset: int\n        """
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
        """
        :param TotalCount: Number of results in current query\n        :type TotalCount: int\n        :param TargetGroupInstanceSet: Information of the bound server\n        :type TargetGroupInstanceSet: list of TargetGroupBackend\n        :param RealCount: Actual statistics, which are not affected by `Limit`, `Offset`, and `CAM`.\n        :type RealCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TargetGroupIds: Target group ID array\n        :type TargetGroupIds: list of str\n        :param Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`. Target group ID will be used first.\n        :type Filters: list of Filter\n        :param Offset: Starting display offset\n        :type Offset: int\n        :param Limit: Limit of the number of displayed results. Default value: 20.\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of displayed results\n        :type TotalCount: int\n        :param TargetGroupSet: Information set of displayed target groups\n        :type TargetGroupSet: list of TargetGroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TargetGroupIds: Target group ID, which is exclusive of `Filters`.\n        :type TargetGroupIds: list of str\n        :param Limit: Limit of the number of displayed results. Default value: 20.\n        :type Limit: int\n        :param Offset: Starting display offset\n        :type Offset: int\n        :param Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`.\n        :type Filters: list of Filter\n        """
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
        """
        :param TotalCount: Number of displayed results\n        :type TotalCount: int\n        :param TargetGroupSet: Information set of displayed target groups\n        :type TargetGroupSet: list of TargetGroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerIds: List of IDs of CLB instances to be queried\n        :type LoadBalancerIds: list of str\n        """
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
        """
        :param LoadBalancers: CLB instance list
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type LoadBalancers: list of LoadBalancerHealth\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerIds: Listener ID list\n        :type ListenerIds: list of str\n        :param Protocol: Listener protocol type\n        :type Protocol: str\n        :param Port: Listener port\n        :type Port: int\n        """
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
        """
        :param Listeners: Information of real servers bound to the listener
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Listeners: list of ListenerBackend\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TaskId: Request ID, i.e., the RequestId parameter returned by the API.\n        :type TaskId: str\n        """
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
        """
        :param Status: Current status of a task. Value range: 0 (succeeded), 1 (failed), 2 (in progress).\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups request structure.

    """

    def __init__(self):
        """
        :param Associations: Array of rules to be unbound\n        :type Associations: list of TargetGroupAssociation\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExclusiveCluster(AbstractModel):
    """Dedicated cluster

    """

    def __init__(self):
        """
        :param L4Clusters: Layer-4 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type L4Clusters: list of ClusterItem\n        :param L7Clusters: Layer-7 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type L7Clusters: list of ClusterItem\n        :param ClassicalCluster: vpcgw cluster
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`\n        """
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
        """
        :param ZhiTong: Whether to enable VIP direct connection
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ZhiTong: bool\n        :param TgwGroupName: TgwGroup name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TgwGroupName: str\n        """
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
        """
        :param Name: Filter name\n        :type Name: str\n        :param Values: Filter value array\n        :type Values: list of str\n        """
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
        """
        :param HealthSwitch: Whether to enable health check. 1: enable; 0: disable.\n        :type HealthSwitch: int\n        :param TimeOut: Health check response timeout period in seconds (applicable only to layer-4 listeners). Value range: 2-60. Default value: 2. This parameter should be less than the check interval.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TimeOut: int\n        :param IntervalTime: Health check interval in seconds. Value range: 5-300. Default value: 5.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type IntervalTime: int\n        :param HealthNum: Health threshold. Default value: 3, indicating that if a forward is found healthy three consecutive times, it is considered to be normal. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HealthNum: int\n        :param UnHealthNum: Unhealthy threshold. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it is considered to be exceptional. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.\n        :type UnHealthNum: int\n        :param HttpCode: Health check status code (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: 1-31. Default value: 31.
1 means that the return value of 1xx after detection means healthy, 2 for returning 2xx for healthy, 4 for returning 3xx for healthy, 8 for returning 4xx for healthy, and 16 for returning 5xx for healthy. If you want multiple return codes to represent healthy, sum up the corresponding values. Note: The HTTP health check mode of TCP listeners only supports specifying one kind of health check status code.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HttpCode: int\n        :param HttpCheckPath: Health check path (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners).
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HttpCheckPath: str\n        :param HttpCheckDomain: Health check domain name (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners).
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HttpCheckDomain: str\n        :param HttpCheckMethod: Health check method (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: HEAD, GET. Default value: HEAD.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HttpCheckMethod: str\n        :param CheckPort: Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, it is recommended to leave it empty. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CheckPort: int\n        :param ContextType: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the input format of the health check. Value range: HEX, TEXT. If the value is HEX, the characters of SendContext and RecvContext can only be selected from 0123456789ABCDEF and the length must be an even number. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ContextType: str\n        :param SendContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the content of the request sent by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SendContext: str\n        :param RecvContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the result returned by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RecvContext: str\n        :param CheckType: Health check protocol (a custom check parameter). Value range: TCP, HTTP, CUSTOM (applicable only to TCP/UDP listeners, where UDP listeners only support CUSTOM. If custom health check is used, this parameter is required).
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CheckType: str\n        :param HttpVersion: Health check protocol (a custom check parameter), which is required if the value of CheckType is HTTP. This parameter represents the HTTP version of the real server. Value range: HTTP/1.0, HTTP/1.1. (Applicable only to TCP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HttpVersion: str\n        """
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
        """
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR: hourly pay-as-you-go by traffic; BANDWIDTH_POSTPAID_BY_HOUR: hourly pay-as-you-go by bandwidth;
BANDWIDTH_PACKAGE: billed by bandwidth package (currently, this method is supported only if the ISP is specified)\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: Maximum outbound bandwidth in Mbps, which applies only to public network CLB. Value range: 0-65,535. Default value: 10.\n        :type InternetMaxBandwidthOut: int\n        :param BandwidthpkgSubType: Bandwidth package type, such as SINGLEISP
Note: This field may return null, indicating that no valid values can be obtained.\n        :type BandwidthpkgSubType: str\n        """
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
        """
        :param RenewFlag: Renewal type. AUTO_RENEW: automatic renewal; MANUAL_RENEW: manual renewal
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RenewFlag: str\n        :param Period: Cycle, indicating the number of months (reserved field)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Period: int\n        """
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
        """
        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Protocol: Listener protocol\n        :type Protocol: str\n        :param Port: Listener port\n        :type Port: int\n        :param Certificate: Information of certificates bound to the listener
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`\n        :param HealthCheck: Health check information of the listener
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Scheduler: Request scheduling method
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Scheduler: str\n        :param SessionExpireTime: Session persistence time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SessionExpireTime: int\n        :param SniSwitch: Whether to enable the SNI feature (this parameter is only meaningful for HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SniSwitch: int\n        :param Rules: All forwarding rules under a listener (this parameter is meaningful only for HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Rules: list of RuleOutput\n        :param ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ListenerName: str\n        :param CreateTime: Listener creation time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param EndPort: End port of a port range
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EndPort: int\n        :param TargetType: Real server type
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetType: str\n        :param TargetGroup: Basic information of a bound target group. This field will be returned when a target group is bound to a listener.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`\n        :param SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionType: str\n        :param KeepaliveEnable: Whether a persistent connection is enabled (1: enabled; 0: disabled). This parameter can only be configured in HTTP/HTTPS listeners.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type KeepaliveEnable: int\n        :param Toa: Only the NAT64 CLB TCP listeners are supported.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Toa: bool\n        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DeregisterTargetRst: bool\n        """
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
        """
        :param ListenerId: Listener ID\n        :type ListenerId: str\n        :param Protocol: Listener protocol\n        :type Protocol: str\n        :param Port: Listener port\n        :type Port: int\n        :param Rules: Information of rules under a listener (applicable only to HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Rules: list of RuleTargets\n        :param Targets: List of real servers bound to a listener (applicable only to TCP/UDP/TCP_SSL listeners)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Targets: list of Backend\n        :param EndPort: Ending port in port range if port range is supported; 0 if port range is not supported
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndPort: int\n        """
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
        """
        :param ListenerId: Listener ID\n        :type ListenerId: str\n        :param ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ListenerName: str\n        :param Protocol: Listener protocol\n        :type Protocol: str\n        :param Port: Listener port\n        :type Port: int\n        :param Rules: List of forwarding rules of the listener
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Rules: list of RuleHealth\n        """
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
        """
        :param LoadBalancerId: CLB instance ID.\n        :type LoadBalancerId: str\n        :param LoadBalancerName: CLB instance name.\n        :type LoadBalancerName: str\n        :param LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.\n        :type LoadBalancerType: str\n        :param Forward: CLB type identifier. Value range: 1 (CLB); 0 (classic CLB).\n        :type Forward: int\n        :param Domain: CLB instance domain name. This field is provided only to public network classic CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param LoadBalancerVips: List of VIPs of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerVips: list of str\n        :param Status: CLB instance status, including:
0: creating; 1: running.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param CreateTime: CLB instance creation time.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param StatusTime: Last status change time of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StatusTime: str\n        :param ProjectId: ID of the project to which a CLB instance belongs. 0: default project.\n        :type ProjectId: int\n        :param VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.\n        :type VpcId: str\n        :param OpenBgp: Protective CLB identifier. Value range: 1 (protective), 0 (non-protective).
Note: This field may return null, indicating that no valid values can be obtained.\n        :type OpenBgp: int\n        :param Snat: SNAT is enabled for all private network classic CLB created before December 2016.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Snat: bool\n        :param Isolation: 0: not isolated; 1: isolated.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Isolation: int\n        :param Log: Log information. Only the public network CLB that have HTTP or HTTPS listeners can generate logs.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Log: str\n        :param SubnetId: Subnet where a CLB instance resides (meaningful only for private network VPC CLB)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SubnetId: str\n        :param Tags: CLB instance tag information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of TagInfo\n        :param SecureGroups: Security group of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SecureGroups: list of str\n        :param TargetRegionInfo: Basic information of a backend server bound to a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`\n        :param AnycastZone: Anycast CLB publishing region. For non-anycast CLB, this field returns an empty string.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type AnycastZone: str\n        :param AddressIPVersion: IP version. Valid values: ipv4, ipv6
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddressIPVersion: str\n        :param NumericalVpcId: VPC ID in a numeric form
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NumericalVpcId: int\n        :param VipIsp: ISP to which a CLB IP address belongs
Note: This field may return null, indicating that no valid values can be obtained.\n        :type VipIsp: str\n        :param MasterZone: Primary AZ
Note: This field may return null, indicating that no valid values can be obtained.\n        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`\n        :param BackupZoneSet: Secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.\n        :type BackupZoneSet: list of ZoneInfo\n        :param IsolatedTime: CLB instance isolation time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type IsolatedTime: str\n        :param ExpireTime: CLB instance expiration time, which takes effect only for prepaid instances
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param ChargeType: Billing mode of CLB instance. Valid values: PREPAID (monthly subscription), POSTPAID_BY_HOUR (pay as you go).
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ChargeType: str\n        :param NetworkAttributes: CLB instance network attributes
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`\n        :param PrepaidAttributes: Prepaid billing attributes of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`\n        :param LogSetId: Logset ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LogSetId: str\n        :param LogTopicId: Log topic ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LogTopicId: str\n        :param AddressIPv6: IPv6 address of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.\n        :type AddressIPv6: str\n        :param ExtraInfo: Reserved field which can be ignored generally.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`\n        :param IsDDos: Whether an Anti-DDoS Pro instance can be bound
Note: This field may return null, indicating that no valid values can be obtained.\n        :type IsDDos: bool\n        :param ConfigId: Custom configuration ID at the CLB instance level
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ConfigId: str\n        :param LoadBalancerPassToTarget: Whether a real server opens the traffic from a CLB instance to the internet
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerPassToTarget: bool\n        :param ExclusiveCluster: Private network dedicated cluster
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`\n        :param IPv6Mode: This field is meaningful only when the IP address version is `ipv6`. Valid values: IPv6Nat64, IPv6FullChain
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IPv6Mode: str\n        :param SnatPro: Whether to enable SnatPro.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnatPro: bool\n        :param SnatIps: `SnatIp` list after SnatPro load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnatIps: list of SnatIp\n        :param SlaType: Performance guarantee specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SlaType: str\n        :param IsBlock: Whether VIP is blocked
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsBlock: bool\n        :param IsBlockTime: Time blocked or unblocked
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsBlockTime: str\n        :param LocalBgp: Whether the IP type is the local BGP\n        :type LocalBgp: bool\n        :param ClusterTag: Dedicated layer-7 tag.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterTag: str\n        :param MixIpTarget: If the layer-7 listener of an IPv6FullChain CLB instance is enabled, the CLB instance can be bound with an IPv4 and an IPv6 CVM instance simultaneously.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MixIpTarget: bool\n        :param Zones: Availability zone of a VPC-based private network CLB instance
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Zones: list of str\n        :param NfvInfo: Whether it is an NFV CLB instance. No returned information: no; l7nfv: yes.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type NfvInfo: str\n        :param HealthLogSetId: Health check logset ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type HealthLogSetId: str\n        :param HealthLogTopicId: Health check log topic ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type HealthLogTopicId: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID.\n        :type LoadBalancerId: str\n        :param LoadBalancerName: CLB instance name.\n        :type LoadBalancerName: str\n        :param LoadBalancerType: CLB instance network type:
Public: public network; Private: private network.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerType: str\n        :param Status: CLB instance status, including:
0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param Address: CLB instance VIP.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Address: str\n        :param AddressIPv6: IPv6 VIP address of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddressIPv6: str\n        :param AddressIPVersion: IP version of the CLB instance. Valid values: IPv4, IPv6.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddressIPVersion: str\n        :param IPv6Mode: IPv6 address type of the CLB instance. Valid values: IPv6Nat64, IPv6FullChain.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IPv6Mode: str\n        :param Zone: Availability zone where the CLB instance resides.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Zone: str\n        :param AddressIsp: ISP to which the CLB IP address belongs.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddressIsp: str\n        :param VpcId: ID of the VPC instance to which the CLB instance belongs.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VpcId: str\n        :param ProjectId: ID of the project to which the CLB instance belongs. 0: default project.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: int\n        :param CreateTime: CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param ChargeType: CLB instance billing mode.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeType: str\n        :param NetworkAttributes: CLB instance network attribute.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`\n        :param PrepaidAttributes: Pay-as-you-go attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`\n        :param ExtraInfo: Reserved field, which can be ignored generally.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`\n        :param ConfigId: Custom configuration ID at the CLB instance level.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConfigId: str\n        :param Tags: CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of TagInfo\n        :param ListenerId: CLB listener ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ListenerId: str\n        :param Protocol: Listener protocol.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param Port: Listener port.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Port: int\n        :param LocationId: Forwarding rule ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LocationId: str\n        :param Domain: Domain name of the forwarding rule.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Url: Forwarding rule path.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param TargetId: ID of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TargetId: str\n        :param TargetAddress: Address of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TargetAddress: str\n        :param TargetPort: Listening port of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TargetPort: int\n        :param TargetWeight: Forwarding weight of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TargetWeight: int\n        :param Isolation: 0: not isolated; 1: isolated.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Isolation: int\n        :param SecurityGroup: List of the security groups bound to the CLB instance.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SecurityGroup: list of str\n        :param LoadBalancerPassToTarget: Whether the CLB instance is billed by IP.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type LoadBalancerPassToTarget: int\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param LoadBalancerName: CLB instance name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LoadBalancerName: str\n        :param Listeners: List of listeners
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Listeners: list of ListenerHealth\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param LoadBalancerName: CLB instance name\n        :type LoadBalancerName: str\n        :param Region: CLB instance region\n        :type Region: str\n        :param Vip: CLB instance VIP\n        :type Vip: str\n        :param OutBandwidth: Maximum outbound bandwidth in Mbps\n        :type OutBandwidth: float\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param SourceListenerId: Source listener ID\n        :type SourceListenerId: str\n        :param TargetListenerId: Target listener ID\n        :type TargetListenerId: str\n        :param RewriteInfos: Redirection relationship between forwarding rules\n        :type RewriteInfos: list of RewriteLocationMap\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerIds: CLB instance ID\n        :type LoadBalancerIds: list of str\n        :param Type: Operation type. Valid values:
<li> add_customized_field (sets header initially to enable the blocklist feature)</li>
<li> set_customized_field (modifies header)</li>
<li> del_customized_field (deletes header)</li>
<li> add_blocked (adds IPs to blocklist)</li>
<li> del_blocked (deletes IPs from blocklist)</li>
<li> flush_blocked (clears blocklist)</li>\n        :type Type: str\n        :param ClientIPField: Header field that stores real client IPs\n        :type ClientIPField: str\n        :param BlockIPList: List of blocked IPs. The array can contain up to 200,000 entries in one operation.\n        :type BlockIPList: list of str\n        :param ExpireTime: Expiration time in seconds. Default value: 3600\n        :type ExpireTime: int\n        :param AddStrategy: IP adding policy. Valid value: fifo (if a blocklist is full, new IPs added to the blocklist will adopt the first-in first-out policy)\n        :type AddStrategy: str\n        """
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
        """
        :param JodId: Async task ID\n        :type JodId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.JodId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JodId = params.get("JodId")
        self.RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Domain: Domain name, which must be under a created forwarding rule.\n        :type Domain: str\n        :param NewDomain: New domain name\n        :type NewDomain: str\n        :param Certificate: Domain name certificate information. Note: This is only applicable to SNI-enabled listeners.\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`\n        :param Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.\n        :type Http2: bool\n        :param DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.\n        :type DefaultServer: bool\n        :param NewDefaultServerDomain: A listener must be configured with a default domain name. If you need to disable the default domain name, you must specify another one as the new default domain name.\n        :type NewDefaultServerDomain: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Domain: Legacy domain name under a listener.\n        :type Domain: str\n        :param NewDomain: New domain name. 	Length limit: 1-120. There are three usage formats: non-regular expression, wildcard, and regular expression. A non-regular expression can only contain letters, digits, "-", and ".". In a wildcard, "*" can only be at the beginning or the end. A regular expressions must begin with a "~".\n        :type NewDomain: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param ListenerName: New listener name\n        :type ListenerName: str\n        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.\n        :type SessionExpireTime: int\n        :param HealthCheck: Health check parameter, which is applicable only to TCP, UDP, and TCP_SSL listeners.\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Certificate: Certificate information. This parameter is applicable only to HTTPS and TCP_SSL listeners.\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`\n        :param Scheduler: Forwarding method of a listener. Value range: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.\n        :type Scheduler: str\n        :param SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners. Note: The SNI feature can be enabled but cannot be disabled once enabled.\n        :type SniSwitch: int\n        :param KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners.\n        :type KeepaliveEnable: int\n        :param DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.\n        :type DeregisterTargetRst: bool\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: Unique CLB ID\n        :type LoadBalancerId: str\n        :param LoadBalancerName: CLB instance name\n        :type LoadBalancerName: str\n        :param TargetRegionInfo: Region information of the real server bound to a CLB.\n        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`\n        :param InternetChargeInfo: Network billing parameter\n        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`\n        :param LoadBalancerPassToTarget: Whether the target opens traffic from CLB to the internet. If yes (true), only security groups on CLB will be verified; if no (false), security groups on both CLB and backend instance need to be verified.\n        :type LoadBalancerPassToTarget: bool\n        :param SnatPro: Whether to enable SnatPro\n        :type SnatPro: bool\n        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None
        self.SnatPro = None


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
        """
        :param DealName: This parameter can be used to query whether CLB billing mode switch is successful.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param LocationId: ID of the forwarding rule to be modified.\n        :type LocationId: str\n        :param Url: New forwarding path of the forwarding rule. This parameter is not required if the URL does not need to be modified.\n        :type Url: str\n        :param HealthCheck: Health check information\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.\n        :type Scheduler: str\n        :param SessionExpireTime: Session persistence time\n        :type SessionExpireTime: int\n        :param ForwardType: Forwarding protocol between CLB instance and real server. Default value: HTTP. Valid values: HTTP, HTTPS, and TRPC.\n        :type ForwardType: str\n        :param TrpcCallee: TRPC callee server route, which is required when `ForwardType` is "TRPC".\n        :type TrpcCallee: str\n        :param TrpcFunc: TRPC calling service API, which is required when `ForwardType` is "TRPC".\n        :type TrpcFunc: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupName: New name of target group\n        :type TargetGroupName: str\n        :param Port: New default port of target group\n        :type Port: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort request structure.

    """

    def __init__(self):
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupInstances: Array of servers for which to modify ports\n        :type TargetGroupInstances: list of TargetGroupInstance\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight request structure.

    """

    def __init__(self):
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupInstances: Array of servers for which to modify weights\n        :type TargetGroupInstances: list of TargetGroupInstance\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Targets: List of real servers for which to modify the ports\n        :type Targets: list of Target\n        :param NewPort: New port of the real server bound to a listener or forwarding rule\n        :type NewPort: int\n        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.\n        :type LocationId: str\n        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.\n        :type Domain: str\n        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.\n        :type Url: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.\n        :type LocationId: str\n        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.\n        :type Domain: str\n        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified.\n        :type Url: str\n        :param Targets: List of real servers for which to modify the weights\n        :type Targets: list of Target\n        :param Weight: New forwarding weight of a real server. Value range: 0-100. Default value: 10. If the Targets.Weight parameter is set, this parameter will not take effect.\n        :type Weight: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """Quota description. All quotas are in the current region.

    """

    def __init__(self):
        """
        :param QuotaId: Quota name. Valid values:
<li> TOTAL_OPEN_CLB_QUOTA: quota of public network CLB instances in the current region</li>
<li> TOTAL_INTERNAL_CLB_QUOTA: quota of private network CLB instances in the current region</li>
<li> TOTAL_LISTENER_QUOTA: quota of listeners under one CLB instance</li>
<li> TOTAL_LISTENER_RULE_QUOTA: quota of forwarding rules under one listener</li>
<li> TOTAL_TARGET_BIND_QUOTA: quota of CVM instances can be bound under one forwarding rule</li>\n        :type QuotaId: str\n        :param QuotaCurrent: Currently used quantity. If it is `null`, it is meaningless.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type QuotaCurrent: int\n        :param QuotaLimit: Quota limit.\n        :type QuotaLimit: int\n        """
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
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param TargetGroupInstances: Server instance array\n        :type TargetGroupInstances: list of TargetGroupInstance\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Targets: List of real servers to be bound. Array length limit: 20.\n        :type Targets: list of Target\n        :param LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.\n        :type LocationId: str\n        :param Domain: Target forwarding rule domain name. This parameter does not take effect if LocationId is specified.\n        :type Domain: str\n        :param Url: Target forwarding rule URL. This parameter does not take effect if LocationId is specified.\n        :type Url: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param Targets: Real server information\n        :type Targets: list of ClassicalTargetInfo\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers request structure.

    """

    def __init__(self):
        """
        :param OldCertificateId: ID of the certificate to be replaced, which can be a server certificate or a client certificate.\n        :type OldCertificateId: str\n        :param Certificate: Information such as the content of the new certificate\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RewriteLocationMap(AbstractModel):
    """Redirection relationship between forwarding rules

    """

    def __init__(self):
        """
        :param SourceLocationId: Source forwarding rule ID\n        :type SourceLocationId: str\n        :param TargetLocationId: Forwarding rule ID of a redirect target\n        :type TargetLocationId: str\n        :param RewriteCode: Redirection status code. Valid values: 301, 302, and 307.\n        :type RewriteCode: int\n        :param TakeUrl: Whether the matched URL is carried in redirection. It is required when configuring `RewriteCode`.\n        :type TakeUrl: bool\n        :param SourceDomain: Original domain name of redirection, which must be the corresponding domain name of `SourceLocationId`. It is required when configuring `RewriteCode`.\n        :type SourceDomain: str\n        """
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
        """
        :param TargetListenerId: Listener ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetListenerId: str\n        :param TargetLocationId: Forwarding rule ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetLocationId: str\n        :param RewriteCode: Redirection status code
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RewriteCode: int\n        :param TakeUrl: Whether the matched URL is carried in redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TakeUrl: bool\n        :param RewriteType: Redirection type. Manual: manual redirection; Auto: automatic redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RewriteType: str\n        """
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
        """
        :param ListenerId: CLB listener ID\n        :type ListenerId: str\n        :param Targets: List of real servers for which to modify the weight\n        :type Targets: list of Target\n        :param LocationId: Forwarding rule ID\n        :type LocationId: str\n        :param Domain: Target rule domain name. This parameter does not take effect if LocationId is specified\n        :type Domain: str\n        :param Url: Target rule URL. This parameter does not take effect if LocationId is specified\n        :type Url: str\n        :param Weight: New forwarding weight of a real server. Value range: 0-100.\n        :type Weight: int\n        """
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
        """
        :param LocationId: Forwarding rule ID\n        :type LocationId: str\n        :param Domain: Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Url: Forwarding rule Url
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param Targets: Health status of the real server bound to this rule
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Targets: list of TargetHealth\n        """
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
        """
        :param Domain: Domain name of the forwarding rule. Length: 1-80.\n        :type Domain: str\n        :param Url: Forwarding rule path. Length: 1-200.\n        :type Url: str\n        :param SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. Setting it to 0 indicates that session persistence is disabled.\n        :type SessionExpireTime: int\n        :param HealthCheck: Health check information. For more information, please see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1)\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Certificate: Certificate information\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`\n        :param Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.\n        :type Scheduler: str\n        :param ForwardType: Forwarding protocol between the CLB instance and real server. Currently, HTTP/HTTPS/TRPC are supported.\n        :type ForwardType: str\n        :param DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.\n        :type DefaultServer: bool\n        :param Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.\n        :type Http2: bool\n        :param TargetType: Target real server type. NODE: binding a general node; TARGETGROUP: binding a target group.\n        :type TargetType: str\n        :param TrpcCallee: TRPC callee server route, which is required when `ForwardType` is `TRPC`.\n        :type TrpcCallee: str\n        :param TrpcFunc: TRPC calling service API, which is required when `ForwardType` is `TRPC`.\n        :type TrpcFunc: str\n        :param Quic: Whether to enable QUIC. Note: QUIC can be enabled only for HTTPS domain names\n        :type Quic: bool\n        """
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
        """
        :param LocationId: Forwarding rule ID\n        :type LocationId: str\n        :param Domain: Domain name of the forwarding rule.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Url: Forwarding rule path.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param SessionExpireTime: Session persistence time\n        :type SessionExpireTime: int\n        :param HealthCheck: Health check information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`\n        :param Certificate: Certificate information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`\n        :param Scheduler: Request forwarding method of the rule\n        :type Scheduler: str\n        :param ListenerId: ID of the listener to which the forwarding rule belongs\n        :type ListenerId: str\n        :param RewriteTarget: Redirect target information of a forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`\n        :param HttpGzip: Whether to enable gzip\n        :type HttpGzip: bool\n        :param BeAutoCreated: Whether the forwarding rule is automatically created\n        :type BeAutoCreated: bool\n        :param DefaultServer: Whether to use as the default domain name\n        :type DefaultServer: bool\n        :param Http2: Whether to enable Http2\n        :type Http2: bool\n        :param ForwardType: Forwarding protocol between CLB and real server\n        :type ForwardType: str\n        :param CreateTime: Forwarding rule creation time\n        :type CreateTime: str\n        :param TargetType: Real server type\n        :type TargetType: str\n        :param TargetGroup: Basic information of a bound target group. This field will be returned if a target group is bound to a rule.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`\n        :param WafDomainId: WAF instance ID
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WafDomainId: str\n        :param TrpcCallee: TRPC callee server route, which is valid when `ForwardType` is `TRPC`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TrpcCallee: str\n        :param TrpcFunc: TRPC calling service API, which is valid when `ForwardType` is `TRPC`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TrpcFunc: str\n        :param QuicStatus: QUIC status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type QuicStatus: str\n        """
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
        """
        :param LocationId: Forwarding rule ID\n        :type LocationId: str\n        :param Domain: Domain name of the forwarding rule\n        :type Domain: str\n        :param Url: Forwarding rule path.\n        :type Url: str\n        :param Targets: Real server information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Targets: list of Backend\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param LogSetId: CLS logset ID\n        :type LogSetId: str\n        :param LogTopicId: CLS log topic ID\n        :type LogTopicId: str\n        :param LogType: Log type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).\n        :type LogType: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param SecurityGroups: Array of security group IDs. One CLB instance can be bound to up to 50 security groups. If you want to unbind all security groups, you do not need to pass in this parameter, or you can pass in an empty array.\n        :type SecurityGroups: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers request structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group ID, such as sg-12345678\n        :type SecurityGroup: str\n        :param OperationType: ADD: bind a security group;
DEL: unbind a security group\n        :type OperationType: str\n        :param LoadBalancerIds: Array of CLB instance IDs\n        :type LoadBalancerIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnatIp(AbstractModel):
    """`SnatIp` information structure

    """

    def __init__(self):
        """
        :param SubnetId: Unique VPC subnet ID, such as `subnet-12345678`.\n        :type SubnetId: str\n        :param Ip: IP address, such as 192.168.0.1\n        :type Ip: str\n        """
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
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
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
        """
        :param Port: Listening port of a real server
Note: this parameter is required when binding a CVM or ENI.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Port: int\n        :param Type: Real server type. Value range: CVM (Cloud Virtual Machine), ENI (Elastic Network Interface). This parameter does not take effect currently as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Type: str\n        :param InstanceId: Unique ID of a CVM instance, which is required when binding a CVM instance. It can be obtained from the `InstanceId` field in the response of the `DescribeInstances` API. It indicates binding the primary IP of the primary ENI.
Note: either `InstanceId` or `EniIp` must be passed in.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.\n        :type Weight: int\n        :param EniIp: It is required when binding an IP. ENI IPs and other private IPs are supported. To bind an ENI IP, the ENI should be bound to a CVM instance before being bound to a CLB instance.
Note: either `InstanceId` or `EniIp` must be passed in. It is required when binding a dual-stack IPv6 CVM instance.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type EniIp: str\n        """
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
        """
        :param LoadBalancerId: CLB instance ID\n        :type LoadBalancerId: str\n        :param ListenerId: Listener ID\n        :type ListenerId: str\n        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param LocationId: Forwarding rule ID\n        :type LocationId: str\n        """
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
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param Type: Real server type. Valid values: CVM, ENI (coming soon)\n        :type Type: str\n        :param InstanceId: Unique real server ID\n        :type InstanceId: str\n        :param Port: Listening port of real server\n        :type Port: int\n        :param Weight: Forwarding weight of real server. Value range: [0, 100]. Default value: 10.\n        :type Weight: int\n        :param PublicIpAddresses: Public IP of real server
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PublicIpAddresses: list of str\n        :param PrivateIpAddresses: Private IP of real server
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PrivateIpAddresses: list of str\n        :param InstanceName: Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceName: str\n        :param RegisteredTime: Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegisteredTime: str\n        :param EniId: Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EniId: str\n        :param ZoneId: AZ ID of the real server
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        """
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
        """
        :param TargetGroupId: Target group ID\n        :type TargetGroupId: str\n        :param VpcId: `vpcid` of target group\n        :type VpcId: str\n        :param TargetGroupName: Target group name\n        :type TargetGroupName: str\n        :param Port: Default port of target group
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Port: int\n        :param CreatedTime: Target group creation time\n        :type CreatedTime: str\n        :param UpdatedTime: Target group modification time\n        :type UpdatedTime: str\n        :param AssociatedRule: Array of associated rules
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AssociatedRule: list of AssociationItem\n        """
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
        """
        :param BindIP: Private IP of target group instance\n        :type BindIP: str\n        :param Port: Port of target group instance\n        :type Port: int\n        :param Weight: Weight of target group instance\n        :type Weight: int\n        :param NewPort: New port of target group instance\n        :type NewPort: int\n        """
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
        """
        :param IP: Private IP of the target\n        :type IP: str\n        :param Port: Port bound to the target\n        :type Port: int\n        :param HealthStatus: Current health status. true: healthy; false: unhealthy.\n        :type HealthStatus: bool\n        :param TargetId: Instance ID of the target, such as ins-12345678\n        :type TargetId: str\n        :param HealthStatusDetial: Detailed information of the current health status. Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status.\n        :type HealthStatusDetial: str\n        """
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
        """
        :param Region: Region of the target, such as ap-guangzhou\n        :type Region: str\n        :param VpcId: Network of the target, which is in the format of vpc-abcd1234 for VPC or 0 for basic network\n        :type VpcId: str\n        """
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
        """
        :param ZoneId: Unique AZ ID in a numeric form, such as 100001
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param Zone: Unique AZ ID in a string form, such as ap-guangzhou-1
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Zone: str\n        :param ZoneName: AZ name, such as Guangzhou Zone 1
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ZoneName: str\n        :param ZoneRegion: AZ region, e.g., ap-guangzhou.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type ZoneRegion: str\n        :param LocalZone: Whether the AZ is the `LocalZone`, e.g., false.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type LocalZone: bool\n        """
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
        