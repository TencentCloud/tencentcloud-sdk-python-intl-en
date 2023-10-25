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
        :param _Associations: Association array
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups response structure.

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


class AssociationItem(AbstractModel):
    """Rule associated with target group

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: ID of associated CLB instance
        :type LoadBalancerId: str
        :param _ListenerId: ID of associated listener
        :type ListenerId: str
        :param _LocationId: ID of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocationId: str
        :param _Protocol: Protocol type of associated listener, such as HTTP or TCP
        :type Protocol: str
        :param _Port: Port of associated listener
        :type Port: int
        :param _Domain: Domain name of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: URL of associated forwarding rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Protocol = None
        self._Port = None
        self._Domain = None
        self._Url = None
        self._LoadBalancerName = None
        self._ListenerName = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

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

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._ListenerName = params.get("ListenerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: `HTTPS:443` listener ID
        :type ListenerId: str
        :param _Domains: The domain name to be redirected under the listener `HTTPS:443`. If it is left empty, all domain names under the listener `HTTPS:443` will be configured with redirects.
        :type Domains: list of str
        :param _RewriteCodes: Redirection status code. Valid values: 301, 302, and 307.
        :type RewriteCodes: list of int
        :param _TakeUrls: Whether the matched URL is carried in redirection.
        :type TakeUrls: list of bool
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domains = None
        self._RewriteCodes = None
        self._TakeUrls = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RewriteCodes(self):
        return self._RewriteCodes

    @RewriteCodes.setter
    def RewriteCodes(self, RewriteCodes):
        self._RewriteCodes = RewriteCodes

    @property
    def TakeUrls(self):
        return self._TakeUrls

    @TakeUrls.setter
    def TakeUrls(self, TakeUrls):
        self._TakeUrls = TakeUrls


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domains = params.get("Domains")
        self._RewriteCodes = params.get("RewriteCodes")
        self._TakeUrls = params.get("TakeUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite response structure.

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


class Backend(AbstractModel):
    """Details of a real server bound to a listener

    """

    def __init__(self):
        r"""
        :param _Type: Real server type. Valid values: CVM, ENI.
        :type Type: str
        :param _InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API
        :type InstanceId: str
        :param _Port: Listening port of a real server
        :type Port: int
        :param _Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param _PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param _InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _RegisteredTime: Bound time of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param _EniId: Unique ENI ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        """
        self._Type = None
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RegisteredTime = None
        self._EniId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegisteredTime(self):
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicTargetGroupInfo(AbstractModel):
    """Basic information of a target group bound to a forwarding rule or a listener

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupName: Target group name
        :type TargetGroupName: str
        """
        self._TargetGroupId = None
        self._TargetGroupName = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Targets: Unbinding targets
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: IDs of the listeners failed to unbind
        :type FailListenerIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ModifyList: List of weights to be modified in batches
        :type ModifyList: list of RsWeightRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        return self._ModifyList

    @ModifyList.setter
    def ModifyList(self, ModifyList):
        self._ModifyList = ModifyList


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self._ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self._ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight response structure.

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


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Targets: Binding target
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: IDs of the listeners failed to bind. If this is blank, all listeners are bound successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """Batch binding type

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Port: The port to Bind
        :type Port: int
        :param _InstanceId: CVM instance ID. The primary IP of the primary ENI will be bound.
        :type InstanceId: str
        :param _EniIp: It is required for binding an IP. It supports an ENI IP or any other private IP. To bind an ENI IP, the ENI should be bound to a CVM instance before being bound to a CLB instance.
