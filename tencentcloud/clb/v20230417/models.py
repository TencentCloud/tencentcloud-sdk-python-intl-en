# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AvailableZoneAffinityInfo(AbstractModel):
    r"""Forward affinity info in availability zone

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable availability zone forwarding affinity. true: enable availability zone forwarding affinity; false: enable availability zone forwarding affinity.
        :type Enable: bool
        :param _ExitRatio: The availability zone forwarding affinity failure threshold. When the healthy ratio of backend services in an availability zone is less than this threshold, the Cloud Load Balancer will exit availability zone forwarding affinity and convert to forwarding across all availability zones.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExitRatio: int
        :param _ReentryRatio: The threshold for re-enabling availability zone forwarding affinity. When forwarding is in all availability zones and the proportion of healthy backend services in the Cloud Load Balancer availability zone is greater than or equal to this threshold, the CLB will enter availability zone forwarding affinity again.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReentryRatio: int
        """
        self._Enable = None
        self._ExitRatio = None
        self._ReentryRatio = None

    @property
    def Enable(self):
        r"""Whether to enable availability zone forwarding affinity. true: enable availability zone forwarding affinity; false: enable availability zone forwarding affinity.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ExitRatio(self):
        r"""The availability zone forwarding affinity failure threshold. When the healthy ratio of backend services in an availability zone is less than this threshold, the Cloud Load Balancer will exit availability zone forwarding affinity and convert to forwarding across all availability zones.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExitRatio

    @ExitRatio.setter
    def ExitRatio(self, ExitRatio):
        self._ExitRatio = ExitRatio

    @property
    def ReentryRatio(self):
        r"""The threshold for re-enabling availability zone forwarding affinity. When forwarding is in all availability zones and the proportion of healthy backend services in the Cloud Load Balancer availability zone is greater than or equal to this threshold, the CLB will enter availability zone forwarding affinity again.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReentryRatio

    @ReentryRatio.setter
    def ReentryRatio(self, ReentryRatio):
        self._ReentryRatio = ReentryRatio


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._ExitRatio = params.get("ExitRatio")
        self._ReentryRatio = params.get("ReentryRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightRequest(AbstractModel):
    r"""BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ModifyList: List of weights to be modified in batches.
        :type ModifyList: list of RsWeightRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        r"""List of weights to be modified in batches.
        :rtype: list of RsWeightRule
        """
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
    r"""BatchModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BindDetailItem(AbstractModel):
    r"""Binding relationship, including listener name, protocol, URL, and vport.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: ID of the CLB instance bound to the configuration
        :type LoadBalancerId: str
        :param _ListenerId: ID of the listener bound to the configuration
        :type ListenerId: str
        :param _Domain: Domain name bound to the configuration
        :type Domain: str
        :param _LocationId: Rule bound to the configuration
        :type LocationId: str
        :param _ListenerName: Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _Protocol: Listener protocol
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Vport: Listener port
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vport: int
        :param _Url: Location URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _ConfigId: Configuration ID
        :type ConfigId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Domain = None
        self._LocationId = None
        self._ListenerName = None
        self._Protocol = None
        self._Vport = None
        self._Url = None
        self._ConfigId = None

    @property
    def LoadBalancerId(self):
        r"""ID of the CLB instance bound to the configuration
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        r"""ID of the listener bound to the configuration
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        r"""Domain name bound to the configuration
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LocationId(self):
        r"""Rule bound to the configuration
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def ListenerName(self):
        r"""Listener name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""Listener protocol
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Vport(self):
        r"""Listener port
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Url(self):
        r"""Location URL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ConfigId(self):
        r"""Configuration ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._LocationId = params.get("LocationId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Vport = params.get("Vport")
        self._Url = params.get("Url")
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdRelatedWithLoadBalancers(AbstractModel):
    r"""Certificate ID and the list of CLB instances associated with the certificate ID

    """

    def __init__(self):
        r"""
        :param _CertId: Certificate ID
        :type CertId: str
        :param _LoadBalancers: List of CLB instances associated with the certificate
        :type LoadBalancers: list of LoadBalancer
        """
        self._CertId = None
        self._LoadBalancers = None

    @property
    def CertId(self):
        r"""Certificate ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def LoadBalancers(self):
        r"""List of CLB instances associated with the certificate
        :rtype: list of LoadBalancer
        """
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
        


class ClassicalListener(AbstractModel):
    r"""Classic CLB listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _ListenerPort: CLB listener port
        :type ListenerPort: int
        :param _InstancePort: Listener backend forwarding port
        :type InstancePort: int
        :param _ListenerName: listener name
        :type ListenerName: str
        :param _Protocol: Listener protocol type
        :type Protocol: str
        :param _SessionExpire: Session hold time
        :type SessionExpire: int
        :param _HealthSwitch: Whether health check is enabled. 1: Enabled; 0: Disabled
        :type HealthSwitch: int
        :param _TimeOut: Response timeout duration
        :type TimeOut: int
        :param _IntervalTime: check interval
        :type IntervalTime: int
        :param _HealthNum: health threshold
        :type HealthNum: int
        :param _AbnormalNum: unhealthy threshold
        :type AbnormalNum: int
        :param _HttpHash: Request balancing method for listeners of the classic public network CLB. An empty string or wrr indicates weighted round robin. ip_hash indicates consistent hashing based on the accessed source IP address. least_conn indicates least connections.
        :type HttpHash: str
        :param _HttpCode: Health check return code for HTTP and HTTPS listeners of a public network Classic CLB instance. For more information, refer to the explanation of this field in the listener creation API.
        :type HttpCode: int
        :param _HttpCheckPath: Health check path for HTTP and HTTPS listeners of a public network Classic CLB instance
        :type HttpCheckPath: str
        :param _SSLMode: Authentication method for an HTTPS listener of a public network Classic CLB instance
        :type SSLMode: str
        :param _CertId: Server certificate ID for an HTTPS listener of a public network Classic CLB instance
        :type CertId: str
        :param _CertCaId: Client certificate ID for an HTTPS listener of a public network Classic CLB instance
        :type CertCaId: str
        :param _Status: Listener status. 0: Creating; 1: Running
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
        self._AbnormalNum = None
        self._HttpHash = None
        self._HttpCode = None
        self._HttpCheckPath = None
        self._SSLMode = None
        self._CertId = None
        self._CertCaId = None
        self._Status = None

    @property
    def ListenerId(self):
        r"""CLB listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        r"""CLB listener port
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def InstancePort(self):
        r"""Listener backend forwarding port
        :rtype: int
        """
        return self._InstancePort

    @InstancePort.setter
    def InstancePort(self, InstancePort):
        self._InstancePort = InstancePort

    @property
    def ListenerName(self):
        r"""listener name
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""Listener protocol type
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SessionExpire(self):
        r"""Session hold time
        :rtype: int
        """
        return self._SessionExpire

    @SessionExpire.setter
    def SessionExpire(self, SessionExpire):
        self._SessionExpire = SessionExpire

    @property
    def HealthSwitch(self):
        r"""Whether health check is enabled. 1: Enabled; 0: Disabled
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        r"""Response timeout duration
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        r"""check interval
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        r"""health threshold
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def AbnormalNum(self):
        r"""unhealthy threshold
        :rtype: int
        """
        return self._AbnormalNum

    @AbnormalNum.setter
    def AbnormalNum(self, AbnormalNum):
        self._AbnormalNum = AbnormalNum

    @property
    def HttpHash(self):
        r"""Request balancing method for listeners of the classic public network CLB. An empty string or wrr indicates weighted round robin. ip_hash indicates consistent hashing based on the accessed source IP address. least_conn indicates least connections.
        :rtype: str
        """
        return self._HttpHash

    @HttpHash.setter
    def HttpHash(self, HttpHash):
        self._HttpHash = HttpHash

    @property
    def HttpCode(self):
        r"""Health check return code for HTTP and HTTPS listeners of a public network Classic CLB instance. For more information, refer to the explanation of this field in the listener creation API.
        :rtype: int
        """
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def HttpCheckPath(self):
        r"""Health check path for HTTP and HTTPS listeners of a public network Classic CLB instance
        :rtype: str
        """
        return self._HttpCheckPath

    @HttpCheckPath.setter
    def HttpCheckPath(self, HttpCheckPath):
        self._HttpCheckPath = HttpCheckPath

    @property
    def SSLMode(self):
        r"""Authentication method for an HTTPS listener of a public network Classic CLB instance
        :rtype: str
        """
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode

    @property
    def CertId(self):
        r"""Server certificate ID for an HTTPS listener of a public network Classic CLB instance
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertCaId(self):
        r"""Client certificate ID for an HTTPS listener of a public network Classic CLB instance
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def Status(self):
        r"""Listener status. 0: Creating; 1: Running
        :rtype: int
        """
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
        self._AbnormalNum = params.get("AbnormalNum")
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
        


class CloneLoadBalancerRequest(AbstractModel):
    r"""CloneLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: The name of the cloned CLB instance. Rule: 1-60 English letters, Chinese characters, digits, hyphens "-", or underscores "_".
Note: If the name is the same as an existing Cloud Load Balancer instance in the system, the system will automatically generate the name of the created CLB instance.
        :type LoadBalancerName: str
        :param _ProjectId: The project ID associated with the Cloud Load Balancer instance can be obtained through the [DescribeLoadBalancers](https://www.tencentcloud.com/document/product/214/30685?from_cn_redirect=1) API. If this parameter is not specified, it will be used as the default project.
        :type ProjectId: int
        :param _MasterZoneId: Applicable only to public network CLB. Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.
Note: The primary AZ loads traffic, while the secondary AZ does not load traffic by default and is used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. You can call the [DescribeResources](https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1) API to query the primary AZ list of a region.
        :type MasterZoneId: str
        :param _SlaveZoneId: Applicable only to public network CLB. Sets the secondary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.
Note: The secondary AZ sustains traffic when the primary AZ encounters faults. You can call the [DescribeResources](https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1) API to query the list of primary/secondary AZs in a region.
        :type SlaveZoneId: str
        :param _ZoneId: Applicable only to public network CLB. Availability zone ID. Specify an availability zone to create a Cloud Load Balancer instance, for example, ap-guangzhou-1. If not specified, queries CVM instances in all AZs. If needed, call the DescribeZones API (https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1) to query the availability zone list.
        :type ZoneId: str
        :param _InternetAccessible: CLB network billing mode, applicable only to public network CLB instances.
        :type InternetAccessible: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        :param _VipIsp: It only applies to public CLB. Currently, the static single-line IP type is supported only for the regions of Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu, and Chongqing. If you need to experience it, contact your business manager. After approval, you can select the ISP type as China Mobile (CMCC), China Unicom (CUCC), or China Telecom (CTCC). The network billing mode should be selected as billing by bandwidth package (BANDWIDTH_PACKAGE). If this parameter is not specified, BGP is used by default. You can use the DescribeResources API to query ISPs supported for a region.
        :type VipIsp: str
        :param _Vip: Designate a Vip to apply for Cloud Load Balancer.
        :type Vip: str
        :param _Tags: When you purchase Cloud Load Balancer (CLB), you can tag it.
        :type Tags: list of TagInfo
        :param _ExclusiveCluster: Exclusive cluster information.
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        :param _BandwidthPackageId: Bandwidth package ID. If this parameter is specified, the network billing mode (InternetAccessible.InternetChargeType) supports only billing by bandwidth package (BANDWIDTH_PACKAGE).
        :type BandwidthPackageId: str
        :param _SnatPro: Whether to support the feature of binding IP addresses across regions/VPCs.
        :type SnatPro: bool
        :param _SnatIps: SNAT IP addresses to be created when the feature of cross-region/cross-VPC IP address binding is enabled.
        :type SnatIps: list of SnatIp
        :param _ClusterIds: Public network exclusive cluster ID or CDCId.
        :type ClusterIds: list of str
        :param _SlaType: Performance capacity specification.<li>clb.c2.medium (standard type)</li><li>clb.c3.small (advanced type 1)</li><li>clb.c3.medium (advanced type 2)</li><li>clb.c4.small (high-strength type 1)</li><li>clb.c4.medium (high-strength type 2)</li><li>clb.c4.large (high-strength type 3)</li><li>clb.c4.xlarge (high-strength type 4)</li>
        :type SlaType: str
        :param _ClusterTag: Exclusive STGW cluster tag.
        :type ClusterTag: str
        :param _Zones: Applicable only to private network CLB. When connected to nearby via private network, select availability zone for deployment. You can call the [DescribeZones](https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1) API to query the availability zone list.
        :type Zones: list of str
        :param _EipAddressId: Unique ID of an EIP, in the format of eip-11112222, which is applicable only for binding EIP to private network CLB.
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
        r"""CLB ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""The name of the cloned CLB instance. Rule: 1-60 English letters, Chinese characters, digits, hyphens "-", or underscores "_".
Note: If the name is the same as an existing Cloud Load Balancer instance in the system, the system will automatically generate the name of the created CLB instance.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ProjectId(self):
        r"""The project ID associated with the Cloud Load Balancer instance can be obtained through the [DescribeLoadBalancers](https://www.tencentcloud.com/document/product/214/30685?from_cn_redirect=1) API. If this parameter is not specified, it will be used as the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def MasterZoneId(self):
        r"""Applicable only to public network CLB. Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.
Note: The primary AZ loads traffic, while the secondary AZ does not load traffic by default and is used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. You can call the [DescribeResources](https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1) API to query the primary AZ list of a region.
        :rtype: str
        """
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        r"""Applicable only to public network CLB. Sets the secondary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.
Note: The secondary AZ sustains traffic when the primary AZ encounters faults. You can call the [DescribeResources](https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1) API to query the list of primary/secondary AZs in a region.
        :rtype: str
        """
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def ZoneId(self):
        r"""Applicable only to public network CLB. Availability zone ID. Specify an availability zone to create a Cloud Load Balancer instance, for example, ap-guangzhou-1. If not specified, queries CVM instances in all AZs. If needed, call the DescribeZones API (https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1) to query the availability zone list.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        r"""CLB network billing mode, applicable only to public network CLB instances.
        :rtype: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        r"""It only applies to public CLB. Currently, the static single-line IP type is supported only for the regions of Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu, and Chongqing. If you need to experience it, contact your business manager. After approval, you can select the ISP type as China Mobile (CMCC), China Unicom (CUCC), or China Telecom (CTCC). The network billing mode should be selected as billing by bandwidth package (BANDWIDTH_PACKAGE). If this parameter is not specified, BGP is used by default. You can use the DescribeResources API to query ISPs supported for a region.
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Vip(self):
        r"""Designate a Vip to apply for Cloud Load Balancer.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Tags(self):
        r"""When you purchase Cloud Load Balancer (CLB), you can tag it.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExclusiveCluster(self):
        r"""Exclusive cluster information.
        :rtype: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        """
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def BandwidthPackageId(self):
        r"""Bandwidth package ID. If this parameter is specified, the network billing mode (InternetAccessible.InternetChargeType) supports only billing by bandwidth package (BANDWIDTH_PACKAGE).
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def SnatPro(self):
        r"""Whether to support the feature of binding IP addresses across regions/VPCs.
        :rtype: bool
        """
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        r"""SNAT IP addresses to be created when the feature of cross-region/cross-VPC IP address binding is enabled.
        :rtype: list of SnatIp
        """
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterIds(self):
        r"""Public network exclusive cluster ID or CDCId.
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SlaType(self):
        r"""Performance capacity specification.<li>clb.c2.medium (standard type)</li><li>clb.c3.small (advanced type 1)</li><li>clb.c3.medium (advanced type 2)</li><li>clb.c4.small (high-strength type 1)</li><li>clb.c4.medium (high-strength type 2)</li><li>clb.c4.large (high-strength type 3)</li><li>clb.c4.xlarge (high-strength type 4)</li>
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClusterTag(self):
        r"""Exclusive STGW cluster tag.
        :rtype: str
        """
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def Zones(self):
        r"""Applicable only to private network CLB. When connected to nearby via private network, select availability zone for deployment. You can call the [DescribeZones](https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1) API to query the availability zone list.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def EipAddressId(self):
        r"""Unique ID of an EIP, in the format of eip-11112222, which is applicable only for binding EIP to private network CLB.
        :rtype: str
        """
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
    r"""CloneLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ClusterItem(AbstractModel):
    r"""Exclusive cluster information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster unique ID.
        :type ClusterId: str
        :param _ClusterName: Cluster name.
        :type ClusterName: str
        :param _Zone: AZ of the cluster, such as ap-guangzhou-1
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Zone = None

    @property
    def ClusterId(self):
        r"""Cluster unique ID.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Cluster name.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Zone(self):
        r"""AZ of the cluster, such as ap-guangzhou-1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
    r"""configuration content

    """

    def __init__(self):
        r"""
        :param _ConfigId: Configuration ID
        :type ConfigId: str
        :param _ConfigType: Configuration type
        :type ConfigType: str
        :param _ConfigName: Configuration name
        :type ConfigName: str
        :param _ConfigContent: Configuration content
        :type ConfigContent: str
        :param _CreateTimestamp: Configuration creation time
        :type CreateTimestamp: str
        :param _UpdateTimestamp: Configuration modification time
        :type UpdateTimestamp: str
        :param _Tag: Tag.
        :type Tag: list of TagInfo
        """
        self._ConfigId = None
        self._ConfigType = None
        self._ConfigName = None
        self._ConfigContent = None
        self._CreateTimestamp = None
        self._UpdateTimestamp = None
        self._Tag = None

    @property
    def ConfigId(self):
        r"""Configuration ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def ConfigType(self):
        r"""Configuration type
        :rtype: str
        """
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def ConfigName(self):
        r"""Configuration name
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ConfigContent(self):
        r"""Configuration content
        :rtype: str
        """
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def CreateTimestamp(self):
        r"""Configuration creation time
        :rtype: str
        """
        return self._CreateTimestamp

    @CreateTimestamp.setter
    def CreateTimestamp(self, CreateTimestamp):
        self._CreateTimestamp = CreateTimestamp

    @property
    def UpdateTimestamp(self):
        r"""Configuration modification time
        :rtype: str
        """
        return self._UpdateTimestamp

    @UpdateTimestamp.setter
    def UpdateTimestamp(self, UpdateTimestamp):
        self._UpdateTimestamp = UpdateTimestamp

    @property
    def Tag(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._ConfigType = params.get("ConfigType")
        self._ConfigName = params.get("ConfigName")
        self._ConfigContent = params.get("ConfigContent")
        self._CreateTimestamp = params.get("CreateTimestamp")
        self._UpdateTimestamp = params.get("UpdateTimestamp")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerRequest(AbstractModel):
    r"""CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: <p>Network type of the Cloud Load Balancer instance:<br>OPEN: public network attribute, INTERNAL: private network attribute.</p>
        :type LoadBalancerType: str
        :param _Forward: <p>Type of the Cloud Load Balancer instance. 1: Common Cloud Load Balancer instance. Currently only support input 1.</p>
        :type Forward: int
        :param _LoadBalancerName: <p>The name of a Cloud Load Balancer instance takes effect only when creating an instance. Rule: 1-80 characters in internationally compatible languages, including English letters, Chinese characters, digits, hyphens "-", underscores "_", and other common characters (Unicode supplementary characters such as emojis and rare Chinese characters are forbidden). Note: If the name is identical to that of an existing Cloud Load Balancer instance in the system, the system will automatically generate a name for the newly created CLB instance.</p>
        :type LoadBalancerName: str
        :param _VpcId: <p>The network ID of the backend target device belonging to the Cloud Load Balancer, such as vpc-12345678, can be obtained through the <a href="https://www.tencentcloud.com/document/product/215/15778?from_cn_redirect=1">DescribeVpcs</a> API. It defaults to DefaultVPC if this parameter is not specified. This parameter is required when creating a private network CLB instance.</p>
        :type VpcId: str
        :param _SubnetId: <p>A subnet ID must be specified when you purchase a private network CLB instance under a VPC. The VIP of the private network CLB instance is generated in this subnet. This parameter is required when you create a private network CLB instance but not supported when you create a public network IPv4 CLB instance.</p>
        :type SubnetId: str
        :param _ProjectId: <p>The project ID associated with the Cloud Load Balancer instance can be obtained through the <a href="https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1">DescribeProject</a> API. If this parameter is left blank, it will be used as the default project.</p>
        :type ProjectId: int
        :param _AddressIPVersion: <p>Applicable only to public network CLB. IP version, valid values: IPV4, IPV6, IPv6FullChain, case-insensitive, default value IPV4. Description: A value of IPV6 means IPV6 NAT64 version; a value of IPv6FullChain means IPv6 version.</p>
        :type AddressIPVersion: str
        :param _Number: <p>Count of Cloud Load Balancers to create. Default value: 1.</p>
        :type Number: int
        :param _MasterZoneId: <p>Applicable only to public network IPv4 Cloud Load Balancer. Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.<br>Note: The primary AZ loads traffic. The secondary AZ does not load traffic by default and is used only if the primary AZ becomes unavailable. Currently, primary and secondary AZs are supported only for IPv4 CLB instances in Guangzhou, Shanghai, Nanjing, Beijing, Chengdu, Shenzhen Finance, Hong Kong (China), Seoul, Frankfurt, and Singapore regions. You can call the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> API to query the primary AZ list of a region. [If you need to experience this feature, submit a ticket](https://console.cloud.tencent.com/workorder/category).</p>
        :type MasterZoneId: str
        :param _ZoneId: <p>Applicable only to public network load balancing with IPv4 version. Availability zone ID. Designated availability zone to create a CLB instance, for example: ap-guangzhou-1.</p>
        :type ZoneId: str
        :param _InternetAccessible: <p>Maximum outbound bandwidth under the network billing mode. It applies only to LCU-supported instances of the private network type and all instances of the public network type.</p>
        :type InternetAccessible: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        :param _VipIsp: <p>Applicable only to public network CLB. Currently, static single-line IP type is supported in Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu, and Chongqing regions. If you need to experience it, contact business manager to submit a request. After approval, just select CMCC, CUCC, or CTCC as the operator type. Only can be used BANDWIDTH_PACKAGE for network billing mode. If this parameter is not specified, use BGP by default. You can check ISPs supported in a region via the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> api query.</p>
        :type VipIsp: str
        :param _Tags: <p>When you purchase Cloud Load Balancer (CLB), you can tag it with up to 20 tag key-value pairs.</p>
        :type Tags: list of TagInfo
        :param _Vip: <p>Apply for a Cloud Load Balancer with a designated VIP. This parameter is optional. If this parameter is not specified, the VIP is assigned by system. This parameter is supported for IPv4 and IPv6 types but unsupported for IPv6 NAT64 type.<br>Note: When specifying a VIP to create a private network instance or a public IPv6 BGP instance, creation fails if the VIP is not within the specified VPC subnet or if the VIP is already occupied.</p>
        :type Vip: str
        :param _BandwidthPackageId: <p>Bandwidth package ID. If this parameter is specified, the network billing mode (InternetAccessible.InternetChargeType) will only support billing by bandwidth package (BANDWIDTH_PACKAGE). The attributes of the bandwidth package determine the settlement method. For IPv6 CLB instances purchased by non-promoted users, if the ISP type is not BGP, the bandwidth package ID cannot be specified.</p>
        :type BandwidthPackageId: str
        :param _ExclusiveCluster: <p>Dedicated instance info. This parameter is required when creating a private network CLB instance of exclusive type.</p>
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        :param _SlaType: <p>Performance capacity specification.</p><ul><li>If you need to create an LCU-supported instance, this parameter is required. Valid values:<ul><li> clb.c2.medium: Standard </li><li> clb.c3.small: Advanced 1 </li><li> clb.c3.medium: Advanced 2 </li><li> clb.c4.small: Super Large 1 </li><li> clb.c4.medium: Super Large 2 </li><li> clb.c4.large: Super Large 3 </li><li> clb.c4.xlarge: Super Large 4 </li></ul></li><li>For domestic site users, this parameter is not required when creating a shared instance. For international site users, the default purchased instance is standard if this parameter is not passed.</li></ul> For specification details, see [Instance Specifications Comparison](https://www.tencentcloud.com/document/product/214/84689?from_cn_redirect=1).
        :type SlaType: str
        :param _ClientToken: <p>A string used to ensure request idempotency. This string is generated by the customer and must be unique among different requests, with a maximum value of no more than 64 ASCII characters. If not specified, request idempotency cannot be guaranteed.</p>
        :type ClientToken: str
        :param _SnatPro: <p>Whether the cross-regional or cross-Vpc IP binding feature is supported.</p>
        :type SnatPro: bool
        :param _SnatIps: <p>After enabling the cross-regional/cross-Vpc IP binding feature, create a SnatIp.</p>
        :type SnatIps: list of SnatIp
        :param _ClusterTag: <p>Tag of the Stgw exclusive cluster.</p>
        :type ClusterTag: str
        :param _SlaveZoneId: <p>Applicable only to public network load balancing with IPv4 version. Sets the secondary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.<br>Note: The secondary AZ is the availability zone that needs to carry traffic after primary availability zone failure. You can query a region's list of primary/secondary AZs via the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> API. [If you need to trial the feature, submit a <a href="https://console.cloud.tencent.com/workorder/category">ticket application</a>]</p>
        :type SlaveZoneId: str
        :param _EipAddressId: <p>Unique ID of EIP, such as eip-11112222, applicable only to private network CLB to bind EIP.</p>
        :type EipAddressId: str
        :param _LoadBalancerPassToTarget: <p>Allow CLB traffic to the Target. Enable (true): verify security groups on CLB; deny CLB traffic to the Target (false): verify security groups on both CLB and backend instances.</p>
        :type LoadBalancerPassToTarget: bool
        :param _Egress: <p>Network outbound</p>
        :type Egress: str
        :param _LBChargePrepaid: <p>Prepaid billing attributes of the Cloud Load Balancer instance</p>
        :type LBChargePrepaid: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        :param _LBChargeType: <p>Billing type of the CLB instance. Valid values: POSTPAID_BY_HOUR and PREPAID. Default value: POSTPAID_BY_HOUR.</p>
        :type LBChargeType: str
        :param _AccessLogTopicId: <p>L7 access log topic ID</p>
        :type AccessLogTopicId: str
        :param _AdvancedRoute: <p>Whether layer-7 advanced routing is enabled</p>
        :type AdvancedRoute: bool
        :param _AvailableZoneAffinityInfo: <p>Availability zone affinity info</p>
        :type AvailableZoneAffinityInfo: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
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
        self._Egress = None
        self._LBChargePrepaid = None
        self._LBChargeType = None
        self._AccessLogTopicId = None
        self._AdvancedRoute = None
        self._AvailableZoneAffinityInfo = None

    @property
    def LoadBalancerType(self):
        r"""<p>Network type of the Cloud Load Balancer instance:<br>OPEN: public network attribute, INTERNAL: private network attribute.</p>
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        r"""<p>Type of the Cloud Load Balancer instance. 1: Common Cloud Load Balancer instance. Currently only support input 1.</p>
        :rtype: int
        """
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        r"""<p>The name of a Cloud Load Balancer instance takes effect only when creating an instance. Rule: 1-80 characters in internationally compatible languages, including English letters, Chinese characters, digits, hyphens "-", underscores "_", and other common characters (Unicode supplementary characters such as emojis and rare Chinese characters are forbidden). Note: If the name is identical to that of an existing Cloud Load Balancer instance in the system, the system will automatically generate a name for the newly created CLB instance.</p>
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        r"""<p>The network ID of the backend target device belonging to the Cloud Load Balancer, such as vpc-12345678, can be obtained through the <a href="https://www.tencentcloud.com/document/product/215/15778?from_cn_redirect=1">DescribeVpcs</a> API. It defaults to DefaultVPC if this parameter is not specified. This parameter is required when creating a private network CLB instance.</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>A subnet ID must be specified when you purchase a private network CLB instance under a VPC. The VIP of the private network CLB instance is generated in this subnet. This parameter is required when you create a private network CLB instance but not supported when you create a public network IPv4 CLB instance.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        r"""<p>The project ID associated with the Cloud Load Balancer instance can be obtained through the <a href="https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1">DescribeProject</a> API. If this parameter is left blank, it will be used as the default project.</p>
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AddressIPVersion(self):
        r"""<p>Applicable only to public network CLB. IP version, valid values: IPV4, IPV6, IPv6FullChain, case-insensitive, default value IPV4. Description: A value of IPV6 means IPV6 NAT64 version; a value of IPv6FullChain means IPv6 version.</p>
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Number(self):
        r"""<p>Count of Cloud Load Balancers to create. Default value: 1.</p>
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def MasterZoneId(self):
        r"""<p>Applicable only to public network IPv4 Cloud Load Balancer. Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.<br>Note: The primary AZ loads traffic. The secondary AZ does not load traffic by default and is used only if the primary AZ becomes unavailable. Currently, primary and secondary AZs are supported only for IPv4 CLB instances in Guangzhou, Shanghai, Nanjing, Beijing, Chengdu, Shenzhen Finance, Hong Kong (China), Seoul, Frankfurt, and Singapore regions. You can call the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> API to query the primary AZ list of a region. [If you need to experience this feature, submit a ticket](https://console.cloud.tencent.com/workorder/category).</p>
        :rtype: str
        """
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def ZoneId(self):
        r"""<p>Applicable only to public network load balancing with IPv4 version. Availability zone ID. Designated availability zone to create a CLB instance, for example: ap-guangzhou-1.</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InternetAccessible(self):
        r"""<p>Maximum outbound bandwidth under the network billing mode. It applies only to LCU-supported instances of the private network type and all instances of the public network type.</p>
        :rtype: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VipIsp(self):
        r"""<p>Applicable only to public network CLB. Currently, static single-line IP type is supported in Guangzhou, Shanghai, Nanjing, Jinan, Hangzhou, Fuzhou, Beijing, Shijiazhuang, Wuhan, Changsha, Chengdu, and Chongqing regions. If you need to experience it, contact business manager to submit a request. After approval, just select CMCC, CUCC, or CTCC as the operator type. Only can be used BANDWIDTH_PACKAGE for network billing mode. If this parameter is not specified, use BGP by default. You can check ISPs supported in a region via the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> api query.</p>
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def Tags(self):
        r"""<p>When you purchase Cloud Load Balancer (CLB), you can tag it with up to 20 tag key-value pairs.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Vip(self):
        r"""<p>Apply for a Cloud Load Balancer with a designated VIP. This parameter is optional. If this parameter is not specified, the VIP is assigned by system. This parameter is supported for IPv4 and IPv6 types but unsupported for IPv6 NAT64 type.<br>Note: When specifying a VIP to create a private network instance or a public IPv6 BGP instance, creation fails if the VIP is not within the specified VPC subnet or if the VIP is already occupied.</p>
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def BandwidthPackageId(self):
        r"""<p>Bandwidth package ID. If this parameter is specified, the network billing mode (InternetAccessible.InternetChargeType) will only support billing by bandwidth package (BANDWIDTH_PACKAGE). The attributes of the bandwidth package determine the settlement method. For IPv6 CLB instances purchased by non-promoted users, if the ISP type is not BGP, the bandwidth package ID cannot be specified.</p>
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def ExclusiveCluster(self):
        r"""<p>Dedicated instance info. This parameter is required when creating a private network CLB instance of exclusive type.</p>
        :rtype: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        """
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def SlaType(self):
        r"""<p>Performance capacity specification.</p><ul><li>If you need to create an LCU-supported instance, this parameter is required. Valid values:<ul><li> clb.c2.medium: Standard </li><li> clb.c3.small: Advanced 1 </li><li> clb.c3.medium: Advanced 2 </li><li> clb.c4.small: Super Large 1 </li><li> clb.c4.medium: Super Large 2 </li><li> clb.c4.large: Super Large 3 </li><li> clb.c4.xlarge: Super Large 4 </li></ul></li><li>For domestic site users, this parameter is not required when creating a shared instance. For international site users, the default purchased instance is standard if this parameter is not passed.</li></ul> For specification details, see [Instance Specifications Comparison](https://www.tencentcloud.com/document/product/214/84689?from_cn_redirect=1).
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def ClientToken(self):
        r"""<p>A string used to ensure request idempotency. This string is generated by the customer and must be unique among different requests, with a maximum value of no more than 64 ASCII characters. If not specified, request idempotency cannot be guaranteed.</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def SnatPro(self):
        r"""<p>Whether the cross-regional or cross-Vpc IP binding feature is supported.</p>
        :rtype: bool
        """
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        r"""<p>After enabling the cross-regional/cross-Vpc IP binding feature, create a SnatIp.</p>
        :rtype: list of SnatIp
        """
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def ClusterTag(self):
        r"""<p>Tag of the Stgw exclusive cluster.</p>
        :rtype: str
        """
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def SlaveZoneId(self):
        r"""<p>Applicable only to public network load balancing with IPv4 version. Sets the secondary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1.<br>Note: The secondary AZ is the availability zone that needs to carry traffic after primary availability zone failure. You can query a region's list of primary/secondary AZs via the <a href="https://www.tencentcloud.com/document/api/214/70213?from_cn_redirect=1">DescribeResources</a> API. [If you need to trial the feature, submit a <a href="https://console.cloud.tencent.com/workorder/category">ticket application</a>]</p>
        :rtype: str
        """
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def EipAddressId(self):
        r"""<p>Unique ID of EIP, such as eip-11112222, applicable only to private network CLB to bind EIP.</p>
        :rtype: str
        """
        return self._EipAddressId

    @EipAddressId.setter
    def EipAddressId(self, EipAddressId):
        self._EipAddressId = EipAddressId

    @property
    def LoadBalancerPassToTarget(self):
        r"""<p>Allow CLB traffic to the Target. Enable (true): verify security groups on CLB; deny CLB traffic to the Target (false): verify security groups on both CLB and backend instances.</p>
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def Egress(self):
        r"""<p>Network outbound</p>
        :rtype: str
        """
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress

    @property
    def LBChargePrepaid(self):
        r"""<p>Prepaid billing attributes of the Cloud Load Balancer instance</p>
        :rtype: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        """
        return self._LBChargePrepaid

    @LBChargePrepaid.setter
    def LBChargePrepaid(self, LBChargePrepaid):
        self._LBChargePrepaid = LBChargePrepaid

    @property
    def LBChargeType(self):
        r"""<p>Billing type of the CLB instance. Valid values: POSTPAID_BY_HOUR and PREPAID. Default value: POSTPAID_BY_HOUR.</p>
        :rtype: str
        """
        return self._LBChargeType

    @LBChargeType.setter
    def LBChargeType(self, LBChargeType):
        self._LBChargeType = LBChargeType

    @property
    def AccessLogTopicId(self):
        r"""<p>L7 access log topic ID</p>
        :rtype: str
        """
        return self._AccessLogTopicId

    @AccessLogTopicId.setter
    def AccessLogTopicId(self, AccessLogTopicId):
        self._AccessLogTopicId = AccessLogTopicId

    @property
    def AdvancedRoute(self):
        r"""<p>Whether layer-7 advanced routing is enabled</p>
        :rtype: bool
        """
        return self._AdvancedRoute

    @AdvancedRoute.setter
    def AdvancedRoute(self, AdvancedRoute):
        self._AdvancedRoute = AdvancedRoute

    @property
    def AvailableZoneAffinityInfo(self):
        r"""<p>Availability zone affinity info</p>
        :rtype: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
        """
        return self._AvailableZoneAffinityInfo

    @AvailableZoneAffinityInfo.setter
    def AvailableZoneAffinityInfo(self, AvailableZoneAffinityInfo):
        self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo


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
        self._Egress = params.get("Egress")
        if params.get("LBChargePrepaid") is not None:
            self._LBChargePrepaid = LBChargePrepaid()
            self._LBChargePrepaid._deserialize(params.get("LBChargePrepaid"))
        self._LBChargeType = params.get("LBChargeType")
        self._AccessLogTopicId = params.get("AccessLogTopicId")
        self._AdvancedRoute = params.get("AdvancedRoute")
        if params.get("AvailableZoneAffinityInfo") is not None:
            self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo()
            self._AvailableZoneAffinityInfo._deserialize(params.get("AvailableZoneAffinityInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    r"""CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: <p>An array of unique IDs of Cloud Load Balancer instances.<br>In certain scenarios, such as a delay in creation, this field may return null. At this point, you can query the created resource ID through the DescribeTaskStatus API using the RequestId or DealName parameter returned by the API.</p>
        :type LoadBalancerIds: list of str
        :param _DealName: <p>Order ID.</p>
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        r"""<p>An array of unique IDs of Cloud Load Balancer instances.<br>In certain scenarios, such as a delay in creation, this field may return null. At this point, you can query the created resource ID through the DescribeTaskStatus API using the RequestId or DealName parameter returned by the API.</p>
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def DealName(self):
        r"""<p>Order ID.</p>
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    r"""DescribeClassicalLBListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _ListenerIds: CLB listener ID list.
        :type ListenerIds: list of str
        :param _Protocol: Protocols for Cloud Load Balancer listeners: 'TCP', 'UDP', 'HTTP', 'HTTPS'.
        :type Protocol: str
        :param _ListenerPort: CLB listening port, range [1-65535].
        :type ListenerPort: int
        :param _Status: Listener status. 0: Creating; 1: Running.
        :type Status: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._ListenerPort = None
        self._Status = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        r"""CLB listener ID list.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        r"""Protocols for Cloud Load Balancer listeners: 'TCP', 'UDP', 'HTTP', 'HTTPS'.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerPort(self):
        r"""CLB listening port, range [1-65535].
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def Status(self):
        r"""Listener status. 0: Creating; 1: Running.
        :rtype: int
        """
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
    r"""DescribeClassicalLBListeners response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Listener list.
        :type Listeners: list of ClassicalListener
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        r"""Listener list.
        :rtype: list of ClassicalListener
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeCustomizedConfigAssociateListRequest(AbstractModel):
    r"""DescribeCustomizedConfigAssociateList request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Configuration ID
        :type ConfigId: str
        :param _Offset: Start position of the binding list. Default: 0.
        :type Offset: int
        :param _Limit: Number of binding lists to pull. Default: 20.
        :type Limit: int
        :param _Domain: search domain
        :type Domain: str
        """
        self._ConfigId = None
        self._Offset = None
        self._Limit = None
        self._Domain = None

    @property
    def ConfigId(self):
        r"""Configuration ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Offset(self):
        r"""Start position of the binding list. Default: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of binding lists to pull. Default: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Domain(self):
        r"""search domain
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
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
    r"""DescribeCustomizedConfigAssociateList response structure.

    """

    def __init__(self):
        r"""
        :param _BindList: Binding relationship list
        :type BindList: list of BindDetailItem
        :param _TotalCount: Total number of binding relationships
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BindList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BindList(self):
        r"""Binding relationship list
        :rtype: list of BindDetailItem
        """
        return self._BindList

    @BindList.setter
    def BindList(self, BindList):
        self._BindList = BindList

    @property
    def TotalCount(self):
        r"""Total number of binding relationships
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeCustomizedConfigList request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigType: Configuration type. CLB: CLB dimension; SERVER: Domain name dimension; LOCATION: Rule dimension.
        :type ConfigType: str
        :param _Offset: Pagination offset. Default: 0
        :type Offset: int
        :param _Limit: Number of results. Default: 20
        :type Limit: int
        :param _ConfigName: Specify the name of configurations to query. Fuzzy match is supported.
        :type ConfigName: str
        :param _ConfigIds: Configuration ID
        :type ConfigIds: list of str
        :param _Filters: Filter criteria are as follows:
<li> loadbalancer-id - String - Required: No - (Filter condition) Filter by CLB ID, for example: "lb-12345678".</li>
<li> vip - String - Required: No - (Filter condition) Filter by CLB vip, for example: "1.1.1.1", "2204::22:3".</li>
        :type Filters: list of Filter
        """
        self._ConfigType = None
        self._Offset = None
        self._Limit = None
        self._ConfigName = None
        self._ConfigIds = None
        self._Filters = None

    @property
    def ConfigType(self):
        r"""Configuration type. CLB: CLB dimension; SERVER: Domain name dimension; LOCATION: Rule dimension.
        :rtype: str
        """
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType

    @property
    def Offset(self):
        r"""Pagination offset. Default: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of results. Default: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConfigName(self):
        r"""Specify the name of configurations to query. Fuzzy match is supported.
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ConfigIds(self):
        r"""Configuration ID
        :rtype: list of str
        """
        return self._ConfigIds

    @ConfigIds.setter
    def ConfigIds(self, ConfigIds):
        self._ConfigIds = ConfigIds

    @property
    def Filters(self):
        r"""Filter criteria are as follows:
<li> loadbalancer-id - String - Required: No - (Filter condition) Filter by CLB ID, for example: "lb-12345678".</li>
<li> vip - String - Required: No - (Filter condition) Filter by CLB vip, for example: "1.1.1.1", "2204::22:3".</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ConfigType = params.get("ConfigType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConfigName = params.get("ConfigName")
        self._ConfigIds = params.get("ConfigIds")
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
    r"""DescribeCustomizedConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigList: Configuration list
        :type ConfigList: list of ConfigListItem
        :param _TotalCount: Number of configurations
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConfigList(self):
        r"""Configuration list
        :rtype: list of ConfigListItem
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def TotalCount(self):
        r"""Number of configurations
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    r"""DescribeLoadBalancerListByCertId request structure.

    """

    def __init__(self):
        r"""
        :param _CertIds: Server or client certificate ID
        :type CertIds: list of str
        """
        self._CertIds = None

    @property
    def CertIds(self):
        r"""Server or client certificate ID
        :rtype: list of str
        """
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
    r"""DescribeLoadBalancerListByCertId response structure.

    """

    def __init__(self):
        r"""
        :param _CertSet: Certificate ID and the list of CLB instances associated with the certificate ID
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertSet = None
        self._RequestId = None

    @property
    def CertSet(self):
        r"""Certificate ID and the list of CLB instances associated with the certificate ID
        :rtype: list of CertIdRelatedWithLoadBalancers
        """
        return self._CertSet

    @CertSet.setter
    def CertSet(self, CertSet):
        self._CertSet = CertSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeLoadBalancersDetailRequest(AbstractModel):
    r"""DescribeLoadBalancersDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Return the number of Cloud Load Balancer (CLB) lists. Default is 20. Maximum value is 100.
        :type Limit: int
        :param _Offset: Starting offset for returning the list of CLB instances, with a default value of 0.
        :type Offset: int
        :param _Fields: Select the Fields list to return. The system will only return the Fields filled in Fields. For fillable field details, see <a href="https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#LoadBalancerDetail">LoadBalancerDetail</a>. If a related field is not in Fields, this field returns null. The LoadBalancerId and LoadBalancerName Fields are added by default in Fields.
        :type Fields: list of str
        :param _TargetType: When the Fields include TargetId, TargetAddress, TargetPort, TargetWeight, ListenerId, Protocol, Port, LocationId, Domain, and Url, you must select exporting the Target of the target group or a non-target group. Valid values: NODE, GROUP.
        :type TargetType: str
        :param _Filters: Query the detailed information list of Cloud Load Balancer. Detailed filter criteria:
<li> loadbalancer-id - String - Required: No - (Filter condition) Filter by CLB ID, for example: "lb-12345678".</li>
<li> project-id - String - Required: No - (Filter condition) Filter by project ID, for example: "0", "123".</li>
<li>network - String - Required: No - (Filter condition) Filter by CLB network type, such as "Public" or "Private".</li>
<li> vip - String - Required: No - (Filter condition) Filter by CLB vip, for example: "1.1.1.1", "2204::22:3".</li>
<li> target-ip - String - Required: No - (Filtering Conditions) Filter by private ip of the target real server, such as "1.1.1.1", "2203::214:4".</li>
<li> vpcid - String - Required: No - (Filter condition) Filter by the associated vpc ID of the Cloud Load Balancer (CLB), such as "vpc-12345678".</li>
<li> zone - String - Required: No - (Filtering Conditions) Filter by the availability zone the load balancing belongs to, such as "ap-guangzhou-1".</li>
<li>tag-key - String - required: no - (filter condition) filter by tag key of Cloud Load Balancer, such as "name".</li>
<li> tag:* - String - Required: No - (Filter criteria) Filter by the tag of Cloud Load Balancer (CLB), where ':' is followed by the tag key. For example, to filter by tag key 'name' and tag values 'zhangsan' and 'lisi', use {"Name": "tag:name","Values": ["zhangsan", "lisi"]}.</li>
<li>fuzzy-search - String - required: no - (filter condition) fuzzy search by CLB Vip and CLB name, for example: "1.1".</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Fields = None
        self._TargetType = None
        self._Filters = None

    @property
    def Limit(self):
        r"""Return the number of Cloud Load Balancer (CLB) lists. Default is 20. Maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Starting offset for returning the list of CLB instances, with a default value of 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Fields(self):
        r"""Select the Fields list to return. The system will only return the Fields filled in Fields. For fillable field details, see <a href="https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#LoadBalancerDetail">LoadBalancerDetail</a>. If a related field is not in Fields, this field returns null. The LoadBalancerId and LoadBalancerName Fields are added by default in Fields.
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def TargetType(self):
        r"""When the Fields include TargetId, TargetAddress, TargetPort, TargetWeight, ListenerId, Protocol, Port, LocationId, Domain, and Url, you must select exporting the Target of the target group or a non-target group. Valid values: NODE, GROUP.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Filters(self):
        r"""Query the detailed information list of Cloud Load Balancer. Detailed filter criteria:
<li> loadbalancer-id - String - Required: No - (Filter condition) Filter by CLB ID, for example: "lb-12345678".</li>
<li> project-id - String - Required: No - (Filter condition) Filter by project ID, for example: "0", "123".</li>
<li>network - String - Required: No - (Filter condition) Filter by CLB network type, such as "Public" or "Private".</li>
<li> vip - String - Required: No - (Filter condition) Filter by CLB vip, for example: "1.1.1.1", "2204::22:3".</li>
<li> target-ip - String - Required: No - (Filtering Conditions) Filter by private ip of the target real server, such as "1.1.1.1", "2203::214:4".</li>
<li> vpcid - String - Required: No - (Filter condition) Filter by the associated vpc ID of the Cloud Load Balancer (CLB), such as "vpc-12345678".</li>
<li> zone - String - Required: No - (Filtering Conditions) Filter by the availability zone the load balancing belongs to, such as "ap-guangzhou-1".</li>
<li>tag-key - String - required: no - (filter condition) filter by tag key of Cloud Load Balancer, such as "name".</li>
<li> tag:* - String - Required: No - (Filter criteria) Filter by the tag of Cloud Load Balancer (CLB), where ':' is followed by the tag key. For example, to filter by tag key 'name' and tag values 'zhangsan' and 'lisi', use {"Name": "tag:name","Values": ["zhangsan", "lisi"]}.</li>
<li>fuzzy-search - String - required: no - (filter condition) fuzzy search by CLB Vip and CLB name, for example: "1.1".</li>
        :rtype: list of Filter
        """
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
    r"""DescribeLoadBalancersDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items in CLB detail list.
        :type TotalCount: int
        :param _LoadBalancerDetailSet: Cloud Load Balancer detail list.
        :type LoadBalancerDetailSet: list of LoadBalancerDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerDetailSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of items in CLB detail list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerDetailSet(self):
        r"""Cloud Load Balancer detail list.
        :rtype: list of LoadBalancerDetail
        """
        return self._LoadBalancerDetailSet

    @LoadBalancerDetailSet.setter
    def LoadBalancerDetailSet(self, LoadBalancerDetailSet):
        self._LoadBalancerDetailSet = LoadBalancerDetailSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: CLB instance ID. There can be up to 20 IDs.
        :type LoadBalancerIds: list of str
        :param _LoadBalancerType: Network type of the CLB instance:
OPEN: Public network attribute. INTERNAL: Private network attribute.
        :type LoadBalancerType: str
        :param _Forward: CLB instance type. 1: General CLB instance; 0: Classic CLB instance. If this parameter is not specified, all types of CLB instances will be queried.
        :type Forward: int
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _Domain: Domain name assigned for a CLB instance by the cloud platform.
        :type Domain: str
        :param _LoadBalancerVips: VIP address of a CLB instance (there can be multiple addresses).
        :type LoadBalancerVips: list of str
        :param _BackendPublicIps: The public network IP of the backend service bound to Cloud Load Balancer (CLB) only supports querying the public IP of Cloud Virtual Machine (CVM).
        :type BackendPublicIps: list of str
        :param _BackendPrivateIps: The private network IP of the backend service bound to Cloud Load Balancer (CLB) only supports querying the private IP address of Cloud Virtual Machine (CVM).
        :type BackendPrivateIps: list of str
        :param _Offset: Data offset. Default: 0.
        :type Offset: int
        :param _Limit: Number of CLB instances returned. Default: 20. Maximum: 100.
        :type Limit: int
        :param _OrderBy: A sorting parameter. Valid values: LoadBalancerName, CreateTime, Domain, and LoadBalancerType.
        :type OrderBy: str
        :param _OrderType: 1: Reverse; 0: Sequential. Default: reverse by creation time
        :type OrderType: int
        :param _SearchKey: Search field, supporting fuzzy match by name, domain, and VIP.
        :type SearchKey: str
        :param _ProjectId: The ID of the project to which the CLB instance belongs. This parameter can be obtained through the DescribeProject API.
        :type ProjectId: int
        :param _WithRs: Whether CLB is bound to a real server. 0: No; 1: Yes; -1: Query all.
        :type WithRs: int
        :param _VpcId: Unique VPC ID of the CLB instance, such as vpc-bhqkbhdx
Basic network allows input '0'.
        :type VpcId: str
        :param _SecurityGroup: Security group ID, for example sg-m1cc****.
        :type SecurityGroup: str
        :param _MasterZone: Primary availability zone ID, such as 100001 (corresponding to Guangzhou Zone 1). You can obtain the list of availability zones through [DescribeZones](https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1).
        :type MasterZone: str
        :param _Filters: Each request can have up to 10 `Filters` values and 100 `Filter.Values` values.<br/>`Filter.Name` and `Filter.Values` are required items. The detailed filter criteria are as follows:
<li> charge-type - String - Required: No - (Filter condition) Filter by the CLB instance billing mode, including "PREPAID", "POSTPAID_BY_HOUR".</li>
<li> internet-charge-type - String - Required: No - (Filter condition) Filter by CLB network billing mode, including "BANDWIDTH_PREPAID", "TRAFFIC_POSTPAID_BY_HOUR", "BANDWIDTH_POSTPAID_BY_HOUR", "BANDWIDTH_PACKAGE".</li>
<li> master-zone-id - String - Required: No - (Filter condition) Filter by primary AZ ID of CLB, such as "100001" (corresponding to Guangzhou Zone 1).</li>
<li>tag-key - String - required: no - (filter condition) filter by CLB tag key.</li>
<li>tag:tag-key - String - Required: no - (Filter condition) Filter by CLB Tag key-value pair. Replace tag-key with a specific tag key.</li>
<li> function-name - String - Required: No - (Filter condition) Filter by the function name of the Serverless Cloud Function (SCF) bound to the CLB backend.</li>
<li> vip-isp - String - Required: No - (Filter condition) Filter by operator type of CLB VIP, such as "BGP", "INTERNAL", "CMCC", "CTCC", "CUCC".</li>
<li>sla-type - String - required: no - (filter condition) filter by CLB performance capacity specification, including "clb.c2.medium", "clb.c3.small", "clb.c3.medium", "clb.c4.small", "clb.c4.medium", "clb.c4.large", "clb.c4.xlarge".</li>
        :type Filters: list of Filter
        :param _AdditionalFields: Select the expansion fields to return. If not specified, expansion fields are not returned by default. The supported expansion fields are as follows:
<li> TargetCount: Number of real servers bound to it</li>
        :type AdditionalFields: list of str
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
        self._AdditionalFields = None

    @property
    def LoadBalancerIds(self):
        r"""CLB instance ID. There can be up to 20 IDs.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerType(self):
        r"""Network type of the CLB instance:
OPEN: Public network attribute. INTERNAL: Private network attribute.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        r"""CLB instance type. 1: General CLB instance; 0: Classic CLB instance. If this parameter is not specified, all types of CLB instances will be queried.
        :rtype: int
        """
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def LoadBalancerName(self):
        r"""CLB instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Domain(self):
        r"""Domain name assigned for a CLB instance by the cloud platform.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        r"""VIP address of a CLB instance (there can be multiple addresses).
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def BackendPublicIps(self):
        r"""The public network IP of the backend service bound to Cloud Load Balancer (CLB) only supports querying the public IP of Cloud Virtual Machine (CVM).
        :rtype: list of str
        """
        return self._BackendPublicIps

    @BackendPublicIps.setter
    def BackendPublicIps(self, BackendPublicIps):
        self._BackendPublicIps = BackendPublicIps

    @property
    def BackendPrivateIps(self):
        r"""The private network IP of the backend service bound to Cloud Load Balancer (CLB) only supports querying the private IP address of Cloud Virtual Machine (CVM).
        :rtype: list of str
        """
        return self._BackendPrivateIps

    @BackendPrivateIps.setter
    def BackendPrivateIps(self, BackendPrivateIps):
        self._BackendPrivateIps = BackendPrivateIps

    @property
    def Offset(self):
        r"""Data offset. Default: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of CLB instances returned. Default: 20. Maximum: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""A sorting parameter. Valid values: LoadBalancerName, CreateTime, Domain, and LoadBalancerType.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""1: Reverse; 0: Sequential. Default: reverse by creation time
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def SearchKey(self):
        r"""Search field, supporting fuzzy match by name, domain, and VIP.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectId(self):
        r"""The ID of the project to which the CLB instance belongs. This parameter can be obtained through the DescribeProject API.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WithRs(self):
        r"""Whether CLB is bound to a real server. 0: No; 1: Yes; -1: Query all.
        :rtype: int
        """
        return self._WithRs

    @WithRs.setter
    def WithRs(self, WithRs):
        self._WithRs = WithRs

    @property
    def VpcId(self):
        r"""Unique VPC ID of the CLB instance, such as vpc-bhqkbhdx
Basic network allows input '0'.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SecurityGroup(self):
        r"""Security group ID, for example sg-m1cc****.
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def MasterZone(self):
        r"""Primary availability zone ID, such as 100001 (corresponding to Guangzhou Zone 1). You can obtain the list of availability zones through [DescribeZones](https://www.tencentcloud.com/document/product/213/15707?from_cn_redirect=1).
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def Filters(self):
        r"""Each request can have up to 10 `Filters` values and 100 `Filter.Values` values.<br/>`Filter.Name` and `Filter.Values` are required items. The detailed filter criteria are as follows:
<li> charge-type - String - Required: No - (Filter condition) Filter by the CLB instance billing mode, including "PREPAID", "POSTPAID_BY_HOUR".</li>
<li> internet-charge-type - String - Required: No - (Filter condition) Filter by CLB network billing mode, including "BANDWIDTH_PREPAID", "TRAFFIC_POSTPAID_BY_HOUR", "BANDWIDTH_POSTPAID_BY_HOUR", "BANDWIDTH_PACKAGE".</li>
<li> master-zone-id - String - Required: No - (Filter condition) Filter by primary AZ ID of CLB, such as "100001" (corresponding to Guangzhou Zone 1).</li>
<li>tag-key - String - required: no - (filter condition) filter by CLB tag key.</li>
<li>tag:tag-key - String - Required: no - (Filter condition) Filter by CLB Tag key-value pair. Replace tag-key with a specific tag key.</li>
<li> function-name - String - Required: No - (Filter condition) Filter by the function name of the Serverless Cloud Function (SCF) bound to the CLB backend.</li>
<li> vip-isp - String - Required: No - (Filter condition) Filter by operator type of CLB VIP, such as "BGP", "INTERNAL", "CMCC", "CTCC", "CUCC".</li>
<li>sla-type - String - required: no - (filter condition) filter by CLB performance capacity specification, including "clb.c2.medium", "clb.c3.small", "clb.c3.medium", "clb.c4.small", "clb.c4.medium", "clb.c4.large", "clb.c4.xlarge".</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AdditionalFields(self):
        r"""Select the expansion fields to return. If not specified, expansion fields are not returned by default. The supported expansion fields are as follows:
<li> TargetCount: Number of real servers bound to it</li>
        :rtype: list of str
        """
        return self._AdditionalFields

    @AdditionalFields.setter
    def AdditionalFields(self, AdditionalFields):
        self._AdditionalFields = AdditionalFields


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
        self._AdditionalFields = params.get("AdditionalFields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    r"""DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of CLB instances that meet the filter criteria. This value is independent of the Limit in the input parameters.
        :type TotalCount: int
        :param _LoadBalancerSet: Returned CLB instance array.
        :type LoadBalancerSet: list of LoadBalancer
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of CLB instances that meet the filter criteria. This value is independent of the Limit in the input parameters.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        r"""Returned CLB instance array.
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeTargetHealthRequest(AbstractModel):
    r"""DescribeTargetHealth request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: List of CLB instance IDs to query.
        :type LoadBalancerIds: list of str
        :param _ListenerIds: Listener ID list to query.
        :type ListenerIds: list of str
        :param _LocationIds: List of forwarding rule IDs to query.
        :type LocationIds: list of str
        """
        self._LoadBalancerIds = None
        self._ListenerIds = None
        self._LocationIds = None

    @property
    def LoadBalancerIds(self):
        r"""List of CLB instance IDs to query.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ListenerIds(self):
        r"""Listener ID list to query.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def LocationIds(self):
        r"""List of forwarding rule IDs to query.
        :rtype: list of str
        """
        return self._LocationIds

    @LocationIds.setter
    def LocationIds(self, LocationIds):
        self._LocationIds = LocationIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ListenerIds = params.get("ListenerIds")
        self._LocationIds = params.get("LocationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    r"""DescribeTargetHealth response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: LoadBalancer list.
        :type LoadBalancers: list of LoadBalancerHealth
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        r"""LoadBalancer list.
        :rtype: list of LoadBalancerHealth
        """
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class ExclusiveCluster(AbstractModel):
    r"""Exclusive cluster

    """

    def __init__(self):
        r"""
        :param _L4Clusters: Layer-4 exclusive cluster list
Note: This field may return null, indicating that no valid values can be obtained.
        :type L4Clusters: list of ClusterItem
        :param _L7Clusters: Layer-7 exclusive cluster list
Note: This field may return null, indicating that no valid values can be obtained.
        :type L7Clusters: list of ClusterItem
        :param _ClassicalCluster: VPCGW cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClassicalCluster: :class:`tencentcloud.clb.v20230417.models.ClusterItem`
        """
        self._L4Clusters = None
        self._L7Clusters = None
        self._ClassicalCluster = None

    @property
    def L4Clusters(self):
        r"""Layer-4 exclusive cluster list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ClusterItem
        """
        return self._L4Clusters

    @L4Clusters.setter
    def L4Clusters(self, L4Clusters):
        self._L4Clusters = L4Clusters

    @property
    def L7Clusters(self):
        r"""Layer-7 exclusive cluster list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ClusterItem
        """
        return self._L7Clusters

    @L7Clusters.setter
    def L7Clusters(self, L7Clusters):
        self._L7Clusters = L7Clusters

    @property
    def ClassicalCluster(self):
        r"""VPCGW cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.ClusterItem`
        """
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
    r"""Reserved. Generally unnecessary for users to concern.

    """

    def __init__(self):
        r"""
        :param _Dnat: Whether to enable VIP Direct Connect
        :type Dnat: bool
        :param _TgwGroupName: TgwGroup name
        :type TgwGroupName: str
        """
        self._Dnat = None
        self._TgwGroupName = None

    @property
    def Dnat(self):
        r"""Whether to enable VIP Direct Connect
        :rtype: bool
        """
        return self._Dnat

    @Dnat.setter
    def Dnat(self, Dnat):
        self._Dnat = Dnat

    @property
    def TgwGroupName(self):
        r"""TgwGroup name
        :rtype: str
        """
        return self._TgwGroupName

    @TgwGroupName.setter
    def TgwGroupName(self, TgwGroupName):
        self._TgwGroupName = TgwGroupName


    def _deserialize(self, params):
        self._Dnat = params.get("Dnat")
        self._TgwGroupName = params.get("TgwGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Filter criteria

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
        r"""Filter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value array
        :rtype: list of str
        """
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
        


class InternetAccessible(AbstractModel):
    r"""Network billing mode, maximum outbound bandwidth

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR: postpaid by traffic on an hourly basis;
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: Maximum outbound bandwidth in Mbps. It applies only to shared, LCU-supported, and exclusive CLB instances of the public network type and LCU-supported CLB instances of the private network type.
-For shared type and exclusive CLB instances with public network attributes, the maximum outbound bandwidth ranges from 1Mbps to 2048Mbps.
-For LCU-supported CLB instances with public network attributes and private network attributes, the maximum outbound bandwidth ranges from 1Mbps to 61440Mbps.
(If this parameter is not specified when CreateLoadBalancer is called to create a CLB instance, the default value of 10 Mbps is used. This value can be modified.)
        :type InternetMaxBandwidthOut: int
        :param _BandwidthPackageSubType: Bandwidth package type, such as SINGLEISP (single ISP) and BGP (multi ISP).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BandwidthPackageSubType: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._BandwidthPackageSubType = None

    @property
    def InternetChargeType(self):
        r"""TRAFFIC_POSTPAID_BY_HOUR: postpaid by traffic on an hourly basis;
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        r"""Maximum outbound bandwidth in Mbps. It applies only to shared, LCU-supported, and exclusive CLB instances of the public network type and LCU-supported CLB instances of the private network type.
-For shared type and exclusive CLB instances with public network attributes, the maximum outbound bandwidth ranges from 1Mbps to 2048Mbps.
-For LCU-supported CLB instances with public network attributes and private network attributes, the maximum outbound bandwidth ranges from 1Mbps to 61440Mbps.
(If this parameter is not specified when CreateLoadBalancer is called to create a CLB instance, the default value of 10 Mbps is used. This value can be modified.)
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthPackageSubType(self):
        r"""Bandwidth package type, such as SINGLEISP (single ISP) and BGP (multi ISP).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BandwidthPackageSubType

    @BandwidthPackageSubType.setter
    def BandwidthPackageSubType(self, BandwidthPackageSubType):
        self._BandwidthPackageSubType = BandwidthPackageSubType


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._BandwidthPackageSubType = params.get("BandwidthPackageSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LBChargePrepaid(AbstractModel):
    r"""Retention type

    """

    def __init__(self):
        r"""
        :param _RenewFlag: Reserved field.
        :type RenewFlag: str
        :param _Period: Reserved field.
        :type Period: int
        """
        self._RenewFlag = None
        self._Period = None

    @property
    def RenewFlag(self):
        r"""Reserved field.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Period(self):
        r"""Reserved field.
        :rtype: int
        """
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
        


class ListenerHealth(AbstractModel):
    r"""Health check information of the listener

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: listener name
        :type ListenerName: str
        :param _Protocol: Listener protocol
        :type Protocol: str
        :param _Port: Listener port
        :type Port: int
        :param _Rules: List of forwarding rules of the listener
        :type Rules: list of RuleHealth
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._Port = None
        self._Rules = None

    @property
    def ListenerId(self):
        r"""Listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""listener name
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        r"""Listener protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""Listener port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        r"""List of forwarding rules of the listener
        :rtype: list of RuleHealth
        """
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
        


class LoadBalancer(AbstractModel):
    r"""CLB instance information

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerType: Network type of the CLB instance:
OPEN: Public network attribute. INTERNAL: Intranet attribute. For a CLB with intranet attribute, you can bind EIP for public network access. For details, see the EIP document.
        :type LoadBalancerType: str
        :param _Forward: Load balancer type identifier. 1: CLB; 0: Classic CLB.
        :type Forward: int
        :param _Domain: The domain name of the Cloud Load Balancer instance. This field is only provided by public network-based and domain name-based CLB instances. It is being gradually phased out. We recommend using LoadBalancerDomain instead.
        :type Domain: str
        :param _LoadBalancerVips: List of VIPs of a CLB instance.
        :type LoadBalancerVips: list of str
        :param _Status: CLB instance state, including
0: creating, 1: normal operation.
        :type Status: int
        :param _CreateTime: CLB instance creation time
        :type CreateTime: str
        :param _StatusTime: Last status transition time of the CLB instance.
        :type StatusTime: str
        :param _ProjectId: The ID of the project to which the CLB instance belongs. 0: Default project.
        :type ProjectId: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _OpenBgp: Anti-DDoS Pro identifier for CLB. 1: CLB with Anti-DDoS Pro; 0: CLB without Anti-DDoS Pro.
        :type OpenBgp: int
        :param _Snat: Private network Classic CLB instances before December 2016 had SNAT enabled.
        :type Snat: bool
        :param _Isolation: 0: Not isolated; 1: Isolated.
        :type Isolation: int
        :param _Log: User-enabled log information. Only public network CLB instances that have an HTTP or HTTPS listener can generate logs.
        :type Log: str
        :param _SubnetId: Subnet of the CLB instance (applicable only to VPC-type CLB instances on private networks)
        :type SubnetId: str
        :param _Tags: CLB instance tag information
        :type Tags: list of TagInfo
        :param _SecureGroups: Security group of the CLB instance
        :type SecureGroups: list of str
        :param _TargetRegionInfo: Basic information of real servers bound to the CLB instance
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20230417.models.TargetRegionInfo`
        :param _AnycastZone: Anycast CLB release domain. For non-anycast CLB, this field returns an empty string.
        :type AnycastZone: str
        :param _AddressIPVersion: IP Version, ipv4 | ipv6
        :type AddressIPVersion: str
        :param _NumericalVpcId: VPC ID in numerical format
        :type NumericalVpcId: int
        :param _VipIsp: ISP of the load balancer IP. Value ranges from BGP to CUCC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VipIsp: str
        :param _MasterZone: Primary AZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterZone: :class:`tencentcloud.clb.v20230417.models.ZoneInfo`
        :param _BackupZoneSet: standby availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupZoneSet: list of ZoneInfo
        :param _IsolatedTime: CLB instance isolation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param _ExpireTime: Expiration Time of the CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _ChargeType: Billing type of the Cloud Load Balancer instance, PREPAID: Monthly Subscription, POSTPAID_BY_HOUR: Pay-As-You-Go
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _NetworkAttributes: CLB instance network attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        :param _PrepaidAttributes: Reserved field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        :param _LogSetId: Log set ID of Cloud Log Service (CLS) for CLB
        :type LogSetId: str
        :param _LogTopicId: Log topic ID of Cloud Log Service (CLS) for CLB
        :type LogTopicId: str
        :param _AddressIPv6: IPv6 address of the CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param _ExtraInfo: Reserved. Generally unnecessary for users to concern.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20230417.models.ExtraInfo`
        :param _IsDDos: Whether an Anti-DDoS Pro instance can be bound
        :type IsDDos: bool
        :param _ConfigId: Custom configuration IDs of CLB instances
        :type ConfigId: str
        :param _LoadBalancerPassToTarget: Whether the real server allows traffic from CLB
        :type LoadBalancerPassToTarget: bool
        :param _ExclusiveCluster: Exclusive cluster on the private network
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        :param _IPv6Mode: This field is meaningful when the IP address version is IPv6. IPv6Nat64 | IPv6FullChain
Note: This field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param _SnatPro: Is SnatPro enabled?
        :type SnatPro: bool
        :param _SnatIps: After enabling SnatPro load balancing, the SnatIp list.
        :type SnatIps: list of SnatIp
        :param _SlaType: Performance capacity specification.<ul><li> clb.c1.small: Minimalist specification </li><li> clb.c2.medium: Standard specification </li><li> clb.c3.small: High-tier 1 specification </li><li> clb.c3.medium: High-tier 2 specification </li><li> clb.c4.small: Super-tier 1 specification </li><li> clb.c4.medium: Super-tier 2 specification </li><li> clb.c4.large: Super-tier 3 specification </li><li> clb.c4.xlarge: Super-tier 4 specification </li><li>"": Non-LCU-supported instance</li></ul>
        :type SlaType: str
        :param _IsBlock: Whether VIP is blocked
        :type IsBlock: bool
        :param _IsBlockTime: Blocking or unblocking time
        :type IsBlockTime: str
        :param _LocalBgp: Whether the IP type is Local BGP
        :type LocalBgp: bool
        :param _ClusterTag: Layer-7 exclusive tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterTag: str
        :param _MixIpTarget: If the layer-7 listener of an IPv6FullChain CLB instance is enabled, the CLB instance can be bound with IPv4 and IPv6 CVM instances simultaneously.
        :type MixIpTarget: bool
        :param _Zones: VPC-based private network CLB. AZ where the rule is in proximity access mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _NfvInfo: Whether CLB is NFV. Empty: No; l7nfv: NFV for layer 7.
        :type NfvInfo: str
        :param _HealthLogSetId: Health check log set ID of Cloud Log Service (CLS) for CLB
        :type HealthLogSetId: str
        :param _HealthLogTopicId: Health check log topic ID of Cloud Log Service (CLS) for CLB
        :type HealthLogTopicId: str
        :param _ClusterIds: Cluster ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterIds: list of str
        :param _AttributeFlags: Attributes of Cloud Load Balancer
        :type AttributeFlags: list of str
        :param _LoadBalancerDomain: Domain name of the CLB instance.
        :type LoadBalancerDomain: str
        :param _Egress: Network outbound
        :type Egress: str
        :param _Exclusive: Whether the instance type is exclusive type. 1: Dedicated instance. 0: Non-dedicated instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Exclusive: int
        :param _TargetCount: Number of bound backend services.
        :type TargetCount: int
        :param _AssociateEndpoint: Endpoint Id associated with the CLB instance.
        :type AssociateEndpoint: str
        :param _AvailableZoneAffinityInfo: Availability zone forward affinity info
        :type AvailableZoneAffinityInfo: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
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
        self._Exclusive = None
        self._TargetCount = None
        self._AssociateEndpoint = None
        self._AvailableZoneAffinityInfo = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""CLB instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        r"""Network type of the CLB instance:
OPEN: Public network attribute. INTERNAL: Intranet attribute. For a CLB with intranet attribute, you can bind EIP for public network access. For details, see the EIP document.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Forward(self):
        r"""Load balancer type identifier. 1: CLB; 0: Classic CLB.
        :rtype: int
        """
        return self._Forward

    @Forward.setter
    def Forward(self, Forward):
        self._Forward = Forward

    @property
    def Domain(self):
        r"""The domain name of the Cloud Load Balancer instance. This field is only provided by public network-based and domain name-based CLB instances. It is being gradually phased out. We recommend using LoadBalancerDomain instead.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerVips(self):
        r"""List of VIPs of a CLB instance.
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Status(self):
        r"""CLB instance state, including
0: creating, 1: normal operation.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""CLB instance creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        r"""Last status transition time of the CLB instance.
        :rtype: str
        """
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def ProjectId(self):
        r"""The ID of the project to which the CLB instance belongs. 0: Default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OpenBgp(self):
        r"""Anti-DDoS Pro identifier for CLB. 1: CLB with Anti-DDoS Pro; 0: CLB without Anti-DDoS Pro.
        :rtype: int
        """
        return self._OpenBgp

    @OpenBgp.setter
    def OpenBgp(self, OpenBgp):
        self._OpenBgp = OpenBgp

    @property
    def Snat(self):
        r"""Private network Classic CLB instances before December 2016 had SNAT enabled.
        :rtype: bool
        """
        return self._Snat

    @Snat.setter
    def Snat(self, Snat):
        self._Snat = Snat

    @property
    def Isolation(self):
        r"""0: Not isolated; 1: Isolated.
        :rtype: int
        """
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def Log(self):
        r"""User-enabled log information. Only public network CLB instances that have an HTTP or HTTPS listener can generate logs.
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def SubnetId(self):
        r"""Subnet of the CLB instance (applicable only to VPC-type CLB instances on private networks)
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Tags(self):
        r"""CLB instance tag information
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecureGroups(self):
        r"""Security group of the CLB instance
        :rtype: list of str
        """
        return self._SecureGroups

    @SecureGroups.setter
    def SecureGroups(self, SecureGroups):
        self._SecureGroups = SecureGroups

    @property
    def TargetRegionInfo(self):
        r"""Basic information of real servers bound to the CLB instance
        :rtype: :class:`tencentcloud.clb.v20230417.models.TargetRegionInfo`
        """
        return self._TargetRegionInfo

    @TargetRegionInfo.setter
    def TargetRegionInfo(self, TargetRegionInfo):
        self._TargetRegionInfo = TargetRegionInfo

    @property
    def AnycastZone(self):
        r"""Anycast CLB release domain. For non-anycast CLB, this field returns an empty string.
        :rtype: str
        """
        return self._AnycastZone

    @AnycastZone.setter
    def AnycastZone(self, AnycastZone):
        self._AnycastZone = AnycastZone

    @property
    def AddressIPVersion(self):
        r"""IP Version, ipv4 | ipv6
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def NumericalVpcId(self):
        r"""VPC ID in numerical format
        :rtype: int
        """
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def VipIsp(self):
        r"""ISP of the load balancer IP. Value ranges from BGP to CUCC.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def MasterZone(self):
        r"""Primary AZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.ZoneInfo`
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def BackupZoneSet(self):
        r"""standby availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ZoneInfo
        """
        return self._BackupZoneSet

    @BackupZoneSet.setter
    def BackupZoneSet(self, BackupZoneSet):
        self._BackupZoneSet = BackupZoneSet

    @property
    def IsolatedTime(self):
        r"""CLB instance isolation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ExpireTime(self):
        r"""Expiration Time of the CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChargeType(self):
        r"""Billing type of the Cloud Load Balancer instance, PREPAID: Monthly Subscription, POSTPAID_BY_HOUR: Pay-As-You-Go
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        r"""CLB instance network attributes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        """
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        r"""Reserved field.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        """
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def LogSetId(self):
        r"""Log set ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        r"""Log topic ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def AddressIPv6(self):
        r"""IPv6 address of the CLB instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def ExtraInfo(self):
        r"""Reserved. Generally unnecessary for users to concern.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def IsDDos(self):
        r"""Whether an Anti-DDoS Pro instance can be bound
        :rtype: bool
        """
        return self._IsDDos

    @IsDDos.setter
    def IsDDos(self, IsDDos):
        self._IsDDos = IsDDos

    @property
    def ConfigId(self):
        r"""Custom configuration IDs of CLB instances
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def LoadBalancerPassToTarget(self):
        r"""Whether the real server allows traffic from CLB
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def ExclusiveCluster(self):
        r"""Exclusive cluster on the private network
        :rtype: :class:`tencentcloud.clb.v20230417.models.ExclusiveCluster`
        """
        return self._ExclusiveCluster

    @ExclusiveCluster.setter
    def ExclusiveCluster(self, ExclusiveCluster):
        self._ExclusiveCluster = ExclusiveCluster

    @property
    def IPv6Mode(self):
        r"""This field is meaningful when the IP address version is IPv6. IPv6Nat64 | IPv6FullChain
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def SnatPro(self):
        r"""Is SnatPro enabled?
        :rtype: bool
        """
        return self._SnatPro

    @SnatPro.setter
    def SnatPro(self, SnatPro):
        self._SnatPro = SnatPro

    @property
    def SnatIps(self):
        r"""After enabling SnatPro load balancing, the SnatIp list.
        :rtype: list of SnatIp
        """
        return self._SnatIps

    @SnatIps.setter
    def SnatIps(self, SnatIps):
        self._SnatIps = SnatIps

    @property
    def SlaType(self):
        r"""Performance capacity specification.<ul><li> clb.c1.small: Minimalist specification </li><li> clb.c2.medium: Standard specification </li><li> clb.c3.small: High-tier 1 specification </li><li> clb.c3.medium: High-tier 2 specification </li><li> clb.c4.small: Super-tier 1 specification </li><li> clb.c4.medium: Super-tier 2 specification </li><li> clb.c4.large: Super-tier 3 specification </li><li> clb.c4.xlarge: Super-tier 4 specification </li><li>"": Non-LCU-supported instance</li></ul>
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def IsBlock(self):
        r"""Whether VIP is blocked
        :rtype: bool
        """
        return self._IsBlock

    @IsBlock.setter
    def IsBlock(self, IsBlock):
        self._IsBlock = IsBlock

    @property
    def IsBlockTime(self):
        r"""Blocking or unblocking time
        :rtype: str
        """
        return self._IsBlockTime

    @IsBlockTime.setter
    def IsBlockTime(self, IsBlockTime):
        self._IsBlockTime = IsBlockTime

    @property
    def LocalBgp(self):
        r"""Whether the IP type is Local BGP
        :rtype: bool
        """
        return self._LocalBgp

    @LocalBgp.setter
    def LocalBgp(self, LocalBgp):
        self._LocalBgp = LocalBgp

    @property
    def ClusterTag(self):
        r"""Layer-7 exclusive tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterTag

    @ClusterTag.setter
    def ClusterTag(self, ClusterTag):
        self._ClusterTag = ClusterTag

    @property
    def MixIpTarget(self):
        r"""If the layer-7 listener of an IPv6FullChain CLB instance is enabled, the CLB instance can be bound with IPv4 and IPv6 CVM instances simultaneously.
        :rtype: bool
        """
        return self._MixIpTarget

    @MixIpTarget.setter
    def MixIpTarget(self, MixIpTarget):
        self._MixIpTarget = MixIpTarget

    @property
    def Zones(self):
        r"""VPC-based private network CLB. AZ where the rule is in proximity access mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NfvInfo(self):
        r"""Whether CLB is NFV. Empty: No; l7nfv: NFV for layer 7.
        :rtype: str
        """
        return self._NfvInfo

    @NfvInfo.setter
    def NfvInfo(self, NfvInfo):
        self._NfvInfo = NfvInfo

    @property
    def HealthLogSetId(self):
        r"""Health check log set ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._HealthLogSetId

    @HealthLogSetId.setter
    def HealthLogSetId(self, HealthLogSetId):
        self._HealthLogSetId = HealthLogSetId

    @property
    def HealthLogTopicId(self):
        r"""Health check log topic ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._HealthLogTopicId

    @HealthLogTopicId.setter
    def HealthLogTopicId(self, HealthLogTopicId):
        self._HealthLogTopicId = HealthLogTopicId

    @property
    def ClusterIds(self):
        r"""Cluster ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def AttributeFlags(self):
        r"""Attributes of Cloud Load Balancer
        :rtype: list of str
        """
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags

    @property
    def LoadBalancerDomain(self):
        r"""Domain name of the CLB instance.
        :rtype: str
        """
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        r"""Network outbound
        :rtype: str
        """
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress

    @property
    def Exclusive(self):
        r"""Whether the instance type is exclusive type. 1: Dedicated instance. 0: Non-dedicated instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def TargetCount(self):
        r"""Number of bound backend services.
        :rtype: int
        """
        return self._TargetCount

    @TargetCount.setter
    def TargetCount(self, TargetCount):
        self._TargetCount = TargetCount

    @property
    def AssociateEndpoint(self):
        r"""Endpoint Id associated with the CLB instance.
        :rtype: str
        """
        return self._AssociateEndpoint

    @AssociateEndpoint.setter
    def AssociateEndpoint(self, AssociateEndpoint):
        self._AssociateEndpoint = AssociateEndpoint

    @property
    def AvailableZoneAffinityInfo(self):
        r"""Availability zone forward affinity info
        :rtype: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
        """
        return self._AvailableZoneAffinityInfo

    @AvailableZoneAffinityInfo.setter
    def AvailableZoneAffinityInfo(self, AvailableZoneAffinityInfo):
        self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo


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
        self._Exclusive = params.get("Exclusive")
        self._TargetCount = params.get("TargetCount")
        self._AssociateEndpoint = params.get("AssociateEndpoint")
        if params.get("AvailableZoneAffinityInfo") is not None:
            self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo()
            self._AvailableZoneAffinityInfo._deserialize(params.get("AvailableZoneAffinityInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    r"""CLB detailed information

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerType: Network type of the CLB instance:
OPEN: public network attribute, INTERNAL: private network attribute. For a Cloud Load Balancer with private network attribute, you can bind EIP for outbound public network access. For details, see the EIP document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param _Status: CLB instance state, including
0: creating, 1: normal operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Address: VIP of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _AddressIPv6: IPv6 address of the VIP in the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        :param _AddressIPVersion: IP version of the Cloud Load Balancer instance, IPv4 | IPv6.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIPVersion: str
        :param _IPv6Mode: IPv6 address type of the Cloud Load Balancer instance: IPv6Nat64 | IPv6FullChain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IPv6Mode: str
        :param _Zone: Availability Zone of the Cloud Load Balancer instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _AddressIsp: The ISP to which the IP address of the CLB instance belongs. Value ranges from BGP (multi-line), CMCC (China Mobile), CUCC (China Unicom), CTCC (China Telecom) to INTERNAL (private network).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressIsp: str
        :param _VpcId: ID of the VPC that the CLB instance belongs to.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _ProjectId: The ID of the project to which the CLB instance belongs. 0: Default project.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _CreateTime: CLB instance creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ChargeType: Billing type of the CLB instance. Valid values: PREPAID and POSTPAID_BY_HOUR (pay-as-you-go).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _NetworkAttributes: Network properties of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        :param _PrepaidAttributes: Prepaid billing attributes of the Cloud Load Balancer instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        :param _ExtraInfo: Reserved. Generally unnecessary for users to concern.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraInfo: :class:`tencentcloud.clb.v20230417.models.ExtraInfo`
        :param _ConfigId: Personalized configuration ID of the Cloud Load Balancer (CLB) dimension. Multiple configurations are separated by commas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigId: str
        :param _Tags: Tag information of the GWLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param _ListenerId: CLB listener ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Protocol: Listener protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Listener port.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _LocationId: Forwarding rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: Path of forwarding rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _TargetId: Backend target ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetId: str
        :param _TargetAddress: Backend target IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetAddress: str
        :param _TargetPort: Backend target listening port.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetPort: int
        :param _TargetWeight: Backend target forwarding weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetWeight: int
        :param _Isolation: 0: Not isolated; 1: Isolated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Isolation: int
        :param _SecurityGroup: List of security groups bound to Cloud Load Balancer (CLB).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityGroup: list of str
        :param _LoadBalancerPassToTarget: Valid values: 1 (enabled), 0 (not enabled). Value ranges from 1 to 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: int
        :param _TargetHealth: Backend target health status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetHealth: str
        :param _Domains: Domain name list of the forwarding rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domains: str
        :param _SlaveZone: Multi-availability zone Cloud Load Balancer instance selected backup availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveZone: list of str
        :param _Zones: The availability zone of the private network CLB instance is controlled by the allowlist CLB_Internal_Zone.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _SniSwitch: Whether to enable the SNI feature. 1: enable; 0: disable (this parameter is applicable only to HTTPS listeners).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SniSwitch: int
        :param _LoadBalancerDomain: Domain name of the CLB instance.
        :type LoadBalancerDomain: str
        :param _Egress: Network outbound
        :type Egress: str
        :param _AttributeFlags: Attributes of Cloud Load Balancer
        :type AttributeFlags: list of str
        :param _SlaType: Specification type information of Cloud Load Balancer instance<ul><li> clb.c1.small: Minimalist specification </li><li>clb.c2.medium: Standard specification </li><li> clb.c3.small: Advanced type 1 specification </li><li> clb.c3.medium: Advanced type 2 specification </li><li> clb.c4.small: Super type 1 specification </li><li> clb.c4.medium: Super type 2 specification </li><li> clb.c4.large: Super type 3 specification </li><li> clb.c4.xlarge: Super type 4 specification </li><li>\"\": Non-LCU-supported instance</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaType: str
        :param _Exclusive: 0: Non-exclusive type instance; 1: Exclusive type instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Exclusive: int
        :param _AvailableZoneAffinityInfo: Availability zone forward affinity info
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableZoneAffinityInfo: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
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
        self._AttributeFlags = None
        self._SlaType = None
        self._Exclusive = None
        self._AvailableZoneAffinityInfo = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""CLB instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        r"""Network type of the CLB instance:
OPEN: public network attribute, INTERNAL: private network attribute. For a Cloud Load Balancer with private network attribute, you can bind EIP for outbound public network access. For details, see the EIP document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Status(self):
        r"""CLB instance state, including
0: creating, 1: normal operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        r"""VIP of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AddressIPv6(self):
        r"""IPv6 address of the VIP in the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6

    @property
    def AddressIPVersion(self):
        r"""IP version of the Cloud Load Balancer instance, IPv4 | IPv6.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def IPv6Mode(self):
        r"""IPv6 address type of the Cloud Load Balancer instance: IPv6Nat64 | IPv6FullChain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IPv6Mode

    @IPv6Mode.setter
    def IPv6Mode(self, IPv6Mode):
        self._IPv6Mode = IPv6Mode

    @property
    def Zone(self):
        r"""Availability Zone of the Cloud Load Balancer instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AddressIsp(self):
        r"""The ISP to which the IP address of the CLB instance belongs. Value ranges from BGP (multi-line), CMCC (China Mobile), CUCC (China Unicom), CTCC (China Telecom) to INTERNAL (private network).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressIsp

    @AddressIsp.setter
    def AddressIsp(self, AddressIsp):
        self._AddressIsp = AddressIsp

    @property
    def VpcId(self):
        r"""ID of the VPC that the CLB instance belongs to.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ProjectId(self):
        r"""The ID of the project to which the CLB instance belongs. 0: Default project.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""CLB instance creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChargeType(self):
        r"""Billing type of the CLB instance. Valid values: PREPAID and POSTPAID_BY_HOUR (pay-as-you-go).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def NetworkAttributes(self):
        r"""Network properties of the CLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.InternetAccessible`
        """
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def PrepaidAttributes(self):
        r"""Prepaid billing attributes of the Cloud Load Balancer instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.LBChargePrepaid`
        """
        return self._PrepaidAttributes

    @PrepaidAttributes.setter
    def PrepaidAttributes(self, PrepaidAttributes):
        self._PrepaidAttributes = PrepaidAttributes

    @property
    def ExtraInfo(self):
        r"""Reserved. Generally unnecessary for users to concern.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def ConfigId(self):
        r"""Personalized configuration ID of the Cloud Load Balancer (CLB) dimension. Multiple configurations are separated by commas.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Tags(self):
        r"""Tag information of the GWLB instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ListenerId(self):
        r"""CLB listener ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        r"""Listener protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""Listener port.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def LocationId(self):
        r"""Forwarding rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        r"""Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        r"""Path of forwarding rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TargetId(self):
        r"""Backend target ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetAddress(self):
        r"""Backend target IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def TargetPort(self):
        r"""Backend target listening port.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def TargetWeight(self):
        r"""Backend target forwarding weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetWeight

    @TargetWeight.setter
    def TargetWeight(self, TargetWeight):
        self._TargetWeight = TargetWeight

    @property
    def Isolation(self):
        r"""0: Not isolated; 1: Isolated.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def SecurityGroup(self):
        r"""List of security groups bound to Cloud Load Balancer (CLB).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def LoadBalancerPassToTarget(self):
        r"""Valid values: 1 (enabled), 0 (not enabled). Value ranges from 1 to 0.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def TargetHealth(self):
        r"""Backend target health status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetHealth

    @TargetHealth.setter
    def TargetHealth(self, TargetHealth):
        self._TargetHealth = TargetHealth

    @property
    def Domains(self):
        r"""Domain name list of the forwarding rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def SlaveZone(self):
        r"""Multi-availability zone Cloud Load Balancer instance selected backup availability zone
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def Zones(self):
        r"""The availability zone of the private network CLB instance is controlled by the allowlist CLB_Internal_Zone.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SniSwitch(self):
        r"""Whether to enable the SNI feature. 1: enable; 0: disable (this parameter is applicable only to HTTPS listeners).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def LoadBalancerDomain(self):
        r"""Domain name of the CLB instance.
        :rtype: str
        """
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain

    @property
    def Egress(self):
        r"""Network outbound
        :rtype: str
        """
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress

    @property
    def AttributeFlags(self):
        r"""Attributes of Cloud Load Balancer
        :rtype: list of str
        """
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags

    @property
    def SlaType(self):
        r"""Specification type information of Cloud Load Balancer instance<ul><li> clb.c1.small: Minimalist specification </li><li>clb.c2.medium: Standard specification </li><li> clb.c3.small: Advanced type 1 specification </li><li> clb.c3.medium: Advanced type 2 specification </li><li> clb.c4.small: Super type 1 specification </li><li> clb.c4.medium: Super type 2 specification </li><li> clb.c4.large: Super type 3 specification </li><li> clb.c4.xlarge: Super type 4 specification </li><li>\"\": Non-LCU-supported instance</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def Exclusive(self):
        r"""0: Non-exclusive type instance; 1: Exclusive type instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def AvailableZoneAffinityInfo(self):
        r"""Availability zone forward affinity info
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.clb.v20230417.models.AvailableZoneAffinityInfo`
        """
        return self._AvailableZoneAffinityInfo

    @AvailableZoneAffinityInfo.setter
    def AvailableZoneAffinityInfo(self, AvailableZoneAffinityInfo):
        self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo


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
        self._AttributeFlags = params.get("AttributeFlags")
        self._SlaType = params.get("SlaType")
        self._Exclusive = params.get("Exclusive")
        if params.get("AvailableZoneAffinityInfo") is not None:
            self._AvailableZoneAffinityInfo = AvailableZoneAffinityInfo()
            self._AvailableZoneAffinityInfo._deserialize(params.get("AvailableZoneAffinityInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    r"""CLB instance health check status

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: Load balancing instance name
        :type LoadBalancerName: str
        :param _Listeners: Listener list
        :type Listeners: list of ListenerHealth
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""Load balancing instance name
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        r"""Listener list
        :rtype: list of ListenerHealth
        """
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
        


class RsWeightRule(AbstractModel):
    r"""Modify the data type of a node weight

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID.
        :type ListenerId: str
        :param _Targets: List of real servers for which weights are to be modified.
        :type Targets: list of Target
        :param _LocationId: Forwarding rule ID, which is required only for Layer-7 rules but not for Layer-4 rules.
        :type LocationId: str
        :param _Domain: Domain name of the target rule. This parameter will not take effect when LocationId parameter is provided.
        :type Domain: str
        :param _Url: URL of the target rule. This parameter will not take effect when the LocationId parameter is provided.
        :type Url: str
        :param _Weight: The forwarding weight of the backend service after modification, value ranges from 0 to 100. This parameter has a lower priority than the Weight parameter in the Target (https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#Target). The final weight value is determined by the Weight parameter in the Target, and only when the Weight parameter in the Target is empty, the Weight parameter in the RsWeightRule takes effect.
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
        r"""CLB listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        r"""List of real servers for which weights are to be modified.
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def LocationId(self):
        r"""Forwarding rule ID, which is required only for Layer-7 rules but not for Layer-4 rules.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        r"""Domain name of the target rule. This parameter will not take effect when LocationId parameter is provided.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        r"""URL of the target rule. This parameter will not take effect when the LocationId parameter is provided.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Weight(self):
        r"""The forwarding weight of the backend service after modification, value ranges from 0 to 100. This parameter has a lower priority than the Weight parameter in the Target (https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#Target). The final weight value is determined by the Weight parameter in the Target, and only when the Weight parameter in the Target is empty, the Weight parameter in the RsWeightRule takes effect.
        :rtype: int
        """
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
    r"""Health check status of a forwarding rule

    """

    def __init__(self):
        r"""
        :param _LocationId: Forwarding rule ID.
        :type LocationId: str
        :param _Domain: Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Url: URL of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _RuleId: Advanced routing rule ID
        :type RuleId: str
        :param _Targets: Health check status of the backend service bound to this rule
        :type Targets: list of TargetHealth
        """
        self._LocationId = None
        self._Domain = None
        self._Url = None
        self._RuleId = None
        self._Targets = None

    @property
    def LocationId(self):
        r"""Forwarding rule ID.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        r"""Domain name of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        r"""URL of the forwarding rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RuleId(self):
        r"""Advanced routing rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Targets(self):
        r"""Health check status of the backend service bound to this rule
        :rtype: list of TargetHealth
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._RuleId = params.get("RuleId")
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
        


class SetCustomizedConfigForLoadBalancerRequest(AbstractModel):
    r"""SetCustomizedConfigForLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _OperationType: Operation type.
-ADD
- DELETE: delete.
-UPDATE: Modify
-BIND: bind
-UNBIND: unbound
        :type OperationType: str
        :param _ConfigId: This field is required except for creating custom configurations. Example: pz-1234abcd
        :type ConfigId: str
        :param _ConfigContent: Personalized configuration content. This field is required when creating custom configuration or modifying the content of custom configuration.
        :type ConfigContent: str
        :param _ConfigName: This field is required when you create or modify the name of a custom configuration.
        :type ConfigName: str
        :param _LoadBalancerIds: Load balancing instance ID. This field is required for bind/unbind.
        :type LoadBalancerIds: list of str
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        """
        self._OperationType = None
        self._ConfigId = None
        self._ConfigContent = None
        self._ConfigName = None
        self._LoadBalancerIds = None
        self._Tags = None

    @property
    def OperationType(self):
        r"""Operation type.
-ADD
- DELETE: delete.
-UPDATE: Modify
-BIND: bind
-UNBIND: unbound
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def ConfigId(self):
        r"""This field is required except for creating custom configurations. Example: pz-1234abcd
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def ConfigContent(self):
        r"""Personalized configuration content. This field is required when creating custom configuration or modifying the content of custom configuration.
        :rtype: str
        """
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def ConfigName(self):
        r"""This field is required when you create or modify the name of a custom configuration.
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def LoadBalancerIds(self):
        r"""Load balancing instance ID. This field is required for bind/unbind.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._OperationType = params.get("OperationType")
        self._ConfigId = params.get("ConfigId")
        self._ConfigContent = params.get("ConfigContent")
        self._ConfigName = params.get("ConfigName")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCustomizedConfigForLoadBalancerResponse(AbstractModel):
    r"""SetCustomizedConfigForLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Custom configuration ID, such as pz-1234abcd
        :type ConfigId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        r"""Custom configuration ID, such as pz-1234abcd
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class SnatIp(AbstractModel):
    r"""SnatIp information structure

    """

    def __init__(self):
        r"""
        :param _SubnetId: Unique ID of the VPC subnet, such as subnet-12345678
        :type SubnetId: str
        :param _Ip: IP address, such as 192.168.0.1
        :type Ip: str
        """
        self._SubnetId = None
        self._Ip = None

    @property
    def SubnetId(self):
        r"""Unique ID of the VPC subnet, such as subnet-12345678
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Ip(self):
        r"""IP address, such as 192.168.0.1
        :rtype: str
        """
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
        


class TagInfo(AbstractModel):
    r"""CLB tag information

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
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
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
        


class Target(AbstractModel):
    r"""Forwarding target, namely, a real server bound to the CLB instance

    """

    def __init__(self):
        r"""
        :param _Port: Listening port of the backend service.
Note: This parameter must be specified when binding to CVM (Cloud Virtual Machine) or ENI (Elastic Network Interface).
        :type Port: int
        :param _Type: Backend service type, optional: CVM (Cloud Virtual Machine), ENI (Elastic Network Interface). As an input parameter, this parameter does not take effect.
        :type Type: str
        :param _InstanceId: This parameter must be passed in when binding to CVM. It represents the unique ID of the CVM and can be obtained from the InstanceId field in the response of the DescribeInstances API. It indicates binding to the primary IPv4 address of the primary network interface. The following scenarios do not support specifying InstanceId: binding to non-CVM resources, binding to auxiliary network interface IPs on CVM, binding to CVM through cross-region 2.0, and binding to IPv6 addresses of CVM.
Note: You can only input one of the InstanceId or EniIp parameter.
        :type InstanceId: str
        :param _Weight: The forwarding weight of the backend service after modification, with a value range of [0, 100], defaults to 10. This parameter has a higher priority than the Weight parameter in [RsWeightRule](https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#RsWeightRule). The final weight value is based on this Weight parameter. Only when this Weight parameter is empty, the Weight parameter in RsWeightRule will be used.
        :type Weight: int
        :param _EniIp: This parameter must be passed in for IP binding. It supports ENI IPs and other private IP addresses. If it is an ENI, it must first bind to a CVM before binding to a CLB instance.
Note: You can only input one of the InstanceId or EniIp parameter. If it is binding a dual-stack IPV6 instance, you must pass this parameter. If it is cross-region binding, you must pass the parameter, and the InstanceId parameter is not supported.
        :type EniIp: str
        """
        self._Port = None
        self._Type = None
        self._InstanceId = None
        self._Weight = None
        self._EniIp = None

    @property
    def Port(self):
        r"""Listening port of the backend service.
Note: This parameter must be specified when binding to CVM (Cloud Virtual Machine) or ENI (Elastic Network Interface).
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Type(self):
        r"""Backend service type, optional: CVM (Cloud Virtual Machine), ENI (Elastic Network Interface). As an input parameter, this parameter does not take effect.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        r"""This parameter must be passed in when binding to CVM. It represents the unique ID of the CVM and can be obtained from the InstanceId field in the response of the DescribeInstances API. It indicates binding to the primary IPv4 address of the primary network interface. The following scenarios do not support specifying InstanceId: binding to non-CVM resources, binding to auxiliary network interface IPs on CVM, binding to CVM through cross-region 2.0, and binding to IPv6 addresses of CVM.
Note: You can only input one of the InstanceId or EniIp parameter.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        r"""The forwarding weight of the backend service after modification, with a value range of [0, 100], defaults to 10. This parameter has a higher priority than the Weight parameter in [RsWeightRule](https://www.tencentcloud.com/document/api/214/30694?from_cn_redirect=1#RsWeightRule). The final weight value is based on this Weight parameter. Only when this Weight parameter is empty, the Weight parameter in RsWeightRule will be used.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EniIp(self):
        r"""This parameter must be passed in for IP binding. It supports ENI IPs and other private IP addresses. If it is an ENI, it must first bind to a CVM before binding to a CLB instance.
Note: You can only input one of the InstanceId or EniIp parameter. If it is binding a dual-stack IPV6 instance, you must pass this parameter. If it is cross-region binding, you must pass the parameter, and the InstanceId parameter is not supported.
        :rtype: str
        """
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
        


class TargetHealth(AbstractModel):
    r"""Describes the health information of a target

    """

    def __init__(self):
        r"""
        :param _IP: Private network IP of target
        :type IP: str
        :param _Port: Port bound to the target
        :type Port: int
        :param _HealthStatus: Detailed information of the current health status. For example: Alive, Dead, Unknown, Close. Alive status is healthy, Dead state is abnormal, Unknown status includes not started, checking, unknown status, Close means health check disabled or listener status stop.
        :type HealthStatus: bool
        :param _TargetId: Target instance ID, such as ins-12345678
        :type TargetId: str
        :param _HealthStatusDetail: Detailed information about the current health status. Alive: Healthy; Dead: Exceptional; Unknown: Check not started/Checking/Unknown status.
        :type HealthStatusDetail: str
        :param _TargetGroupId: Target group unique ID.
        :type TargetGroupId: str
        :param _Weight: Weight of the Target
        :type Weight: int
        """
        self._IP = None
        self._Port = None
        self._HealthStatus = None
        self._TargetId = None
        self._HealthStatusDetail = None
        self._TargetGroupId = None
        self._Weight = None

    @property
    def IP(self):
        r"""Private network IP of target
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        r"""Port bound to the target
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthStatus(self):
        r"""Detailed information of the current health status. For example: Alive, Dead, Unknown, Close. Alive status is healthy, Dead state is abnormal, Unknown status includes not started, checking, unknown status, Close means health check disabled or listener status stop.
        :rtype: bool
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def TargetId(self):
        r"""Target instance ID, such as ins-12345678
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def HealthStatusDetail(self):
        r"""Detailed information about the current health status. Alive: Healthy; Dead: Exceptional; Unknown: Check not started/Checking/Unknown status.
        :rtype: str
        """
        return self._HealthStatusDetail

    @HealthStatusDetail.setter
    def HealthStatusDetail(self, HealthStatusDetail):
        self._HealthStatusDetail = HealthStatusDetail

    @property
    def TargetGroupId(self):
        r"""Target group unique ID.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Weight(self):
        r"""Weight of the Target
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._HealthStatus = params.get("HealthStatus")
        self._TargetId = params.get("TargetId")
        self._HealthStatusDetail = params.get("HealthStatusDetail")
        self._TargetGroupId = params.get("TargetGroupId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetRegionInfo(AbstractModel):
    r"""Information of the real server bound to a CLB instance, including region and network to which it belongs.

    """

    def __init__(self):
        r"""
        :param _Region: Region of the target, such as ap-guangzhou
        :type Region: str
        :param _VpcId: Network of the target. For VPC, the format is vpc-abcd1234. For a basic network, the value is 0.
        :type VpcId: str
        :param _NumericalVpcId: Target's network, in the format of 86323 for a private network, or 0 if it is a basic network
        :type NumericalVpcId: int
        """
        self._Region = None
        self._VpcId = None
        self._NumericalVpcId = None

    @property
    def Region(self):
        r"""Region of the target, such as ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""Network of the target. For VPC, the format is vpc-abcd1234. For a basic network, the value is 0.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def NumericalVpcId(self):
        r"""Target's network, in the format of 86323 for a private network, or 0 if it is a basic network
        :rtype: int
        """
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._NumericalVpcId = params.get("NumericalVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    r"""AZ information

    """

    def __init__(self):
        r"""
        :param _ZoneId: Unique ID of the AZ in numeric form, such as 100001
        :type ZoneId: int
        :param _Zone: Unique ID of the AZ in string format, such as ap-guangzhou-1
        :type Zone: str
        :param _ZoneName: AZ name, such as Guangzhou 1
        :type ZoneName: str
        :param _ZoneRegion: Region of the availability zone, such as ap-guangzhou.
        :type ZoneRegion: str
        :param _LocalZone: Whether the availability zone is a local availability zone. For example, false.
        :type LocalZone: bool
        :param _EdgeZone: Whether the availability zone is an edge availability zone. For example, false.
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
        r"""Unique ID of the AZ in numeric form, such as 100001
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        r"""Unique ID of the AZ in string format, such as ap-guangzhou-1
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""AZ name, such as Guangzhou 1
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneRegion(self):
        r"""Region of the availability zone, such as ap-guangzhou.
        :rtype: str
        """
        return self._ZoneRegion

    @ZoneRegion.setter
    def ZoneRegion(self, ZoneRegion):
        self._ZoneRegion = ZoneRegion

    @property
    def LocalZone(self):
        r"""Whether the availability zone is a local availability zone. For example, false.
        :rtype: bool
        """
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def EdgeZone(self):
        r"""Whether the availability zone is an edge availability zone. For example, false.
        :rtype: bool
        """
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
        