Note: either `InstanceId` or `EniIp` must be passed in, which is required for binding a dual-stack IPv6 CVM instance.
        :type EniIp: str
        :param _Weight: Weight of the CVM instance. Value range: [0, 100]. If it is not specified for binding the instance, 10 will be used by default.
        :type Weight: int
        :param _LocationId: Layer-7 rule ID.
        :type LocationId: str
        """
        self._ListenerId = None
        self._Port = None
        self._InstanceId = None
        self._EniIp = None
        self._Weight = None
        self._LocationId = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EniIp(self):
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._EniIp = params.get("EniIp")
        self._Weight = params.get("Weight")
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDetailItem(AbstractModel):
    """Binding details including listener name, protocol, url and vport

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Specifies the ID of CLB to be bound
        :type LoadBalancerId: str
        :param _ListenerId: Specifies the ID of listener to be bound
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Domain: Specifies the domain name to be bound
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        :param _LocationId: Sets the bound rule.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LocationId: str
        :param _ListenerName: Listener name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _Protocol: Listener protocol.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Vport: Listener port.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vport: int
        :param _Url: URL of the location.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Url: str
        :param _UconfigId: Configuration ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UconfigId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._LocationId = None
        self._ListenerName = None
        self._Protocol = None
        self._Vport = None
        self._Url = None
        self._UconfigId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._LocationId = params.get("LocationId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Vport = params.get("Vport")
        self._Url = params.get("Url")
        self._UconfigId = params.get("UconfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockedIP(AbstractModel):
    """IP added to blocklist 12306

    """

    def __init__(self):
        r"""
        :param _IP: Blacklisted IP
        :type IP: str
        :param _CreateTime: Blacklisted time
        :type CreateTime: str
        :param _ExpireTime: Expiration time
        :type ExpireTime: str
        """
        self._IP = None
        self._CreateTime = None
        self._ExpireTime = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """Certificate ID and list of CLB instances associated with it

    """

    def __init__(self):
        r"""
        :param _CertId: Certificate ID
        :type CertId: str
        :param _LoadBalancers: List of CLB instances associated with certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancer
        """
        self._CertId = None
        self._LoadBalancers = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """Certificate information

    """

    def __init__(self):
        r"""
        :param _CertId: ID of the certificate. If it's not specified, `CertContent` and `CertKey` are required. For a server certificate, you also need to specify `CertName`. 
        :type CertId: str
        :param _CertName: Name of the uploaded certificate. It's required if `CertId` is not specified.
        :type CertName: str
        :param _CertContent: Public key of the uploaded certificate. This is required if `CertId` is not specified.
        :type CertContent: str
        :param _CertKey: Private key of the uploaded server certificate. This is required if `CertId` is not specified.
        :type CertKey: str
        """
        self._CertId = None
        self._CertName = None
        self._CertContent = None
        self._CertKey = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertContent(self):
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertKey(self):
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._CertContent = params.get("CertContent")
        self._CertKey = params.get("CertKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInput(AbstractModel):
    """Certificate information

    """

    def __init__(self):
        r"""
        :param _SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)
        :type SSLMode: str
        :param _CertId: ID of a server certificate. If you leave this parameter empty, you must upload the certificate, including CertContent, CertKey, and CertName.
        :type CertId: str
        :param _CertCaId: ID of a client certificate. When the listener adopts mutual authentication (i.e., SSLMode = mutual), if you leave this parameter empty, you must upload the client certificate, including CertCaContent and CertCaName.
        :type CertCaId: str
        :param _CertName: Name of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertName: str
        :param _CertKey: Key of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertKey: str
        :param _CertContent: Content of the uploaded server certificate. If there is no CertId, this parameter is required.
        :type CertContent: str
        :param _CertCaName: Name of the uploaded client CA certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.
        :type CertCaName: str
        :param _CertCaContent: Content of the uploaded client certificate. When SSLMode = mutual, if there is no CertCaId, this parameter is required.
        :type CertCaContent: str
        """
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._CertName = None
        self._CertKey = None
        self._CertContent = None
        self._CertCaName = None
        self._CertCaContent = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertKey(self):
        return self._CertKey

    @CertKey.setter
    def CertKey(self, CertKey):
        self._CertKey = CertKey

    @property
    def CertContent(self):
        return self._CertContent

    @CertContent.setter
    def CertContent(self, CertContent):
        self._CertContent = CertContent

    @property
    def CertCaName(self):
        return self._CertCaName

    @CertCaName.setter
    def CertCaName(self, CertCaName):
        self._CertCaName = CertCaName

    @property
    def CertCaContent(self):
        return self._CertCaContent

    @CertCaContent.setter
    def CertCaContent(self, CertCaContent):
        self._CertCaContent = CertCaContent


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._CertName = params.get("CertName")
        self._CertKey = params.get("CertKey")
        self._CertContent = params.get("CertContent")
        self._CertCaName = params.get("CertCaName")
        self._CertCaContent = params.get("CertCaContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateOutput(AbstractModel):
    """Certificate information

    """

    def __init__(self):
        r"""
        :param _SSLMode: Authentication type. Value range: UNIDIRECTIONAL (unidirectional authentication), MUTUAL (mutual authentication)
        :type SSLMode: str
        :param _CertId: Server certificate ID.
        :type CertId: str
        :param _CertCaId: Client certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertCaId: str
        :param _ExtCertIds: IDs of extra server certificates
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExtCertIds: list of str
        """
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._ExtCertIds = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def ExtCertIds(self):
        return self._ExtCertIds

    @ExtCertIds.setter
    def ExtCertIds(self, ExtCertIds):
        self._ExtCertIds = ExtCertIds


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._ExtCertIds = params.get("ExtCertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalHealth(AbstractModel):
    """Real server health status of a classic CLB

    """

    def __init__(self):
        r"""
        :param _IP: Private IP of a real server
        :type IP: str
        :param _Port: Real server port
        :type Port: int
        :param _ListenerPort: CLB listener port
        :type ListenerPort: int
        :param _Protocol: Forwarding protocol
        :type Protocol: str
        :param _HealthStatus: Health check result. Value range: 1 (healthy), 0 (unhealthy)
        :type HealthStatus: int
        """
        self._IP = None
        self._Port = None
        self._ListenerPort = None
        self._Protocol = None
        self._HealthStatus = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._ListenerPort = params.get("ListenerPort")
        self._Protocol = params.get("Protocol")
        self._HealthStatus = params.get("HealthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalListener(AbstractModel):
    """Classic CLB listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _ListenerPort: CLB listener port
        :type ListenerPort: int
        :param _InstancePort: Backend forwarding port of a listener
        :type InstancePort: int
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Protocol: Listener protocol type
        :type Protocol: str
        :param _SessionExpire: Session persistence time
        :type SessionExpire: int
        :param _HealthSwitch: Whether health check is enabled. 1: enabled; 0: disabled.
        :type HealthSwitch: int
        :param _TimeOut: Response timeout period
        :type TimeOut: int
        :param _IntervalTime: Check interval
        :type IntervalTime: int
        :param _HealthNum: Health threshold
        :type HealthNum: int
        :param _UnhealthNum: Unhealthy threshold
        :type UnhealthNum: int
        :param _HttpHash: A request balancing method for HTTP and HTTPS listeners of a public network classic CLB. wrr means weighted round robin, while ip_hash means consistent hashing based on source IPs of access requests.
        :type HttpHash: str
        :param _HttpCode: Health check return code for HTTP and HTTPS listeners of a public network classic CLB. For more information, see the explanation of the field in the listener creating API.
        :type HttpCode: int
        :param _HttpCheckPath: Health check path for HTTP and HTTPS listeners of a public network classic CLB
        :type HttpCheckPath: str
        :param _SSLMode: Authentication method for an HTTPS listener of a public network classic CLB
        :type SSLMode: str
        :param _CertId: Server certificate ID for an HTTPS listener of a public network classic CLB
        :type CertId: str
        :param _CertCaId: Client certificate ID for an HTTPS listener of a public network classic CLB
        :type CertCaId: str
        :param _Status: Listener status. Value range: 0 (creating), 1 (running)
        :type Status: int
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._InstancePort = None
        self._ListenerName = None
        self._Protocol = None
        self._SessionExpire = None
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnhealthNum = None
        self._HttpHash = None
        self._HttpCode = None
        self._HttpCheckPath = None
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._Status = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def InstancePort(self):
        return self._InstancePort

    @InstancePort.setter
    def InstancePort(self, InstancePort):
        self._InstancePort = InstancePort

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SessionExpire(self):
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnhealthNum(self):
        return self._UnhealthNum

    @UnhealthNum.setter
    def UnhealthNum(self, UnhealthNum):
        self._UnhealthNum = UnhealthNum

    @property
    def HttpHash(self):
        return self._HttpHash

    @HttpHash.setter
    def HttpHash(self, HttpHash):
        self._HttpHash = HttpHash

    @property
    def HttpCode(self):
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def HttpCheckPath(self):
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._InstancePort = params.get("InstancePort")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._SessionExpire = params.get("SessionExpire")
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnhealthNum = params.get("UnhealthNum")
        self._HttpHash = params.get("HttpHash")
        self._HttpCode = params.get("HttpCode")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._SSLMode = params.get("SSLMode")
        self._CertId = params.get("CertId")
        self._CertCaId = params.get("CertCaId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalLoadBalancerInfo(AbstractModel):
    """CLB information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Real server ID
        :type InstanceId: str
        :param _LoadBalancerIds: List of CLB instance IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        """
        self._InstanceId = None
        self._LoadBalancerIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTarget(AbstractModel):
    """Real server information of a classic CLB

    """

    def __init__(self):
        r"""
        :param _Type: Real server type. Value range: CVM, ENI (coming soon)
        :type Type: str
        :param _InstanceId: Unique ID of a real server, which can be obtained from the unInstanceId field in the return of the DescribeInstances API
        :type InstanceId: str
        :param _Weight: Forwarding weight of a real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param _PublicIpAddresses: Public IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: Private IP of a real server
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param _InstanceName: Real server instance names
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _RunFlag: Real server status
1: failed; 2: running; 3: creating; 4: shut down; 5: returned; 6: returning; 7: restarting; 8: starting; 9: shutting down; 10: resetting password; 11: formatting; 12: making image; 13: setting bandwidth; 14: reinstalling system; 19: upgrading; 21: hot migrating
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunFlag: int
        """
        self._Type = None
        self._InstanceId = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RunFlag = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RunFlag(self):
        return self._RunFlag

    @RunFlag.setter
    def RunFlag(self, RunFlag):
        self._RunFlag = RunFlag


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RunFlag = params.get("RunFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicalTargetInfo(AbstractModel):
    """Backend information of a classic CLB

    """

    def __init__(self):
        r"""
        :param _InstanceId: Real server ID
        :type InstanceId: str
        :param _Weight: Weight. Value range: [0, 100]
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneLoadBalancerRequest(AbstractModel):
    """CloneLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: Clones the name of the CLB instance. The name must be 1-60 characters containing letters, numbers, "-" or "_".
Note: if the name of a new CLB instance already exists, a default name will be generated automatically.
        :type LoadBalancerName: str
        :param _ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the `DescribeProject` API. If this parameter is not passed in, the default project will be used.
        :type ProjectId: int
        :param _MasterZoneId: Sets the primary AZ ID for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`, which is applicable only to public network CLB.
Note: A primary AZ loads traffic, while a secondary AZ does not load traffic by default and will be used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. You can use the `DescribeResource` API to query the primary AZ list of a region.
        :type MasterZoneId: str
        :param _SlaveZoneId: Specifies the secondary AZ ID for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`. It is applicable only to public network CLB.
Note: A secondary AZ will load traffic if the primary AZ is faulty. You can use the `DescribeMasterZones` API to query the primary and secondary AZ list of a region.
        :type SlaveZoneId: str
        :param _ZoneId: Specifies an AZ ID for creating a CLB instance, such as `ap-guangzhou-1`, which is applicable only to public network CLB instances.
        :type ZoneId: str
        :param _InternetAccessible: CLB network billing mode. This parameter is applicable only to public network CLB instances.
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _VipIsp: ISP of VIP. Values: `CMCC` (China Mobile), `CUCC` (China Unicom) and `CTCC` (China Telecom). You need to activate static single-line IPs. This feature is in beta and is only available in Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu and Chongqing regions. To try it out, please contact your sales rep. If it's specified, the network billing mode must be `BANDWIDTH_PACKAGE`. If it's not specified, BGP is used by default. To query ISPs supported in a region, please use [DescribeResources](https://intl.cloud.tencent.com/document/api/214/70213?from_cn_redirect=1). 
        :type VipIsp: str
        :param _Vip: Applies for CLB instances for a specified VIP
        :type Vip: str
        :param _Tags: Tags a CLB instance when purchasing it
        :type Tags: list of TagInfo
        :param _ExclusiveCluster: Dedicated cluster information
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _BandwidthPackageId: Bandwidth package ID. If this parameter is specified, the network billing mode (`InternetAccessible.InternetChargeType`) will only support bill-by-bandwidth package (`BANDWIDTH_PACKAGE`).
        :type BandwidthPackageId: str
        :param _SnatPro: Whether to support binding cross-VPC IPs or cross-region IPs
        :type SnatPro: bool
        :param _SnatIps: Creates `SnatIp` when the binding IPs of other VPCs feature is enabled
        :type SnatIps: list of SnatIp
        :param _ClusterIds: ID of the public network CLB dedicated cluster
        :type ClusterIds: list of str
        :param _SlaType: Specification of the LCU-supported instance.
        :type SlaType: str
        :param _ClusterTag: Tag of the STGW dedicated cluster
        :type ClusterTag: str
        :param _Zones: Availability zones for nearby access of private network CLB instances to distribute traffic
        :type Zones: list of str
        :param _EipAddressId: Unique ID of an EIP, which can only be used when binding the EIP of a private network CLB instance (e.g., `eip-11112222`)
        :type EipAddressId: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._ProjectId = None
        self._MasterZoneId = None
        self._SlaveZoneId = None
        self._ZoneId = None
        self._InternetAccessible = None
        self._VipIsp = None
        self._Vip = None
        self._Tags = None
        self._ExclusiveCluster = None
        self._BandwidthPackageId = None
        self._SnatPro = None
        self._SnatIps = None
        self._ClusterIds = None
        self._SlaType = None
        self._ClusterTag = None
        self._Zones = None
        self._EipAddressId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def EipAddressId(self):
        return self._EipAddressId

    @EipAddressId.setter
    def EipAddressId(self, EipAddressId):
        self._EipAddressId = EipAddressId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._ProjectId = params.get("ProjectId")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._VipIsp = params.get("VipIsp")
        self._Vip = params.get("Vip")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._ClusterIds = params.get("ClusterIds")
        self._SlaType = params.get("SlaType")
        self._ClusterTag = params.get("ClusterTag")
        self._Zones = params.get("Zones")
        self._EipAddressId = params.get("EipAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneLoadBalancerResponse(AbstractModel):
    """CloneLoadBalancer response structure.

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


class ClusterItem(AbstractModel):
    """Dedicated cluster information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Unique cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param _Zone: Cluster AZ, such as ap-guangzhou-1
Note: this field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Zone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigListItem(AbstractModel):
    """Configuration content

    """

    def __init__(self):
        r"""
        :param _UconfigId: Configuration ID.
        :type UconfigId: str
        :param _ConfigType: Configuration type.
        :type ConfigType: str
        :param _ConfigName: Configuration name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ConfigName: str
        :param _ConfigContent: Configuration content.
        :type ConfigContent: str
        :param _CreateTimestamp: Creates configuration time.
        :type CreateTimestamp: str
        :param _UpdateTimestamp: Modifies configuration time.
        :type UpdateTimestamp: str
        """
        self._UconfigId = None
        self._ConfigType = None
        self._ConfigName = None
        self._ConfigContent = None
        self._CreateTimestamp = None
        self._UpdateTimestamp = None

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ConfigContent(self):
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def CreateTimestamp(self):
        return self._CreateTimestamp

    @CreateTimestamp.setter
    def CreateTimestamp(self, CreateTimestamp):
        self._CreateTimestamp = CreateTimestamp

    @property
    def UpdateTimestamp(self):
        return self._UpdateTimestamp

    @UpdateTimestamp.setter
    def UpdateTimestamp(self, UpdateTimestamp):
        self._UpdateTimestamp = UpdateTimestamp


    def _deserialize(self, params):
        self._UconfigId = params.get("UconfigId")
        self._ConfigType = params.get("ConfigType")
        self._ConfigName = params.get("ConfigName")
        self._ConfigContent = params.get("ConfigContent")
        self._CreateTimestamp = params.get("CreateTimestamp")
        self._UpdateTimestamp = params.get("UpdateTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetRequest(AbstractModel):
    """CreateClsLogSet request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetName: Logset name, which must be unique among all CLS logsets; default value: clb_logset
        :type LogsetName: str
        :param _Period: Logset retention period (in days)
        :type Period: int
        :param _LogsetType: Logset type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).
        :type LogsetType: str
        """
        self._LogsetName = None
        self._Period = None
        self._LogsetType = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def LogsetType(self):
        return self._LogsetType

    @LogsetType.setter
    def LogsetType(self, LogsetType):
        self._LogsetType = LogsetType


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
        self._Period = params.get("Period")
        self._LogsetType = params.get("LogsetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogSetResponse(AbstractModel):
    """CreateClsLogSet response structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID.
        :type LogsetId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Ports: Specifies for which ports to create listeners. Each port corresponds to a new listener.
        :type Ports: list of int
        :param _Protocol: Listener protocol. Values: TCP | UDP | HTTP | HTTPS | TCP_SSL | QUIC
        :type Protocol: str
        :param _ListenerNames: List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.
        :type ListenerNames: list of str
        :param _HealthCheck: Health check parameter. It is only applicable only to TCP, UDP, TCP_SSL and QUIC listeners.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: Certificate information. This parameter is only applicable to TCP_SSL listeners and HTTPS listeners with the SNI feature not enabled. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param _Scheduler: Listener forwarding mode. u200dValues: `WRR` (weighted round robin) and `LEAST_CONN` (least connections). 
Default value: `WRR`. This parameter is only applicable to TCP, UDP, TCP_SSL and QUIC listeners.
        :type Scheduler: str
        :param _SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners
        :type SniSwitch: int
        :param _TargetType: Target real server type. `NODE`: binding a general node; `TARGETGROUP`: binding a target group.
        :type TargetType: str
        :param _SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.
        :type SessionType: str
        :param _KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners. Valid values: 0 (disable; default value) and 1 (enable).
        :type KeepaliveEnable: int
        :param _EndPort: This parameter is used to specify the end port and is required when creating a port range listener. Only one member can be passed in when inputting the `Ports` parameter, which is used to specify the start port. If you want to try the port range feature, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).
        :type EndPort: int
        :param _DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
        :type DeregisterTargetRst: bool
        :param _MultiCertInfo: Certificate information. You can specify multiple server-side certificates with different algorithm types. This parameter is only applicable to HTTPS listeners with the SNI feature not enabled. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        :param _MaxConn: Maximum number of concurrent listener connections. It’s available for TCP/UDP/TCP_SSL/QUIC listeners. If it’s set to `-1` or not specified, the listener speed is not limited. 
        :type MaxConn: int
        :param _MaxCps: Maximum number of new listener connections. It’s available for TCP/UDP/TCP_SSL/QUIC listeners. If it’s set to `-1` or not specified, the listener speed is not limited. 
        :type MaxCps: int
        :param _IdleConnectTimeout: Connection idle timeout period (in seconds). It’s only available to TCP listeners. Value range: 300-900 for shared and dedicated instances; 300-2000 for LCU-supported CLB instances. It defaults to 900. To set a period longer than 2000 seconds (up to 3600 seconds), please submit a [submit](https://console.cloud.tencent.com/workorder/category). 
        :type IdleConnectTimeout: int
        """
        self._LoadBalancerId = None
        self._Ports = None
        self._Protocol = None
        self._ListenerNames = None
        self._HealthCheck = None
        self._Certificate = None
        self._SessionExpireTime = None
        self._Scheduler = None
        self._SniSwitch = None
        self._TargetType = None
        self._SessionType = None
        self._KeepaliveEnable = None
        self._EndPort = None
        self._DeregisterTargetRst = None
        self._MultiCertInfo = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerNames(self):
        return self._ListenerNames

    @ListenerNames.setter
    def ListenerNames(self, ListenerNames):
        self._ListenerNames = ListenerNames

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ports = params.get("Ports")
        self._Protocol = params.get("Protocol")
        self._ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._Scheduler = params.get("Scheduler")
        self._SniSwitch = params.get("SniSwitch")
        self._TargetType = params.get("TargetType")
        self._SessionType = params.get("SessionType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._EndPort = params.get("EndPort")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: Array of unique IDs of the created listeners
        :type ListenerIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param _Forward: CLB instance type. Valid value: 1 (generic CLB instance).
        :type Forward: int
        :param _LoadBalancerName: CLB instance name, which takes effect only when only one instance is to be created in the request. It can consist 1 to 60 letters, digits, hyphens (-), or underscores (_).
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.
        :type LoadBalancerName: str
        :param _VpcId: Network ID of the target device on the CLB backend, such as `vpc-12345678`, which can be obtained through the `DescribeVpcEx` API. If this parameter is not entered, `DefaultVPC` is used by default. This parameter is required when creating a private network instance.
        :type VpcId: str
        :param _SubnetId: A subnet ID must be specified when you purchase a private network CLB instance in a VPC, and the VIP of this instance will be generated in this subnet. This parameter is required for creating a CLB instance.
        :type SubnetId: str
        :param _ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the `DescribeProject` API. If this parameter is not entered, the default project will be used.
        :type ProjectId: int
        :param _AddressIPVersion: It's only applicable to public network CLB instances. IP version. Values: `IPV4`, `IPV6` and `IPv6FullChain` (case-insensitive). Default: `IPV4`. Note: `IPV6` indicates IPv6 NAT64, while `IPv6FullChain` indicates IPv6. 
        :type AddressIPVersion: str
        :param _Number: Number of CLBs to be created. Default value: 1.
        :type Number: int
        :param _MasterZoneId: ID of the primary AZ for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`. It's only available to public CLB instances. 
Note: The traffic only goes to the primary AZ in normal cases. The secondary AZ is used only when the primary AZ is unavailable. To query the list of primary AZs in a region, use [DescribeResources](https://intl.cloud.tencent.com/document/api/214/70213?from_cn_redirect=1).
        :type MasterZoneId: str
        :param _ZoneId: Specifies an AZ ID for creating a CLB instance, such as `ap-guangzhou-1`, which is applicable only to public network CLB instances.
        :type ZoneId: str
        :param _InternetAccessible: It only works on LCU-supported instances on private networks and all instances on public networks.
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _VipIsp: ISP of VIP. Values: `CMCC` (China Mobile), `CUCC` (China Unicom) and `CTCC` (China Telecom). You need to activate static single-line IPs. This feature is in beta and is only available in Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu and Chongqing regions. To try it out, please contact your sales rep. If it's specified, the network billing mode must be `BANDWIDTH_PACKAGE`. If it's not specified, BGP is used by default. To query ISPs supported in a region, please use [DescribeResources](https://intl.cloud.tencent.com/document/api/214/70213?from_cn_redirect=1). 
        :type VipIsp: str
        :param _Tags: Tags the CLB instance when purchasing it. Up to 20 tag key value pairs are supported.
        :type Tags: list of TagInfo
        :param _Vip: Specifies the VIP for the application of a CLB instance. This parameter is optional. If you do not specify this parameter, the system automatically assigns a value for the parameter. IPv4 and IPv6 CLB instances support this parameter, but IPv6 NAT64 CLB instances do not.
Note: If the specified VIP is occupied or is not within the IP range of the specified VPC subnet, you cannot use the VIP to create a CLB instance in a private network or an IPv6 BGP CLB instance in a public network.
        :type Vip: str
        :param _BandwidthPackageId: Bandwidth package ID. If this parameter is specified, the network billing mode (`InternetAccessible.InternetChargeType`) will only support bill-by-bandwidth package (`BANDWIDTH_PACKAGE`).
        :type BandwidthPackageId: str
        :param _ExclusiveCluster: Information about the dedicated CLB instance. You must specify this parameter when you create a dedicated CLB instance in a private network.
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _SlaType: Specification of LCU-supported instance.
<ul><li>This parameter is required to create LCU-supported instances. Values: <ul><li>`SLA`: Super Large 4. When you have activated Super Large models, `SLA` refers to Super Large 4.</li><li>`clb.c2.medium`: Standard</li><li>`clb.c3.small`: Advanced 1</li><li>`clb.c3.medium`: Advanced 1</li><li>`clb.c4.small`: Super Large 1</li><li>`clb.c4.medium`: Super Large 2</li><li>`clb.c4.large`: Super Large 3</li><li>`clb.c4.xlarge`: Super Large 4</li> For Super Large 2 and above models, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).</ul></li><li> This parameter is not required for creating shared instances.</li></ul>For more details, see [Instance Specifications](https://intl.cloud.tencent.com/document/product/214/84689?from_cn_redirect=1).
        :type SlaType: str
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _SnatPro: Whether Binding IPs of other VPCs feature switch
        :type SnatPro: bool
        :param _SnatIps: Creates `SnatIp` when the binding IPs of other VPCs feature is enabled
        :type SnatIps: list of SnatIp
        :param _ClusterTag: Tag for the STGW exclusive cluster.
        :type ClusterTag: str
        :param _SlaveZoneId: Specifies the secondary AZ ID for cross-AZ disaster recovery, such as `100001` or `ap-guangzhou-1`. It is applicable only to public network CLB.
Note: The traffic only goes to the secondary AZ when the primary AZ is unavailable. You can query the list of primary and secondary AZ of a region by calling [DescribeResources](https://intl.cloud.tencent.com/document/api/214/70213?from_cn_redirect=1).
        :type SlaveZoneId: str
        :param _EipAddressId: Unique ID of an EIP, which can only be used when binding the EIP of a private network CLB instance. E.g., `eip-11112222`.
        :type EipAddressId: str
        :param _LoadBalancerPassToTarget: Whether to allow CLB traffic to the target group. `true`: allows CLB traffic to the target group and verifies security groups only on CLB; `false`: denies CLB traffic to the target group and verifies security groups on both CLB and backend instances.
        :type LoadBalancerPassToTarget: bool
        :param _DynamicVip: Upgrades to domain name-based CLB
        :type DynamicVip: bool
        :param _Egress: Network egress point
        :type Egress: str
        """
        self._LoadBalancerType = None
        self._Forward = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._AddressIPVersion = None
        self._Number = None
        self._MasterZoneId = None
        self._ZoneId = None
        self._InternetAccessible = None
        self._VipIsp = None
        self._Tags = None
        self._Vip = None
        self._BandwidthPackageId = None
        self._ExclusiveCluster = None
        self._SlaType = None
        self._ClientToken = None
        self._SnatPro = None
        self._SnatIps = None
        self._ClusterTag = None
        self._SlaveZoneId = None
        self._EipAddressId = None
        self._LoadBalancerPassToTarget = None
        self._DynamicVip = None
        self._Egress = None

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def EipAddressId(self):
        return self._EipAddressId

    @EipAddressId.setter
    def EipAddressId(self, EipAddressId):
        self._EipAddressId = EipAddressId

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def DynamicVip(self):
        return self._DynamicVip

    @DynamicVip.setter
    def DynamicVip(self, DynamicVip):
        self._DynamicVip = DynamicVip

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._Number = params.get("Number")
        self._MasterZoneId = params.get("MasterZoneId")
        self._ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Vip = params.get("Vip")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._SlaType = params.get("SlaType")
        self._ClientToken = params.get("ClientToken")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._ClusterTag = params.get("ClusterTag")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._EipAddressId = params.get("EipAddressId")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._DynamicVip = params.get("DynamicVip")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of unique CLB instance IDs.
This field may return `null` in some cases, such as there is delay during instance creation. You can query the IDs of the created instances by invoking `DescribeTaskStatus` with the `RequestId` or `DealName` returned by this API.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        :param _DealName: Order ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.
        :type LoadBalancerId: str
        :param _SnatIps: Information of the SNAT IP to be added. You can specify a SNAT IP or use the one automatically assigned by a subnet.
        :type SnatIps: list of SnatIp
        :param _Number: Number of SNAT IPs to be added. This parameter is used in conjunction with `SnatIps`. Note that if `Ip` is specified in `SnapIps`, this parameter is not available. It defaults to `1` and the upper limit is `10`.
        :type Number: int
        """
        self._LoadBalancerId = None
        self._SnatIps = None
        self._Number = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps response structure.

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


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Rules: Information of the new forwarding rule
        :type Rules: list of RuleInput
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Rules = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param _LocationIds: Array of unique IDs of created forwarding rules
        :type LocationIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LocationIds = None
        self._RequestId = None

    @property
    def LocationIds(self):
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LocationIds = params.get("LocationIds")
        self._RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupName: Target group name (up to 50 characters)
        :type TargetGroupName: str
        :param _VpcId: `vpcid` attribute of a target group. If this parameter is left empty, the default VPC will be used.
        :type VpcId: str
        :param _Port: Default port of a target group, which can be used for subsequently added servers.
        :type Port: int
        :param _TargetGroupInstances: Real server bound to a target group
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupName = None
        self._VpcId = None
        self._Port = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupName = params.get("TargetGroupName")
        self._VpcId = params.get("VpcId")
        self._Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: ID generated after target group creation
        :type TargetGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetGroupId = None
        self._RequestId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _PartitionCount: The number of topic partitions, which changes as partitions are split or merged. Each log topic can have up to 50 partitions. If this parameter is not passed in, 1 partition will be created by default and up to 10 partitions are allowed to be created.
        :type PartitionCount: int
        :param _TopicType: Log type. Valid values: ACCESS (access logs; default value) and HEALTH (health check logs).
        :type TopicType: str
        :param _Period: Logset retention period (in days). Default: 30 days.
        :type Period: int
        :param _StorageType: Log topic storage type. Valid values: `hot` (STANDARD storage); `cold` (IA storage). Default value: `hot`.
        :type StorageType: str
        """
        self._TopicName = None
        self._PartitionCount = None
        self._TopicType = None
        self._Period = None
        self._StorageType = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        self._TopicType = params.get("TopicType")
        self._Period = params.get("Period")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CrossTargets(AbstractModel):
    """Information of CVMs and ENIs that use cross-region binding 2.0

    """

    def __init__(self):
        r"""
        :param _LocalVpcId: VPC ID of the CLB instance
        :type LocalVpcId: str
        :param _VpcId: VPC ID of the CVM or ENI instance
        :type VpcId: str
        :param _IP: IP address of the CVM or ENI instance
        :type IP: str
        :param _VpcName: VPC name of the CVM or ENI instance
        :type VpcName: str
        :param _EniId: ENI ID of the CVM instance
        :type EniId: str
        :param _InstanceId: ID of the CVM instance
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param _InstanceName: Name of the CVM instance
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param _Region: Region of the CVM or ENI instance
        :type Region: str
        """
        self._LocalVpcId = None
        self._VpcId = None
        self._IP = None
        self._VpcName = None
        self._EniId = None
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None

    @property
    def LocalVpcId(self):
        return self._LocalVpcId

    @LocalVpcId.setter
    def LocalVpcId(self, LocalVpcId):
        self._LocalVpcId = LocalVpcId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LocalVpcId = params.get("LocalVpcId")
        self._VpcId = params.get("VpcId")
        self._IP = params.get("IP")
        self._VpcName = params.get("VpcName")
        self._EniId = params.get("EniId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerRequest(AbstractModel):
    """DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: ID of the listener to be deleted
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener response structure.

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


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerIds: Array of listener IDs to delete (20 IDs at most). If this parameter is left empty, all listeners of the CLB instance will be deleted.
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners response structure.

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


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of IDs of the CLB instances to be deleted. Array length limit: 20.
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer response structure.

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


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Unique ID of a CLB instance, e.g., lb-12345678.
        :type LoadBalancerId: str
        :param _Ips: Array of the SNAT IP addresses to be deleted
        :type Ips: list of str
        """
        self._LoadBalancerId = None
        self._Ips = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps response structure.

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


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _SourceListenerId: Source listener ID
        :type SourceListenerId: str
        :param _TargetListenerId: Target listener ID
        :type TargetListenerId: str
        :param _RewriteInfos: Redirection relationship between forwarding rules
        :type RewriteInfos: list of RewriteLocationMap
        """
        self._LoadBalancerId = None
        self._SourceListenerId = None
        self._TargetListenerId = None
        self._RewriteInfos = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerId(self):
        return self._SourceListenerId

    @SourceListenerId.setter
    def SourceListenerId(self, SourceListenerId):
        self._SourceListenerId = SourceListenerId

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def RewriteInfos(self):
        return self._RewriteInfos

    @RewriteInfos.setter
    def RewriteInfos(self, RewriteInfos):
        self._RewriteInfos = RewriteInfos


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerId = params.get("SourceListenerId")
        self._TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self._RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self._RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite response structure.

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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _LocationIds: Array of IDs of the forwarding rules to be deleted
        :type LocationIds: list of str
        :param _Domain: The domain name associated with the forwarding rule to delete. If the rule is associated with multiple domain names, specify any one of them.
        :type Domain: str
        :param _Url: The forwarding path of the forwarding rule to delete.
        :type Url: str
        :param _NewDefaultServerDomain: Specifies a new default domain name for the listener. This field is used when the original default domain name is disabled. If there are multiple domain names, specify one of them.
        :type NewDefaultServerDomain: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationIds = None
        self._Domain = None
        self._Url = None
        self._NewDefaultServerDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationIds(self):
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def NewDefaultServerDomain(self):
        return self._NewDefaultServerDomain

    @NewDefaultServerDomain.setter
    def NewDefaultServerDomain(self, NewDefaultServerDomain):
        self._NewDefaultServerDomain = NewDefaultServerDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationIds = params.get("LocationIds")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

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


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: Target group ID array
        :type TargetGroupIds: list of str
        """
        self._TargetGroupIds = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups response structure.

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


class DeregisterFunctionTargetsRequest(AbstractModel):
    """DeregisterFunctionTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID.
        :type ListenerId: str
        :param _FunctionTargets: List of functions to be unbound
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: The ID of target forwarding rule. To unbind a function from an L7 forwarding rule, either `LocationId` or `Domain+Url` is required. 
        :type LocationId: str
        :param _Domain: Domain name of the target forwarding rule. It is ignored if `LocationId` is specified. 
        :type Domain: str
        :param _Url: URL of the target forwarding rule. It is ignored if `LocationId` is specified. 
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterFunctionTargetsResponse(AbstractModel):
    """DeregisterFunctionTargets response structure.

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


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: Information of server to be unbound
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances response structure.

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


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _InstanceIds: List of real server IDs
        :type InstanceIds: list of str
        """
        self._LoadBalancerId = None
        self._InstanceIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB response structure.

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


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID in the format of "lb-12345678"
        :type LoadBalancerId: str
        :param _ListenerId: Listener ID in the format of "lbl-12345678"
        :type ListenerId: str
        :param _Targets: List of real servers to be unbound. Array length limit: 20.
        :type Targets: list of Target
        :param _LocationId: Forwarding rule ID in the format of "loc-12345678". When unbinding a server from a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param _Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param _Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets response structure.

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


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _Offset: Data offset. Default value: 0.
        :type Offset: int
        :param _Limit: Maximum number of IPs to be returned. Default value: 100,000.
        :type Limit: int
        """
        self._LoadBalancerId = None
        self._Offset = None
        self._Limit = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

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
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList response structure.

    """

    def __init__(self):
        r"""
        :param _BlockedIPCount: Number of returned IPs
        :type BlockedIPCount: int
        :param _ClientIPField: Field for getting real client IP
        :type ClientIPField: str
        :param _BlockedIPList: List of IPs added to blocklist 12360
        :type BlockedIPList: list of BlockedIP
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlockedIPCount = None
        self._ClientIPField = None
        self._BlockedIPList = None
        self._RequestId = None

    @property
    def BlockedIPCount(self):
        return self._BlockedIPCount

    @BlockedIPCount.setter
    def BlockedIPCount(self, BlockedIPCount):
        self._BlockedIPCount = BlockedIPCount

    @property
    def ClientIPField(self):
        return self._ClientIPField

    @ClientIPField.setter
    def ClientIPField(self, ClientIPField):
        self._ClientIPField = ClientIPField

    @property
    def BlockedIPList(self):
        return self._BlockedIPList

    @BlockedIPList.setter
    def BlockedIPList(self, BlockedIPList):
        self._BlockedIPList = BlockedIPList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlockedIPCount = params.get("BlockedIPCount")
        self._ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self._BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self._BlockedIPList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID returned by the `ModifyBlockIPList` API
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 1: running; 2: failed; 6: succeeded
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


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of real server IDs
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerInfoList: CLB information list
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerInfoList = None
        self._RequestId = None

    @property
    def LoadBalancerInfoList(self):
        return self._LoadBalancerInfoList

    @LoadBalancerInfoList.setter
    def LoadBalancerInfoList(self, LoadBalancerInfoList):
        self._LoadBalancerInfoList = LoadBalancerInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self._LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self._LoadBalancerInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus response structure.

    """

    def __init__(self):
        r"""
        :param _HealthList: List of real server health statuses
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HealthList: list of ClassicalHealth
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthList = None
        self._RequestId = None

    @property
    def HealthList(self):
        return self._HealthList

    @HealthList.setter
    def HealthList(self, HealthList):
        self._HealthList = HealthList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self._HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self._HealthList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerIds: List of CLB listener IDs
        :type ListenerIds: list of str
        :param _Protocol: CLB listening protocol. Valid values: TCP, UDP, HTTP, and HTTPS.
        :type Protocol: str
        :param _ListenerPort: CLB listening port. Value range: 1 - 65535.
        :type ListenerPort: int
        :param _Status: Listener status. Valid values: 0 (creating) and 1 (running).
        :type Status: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._ListenerPort = None
        self._Status = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerPort(self):
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._ListenerPort = params.get("ListenerPort")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Listener list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Listeners: list of ClassicalListener
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets response structure.

    """

    def __init__(self):
        r"""
        :param _Targets: Real server list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Targets: list of ClassicalTarget
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Targets = None
        self._RequestId = None

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClsLogSetRequest(AbstractModel):
    """DescribeClsLogSet request structure.

    """


class DescribeClsLogSetResponse(AbstractModel):
    """DescribeClsLogSet response structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _HealthLogsetId: Health check logset ID
        :type HealthLogsetId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogsetId = None
        self._HealthLogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def HealthLogsetId(self):
        return self._HealthLogsetId

    @HealthLogsetId.setter
    def HealthLogsetId(self, HealthLogsetId):
        self._HealthLogsetId = HealthLogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._HealthLogsetId = params.get("HealthLogsetId")
        self._RequestId = params.get("RequestId")


class DescribeCrossTargetsRequest(AbstractModel):
    """DescribeCrossTargets request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of real server lists returned. Default value: 20; maximum value: 100.
        :type Limit: int
        :param _Offset: Starting offset of the real server list returned. Default value: 0.
        :type Offset: int
        :param _Filters: Filter conditions to query CVMs and ENIs
<li> `vpc-id` - String - Required: No - (Filter condition) Filter by VPC ID, such as "vpc-12345678".</li>
<li> `ip` - String - Required: No - (Filter condition) Filter by real server IP, such as "192.168.0.1".</li>
<li> `listener-id` - String - Required: No - (Filter condition) Filter by listener ID, such as "lbl-12345678".</li>
<li> `location-id` - String - Required: No - (Filter condition) Filter by forwarding rule ID of the layer-7 listener, such as "loc-12345678".</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeCrossTargetsResponse(AbstractModel):
    """DescribeCrossTargets response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of real server lists
        :type TotalCount: int
        :param _CrossTargetSet: Real server list
        :type CrossTargetSet: list of CrossTargets
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CrossTargetSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CrossTargetSet(self):
        return self._CrossTargetSet

    @CrossTargetSet.setter
    def CrossTargetSet(self, CrossTargetSet):
        self._CrossTargetSet = CrossTargetSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CrossTargetSet") is not None:
            self._CrossTargetSet = []
            for item in params.get("CrossTargetSet"):
                obj = CrossTargets()
                obj._deserialize(item)
                self._CrossTargetSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomizedConfigAssociateListRequest(AbstractModel):
    """DescribeCustomizedConfigAssociateList request structure.

    """

    def __init__(self):
        r"""
        :param _UconfigId: Configuration ID.
        :type UconfigId: str
        :param _Offset: Start position of the binding list. Default: 0.
        :type Offset: int
        :param _Limit: Number of binding lists to pull. Default: 20.
        :type Limit: int
        :param _Domain: Searches for the domain name.
        :type Domain: str
        """
        self._UconfigId = None
        self._Offset = None
        self._Limit = None
        self._Domain = None

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

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

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._UconfigId = params.get("UconfigId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizedConfigAssociateListResponse(AbstractModel):
    """DescribeCustomizedConfigAssociateList response structure.

    """

    def __init__(self):
        r"""
        :param _BindList: List of bound resources
        :type BindList: list of BindDetailItem
        :param _TotalCount: Total number of bound resources
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BindList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BindList(self):
        return self._BindList

    @BindList.setter
    def BindList(self, BindList):
        self._BindList = BindList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BindList") is not None:
            self._BindList = []
            for item in params.get("BindList"):
                obj = BindDetailItem()
                obj._deserialize(item)
                self._BindList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCustomizedConfigListRequest(AbstractModel):
    """DescribeCustomizedConfigList request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigType: Configuration type. Valid values: `CLB` (CLB-specific configs), `SERVER` (domain name-specific configs), and `LOCATION` (forwarding rule-specific configs).
        :type ConfigType: str
        :param _Offset: Pagination offset. Default: 0.
        :type Offset: int
        :param _Limit: Number of results per page. Default: 20.
        :type Limit: int
        :param _ConfigName: Specifies the name of configs to query. Fuzzy match is supported.
        :type ConfigName: str
        :param _UconfigIds: Configuration ID.
        :type UconfigIds: list of str
        :param _Filters: The filters are:
<li> loadbalancer-id - String - Required: no - (filter) CLB instance ID, such as "lb-12345678". </li>
<li> vip - String - Required: no - (filter) CLB instance VIP, such as "1.1.1.1" and "2204::22:3". </li>
        :type Filters: list of Filter
        """
        self._ConfigType = None
        self._Offset = None
        self._Limit = None
        self._ConfigName = None
        self._UconfigIds = None
        self._Filters = None

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

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

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def UconfigIds(self):
        return self._UconfigIds

    @UconfigIds.setter
    def UconfigIds(self, UconfigIds):
        self._UconfigIds = UconfigIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ConfigType = params.get("ConfigType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConfigName = params.get("ConfigName")
        self._UconfigIds = params.get("UconfigIds")
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
        


class DescribeCustomizedConfigListResponse(AbstractModel):
    """DescribeCustomizedConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigList: Configuration list.
        :type ConfigList: list of ConfigListItem
        :param _TotalCount: Number of configurations.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConfigListItem()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIdleLoadBalancersRequest(AbstractModel):
    """DescribeIdleLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Data offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _LoadBalancerRegion: CLB instance region
        :type LoadBalancerRegion: str
        """
        self._Offset = None
        self._Limit = None
        self._LoadBalancerRegion = None

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

    @property
    def LoadBalancerRegion(self):
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdleLoadBalancersResponse(AbstractModel):
    """DescribeIdleLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _IdleLoadBalancers: List of idle CLBs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IdleLoadBalancers: list of IdleLoadBalancer
        :param _TotalCount: Total number of idle CLB instances
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdleLoadBalancers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IdleLoadBalancers(self):
        return self._IdleLoadBalancers

    @IdleLoadBalancers.setter
    def IdleLoadBalancers(self, IdleLoadBalancers):
        self._IdleLoadBalancers = IdleLoadBalancers

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IdleLoadBalancers") is not None:
            self._IdleLoadBalancers = []
            for item in params.get("IdleLoadBalancers"):
                obj = IdleLoadBalancer()
                obj._deserialize(item)
                self._IdleLoadBalancers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLBListenersRequest(AbstractModel):
    """DescribeLBListeners request structure.

    """

    def __init__(self):
        r"""
        :param _Backends: List of private network IPs to be queried.
        :type Backends: list of LbRsItem
        """
        self._Backends = None

    @property
    def Backends(self):
        return self._Backends

    @Backends.setter
    def Backends(self, Backends):
        self._Backends = Backends


    def _deserialize(self, params):
        if params.get("Backends") is not None:
            self._Backends = []
            for item in params.get("Backends"):
                obj = LbRsItem()
                obj._deserialize(item)
                self._Backends.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLBListenersResponse(AbstractModel):
    """DescribeLBListeners response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: Listener rule associated with the real server.
        :type LoadBalancers: list of LBItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LBItem()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerIds: Array of CLB listener IDs to query (100 IDs at most).
        :type ListenerIds: list of str
        :param _Protocol: Type of the listener protocols to be queried. Values: TCP`, `UDP`, `HTTP`, `HTTPS`, `TCP_SSL` and `QUIC`.
        :type Protocol: str
        :param _Port: Port of the listeners to be queried
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

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
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Listener list
        :type Listeners: list of Listener
        :param _TotalCount: Total number of listeners (with filters of port, protocol, and listener ID applied).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId request structure.

    """

    def __init__(self):
        r"""
        :param _CertIds: Server or client certificate ID
        :type CertIds: list of str
        """
        self._CertIds = None

    @property
    def CertIds(self):
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


    def _deserialize(self, params):
        self._CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId response structure.

    """

    def __init__(self):
        r"""
        :param _CertSet: Certificate ID and list of CLB instances associated with it
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertSet = None
        self._RequestId = None

    @property
    def CertSet(self):
        return self._CertSet

    @CertSet.setter
    def CertSet(self, CertSet):
        self._CertSet = CertSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self._CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self._CertSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerOverviewRequest(AbstractModel):
    """DescribeLoadBalancerOverview request structure.

    """


class DescribeLoadBalancerOverviewResponse(AbstractModel):
    """DescribeLoadBalancerOverview response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of CLB instances
        :type TotalCount: int
        :param _RunningCount: Number of CLB instances that are running
        :type RunningCount: int
        :param _IsolationCount: Number of CLB instances that are isolated
        :type IsolationCount: int
        :param _WillExpireCount: Number of CLB instances that are about to expire
        :type WillExpireCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RunningCount = None
        self._IsolationCount = None
        self._WillExpireCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def IsolationCount(self):
        return self._IsolationCount

    @IsolationCount.setter
    def IsolationCount(self, IsolationCount):
        self._IsolationCount = IsolationCount

    @property
    def WillExpireCount(self):
        return self._WillExpireCount

    @WillExpireCount.setter
    def WillExpireCount(self, WillExpireCount):
        self._WillExpireCount = WillExpireCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._RunningCount = params.get("RunningCount")
        self._IsolationCount = params.get("IsolationCount")
        self._WillExpireCount = params.get("WillExpireCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerTrafficRequest(AbstractModel):
    """DescribeLoadBalancerTraffic request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerRegion: CLB instance region. If this parameter is not passed in, CLB instances in all regions will be returned.
        :type LoadBalancerRegion: str
        """
        self._LoadBalancerRegion = None

    @property
    def LoadBalancerRegion(self):
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion


    def _deserialize(self, params):
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerTrafficResponse(AbstractModel):
    """DescribeLoadBalancerTraffic response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerTraffic: Information of CLB instances sorted by outbound bandwidth from highest to lowest
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerTraffic: list of LoadBalancerTraffic
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerTraffic = None
        self._RequestId = None

    @property
    def LoadBalancerTraffic(self):
        return self._LoadBalancerTraffic

    @LoadBalancerTraffic.setter
    def LoadBalancerTraffic(self, LoadBalancerTraffic):
        self._LoadBalancerTraffic = LoadBalancerTraffic

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerTraffic") is not None:
            self._LoadBalancerTraffic = []
            for item in params.get("LoadBalancerTraffic"):
                obj = LoadBalancerTraffic()
                obj._deserialize(item)
                self._LoadBalancerTraffic.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersDetailRequest(AbstractModel):
    """DescribeLoadBalancersDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of CLB instance lists returned. Default value: 20; maximum value: 100.
        :type Limit: int
        :param _Offset: Starting offset of the CLB instance list returned. Default value: 0.
        :type Offset: int
        :param _Fields: List of fields. Only fields specified will be returned. If it’s left blank, `null` is returned. The fields `LoadBalancerId` and `LoadBalancerName` are added by default. For details about fields, see <a href="https://intl.cloud.tencent.com/document/api/214/30694?from_cn_redirect=1#LoadBalancerDetail">LoadBalancerDetail</a>.
        :type Fields: list of str
        :param _TargetType: Target type. Valid values: NODE and GROUP. If the list of fields contains `TargetId`, `TargetAddress`, `TargetPort`, `TargetWeight` and other fields, `Target` of the target group or non-target group must be exported.
        :type TargetType: str
        :param _Filters: Filter condition of querying lists describing CLB instance details:
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
        self._Limit = None
        self._Offset = None
        self._Fields = None
        self._TargetType = None
        self._Filters = None

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
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Fields = params.get("Fields")
        self._TargetType = params.get("TargetType")
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
        


class DescribeLoadBalancersDetailResponse(AbstractModel):
    """DescribeLoadBalancersDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of lists describing CLB instance details.
        :type TotalCount: int
        :param _LoadBalancerDetailSet: List of CLB instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerDetailSet: list of LoadBalancerDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerDetailSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerDetailSet(self):
        return self._LoadBalancerDetailSet

    @LoadBalancerDetailSet.setter
    def LoadBalancerDetailSet(self, LoadBalancerDetailSet):
        self._LoadBalancerDetailSet = LoadBalancerDetailSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerDetailSet") is not None:
            self._LoadBalancerDetailSet = []
            for item in params.get("LoadBalancerDetailSet"):
                obj = LoadBalancerDetail()
                obj._deserialize(item)
                self._LoadBalancerDetailSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: CLB instance IDs. There can be up to 20 IDs.
        :type LoadBalancerIds: list of str
        :param _LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param _Forward: CLB instance type. 1: generic CLB instance; 0: classic CLB instance
        :type Forward: int
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _Domain: The domain name that Tencent Cloud assigned for the CLB instance.
        :type Domain: str
        :param _LoadBalancerVips: VIP address of a CLB instance (there can be multiple addresses)
        :type LoadBalancerVips: list of str
        :param _BackendPublicIps: Public IPs of the backend services bound with the load balancer. Only the public IPs of CVMs are supported now.
        :type BackendPublicIps: list of str
        :param _BackendPrivateIps: Private IPs of the backend services bound with the load balancer. Only the private IPs of CVMs are supported now.
        :type BackendPrivateIps: list of str
        :param _Offset: Data offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _OrderBy: Sort by parameter. Value range: LoadBalancerName, CreateTime, Domain, LoadBalancerType.
        :type OrderBy: str
        :param _OrderType: 1: reverse; 0: sequential. Default value: reverse by creation time |
        :type OrderType: int
        :param _SearchKey: Search field which fuzzy matches name, domain name, or VIP.
        :type SearchKey: str
        :param _ProjectId: ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API.
        :type ProjectId: int
        :param _WithRs: Whether a CLB instance is bound to a real server. 0: no; 1: yes; -1: query all.
        :type WithRs: int
        :param _VpcId: VPC where a CLB instance resides, such as vpc-bhqkbhdx.
Basic network does not support queries by VpcId.
        :type VpcId: str
        :param _SecurityGroup: Security group ID, e.g., `sg-m1cc****`.
        :type SecurityGroup: str
        :param _MasterZone: Primary AZ ID, e.g., `100001` (Guangzhou Zone 1).
        :type MasterZone: str
        :param _Filters: Each request can have up to 10 `Filters` and 100 `Filter.Values`. Detailed filter conditions:
<li> internet-charge-type - Type: String - Required: No - Filter by CLB network billing mode, including `TRAFFIC_POSTPAID_BY_HOUR`</li>
        :type Filters: list of Filter
        """
        self._LoadBalancerIds = None
        self._LoadBalancerType = None
        self._Forward = None
        self._LoadBalancerName = None
        self._Domain = None
        self._LoadBalancerVips = None
        self._BackendPublicIps = None
        self._BackendPrivateIps = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderType = None
        self._SearchKey = None
        self._ProjectId = None
        self._WithRs = None
        self._VpcId = None
        self._SecurityGroup = None
        self._MasterZone = None
        self._Filters = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def BackendPublicIps(self):
        return self._BackendPublicIps

    @BackendPublicIps.setter
    def BackendPublicIps(self, BackendPublicIps):
        self._BackendPublicIps = BackendPublicIps

    @property
    def BackendPrivateIps(self):
        return self._BackendPrivateIps

    @BackendPrivateIps.setter
    def BackendPrivateIps(self, BackendPrivateIps):
        self._BackendPrivateIps = BackendPrivateIps

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

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WithRs(self):
        return self._WithRs

    @WithRs.setter
    def WithRs(self, WithRs):
        self._WithRs = WithRs

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Domain = params.get("Domain")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._BackendPublicIps = params.get("BackendPublicIps")
        self._BackendPrivateIps = params.get("BackendPrivateIps")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._SearchKey = params.get("SearchKey")
        self._ProjectId = params.get("ProjectId")
        self._WithRs = params.get("WithRs")
        self._VpcId = params.get("VpcId")
        self._SecurityGroup = params.get("SecurityGroup")
        self._MasterZone = params.get("MasterZone")
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
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of CLB instances that meet the filter criteria. This value is independent of the Limit in the input parameter.
        :type TotalCount: int
        :param _LoadBalancerSet: Array of returned CLB instances.
        :type LoadBalancerSet: list of LoadBalancer
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    """DescribeQuota request structure.

    """


class DescribeQuotaResponse(AbstractModel):
    """DescribeQuota response structure.

    """

    def __init__(self):
        r"""
        :param _QuotaSet: Quota list
        :type QuotaSet: list of Quota
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QuotaSet = None
        self._RequestId = None

    @property
    def QuotaSet(self):
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned AZ resources. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Starting offset of the returned AZ resource list. Default value: 0.
        :type Offset: int
        :param _Filters: Filter to query the list of AZ resources as detailed below:
<li> `zone` - String - Optional - Filter by AZ, such as "ap-guangzhou-1".</li>
<li> `isp` -- String - Optional - Filter by the ISP. Values: `BGP`, `CMCC`, `CUCC` and `CTCC`.</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeResourcesResponse(AbstractModel):
    """DescribeResources response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneResourceSet: List of resources supported by the AZ
        :type ZoneResourceSet: list of ZoneResource
        :param _TotalCount: Number of entries in the AZ resource list.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ZoneResourceSet(self):
        return self._ZoneResourceSet

    @ZoneResourceSet.setter
    def ZoneResourceSet(self, ZoneResourceSet):
        self._ZoneResourceSet = ZoneResourceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneResourceSet") is not None:
            self._ZoneResourceSet = []
            for item in params.get("ZoneResourceSet"):
                obj = ZoneResource()
                obj._deserialize(item)
                self._ZoneResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _SourceListenerIds: Array of CLB listener IDs
        :type SourceListenerIds: list of str
        :param _SourceLocationIds: Array of CLB forwarding rule IDs
        :type SourceLocationIds: list of str
        """
        self._LoadBalancerId = None
        self._SourceListenerIds = None
        self._SourceLocationIds = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerIds(self):
        return self._SourceListenerIds

    @SourceListenerIds.setter
    def SourceListenerIds(self, SourceListenerIds):
        self._SourceListenerIds = SourceListenerIds

    @property
    def SourceLocationIds(self):
        return self._SourceLocationIds

    @SourceLocationIds.setter
    def SourceLocationIds(self, SourceLocationIds):
        self._SourceLocationIds = SourceLocationIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerIds = params.get("SourceListenerIds")
        self._SourceLocationIds = params.get("SourceLocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite response structure.

    """

    def __init__(self):
        r"""
        :param _RewriteSet: Array of redirection forwarding rules. If there are no redirection rules, an empty array will be returned.
        :type RewriteSet: list of RuleOutput
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RewriteSet = None
        self._RequestId = None

    @property
    def RewriteSet(self):
        return self._RewriteSet

    @RewriteSet.setter
    def RewriteSet(self, RewriteSet):
        self._RewriteSet = RewriteSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self._RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._RewriteSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter. Currently, only filtering by `TargetGroupId`, `BindIP`, or `InstanceId` is supported.
        :type Filters: list of Filter
        :param _Limit: Number of displayed results. Default value: 20
        :type Limit: int
        :param _Offset: Display offset. Default value: 0
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of results returned for the current query
        :type TotalCount: int
        :param _TargetGroupInstanceSet: Information of the bound server
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param _RealCount: The actual total number of bound instances, which is not affected by the setting of `Limit`, `Offset` and the CAM permissions.
        :type RealCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupInstanceSet = None
        self._RealCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupInstanceSet(self):
        return self._TargetGroupInstanceSet

    @TargetGroupInstanceSet.setter
    def TargetGroupInstanceSet(self, TargetGroupInstanceSet):
        self._TargetGroupInstanceSet = TargetGroupInstanceSet

    @property
    def RealCount(self):
        return self._RealCount

    @RealCount.setter
    def RealCount(self, RealCount):
        self._RealCount = RealCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self._TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self._TargetGroupInstanceSet.append(obj)
        self._RealCount = params.get("RealCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: Target group ID array
        :type TargetGroupIds: list of str
        :param _Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`. Target group ID will be used first.
        :type Filters: list of Filter
        :param _Offset: Starting display offset
        :type Offset: int
        :param _Limit: Limit of the number of displayed results. Default value: 20.
        :type Limit: int
        """
        self._TargetGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of displayed results
        :type TotalCount: int
        :param _TargetGroupSet: Information set of displayed target groups
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: Target group ID, which is exclusive of `Filters`.
        :type TargetGroupIds: list of str
        :param _Limit: Limit of the number of displayed results. Default value: 20.
        :type Limit: int
        :param _Offset: Starting display offset
        :type Offset: int
        :param _Filters: Filter array, which is exclusive of `TargetGroupIds`. Valid values: `TargetGroupVpcId` and `TargetGroupName`.
        :type Filters: list of Filter
        """
        self._TargetGroupIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of displayed results
        :type TotalCount: int
        :param _TargetGroupSet: Information set of displayed target groups
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: List of IDs of CLB instances to be queried
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: CLB instance list
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancerHealth
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerIds: List of listener IDs (20 IDs at most).
        :type ListenerIds: list of str
        :param _Protocol: Listener protocol type
        :type Protocol: str
        :param _Port: Listener port
        :type Port: int
        :param _Filters: Query the list of backend services associated with a load balancer
<li> `location-id` - String - Optional - Rule ID, such as "loc-12345678".</li>
<li> `private-ip-address` - String - Optional - Backend service private IP, such as `172.16.1.1`</li>
        :type Filters: list of Filter
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None
        self._Filters = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
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
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Information of real servers bound to the listener
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerBackend
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Request ID, i.e., the RequestId parameter returned by the API.
        :type TaskId: str
        :param _DealName: Order ID.
Note: Either `TaskId` or `DealName` is required.
        :type DealName: str
        """
        self._TaskId = None
        self._DealName = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Current status of a task. Value range: 0 (succeeded), 1 (failed), 2 (in progress).
        :type Status: int
        :param _LoadBalancerIds: Array of unique CLB instance IDs.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._LoadBalancerIds = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Associations: Array of rules to be unbound
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups response structure.

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


class ExclusiveCluster(AbstractModel):
    """Dedicated cluster

    """

    def __init__(self):
        r"""
        :param _L4Clusters: Layer-4 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.
        :type L4Clusters: list of ClusterItem
        :param _L7Clusters: Layer-7 dedicated cluster list
Note: this field may return null, indicating that no valid values can be obtained.
        :type L7Clusters: list of ClusterItem
        :param _ClassicalCluster: vpcgw cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`
        """
        self._L4Clusters = None
        self._L7Clusters = None
        self._ClassicalCluster = None

    @property
    def L4Clusters(self):
        return self._L4Clusters

    @L4Clusters.setter
    def L4Clusters(self, L4Clusters):
        self._L4Clusters = L4Clusters

    @property
    def L7Clusters(self):
        return self._L7Clusters

    @L7Clusters.setter
    def L7Clusters(self, L7Clusters):
        self._L7Clusters = L7Clusters

    @property
    def ClassicalCluster(self):
        return self._ClassicalCluster

    @ClassicalCluster.setter
    def ClassicalCluster(self, ClassicalCluster):
        self._ClassicalCluster = ClassicalCluster


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self._L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self._L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self._L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self._L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self._ClassicalCluster = ClusterItem()
            self._ClassicalCluster._deserialize(params.get("ClassicalCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfo(AbstractModel):
    """Reserved field which can be ignored generally.

    """

    def __init__(self):
        r"""
        :param _ZhiTong: Whether to enable VIP direct connection
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZhiTong: bool
        :param _TgwGroupName: TgwGroup name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TgwGroupName: str
        """
        self._ZhiTong = None
        self._TgwGroupName = None

    @property
    def ZhiTong(self):
        return self._ZhiTong

    @ZhiTong.setter
    def ZhiTong(self, ZhiTong):
        self._ZhiTong = ZhiTong

    @property
    def TgwGroupName(self):
        return self._TgwGroupName

    @TgwGroupName.setter
    def TgwGroupName(self, TgwGroupName):
        self._TgwGroupName = TgwGroupName


    def _deserialize(self, params):
        self._ZhiTong = params.get("ZhiTong")
        self._TgwGroupName = params.get("TgwGroupName")
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
        :param _Name: Filter name
        :type Name: str
        :param _Values: Filter value array
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    """SCF related information

    """

    def __init__(self):
        r"""
        :param _FunctionNamespace: Function namespace
        :type FunctionNamespace: str
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _FunctionQualifier: Function version name or alias
        :type FunctionQualifier: str
        :param _FunctionQualifierType: Function qualifier type. Values: `VERSION`, `ALIAS`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FunctionQualifierType: str
        """
        self._FunctionNamespace = None
        self._FunctionName = None
        self._FunctionQualifier = None
        self._FunctionQualifierType = None

    @property
    def FunctionNamespace(self):
        return self._FunctionNamespace

    @FunctionNamespace.setter
    def FunctionNamespace(self, FunctionNamespace):
        self._FunctionNamespace = FunctionNamespace

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionQualifier(self):
        return self._FunctionQualifier

    @FunctionQualifier.setter
    def FunctionQualifier(self, FunctionQualifier):
        self._FunctionQualifier = FunctionQualifier

    @property
    def FunctionQualifierType(self):
        return self._FunctionQualifierType

    @FunctionQualifierType.setter
    def FunctionQualifierType(self, FunctionQualifierType):
        self._FunctionQualifierType = FunctionQualifierType


    def _deserialize(self, params):
        self._FunctionNamespace = params.get("FunctionNamespace")
        self._FunctionName = params.get("FunctionName")
        self._FunctionQualifier = params.get("FunctionQualifier")
        self._FunctionQualifierType = params.get("FunctionQualifierType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionTarget(AbstractModel):
    """Whether to use SCF (Serverless Cloud Function) as the backend service

    """

    def __init__(self):
        r"""
        :param _Function: SCF related information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Function: :class:`tencentcloud.clb.v20180317.models.FunctionInfo`
        :param _Weight: Weight
        :type Weight: int
        """
        self._Function = None
        self._Weight = None

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        if params.get("Function") is not None:
            self._Function = FunctionInfo()
            self._Function._deserialize(params.get("Function"))
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """Health check information.
    Note: Custom check parameters are currently supported only in certain beta test regions.

    """

    def __init__(self):
        r"""
        :param _HealthSwitch: Whether to enable health check. 1: enable; 0: disable.
        :type HealthSwitch: int
        :param _TimeOut: Health check response timeout period in seconds (applicable only to layer-4 listeners). Value range: 2-60. Default value: 2. This parameter should be less than the check interval.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeOut: int
        :param _IntervalTime: Health check probing interval period. It defaults to `5`. For IPv4 CLB instances, the range is 2-300. For IPv6 CLB instances, the range is 5-300. Unit: second
Note: For some IPv4 CLB instances created long ago, the range is 5-300.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntervalTime: int
        :param _HealthNum: Health threshold. Default value: 3, indicating that if a forward is found healthy three consecutive times, it is considered to be normal. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthNum: int
        :param _UnHealthNum: Unhealthy threshold. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it is considered to be exceptional. Value range: 2-10
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnHealthNum: int
        :param _HttpCode: Health check status code (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: 1-31. Default value: 31.
`1`: Returns code 1xx for healthy status. `2`: Returns code 2xx for healthy status. `4`: Returns code 3xx for healthy status. `8`: Returns code 4xx for healthy status. `16`: Returns code 5xx for healthy status. If you want multiple return codes to represent healthy, sum up the corresponding values. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HttpCode: int
        :param _HttpCheckPath: Health check path (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners).
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCheckPath: str
        :param _HttpCheckDomain: Health check domain name. It’s applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners. It’s required for HTTP health check of TCP listeners.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type HttpCheckDomain: str
        :param _HttpCheckMethod: Health check method (applicable only to HTTP/HTTPS forwarding rules and HTTP health checks of TCP listeners). Value range: HEAD, GET. Default value: HEAD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpCheckMethod: str
        :param _CheckPort: Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, it is recommended to leave it empty. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckPort: int
        :param _ContextType: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the input format of the health check. Value range: HEX, TEXT. If the value is HEX, the characters of SendContext and RecvContext can only be selected from 0123456789ABCDEF and the length must be an even number. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContextType: str
        :param _SendContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the content of the request sent by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SendContext: str
        :param _RecvContext: Health check protocol (a custom check parameter), which is required if the value of CheckType is CUSTOM. This parameter represents the result returned by the health check. Only ASCII visible characters are allowed, and the maximum length is 500. (Applicable only to TCP/UDP listeners.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecvContext: str
        :param _CheckType: u200dHealth check protocol. Values: `TCP`, `HTTP`, `HTTPS`, `GRPC`, `PING`, and `CUSTOM`. UDP listeners support `PING`/`CUSTOM`. TCP listener support `TCP`/`HTTP`/`CUSTOM`. TCP_SSL and QUIC listeners support `TCP`/`HTTP`. HTTP rules support `HTTP`/`GRPC. HTTPS rules support `HTTP`/`HTTPS`/`GRPC`.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type CheckType: str
        :param _HttpVersion: HTTP version. HTTP version of the backend service. Values: `HTTP/1.0`, HTTP/1.1`. It is only applicable to TCP listeners, and is required when `CheckType`=`HTTP`. 
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type HttpVersion: str
        :param _SourceIpType: Specifies the type of health check source IP. `0` (default): CLB VIP. `1`: 100.64 IP range.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type SourceIpType: int
        :param _ExtendedCode: GRPC health check status code, which is only applicable to rules with GRPC as the backend forwarding protocol. It can be a single number (such as `20`), multiple numbers (such as `20,25`) or a range (such as `0-99`). The default value is `12`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExtendedCode: str
        """
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnHealthNum = None
        self._HttpCode = None
        self._HttpCheckPath = None
        self._HttpCheckDomain = None
        self._HttpCheckMethod = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._CheckType = None
        self._HttpVersion = None
        self._SourceIpType = None
        self._ExtendedCode = None

    @property
    def HealthSwitch(self):
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnHealthNum(self):
        return self._UnHealthNum

    @UnHealthNum.setter
    def UnHealthNum(self, UnHealthNum):
        self._UnHealthNum = UnHealthNum

    @property
    def HttpCode(self):
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def HttpCheckPath(self):
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def HttpCheckDomain(self):
        return self._HttpCheckDomain

    @HttpCheckDomain.setter
    def HttpCheckDomain(self, HttpCheckDomain):
        self._HttpCheckDomain = HttpCheckDomain

    @property
    def HttpCheckMethod(self):
        return self._HttpCheckMethod

    @HttpCheckMethod.setter
    def HttpCheckMethod(self, HttpCheckMethod):
        self._HttpCheckMethod = HttpCheckMethod

    @property
    def CheckPort(self):
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def HttpVersion(self):
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion

    @property
    def SourceIpType(self):
        return self._SourceIpType

    @SourceIpType.setter
    def SourceIpType(self, SourceIpType):
        self._SourceIpType = SourceIpType

    @property
    def ExtendedCode(self):
        return self._ExtendedCode

    @ExtendedCode.setter
    def ExtendedCode(self, ExtendedCode):
        self._ExtendedCode = ExtendedCode


    def _deserialize(self, params):
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnHealthNum = params.get("UnHealthNum")
        self._HttpCode = params.get("HttpCode")
        self._HttpCheckPath = params.get("HttpCheckPath")
        self._HttpCheckDomain = params.get("HttpCheckDomain")
        self._HttpCheckMethod = params.get("HttpCheckMethod")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._CheckType = params.get("CheckType")
        self._HttpVersion = params.get("HttpVersion")
        self._SourceIpType = params.get("SourceIpType")
        self._ExtendedCode = params.get("ExtendedCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdleLoadBalancer(AbstractModel):
    """ID of the idle CLB instance

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param _Region: CLB instance region
        :type Region: str
        :param _Vip: CLB instance VIP
        :type Vip: str
        :param _IdleReason: The reason why the load balancer is considered idle. `NO_RULES`: No rules configured. `NO_RS`: The rules are not associated with servers.
        :type IdleReason: str
        :param _Status: CLB instance status, including:
`0`: Creating; `1`: Running.
        :type Status: int
        :param _Forward: CLB type. Value range: `1` (CLB); `0` (classic CLB).
        :type Forward: int
        :param _Domain: The load balancing hostname.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Region = None
        self._Vip = None
        self._IdleReason = None
        self._Status = None
        self._Forward = None
        self._Domain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def IdleReason(self):
        return self._IdleReason

    @IdleReason.setter
    def IdleReason(self, IdleReason):
        self._IdleReason = IdleReason

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._IdleReason = params.get("IdleReason")
        self._Status = params.get("Status")
        self._Forward = params.get("Forward")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateLoadBalancerRequest(AbstractModel):
    """InquiryPriceCreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: Network type of the CLB to query. `OPEN`: Public network; `INTERNAL`: Private network is intranet type
        :type LoadBalancerType: str
        :param _LoadBalancerChargeType: The billing mode to query. `POSTPAID`:Pay as you go
        :type LoadBalancerChargeType: str
        :param _LoadBalancerChargePrepaid: Reserved field
        :type LoadBalancerChargePrepaid: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _InternetAccessible: The network billing mode to query 
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _GoodsNum: Number of CLB instances to query. Default value: 1.
        :type GoodsNum: int
        :param _ZoneId: Availability zone in the format of "ap-guangzhou-1"
        :type ZoneId: str
        :param _SlaType: To query the price of monthly subscribed LCU-supported instances, specify the instance specification in this parameter, such as `clb.c3.small`. For PAYG instances, use `SLA`.
        :type SlaType: str
        :param _AddressIPVersion: IP version. Valid values: `IPV4` (default), `IPV6` (IPV6 NAT64 version) or `IPv6FullChain` (IPv6 version). 
        :type AddressIPVersion: str
        :param _VipIsp: ISP of VIP. Values: `CMCC` (China Mobile), `CUCC` (China Unicom) and `CTCC` (China Telecom). You need to activate static single-line IPs. This feature is in beta and is only available in Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu and Chongqing regions. To try it out, please contact your sales rep. If it's specified, the network billing mode must be `BANDWIDTH_PACKAGE`. If it's not specified, BGP is used by default. To query ISPs supported in a region, please use [DescribeResources](https://intl.cloud.tencent.com/document/api/214/70213?from_cn_redirect=1). 
        :type VipIsp: str
        """
        self._LoadBalancerType = None
        self._LoadBalancerChargeType = None
        self._LoadBalancerChargePrepaid = None
        self._InternetAccessible = None
        self._GoodsNum = None
        self._ZoneId = None
        self._SlaType = None
        self._AddressIPVersion = None
        self._VipIsp = None

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerChargeType(self):
        return self._LoadBalancerChargeType

    @LoadBalancerChargeType.setter
    def LoadBalancerChargeType(self, LoadBalancerChargeType):
        self._LoadBalancerChargeType = LoadBalancerChargeType

    @property
    def LoadBalancerChargePrepaid(self):
        return self._LoadBalancerChargePrepaid

    @LoadBalancerChargePrepaid.setter
    def LoadBalancerChargePrepaid(self, LoadBalancerChargePrepaid):
        self._LoadBalancerChargePrepaid = LoadBalancerChargePrepaid

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp


    def _deserialize(self, params):
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerChargeType = params.get("LoadBalancerChargeType")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self._LoadBalancerChargePrepaid = LBChargePrepaid()
            self._LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._GoodsNum = params.get("GoodsNum")
        self._ZoneId = params.get("ZoneId")
        self._SlaType = params.get("SlaType")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._VipIsp = params.get("VipIsp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateLoadBalancerResponse(AbstractModel):
    """InquiryPriceCreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the instance with the specified configurations.
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceModifyLoadBalancerRequest(AbstractModel):
    """InquiryPriceModifyLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _InternetAccessible: New bandwidth bandwidth specification
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        """
        self._LoadBalancerId = None
        self._InternetAccessible = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceModifyLoadBalancerResponse(AbstractModel):
    """InquiryPriceModifyLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Pricing information
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRefundLoadBalancerRequest(AbstractModel):
    """InquiryPriceRefundLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRefundLoadBalancerResponse(AbstractModel):
    """InquiryPriceRefundLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price of the instance with the specified configurations.
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewLoadBalancerRequest(AbstractModel):
    """InquiryPriceRenewLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerChargePrepaid: Renewal period
        :type LoadBalancerChargePrepaid: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        """
        self._LoadBalancerId = None
        self._LoadBalancerChargePrepaid = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerChargePrepaid(self):
        return self._LoadBalancerChargePrepaid

    @LoadBalancerChargePrepaid.setter
    def LoadBalancerChargePrepaid(self, LoadBalancerChargePrepaid):
        self._LoadBalancerChargePrepaid = LoadBalancerChargePrepaid


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self._LoadBalancerChargePrepaid = LBChargePrepaid()
            self._LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewLoadBalancerResponse(AbstractModel):
    """InquiryPriceRenewLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price to renew
        :type Price: :class:`tencentcloud.clb.v20180317.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InternetAccessible(AbstractModel):
    """Network billing mode based on maximum outbound bandwidth

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR: hourly pay-as-you-go by traffic; BANDWIDTH_POSTPAID_BY_HOUR: hourly pay-as-you-go by bandwidth;
BANDWIDTH_PACKAGE: billed by bandwidth package (currently, this method is supported only if the ISP is specified)
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: Maximum outgoing bandwidth in Mbps. It works on LCU-supported instances on private networks and all instances on public networks.
- For shared and dedicated CLB instances on public networks, the range is 1Mbps-2048Mbps.
- For all LCU-supported CLB instances:
  - It defaults to General LCU-supported instance. SLA corresponds to Super Large 1, and the range of maximum outgoing bandwidth is 1 Mbps - 10240 Mbps.
  - If you have enabled Super Large specification, the range of maximum outgoing bandwidth is 1 Mbps - 61440 Mbps Super Large LCU-supported specification is in beta now. To join the beta, [submit a ticket](https://console.cloud.tencent.com/workorder/category).
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        :param _BandwidthpkgSubType: Bandwidth package type, such as SINGLEISP
Note: This field may return null, indicating that no valid values can be obtained.
        :type BandwidthpkgSubType: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._BandwidthpkgSubType = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthpkgSubType(self):
        return self._BandwidthpkgSubType

    @BandwidthpkgSubType.setter
    def BandwidthpkgSubType(self, BandwidthpkgSubType):
        self._BandwidthpkgSubType = BandwidthpkgSubType


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._BandwidthpkgSubType = params.get("BandwidthpkgSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """Pricing information of an item

    """

    def __init__(self):
        r"""
        :param _UnitPrice: PAYG unit price, in USD.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _ChargeUnit: Subsequent billing unit. Value Range: 
`HOUR`: Calculate the cost by hour. It's available when "InternetChargeType=POSTPAID_BY_HOUR".
`GB`: Calculate the cost by traffic in GB. It's available when "InternetChargeType=TRAFFIC_POSTPAID_BY_HOUR".
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ChargeUnit: str
        :param _OriginalPrice: Reserved field
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Reserved field
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _UnitPriceDiscount: Discount unit price of a pay-as-you-go instance, in USD.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _Discount: Discount. For example, 20.0 indicates 80% off.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Discount: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPriceDiscount = None
        self._Discount = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._Discount = params.get("Discount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBChargePrepaid(AbstractModel):
    """Monthly subscription configuration of a CLB instance

    """

    def __init__(self):
        r"""
        :param _RenewFlag: Renewal type. AUTO_RENEW: automatic renewal; MANUAL_RENEW: manual renewal
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: str
        :param _Period: Cycle, indicating the number of months (reserved field)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Period: int
        """
        self._RenewFlag = None
        self._Period = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBItem(AbstractModel):
    """Querying the binding relation of the CLB instance

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: String ID of the CLB instance.
        :type LoadBalancerId: str
        :param _Vip: VIP of the CLB instance.
        :type Vip: str
        :param _Listeners: Listener rule.
        :type Listeners: list of ListenerItem
        :param _Region: Region of the CLB instance
        :type Region: str
        """
        self._LoadBalancerId = None
        self._Vip = None
        self._Listeners = None
        self._Region = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Vip = params.get("Vip")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerItem()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LbRsItem(AbstractModel):
    """Querying the input data types

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _PrivateIp: Private network IP to be queried, which can be of the CVM or ENI.
        :type PrivateIp: str
        """
        self._VpcId = None
        self._PrivateIp = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._PrivateIp = params.get("PrivateIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LbRsTargets(AbstractModel):
    """Querying the output data types

    """

    def __init__(self):
        r"""
        :param _Type: Private network IP type, which can be `cvm` or `eni`.
        :type Type: str
        :param _PrivateIp: Private network IP of the real server.
        :type PrivateIp: str
        :param _Port: Port bound to the real server.
        :type Port: int
        :param _VpcId: VPC ID of the real server.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VpcId: int
        :param _Weight: Weight of the real server.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self._Type = None
        self._PrivateIp = None
        self._Port = None
        self._VpcId = None
        self._Weight = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PrivateIp = params.get("PrivateIp")
        self._Port = params.get("Port")
        self._VpcId = params.get("VpcId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """Listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Protocol: Listener protocol
        :type Protocol: str
        :param _Port: Listener port
        :type Port: int
        :param _Certificate: Information of certificates bound to the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param _HealthCheck: Health check information of the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Scheduler: Request scheduling method
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scheduler: str
        :param _SessionExpireTime: Session persistence time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionExpireTime: int
        :param _SniSwitch: Whether to enable SNI. `1`: Enable; `0`: Do not enable. This parameter is only meaningful for HTTPS listeners.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SniSwitch: int
        :param _Rules: All forwarding rules under a listener (this parameter is meaningful only for HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleOutput
        :param _ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _CreateTime: Listener creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _EndPort: End port of a port range
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        :param _TargetType: Real server type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetType: str
        :param _TargetGroup: Basic information of a bound target group. This field will be returned when a target group is bound to a listener.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param _SessionType: Session persistence type. Valid values: Normal: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionType: str
        :param _KeepaliveEnable: Whether a persistent connection is enabled (1: enabled; 0: disabled). This parameter can only be configured in HTTP/HTTPS listeners.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KeepaliveEnable: int
        :param _Toa: Only the NAT64 CLB TCP listeners are supported.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Toa: bool
        :param _DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeregisterTargetRst: bool
        :param _AttrFlags: Attribute of listener
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AttrFlags: list of str
        :param _TargetGroupList: List of bound target groups
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetGroupList: list of BasicTargetGroupInfo
        :param _MaxConn: Maximum number of concurrent listener connections. If it’s set to `-1`, the listener speed is not limited. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MaxConn: int
        :param _MaxCps: Maximum number of new listener connections. If it’s set to `-1`, the listener speed is not limited. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MaxCps: int
        :param _IdleConnectTimeout: Connection idle timeout period (in seconds). It’s only available to TCP listeners. Value range: 300-900 for shared and dedicated instances; 300-2000 for LCU-supported CLB instances. It defaults to 900.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IdleConnectTimeout: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Certificate = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._SniSwitch = None
        self._Rules = None
        self._ListenerName = None
        self._CreateTime = None
        self._EndPort = None
        self._TargetType = None
        self._TargetGroup = None
        self._SessionType = None
        self._KeepaliveEnable = None
        self._Toa = None
        self._DeregisterTargetRst = None
        self._AttrFlags = None
        self._TargetGroupList = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetGroup(self):
        return self._TargetGroup

    @TargetGroup.setter
    def TargetGroup(self, TargetGroup):
        self._TargetGroup = TargetGroup

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def Toa(self):
        return self._Toa

    @Toa.setter
    def Toa(self, Toa):
        self._Toa = Toa

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def AttrFlags(self):
        return self._AttrFlags

    @AttrFlags.setter
    def AttrFlags(self, AttrFlags):
        self._AttrFlags = AttrFlags

    @property
    def TargetGroupList(self):
        return self._TargetGroupList

    @TargetGroupList.setter
    def TargetGroupList(self, TargetGroupList):
        self._TargetGroupList = TargetGroupList

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateOutput()
            self._Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ListenerName = params.get("ListenerName")
        self._CreateTime = params.get("CreateTime")
        self._EndPort = params.get("EndPort")
        self._TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self._TargetGroup = BasicTargetGroupInfo()
            self._TargetGroup._deserialize(params.get("TargetGroup"))
        self._SessionType = params.get("SessionType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._Toa = params.get("Toa")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        self._AttrFlags = params.get("AttrFlags")
        if params.get("TargetGroupList") is not None:
            self._TargetGroupList = []
            for item in params.get("TargetGroupList"):
                obj = BasicTargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupList.append(obj)
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """Details of real servers bound to a listener

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Protocol: Listener protocol
        :type Protocol: str
        :param _Port: Listener port
        :type Port: int
        :param _Rules: Information of rules under a listener (applicable only to HTTP/HTTPS listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleTargets
        :param _Targets: List of real servers bound to a listener (applicable only to TCP/UDP/TCP_SSL listeners)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        :param _EndPort: Ending port in port range if port range is supported; 0 if port range is not supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Rules = None
        self._Targets = None
        self._EndPort = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """Health check information of the listener

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _Protocol: Listener protocol
        :type Protocol: str
        :param _Port: Listener port
        :type Port: int
        :param _Rules: List of forwarding rules of the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleHealth
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._Port = None
        self._Rules = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

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

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerItem(AbstractModel):
    """Querying the listener type

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Protocol: Listener protocol.
        :type Protocol: str
        :param _Port: Listener port.
        :type Port: int
        :param _Rules: Bound rule.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rules: list of RulesItems
        :param _Targets: Object bound to the layer-4 listener.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Targets: list of LbRsTargets
        :param _EndPort: End port of the listener.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Rules = None
        self._Targets = None
        self._EndPort = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RulesItems()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """CLB instance information

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerType: CLB instance network type:
OPEN: public network; INTERNAL: private network.
        :type LoadBalancerType: str
        :param _Forward: CLB type identifier. Value range: 1 (CLB); 0 (classic CLB).
        :type Forward: int
        :param _Domain: Domain name of the CLB instance. It is only available for public classic CLBs. This parameter will be discontinued soon. Please use `LoadBalancerDomain` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _LoadBalancerVips: List of VIPs of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerVips: list of str
        :param _Status: CLB instance status, including:
0: creating; 1: running.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _CreateTime: CLB instance creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _StatusTime: Last status change time of a CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusTime: str
        :param _ProjectId: ID of the project to which a CLB instance belongs. 0: default project.
        :type ProjectId: int
        :param _VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _OpenBgp: Protective CLB identifier. Value range: 1 (protective), 0 (non-protective).
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpenBgp: int
        :param _Snat: SNAT is enabled for all private network classic CLB created before December 2016.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Snat: bool
        :param _Isolation: 0: not isolated; 1: isolated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Isolation: int
        :param _Log: Log information. Only the public network CLB that have HTTP or HTTPS listeners can generate logs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Log: str
        :param _SubnetId: Subnet where a CLB instance resides (meaningful only for private network VPC CLB)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _Tags: CLB instance tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param _SecureGroups: Security group of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecureGroups: list of str
        :param _TargetRegionInfo: Basic information of a backend server bound to a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param _AnycastZone: Anycast CLB publishing region. For non-anycast CLB, this field returns an empty string.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AnycastZone: str
        :param _AddressIPVersion: IP version. Valid values: ipv4, ipv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPVersion: str
        :param _NumericalVpcId: VPC ID in a numeric form
Note: This field may return null, indicating that no valid values can be obtained.
        :type NumericalVpcId: int
        :param _VipIsp: ISP to which a CLB IP address belongs
Note: This field may return null, indicating that no valid values can be obtained.
        :type VipIsp: str
        :param _MasterZone: Primary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`
        :param _BackupZoneSet: Secondary AZ
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupZoneSet: list of ZoneInfo
        :param _IsolatedTime: CLB instance isolation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param _ExpireTime: CLB instance expiration time, which takes effect only for prepaid instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _ChargeType: Billing mode of CLB instance. Valid values: PREPAID (monthly subscription), POSTPAID_BY_HOUR (pay as you go).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _NetworkAttributes: CLB instance network attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _PrepaidAttributes: Prepaid billing attributes of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _LogSetId: Logset ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetId: str
        :param _LogTopicId: Log topic ID of CLB Log Service (CLS)
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogTopicId: str
        :param _AddressIPv6: IPv6 address of a CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param _ExtraInfo: Reserved field which can be ignored generally.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param _IsDDos: Whether an Anti-DDoS Pro instance can be bound
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDDos: bool
        :param _ConfigId: Custom configuration ID at the CLB instance level
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigId: str
        :param _LoadBalancerPassToTarget: Whether a real server opens the traffic from a CLB instance to the internet
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: bool
        :param _ExclusiveCluster: Private network dedicated cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param _IPv6Mode: This field is meaningful only when the IP address version is `ipv6`. Valid values: IPv6Nat64, IPv6FullChain
Note: this field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param _SnatPro: Whether to enable SnatPro.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SnatPro: bool
        :param _SnatIps: `SnatIp` list after SnatPro load balancing is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SnatIps: list of SnatIp
        :param _SlaType: Specification of the LCU-supported instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaType: str
        :param _IsBlock: Whether VIP is blocked
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsBlock: bool
        :param _IsBlockTime: Time blocked or unblocked
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsBlockTime: str
        :param _LocalBgp: Whether the IP type is the local BGP
        :type LocalBgp: bool
        :param _ClusterTag: Dedicated layer-7 tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterTag: str
        :param _MixIpTarget: If the layer-7 listener of an IPv6FullChain CLB instance is enabled, the CLB instance can be bound with an IPv4 and an IPv6 CVM instance simultaneously.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MixIpTarget: bool
        :param _Zones: Availability zone of a VPC-based private network CLB instance
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _NfvInfo: Whether it is an NFV CLB instance. No returned information: no; l7nfv: yes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NfvInfo: str
        :param _HealthLogSetId: Health check logset ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type HealthLogSetId: str
        :param _HealthLogTopicId: Health check log topic ID of CLB CLS
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type HealthLogTopicId: str
        :param _ClusterIds: Cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterIds: list of str
        :param _AttributeFlags: CLB attribute
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AttributeFlags: list of str
        :param _LoadBalancerDomain: Domain name of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerDomain: str
        :param _Egress: Network egress
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Egress: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._Forward = None
        self._Domain = None
        self._LoadBalancerVips = None
        self._Status = None
        self._CreateTime = None
        self._StatusTime = None
        self._ProjectId = None
        self._VpcId = None
        self._OpenBgp = None
        self._Snat = None
        self._Isolation = None
        self._Log = None
        self._SubnetId = None
        self._Tags = None
        self._SecureGroups = None
        self._TargetRegionInfo = None
        self._AnycastZone = None
        self._AddressIPVersion = None
        self._NumericalVpcId = None
        self._VipIsp = None
        self._MasterZone = None
        self._BackupZoneSet = None
        self._IsolatedTime = None
        self._ExpireTime = None
        self._ChargeType = None
        self._NetworkAttributes = None
        self._PrepaidAttributes = None
        self._LogSetId = None
        self._LogTopicId = None
        self._AddressIPv6 = None
        self._ExtraInfo = None
        self._IsDDos = None
        self._ConfigId = None
        self._LoadBalancerPassToTarget = None
        self._ExclusiveCluster = None
        self._IPv6Mode = None
        self._SnatPro = None
        self._SnatIps = None
        self._SlaType = None
        self._IsBlock = None
        self._IsBlockTime = None
        self._LocalBgp = None
        self._ClusterTag = None
        self._MixIpTarget = None
        self._Zones = None
        self._NfvInfo = None
        self._HealthLogSetId = None
        self._HealthLogTopicId = None
        self._ClusterIds = None
        self._AttributeFlags = None
        self._LoadBalancerDomain = None
        self._Egress = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OpenBgp(self):
        return self._OpenBgp

    @OpenBgp.setter
    def OpenBgp(self, OpenBgp):
        self._OpenBgp = OpenBgp

    @property
    def Snat(self):
        return self._Snat

    @Snat.setter
    def Snat(self, Snat):
        self._Snat = Snat

    @property
    def Isolation(self):
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecureGroups(self):
        return self._SecureGroups

    @SecureGroups.setter
    def SecureGroups(self, SecureGroups):
        self._SecureGroups = SecureGroups

    @property
    def TargetRegionInfo(self):
        return self._TargetRegionInfo

    @TargetRegionInfo.setter
    def TargetRegionInfo(self, TargetRegionInfo):
        self._TargetRegionInfo = TargetRegionInfo

    @property
    def AnycastZone(self):
        return self._AnycastZone

    @AnycastZone.setter
    def AnycastZone(self, AnycastZone):
        self._AnycastZone = AnycastZone

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def VipIsp(self):
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def BackupZoneSet(self):
        return self._BackupZoneSet

    @BackupZoneSet.setter
    def BackupZoneSet(self, BackupZoneSet):
        self._BackupZoneSet = BackupZoneSet

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def AddressIPv6(self):
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def IsDDos(self):
        return self._IsDDos

    @IsDDos.setter
    def IsDDos(self, IsDDos):
        self._IsDDos = IsDDos

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def IPv6Mode(self):
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def IsBlock(self):
        return self._IsBlock

    @IsBlock.setter
    def IsBlock(self, IsBlock):
        self._IsBlock = IsBlock

    @property
    def IsBlockTime(self):
        return self._IsBlockTime

    @IsBlockTime.setter
    def IsBlockTime(self, IsBlockTime):
        self._IsBlockTime = IsBlockTime

    @property
    def LocalBgp(self):
        return self._LocalBgp

    @LocalBgp.setter
    def LocalBgp(self, LocalBgp):
        self._LocalBgp = LocalBgp

    @property
    def ClusterTag(self):
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def MixIpTarget(self):
        return self._MixIpTarget

    @MixIpTarget.setter
    def MixIpTarget(self, MixIpTarget):
        self._MixIpTarget = MixIpTarget

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NfvInfo(self):
        return self._NfvInfo

    @NfvInfo.setter
    def NfvInfo(self, NfvInfo):
        self._NfvInfo = NfvInfo

    @property
    def HealthLogSetId(self):
        return self._HealthLogSetId

    @HealthLogSetId.setter
    def HealthLogSetId(self, HealthLogSetId):
        self._HealthLogSetId = HealthLogSetId

    @property
    def HealthLogTopicId(self):
        return self._HealthLogTopicId

    @HealthLogTopicId.setter
    def HealthLogTopicId(self, HealthLogTopicId):
        self._HealthLogTopicId = HealthLogTopicId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def AttributeFlags(self):
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Forward = params.get("Forward")
        self._Domain = params.get("Domain")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StatusTime = params.get("StatusTime")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._OpenBgp = params.get("OpenBgp")
        self._Snat = params.get("Snat")
        self._Isolation = params.get("Isolation")
        self._Log = params.get("Log")
        self._SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self._TargetRegionInfo = TargetRegionInfo()
            self._TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self._AnycastZone = params.get("AnycastZone")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self._MasterZone = ZoneInfo()
            self._MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self._BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._BackupZoneSet.append(obj)
        self._IsolatedTime = params.get("IsolatedTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = InternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self._PrepaidAttributes = LBChargePrepaid()
            self._PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        self._AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._IsDDos = params.get("IsDDos")
        self._ConfigId = params.get("ConfigId")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self._IPv6Mode = params.get("IPv6Mode")
        self._SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self._SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self._SnatIps.append(obj)
        self._SlaType = params.get("SlaType")
        self._IsBlock = params.get("IsBlock")
        self._IsBlockTime = params.get("IsBlockTime")
        self._LocalBgp = params.get("LocalBgp")
        self._ClusterTag = params.get("ClusterTag")
        self._MixIpTarget = params.get("MixIpTarget")
        self._Zones = params.get("Zones")
        self._NfvInfo = params.get("NfvInfo")
        self._HealthLogSetId = params.get("HealthLogSetId")
        self._HealthLogTopicId = params.get("HealthLogTopicId")
        self._ClusterIds = params.get("ClusterIds")
        self._AttributeFlags = params.get("AttributeFlags")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    """CLB instance details

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerType: CLB instance network type:
Public: public network; Private: private network.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param _Status: CLB instance status, including:
0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Address: CLB instance VIP.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _AddressIPv6: IPv6 VIP address of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param _AddressIPVersion: IP version of the CLB instance. Valid values: IPv4, IPv6.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIPVersion: str
        :param _IPv6Mode: IPv6 address type of the CLB instance. Valid values: IPv6Nat64, IPv6FullChain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param _Zone: Availability zone where the CLB instance resides.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _AddressIsp: ISP to which the CLB IP address belongs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressIsp: str
        :param _VpcId: ID of the VPC instance to which the CLB instance belongs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _ProjectId: ID of the project to which the CLB instance belongs. 0: default project.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _CreateTime: CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ChargeType: CLB instance billing mode.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _NetworkAttributes: CLB instance network attribute.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _PrepaidAttributes: Pay-as-you-go attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param _ExtraInfo: Reserved field, which can be ignored generally.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param _ConfigId: Custom configuration IDs of CLB instances. Multiple IDs must be separated by commas (,).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigId: str
        :param _Tags: CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param _ListenerId: CLB listener ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Protocol: Listener protocol.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Listener port.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _LocationId: Forwarding rule ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: Forwarding rule path.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _TargetId: ID of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetId: str
        :param _TargetAddress: Address of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetAddress: str
        :param _TargetPort: Listening port of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetPort: int
        :param _TargetWeight: Forwarding weight of target real servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetWeight: int
        :param _Isolation: 0: not isolated; 1: isolated.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Isolation: int
        :param _SecurityGroup: List of the security groups bound to the CLB instance.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroup: list of str
        :param _LoadBalancerPassToTarget: Whether the CLB instance is billed by IP.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: int
        :param _TargetHealth: Health status of the target real server.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetHealth: str
        :param _Domains: List o domain names associated with the forwarding rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Domains: str
        :param _SlaveZone: The secondary zone of multi-AZ CLB instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SlaveZone: list of str
        :param _Zones: The AZ of private CLB instance. This is only available for beta users.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _SniSwitch: Whether to enable SNI. `1`: Enable; `0`: Do not enable. This parameter is only meaningful for HTTPS listeners.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SniSwitch: int
        :param _LoadBalancerDomain: Domain name of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerDomain: str
        :param _Egress: Network egress
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Egress: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._Status = None
        self._Address = None
        self._AddressIPv6 = None
        self._AddressIPVersion = None
        self._IPv6Mode = None
        self._Zone = None
        self._AddressIsp = None
        self._VpcId = None
        self._ProjectId = None
        self._CreateTime = None
        self._ChargeType = None
        self._NetworkAttributes = None
        self._PrepaidAttributes = None
        self._ExtraInfo = None
        self._ConfigId = None
        self._Tags = None
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._TargetId = None
        self._TargetAddress = None
        self._TargetPort = None
        self._TargetWeight = None
        self._Isolation = None
        self._SecurityGroup = None
        self._LoadBalancerPassToTarget = None
        self._TargetHealth = None
        self._Domains = None
        self._SlaveZone = None
        self._Zones = None
        self._SniSwitch = None
        self._LoadBalancerDomain = None
        self._Egress = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AddressIPv6(self):
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def IPv6Mode(self):
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AddressIsp(self):
        return self._AddressIsp

    @AddressIsp.setter
    def AddressIsp(self, AddressIsp):
        self._AddressIsp = AddressIsp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def TargetWeight(self):
        return self._TargetWeight

    @TargetWeight.setter
    def TargetWeight(self, TargetWeight):
        self._TargetWeight = TargetWeight

    @property
    def Isolation(self):
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def TargetHealth(self):
        return self._TargetHealth

    @TargetHealth.setter
    def TargetHealth(self, TargetHealth):
        self._TargetHealth = TargetHealth

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Status = params.get("Status")
        self._Address = params.get("Address")
        self._AddressIPv6 = params.get("AddressIPv6")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._IPv6Mode = params.get("IPv6Mode")
        self._Zone = params.get("Zone")
        self._AddressIsp = params.get("AddressIsp")
        self._VpcId = params.get("VpcId")
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = InternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self._PrepaidAttributes = LBChargePrepaid()
            self._PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._ConfigId = params.get("ConfigId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._TargetId = params.get("TargetId")
        self._TargetAddress = params.get("TargetAddress")
        self._TargetPort = params.get("TargetPort")
        self._TargetWeight = params.get("TargetWeight")
        self._Isolation = params.get("Isolation")
        self._SecurityGroup = params.get("SecurityGroup")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._TargetHealth = params.get("TargetHealth")
        self._Domains = params.get("Domains")
        self._SlaveZone = params.get("SlaveZone")
        self._Zones = params.get("Zones")
        self._SniSwitch = params.get("SniSwitch")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """CLB instance health check status

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param _Listeners: List of listeners
Note: This field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerHealth
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerTraffic(AbstractModel):
    """CLB instance traffic data

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param _Region: CLB instance region
        :type Region: str
        :param _Vip: CLB instance VIP
        :type Vip: str
        :param _OutBandwidth: Maximum outbound bandwidth in Mbps
        :type OutBandwidth: float
        :param _Domain: CLB domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Region = None
        self._Vip = None
        self._OutBandwidth = None
        self._Domain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._OutBandwidth = params.get("OutBandwidth")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _SourceListenerId: Source listener ID
        :type SourceListenerId: str
        :param _TargetListenerId: Target listener ID
        :type TargetListenerId: str
        :param _RewriteInfos: Redirection relationship between forwarding rules
        :type RewriteInfos: list of RewriteLocationMap
        """
        self._LoadBalancerId = None
        self._SourceListenerId = None
        self._TargetListenerId = None
        self._RewriteInfos = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SourceListenerId(self):
        return self._SourceListenerId

    @SourceListenerId.setter
    def SourceListenerId(self, SourceListenerId):
        self._SourceListenerId = SourceListenerId

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def RewriteInfos(self):
        return self._RewriteInfos

    @RewriteInfos.setter
    def RewriteInfos(self, RewriteInfos):
        self._RewriteInfos = RewriteInfos


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SourceListenerId = params.get("SourceListenerId")
        self._TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self._RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self._RewriteInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite response structure.

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


class MigrateClassicalLoadBalancersRequest(AbstractModel):
    """MigrateClassicalLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of classic CLB instance IDs
        :type LoadBalancerIds: list of str
        :param _ExclusiveCluster: Exclusive cluster information
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        """
        self._LoadBalancerIds = None
        self._ExclusiveCluster = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ExclusiveCluster(self):
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ExclusiveCluster") is not None:
            self._ExclusiveCluster = ExclusiveCluster()
            self._ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateClassicalLoadBalancersResponse(AbstractModel):
    """MigrateClassicalLoadBalancers response structure.

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


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: CLB instance ID
        :type LoadBalancerIds: list of str
        :param _Type: Operation type. Valid values:
<li> add_customized_field (sets header initially to enable the blocklist feature)</li>
<li> set_customized_field (modifies header)</li>
<li> del_customized_field (deletes header)</li>
<li> add_blocked (adds IPs to blocklist)</li>
<li> del_blocked (deletes IPs from blocklist)</li>
<li> flush_blocked (clears blocklist)</li>
        :type Type: str
        :param _ClientIPField: Header field that stores real client IPs
        :type ClientIPField: str
        :param _BlockIPList: List of blocked IPs. The array can contain up to 200,000 entries in one operation.
        :type BlockIPList: list of str
        :param _ExpireTime: Expiration time in seconds. Default value: 3600
        :type ExpireTime: int
        :param _AddStrategy: IP adding policy. Valid value: fifo (if a blocklist is full, new IPs added to the blocklist will adopt the first-in first-out policy)
        :type AddStrategy: str
        """
        self._LoadBalancerIds = None
        self._Type = None
        self._ClientIPField = None
        self._BlockIPList = None
        self._ExpireTime = None
        self._AddStrategy = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientIPField(self):
        return self._ClientIPField

    @ClientIPField.setter
    def ClientIPField(self, ClientIPField):
        self._ClientIPField = ClientIPField

    @property
    def BlockIPList(self):
        return self._BlockIPList

    @BlockIPList.setter
    def BlockIPList(self, BlockIPList):
        self._BlockIPList = BlockIPList

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AddStrategy(self):
        return self._AddStrategy

    @AddStrategy.setter
    def AddStrategy(self, AddStrategy):
        self._AddStrategy = AddStrategy


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._Type = params.get("Type")
        self._ClientIPField = params.get("ClientIPField")
        self._BlockIPList = params.get("BlockIPList")
        self._ExpireTime = params.get("ExpireTime")
        self._AddStrategy = params.get("AddStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList response structure.

    """

    def __init__(self):
        r"""
        :param _JodId: Async task ID
        :type JodId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JodId = None
        self._RequestId = None

    @property
    def JodId(self):
        return self._JodId

    @JodId.setter
    def JodId(self, JodId):
        self._JodId = JodId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JodId = params.get("JodId")
        self._RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Domain: The domain name, which must be associated with an existing forwarding rule. If there are multiple domain names, you only need to specify one.
        :type Domain: str
        :param _NewDomain: The one domain name to modify. `NewDomain` and `NewDomains` can not be both specified.
        :type NewDomain: str
        :param _Certificate: Certificate information of the domain name. It is only applicable to listeners with SNI enabled. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.
        :type Http2: bool
        :param _DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.
        :type DefaultServer: bool
        :param _Quic: Whether to enable QUIC. Note: QUIC can be enabled only for HTTPS domain names.
        :type Quic: bool
        :param _NewDefaultServerDomain: Specifies a new default domain name for the listener. This field is used when the original default domain name is disabled. If there are multiple domain names, specify one of them.
        :type NewDefaultServerDomain: str
        :param _NewDomains: The new domain names to modify. `NewDomain` and `NewDomains` can not be both specified.
        :type NewDomains: list of str
        :param _MultiCertInfo: Certificate information of the domain name. It is only applicable to listeners with SNI enabled. You can specify multiple server-side certificates with different algorithm types. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._NewDomain = None
        self._Certificate = None
        self._Http2 = None
        self._DefaultServer = None
        self._Quic = None
        self._NewDefaultServerDomain = None
        self._NewDomains = None
        self._MultiCertInfo = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def NewDomain(self):
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def NewDefaultServerDomain(self):
        return self._NewDefaultServerDomain

    @NewDefaultServerDomain.setter
    def NewDefaultServerDomain(self, NewDefaultServerDomain):
        self._NewDefaultServerDomain = NewDefaultServerDomain

    @property
    def NewDomains(self):
        return self._NewDomains

    @NewDomains.setter
    def NewDomains(self, NewDomains):
        self._NewDomains = NewDomains

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Http2 = params.get("Http2")
        self._DefaultServer = params.get("DefaultServer")
        self._Quic = params.get("Quic")
        self._NewDefaultServerDomain = params.get("NewDefaultServerDomain")
        self._NewDomains = params.get("NewDomains")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes response structure.

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


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID.
        :type ListenerId: str
        :param _Domain: Legacy domain name under a listener.
        :type Domain: str
        :param _NewDomain: New domain name. 	Length limit: 1-120. There are three usage formats: non-regular expression, wildcard, and regular expression. A non-regular expression can only contain letters, digits, "-", and ".". In a wildcard, "*" can only be at the beginning or the end. A regular expressions must begin with a "~".
        :type NewDomain: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._NewDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def NewDomain(self):
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._NewDomain = params.get("NewDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain response structure.

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


class ModifyFunctionTargetsRequest(AbstractModel):
    """ModifyFunctionTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _FunctionTargets: The backend cloud functions to modify
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or `Domain`+`Url`.
        :type LocationId: str
        :param _Domain: Target rule domain name. This parameter does not take effect if `LocationId` is specified.
        :type Domain: str
        :param _Url: Target rule URL. This parameter does not take effect if `LocationId` is specified.
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFunctionTargetsResponse(AbstractModel):
    """ModifyFunctionTargets response structure.

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


class ModifyListenerRequest(AbstractModel):
    """ModifyListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _ListenerName: New listener name
        :type ListenerName: str
        :param _SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param _HealthCheck: Health check parameter. It is only applicable only to TCP, UDP, TCP_SSL and QUIC listeners.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: Certificate information. This parameter is only applicable to HTTPS/TCP_SSL/QUIC listeners. `Certificate` and `MultiCertInfo` cannot be both specified.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Scheduler: Forwarding method of a listener. Value range: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        :param _SniSwitch: Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners. Note: The SNI feature can be enabled but cannot be disabled once enabled.
        :type SniSwitch: int
        :param _TargetType: Target backend type. `NODE`: A single node; `TARGETGROUP`: A target group.
        :type TargetType: str
        :param _KeepaliveEnable: Whether to enable a persistent connection. This parameter is applicable only to HTTP and HTTPS listeners.
        :type KeepaliveEnable: int
        :param _DeregisterTargetRst: Whether to send the TCP RST packet to the client when unbinding a real server. This parameter is applicable to TCP listeners only.
        :type DeregisterTargetRst: bool
        :param _SessionType: Session persistence type. `NORMAL`: default session persistence type (L4/L7 session persistence); `QUIC_CID`: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners.
        :type SessionType: str
        :param _MultiCertInfo: Certificate information. You can specify multiple server-side certificates with different algorithm types. This parameter is only applicable to HTTPS listeners with the SNI feature not enabled. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        :param _MaxConn: The maximum number of concurrent connections at the listener level. This parameter takes effect only on LCU-supported instances and TCP/UDP/TCP_SSL/QUIC listeners. Value range: 1 to the maximum concurrency of the instance. -1 indicates that no limit is set on concurrent connections.
        :type MaxConn: int
        :param _MaxCps: The maximum number of new connections at the listener level. This parameter takes effect only on LCU-supported instances and TCP/UDP/TCP_SSL/QUIC listeners. Value range: 1 to the maximum number of new connections of the instance. -1 indicates that no limit is set on concurrent connections.
        :type MaxCps: int
        :param _IdleConnectTimeout: Connection idle timeout period (in seconds). It’s only available to TCP listeners. Value range: 300-900 for shared and dedicated instances; 300-2000 for LCU-supported CLB instances. It defaults to 900. To set a period longer than 2000 seconds (up to 3600 seconds), please submit a [submit](https://console.cloud.tencent.com/workorder/category). 
        :type IdleConnectTimeout: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._SniSwitch = None
        self._TargetType = None
        self._KeepaliveEnable = None
        self._DeregisterTargetRst = None
        self._SessionType = None
        self._MultiCertInfo = None
        self._MaxConn = None
        self._MaxCps = None
        self._IdleConnectTimeout = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def KeepaliveEnable(self):
        return self._KeepaliveEnable

    @KeepaliveEnable.setter
    def KeepaliveEnable(self, KeepaliveEnable):
        self._KeepaliveEnable = KeepaliveEnable

    @property
    def DeregisterTargetRst(self):
        return self._DeregisterTargetRst

    @DeregisterTargetRst.setter
    def DeregisterTargetRst(self, DeregisterTargetRst):
        self._DeregisterTargetRst = DeregisterTargetRst

    @property
    def SessionType(self):
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo

    @property
    def MaxConn(self):
        return self._MaxConn

    @MaxConn.setter
    def MaxConn(self, MaxConn):
        self._MaxConn = MaxConn

    @property
    def MaxCps(self):
        return self._MaxCps

    @MaxCps.setter
    def MaxCps(self, MaxCps):
        self._MaxCps = MaxCps

    @property
    def IdleConnectTimeout(self):
        return self._IdleConnectTimeout

    @IdleConnectTimeout.setter
    def IdleConnectTimeout(self, IdleConnectTimeout):
        self._IdleConnectTimeout = IdleConnectTimeout


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._SniSwitch = params.get("SniSwitch")
        self._TargetType = params.get("TargetType")
        self._KeepaliveEnable = params.get("KeepaliveEnable")
        self._DeregisterTargetRst = params.get("DeregisterTargetRst")
        self._SessionType = params.get("SessionType")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        self._MaxConn = params.get("MaxConn")
        self._MaxCps = params.get("MaxCps")
        self._IdleConnectTimeout = params.get("IdleConnectTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener response structure.

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


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Unique CLB ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param _TargetRegionInfo: The backend service information of cross-region binding 1.0
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param _InternetChargeInfo: Network billing parameter
        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param _LoadBalancerPassToTarget: Whether the target opens traffic from CLB to the internet. If yes (true), only security groups on CLB will be verified; if no (false), security groups on both CLB and backend instance need to be verified.
        :type LoadBalancerPassToTarget: bool
        :param _SnatPro: Whether to enable cross-region binding 2.0
        :type SnatPro: bool
        :param _DeleteProtect: Specifies whether to enable deletion protection.
        :type DeleteProtect: bool
        :param _ModifyClassicDomain: Modifies the second-level domain name of CLB from mycloud.com to tencentclb.com. Note that the sub-domain names will be changed as well. After the modification, mycloud.com will be invalidated. 
        :type ModifyClassicDomain: bool
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._TargetRegionInfo = None
        self._InternetChargeInfo = None
        self._LoadBalancerPassToTarget = None
        self._SnatPro = None
        self._DeleteProtect = None
        self._ModifyClassicDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def TargetRegionInfo(self):
        return self._TargetRegionInfo

    @TargetRegionInfo.setter
    def TargetRegionInfo(self, TargetRegionInfo):
        self._TargetRegionInfo = TargetRegionInfo

    @property
    def InternetChargeInfo(self):
        return self._InternetChargeInfo

    @InternetChargeInfo.setter
    def InternetChargeInfo(self, InternetChargeInfo):
        self._InternetChargeInfo = InternetChargeInfo

    @property
    def LoadBalancerPassToTarget(self):
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def SnatPro(self):
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def DeleteProtect(self):
        return self._DeleteProtect

    @DeleteProtect.setter
    def DeleteProtect(self, DeleteProtect):
        self._DeleteProtect = DeleteProtect

    @property
    def ModifyClassicDomain(self):
        return self._ModifyClassicDomain

    @ModifyClassicDomain.setter
    def ModifyClassicDomain(self, ModifyClassicDomain):
        self._ModifyClassicDomain = ModifyClassicDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self._TargetRegionInfo = TargetRegionInfo()
            self._TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self._InternetChargeInfo = InternetAccessible()
            self._InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._SnatPro = params.get("SnatPro")
        self._DeleteProtect = params.get("DeleteProtect")
        self._ModifyClassicDomain = params.get("ModifyClassicDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: This parameter can be used to query whether CLB billing mode switch is successful.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerSlaRequest(AbstractModel):
    """ModifyLoadBalancerSla request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerSla: CLB instance information.
        :type LoadBalancerSla: list of SlaUpdateParam
        """
        self._LoadBalancerSla = None

    @property
    def LoadBalancerSla(self):
        return self._LoadBalancerSla

    @LoadBalancerSla.setter
    def LoadBalancerSla(self, LoadBalancerSla):
        self._LoadBalancerSla = LoadBalancerSla


    def _deserialize(self, params):
        if params.get("LoadBalancerSla") is not None:
            self._LoadBalancerSla = []
            for item in params.get("LoadBalancerSla"):
                obj = SlaUpdateParam()
                obj._deserialize(item)
                self._LoadBalancerSla.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerSlaResponse(AbstractModel):
    """ModifyLoadBalancerSla response structure.

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


class ModifyLoadBalancersProjectRequest(AbstractModel):
    """ModifyLoadBalancersProject request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: IDs of CLB instances ID(s).
        :type LoadBalancerIds: list of str
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._LoadBalancerIds = None
        self._ProjectId = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancersProjectResponse(AbstractModel):
    """ModifyLoadBalancersProject response structure.

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


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _LocationId: ID of the forwarding rule to be modified.
        :type LocationId: str
        :param _Url: New forwarding path of the forwarding rule. This parameter is not required if the URL does not need to be modified.
        :type Url: str
        :param _HealthCheck: Health check information
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.
        :type Scheduler: str
        :param _SessionExpireTime: Session persistence time
        :type SessionExpireTime: int
        :param _ForwardType: Forwarding protocol between CLB instance and real server. Default value: HTTP. Valid values: HTTP, HTTPS, and TRPC.
        :type ForwardType: str
        :param _TrpcCallee: TRPC callee server route, which is required when `ForwardType` is "TRPC". This is now only for internal usage.
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC calling service API, which is required when `ForwardType` is "TRPC". This is now only for internal usage.
        :type TrpcFunc: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Url = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._ForwardType = None
        self._TrpcCallee = None
        self._TrpcFunc = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._ForwardType = params.get("ForwardType")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

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


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupName: New name of target group
        :type TargetGroupName: str
        :param _Port: New default port of target group
        :type Port: int
        """
        self._TargetGroupId = None
        self._TargetGroupName = None
        self._Port = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute response structure.

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


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: Array of servers for which to modify ports
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort response structure.

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


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: Array of servers for which to modify weights
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight response structure.

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


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Targets: List of real servers for which to modify the ports
        :type Targets: list of Target
        :param _NewPort: New port of the real server bound to a listener or forwarding rule
        :type NewPort: int
        :param _LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param _Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param _Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._NewPort = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def NewPort(self):
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._NewPort = params.get("NewPort")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort response structure.

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


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param _Domain: Target rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param _Url: Target rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        :param _Targets: List of real servers for which to modify the weights
        :type Targets: list of Target
        :param _Weight: New forwarding weight of a real server. Value range: 0-100. Default value: 10. If the Targets.Weight parameter is set, this parameter will not take effect.
        :type Weight: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None
        self._Weight = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight response structure.

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


class MultiCertInfo(AbstractModel):
    """Information of multiple certificates bound with the load balancer listener or rule.

    """

    def __init__(self):
        r"""
        :param _SSLMode: Authentication type. Values: `UNIDIRECTIONAL` (one-way authentication), `MUTUAL` (two-way authentication)
        :type SSLMode: str
        :param _CertList: List of listener or rule certificates. One-way and two-way authentication are supported. Only one certificate can be specified for one algorithm. If `SSLMode` is `MUTUAL` (two-way authentication), at least one CA certificate is required. 
        :type CertList: list of CertInfo
        """
        self._SSLMode = None
        self._CertList = None

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertList(self):
        return self._CertList

    @CertList.setter
    def CertList(self, CertList):
        self._CertList = CertList


    def _deserialize(self, params):
        self._SSLMode = params.get("SSLMode")
        if params.get("CertList") is not None:
            self._CertList = []
            for item in params.get("CertList"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CertList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Price of CLB instances.

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InstancePrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        :param _BandwidthPrice: Network price.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type BandwidthPrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        :param _LcuPrice: LCU price.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LcuPrice: :class:`tencentcloud.clb.v20180317.models.ItemPrice`
        """
        self._InstancePrice = None
        self._BandwidthPrice = None
        self._LcuPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def BandwidthPrice(self):
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def LcuPrice(self):
        return self._LcuPrice

    @LcuPrice.setter
    def LcuPrice(self, LcuPrice):
        self._LcuPrice = LcuPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = ItemPrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        if params.get("LcuPrice") is not None:
            self._LcuPrice = ItemPrice()
            self._LcuPrice._deserialize(params.get("LcuPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Quota description. All quotas are in the current region.

    """

    def __init__(self):
        r"""
        :param _QuotaId: Quota name. Valid values:
<li> `TOTAL_OPEN_CLB_QUOTA`: Quota of public network CLB instances in the current region</li>
<li> `TOTAL_INTERNAL_CLB_QUOTA`: Quota of private network CLB instances in the current region</li>
<li> `TOTAL_LISTENER_QUOTA`: Quota of listeners under one CLB instance</li>
<li> `TOTAL_LISTENER_RULE_QUOTA`: Quota of forwarding rules under one listener</li>
<li> `TOTAL_TARGET_BIND_QUOTA`: Quota of CVM instances can be bound under one forwarding rule</li>
<li> `TOTAL_SNAP_IP_QUOTA`: Quota of SNAT IPs for cross-region binding 2.0 under one CLB instance </li>
<li> `TOTAL_ISP_CLB_QUOTA`: Quota of triple-ISP (CMCC/CUCC/CTCC) CLB instances in the current region</li>
        :type QuotaId: str
        :param _QuotaCurrent: Currently used quantity. If it is `null`, it is meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type QuotaCurrent: int
        :param _QuotaLimit: Quota limit.
        :type QuotaLimit: int
        """
        self._QuotaId = None
        self._QuotaCurrent = None
        self._QuotaLimit = None

    @property
    def QuotaId(self):
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaCurrent(self):
        return self._QuotaCurrent

    @QuotaCurrent.setter
    def QuotaCurrent(self, QuotaCurrent):
        self._QuotaCurrent = QuotaCurrent

    @property
    def QuotaLimit(self):
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit


    def _deserialize(self, params):
        self._QuotaId = params.get("QuotaId")
        self._QuotaCurrent = params.get("QuotaCurrent")
        self._QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterFunctionTargetsRequest(AbstractModel):
    """RegisterFunctionTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID.
        :type ListenerId: str
        :param _FunctionTargets: SCF functions to be bound.
        :type FunctionTargets: list of FunctionTarget
        :param _LocationId: ID of the target forwarding rule. To bind an SCF function to a L7 forwarding rule, this parameter or `Domain+Url` is required.
        :type LocationId: str
        :param _Domain: Domain name of the target forwarding rule. It is ignored if `LocationId` is specified.
        :type Domain: str
        :param _Url: URL of the target forwarding rule. It is ignored if `LocationId` is specified.
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._FunctionTargets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterFunctionTargetsResponse(AbstractModel):
    """RegisterFunctionTargets response structure.

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


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: Server instance array
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances response structure.

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


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Targets: List of real servers to be bound. Array length limit: 20.
        :type Targets: list of Target
        :param _LocationId: Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url.
        :type LocationId: str
        :param _Domain: Target forwarding rule domain name. This parameter does not take effect if LocationId is specified.
        :type Domain: str
        :param _Url: Target forwarding rule URL. This parameter does not take effect if LocationId is specified.
        :type Url: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets response structure.

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


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Targets: Real server information
        :type Targets: list of ClassicalTargetInfo
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB response structure.

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


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _OldCertificateId: ID of the certificate to be replaced, which can be a server certificate or a client certificate.
        :type OldCertificateId: str
        :param _Certificate: Information such as the content of the new certificate
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        """
        self._OldCertificateId = None
        self._Certificate = None

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate


    def _deserialize(self, params):
        self._OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers response structure.

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


class Resource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param _Type: Specific ISP resource information, Vaules: `CMCC`, `CUCC`, `CTCC`, `BGP`, and `INTERNAL`.
        :type Type: list of str
        :param _Isp: ISP information, such as `CMCC`, `CUCC`, `CTCC`, `BGP`, and `INTERNAL`.
        :type Isp: str
        :param _AvailabilitySet: Available resources
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AvailabilitySet: list of ResourceAvailability
        :param _TypeSet: ISP Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type TypeSet: list of TypeInfo
        """
        self._Type = None
        self._Isp = None
        self._AvailabilitySet = None
        self._TypeSet = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def AvailabilitySet(self):
        return self._AvailabilitySet

    @AvailabilitySet.setter
    def AvailabilitySet(self, AvailabilitySet):
        self._AvailabilitySet = AvailabilitySet

    @property
    def TypeSet(self):
        return self._TypeSet

    @TypeSet.setter
    def TypeSet(self, TypeSet):
        self._TypeSet = TypeSet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Isp = params.get("Isp")
        if params.get("AvailabilitySet") is not None:
            self._AvailabilitySet = []
            for item in params.get("AvailabilitySet"):
                obj = ResourceAvailability()
                obj._deserialize(item)
                self._AvailabilitySet.append(obj)
        if params.get("TypeSet") is not None:
            self._TypeSet = []
            for item in params.get("TypeSet"):
                obj = TypeInfo()
                obj._deserialize(item)
                self._TypeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceAvailability(AbstractModel):
    """Resource availability

    """

    def __init__(self):
        r"""
        :param _Type: Specific ISP resource information. Values: `CMCC`, `CUCC`, `CTCC`, `BGP`.
        :type Type: str
        :param _Availability: Whether the resource is available. Values: `Available`, `Unavailable`
        :type Availability: str
        """
        self._Type = None
        self._Availability = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Availability(self):
        return self._Availability

    @Availability.setter
    def Availability(self, Availability):
        self._Availability = Availability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Availability = params.get("Availability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteLocationMap(AbstractModel):
    """Redirection relationship between forwarding rules

    """

    def __init__(self):
        r"""
        :param _SourceLocationId: Source forwarding rule ID
        :type SourceLocationId: str
        :param _TargetLocationId: ID of the forwarding rule of the destination
        :type TargetLocationId: str
        :param _RewriteCode: Redirection status code. Valid values: 301, 302, and 307.
        :type RewriteCode: int
        :param _TakeUrl: Whether the matched URL is carried in redirection. It is required when configuring `RewriteCode`.
        :type TakeUrl: bool
        :param _SourceDomain: Original domain name of redirection, which must be the corresponding domain name of `SourceLocationId`. It is required when configuring `RewriteCode`.
        :type SourceDomain: str
        """
        self._SourceLocationId = None
        self._TargetLocationId = None
        self._RewriteCode = None
        self._TakeUrl = None
        self._SourceDomain = None

    @property
    def SourceLocationId(self):
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def TargetLocationId(self):
        return self._TargetLocationId

    @TargetLocationId.setter
    def TargetLocationId(self, TargetLocationId):
        self._TargetLocationId = TargetLocationId

    @property
    def RewriteCode(self):
        return self._RewriteCode

    @RewriteCode.setter
    def RewriteCode(self, RewriteCode):
        self._RewriteCode = RewriteCode

    @property
    def TakeUrl(self):
        return self._TakeUrl

    @TakeUrl.setter
    def TakeUrl(self, TakeUrl):
        self._TakeUrl = TakeUrl

    @property
    def SourceDomain(self):
        return self._SourceDomain

    @SourceDomain.setter
    def SourceDomain(self, SourceDomain):
        self._SourceDomain = SourceDomain


    def _deserialize(self, params):
        self._SourceLocationId = params.get("SourceLocationId")
        self._TargetLocationId = params.get("TargetLocationId")
        self._RewriteCode = params.get("RewriteCode")
        self._TakeUrl = params.get("TakeUrl")
        self._SourceDomain = params.get("SourceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteTarget(AbstractModel):
    """Redirect target information

    """

    def __init__(self):
        r"""
        :param _TargetListenerId: Listener ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetListenerId: str
        :param _TargetLocationId: Forwarding rule ID of a redirect target
Note: This field may return null, indicating that there is no redirection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetLocationId: str
        :param _RewriteCode: Redirection status code
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RewriteCode: int
        :param _TakeUrl: Whether the matched URL is carried in redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TakeUrl: bool
        :param _RewriteType: Redirection type. Manual: manual redirection; Auto: automatic redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RewriteType: str
        """
        self._TargetListenerId = None
        self._TargetLocationId = None
        self._RewriteCode = None
        self._TakeUrl = None
        self._RewriteType = None

    @property
    def TargetListenerId(self):
        return self._TargetListenerId

    @TargetListenerId.setter
    def TargetListenerId(self, TargetListenerId):
        self._TargetListenerId = TargetListenerId

    @property
    def TargetLocationId(self):
        return self._TargetLocationId

    @TargetLocationId.setter
    def TargetLocationId(self, TargetLocationId):
        self._TargetLocationId = TargetLocationId

    @property
    def RewriteCode(self):
        return self._RewriteCode

    @RewriteCode.setter
    def RewriteCode(self, RewriteCode):
        self._RewriteCode = RewriteCode

    @property
    def TakeUrl(self):
        return self._TakeUrl

    @TakeUrl.setter
    def TakeUrl(self, TakeUrl):
        self._TakeUrl = TakeUrl

    @property
    def RewriteType(self):
        return self._RewriteType

    @RewriteType.setter
    def RewriteType(self, RewriteType):
        self._RewriteType = RewriteType


    def _deserialize(self, params):
        self._TargetListenerId = params.get("TargetListenerId")
        self._TargetLocationId = params.get("TargetLocationId")
        self._RewriteCode = params.get("RewriteCode")
        self._TakeUrl = params.get("TakeUrl")
        self._RewriteType = params.get("RewriteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsWeightRule(AbstractModel):
    """Modifies the data type of a node weight

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID.
        :type ListenerId: str
        :param _Targets: List of real servers whose weights to modify.
        :type Targets: list of Target
        :param _LocationId: Forwarding rule ID, which is required only for layer-7 rules.
        :type LocationId: str
        :param _Domain: Target rule domain name. This parameter does not take effect if LocationId is specified
        :type Domain: str
        :param _Url: Target rule URL. This parameter does not take effect if LocationId is specified
        :type Url: str
        :param _Weight: The new forwarding weight of the real server. Value range: [0, 100]. This parameter takes lower precedence than `Weight` in [`Targets`](https://intl.cloud.tencent.com/document/api/214/30694?from_cn_redirect=1#Target), which means that this parameter only takes effect when the `Weight` in `RsWeightRule` is left empty.
        :type Weight: int
        """
        self._ListenerId = None
        self._Targets = None
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Weight = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """Health check status of a forwarding rule

    """

    def __init__(self):
        r"""
        :param _LocationId: Forwarding rule ID
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: Forwarding rule Url
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _Targets: Health status of the real server bound to this rule
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Targets: list of TargetHealth
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInput(AbstractModel):
    """HTTP/HTTPS forwarding rule (input)

    """

    def __init__(self):
        r"""
        :param _Url: Forwarding rule path. Length: 1-200.
        :type Url: str
        :param _Domain: The domain name associated with the forwarding rule. It can contain 1-80 characters. Only one domain name can be entered. If you need to enter multiple domain names, use `Domains`.
        :type Domain: str
        :param _SessionExpireTime: Session persistence time in seconds. Value range: 30-3,600. Setting it to 0 indicates that session persistence is disabled.
        :type SessionExpireTime: int
        :param _HealthCheck: Health check information. For more information, please see [Health Check](https://intl.cloud.tencent.com/document/product/214/6097?from_cn_redirect=1)
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: Certificate information. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param _Scheduler: Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH
They represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR.
        :type Scheduler: str
        :param _ForwardType: Forwarding protocol between the CLB instance and backend service. Values: `HTTP`, `HTTPS`, `GRPC` and `TRPC` (only for internal usage). It defaults to `HTTP`.
        :type ForwardType: str
        :param _DefaultServer: Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener.
        :type DefaultServer: bool
        :param _Http2: Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names.
        :type Http2: bool
        :param _TargetType: Target real server type. NODE: binding a general node; TARGETGROUP: binding a target group.
        :type TargetType: str
        :param _TrpcCallee: TRPC callee server route, which is required when `ForwardType` is "TRPC". This is now only for internal usage.
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC calling service API, which is required when `ForwardType` is "TRPC". This is now only for internal usage.
        :type TrpcFunc: str
        :param _Quic: Whether to enable QUIC. Note: QUIC can be enabled only for HTTPS domain names
        :type Quic: bool
        :param _Domains: The domain name associated with the forwarding rule. Each contain 1-80 characters. If you only need to enter one domain name, use `Domain` instead.
        :type Domains: list of str
        :param _MultiCertInfo: Certificate information. You can specify multiple server-side certificates with different algorithm types. `Certificate` and `MultiCertInfo` cannot be specified at the same time. 
        :type MultiCertInfo: :class:`tencentcloud.clb.v20180317.models.MultiCertInfo`
        """
        self._Url = None
        self._Domain = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._ForwardType = None
        self._DefaultServer = None
        self._Http2 = None
        self._TargetType = None
        self._TrpcCallee = None
        self._TrpcFunc = None
        self._Quic = None
        self._Domains = None
        self._MultiCertInfo = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def MultiCertInfo(self):
        return self._MultiCertInfo

    @MultiCertInfo.setter
    def MultiCertInfo(self, MultiCertInfo):
        self._MultiCertInfo = MultiCertInfo


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Domain = params.get("Domain")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateInput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._ForwardType = params.get("ForwardType")
        self._DefaultServer = params.get("DefaultServer")
        self._Http2 = params.get("Http2")
        self._TargetType = params.get("TargetType")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        self._Quic = params.get("Quic")
        self._Domains = params.get("Domains")
        if params.get("MultiCertInfo") is not None:
            self._MultiCertInfo = MultiCertInfo()
            self._MultiCertInfo._deserialize(params.get("MultiCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleOutput(AbstractModel):
    """HTTP/HTTPS listener forwarding rule (output)

    """

    def __init__(self):
        r"""
        :param _LocationId: Forwarding rule ID
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: Forwarding rule path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _SessionExpireTime: Session persistence time
        :type SessionExpireTime: int
        :param _HealthCheck: Health check information
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param _Certificate: Certificate information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param _Scheduler: Request forwarding method of the rule
        :type Scheduler: str
        :param _ListenerId: ID of the listener to which the forwarding rule belongs
        :type ListenerId: str
        :param _RewriteTarget: Redirect target information of a forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`
        :param _HttpGzip: Whether to enable gzip
        :type HttpGzip: bool
        :param _BeAutoCreated: Whether the forwarding rule is automatically created
        :type BeAutoCreated: bool
        :param _DefaultServer: Whether to use as the default domain name
        :type DefaultServer: bool
        :param _Http2: Whether to enable Http2
        :type Http2: bool
        :param _ForwardType: Forwarding protocol between CLB and real server
        :type ForwardType: str
        :param _CreateTime: Forwarding rule creation time
        :type CreateTime: str
        :param _TargetType: Real server type
        :type TargetType: str
        :param _TargetGroup: Basic information of a bound target group. This field will be returned if a target group is bound to a rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param _WafDomainId: WAF instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type WafDomainId: str
        :param _TrpcCallee: TRPC callee server route, which is valid when `ForwardType` is `TRPC`. This is now only for internal usage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrpcCallee: str
        :param _TrpcFunc: TRPC calling service API, which is valid when `ForwardType` is `TRPC`. This is now only for internal usage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrpcFunc: str
        :param _QuicStatus: QUIC status
Note: this field may return null, indicating that no valid values can be obtained.
        :type QuicStatus: str
        :param _Domains: List of domain names associated with the forwarding rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Domains: list of str
        :param _TargetGroupList: List of bound target groups
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetGroupList: list of BasicTargetGroupInfo
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Certificate = None
        self._Scheduler = None
        self._ListenerId = None
        self._RewriteTarget = None
        self._HttpGzip = None
        self._BeAutoCreated = None
        self._DefaultServer = None
        self._Http2 = None
        self._ForwardType = None
        self._CreateTime = None
        self._TargetType = None
        self._TargetGroup = None
        self._WafDomainId = None
        self._TrpcCallee = None
        self._TrpcFunc = None
        self._QuicStatus = None
        self._Domains = None
        self._TargetGroupList = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SessionExpireTime(self):
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RewriteTarget(self):
        return self._RewriteTarget

    @RewriteTarget.setter
    def RewriteTarget(self, RewriteTarget):
        self._RewriteTarget = RewriteTarget

    @property
    def HttpGzip(self):
        return self._HttpGzip

    @HttpGzip.setter
    def HttpGzip(self, HttpGzip):
        self._HttpGzip = HttpGzip

    @property
    def BeAutoCreated(self):
        return self._BeAutoCreated

    @BeAutoCreated.setter
    def BeAutoCreated(self, BeAutoCreated):
        self._BeAutoCreated = BeAutoCreated

    @property
    def DefaultServer(self):
        return self._DefaultServer

    @DefaultServer.setter
    def DefaultServer(self, DefaultServer):
        self._DefaultServer = DefaultServer

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def ForwardType(self):
        return self._ForwardType

    @ForwardType.setter
    def ForwardType(self, ForwardType):
        self._ForwardType = ForwardType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetGroup(self):
        return self._TargetGroup

    @TargetGroup.setter
    def TargetGroup(self, TargetGroup):
        self._TargetGroup = TargetGroup

    @property
    def WafDomainId(self):
        return self._WafDomainId

    @WafDomainId.setter
    def WafDomainId(self, WafDomainId):
        self._WafDomainId = WafDomainId

    @property
    def TrpcCallee(self):
        return self._TrpcCallee

    @TrpcCallee.setter
    def TrpcCallee(self, TrpcCallee):
        self._TrpcCallee = TrpcCallee

    @property
    def TrpcFunc(self):
        return self._TrpcFunc

    @TrpcFunc.setter
    def TrpcFunc(self, TrpcFunc):
        self._TrpcFunc = TrpcFunc

    @property
    def QuicStatus(self):
        return self._QuicStatus

    @QuicStatus.setter
    def QuicStatus(self, QuicStatus):
        self._QuicStatus = QuicStatus

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TargetGroupList(self):
        return self._TargetGroupList

    @TargetGroupList.setter
    def TargetGroupList(self, TargetGroupList):
        self._TargetGroupList = TargetGroupList


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self._Certificate = CertificateOutput()
            self._Certificate._deserialize(params.get("Certificate"))
        self._Scheduler = params.get("Scheduler")
        self._ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self._RewriteTarget = RewriteTarget()
            self._RewriteTarget._deserialize(params.get("RewriteTarget"))
        self._HttpGzip = params.get("HttpGzip")
        self._BeAutoCreated = params.get("BeAutoCreated")
        self._DefaultServer = params.get("DefaultServer")
        self._Http2 = params.get("Http2")
        self._ForwardType = params.get("ForwardType")
        self._CreateTime = params.get("CreateTime")
        self._TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self._TargetGroup = BasicTargetGroupInfo()
            self._TargetGroup._deserialize(params.get("TargetGroup"))
        self._WafDomainId = params.get("WafDomainId")
        self._TrpcCallee = params.get("TrpcCallee")
        self._TrpcFunc = params.get("TrpcFunc")
        self._QuicStatus = params.get("QuicStatus")
        self._Domains = params.get("Domains")
        if params.get("TargetGroupList") is not None:
            self._TargetGroupList = []
            for item in params.get("TargetGroupList"):
                obj = BasicTargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTargets(AbstractModel):
    """Information of the real server bound to a forwarding rule under an HTTP/HTTPS listener

    """

    def __init__(self):
        r"""
        :param _LocationId: Forwarding rule ID
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule
        :type Domain: str
        :param _Url: Forwarding rule path.
        :type Url: str
        :param _Targets: Real server information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        :param _FunctionTargets: Information about backend SCF functions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FunctionTargets: list of FunctionTarget
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None
        self._FunctionTargets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def FunctionTargets(self):
        return self._FunctionTargets

    @FunctionTargets.setter
    def FunctionTargets(self, FunctionTargets):
        self._FunctionTargets = FunctionTargets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        if params.get("FunctionTargets") is not None:
            self._FunctionTargets = []
            for item in params.get("FunctionTargets"):
                obj = FunctionTarget()
                obj._deserialize(item)
                self._FunctionTargets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesItems(AbstractModel):
    """Object bound to the layer-7 listener rule

    """

    def __init__(self):
        r"""
        :param _LocationId: Rule ID.
        :type LocationId: str
        :param _Domain: Domain name.
        :type Domain: str
        :param _Url: Uri
        :type Url: str
        :param _Targets: Object bound to the real server.
        :type Targets: list of LbRsTargets
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._Targets = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCustomizedConfigForLoadBalancerRequest(AbstractModel):
    """SetCustomizedConfigForLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _OperationType: Operation type: `ADD`, `DELETE`, `UPDATE`, `BIND`, `UNBIND`
        :type OperationType: str
        :param _UconfigId: This field is required except for creating custom configurations, such as "pz-1234abcd".
        :type UconfigId: str
        :param _ConfigContent: This field is required when creating or modifying custom configurations.
        :type ConfigContent: str
        :param _ConfigName: This field is required when creating or renaming custom configurations.
        :type ConfigName: str
        :param _LoadBalancerIds: This field is required when binding/unbinding resources.
        :type LoadBalancerIds: list of str
        """
        self._OperationType = None
        self._UconfigId = None
        self._ConfigContent = None
        self._ConfigName = None
        self._LoadBalancerIds = None

    @property
    def OperationType(self):
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def UconfigId(self):
        return self._UconfigId

    @UconfigId.setter
    def UconfigId(self, UconfigId):
        self._UconfigId = UconfigId

    @property
    def ConfigContent(self):
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._OperationType = params.get("OperationType")
        self._UconfigId = params.get("UconfigId")
        self._ConfigContent = params.get("ConfigContent")
        self._ConfigName = params.get("ConfigName")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCustomizedConfigForLoadBalancerResponse(AbstractModel):
    """SetCustomizedConfigForLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Configuration ID, such as "pz-1234abcd"
        :type ConfigId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LogSetId: CLS logset ID
<li>Enter the ID of logset you need to add or update. You can acquire the ID by invoking [DescribeLogsets](https://intl.cloud.tencent.com/document/product/614/56454?from_cn_redirect=1).</li>
<li>To delete the log set, set this parameter to `null`.</li>
        :type LogSetId: str
        :param _LogTopicId: CLS log topic ID
<li>Enter the ID of log topic you need to add or update. You can acquire the ID by invoking [DescribeTopics](https://intl.cloud.tencent.com/document/product/614/56454?from_cn_redirect=1).</li>
<li>To delete the log set, set this parameter to `null`.</li>
        :type LogTopicId: str
        :param _LogType: Log type:
<li>`ACCESS`: access logs</li>
<li>`HEALTH`: health check logs</li>
Default: `ACCESS`
        :type LogType: str
        """
        self._LoadBalancerId = None
        self._LogSetId = None
        self._LogTopicId = None
        self._LogType = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog response structure.

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


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _SecurityGroups: Array of security group IDs. One CLB instance can be bound to up to 50 security groups. If you want to unbind all security groups, you do not need to pass in this parameter, or you can pass in an empty array.
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups response structure.

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


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroup: Security group ID, such as sg-12345678
        :type SecurityGroup: str
        :param _OperationType: ADD: bind a security group;
DEL: unbind a security group
        :type OperationType: str
        :param _LoadBalancerIds: Array of CLB instance IDs
        :type LoadBalancerIds: list of str
        """
        self._SecurityGroup = None
        self._OperationType = None
        self._LoadBalancerIds = None

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def OperationType(self):
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._SecurityGroup = params.get("SecurityGroup")
        self._OperationType = params.get("OperationType")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers response structure.

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


class SlaUpdateParam(AbstractModel):
    """Parameters for upgrading to an LCU-supported instance

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: ID of the CLB instance
        :type LoadBalancerId: str
        :param _SlaType: LCU-supported instance specification. Value:
<li>`SLA`: If you have activated Super Large LCU-supported instances, `SLA` indicates Super Large 4.</li>
<li>`clb.c2.medium`: Standard</li>
<li>`clb.c3.small`: Advanced 1</li>
<li>`clb.c3.medium`: Advanced 2</li>
<li>`clb.c4.small`: Super Large 1</li>
<li>`clb.c4.medium`: Super Large 2</li>
<li>`clb.c4.large`: Super Large 3</li>
<li>`clb.c4.xlarge`: Super Large 4</li> For Super Large 2 and above specifications, please [submit a ticket](https://console.cloud.tencent.com/workorder/category). For more specifications, see [Specifications Comparison](https://intl.cloud.tencent.com/document/product/214/84689?from_cn_redirect=1)
        :type SlaType: str
        """
        self._LoadBalancerId = None
        self._SlaType = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SlaType = params.get("SlaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnatIp(AbstractModel):
    """`SnatIp` information structure

    """

    def __init__(self):
        r"""
        :param _SubnetId: Unique VPC subnet ID, such as `subnet-12345678`.
        :type SubnetId: str
        :param _Ip: IP address, such as 192.168.0.1
        :type Ip: str
        """
        self._SubnetId = None
        self._Ip = None

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecAvailability(AbstractModel):
    """Specification availability

    """

    def __init__(self):
        r"""
        :param _SpecType: Specification type
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecType: str
        :param _Availability: Specification availability
Note: This field may return null, indicating that no valid values can be obtained.
        :type Availability: str
        """
        self._SpecType = None
        self._Availability = None

    @property
    def SpecType(self):
        return self._SpecType

    @SpecType.setter
    def SpecType(self, SpecType):
        self._SpecType = SpecType

    @property
    def Availability(self):
        return self._Availability

    @Availability.setter
    def Availability(self, Availability):
        self._Availability = Availability


    def _deserialize(self, params):
        self._SpecType = params.get("SpecType")
        self._Availability = params.get("Availability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """CLB tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class Target(AbstractModel):
    """Redirect target, i.e., the real server bound to a CLB

    """

    def __init__(self):
        r"""
        :param _Port: Listening port of a real server
Note: this parameter is required when binding a CVM or ENI.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param _Type: Real server type. Value range: CVM (Cloud Virtual Machine), ENI (Elastic Network Interface). This parameter does not take effect currently as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _InstanceId: Unique ID of a CVM instance, which is required when binding a CVM instance. It can be obtained from the `InstanceId` field in the response of the `DescribeInstances` API. It indicates binding the primary IP of the primary ENI.
Note: Either `InstanceId` or `EniIp` can be passed in.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Weight: The new forwarding weight of the real server. Value range: [0, 100]. Default: 10. This parameter takes priority over `Weight` in [`RsWeightRule`](https://intl.cloud.tencent.com/document/api/214/30694?from_cn_redirect=1#RsWeightRule). If it’s left empty, the value of `Weight` in `RsWeightRule` will be used.
        :type Weight: int
        :param _EniIp: It is required when binding an IP. ENI IPs and other private IPs are supported. To bind an ENI IP, the ENI should be bound to a CVM instance before being bound to a CLB instance.
Note: Either `InstanceId` or `EniIp` can be passed in. `EniIp` is required in a cross-region binding or when the dual-stack IPV6 CVM is bound.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EniIp: str
        """
        self._Port = None
        self._Type = None
        self._InstanceId = None
        self._Weight = None
        self._EniIp = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EniIp(self):
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupAssociation(AbstractModel):
    """Association between rule and target group

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _LocationId: Forwarding rule ID
        :type LocationId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._TargetGroupId = None
        self._LocationId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._TargetGroupId = params.get("TargetGroupId")
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupBackend(AbstractModel):
    """Real server bound to a target group

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _Type: Real server type. Valid values: CVM, ENI (coming soon)
        :type Type: str
        :param _InstanceId: Unique real server ID
        :type InstanceId: str
        :param _Port: Listening port of real server
        :type Port: int
        :param _Weight: Forwarding weight of real server. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        :param _PublicIpAddresses: Public IP of real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: Private IP of real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param _InstanceName: Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _RegisteredTime: Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param _EniId: Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        :param _ZoneId: AZ ID of the real server
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ZoneId: int
        """
        self._TargetGroupId = None
        self._Type = None
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RegisteredTime = None
        self._EniId = None
        self._ZoneId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegisteredTime(self):
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInfo(AbstractModel):
    """Target group information

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID
        :type TargetGroupId: str
        :param _VpcId: `vpcid` of target group
        :type VpcId: str
        :param _TargetGroupName: Target group name
        :type TargetGroupName: str
        :param _Port: Default port of target group
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _CreatedTime: Target group creation time
        :type CreatedTime: str
        :param _UpdatedTime: Target group modification time
        :type UpdatedTime: str
        :param _AssociatedRule: Array of associated rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedRule: list of AssociationItem
        """
        self._TargetGroupId = None
        self._VpcId = None
        self._TargetGroupName = None
        self._Port = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._AssociatedRule = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def AssociatedRule(self):
        return self._AssociatedRule

    @AssociatedRule.setter
    def AssociatedRule(self, AssociatedRule):
        self._AssociatedRule = AssociatedRule


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._VpcId = params.get("VpcId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._Port = params.get("Port")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self._AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self._AssociatedRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInstance(AbstractModel):
    """Target group instance

    """

    def __init__(self):
        r"""
        :param _BindIP: Private IP of target group instance
        :type BindIP: str
        :param _Port: Port of target group instance
        :type Port: int
        :param _Weight: Weight of target group instance
        :type Weight: int
        :param _NewPort: New port of target group instance
        :type NewPort: int
        """
        self._BindIP = None
        self._Port = None
        self._Weight = None
        self._NewPort = None

    @property
    def BindIP(self):
        return self._BindIP

    @BindIP.setter
    def BindIP(self, BindIP):
        self._BindIP = BindIP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def NewPort(self):
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort


    def _deserialize(self, params):
        self._BindIP = params.get("BindIP")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """Describes the health information of a target

    """

    def __init__(self):
        r"""
        :param _IP: Private IP of the target
        :type IP: str
        :param _Port: Port bound to the target
        :type Port: int
        :param _HealthStatus: Current health status. true: healthy; false: unhealthy.
        :type HealthStatus: bool
        :param _TargetId: Instance ID of the target, such as ins-12345678
        :type TargetId: str
        :param _HealthStatusDetail: Detailed information about the current health status. Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status.
        :type HealthStatusDetail: str
        :param _HealthStatusDetial: (**This parameter will be disused soon. Please use `HealthStatusDetail` instead.**) Details of the current health status. Values: `Alive` (healthy), `Dead` (abnormal), `Unknown` (Health check not started/checking/unknown status)
        :type HealthStatusDetial: str
        """
        self._IP = None
        self._Port = None
        self._HealthStatus = None
        self._TargetId = None
        self._HealthStatusDetail = None
        self._HealthStatusDetial = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def HealthStatusDetail(self):
        return self._HealthStatusDetail

    @HealthStatusDetail.setter
    def HealthStatusDetail(self, HealthStatusDetail):
        self._HealthStatusDetail = HealthStatusDetail

    @property
    def HealthStatusDetial(self):
        warnings.warn("parameter `HealthStatusDetial` is deprecated", DeprecationWarning) 

        return self._HealthStatusDetial

    @HealthStatusDetial.setter
    def HealthStatusDetial(self, HealthStatusDetial):
        warnings.warn("parameter `HealthStatusDetial` is deprecated", DeprecationWarning) 

        self._HealthStatusDetial = HealthStatusDetial


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._HealthStatus = params.get("HealthStatus")
        self._TargetId = params.get("TargetId")
        self._HealthStatusDetail = params.get("HealthStatusDetail")
        self._HealthStatusDetial = params.get("HealthStatusDetial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetRegionInfo(AbstractModel):
    """Information of the real server bound to a CLB instance, including region and network to which it belongs.

    """

    def __init__(self):
        r"""
        :param _Region: Region of the target, such as ap-guangzhou
        :type Region: str
        :param _VpcId: Network of the target, which is in the format of vpc-abcd1234 for VPC or 0 for basic network
        :type VpcId: str
        """
        self._Region = None
        self._VpcId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TypeInfo(AbstractModel):
    """ISP Type

    """

    def __init__(self):
        r"""
        :param _Type: ISP Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _SpecAvailabilitySet: Specification availability
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecAvailabilitySet: list of SpecAvailability
        """
        self._Type = None
        self._SpecAvailabilitySet = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpecAvailabilitySet(self):
        return self._SpecAvailabilitySet

    @SpecAvailabilitySet.setter
    def SpecAvailabilitySet(self, SpecAvailabilitySet):
        self._SpecAvailabilitySet = SpecAvailabilitySet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("SpecAvailabilitySet") is not None:
            self._SpecAvailabilitySet = []
            for item in params.get("SpecAvailabilitySet"):
                obj = SpecAvailability()
                obj._deserialize(item)
                self._SpecAvailabilitySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """AZ information

    """

    def __init__(self):
        r"""
        :param _ZoneId: Unique AZ ID in a numeric form, such as 100001
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _Zone: Unique AZ ID in a string form, such as ap-guangzhou-1
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _ZoneName: AZ name, such as Guangzhou Zone 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param _ZoneRegion: AZ region, e.g., ap-guangzhou.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ZoneRegion: str
        :param _LocalZone: Whether the AZ is the `LocalZone`, e.g., false.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LocalZone: bool
        :param _EdgeZone: Whether the AZ is an edge zone. Values: `true`, `false`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EdgeZone: bool
        """
        self._ZoneId = None
        self._Zone = None
        self._ZoneName = None
        self._ZoneRegion = None
        self._LocalZone = None
        self._EdgeZone = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneRegion(self):
        return self._ZoneRegion

    @ZoneRegion.setter
    def ZoneRegion(self, ZoneRegion):
        self._ZoneRegion = ZoneRegion

    @property
    def LocalZone(self):
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def EdgeZone(self):
        return self._EdgeZone

    @EdgeZone.setter
    def EdgeZone(self, EdgeZone):
        self._EdgeZone = EdgeZone


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneRegion = params.get("ZoneRegion")
        self._LocalZone = params.get("LocalZone")
        self._EdgeZone = params.get("EdgeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResource(AbstractModel):
    """List of AZs

    """

    def __init__(self):
        r"""
        :param _MasterZone: Primary AZ, such as "ap-guangzhou-1".
        :type MasterZone: str
        :param _ResourceSet: List of resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceSet: list of Resource
        :param _SlaveZone: Secondary AZ, such as "ap-guangzhou-2". 
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveZone: str
        :param _IPVersion: IP version. Values: `IPv4`, `IPv6`, and `IPv6_Nat`.
        :type IPVersion: str
        :param _ZoneRegion: Region of the AZ, such as `ap-guangzhou`.
        :type ZoneRegion: str
        :param _LocalZone: Whether the AZ is a `LocalZone`. Values: `true`, `false`.
        :type LocalZone: bool
        :param _ZoneResourceType: Type of resources in the zone. Values: `SHARED`, `EXCLUSIVE`
        :type ZoneResourceType: str
        :param _EdgeZone: Whether the AZ is an edge zone. Values: `true`, `false`.
        :type EdgeZone: bool
        :param _Egress: Network egress
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Egress: str
        """
        self._MasterZone = None
        self._ResourceSet = None
        self._SlaveZone = None
        self._IPVersion = None
        self._ZoneRegion = None
        self._LocalZone = None
        self._ZoneResourceType = None
        self._EdgeZone = None
        self._Egress = None

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def ResourceSet(self):
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def IPVersion(self):
        return self._IPVersion

    @IPVersion.setter
    def IPVersion(self, IPVersion):
        self._IPVersion = IPVersion

    @property
    def ZoneRegion(self):
        return self._ZoneRegion

    @ZoneRegion.setter
    def ZoneRegion(self, ZoneRegion):
        self._ZoneRegion = ZoneRegion

    @property
    def LocalZone(self):
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def ZoneResourceType(self):
        return self._ZoneResourceType

    @ZoneResourceType.setter
    def ZoneResourceType(self, ZoneResourceType):
        self._ZoneResourceType = ZoneResourceType

    @property
    def EdgeZone(self):
        return self._EdgeZone

    @EdgeZone.setter
    def EdgeZone(self, EdgeZone):
        self._EdgeZone = EdgeZone

    @property
    def Egress(self):
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress


    def _deserialize(self, params):
        self._MasterZone = params.get("MasterZone")
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._SlaveZone = params.get("SlaveZone")
        self._IPVersion = params.get("IPVersion")
        self._ZoneRegion = params.get("ZoneRegion")
        self._LocalZone = params.get("LocalZone")
        self._ZoneResourceType = params.get("ZoneResourceType")
        self._EdgeZone = params.get("EdgeZone")
        self._Egress = params.get("Egress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        