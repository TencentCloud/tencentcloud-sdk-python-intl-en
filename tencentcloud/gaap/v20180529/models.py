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


class AccessConfiguration(AbstractModel):
    """List of acceleration regions in a connection group, including acceleration regions and their bandwidth and concurrence configuration.

    """

    def __init__(self):
        r"""
        :param _AccessRegion: Acceleration region.
        :type AccessRegion: str
        :param _Bandwidth: Connection bandwidth cap. Unit: Mbps.
        :type Bandwidth: int
        :param _Concurrent: Connection concurrence cap, which indicates the maximum number of simultaneous online connections. Unit: 10,000 connections.
        :type Concurrent: int
        :param _NetworkType: Network type. Valid values: `normal` (default), `cn2`
        :type NetworkType: str
        """
        self._AccessRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._NetworkType = None

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._NetworkType = params.get("NetworkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDetial(AbstractModel):
    """Query the available acceleration region information, the corresponding bandwidth options, and the concurrence based on origin servers.

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name in Chinese or English
        :type RegionName: str
        :param _ConcurrentList: Value array of the available concurrence
        :type ConcurrentList: list of int
        :param _BandwidthList: Value array of the available bandwidth
        :type BandwidthList: list of int
        :param _RegionArea: Region where the data center locates
        :type RegionArea: str
        :param _RegionAreaName: Name of the region where the data center locates
        :type RegionAreaName: str
        :param _IDCType: Data center type. `dc`: data center; `ec`: edge server.
        :type IDCType: str
        :param _FeatureBitmap: Feature bitmap. Valid values:
`0`: disable the feature;
`1`: enable the feature.
Each bit in the bitmap represents a feature:
1st bit: layer-4 acceleration;
2nd bit: layer-7 acceleration;
3rd bit: HTTP3 access;
4th bit: IPv6;
5th bit: dedicated BGP access;
6th bit: non-BGP access;
7th bit: QoS acceleration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FeatureBitmap: int
        """
        self._RegionId = None
        self._RegionName = None
        self._ConcurrentList = None
        self._BandwidthList = None
        self._RegionArea = None
        self._RegionAreaName = None
        self._IDCType = None
        self._FeatureBitmap = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ConcurrentList(self):
        return self._ConcurrentList

    @ConcurrentList.setter
    def ConcurrentList(self, ConcurrentList):
        self._ConcurrentList = ConcurrentList

    @property
    def BandwidthList(self):
        return self._BandwidthList

    @BandwidthList.setter
    def BandwidthList(self, BandwidthList):
        self._BandwidthList = BandwidthList

    @property
    def RegionArea(self):
        return self._RegionArea

    @RegionArea.setter
    def RegionArea(self, RegionArea):
        self._RegionArea = RegionArea

    @property
    def RegionAreaName(self):
        return self._RegionAreaName

    @RegionAreaName.setter
    def RegionAreaName(self, RegionAreaName):
        self._RegionAreaName = RegionAreaName

    @property
    def IDCType(self):
        return self._IDCType

    @IDCType.setter
    def IDCType(self, IDCType):
        self._IDCType = IDCType

    @property
    def FeatureBitmap(self):
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ConcurrentList = params.get("ConcurrentList")
        self._BandwidthList = params.get("BandwidthList")
        self._RegionArea = params.get("RegionArea")
        self._RegionAreaName = params.get("RegionAreaName")
        self._IDCType = params.get("IDCType")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDomainConf(AbstractModel):
    """Domain name nearest access configuration

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID.
        :type RegionId: str
        :param _NationCountryInnerList: Region/country code for the nearest access, which can be obtained via the DescribeCountryAreaMapping API.
        :type NationCountryInnerList: list of str
        """
        self._RegionId = None
        self._NationCountryInnerList = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def NationCountryInnerList(self):
        return self._NationCountryInnerList

    @NationCountryInnerList.setter
    def NationCountryInnerList(self, NationCountryInnerList):
        self._NationCountryInnerList = NationCountryInnerList


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._NationCountryInnerList = params.get("NationCountryInnerList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersRequest(AbstractModel):
    """AddRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID corresponding to origin server
        :type ProjectId: int
        :param _RealServerIP: IP or domain name corresponding to origin server
        :type RealServerIP: list of str
        :param _RealServerName: Name of the origin server
        :type RealServerName: str
        :param _TagSet: List of tags
        :type TagSet: list of TagPair
        """
        self._ProjectId = None
        self._RealServerIP = None
        self._RealServerName = None
        self._TagSet = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerName(self):
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerName = params.get("RealServerName")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersResponse(AbstractModel):
    """AddRealServers response structure.

    """

    def __init__(self):
        r"""
        :param _RealServerSet: An information list of origin server
        :type RealServerSet: list of NewRealServer
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RealServerSet = None
        self._RequestId = None

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = NewRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class BandwidthPriceGradient(AbstractModel):
    """Bandwidth price gradient

    """

    def __init__(self):
        r"""
        :param _BandwidthRange: Bandwidth range.
        :type BandwidthRange: list of int
        :param _BandwidthUnitPrice: Bandwidth unit price within the bandwidth range. Unit: CNY/Mbps/day.
        :type BandwidthUnitPrice: float
        :param _DiscountBandwidthUnitPrice: Discounted bandwidth price in CNY/Mbps/day.
        :type DiscountBandwidthUnitPrice: float
        """
        self._BandwidthRange = None
        self._BandwidthUnitPrice = None
        self._DiscountBandwidthUnitPrice = None

    @property
    def BandwidthRange(self):
        return self._BandwidthRange

    @BandwidthRange.setter
    def BandwidthRange(self, BandwidthRange):
        self._BandwidthRange = BandwidthRange

    @property
    def BandwidthUnitPrice(self):
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def DiscountBandwidthUnitPrice(self):
        return self._DiscountBandwidthUnitPrice

    @DiscountBandwidthUnitPrice.setter
    def DiscountBandwidthUnitPrice(self, DiscountBandwidthUnitPrice):
        self._DiscountBandwidthUnitPrice = DiscountBandwidthUnitPrice


    def _deserialize(self, params):
        self._BandwidthRange = params.get("BandwidthRange")
        self._BandwidthUnitPrice = params.get("BandwidthUnitPrice")
        self._DiscountBandwidthUnitPrice = params.get("DiscountBandwidthUnitPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersRequest(AbstractModel):
    """BindListenerRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _RealServerBindSet: List of origin servers to be bound. If the origin server scheduling policy type of this listener is weighted round robin, you need to enter the `RealServerWeight`, i.e., the origin server weight. If this field is left empty or for other scheduling types, the default origin server weight is 1.
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self._ListenerId = None
        self._RealServerBindSet = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RealServerBindSet(self):
        return self._RealServerBindSet

    @RealServerBindSet.setter
    def RealServerBindSet(self, RealServerBindSet):
        self._RealServerBindSet = RealServerBindSet


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("RealServerBindSet") is not None:
            self._RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self._RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersResponse(AbstractModel):
    """BindListenerRealServers response structure.

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


class BindRealServer(AbstractModel):
    """Bound origin server information

    """

    def __init__(self):
        r"""
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _RealServerIP: Origin server IP or domain name
        :type RealServerIP: str
        :param _RealServerWeight: Origin server weight
        :type RealServerWeight: int
        :param _RealServerStatus: Origin server health check status. Valid values:
0: normal;
1: exceptional.
If health check is not enabled, this status will always be normal.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RealServerStatus: int
        :param _RealServerPort: Origin server port number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerPort: int
        :param _DownIPList: If the origin server is a domain name, the domain name will be resolved to one or multiple IPs. This field indicates the exceptional IP list.
        :type DownIPList: list of str
        :param _RealServerFailoverRole: Role of the origin server. Values: `master` (primary origin server); `slave` (secondary origin server). This parameter only takes effect when origin failover is enabled for the listener.
        :type RealServerFailoverRole: str
        """
        self._RealServerId = None
        self._RealServerIP = None
        self._RealServerWeight = None
        self._RealServerStatus = None
        self._RealServerPort = None
        self._DownIPList = None
        self._RealServerFailoverRole = None

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerWeight(self):
        return self._RealServerWeight

    @RealServerWeight.setter
    def RealServerWeight(self, RealServerWeight):
        self._RealServerWeight = RealServerWeight

    @property
    def RealServerStatus(self):
        return self._RealServerStatus

    @RealServerStatus.setter
    def RealServerStatus(self, RealServerStatus):
        self._RealServerStatus = RealServerStatus

    @property
    def RealServerPort(self):
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def DownIPList(self):
        return self._DownIPList

    @DownIPList.setter
    def DownIPList(self, DownIPList):
        self._DownIPList = DownIPList

    @property
    def RealServerFailoverRole(self):
        return self._RealServerFailoverRole

    @RealServerFailoverRole.setter
    def RealServerFailoverRole(self, RealServerFailoverRole):
        self._RealServerFailoverRole = RealServerFailoverRole


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerWeight = params.get("RealServerWeight")
        self._RealServerStatus = params.get("RealServerStatus")
        self._RealServerPort = params.get("RealServerPort")
        self._DownIPList = params.get("DownIPList")
        self._RealServerFailoverRole = params.get("RealServerFailoverRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRealServerInfo(AbstractModel):
    """The returned value of the added origin server information

    """

    def __init__(self):
        r"""
        :param _RealServerIP: Origin server IP or domain name
        :type RealServerIP: str
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _RealServerName: Origin server name
        :type RealServerName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _TagSet: Tag list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of TagPair
        """
        self._RealServerIP = None
        self._RealServerId = None
        self._RealServerName = None
        self._ProjectId = None
        self._TagSet = None

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerName(self):
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerId = params.get("RealServerId")
        self._RealServerName = params.get("RealServerName")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersRequest(AbstractModel):
    """BindRuleRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID
        :type RuleId: str
        :param _RealServerBindSet: An information list of the origin servers to bind.
If there are origin servers bound already, they will be replaced by this new origin server list.
If this field is empty, it indicates unbinding all origin servers of this rule.
If the origin server scheduling policy type of this rule is weighted round robin, you need to enter `RealServerWeight`, i.e., the origin server weight. If this field is left empty or for other scheduling types, the default origin server weight is 1.
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self._RuleId = None
        self._RealServerBindSet = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RealServerBindSet(self):
        return self._RealServerBindSet

    @RealServerBindSet.setter
    def RealServerBindSet(self, RealServerBindSet):
        self._RealServerBindSet = RealServerBindSet


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("RealServerBindSet") is not None:
            self._RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self._RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersResponse(AbstractModel):
    """BindRuleRealServers response structure.

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


class Certificate(AbstractModel):
    """Server Certificate

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _CertificateName: Certificate name; It's an old parameter, please switch to CertificateAlias.
        :type CertificateName: str
        :param _CertificateType: Certificate type.
        :type CertificateType: int
        :param _CertificateAlias: Certificate name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateAlias: str
        :param _CreateTime: Certificate creation time in the format of UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
        :type CreateTime: int
        :param _BeginTime: Certificate effective time in the format of UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeginTime: int
        :param _EndTime: Certificate expiration time in the format of UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _IssuerCN: Common name of the certificate issuer.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuerCN: str
        :param _SubjectCN: Common name of the certificate subject.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectCN: str
        """
        self._CertificateId = None
        self._CertificateName = None
        self._CertificateType = None
        self._CertificateAlias = None
        self._CreateTime = None
        self._BeginTime = None
        self._EndTime = None
        self._IssuerCN = None
        self._SubjectCN = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateName(self):
        return self._CertificateName

    @CertificateName.setter
    def CertificateName(self, CertificateName):
        self._CertificateName = CertificateName

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def IssuerCN(self):
        return self._IssuerCN

    @IssuerCN.setter
    def IssuerCN(self, IssuerCN):
        self._IssuerCN = IssuerCN

    @property
    def SubjectCN(self):
        return self._SubjectCN

    @SubjectCN.setter
    def SubjectCN(self, SubjectCN):
        self._SubjectCN = SubjectCN


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateName = params.get("CertificateName")
        self._CertificateType = params.get("CertificateType")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CreateTime = params.get("CreateTime")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._IssuerCN = params.get("IssuerCN")
        self._SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateAliasInfo(AbstractModel):
    """Certificate alias information.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID.
        :type CertificateId: str
        :param _CertificateAlias: Certificate alias.
        :type CertificateAlias: str
        """
        self._CertificateId = None
        self._CertificateAlias = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateDetail(AbstractModel):
    """Certificate details, including the certificate ID, name, type, content, and key content.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _CertificateType: Certificate type.
        :type CertificateType: int
        :param _CertificateAlias: Certificate name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateAlias: str
        :param _CertificateContent: Certificate content.
        :type CertificateContent: str
        :param _CertificateKey: Key content. This field will be returned if the certificate type is the SSL certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateKey: str
        :param _CreateTime: Creation time in the format of UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _BeginTime: Time that the certificate takes effect. Using the UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BeginTime: int
        :param _EndTime: Certificate expiration time. Using the UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _IssuerCN: Common name of the certificate’s issuer.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuerCN: str
        :param _SubjectCN: Common name of the certificate subject.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectCN: str
        """
        self._CertificateId = None
        self._CertificateType = None
        self._CertificateAlias = None
        self._CertificateContent = None
        self._CertificateKey = None
        self._CreateTime = None
        self._BeginTime = None
        self._EndTime = None
        self._IssuerCN = None
        self._SubjectCN = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CertificateContent(self):
        return self._CertificateContent

    @CertificateContent.setter
    def CertificateContent(self, CertificateContent):
        self._CertificateContent = CertificateContent

    @property
    def CertificateKey(self):
        return self._CertificateKey

    @CertificateKey.setter
    def CertificateKey(self, CertificateKey):
        self._CertificateKey = CertificateKey

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def IssuerCN(self):
        return self._IssuerCN

    @IssuerCN.setter
    def IssuerCN(self, IssuerCN):
        self._IssuerCN = IssuerCN

    @property
    def SubjectCN(self):
        return self._SubjectCN

    @SubjectCN.setter
    def SubjectCN(self, SubjectCN):
        self._SubjectCN = SubjectCN


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateType = params.get("CertificateType")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CertificateContent = params.get("CertificateContent")
        self._CertificateKey = params.get("CertificateKey")
        self._CreateTime = params.get("CreateTime")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._IssuerCN = params.get("IssuerCN")
        self._SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateRequest(AbstractModel):
    """CheckProxyCreate request structure.

    """

    def __init__(self):
        r"""
        :param _AccessRegion: Access (acceleration) region of the connection. The value can be obtained via the DescribeAccessRegionsByDestRegion API.
        :type AccessRegion: str
        :param _RealServerRegion: Origin server region of the connection. The value can be obtained via the DescribeDestRegions API.
        :type RealServerRegion: str
        :param _Bandwidth: Connection bandwidth cap. Unit: Mbps.
        :type Bandwidth: int
        :param _Concurrent: Connection concurrence cap, which indicates the maximum number of simultaneous online connections. Unit: 10,000 connections.
        :type Concurrent: int
        :param _GroupId: Connection group ID that needs to be entered when a connection is created in a connection group
        :type GroupId: str
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _NetworkType: Network type. Valid values: `normal` (default), `cn2`
        :type NetworkType: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general connection group), `Accelerator` (game accelerator connection group), and `CrossBorder` (cross-border connection group).
        :type PackageType: str
        :param _Http3Supported: (Disused) HTTP3.0 is supported by default when `IPAddressVersion` is `IPv4`.
        :type Http3Supported: int
        """
        self._AccessRegion = None
        self._RealServerRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._GroupId = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def RealServerRegion(self):
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._GroupId = params.get("GroupId")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateResponse(AbstractModel):
    """CheckProxyCreate response structure.

    """

    def __init__(self):
        r"""
        :param _CheckFlag: Queries whether a connection with the specified configuration can be created. 1: yes; 0: no.
        :type CheckFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CheckFlag = None
        self._RequestId = None

    @property
    def CheckFlag(self):
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class CloseProxiesRequest(AbstractModel):
    """CloseProxies request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Connection instance ID; It’s an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyIds: Connection instance ID; It’s a new parameter.
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxiesResponse(AbstractModel):
    """CloseProxies response structure.

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: Only the running connection instance ID lists can be enabled.
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: ID list of connection instances failed to be enabled.
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class CloseProxyGroupRequest(AbstractModel):
    """CloseProxyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group instance ID.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxyGroupResponse(AbstractModel):
    """CloseProxyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: List of IDs of the connection instances that are not running, which cannot be enabled.
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: List of IDs of the connection instances failed to be enabled.
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class CloseSecurityPolicyRequest(AbstractModel):
    """CloseSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
        :type ProxyId: str
        :param _PolicyId: Security group policy ID
        :type PolicyId: str
        """
        self._ProxyId = None
        self._PolicyId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseSecurityPolicyResponse(AbstractModel):
    """CloseSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async Process ID. Using DescribeAsyncTaskStatus to query process and status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CountryAreaMap(AbstractModel):
    """Country/region code mapping (name and code)

    """

    def __init__(self):
        r"""
        :param _NationCountryName: Country name.
        :type NationCountryName: str
        :param _NationCountryInnerCode: Country code.
        :type NationCountryInnerCode: str
        :param _GeographicalZoneName: Region name.
        :type GeographicalZoneName: str
        :param _GeographicalZoneInnerCode: Region code.
        :type GeographicalZoneInnerCode: str
        :param _ContinentName: Continent name.
        :type ContinentName: str
        :param _ContinentInnerCode: Continent code.
        :type ContinentInnerCode: str
        :param _Remark: Remark information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self._NationCountryName = None
        self._NationCountryInnerCode = None
        self._GeographicalZoneName = None
        self._GeographicalZoneInnerCode = None
        self._ContinentName = None
        self._ContinentInnerCode = None
        self._Remark = None

    @property
    def NationCountryName(self):
        return self._NationCountryName

    @NationCountryName.setter
    def NationCountryName(self, NationCountryName):
        self._NationCountryName = NationCountryName

    @property
    def NationCountryInnerCode(self):
        return self._NationCountryInnerCode

    @NationCountryInnerCode.setter
    def NationCountryInnerCode(self, NationCountryInnerCode):
        self._NationCountryInnerCode = NationCountryInnerCode

    @property
    def GeographicalZoneName(self):
        return self._GeographicalZoneName

    @GeographicalZoneName.setter
    def GeographicalZoneName(self, GeographicalZoneName):
        self._GeographicalZoneName = GeographicalZoneName

    @property
    def GeographicalZoneInnerCode(self):
        return self._GeographicalZoneInnerCode

    @GeographicalZoneInnerCode.setter
    def GeographicalZoneInnerCode(self, GeographicalZoneInnerCode):
        self._GeographicalZoneInnerCode = GeographicalZoneInnerCode

    @property
    def ContinentName(self):
        return self._ContinentName

    @ContinentName.setter
    def ContinentName(self, ContinentName):
        self._ContinentName = ContinentName

    @property
    def ContinentInnerCode(self):
        return self._ContinentInnerCode

    @ContinentInnerCode.setter
    def ContinentInnerCode(self, ContinentInnerCode):
        self._ContinentInnerCode = ContinentInnerCode

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._NationCountryName = params.get("NationCountryName")
        self._NationCountryInnerCode = params.get("NationCountryInnerCode")
        self._GeographicalZoneName = params.get("GeographicalZoneName")
        self._GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self._ContinentName = params.get("ContinentName")
        self._ContinentInnerCode = params.get("ContinentInnerCode")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateType: Certificate type. Where:
`0`: Basic authentication configuration;
`1`: Client CA certificate;
`2`: Server SSL certificate;
`3`: Origin server CA certificate;
`4`: Connection SSL certificate.
        :type CertificateType: int
        :param _CertificateContent: Certificate content. URL encoding. Where:
If the certificate type is basic authentication, enter username/password pair for this parameter. Format: “username:password”, for example, root:FSGdT. The password is `htpasswd` or `openssl`, for example, openssl passwd -crypt 123456.
When the certificate type is CA/SSL certificate, enter the certificate content for this parameter in the format of ‘pem’.
        :type CertificateContent: str
        :param _CertificateAlias: Certificate name
        :type CertificateAlias: str
        :param _CertificateKey: URL-encoded key content. This parameter is required only when the certificate type is SSL certificate. Its format is `PEM`.
        :type CertificateKey: str
        """
        self._CertificateType = None
        self._CertificateContent = None
        self._CertificateAlias = None
        self._CertificateKey = None

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateContent(self):
        return self._CertificateContent

    @CertificateContent.setter
    def CertificateContent(self, CertificateContent):
        self._CertificateContent = CertificateContent

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CertificateKey(self):
        return self._CertificateKey

    @CertificateKey.setter
    def CertificateKey(self, CertificateKey):
        self._CertificateKey = CertificateKey


    def _deserialize(self, params):
        self._CertificateType = params.get("CertificateType")
        self._CertificateContent = params.get("CertificateContent")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CertificateKey = params.get("CertificateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CreateCustomHeaderRequest(AbstractModel):
    """CreateCustomHeader request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Headers: Custom header name and content list. `‘’$remote_addr‘’` will be resolved and replaced with the client IP. Other values will be directly passed to the origin server.
        :type Headers: list of HttpHeaderParam
        """
        self._RuleId = None
        self._Headers = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomHeaderResponse(AbstractModel):
    """CreateCustomHeader response structure.

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


class CreateDomainErrorPageInfoRequest(AbstractModel):
    """CreateDomainErrorPageInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Domain: Domain name
        :type Domain: str
        :param _ErrorNos: Original error code
        :type ErrorNos: list of int
        :param _Body: New response packet
        :type Body: str
        :param _NewErrorNo: New error code
        :type NewErrorNo: int
        :param _ClearHeaders: Response header to be deleted
        :type ClearHeaders: list of str
        :param _SetHeaders: Response header to be set
        :type SetHeaders: list of HttpHeaderParam
        """
        self._ListenerId = None
        self._Domain = None
        self._ErrorNos = None
        self._Body = None
        self._NewErrorNo = None
        self._ClearHeaders = None
        self._SetHeaders = None

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
    def ErrorNos(self):
        return self._ErrorNos

    @ErrorNos.setter
    def ErrorNos(self, ErrorNos):
        self._ErrorNos = ErrorNos

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def NewErrorNo(self):
        return self._NewErrorNo

    @NewErrorNo.setter
    def NewErrorNo(self, NewErrorNo):
        self._NewErrorNo = NewErrorNo

    @property
    def ClearHeaders(self):
        return self._ClearHeaders

    @ClearHeaders.setter
    def ClearHeaders(self, ClearHeaders):
        self._ClearHeaders = ClearHeaders

    @property
    def SetHeaders(self):
        return self._SetHeaders

    @SetHeaders.setter
    def SetHeaders(self, SetHeaders):
        self._SetHeaders = SetHeaders


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._ErrorNos = params.get("ErrorNos")
        self._Body = params.get("Body")
        self._NewErrorNo = params.get("NewErrorNo")
        self._ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self._SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._SetHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainErrorPageInfoResponse(AbstractModel):
    """CreateDomainErrorPageInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: Configuration ID of a custom error response
        :type ErrorPageId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorPageId = None
        self._RequestId = None

    @property
    def ErrorPageId(self):
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorPageId = params.get("ErrorPageId")
        self._RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Domain: Domain name to be created. Each listener supports up to 100 domain names.
        :type Domain: str
        :param _CertificateId: Server certificate, which is used for the HTTPS interaction between client and GAAP.
        :type CertificateId: str
        :param _ClientCertificateId: Client CA certificate, which is used for the HTTPS interaction between client and GAAP.
This field is required only when the mutual authentication method is adopted.
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: Client CA certificate, which is used for the HTTPS interaction between the client and GAAP.
This field or the `ClientCertificateId` field is required for mutual authentication only.
        :type PolyClientCertificateIds: list of str
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: disable HTTP3;
`1`: enable HTTP3.
HTTP3 is not enabled by default. You can enable it with this field SetDomainHttp3.
        :type Http3Supported: int
        """
        self._ListenerId = None
        self._Domain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None
        self._Http3Supported = None

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
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain response structure.

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


class CreateHTTPListenerRequest(AbstractModel):
    """CreateHTTPListener request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port, which is based on the listeners of same transport layer protocol (TCP or UDP). The port must be unique.
        :type Port: int
        :param _ProxyId: Connection ID, which cannot be set together with `GroupId` at the same time. A listener will be created for the corresponding connection.
        :type ProxyId: str
        :param _GroupId: Connection group ID, which cannot be set together with `ProxyId` at the same time. A listener will be created for the corresponding connection group.
        :type GroupId: str
        """
        self._ListenerName = None
        self._Port = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPListenerResponse(AbstractModel):
    """CreateHTTPListener response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Created listener ID
        :type ListenerId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateHTTPSListenerRequest(AbstractModel):
    """CreateHTTPSListener request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port, which is based on the listeners of same transport layer protocol (TCP or UDP). The port must be unique.
        :type Port: int
        :param _CertificateId: Server certificate ID
        :type CertificateId: str
        :param _ForwardProtocol: Protocol types of the forwarding from acceleration connection to origin server: HTTP | HTTPS
        :type ForwardProtocol: str
        :param _ProxyId: Connection ID, which cannot be set together with `GroupId` at the same time. A listener will be created for the corresponding connection.
        :type ProxyId: str
        :param _AuthType: Authentication type, where:
0: one-way authentication;
1: mutual authentication.
The one-way authentication is used by default.
        :type AuthType: int
        :param _ClientCertificateId: Client CA certificate ID, which is required only when the mutual authentication is adopted.
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: IDs of multiple new client CA certificates. This field or the `ClientCertificateId` field is required for mutual authentication only.
        :type PolyClientCertificateIds: list of str
        :param _GroupId: Connection group ID, which cannot be set together with `ProxyId` at the same time. A listener will be created for the corresponding connection group.
        :type GroupId: str
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: disable HTTP3;
`1`: enable HTTP3.
Note: If HTTP3 is enabled for a connection, the listener will use the port that is originally accessed to UDP, and a UDP listener with the same port cannot be created.
After the connection is created, you cannot change your HTTP3 setting.
        :type Http3Supported: int
        """
        self._ListenerName = None
        self._Port = None
        self._CertificateId = None
        self._ForwardProtocol = None
        self._ProxyId = None
        self._AuthType = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None
        self._GroupId = None
        self._Http3Supported = None

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._CertificateId = params.get("CertificateId")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ProxyId = params.get("ProxyId")
        self._AuthType = params.get("AuthType")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self._GroupId = params.get("GroupId")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPSListenerResponse(AbstractModel):
    """CreateHTTPSListener response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Created listener ID
        :type ListenerId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateProxyGroupDomainRequest(AbstractModel):
    """CreateProxyGroupDomain request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID of the domain name to be enabled.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupDomainResponse(AbstractModel):
    """CreateProxyGroupDomain response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID.
        :type GroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyGroupRequest(AbstractModel):
    """CreateProxyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID of connection group
        :type ProjectId: int
        :param _GroupName: Alias of connection group
        :type GroupName: str
        :param _RealServerRegion: Origin server region; Reference API: DescribeDestRegions; It returnes the `RegionId` of the parameter `RegionDetail`.
        :type RealServerRegion: str
        :param _TagSet: List of tags
        :type TagSet: list of TagPair
        :param _AccessRegionSet: List of acceleration regions, including their names, bandwidth, and concurrence configuration.
        :type AccessRegionSet: list of AccessConfiguration
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _PackageType: Package type of connection group. Valid values: `Thunder` (default) and `Accelerator`.
        :type PackageType: str
        :param _Http3Supported: (Disused) HTTP3.0 is supported by default when `IPAddressVersion` is `IPv4`.
        :type Http3Supported: int
        """
        self._ProjectId = None
        self._GroupName = None
        self._RealServerRegion = None
        self._TagSet = None
        self._AccessRegionSet = None
        self._IPAddressVersion = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def RealServerRegion(self):
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AccessRegionSet(self):
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._GroupName = params.get("GroupName")
        self._RealServerRegion = params.get("RealServerRegion")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessConfiguration()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupResponse(AbstractModel):
    """CreateProxyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the connection group
        :type GroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID of connection.
        :type ProjectId: int
        :param _ProxyName: Name of the connection
        :type ProxyName: str
        :param _AccessRegion: Access region.
        :type AccessRegion: str
        :param _Bandwidth: Connection bandwidth cap. Unit: Mbps.
        :type Bandwidth: int
        :param _Concurrent: Connection concurrence cap, which indicates the maximum number of simultaneous online connections. Unit: 10,000 connections.
        :type Concurrent: int
        :param _RealServerRegion: Origin server region. If GroupId exists, the origin server region is the one of connection group, and this field is not required. If GroupId does not exist, this field is reuqired.
        :type RealServerRegion: str
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _GroupId: Connection group ID. This parameter is required when the connection is created in the connection group. Otherwise, this field is ignored.
        :type GroupId: str
        :param _TagSet: List of tags to be added for connection.
        :type TagSet: list of TagPair
        :param _ClonedProxyId: ID of the replicated connection. Only a running connection can be replicated.
The connection is to be replicated if this parameter is set.
        :type ClonedProxyId: str
        :param _BillingType: Billing mode (0: bill-by-bandwidth, 1: bill-by-traffic. Default value: bill-by-bandwidth)
        :type BillingType: int
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _NetworkType: Network type. `normal`: general BGP; `cn2`: dedicated BGP; `triple`: Non-BGP (provided by the top 3 ISPs in the Chinese mainland).
        :type NetworkType: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general), `Accelerator` (specific for games), and `CrossBorder` (cross-MLC-border connection).
        :type PackageType: str
        :param _Http3Supported: (Disused) HTTP3.0 is supported by default when `IPAddressVersion` is `IPv4`.
        :type Http3Supported: int
        """
        self._ProjectId = None
        self._ProxyName = None
        self._AccessRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._RealServerRegion = None
        self._ClientToken = None
        self._GroupId = None
        self._TagSet = None
        self._ClonedProxyId = None
        self._BillingType = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def RealServerRegion(self):
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def ClonedProxyId(self):
        return self._ClonedProxyId

    @ClonedProxyId.setter
    def ClonedProxyId(self, ClonedProxyId):
        self._ClonedProxyId = ClonedProxyId

    @property
    def BillingType(self):
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProxyName = params.get("ProxyName")
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._RealServerRegion = params.get("RealServerRegion")
        self._ClientToken = params.get("ClientToken")
        self._GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._ClonedProxyId = params.get("ClonedProxyId")
        self._BillingType = params.get("BillingType")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyResponse(AbstractModel):
    """CreateProxy response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID of connection.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Layer-7 listener ID
        :type ListenerId: str
        :param _Domain: Domain name of the forwarding rule
        :type Domain: str
        :param _Path: Path of the forwarding rule
        :type Path: str
        :param _RealServerType: The origin server type of the forwarding rule, which supports IP and DOMAIN types.
        :type RealServerType: str
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy).
        :type Scheduler: str
        :param _HealthCheck: Whether the health check is enabled for rules. 1: enabled; 0: disabled.
        :type HealthCheck: int
        :param _CheckParams: Parameters related to origin server health check
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _ForwardProtocol: Protocol types of the forwarding from acceleration connection to origin server, which supports HTTP or HTTPS.
If this field is not passed in, it indicates that the ForwardProtocol of the corresponding listener will be used.
        :type ForwardProtocol: str
        :param _ForwardHost: The host to which the acceleration connection forwards. If this parameter is not specified, the default host will be used, i.e., the host with which the client initiates HTTP requests.
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: Whether to enable SNI. Values: `on` (enable), `off` (disable). For creation of HTTP listener forwarding rules, SNI is disabled by default.
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: Server Name Indication (SNI). This field is required when `ServerNameIndicationSwitch` is `ON`.
        :type ServerNameIndication: str
        :param _ForcedRedirect: Enables HTTP-to-HTTPS force redirect for a forwarding rule. Enter a hostname and path of the current forwarding rule.
        :type ForcedRedirect: str
        """
        self._ListenerId = None
        self._Domain = None
        self._Path = None
        self._RealServerType = None
        self._Scheduler = None
        self._HealthCheck = None
        self._CheckParams = None
        self._ForwardProtocol = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

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
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckParams(self):
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ForwardHost(self):
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Path = params.get("Path")
        self._RealServerType = params.get("RealServerType")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
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
        :param _RuleId: The ID of the successfully created forwarding rule
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _DefaultAction: Default policy: ACCEPT or DROP
        :type DefaultAction: str
        :param _ProxyId: Acceleration connection ID
        :type ProxyId: str
        :param _GroupId: Connection group ID
        :type GroupId: str
        """
        self._DefaultAction = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def DefaultAction(self):
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._DefaultAction = params.get("DefaultAction")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Security policy ID
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


class CreateSecurityRulesRequest(AbstractModel):
    """CreateSecurityRules request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Security policy ID
        :type PolicyId: str
        :param _RuleList: List of access rules
        :type RuleList: list of SecurityPolicyRuleIn
        """
        self._PolicyId = None
        self._RuleList = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleIn()
                obj._deserialize(item)
                self._RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityRulesResponse(AbstractModel):
    """CreateSecurityRules response structure.

    """

    def __init__(self):
        r"""
        :param _RuleIdList: List of rule IDs
        :type RuleIdList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleIdList = None
        self._RequestId = None

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleIdList = params.get("RuleIdList")
        self._RequestId = params.get("RequestId")


class CreateTCPListenersRequest(AbstractModel):
    """CreateTCPListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerName: Listener name.
        :type ListenerName: str
        :param _Ports: List of listener ports.
        :type Ports: list of int non-negative
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _HealthCheck: Whether origin server has the health check enabled. 1: enabled; 0: disabled. UDP listeners do not support health check.
        :type HealthCheck: int
        :param _RealServerType: The origin server type. Values: `IP` (IP address); `DOMAIN` (domain name).
        :type RealServerType: str
        :param _ProxyId: Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type ProxyId: str
        :param _GroupId: Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type GroupId: str
        :param _DelayLoop: Time interval of origin server health check (unit: seconds). Value range: [5, 300].
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop.
        :type ConnectTimeout: int
        :param _RealServerPorts: List of origin server ports, which only supports the listeners of version 1.0 and connection group.
        :type RealServerPorts: list of int non-negative
        :param _ClientIPMethod: Listener methods of getting client IPs. 0: TOA; 1: Proxy Protocol.
        :type ClientIPMethod: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode. Valid values: 1 (enable) and 0 (disable). It cannot be enabled for domain name origin servers.
        :type FailoverSwitch: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 - 10.
        :type UnhealthyThreshold: int
        """
        self._ListenerName = None
        self._Ports = None
        self._Scheduler = None
        self._HealthCheck = None
        self._RealServerType = None
        self._ProxyId = None
        self._GroupId = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._RealServerPorts = None
        self._ClientIPMethod = None
        self._FailoverSwitch = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def RealServerPorts(self):
        return self._RealServerPorts

    @RealServerPorts.setter
    def RealServerPorts(self, RealServerPorts):
        self._RealServerPorts = RealServerPorts

    @property
    def ClientIPMethod(self):
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Ports = params.get("Ports")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        self._RealServerType = params.get("RealServerType")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._RealServerPorts = params.get("RealServerPorts")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTCPListenersResponse(AbstractModel):
    """CreateTCPListeners response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: Returns the listener ID
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


class CreateUDPListenersRequest(AbstractModel):
    """CreateUDPListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Ports: List of listener ports
        :type Ports: list of int non-negative
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _RealServerType: The origin server type. Values: `IP` (IP address); `DOMAIN` (domain name).
        :type RealServerType: str
        :param _ProxyId: Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type ProxyId: str
        :param _GroupId: Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type GroupId: str
        :param _RealServerPorts: List of origin server ports, which only supports the listeners of version 1.0 and connection group.
        :type RealServerPorts: list of int non-negative
        :param _DelayLoop: Time interval of origin server health check (unit: seconds). Value range: [5, 300].
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop.
        :type ConnectTimeout: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 - 10.
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode for failover. Values: `1` (enabled); `0` (disabled). It’s not available if the origin type is `DOMAIN`.
        :type FailoverSwitch: int
        :param _HealthCheck: Whether the health check is enabled for the origin server. Values: `1` (enabled); `0` (disabled).
        :type HealthCheck: int
        :param _CheckType: The health check type. Values: `PORT` (port); `PING` (ping).
        :type CheckType: str
        :param _CheckPort: The health probe port.
        :type CheckPort: int
        :param _ContextType: The UDP message type. Values: `TEXT` (text). This parameter is used only when `CheckType = PORT`.
        :type ContextType: str
        :param _SendContext: The UDP message sent by the health probe port. This parameter is used only when `CheckType = PORT`.
        :type SendContext: str
        :param _RecvContext: The UDP message received by the health probe port. This parameter is used only when `CheckType = PORT`.
        :type RecvContext: str
        """
        self._ListenerName = None
        self._Ports = None
        self._Scheduler = None
        self._RealServerType = None
        self._ProxyId = None
        self._GroupId = None
        self._RealServerPorts = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RealServerPorts(self):
        return self._RealServerPorts

    @RealServerPorts.setter
    def RealServerPorts(self, RealServerPorts):
        self._RealServerPorts = RealServerPorts

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

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


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Ports = params.get("Ports")
        self._Scheduler = params.get("Scheduler")
        self._RealServerType = params.get("RealServerType")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._RealServerPorts = params.get("RealServerPorts")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUDPListenersResponse(AbstractModel):
    """CreateUDPListeners response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: Returns the listener ID
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


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: ID of the certificate to be deleted.
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate response structure.

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


class DeleteDomainErrorPageInfoRequest(AbstractModel):
    """DeleteDomainErrorPageInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: Unique ID of a custom error page. For more information, please see the response to CreateDomainErrorPageInfo.
        :type ErrorPageId: str
        """
        self._ErrorPageId = None

    @property
    def ErrorPageId(self):
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId


    def _deserialize(self, params):
        self._ErrorPageId = params.get("ErrorPageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainErrorPageInfoResponse(AbstractModel):
    """DeleteDomainErrorPageInfo response structure.

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


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Domain: Domain name to be deleted
        :type Domain: str
        :param _Force: Whether to make a forced deletion of forwarding rules that have been bound to origin servers. 0: no; 1: yes.
When not making a forced deletion, if there are rules bound to origin servers, they will not be deleted.
        :type Force: int
        """
        self._ListenerId = None
        self._Domain = None
        self._Force = None

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
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain response structure.

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


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: ID list of listeners to be deleted
        :type ListenerIds: list of str
        :param _Force: Whether to allow a forced deletion of listeners that have been bound to origin servers. 1: allowed; 0: not allow.
        :type Force: int
        :param _GroupId: Connection group ID; Either this parameter or `GroupId` must be set, but you cannot set both.
        :type GroupId: str
        :param _ProxyId: Connection ID; Either this parameter or `GroupId` must be set, but you cannot set both.
        :type ProxyId: str
        """
        self._ListenerIds = None
        self._Force = None
        self._GroupId = None
        self._ProxyId = None

    @property
    def ListenerIds(self):
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._Force = params.get("Force")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners response structure.

    """

    def __init__(self):
        r"""
        :param _OperationFailedListenerSet: ID list of listeners failed to be deleted
        :type OperationFailedListenerSet: list of str
        :param _OperationSucceedListenerSet: ID list of listeners deleted successfully
        :type OperationSucceedListenerSet: list of str
        :param _InvalidStatusListenerSet: ID list of invalid listeners. For example: the listener does not exist, or the instance corresponding to the listener does not match.
        :type InvalidStatusListenerSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OperationFailedListenerSet = None
        self._OperationSucceedListenerSet = None
        self._InvalidStatusListenerSet = None
        self._RequestId = None

    @property
    def OperationFailedListenerSet(self):
        return self._OperationFailedListenerSet

    @OperationFailedListenerSet.setter
    def OperationFailedListenerSet(self, OperationFailedListenerSet):
        self._OperationFailedListenerSet = OperationFailedListenerSet

    @property
    def OperationSucceedListenerSet(self):
        return self._OperationSucceedListenerSet

    @OperationSucceedListenerSet.setter
    def OperationSucceedListenerSet(self, OperationSucceedListenerSet):
        self._OperationSucceedListenerSet = OperationSucceedListenerSet

    @property
    def InvalidStatusListenerSet(self):
        return self._InvalidStatusListenerSet

    @InvalidStatusListenerSet.setter
    def InvalidStatusListenerSet(self, InvalidStatusListenerSet):
        self._InvalidStatusListenerSet = InvalidStatusListenerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OperationFailedListenerSet = params.get("OperationFailedListenerSet")
        self._OperationSucceedListenerSet = params.get("OperationSucceedListenerSet")
        self._InvalidStatusListenerSet = params.get("InvalidStatusListenerSet")
        self._RequestId = params.get("RequestId")


class DeleteProxyGroupRequest(AbstractModel):
    """DeleteProxyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the connection group to be deleted.
        :type GroupId: str
        :param _Force: Whether to enable forced deletion. Valid values:
`0`: No;
`1`: Yes.
Default value: 0. If there is a connection or listener/rule bound to an origin server in the connection group and `Force` is 0, the operation will return a failure.
        :type Force: int
        """
        self._GroupId = None
        self._Force = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProxyGroupResponse(AbstractModel):
    """DeleteProxyGroup response structure.

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
        :param _ListenerId: Layer-7 listener ID
        :type ListenerId: str
        :param _RuleId: Forwarding rule ID
        :type RuleId: str
        :param _Force: Whether to make a forced deletion of forwarding rules that have been bound to origin servers. 0: no; 1: yes.
        :type Force: int
        """
        self._ListenerId = None
        self._RuleId = None
        self._Force = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._Force = params.get("Force")
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


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy response structure.

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


class DeleteSecurityRulesRequest(AbstractModel):
    """DeleteSecurityRules request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Security policy ID
        :type PolicyId: str
        :param _RuleIdList: List of access rule IDs
        :type RuleIdList: list of str
        """
        self._PolicyId = None
        self._RuleIdList = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityRulesResponse(AbstractModel):
    """DeleteSecurityRules response structure.

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


class DescribeAccessRegionsByDestRegionRequest(AbstractModel):
    """DescribeAccessRegionsByDestRegion request structure.

    """

    def __init__(self):
        r"""
        :param _DestRegion: Origin server region: the DescribeDestRegions API returns the value of `RegionId` field of `DestRegionSet`.
        :type DestRegion: str
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general), `Accelerator` (specific for games), and `CrossBorder` (cross-MLC-border connection).
        :type PackageType: str
        """
        self._DestRegion = None
        self._IPAddressVersion = None
        self._PackageType = None

    @property
    def DestRegion(self):
        return self._DestRegion

    @DestRegion.setter
    def DestRegion(self, DestRegion):
        self._DestRegion = DestRegion

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._DestRegion = params.get("DestRegion")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRegionsByDestRegionResponse(AbstractModel):
    """DescribeAccessRegionsByDestRegion response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of available acceleration regions
        :type TotalCount: int
        :param _AccessRegionSet: List of available acceleration region information
        :type AccessRegionSet: list of AccessRegionDetial
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccessRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessRegionSet(self):
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessRegionDetial()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessRegionsRequest(AbstractModel):
    """DescribeAccessRegions request structure.

    """


class DescribeAccessRegionsResponse(AbstractModel):
    """DescribeAccessRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity of acceleration regions
        :type TotalCount: int
        :param _AccessRegionSet: Acceleration region details list
        :type AccessRegionSet: list of RegionDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccessRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessRegionSet(self):
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuthSignatureRequest(AbstractModel):
    """DescribeAuthSignature request structure.

    """


class DescribeAuthSignatureResponse(AbstractModel):
    """DescribeAuthSignature response structure.

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


class DescribeBlackHeaderRequest(AbstractModel):
    """DescribeBlackHeader request structure.

    """


class DescribeBlackHeaderResponse(AbstractModel):
    """DescribeBlackHeader response structure.

    """

    def __init__(self):
        r"""
        :param _BlackHeaders: List of blocked custom headers
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BlackHeaders: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlackHeaders = None
        self._RequestId = None

    @property
    def BlackHeaders(self):
        return self._BlackHeaders

    @BlackHeaders.setter
    def BlackHeaders(self, BlackHeaders):
        self._BlackHeaders = BlackHeaders

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlackHeaders = params.get("BlackHeaders")
        self._RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateDetail: Certificate Details.
        :type CertificateDetail: :class:`tencentcloud.gaap.v20180529.models.CertificateDetail`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateDetail = None
        self._RequestId = None

    @property
    def CertificateDetail(self):
        return self._CertificateDetail

    @CertificateDetail.setter
    def CertificateDetail(self, CertificateDetail):
        self._CertificateDetail = CertificateDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertificateDetail") is not None:
            self._CertificateDetail = CertificateDetail()
            self._CertificateDetail._deserialize(params.get("CertificateDetail"))
        self._RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateType: Certificate type. Where:
0: basic authentication configuration;
1: client CA certificate;
2: server SSL certificate;
3: origin server CA certificate;
4: connection SSL certificate.
-1: all types.
The default value is -1.
        :type CertificateType: int
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Quantity limit. The default value is 20.
        :type Limit: int
        """
        self._CertificateType = None
        self._Offset = None
        self._Limit = None

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

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
        self._CertificateType = params.get("CertificateType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateSet: Server certificate list, which includes certificate ID and certificate name.
        :type CertificateSet: list of Certificate
        :param _TotalCount: Total quantity of server certificates that match the query conditions.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CertificateSet(self):
        return self._CertificateSet

    @CertificateSet.setter
    def CertificateSet(self, CertificateSet):
        self._CertificateSet = CertificateSet

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
        if params.get("CertificateSet") is not None:
            self._CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = Certificate()
                obj._deserialize(item)
                self._CertificateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCountryAreaMappingRequest(AbstractModel):
    """DescribeCountryAreaMapping request structure.

    """


class DescribeCountryAreaMappingResponse(AbstractModel):
    """DescribeCountryAreaMapping response structure.

    """

    def __init__(self):
        r"""
        :param _CountryAreaMappingList: Country/region code mapping table
        :type CountryAreaMappingList: list of CountryAreaMap
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CountryAreaMappingList = None
        self._RequestId = None

    @property
    def CountryAreaMappingList(self):
        return self._CountryAreaMappingList

    @CountryAreaMappingList.setter
    def CountryAreaMappingList(self, CountryAreaMappingList):
        self._CountryAreaMappingList = CountryAreaMappingList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CountryAreaMappingList") is not None:
            self._CountryAreaMappingList = []
            for item in params.get("CountryAreaMappingList"):
                obj = CountryAreaMap()
                obj._deserialize(item)
                self._CountryAreaMappingList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomHeaderRequest(AbstractModel):
    """DescribeCustomHeader request structure.

    """


class DescribeCustomHeaderResponse(AbstractModel):
    """DescribeCustomHeader response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleId: str
        :param _Headers: List of custom headers
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Headers: list of HttpHeaderParam
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._Headers = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDestRegionsRequest(AbstractModel):
    """DescribeDestRegions request structure.

    """


class DescribeDestRegionsResponse(AbstractModel):
    """DescribeDestRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of origin server regions
        :type TotalCount: int
        :param _DestRegionSet: List of origin server region details
        :type DestRegionSet: list of RegionDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DestRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DestRegionSet(self):
        return self._DestRegionSet

    @DestRegionSet.setter
    def DestRegionSet(self, DestRegionSet):
        self._DestRegionSet = DestRegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self._DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._DestRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoByIdsRequest(AbstractModel):
    """DescribeDomainErrorPageInfoByIds request structure.

    """

    def __init__(self):
        r"""
        :param _ErrorPageIds: List of custom error IDs. Up to 10 IDs are supported
        :type ErrorPageIds: list of str
        """
        self._ErrorPageIds = None

    @property
    def ErrorPageIds(self):
        return self._ErrorPageIds

    @ErrorPageIds.setter
    def ErrorPageIds(self, ErrorPageIds):
        self._ErrorPageIds = ErrorPageIds


    def _deserialize(self, params):
        self._ErrorPageIds = params.get("ErrorPageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoByIdsResponse(AbstractModel):
    """DescribeDomainErrorPageInfoByIds response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorPageSet: Configuration set of custom error responses
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorPageSet = None
        self._RequestId = None

    @property
    def ErrorPageSet(self):
        return self._ErrorPageSet

    @ErrorPageSet.setter
    def ErrorPageSet(self, ErrorPageSet):
        self._ErrorPageSet = ErrorPageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self._ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self._ErrorPageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoRequest(AbstractModel):
    """DescribeDomainErrorPageInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Domain: Domain name
        :type Domain: str
        """
        self._ListenerId = None
        self._Domain = None

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


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoResponse(AbstractModel):
    """DescribeDomainErrorPageInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorPageSet: Configuration set of a custom error response
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorPageSet = None
        self._RequestId = None

    @property
    def ErrorPageSet(self):
        return self._ErrorPageSet

    @ErrorPageSet.setter
    def ErrorPageSet(self, ErrorPageSet):
        self._ErrorPageSet = ErrorPageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self._ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self._ErrorPageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupAndStatisticsProxyRequest(AbstractModel):
    """DescribeGroupAndStatisticsProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupAndStatisticsProxyResponse(AbstractModel):
    """DescribeGroupAndStatisticsProxy response structure.

    """

    def __init__(self):
        r"""
        :param _GroupSet: Information of connection groups that the statistics can be derived from
        :type GroupSet: list of GroupStatisticsInfo
        :param _TotalCount: Connection group quantity
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GroupSet(self):
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

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
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = GroupStatisticsInfo()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGroupDomainConfigRequest(AbstractModel):
    """DescribeGroupDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupDomainConfigResponse(AbstractModel):
    """DescribeGroupDomainConfig response structure.

    """

    def __init__(self):
        r"""
        :param _AccessRegionList: Nearest access configuration list of domain name resolution.
        :type AccessRegionList: list of DomainAccessRegionDict
        :param _DefaultDnsIp: Default accesses Ip.
        :type DefaultDnsIp: str
        :param _GroupId: Connection group ID.
        :type GroupId: str
        :param _AccessRegionCount: Total number of configuration of access regions.
        :type AccessRegionCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessRegionList = None
        self._DefaultDnsIp = None
        self._GroupId = None
        self._AccessRegionCount = None
        self._RequestId = None

    @property
    def AccessRegionList(self):
        return self._AccessRegionList

    @AccessRegionList.setter
    def AccessRegionList(self, AccessRegionList):
        self._AccessRegionList = AccessRegionList

    @property
    def DefaultDnsIp(self):
        return self._DefaultDnsIp

    @DefaultDnsIp.setter
    def DefaultDnsIp(self, DefaultDnsIp):
        self._DefaultDnsIp = DefaultDnsIp

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def AccessRegionCount(self):
        return self._AccessRegionCount

    @AccessRegionCount.setter
    def AccessRegionCount(self, AccessRegionCount):
        self._AccessRegionCount = AccessRegionCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessRegionList") is not None:
            self._AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = DomainAccessRegionDict()
                obj._deserialize(item)
                self._AccessRegionList.append(obj)
        self._DefaultDnsIp = params.get("DefaultDnsIp")
        self._GroupId = params.get("GroupId")
        self._AccessRegionCount = params.get("AccessRegionCount")
        self._RequestId = params.get("RequestId")


class DescribeHTTPListenersRequest(AbstractModel):
    """DescribeHTTPListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
        :type ProxyId: str
        :param _ListenerId: Filter condition. Exact query by listener IDs.
        :type ListenerId: str
        :param _ListenerName: Filter condition. Exact query by listener names.
        :type ListenerName: str
        :param _Port: Filter condition. Exact query by listener ports.
        :type Port: int
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Quantity limit. The default value is 20.
        :type Limit: int
        :param _SearchValue: Filter condition. It supports fuzzy query by ports or listener names. This parameter cannot be used with `ListenerName` or `Port`.
        :type SearchValue: str
        :param _GroupId: Connection group ID
        :type GroupId: str
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._SearchValue = None
        self._GroupId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

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
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchValue = params.get("SearchValue")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPListenersResponse(AbstractModel):
    """DescribeHTTPListeners response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of listeners
        :type TotalCount: int
        :param _ListenerSet: HTTP listener list
        :type ListenerSet: list of HTTPListener
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHTTPSListenersRequest(AbstractModel):
    """DescribeHTTPSListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Filter condition. Connection ID.
        :type ProxyId: str
        :param _ListenerId: Filter condition. Exact query by listener IDs.
        :type ListenerId: str
        :param _ListenerName: Filter condition. Exact query by listener names.
        :type ListenerName: str
        :param _Port: Filter condition. Exact query by listener ports.
        :type Port: int
        :param _Offset: Offset. The default value is 0
        :type Offset: int
        :param _Limit: Quantity limit. The default value is 20.
        :type Limit: int
        :param _SearchValue: Filter condition. It supports fuzzy query by ports or listener names.
        :type SearchValue: str
        :param _GroupId: Connection group ID as a filter
        :type GroupId: str
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: disable HTTP3;
`1`: enable HTTP3.
Note: If HTTP3 is enabled for a connection, the listener will use the port that is originally accessed to UDP, and a UDP listener with the same port cannot be created.
After the connection is created, you cannot change your HTTP3 setting.
        :type Http3Supported: int
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._SearchValue = None
        self._GroupId = None
        self._Http3Supported = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

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
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchValue = params.get("SearchValue")
        self._GroupId = params.get("GroupId")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPSListenersResponse(AbstractModel):
    """DescribeHTTPSListeners response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of listeners
        :type TotalCount: int
        :param _ListenerSet: HTTPS listener list
        :type ListenerSet: list of HTTPSListener
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPSListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerRealServersRequest(AbstractModel):
    """DescribeListenerRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        """
        self._ListenerId = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerRealServersResponse(AbstractModel):
    """DescribeListenerRealServers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of origin servers that can be bound
        :type TotalCount: int
        :param _RealServerSet: An information list of origin servers
        :type RealServerSet: list of RealServer
        :param _BindRealServerTotalCount: Number of bound origin servers
        :type BindRealServerTotalCount: int
        :param _BindRealServerSet: Information list of bound origin servers
        :type BindRealServerSet: list of BindRealServer
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerSet = None
        self._BindRealServerTotalCount = None
        self._BindRealServerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindRealServerTotalCount(self):
        return self._BindRealServerTotalCount

    @BindRealServerTotalCount.setter
    def BindRealServerTotalCount(self, BindRealServerTotalCount):
        self._BindRealServerTotalCount = BindRealServerTotalCount

    @property
    def BindRealServerSet(self):
        return self._BindRealServerSet

    @BindRealServerSet.setter
    def BindRealServerSet(self, BindRealServerSet):
        self._BindRealServerSet = BindRealServerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self._BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._BindRealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerStatisticsRequest(AbstractModel):
    """DescribeListenerStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricNames: Statistical metric name list. It supports:["InBandwidth", "OutBandwidth", "Concurrent", "InPackets", "OutPackets"]
        :type MetricNames: list of str
        :param _Granularity: Monitoring granularity. It currently supports: 300, 3,600, and 86,400. Unit: seconds.
Time range: <= 1 day, supported minimum granularity: 300 seconds;
Time range: <= 7 days, supported minimum granularity:3,600 seconds;
Time range: > 7 days, supported minimum granularity:86,400 seconds;
        :type Granularity: int
        """
        self._ListenerId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerStatisticsResponse(AbstractModel):
    """DescribeListenerStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _StatisticsData: Connection group statistics
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Queries by one or multiple instance IDs. The upper limit on the number of instances for each request is 100. This parameter does not support specifying InstanceIds and Filters at the same time. It’s an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filters   
The upper limit on Filters for each request is 10, and the upper limit on Filter.Values is 5. This parameter does not support specifying InstanceIds and Filters at the same time. 
ProjectId - String - Required: No - Filter by a project ID.   
AccessRegion - String - Required: No - Filter by an access region.    
RealServerRegion - String - Required: No - Filter by an origin server region.
GroupId - String - Required: No - Filter by a connection group ID.
IPAddressVersion - String - Required: No - Filter by IP version.
PackageType - String - Required: No - Filter by package type of connection groups.
        :type Filters: list of Filter
        :param _ProxyIds: Queries by one or multiple instance IDs. The upper limit on the number of instances for each request is 100. This parameter does not support specifying InstanceIds and Filters at the same time. It’s a new parameter, and replaces InstanceIds.
        :type ProxyIds: list of str
        :param _TagSet: Tag list. If this field exists, the list of the resources with the tag will be pulled.
It supports up to 5 tags. If there are two or more tags, the connections tagged any of them will be pulled.
        :type TagSet: list of TagPair
        :param _Independent: When this field is 1, only not-grouped connections are pulled.
When this field is 0, only grouped connections are pulled.
When this field does not exist, all connections are pulled, including both not-grouped and grouped connections.
        :type Independent: int
        :param _Order: Specifies how connections are listed. Valid values:
`asc`: Ascending order
`desc`: Descending order
Default: `desc`
        :type Order: str
        :param _OrderField: Sorting field. Valid values:
`create_time`: Sort by creation time
`proxy_id`: Sort by connection ID
`bandwidth`:Sort by bandwidth limit
`concurrent_connections`: Sort by number of concurrent connections
Default: `create_time`
        :type OrderField: str
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ProxyIds = None
        self._TagSet = None
        self._Independent = None
        self._Order = None
        self._OrderField = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Independent(self):
        return self._Independent

    @Independent.setter
    def Independent(self, Independent):
        self._Independent = Independent

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ProxyIds = params.get("ProxyIds")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Independent = params.get("Independent")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of connections.
        :type TotalCount: int
        :param _InstanceSet: Connection instance information list; It’s an old parameter, please switch to ProxySet.
        :type InstanceSet: list of ProxyInfo
        :param _ProxySet: Connection instance information list; It’s a new parameter.
        :type ProxySet: list of ProxyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._ProxySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def ProxySet(self):
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxiesStatusRequest(AbstractModel):
    """DescribeProxiesStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Connection ID list; It’s an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ProxyIds: Connection ID list; It’s a new parameter.
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesStatusResponse(AbstractModel):
    """DescribeProxiesStatus response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceStatusSet: Connection status list.
        :type InstanceStatusSet: list of ProxyStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceStatusSet = None
        self._RequestId = None

    @property
    def InstanceStatusSet(self):
        return self._InstanceStatusSet

    @InstanceStatusSet.setter
    def InstanceStatusSet(self, InstanceStatusSet):
        self._InstanceStatusSet = InstanceStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceStatusSet") is not None:
            self._InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = ProxyStatus()
                obj._deserialize(item)
                self._InstanceStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyAndStatisticsListenersRequest(AbstractModel):
    """DescribeProxyAndStatisticsListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyAndStatisticsListenersResponse(AbstractModel):
    """DescribeProxyAndStatisticsListeners response structure.

    """

    def __init__(self):
        r"""
        :param _ProxySet: Information of connections that the statistics can be derived from
        :type ProxySet: list of ProxySimpleInfo
        :param _TotalCount: Quantity of connections
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProxySet(self):
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet

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
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProxyDetailRequest(AbstractModel):
    """DescribeProxyDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID to be queried.
        :type ProxyId: str
        """
        self._ProxyId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyDetailResponse(AbstractModel):
    """DescribeProxyDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyDetail: Connection details
        :type ProxyDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyDetail = None
        self._RequestId = None

    @property
    def ProxyDetail(self):
        return self._ProxyDetail

    @ProxyDetail.setter
    def ProxyDetail(self, ProxyDetail):
        self._ProxyDetail = ProxyDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProxyDetail") is not None:
            self._ProxyDetail = ProxyInfo()
            self._ProxyDetail._deserialize(params.get("ProxyDetail"))
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupDetailsRequest(AbstractModel):
    """DescribeProxyGroupDetails request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupDetailsResponse(AbstractModel):
    """DescribeProxyGroupDetails response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupDetail: Connection group details
        :type ProxyGroupDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyGroupDetail`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyGroupDetail = None
        self._RequestId = None

    @property
    def ProxyGroupDetail(self):
        return self._ProxyGroupDetail

    @ProxyGroupDetail.setter
    def ProxyGroupDetail(self, ProxyGroupDetail):
        self._ProxyGroupDetail = ProxyGroupDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProxyGroupDetail") is not None:
            self._ProxyGroupDetail = ProxyGroupDetail()
            self._ProxyGroupDetail._deserialize(params.get("ProxyGroupDetail"))
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupListRequest(AbstractModel):
    """DescribeProxyGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Number of returned results. The default value is 20. The maximum value is 100.
        :type Limit: int
        :param _ProjectId: Project ID. Value range:
-1: all projects of this user
0: default project
Other values: specified project
        :type ProjectId: int
        :param _Filters: Filter condition   
Each request can have a maximum of 5 filter conditions for `Filter.Values`.
`RealServerRegion` - String - Required: No - Filter by origin server region. You can also check the value of `RegionId` returned by the `DescribeDestRegions` API.
`PackageType` - String - Required: No - Filter by type of connection groups, which can be `Thunder` (general connection group) or `Accelerator` (silver connection group).
        :type Filters: list of Filter
        :param _TagSet: Tag list. If this field exists, the list of the resources with the tag will be pulled.
It supports up to 5 tags. If there are two or more tags, the connection groups tagged any of them will be pulled.
        :type TagSet: list of TagPair
        """
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._Filters = None
        self._TagSet = None

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupListResponse(AbstractModel):
    """DescribeProxyGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of connection groups.
        :type TotalCount: int
        :param _ProxyGroupList: List of connection groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyGroupList: list of ProxyGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyGroupList(self):
        return self._ProxyGroupList

    @ProxyGroupList.setter
    def ProxyGroupList(self, ProxyGroupList):
        self._ProxyGroupList = ProxyGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProxyGroupList") is not None:
            self._ProxyGroupList = []
            for item in params.get("ProxyGroupList"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupStatisticsRequest(AbstractModel):
    """DescribeProxyGroupStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID
        :type GroupId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _MetricNames: Statistical metric name list. Values: InBandwidth (inbound bandwidth); OutBandwidth (outbound bandwidth); Concurrent (concurrence); InPackets (inbound packets); OutPackets (outbound packets).
        :type MetricNames: list of str
        :param _Granularity: Monitoring granularity (in seconds). Valid values: 60s, 300s, 3,600s, 86,400s.
Time range: ≤ 1 day. Supported minimum granularity: 60 seconds;
Time range: ≤ 7 days. Supported minimum granularity: 3,600 seconds;
Time range: ≤ 30 days. Supported minimum granularity: 86,400 seconds;
        :type Granularity: int
        """
        self._GroupId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupStatisticsResponse(AbstractModel):
    """DescribeProxyGroupStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _StatisticsData: Connection group statistics
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyStatisticsRequest(AbstractModel):
    """DescribeProxyStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
        :type ProxyId: str
        :param _StartTime: Start time (2019-03-25 12:00:00)
        :type StartTime: str
        :param _EndTime: End time (2019-03-25 12:00:00)
        :type EndTime: str
        :param _MetricNames: Statistical metric name list. Valid values: `InBandwidth` (inbound bandwidth); `OutBandwidth` (outbound bandwidth); Concurrent (concurrence); `InPackets` (inbound packets); `OutPackets` (outbound packets); `PacketLoss` (packet loss rate); `Latency` (latency); `HttpQPS` (the number of HTTP requests); `HttpsQPS` (the number of HTTPS requests).
        :type MetricNames: list of str
        :param _Granularity: Monitoring granularity. It currently supports: 60, 300, 3,600, and 86,400. Unit: seconds.
Time range: ≤ 3 day. Supported minimum granularity: 60 seconds;
Time range: ≤ 7 day. Supported minimum granularity: 300 seconds;
Time range: ≤ 30 days. Supported minimum granularity: 36,00 seconds;
        :type Granularity: int
        :param _Isp: Specifies the ISP. Valid values: `CMCC`, `CUCC`, and `CTCC`. If it is not specified, all ISP data will be returned. Note that this field is valid only when a non-BGP connection is used.
        :type Isp: str
        """
        self._ProxyId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None
        self._Isp = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        self._Isp = params.get("Isp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyStatisticsResponse(AbstractModel):
    """DescribeProxyStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _StatisticsData: Connection statistics
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRealServerStatisticsRequest(AbstractModel):
    """DescribeRealServerStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _RuleId: Layer-7 rule ID
        :type RuleId: str
        :param _WithinTime: Statistics duration. Unit: hours. It only supports querying statistics for the past 1, 3, 6, 12, and 24 hours.
        :type WithinTime: int
        :param _StartTime: Statistics start time, such as `2020-08-19 00:00:00`
        :type StartTime: str
        :param _EndTime: Statistics end time, such as `2020-08-19 23:59:59`
        :type EndTime: str
        :param _Granularity: Statistics granularity in seconds. Only 1-minute (60-second) and 5-minute (300-second) granularities are supported.
        :type Granularity: int
        """
        self._RealServerId = None
        self._ListenerId = None
        self._RuleId = None
        self._WithinTime = None
        self._StartTime = None
        self._EndTime = None
        self._Granularity = None

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def WithinTime(self):
        return self._WithinTime

    @WithinTime.setter
    def WithinTime(self, WithinTime):
        self._WithinTime = WithinTime

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
    def Granularity(self):
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._WithinTime = params.get("WithinTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServerStatisticsResponse(AbstractModel):
    """DescribeRealServerStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _StatisticsData: Origin server status statistics of specified listener
        :type StatisticsData: list of StatisticsDataInfo
        :param _RsStatisticsData: Status statistics of multiple origin servers
        :type RsStatisticsData: list of MetricStatisticsInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RsStatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

    @property
    def RsStatisticsData(self):
        return self._RsStatisticsData

    @RsStatisticsData.setter
    def RsStatisticsData(self, RsStatisticsData):
        self._RsStatisticsData = RsStatisticsData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        if params.get("RsStatisticsData") is not None:
            self._RsStatisticsData = []
            for item in params.get("RsStatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._RsStatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRealServersRequest(AbstractModel):
    """DescribeRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Queries the project ID to which the origin server belongs. -1: all projects.
        :type ProjectId: int
        :param _SearchValue: Origin server IP or domain name to be queried. The fuzzy match is supported.
        :type SearchValue: str
        :param _Offset: Offset, which is 0 by default.
        :type Offset: int
        :param _Limit: Quantity of values to return. The default value is 20 and the maximum value is 50.
        :type Limit: int
        :param _TagSet: Tag list. If this field exists, the list of the resources with the tag will be pulled.
It supports up to 5 tags. If there are two or more tags, the origin servers tagged any of them will be pulled.
        :type TagSet: list of TagPair
        :param _Filters: Filter conditions. The value of the `name` of the `filter` (RealServerName, RealServerIP)
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._SearchValue = None
        self._Offset = None
        self._Limit = None
        self._TagSet = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

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
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SearchValue = params.get("SearchValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
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
        


class DescribeRealServersResponse(AbstractModel):
    """DescribeRealServers response structure.

    """

    def __init__(self):
        r"""
        :param _RealServerSet: An information list of origin server
        :type RealServerSet: list of BindRealServerInfo
        :param _TotalCount: The quantity of origin servers
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RealServerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

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
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServerInfo()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRealServersStatusRequest(AbstractModel):
    """DescribeRealServersStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RealServerIds: List of origin server IDs
        :type RealServerIds: list of str
        """
        self._RealServerIds = None

    @property
    def RealServerIds(self):
        return self._RealServerIds

    @RealServerIds.setter
    def RealServerIds(self, RealServerIds):
        self._RealServerIds = RealServerIds


    def _deserialize(self, params):
        self._RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServersStatusResponse(AbstractModel):
    """DescribeRealServersStatus response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of origin server query results returned
        :type TotalCount: int
        :param _RealServerStatusSet: Binding status list of origin servers
        :type RealServerStatusSet: list of RealServerStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerStatusSet(self):
        return self._RealServerStatusSet

    @RealServerStatusSet.setter
    def RealServerStatusSet(self, RealServerStatusSet):
        self._RealServerStatusSet = RealServerStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RealServerStatusSet") is not None:
            self._RealServerStatusSet = []
            for item in params.get("RealServerStatusSet"):
                obj = RealServerStatus()
                obj._deserialize(item)
                self._RealServerStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionAndPriceRequest(AbstractModel):
    """DescribeRegionAndPrice request structure.

    """

    def __init__(self):
        r"""
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general), `Accelerator` (specific for games), and `CrossBorder` (cross-MLC-border connection).
        :type PackageType: str
        """
        self._IPAddressVersion = None
        self._PackageType = None

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionAndPriceResponse(AbstractModel):
    """DescribeRegionAndPrice response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of origin server regions
        :type TotalCount: int
        :param _DestRegionSet: List of origin server region details
        :type DestRegionSet: list of RegionDetail
        :param _BandwidthUnitPrice: Connection bandwidth price gradient
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param _Currency: Currency type of bandwidth price:
CNY (Chinese Yuan)
USD (United States Dollar)
        :type Currency: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DestRegionSet = None
        self._BandwidthUnitPrice = None
        self._Currency = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DestRegionSet(self):
        return self._DestRegionSet

    @DestRegionSet.setter
    def DestRegionSet(self, DestRegionSet):
        self._DestRegionSet = DestRegionSet

    @property
    def BandwidthUnitPrice(self):
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self._DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._DestRegionSet.append(obj)
        if params.get("BandwidthUnitPrice") is not None:
            self._BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self._BandwidthUnitPrice.append(obj)
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagRequest(AbstractModel):
    """DescribeResourcesByTag request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        :param _ResourceType: Resource types:
Proxy (connection);
ProxyGroup (connection group);
RealServer (origin server).
If this field is not specified, all resources with the tag will be queried.
        :type ResourceType: str
        """
        self._TagKey = None
        self._TagValue = None
        self._ResourceType = None

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

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagResponse(AbstractModel):
    """DescribeResourcesByTag response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total resources
        :type TotalCount: int
        :param _ResourceSet: Resource list corresponding to the tag
        :type ResourceSet: list of TagResourceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceSet(self):
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = TagResourceInfo()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRuleRealServersRequest(AbstractModel):
    """DescribeRuleRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID
        :type RuleId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self._RuleId = None
        self._Offset = None
        self._Limit = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
        self._RuleId = params.get("RuleId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleRealServersResponse(AbstractModel):
    """DescribeRuleRealServers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of origin servers that can be bound
        :type TotalCount: int
        :param _RealServerSet: Information list of origin servers that can be bound
        :type RealServerSet: list of RealServer
        :param _BindRealServerTotalCount: Quantity of bound origin servers
        :type BindRealServerTotalCount: int
        :param _BindRealServerSet: Bound origin server information list
        :type BindRealServerSet: list of BindRealServer
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerSet = None
        self._BindRealServerTotalCount = None
        self._BindRealServerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindRealServerTotalCount(self):
        return self._BindRealServerTotalCount

    @BindRealServerTotalCount.setter
    def BindRealServerTotalCount(self, BindRealServerTotalCount):
        self._BindRealServerTotalCount = BindRealServerTotalCount

    @property
    def BindRealServerSet(self):
        return self._BindRealServerSet

    @BindRealServerSet.setter
    def BindRealServerSet(self, BindRealServerSet):
        self._BindRealServerSet = BindRealServerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self._BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._BindRealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesByRuleIdsRequest(AbstractModel):
    """DescribeRulesByRuleIds request structure.

    """

    def __init__(self):
        r"""
        :param _RuleIds: List of rule IDs. Up to 10 rules are supported.
        :type RuleIds: list of str
        """
        self._RuleIds = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesByRuleIdsResponse(AbstractModel):
    """DescribeRulesByRuleIds response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of returned rules.
        :type TotalCount: int
        :param _RuleSet: List of returned rules.
        :type RuleSet: list of RuleInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RuleSet(self):
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Layer-7 listener ID.
        :type ListenerId: str
        """
        self._ListenerId = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param _DomainRuleSet: Rule information list classified by domain name type
        :type DomainRuleSet: list of DomainRuleSet
        :param _TotalCount: Total quantity of domain names under this listener
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainRuleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainRuleSet(self):
        return self._DomainRuleSet

    @DomainRuleSet.setter
    def DomainRuleSet(self, DomainRuleSet):
        self._DomainRuleSet = DomainRuleSet

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
        if params.get("DomainRuleSet") is not None:
            self._DomainRuleSet = []
            for item in params.get("DomainRuleSet"):
                obj = DomainRuleSet()
                obj._deserialize(item)
                self._DomainRuleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyDetailRequest(AbstractModel):
    """DescribeSecurityPolicyDetail request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Security policy ID
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyDetailResponse(AbstractModel):
    """DescribeSecurityPolicyDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param _Status: Security policy status:
BOUND (security policies enabled)
UNBIND (security policies disabled)
BINDING (enabling security policies)
UNBINDING (disabling security policies)
        :type Status: str
        :param _DefaultAction: Default policy: ACCEPT or DROP.
        :type DefaultAction: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _RuleList: List of rules
        :type RuleList: list of SecurityPolicyRuleOut
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._Status = None
        self._DefaultAction = None
        self._PolicyId = None
        self._RuleList = None
        self._RequestId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DefaultAction(self):
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        self._DefaultAction = params.get("DefaultAction")
        self._PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityRulesRequest(AbstractModel):
    """DescribeSecurityRules request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityRuleIds: List of security rule IDs. Up to 20 security rules are supported.
        :type SecurityRuleIds: list of str
        """
        self._SecurityRuleIds = None

    @property
    def SecurityRuleIds(self):
        return self._SecurityRuleIds

    @SecurityRuleIds.setter
    def SecurityRuleIds(self, SecurityRuleIds):
        self._SecurityRuleIds = SecurityRuleIds


    def _deserialize(self, params):
        self._SecurityRuleIds = params.get("SecurityRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityRulesResponse(AbstractModel):
    """DescribeSecurityRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of returned security rules.
        :type TotalCount: int
        :param _SecurityRuleSet: List of returned security rules.
        :type SecurityRuleSet: list of SecurityPolicyRuleOut
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecurityRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityRuleSet(self):
        return self._SecurityRuleSet

    @SecurityRuleSet.setter
    def SecurityRuleSet(self, SecurityRuleSet):
        self._SecurityRuleSet = SecurityRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SecurityRuleSet") is not None:
            self._SecurityRuleSet = []
            for item in params.get("SecurityRuleSet"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self._SecurityRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTCPListenersRequest(AbstractModel):
    """DescribeTCPListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Filter condition that filters by connection ID. You must specify at least one filter condition (ProxyId/GroupId/ListenerId), but ProxyId and GroupId cannot be set at the same time.
        :type ProxyId: str
        :param _ListenerId: Filter condition. Exact query by listener ID.
When ProxyId is specified, the listener will be checked whether it belongs to the connection.
When GroupId is specified, the listener will be checked whether it belongs to the connection group.
        :type ListenerId: str
        :param _ListenerName: Filter condition. Exact query by listener name.
        :type ListenerName: str
        :param _Port: Filter condition. Exact query by listener port.
        :type Port: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Quantity limit. The default value is 20.
        :type Limit: int
        :param _GroupId: Filter condition that filters by connection group ID. You must specify at least one filter condition (ProxyId/GroupId/ListenerId), but ProxyId and GroupId cannot be set at the same time.
        :type GroupId: str
        :param _SearchValue: Filter condition. It supports fuzzy query by port or listener name. This parameter cannot be used with `ListenerName` or `Port`.
        :type SearchValue: str
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._SearchValue = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTCPListenersResponse(AbstractModel):
    """DescribeTCPListeners response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity of listeners that matches the conditions
        :type TotalCount: int
        :param _ListenerSet: TCP listener list
        :type ListenerSet: list of TCPListener
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TCPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUDPListenersRequest(AbstractModel):
    """DescribeUDPListeners request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Filter condition that filters by connection ID. You must specify at least one filter condition (ProxyId/GroupId/ListenerId), but ProxyId and GroupId cannot be set at the same time.
        :type ProxyId: str
        :param _ListenerId: Filter condition. Exact query by listener IDs.
When ProxyId is specified, the listener will be checked whether it belongs to the connection.
When GroupId is specified, the listener will be checked whether it belongs to the connection group.
        :type ListenerId: str
        :param _ListenerName: Filter condition. Exact query by listener names.
        :type ListenerName: str
        :param _Port: Filter condition. Exact query by listener ports.
        :type Port: int
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Quantity limit. The default value is 20.
        :type Limit: int
        :param _GroupId: Filter condition that filters by connection group ID. You must specify at least one filter condition (ProxyId/GroupId/ListenerId), but ProxyId and GroupId cannot be set at the same time.
        :type GroupId: str
        :param _SearchValue: Filter condition. It supports fuzzy query by ports or listener names. This parameter cannot be used with `ListenerName` or `Port`.
        :type SearchValue: str
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._SearchValue = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUDPListenersResponse(AbstractModel):
    """DescribeUDPListeners response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of listeners
        :type TotalCount: int
        :param _ListenerSet: UDP listener list
        :type ListenerSet: list of UDPListener
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = UDPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyProxiesRequest(AbstractModel):
    """DestroyProxies request structure.

    """

    def __init__(self):
        r"""
        :param _Force: The identifier for forced deletion
1: this connection list is deleted forcibly regardless of whether the origin server has been bound.
0: this connection list cannot be deleted if the origin server has been bound.
If this identifier is 0, the deletion can be performed only when all the connections have not been bound to any origin servers.
        :type Force: int
        :param _InstanceIds: List of connection instance IDs; It's an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyIds: List of connection instance IDs; It's a new parameter.
        :type ProxyIds: list of str
        """
        self._Force = None
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._Force = params.get("Force")
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyProxiesResponse(AbstractModel):
    """DestroyProxies response structure.

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: ID list of connection instances that cannot be terminated.
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: ID list of connection instances that failed to be terminated.
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class DomainAccessRegionDict(AbstractModel):
    """Nearest access configuration details of domain name resolution

    """

    def __init__(self):
        r"""
        :param _NationCountryInnerList: Nearest access region
        :type NationCountryInnerList: list of NationCountryInnerInfo
        :param _ProxyList: Acceleration region connection list
        :type ProxyList: list of ProxyIdDict
        :param _RegionId: Acceleration region ID
        :type RegionId: str
        :param _GeographicalZoneInnerCode: Acceleration region internal code
        :type GeographicalZoneInnerCode: str
        :param _ContinentInnerCode: Internal code of the continent to which the acceleration region belongs
        :type ContinentInnerCode: str
        :param _RegionName: Acceleration region alias
        :type RegionName: str
        """
        self._NationCountryInnerList = None
        self._ProxyList = None
        self._RegionId = None
        self._GeographicalZoneInnerCode = None
        self._ContinentInnerCode = None
        self._RegionName = None

    @property
    def NationCountryInnerList(self):
        return self._NationCountryInnerList

    @NationCountryInnerList.setter
    def NationCountryInnerList(self, NationCountryInnerList):
        self._NationCountryInnerList = NationCountryInnerList

    @property
    def ProxyList(self):
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GeographicalZoneInnerCode(self):
        return self._GeographicalZoneInnerCode

    @GeographicalZoneInnerCode.setter
    def GeographicalZoneInnerCode(self, GeographicalZoneInnerCode):
        self._GeographicalZoneInnerCode = GeographicalZoneInnerCode

    @property
    def ContinentInnerCode(self):
        return self._ContinentInnerCode

    @ContinentInnerCode.setter
    def ContinentInnerCode(self, ContinentInnerCode):
        self._ContinentInnerCode = ContinentInnerCode

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        if params.get("NationCountryInnerList") is not None:
            self._NationCountryInnerList = []
            for item in params.get("NationCountryInnerList"):
                obj = NationCountryInnerInfo()
                obj._deserialize(item)
                self._NationCountryInnerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyIdDict()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._RegionId = params.get("RegionId")
        self._GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self._ContinentInnerCode = params.get("ContinentInnerCode")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainErrorPageInfo(AbstractModel):
    """Custom error response configuration of a domain name

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: Configuration ID of a custom error response
        :type ErrorPageId: str
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _Domain: Domain name
        :type Domain: str
        :param _ErrorNos: Original error code
        :type ErrorNos: list of int
        :param _NewErrorNo: New error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewErrorNo: int
        :param _ClearHeaders: Response header to be cleared
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClearHeaders: list of str
        :param _SetHeaders: Response header to be set
Note: This field may return null, indicating that no valid values can be obtained.
        :type SetHeaders: list of HttpHeaderParam
        :param _Body: Configured response body (excluding HTTP header)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Body: str
        :param _Status: Rule status. 0: success
Note: this field may return null, indicating that no valid value is obtained.
        :type Status: int
        """
        self._ErrorPageId = None
        self._ListenerId = None
        self._Domain = None
        self._ErrorNos = None
        self._NewErrorNo = None
        self._ClearHeaders = None
        self._SetHeaders = None
        self._Body = None
        self._Status = None

    @property
    def ErrorPageId(self):
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId

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
    def ErrorNos(self):
        return self._ErrorNos

    @ErrorNos.setter
    def ErrorNos(self, ErrorNos):
        self._ErrorNos = ErrorNos

    @property
    def NewErrorNo(self):
        return self._NewErrorNo

    @NewErrorNo.setter
    def NewErrorNo(self, NewErrorNo):
        self._NewErrorNo = NewErrorNo

    @property
    def ClearHeaders(self):
        return self._ClearHeaders

    @ClearHeaders.setter
    def ClearHeaders(self, ClearHeaders):
        self._ClearHeaders = ClearHeaders

    @property
    def SetHeaders(self):
        return self._SetHeaders

    @SetHeaders.setter
    def SetHeaders(self, SetHeaders):
        self._SetHeaders = SetHeaders

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ErrorPageId = params.get("ErrorPageId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._ErrorNos = params.get("ErrorNos")
        self._NewErrorNo = params.get("NewErrorNo")
        self._ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self._SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._SetHeaders.append(obj)
        self._Body = params.get("Body")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainRuleSet(AbstractModel):
    """Forwarding rule information of Layer-7 listeners classified by domain name

    """

    def __init__(self):
        r"""
        :param _Domain: Forwarding rule domain name.
        :type Domain: str
        :param _RuleSet: Forwarding rule list of the domain name.
        :type RuleSet: list of RuleInfo
        :param _CertificateId: Server certificate ID of the domain. When it is `default`, it indicates that the default certificate will be used (i.e., the certificate configured for the listener).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param _CertificateAlias: Server certificate name of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateAlias: str
        :param _ClientCertificateId: Client certificate ID of the domain. When it is `default`, it indicates that the default certificate will be used (i.e., the certificate configured for the listener).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientCertificateId: str
        :param _ClientCertificateAlias: Client certificate name of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientCertificateAlias: str
        :param _BasicAuthConfId: Basic authentication configuration ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BasicAuthConfId: str
        :param _BasicAuth: Basic authentication status:
0: disabled;
1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BasicAuth: int
        :param _BasicAuthConfAlias: Basic authentication configuration name of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BasicAuthConfAlias: str
        :param _RealServerCertificateId: Origin server authentication certificate ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerCertificateId: str
        :param _RealServerAuth: Origin server authentication status:
0: disabled;
1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerAuth: int
        :param _RealServerCertificateAlias: Origin server authentication certificate name of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerCertificateAlias: str
        :param _GaapCertificateId: Connection authentication certificate ID of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GaapCertificateId: str
        :param _GaapAuth: Connection authentication status:
0: disabled;
1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GaapAuth: int
        :param _GaapCertificateAlias: Connection authentication certificate name of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GaapCertificateAlias: str
        :param _RealServerCertificateDomain: Origin server authentication domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerCertificateDomain: str
        :param _PolyClientCertificateAliasInfo: Returns IDs and aliases of multiple certificates when there are multiple client certificates.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param _PolyRealServerCertificateAliasInfo: Returns IDs and aliases of multiple certificates when there are multiple origin certificates.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolyRealServerCertificateAliasInfo: list of CertificateAliasInfo
        :param _DomainStatus: Domain name status.
0: running;
1: changing;
2: deleting.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DomainStatus: int
        :param _BanStatus: Blocking-related status of the domain name. `BANNED`: the domain name is blocked; `RECOVER`: the domain name is unblocked or normal; `BANNING`: the domain name is being blocked; `RECOVERING`: the domain name is being unblocked; `BAN_FAILED`: the blocking fails; RECOVER_FAILED: the unblocking fails.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BanStatus: str
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: disable HTTP3;
`1`: enable HTTP3.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Http3Supported: int
        """
        self._Domain = None
        self._RuleSet = None
        self._CertificateId = None
        self._CertificateAlias = None
        self._ClientCertificateId = None
        self._ClientCertificateAlias = None
        self._BasicAuthConfId = None
        self._BasicAuth = None
        self._BasicAuthConfAlias = None
        self._RealServerCertificateId = None
        self._RealServerAuth = None
        self._RealServerCertificateAlias = None
        self._GaapCertificateId = None
        self._GaapAuth = None
        self._GaapCertificateAlias = None
        self._RealServerCertificateDomain = None
        self._PolyClientCertificateAliasInfo = None
        self._PolyRealServerCertificateAliasInfo = None
        self._DomainStatus = None
        self._BanStatus = None
        self._Http3Supported = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleSet(self):
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def ClientCertificateAlias(self):
        return self._ClientCertificateAlias

    @ClientCertificateAlias.setter
    def ClientCertificateAlias(self, ClientCertificateAlias):
        self._ClientCertificateAlias = ClientCertificateAlias

    @property
    def BasicAuthConfId(self):
        return self._BasicAuthConfId

    @BasicAuthConfId.setter
    def BasicAuthConfId(self, BasicAuthConfId):
        self._BasicAuthConfId = BasicAuthConfId

    @property
    def BasicAuth(self):
        return self._BasicAuth

    @BasicAuth.setter
    def BasicAuth(self, BasicAuth):
        self._BasicAuth = BasicAuth

    @property
    def BasicAuthConfAlias(self):
        return self._BasicAuthConfAlias

    @BasicAuthConfAlias.setter
    def BasicAuthConfAlias(self, BasicAuthConfAlias):
        self._BasicAuthConfAlias = BasicAuthConfAlias

    @property
    def RealServerCertificateId(self):
        return self._RealServerCertificateId

    @RealServerCertificateId.setter
    def RealServerCertificateId(self, RealServerCertificateId):
        self._RealServerCertificateId = RealServerCertificateId

    @property
    def RealServerAuth(self):
        return self._RealServerAuth

    @RealServerAuth.setter
    def RealServerAuth(self, RealServerAuth):
        self._RealServerAuth = RealServerAuth

    @property
    def RealServerCertificateAlias(self):
        return self._RealServerCertificateAlias

    @RealServerCertificateAlias.setter
    def RealServerCertificateAlias(self, RealServerCertificateAlias):
        self._RealServerCertificateAlias = RealServerCertificateAlias

    @property
    def GaapCertificateId(self):
        return self._GaapCertificateId

    @GaapCertificateId.setter
    def GaapCertificateId(self, GaapCertificateId):
        self._GaapCertificateId = GaapCertificateId

    @property
    def GaapAuth(self):
        return self._GaapAuth

    @GaapAuth.setter
    def GaapAuth(self, GaapAuth):
        self._GaapAuth = GaapAuth

    @property
    def GaapCertificateAlias(self):
        return self._GaapCertificateAlias

    @GaapCertificateAlias.setter
    def GaapCertificateAlias(self, GaapCertificateAlias):
        self._GaapCertificateAlias = GaapCertificateAlias

    @property
    def RealServerCertificateDomain(self):
        return self._RealServerCertificateDomain

    @RealServerCertificateDomain.setter
    def RealServerCertificateDomain(self, RealServerCertificateDomain):
        self._RealServerCertificateDomain = RealServerCertificateDomain

    @property
    def PolyClientCertificateAliasInfo(self):
        return self._PolyClientCertificateAliasInfo

    @PolyClientCertificateAliasInfo.setter
    def PolyClientCertificateAliasInfo(self, PolyClientCertificateAliasInfo):
        self._PolyClientCertificateAliasInfo = PolyClientCertificateAliasInfo

    @property
    def PolyRealServerCertificateAliasInfo(self):
        return self._PolyRealServerCertificateAliasInfo

    @PolyRealServerCertificateAliasInfo.setter
    def PolyRealServerCertificateAliasInfo(self, PolyRealServerCertificateAliasInfo):
        self._PolyRealServerCertificateAliasInfo = PolyRealServerCertificateAliasInfo

    @property
    def DomainStatus(self):
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def BanStatus(self):
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._ClientCertificateAlias = params.get("ClientCertificateAlias")
        self._BasicAuthConfId = params.get("BasicAuthConfId")
        self._BasicAuth = params.get("BasicAuth")
        self._BasicAuthConfAlias = params.get("BasicAuthConfAlias")
        self._RealServerCertificateId = params.get("RealServerCertificateId")
        self._RealServerAuth = params.get("RealServerAuth")
        self._RealServerCertificateAlias = params.get("RealServerCertificateAlias")
        self._GaapCertificateId = params.get("GaapCertificateId")
        self._GaapAuth = params.get("GaapAuth")
        self._GaapCertificateAlias = params.get("GaapCertificateAlias")
        self._RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self._PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyClientCertificateAliasInfo.append(obj)
        if params.get("PolyRealServerCertificateAliasInfo") is not None:
            self._PolyRealServerCertificateAliasInfo = []
            for item in params.get("PolyRealServerCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyRealServerCertificateAliasInfo.append(obj)
        self._DomainStatus = params.get("DomainStatus")
        self._BanStatus = params.get("BanStatus")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter conditions

    """

    def __init__(self):
        r"""
        :param _Name: Filter conditions
        :type Name: str
        :param _Values: Filter values
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
        


class GroupStatisticsInfo(AbstractModel):
    """The connection groups from which the statistics can be derived, and the connection information.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID
        :type GroupId: str
        :param _GroupName: Connection group name
        :type GroupName: str
        :param _ProxySet: List of connections of a connection group
        :type ProxySet: list of ProxySimpleInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._ProxySet = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProxySet(self):
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPListener(AbstractModel):
    """HTTP listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port
        :type Port: int
        :param _CreateTime: Listener creation time; using UNIX timestamp.
        :type CreateTime: int
        :param _Protocol: Listener protocol. Valid values: HTTP, HTTPS. The value `HTTP` is used for this structure
        :type Protocol: str
        :param _ListenerStatus: Listener status:
0: running;
1: creating;
2: terminating;
3: adjusting origin server;
4: modifying configuration.
        :type ListenerStatus: int
        :param _ProxyId: Connection ID of the listener. A null value is returned if the listener is associated with the connection group.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyId: str
        :param _GroupId: Connection group ID of the listener. A null value is returned if the listener is associated with a specific connection.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._CreateTime = None
        self._Protocol = None
        self._ListenerStatus = None
        self._ProxyId = None
        self._GroupId = None

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._CreateTime = params.get("CreateTime")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPSListener(AbstractModel):
    """HTTPS listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port
        :type Port: int
        :param _Protocol: Listener protocol. Valid values: HTTP, HTTPS. The value `HTTPS` is used for this structure
        :type Protocol: str
        :param _ListenerStatus: Listener status:
0: running;
1: creating;
2: terminating;
3: adjusting origin server;
4: modifying configuration.
        :type ListenerStatus: int
        :param _CertificateId: Server SSL certificate ID of the listener
        :type CertificateId: str
        :param _ForwardProtocol: Protocol used in the forwarding from connections to origin servers
        :type ForwardProtocol: str
        :param _CreateTime: Listener creation time; using UNIX timestamp.
        :type CreateTime: int
        :param _CertificateAlias: Server SSL certificate alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertificateAlias: str
        :param _ClientCertificateId: Client CA certificate ID of the listener
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientCertificateId: str
        :param _AuthType: Listener authentication mode. Valid values:
0: one-way authentication;
1: mutual authentication.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthType: int
        :param _ClientCertificateAlias: Client CA certificate alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientCertificateAlias: str
        :param _PolyClientCertificateAliasInfo: Alias information of multiple client CA certificates.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param _Http3Supported: Whether to support HTTP3. Values:
`0`: Do not support HTTP3 access;
`1`: Support HTTP3 access.
If HTTP3 is supported for a connection, the listener will use the port that is originally accessed to UDP, and a UDP listener with the same port cannot be created.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http3Supported: int
        :param _ProxyId: Connection ID of the listener. A null value is returned if the listener is associated with the connection group.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param _GroupId: Connection group ID of the listener. A null value is returned if the listener is associated with a specific connection.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Protocol = None
        self._ListenerStatus = None
        self._CertificateId = None
        self._ForwardProtocol = None
        self._CreateTime = None
        self._CertificateAlias = None
        self._ClientCertificateId = None
        self._AuthType = None
        self._ClientCertificateAlias = None
        self._PolyClientCertificateAliasInfo = None
        self._Http3Supported = None
        self._ProxyId = None
        self._GroupId = None

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ClientCertificateAlias(self):
        return self._ClientCertificateAlias

    @ClientCertificateAlias.setter
    def ClientCertificateAlias(self, ClientCertificateAlias):
        self._ClientCertificateAlias = ClientCertificateAlias

    @property
    def PolyClientCertificateAliasInfo(self):
        return self._PolyClientCertificateAliasInfo

    @PolyClientCertificateAliasInfo.setter
    def PolyClientCertificateAliasInfo(self, PolyClientCertificateAliasInfo):
        self._PolyClientCertificateAliasInfo = PolyClientCertificateAliasInfo

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._CertificateId = params.get("CertificateId")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CreateTime = params.get("CreateTime")
        self._CertificateAlias = params.get("CertificateAlias")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._AuthType = params.get("AuthType")
        self._ClientCertificateAlias = params.get("ClientCertificateAlias")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self._PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyClientCertificateAliasInfo.append(obj)
        self._Http3Supported = params.get("Http3Supported")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderParam(AbstractModel):
    """Parameter describing an HTTP packet header

    """

    def __init__(self):
        r"""
        :param _HeaderName: HTTP header name
        :type HeaderName: str
        :param _HeaderValue: HTTP header value
        :type HeaderValue: str
        """
        self._HeaderName = None
        self._HeaderValue = None

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue


    def _deserialize(self, params):
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPDetail(AbstractModel):
    """IP details

    """

    def __init__(self):
        r"""
        :param _IP: IP string
        :type IP: str
        :param _Provider: Network provider. `BGP`: Tencent Cloud BGP (default); `CMCC`: China Mobile; `CUCC`: China Unicom; `CTCC`: China Telecom.
        :type Provider: str
        :param _Bandwidth: Max bandwidth
        :type Bandwidth: int
        """
        self._IP = None
        self._Provider = None
        self._Bandwidth = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Provider(self):
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Provider = params.get("Provider")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyRequest(AbstractModel):
    """InquiryPriceCreateProxy request structure.

    """

    def __init__(self):
        r"""
        :param _AccessRegion: Acceleration region name.
        :type AccessRegion: str
        :param _Bandwidth: Connection bandwidth cap. Unit: Mbps.
        :type Bandwidth: int
        :param _DestRegion: Origin server region name. It's an old parameter, please switch to RealServerRegion.
        :type DestRegion: str
        :param _Concurrency: Upper limit of connection concurrence, which indicates a number of simultaneous online connections. Unit: 10,000 connections. It's an old parameter, please switch to Concurrent.
        :type Concurrency: int
        :param _RealServerRegion: Origin server region name; It's a new parameter.
        :type RealServerRegion: str
        :param _Concurrent: Upper limit of connection concurrence, which indicates a number of simultaneous online connections. Unit: 10,000 connections. It's a new parameter.
        :type Concurrent: int
        :param _BillingType: Billing mode. Valid values: 0: bill-by-bandwidth (default value); 1: bill-by-traffic.
        :type BillingType: int
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
        :type IPAddressVersion: str
        :param _NetworkType: Network type. Valid values: `normal` (default), `cn2`
        :type NetworkType: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general), `Accelerator` (specific for games), and `CrossBorder` (cross-MLC-border connection).
        :type PackageType: str
        :param _Http3Supported: (Disused) HTTP3.0 is supported by default when `IPAddressVersion` is `IPv4`.
        :type Http3Supported: int
        """
        self._AccessRegion = None
        self._Bandwidth = None
        self._DestRegion = None
        self._Concurrency = None
        self._RealServerRegion = None
        self._Concurrent = None
        self._BillingType = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DestRegion(self):
        return self._DestRegion

    @DestRegion.setter
    def DestRegion(self, DestRegion):
        self._DestRegion = DestRegion

    @property
    def Concurrency(self):
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def RealServerRegion(self):
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def BillingType(self):
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._DestRegion = params.get("DestRegion")
        self._Concurrency = params.get("Concurrency")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Concurrent = params.get("Concurrent")
        self._BillingType = params.get("BillingType")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyResponse(AbstractModel):
    """InquiryPriceCreateProxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyDailyPrice: Basic price of connection in USD/day.
        :type ProxyDailyPrice: float
        :param _BandwidthUnitPrice: Tiered price of connection bandwidth.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param _DiscountProxyDailyPrice: Discounted basic price of connection in USD/day.
        :type DiscountProxyDailyPrice: float
        :param _Currency: Currency, which supports CNY, USD, etc.
        :type Currency: str
        :param _FlowUnitPrice: Connection traffic price in USD/GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowUnitPrice: float
        :param _DiscountFlowUnitPrice: Discounted connection traffic price in USD/GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountFlowUnitPrice: float
        :param _Cn2BandwidthPrice: Dedicated BGP bandwidth price. Unit: USD/Mbps/day
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Cn2BandwidthPrice: float
        :param _Cn2BandwidthPriceWithDiscount: Dedicated BGP bandwidth discount price. Unit: USD/Mbps/day
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Cn2BandwidthPriceWithDiscount: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyDailyPrice = None
        self._BandwidthUnitPrice = None
        self._DiscountProxyDailyPrice = None
        self._Currency = None
        self._FlowUnitPrice = None
        self._DiscountFlowUnitPrice = None
        self._Cn2BandwidthPrice = None
        self._Cn2BandwidthPriceWithDiscount = None
        self._RequestId = None

    @property
    def ProxyDailyPrice(self):
        return self._ProxyDailyPrice

    @ProxyDailyPrice.setter
    def ProxyDailyPrice(self, ProxyDailyPrice):
        self._ProxyDailyPrice = ProxyDailyPrice

    @property
    def BandwidthUnitPrice(self):
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def DiscountProxyDailyPrice(self):
        return self._DiscountProxyDailyPrice

    @DiscountProxyDailyPrice.setter
    def DiscountProxyDailyPrice(self, DiscountProxyDailyPrice):
        self._DiscountProxyDailyPrice = DiscountProxyDailyPrice

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def FlowUnitPrice(self):
        return self._FlowUnitPrice

    @FlowUnitPrice.setter
    def FlowUnitPrice(self, FlowUnitPrice):
        self._FlowUnitPrice = FlowUnitPrice

    @property
    def DiscountFlowUnitPrice(self):
        return self._DiscountFlowUnitPrice

    @DiscountFlowUnitPrice.setter
    def DiscountFlowUnitPrice(self, DiscountFlowUnitPrice):
        self._DiscountFlowUnitPrice = DiscountFlowUnitPrice

    @property
    def Cn2BandwidthPrice(self):
        return self._Cn2BandwidthPrice

    @Cn2BandwidthPrice.setter
    def Cn2BandwidthPrice(self, Cn2BandwidthPrice):
        self._Cn2BandwidthPrice = Cn2BandwidthPrice

    @property
    def Cn2BandwidthPriceWithDiscount(self):
        return self._Cn2BandwidthPriceWithDiscount

    @Cn2BandwidthPriceWithDiscount.setter
    def Cn2BandwidthPriceWithDiscount(self, Cn2BandwidthPriceWithDiscount):
        self._Cn2BandwidthPriceWithDiscount = Cn2BandwidthPriceWithDiscount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyDailyPrice = params.get("ProxyDailyPrice")
        if params.get("BandwidthUnitPrice") is not None:
            self._BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self._BandwidthUnitPrice.append(obj)
        self._DiscountProxyDailyPrice = params.get("DiscountProxyDailyPrice")
        self._Currency = params.get("Currency")
        self._FlowUnitPrice = params.get("FlowUnitPrice")
        self._DiscountFlowUnitPrice = params.get("DiscountFlowUnitPrice")
        self._Cn2BandwidthPrice = params.get("Cn2BandwidthPrice")
        self._Cn2BandwidthPriceWithDiscount = params.get("Cn2BandwidthPriceWithDiscount")
        self._RequestId = params.get("RequestId")


class ListenerInfo(AbstractModel):
    """Used by internal APIs. It returns the information of listeners whose statistics can be queried.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listening port
        :type Port: int
        :param _Protocol: Listener protocol type
        :type Protocol: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Protocol = None

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricStatisticsInfo(AbstractModel):
    """One-metric statistics

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name
        :type MetricName: str
        :param _MetricData: Metric statistics
        :type MetricData: list of StatisticsDataInfo
        """
        self._MetricName = None
        self._MetricData = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricData(self):
        return self._MetricData

    @MetricData.setter
    def MetricData(self, MetricData):
        self._MetricData = MetricData


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("MetricData") is not None:
            self._MetricData = []
            for item in params.get("MetricData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self._MetricData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesRequest(AbstractModel):
    """ModifyCertificateAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID.
        :type CertificateId: str
        :param _CertificateAlias: Certificate name. Up to 50 characters.
        :type CertificateAlias: str
        """
        self._CertificateId = None
        self._CertificateAlias = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesResponse(AbstractModel):
    """ModifyCertificateAttributes response structure.

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


class ModifyCertificateRequest(AbstractModel):
    """ModifyCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener instance ID
        :type ListenerId: str
        :param _Domain: Domain name whose certificate needs to be modified
        :type Domain: str
        :param _CertificateId: New server certificate ID:
If CertificateId=default, using the listener certificate.
        :type CertificateId: str
        :param _ClientCertificateId: New client certificate ID:
If ClientCertificateId=default, using the listener certificate.
This parameter is required only when the mutual authentication is adopted.
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: List of new IDs of multiple client certificates, where:
This parameter or the `ClientCertificateId` parameter is required for mutual authentication only.
        :type PolyClientCertificateIds: list of str
        """
        self._ListenerId = None
        self._Domain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None

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
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateResponse(AbstractModel):
    """ModifyCertificate response structure.

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
        :param _ListenerId: Layer-7 listener ID
        :type ListenerId: str
        :param _OldDomain: Original domain name information
        :type OldDomain: str
        :param _NewDomain: New domain name information
        :type NewDomain: str
        :param _CertificateId: Server SSL certificate ID. It's only applicable to the connections of version 3.0:
If this field is not passed in, the original certificate will be used;
If this field is passed in, and CertificateId=default, the listener certificate will be used;
For other cases, the certificate specified by CertificateId will be used.
        :type CertificateId: str
        :param _ClientCertificateId: Client CA certificate ID. It's only applicable to the connections of version 3.0:
If this field is not passed in, the original certificate will be used;
If this field is passed in, and ClientCertificateId=default, the listener certificate will be used;
For other cases, the certificate specified by ClientCertificateId will be used.
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: Client CA certificate ID. It is only applicable to connections on version 3.0, where:
If this field and `ClientCertificateId` are not included, the original certificate will be used;
If this field is included, and ClientCertificateId=default, then the listener certificate will be used;
In other cases, the certificate specified by `ClientCertificateId` or `PolyClientCertificateIds` will be used.
        :type PolyClientCertificateIds: list of str
        """
        self._ListenerId = None
        self._OldDomain = None
        self._NewDomain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def OldDomain(self):
        return self._OldDomain

    @OldDomain.setter
    def OldDomain(self, OldDomain):
        self._OldDomain = OldDomain

    @property
    def NewDomain(self):
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._OldDomain = params.get("OldDomain")
        self._NewDomain = params.get("NewDomain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
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


class ModifyGroupDomainConfigRequest(AbstractModel):
    """ModifyGroupDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID.
        :type GroupId: str
        :param _DefaultDnsIp: Default access IP or domain name of domain name resolution
        :type DefaultDnsIp: str
        :param _AccessRegionList: Nearest access region configuration.
        :type AccessRegionList: list of AccessRegionDomainConf
        """
        self._GroupId = None
        self._DefaultDnsIp = None
        self._AccessRegionList = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DefaultDnsIp(self):
        return self._DefaultDnsIp

    @DefaultDnsIp.setter
    def DefaultDnsIp(self, DefaultDnsIp):
        self._DefaultDnsIp = DefaultDnsIp

    @property
    def AccessRegionList(self):
        return self._AccessRegionList

    @AccessRegionList.setter
    def AccessRegionList(self, AccessRegionList):
        self._AccessRegionList = AccessRegionList


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DefaultDnsIp = params.get("DefaultDnsIp")
        if params.get("AccessRegionList") is not None:
            self._AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = AccessRegionDomainConf()
                obj._deserialize(item)
                self._AccessRegionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupDomainConfigResponse(AbstractModel):
    """ModifyGroupDomainConfig response structure.

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


class ModifyHTTPListenerAttributeRequest(AbstractModel):
    """ModifyHTTPListenerAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID to be modified
        :type ListenerId: str
        :param _ListenerName: New listener name
        :type ListenerName: str
        :param _ProxyId: Connection ID
        :type ProxyId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._ProxyId = None

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
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPListenerAttributeResponse(AbstractModel):
    """ModifyHTTPListenerAttribute response structure.

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


class ModifyHTTPSListenerAttributeRequest(AbstractModel):
    """ModifyHTTPSListenerAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ProxyId: Connection ID. This field is required if using a single connection listener.
        :type ProxyId: str
        :param _ListenerName: New listener name
        :type ListenerName: str
        :param _ForwardProtocol: Type of the protocol used in the forwarding from connections to origin servers
        :type ForwardProtocol: str
        :param _CertificateId: New listener server certificate ID
        :type CertificateId: str
        :param _ClientCertificateId: New listener client certificate ID
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: Client certificate ID of the listener after modification, which is a new field.
        :type PolyClientCertificateIds: list of str
        """
        self._ListenerId = None
        self._ProxyId = None
        self._ListenerName = None
        self._ForwardProtocol = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPSListenerAttributeResponse(AbstractModel):
    """ModifyHTTPSListenerAttribute response structure.

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


class ModifyProxiesAttributeRequest(AbstractModel):
    """ModifyProxiesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: ID of one or multiple connections to be operated; It's an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ProxyName: Connection name. Up to 30 characters.
        :type ProxyName: str
        :param _ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyIds: ID of one or multiple connections to be operated; It's a new parameter.
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ProxyName = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProxyName = params.get("ProxyName")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesAttributeResponse(AbstractModel):
    """ModifyProxiesAttribute response structure.

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


class ModifyProxiesProjectRequest(AbstractModel):
    """ModifyProxiesProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: The target project ID.
        :type ProjectId: int
        :param _InstanceIds: ID of one or multiple connections to be operated; It’s an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyIds: ID of one or multiple connections to be operated; It’s a new parameter.
        :type ProxyIds: list of str
        """
        self._ProjectId = None
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesProjectResponse(AbstractModel):
    """ModifyProxiesProject response structure.

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


class ModifyProxyConfigurationRequest(AbstractModel):
    """ModifyProxyConfiguration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Connection instance ID; It's an old parameter, please switch to ProxyId.
        :type InstanceId: str
        :param _Bandwidth: Target bandwidth. Unit: Mbps.
Bandwidth or Concurrent must be set. Use the DescribeAccessRegionsByDestRegion API to obtain the value range.
        :type Bandwidth: int
        :param _Concurrent: Target concurrence value. Unit: 10,000 connections.
Bandwidth or Concurrent must be set. Use the DescribeAccessRegionsByDestRegion API to obtain the value range.
        :type Concurrent: int
        :param _ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyId: Connection instance ID; It's a new parameter.
        :type ProxyId: str
        :param _BillingType: Billing mode (0: bill-by-bandwidth, 1: bill-by-traffic. Default value: bill-by-bandwidth)
        :type BillingType: int
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Concurrent = None
        self._ClientToken = None
        self._ProxyId = None
        self._BillingType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def BillingType(self):
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._ClientToken = params.get("ClientToken")
        self._ProxyId = params.get("ProxyId")
        self._BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyConfigurationResponse(AbstractModel):
    """ModifyProxyConfiguration response structure.

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


class ModifyProxyGroupAttributeRequest(AbstractModel):
    """ModifyProxyGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the connection group to be modified.
        :type GroupId: str
        :param _GroupName: New connection group name. Up to 30 characters. The extra characters will be truncated.
        :type GroupName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._GroupId = None
        self._GroupName = None
        self._ProjectId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyGroupAttributeResponse(AbstractModel):
    """ModifyProxyGroupAttribute response structure.

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


class ModifyRealServerNameRequest(AbstractModel):
    """ModifyRealServerName request structure.

    """

    def __init__(self):
        r"""
        :param _RealServerName: Origin server name
        :type RealServerName: str
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        """
        self._RealServerName = None
        self._RealServerId = None

    @property
    def RealServerName(self):
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId


    def _deserialize(self, params):
        self._RealServerName = params.get("RealServerName")
        self._RealServerId = params.get("RealServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealServerNameResponse(AbstractModel):
    """ModifyRealServerName response structure.

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


class ModifyRuleAttributeRequest(AbstractModel):
    """ModifyRuleAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _RuleId: Forwarding rule ID
        :type RuleId: str
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _HealthCheck: Whether to enable the origin server health check:
1: enable;
0: disable.
        :type HealthCheck: int
        :param _CheckParams: Health check configuration parameters
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _Path: Forwarding rule path
        :type Path: str
        :param _ForwardProtocol: Protocol types of the forwarding from acceleration connection to origin server, which supports default, HTTP and HTTPS.
If `ForwardProtocol=default`, the `ForwardProtocol` of the listener will be used.
        :type ForwardProtocol: str
        :param _ForwardHost: The forwarding host, which is carried in the request forwarded from the acceleration connection to the origin server.
If `ForwardHost=default`, the domain name configured with the forwarding rule will be used. For other cases, the value set in this field will be used.
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: Specifies whether to enable Server Name Indication (SNI). Valid values: `ON` (enable) and `OFF` (disable).
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: Server Name Indication (SNI). This field is required when `ServerNameIndicationSwitch` is `ON`.
        :type ServerNameIndication: str
        :param _ForcedRedirect: Enables HTTP-to-HTTPS force redirect for a forwarding rule. Enter a hostname and path of the current forwarding rule.
        :type ForcedRedirect: str
        """
        self._ListenerId = None
        self._RuleId = None
        self._Scheduler = None
        self._HealthCheck = None
        self._CheckParams = None
        self._Path = None
        self._ForwardProtocol = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckParams(self):
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ForwardHost(self):
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        self._Path = params.get("Path")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleAttributeResponse(AbstractModel):
    """ModifyRuleAttribute response structure.

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


class ModifySecurityRuleRequest(AbstractModel):
    """ModifySecurityRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _AliasName: Rule name: up to 30 characters. The extra characters will be truncated.
        :type AliasName: str
        :param _PolicyId: Security policy ID
        :type PolicyId: str
        :param _RuleAction: Security rule action
        :type RuleAction: str
        :param _SourceCidr: A CIDR IP address associated with the rule
        :type SourceCidr: str
        :param _Protocol: Protocol type
        :type Protocol: str
        :param _DestPortRange: Port range. Valid values:
A single port: 80
Multiple ports: 80 and 443
Consecutive ports: 3306-20000
All ports: ALL
        :type DestPortRange: str
        """
        self._RuleId = None
        self._AliasName = None
        self._PolicyId = None
        self._RuleAction = None
        self._SourceCidr = None
        self._Protocol = None
        self._DestPortRange = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleAction(self):
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def SourceCidr(self):
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DestPortRange(self):
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AliasName = params.get("AliasName")
        self._PolicyId = params.get("PolicyId")
        self._RuleAction = params.get("RuleAction")
        self._SourceCidr = params.get("SourceCidr")
        self._Protocol = params.get("Protocol")
        self._DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityRuleResponse(AbstractModel):
    """ModifySecurityRule response structure.

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


class ModifyTCPListenerAttributeRequest(AbstractModel):
    """ModifyTCPListenerAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _GroupId: Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type GroupId: str
        :param _ProxyId: Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type ProxyId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _DelayLoop: Time interval of origin server health check (unit: seconds). Value range: [5, 300].
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop.
        :type ConnectTimeout: int
        :param _HealthCheck: Whether to enable health check. 1: enable; 0: disable.
        :type HealthCheck: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode. Valid values: 1 (enable) and 0 (disable). It cannot be enabled for domain name origin servers.
        :type FailoverSwitch: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 -10.
        :type UnhealthyThreshold: int
        """
        self._ListenerId = None
        self._GroupId = None
        self._ProxyId = None
        self._ListenerName = None
        self._Scheduler = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthCheck = None
        self._FailoverSwitch = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._Scheduler = params.get("Scheduler")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheck = params.get("HealthCheck")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTCPListenerAttributeResponse(AbstractModel):
    """ModifyTCPListenerAttribute response structure.

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


class ModifyUDPListenerAttributeRequest(AbstractModel):
    """ModifyUDPListenerAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _GroupId: Connection group ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type GroupId: str
        :param _ProxyId: Connection ID; Either `ProxyId` or `GroupId` must be set, but you cannot set both.
        :type ProxyId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _DelayLoop: Time interval of origin server health check (unit: seconds). Value range: [5, 300].
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop.
        :type ConnectTimeout: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 - 10.
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode for failover. Values: `1` (enabled); `0` (disabled). It’s not available if the origin type is `DOMAIN`.
        :type FailoverSwitch: int
        :param _HealthCheck: Whether the health check is enabled for the origin server. Values: `1` (enabled); `0` (disabled).
        :type HealthCheck: int
        :param _CheckType: The health check type. Values: `PORT` (port); `PING` (ping).
        :type CheckType: str
        :param _CheckPort: The health probe port.
        :type CheckPort: int
        :param _ContextType: The UDP message type. Values: `TEXT` (text). This parameter is used only when `CheckType = PORT`.
        :type ContextType: str
        :param _SendContext: The UDP message sent by the health probe port. This parameter is used only when `CheckType = PORT`.
        :type SendContext: str
        :param _RecvContext: The UDP message received by the health probe port. This parameter is used only when `CheckType = PORT`.
        :type RecvContext: str
        """
        self._ListenerId = None
        self._GroupId = None
        self._ProxyId = None
        self._ListenerName = None
        self._Scheduler = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

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


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._Scheduler = params.get("Scheduler")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUDPListenerAttributeResponse(AbstractModel):
    """ModifyUDPListenerAttribute response structure.

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


class NationCountryInnerInfo(AbstractModel):
    """Nearest access country/region details

    """

    def __init__(self):
        r"""
        :param _NationCountryName: Country name
        :type NationCountryName: str
        :param _NationCountryInnerCode: Country internal code
        :type NationCountryInnerCode: str
        """
        self._NationCountryName = None
        self._NationCountryInnerCode = None

    @property
    def NationCountryName(self):
        return self._NationCountryName

    @NationCountryName.setter
    def NationCountryName(self, NationCountryName):
        self._NationCountryName = NationCountryName

    @property
    def NationCountryInnerCode(self):
        return self._NationCountryInnerCode

    @NationCountryInnerCode.setter
    def NationCountryInnerCode(self, NationCountryInnerCode):
        self._NationCountryInnerCode = NationCountryInnerCode


    def _deserialize(self, params):
        self._NationCountryName = params.get("NationCountryName")
        self._NationCountryInnerCode = params.get("NationCountryInnerCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewRealServer(AbstractModel):
    """Add new origin server information

    """

    def __init__(self):
        r"""
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _RealServerIP: Origin server IP or domain name
        :type RealServerIP: str
        """
        self._RealServerId = None
        self._RealServerIP = None

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerIP = params.get("RealServerIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesRequest(AbstractModel):
    """OpenProxies request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of connection instance IDs; It's an old parameter, please switch to ProxyIds.
        :type InstanceIds: list of str
        :param _ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
For more information, please see How to Ensure Idempotence.
        :type ClientToken: str
        :param _ProxyIds: List of connection instance IDs; It's a new parameter.
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesResponse(AbstractModel):
    """OpenProxies response structure.

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: The connection instance ID list cannot be enabled if it's not disabled.
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: ID list of connection instances failed to be enabled.
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class OpenProxyGroupRequest(AbstractModel):
    """OpenProxyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group instance ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxyGroupResponse(AbstractModel):
    """OpenProxyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: The connection instance ID list cannot be enabled if it’s not disabled.
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: ID list of connection instances failed to be enabled.
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class OpenSecurityPolicyRequest(AbstractModel):
    """OpenSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: ID of the connections requiring enabled security policies.
        :type ProxyId: str
        :param _PolicyId: Security policy ID
        :type PolicyId: str
        """
        self._ProxyId = None
        self._PolicyId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenSecurityPolicyResponse(AbstractModel):
    """OpenSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async Process ID. Using DescribeAsyncTaskStatus to query process and status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ProxyGroupDetail(AbstractModel):
    """Connection group details

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProxyNum: Number of connections in connection group
        :type ProxyNum: int
        :param _Status: Connection group status:
`0`: Running normally
`1`: Creating
`4`: Terminating
`11`: Migrating
`12`: Deploying
        :type Status: int
        :param _OwnerUin: Owner UIN
        :type OwnerUin: str
        :param _CreateUin: Creation UIN
        :type CreateUin: str
        :param _GroupName: Connection name
        :type GroupName: str
        :param _DnsDefaultIp: Default IP of domain name resolution for connection groups
        :type DnsDefaultIp: str
        :param _Domain: Connection group domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _RealServerRegionInfo: Target region
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _IsOldGroup: Whether it is an old connection group, i.e., those created before August 3, 2018.
        :type IsOldGroup: bool
        :param _GroupId: Connection group ID
        :type GroupId: str
        :param _TagSet: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of TagPair
        :param _PolicyId: Security policy ID. This field exists if security policies are set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: str
        :param _Version: Connection group version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _ClientIPMethod: Describes how the connection obtains client IPs. `0`: TOA; `1`: Proxy Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIPMethod: list of int
        :param _IPAddressVersion: IP version. Valid values: `IPv4` (default), `IPv6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IPAddressVersion: str
        :param _PackageType: Package type of connection groups. Valid values: `Thunder` (general connection group), `Accelerator` (silver connection group), and `CrossBorder` (cross-MLC-border connection group).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: Disable
`1`: Enable
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http3Supported: int
        :param _FeatureBitmap: Feature bitmap. Valid values:
`0`: Feature not supported
`1`: Feature supported
Each bit in the bitmap represents a feature:
1st bit: Layer-4 acceleration;
2nd bit: Layer-7 acceleration;
3rd bit: HTTP3 access;
4th bit: IPv6;
5th bit: Dedicated BGP access;
6th bit: Non-BGP access;
7th bit: QoS acceleration.
Note: This field may return null, indicating that no valid values can be obtained.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeatureBitmap: int
        """
        self._CreateTime = None
        self._ProjectId = None
        self._ProxyNum = None
        self._Status = None
        self._OwnerUin = None
        self._CreateUin = None
        self._GroupName = None
        self._DnsDefaultIp = None
        self._Domain = None
        self._RealServerRegionInfo = None
        self._IsOldGroup = None
        self._GroupId = None
        self._TagSet = None
        self._PolicyId = None
        self._Version = None
        self._ClientIPMethod = None
        self._IPAddressVersion = None
        self._PackageType = None
        self._Http3Supported = None
        self._FeatureBitmap = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyNum(self):
        return self._ProxyNum

    @ProxyNum.setter
    def ProxyNum(self, ProxyNum):
        self._ProxyNum = ProxyNum

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def DnsDefaultIp(self):
        return self._DnsDefaultIp

    @DnsDefaultIp.setter
    def DnsDefaultIp(self, DnsDefaultIp):
        self._DnsDefaultIp = DnsDefaultIp

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RealServerRegionInfo(self):
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def IsOldGroup(self):
        return self._IsOldGroup

    @IsOldGroup.setter
    def IsOldGroup(self, IsOldGroup):
        self._IsOldGroup = IsOldGroup

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ClientIPMethod(self):
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def FeatureBitmap(self):
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._ProxyNum = params.get("ProxyNum")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUin = params.get("CreateUin")
        self._GroupName = params.get("GroupName")
        self._DnsDefaultIp = params.get("DnsDefaultIp")
        self._Domain = params.get("Domain")
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._IsOldGroup = params.get("IsOldGroup")
        self._GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._Version = params.get("Version")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """Connection group details list

    """

    def __init__(self):
        r"""
        :param _GroupId: Connection group ID
        :type GroupId: str
        :param _Domain: Connection group domain name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _GroupName: Connection group name
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _RealServerRegionInfo: Target region
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _Status: Connection group status.
Where:
`RUNNING`: Running
`CREATING`: Creating
`DESTROYING`: Terminating
`MOVING`: Migrating
`CHANGING`: Deploying
        :type Status: str
        :param _TagSet: Tag list.
        :type TagSet: list of TagPair
        :param _Version: Connection group version
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _CreateTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _ProxyType: Whether the connection group contains a Microsoft connection
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProxyType: int
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: Disable
`1`: Enable
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http3Supported: int
        :param _FeatureBitmap: Feature bitmap. Valid values:
`0`: Feature not supported
`1`: Feature supported
Each bit in the bitmap represents a feature:
1st bit: Layer-4 acceleration;
2nd bit: Layer-7 acceleration;
3rd bit: HTTP3 access;
4th bit: IPv6;
5th bit: Dedicated BGP access;
6th bit: Non-BGP access;
7th bit: QoS acceleration.
Note: this field may return `null`, indicating that no valid values can be obtained.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FeatureBitmap: int
        """
        self._GroupId = None
        self._Domain = None
        self._GroupName = None
        self._ProjectId = None
        self._RealServerRegionInfo = None
        self._Status = None
        self._TagSet = None
        self._Version = None
        self._CreateTime = None
        self._ProxyType = None
        self._Http3Supported = None
        self._FeatureBitmap = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RealServerRegionInfo(self):
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def FeatureBitmap(self):
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._Status = params.get("Status")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Version = params.get("Version")
        self._CreateTime = params.get("CreateTime")
        self._ProxyType = params.get("ProxyType")
        self._Http3Supported = params.get("Http3Supported")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyIdDict(AbstractModel):
    """Connection ID

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
        :type ProxyId: str
        """
        self._ProxyId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInfo(AbstractModel):
    """Connection information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Connection instance ID; It's an old parameter, please switch to ProxyId.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _CreateTime: Creation time in the format of UNIX timestamp, indicating the number of seconds that have elapsed since January 1, 1970 (midnight in UTC/GMT).
        :type CreateTime: int
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _ProxyName: Connection name.
        :type ProxyName: str
        :param _AccessRegion: Access region.
        :type AccessRegion: str
        :param _RealServerRegion: Origin server region.
        :type RealServerRegion: str
        :param _Bandwidth: Bandwidth. Unit: Mbps.
        :type Bandwidth: int
        :param _Concurrent: Concurrence. Unit: 10K requests/second.
        :type Concurrent: int
        :param _Status: Connection status. Valid values:
`RUNNING`: Running
`CREATING`: Creating
`DESTROYING`: Terminating
`OPENING`: Enabling
`CLOSING`: Disabling
`CLOSED`: Disabled
`ADJUSTING`: Adjusting configuration
`ISOLATING`: Isolating
`ISOLATED`: Isolated
`CLONING`: Copying
`RECOVERING`: Maintaining
`MOVING`: Migrating
        :type Status: str
        :param _Domain: Accessed domain name.
        :type Domain: str
        :param _IP: Accessed IP.
        :type IP: str
        :param _Version: Connection versions: 1.0, 2.0, 3.0.
        :type Version: str
        :param _ProxyId: Connection instance ID; It's a new parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param _Scalarable: 1: this connection is expandable; 0: this connection is not expandable.
        :type Scalarable: int
        :param _SupportProtocols: Supported protocol types.
        :type SupportProtocols: list of str
        :param _GroupId: Connection group ID. This field exists if a connection belongs to a connection group.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        :param _PolicyId: Security policy ID. This field exists if security policies are configured.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: str
        :param _AccessRegionInfo: Access region details, including region ID and region name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _RealServerRegionInfo: Origin server region details, including region ID and region name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _ForwardIP: Forwarding IP of the connection
        :type ForwardIP: str
        :param _TagSet: Tag list. This field is an empty list if no tags exist.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of TagPair
        :param _SupportSecurity: Whether security groups are supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportSecurity: int
        :param _BillingType: Billing mode. 0: bill-by-bandwidth; 1: bill-by-traffic.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BillingType: int
        :param _RelatedGlobalDomains: List of domain names associated with resolution record
Note: this field may return null, indicating that no valid values can be obtained.
        :type RelatedGlobalDomains: list of str
        :param _ModifyConfigTime: Configuration change time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifyConfigTime: int
        :param _ProxyType: Connection type. `100`: THUNDER connection; `103`: Microsoft connection.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ProxyType: int
        :param _ClientIPMethod: Describes how the connection obtains client IPs. 0: TOA; 1: Proxy Protocol.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClientIPMethod: list of int
        :param _IPAddressVersion: IP version. Valid values: `IPv4`, `IPv6`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IPAddressVersion: str
        :param _NetworkType: Network type. `normal`: general BGP; `cn2`: Dedicated BGP; `triple`: Non-BGP (provided by the top 3 ISPs in the Chinese mainland); `secure_eip`: Custom security EIP.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NetworkType: str
        :param _PackageType: Package type of connections. Valid values: `Thunder` (general connection), `Accelerator` (silver connection), 
and `CrossBorder` (cross-MLC-border connection).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PackageType: str
        :param _BanStatus: Blocking-related status of the domain name. `BANNED`: the domain name is blocked; `RECOVER`: the domain name is unblocked or normal; `BANNING`: the domain name is being blocked; `RECOVERING`: the domain name is being unblocked; `BAN_FAILED`: the blocking fails; RECOVER_FAILED: the unblocking fails.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type BanStatus: str
        :param _IPList: 
        :type IPList: list of IPDetail
        :param _Http3Supported: Specifies whether to enable HTTP3. Valid values:
`0`: disable HTTP3;
`1`: enable HTTP3.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Http3Supported: int
        :param _InBanBlacklist: Indicates whether the origin server IP or domain name is in the blocklist. Valid values: `0` (no) and `1` (yes).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type InBanBlacklist: int
        :param _FeatureBitmap: Feature bitmap. Valid values:
`0`: Feature not supported
`1`: Feature supported
Each bit in the bitmap represents a feature:
1st bit: Layer-4 acceleration;
2nd bit: Layer-7 acceleration;
3rd bit: HTTP3 access;
4th bit: IPv6;
5th bit: Dedicated BGP access;
6th bit: Non-BGP access;
7th bit: QoS acceleration.
Note: This field may return `null`, indicating that no valid value can be obtained.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FeatureBitmap: int
        """
        self._InstanceId = None
        self._CreateTime = None
        self._ProjectId = None
        self._ProxyName = None
        self._AccessRegion = None
        self._RealServerRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._Status = None
        self._Domain = None
        self._IP = None
        self._Version = None
        self._ProxyId = None
        self._Scalarable = None
        self._SupportProtocols = None
        self._GroupId = None
        self._PolicyId = None
        self._AccessRegionInfo = None
        self._RealServerRegionInfo = None
        self._ForwardIP = None
        self._TagSet = None
        self._SupportSecurity = None
        self._BillingType = None
        self._RelatedGlobalDomains = None
        self._ModifyConfigTime = None
        self._ProxyType = None
        self._ClientIPMethod = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._BanStatus = None
        self._IPList = None
        self._Http3Supported = None
        self._InBanBlacklist = None
        self._FeatureBitmap = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def AccessRegion(self):
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def RealServerRegion(self):
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Scalarable(self):
        return self._Scalarable

    @Scalarable.setter
    def Scalarable(self, Scalarable):
        self._Scalarable = Scalarable

    @property
    def SupportProtocols(self):
        return self._SupportProtocols

    @SupportProtocols.setter
    def SupportProtocols(self, SupportProtocols):
        self._SupportProtocols = SupportProtocols

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AccessRegionInfo(self):
        return self._AccessRegionInfo

    @AccessRegionInfo.setter
    def AccessRegionInfo(self, AccessRegionInfo):
        self._AccessRegionInfo = AccessRegionInfo

    @property
    def RealServerRegionInfo(self):
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def ForwardIP(self):
        return self._ForwardIP

    @ForwardIP.setter
    def ForwardIP(self, ForwardIP):
        self._ForwardIP = ForwardIP

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def SupportSecurity(self):
        return self._SupportSecurity

    @SupportSecurity.setter
    def SupportSecurity(self, SupportSecurity):
        self._SupportSecurity = SupportSecurity

    @property
    def BillingType(self):
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def RelatedGlobalDomains(self):
        return self._RelatedGlobalDomains

    @RelatedGlobalDomains.setter
    def RelatedGlobalDomains(self, RelatedGlobalDomains):
        self._RelatedGlobalDomains = RelatedGlobalDomains

    @property
    def ModifyConfigTime(self):
        return self._ModifyConfigTime

    @ModifyConfigTime.setter
    def ModifyConfigTime(self, ModifyConfigTime):
        self._ModifyConfigTime = ModifyConfigTime

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def ClientIPMethod(self):
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def IPAddressVersion(self):
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def BanStatus(self):
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def IPList(self):
        return self._IPList

    @IPList.setter
    def IPList(self, IPList):
        self._IPList = IPList

    @property
    def Http3Supported(self):
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def InBanBlacklist(self):
        return self._InBanBlacklist

    @InBanBlacklist.setter
    def InBanBlacklist(self, InBanBlacklist):
        self._InBanBlacklist = InBanBlacklist

    @property
    def FeatureBitmap(self):
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._ProxyName = params.get("ProxyName")
        self._AccessRegion = params.get("AccessRegion")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
        self._IP = params.get("IP")
        self._Version = params.get("Version")
        self._ProxyId = params.get("ProxyId")
        self._Scalarable = params.get("Scalarable")
        self._SupportProtocols = params.get("SupportProtocols")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        if params.get("AccessRegionInfo") is not None:
            self._AccessRegionInfo = RegionDetail()
            self._AccessRegionInfo._deserialize(params.get("AccessRegionInfo"))
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._ForwardIP = params.get("ForwardIP")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._SupportSecurity = params.get("SupportSecurity")
        self._BillingType = params.get("BillingType")
        self._RelatedGlobalDomains = params.get("RelatedGlobalDomains")
        self._ModifyConfigTime = params.get("ModifyConfigTime")
        self._ProxyType = params.get("ProxyType")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._BanStatus = params.get("BanStatus")
        if params.get("IPList") is not None:
            self._IPList = []
            for item in params.get("IPList"):
                obj = IPDetail()
                obj._deserialize(item)
                self._IPList.append(obj)
        self._Http3Supported = params.get("Http3Supported")
        self._InBanBlacklist = params.get("InBanBlacklist")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxySimpleInfo(AbstractModel):
    """Used by internal APIs. It returns connections from which the statistics can be derived, and the listener information.

    """

    def __init__(self):
        r"""
        :param _ProxyId: Connection ID
        :type ProxyId: str
        :param _ProxyName: Connection name
        :type ProxyName: str
        :param _ListenerList: Listener list
        :type ListenerList: list of ListenerInfo
        """
        self._ProxyId = None
        self._ProxyName = None
        self._ListenerList = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ListenerList(self):
        return self._ListenerList

    @ListenerList.setter
    def ListenerList(self, ListenerList):
        self._ListenerList = ListenerList


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        if params.get("ListenerList") is not None:
            self._ListenerList = []
            for item in params.get("ListenerList"):
                obj = ListenerInfo()
                obj._deserialize(item)
                self._ListenerList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyStatus(AbstractModel):
    """Connection status information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Connection instance ID.
        :type InstanceId: str
        :param _Status: Connection status.
Where:
`RUNNING`: Running
`CREATING`: Creating
`DESTROYING`: Terminating
`OPENING`: Enabling
`CLOSING`: Disabling
`CLOSED`: Disabled
`ADJUSTING`: Adjusting configuration
`ISOLATING`: Isolating
`ISOLATED`: Isolated
`MOVING`: Migrating
        :type Status: str
        """
        self._InstanceId = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServer(AbstractModel):
    """Query listeners or rules-related origin server information, excluding `tag` information.

    """

    def __init__(self):
        r"""
        :param _RealServerIP: Origin server IP or domain name
        :type RealServerIP: str
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _RealServerName: Origin server name
        :type RealServerName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _InBanBlacklist: Indicates whether the origin server IP or domain name is in the blocklist. Valid values: `0` (no) and `1` (yes).
        :type InBanBlacklist: int
        """
        self._RealServerIP = None
        self._RealServerId = None
        self._RealServerName = None
        self._ProjectId = None
        self._InBanBlacklist = None

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerName(self):
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InBanBlacklist(self):
        return self._InBanBlacklist

    @InBanBlacklist.setter
    def InBanBlacklist(self, InBanBlacklist):
        self._InBanBlacklist = InBanBlacklist


    def _deserialize(self, params):
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerId = params.get("RealServerId")
        self._RealServerName = params.get("RealServerName")
        self._ProjectId = params.get("ProjectId")
        self._InBanBlacklist = params.get("InBanBlacklist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerBindSetReq(AbstractModel):
    """Information of the bound origin server

    """

    def __init__(self):
        r"""
        :param _RealServerId: Origin server ID
        :type RealServerId: str
        :param _RealServerPort: Origin server port
        :type RealServerPort: int
        :param _RealServerIP: Origin server IP
        :type RealServerIP: str
        :param _RealServerWeight: Origin server weight
        :type RealServerWeight: int
        :param _RealServerFailoverRole: Role of the origin server. Values: `master` (primary origin server); `slave` (secondary origin server). This parameter only takes effect when origin failover is enabled for the listener.
        :type RealServerFailoverRole: str
        """
        self._RealServerId = None
        self._RealServerPort = None
        self._RealServerIP = None
        self._RealServerWeight = None
        self._RealServerFailoverRole = None

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerPort(self):
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerIP(self):
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerWeight(self):
        return self._RealServerWeight

    @RealServerWeight.setter
    def RealServerWeight(self, RealServerWeight):
        self._RealServerWeight = RealServerWeight

    @property
    def RealServerFailoverRole(self):
        return self._RealServerFailoverRole

    @RealServerFailoverRole.setter
    def RealServerFailoverRole(self, RealServerFailoverRole):
        self._RealServerFailoverRole = RealServerFailoverRole


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerWeight = params.get("RealServerWeight")
        self._RealServerFailoverRole = params.get("RealServerFailoverRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerStatus(AbstractModel):
    """Query the binding status of origin servers. BindStatus: 0 (not bound), 1(bound to rules or listeners).

    """

    def __init__(self):
        r"""
        :param _RealServerId: Origin server ID.
        :type RealServerId: str
        :param _BindStatus: `0`: Not bound; `1`: Bound to rule or listener.
        :type BindStatus: int
        :param _ProxyId: ID of the connection bound to this origin server. This string is empty if they are not bound.
        :type ProxyId: str
        :param _GroupId: ID of the connection group bound to this origin server. This string is null if no connection groups are bound.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        """
        self._RealServerId = None
        self._BindStatus = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def RealServerId(self):
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._BindStatus = params.get("BindStatus")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionDetail(AbstractModel):
    """Region details

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name in Chinese or English
        :type RegionName: str
        :param _RegionArea: Region where the data center locates
        :type RegionArea: str
        :param _RegionAreaName: Name of the region where the data center locates
        :type RegionAreaName: str
        :param _IDCType: Data center type. `dc`: data center; `ec`: edge server.
        :type IDCType: str
        :param _FeatureBitmap: Feature bitmap. Valid values:
`0`: the feature is not supported;
`1`: the feature is supported.
Each bit in the bitmap represents a feature:
1st bit: layer-4 acceleration;
2nd bit: layer-7 acceleration;
3rd bit: HTTP3 access;
4th bit: IPv6;
5th bit: dedicated BGP access;
6th bit: non-BGP access;
7th bit: QoS acceleration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FeatureBitmap: int
        :param _SupportFeature: Network support 
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportFeature: :class:`tencentcloud.gaap.v20180529.models.SupportFeature`
        """
        self._RegionId = None
        self._RegionName = None
        self._RegionArea = None
        self._RegionAreaName = None
        self._IDCType = None
        self._FeatureBitmap = None
        self._SupportFeature = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionArea(self):
        return self._RegionArea

    @RegionArea.setter
    def RegionArea(self, RegionArea):
        self._RegionArea = RegionArea

    @property
    def RegionAreaName(self):
        return self._RegionAreaName

    @RegionAreaName.setter
    def RegionAreaName(self, RegionAreaName):
        self._RegionAreaName = RegionAreaName

    @property
    def IDCType(self):
        return self._IDCType

    @IDCType.setter
    def IDCType(self, IDCType):
        self._IDCType = IDCType

    @property
    def FeatureBitmap(self):
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap

    @property
    def SupportFeature(self):
        return self._SupportFeature

    @SupportFeature.setter
    def SupportFeature(self, SupportFeature):
        self._SupportFeature = SupportFeature


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RegionArea = params.get("RegionArea")
        self._RegionAreaName = params.get("RegionAreaName")
        self._IDCType = params.get("IDCType")
        self._FeatureBitmap = params.get("FeatureBitmap")
        if params.get("SupportFeature") is not None:
            self._SupportFeature = SupportFeature()
            self._SupportFeature._deserialize(params.get("SupportFeature"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersRequest(AbstractModel):
    """RemoveRealServers request structure.

    """

    def __init__(self):
        r"""
        :param _RealServerIds: List of origin server IDs
        :type RealServerIds: list of str
        """
        self._RealServerIds = None

    @property
    def RealServerIds(self):
        return self._RealServerIds

    @RealServerIds.setter
    def RealServerIds(self, RealServerIds):
        self._RealServerIds = RealServerIds


    def _deserialize(self, params):
        self._RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersResponse(AbstractModel):
    """RemoveRealServers response structure.

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


class RuleCheckParams(AbstractModel):
    """Health check parameters of the layer-7 listeners' forwarding rules

    """

    def __init__(self):
        r"""
        :param _DelayLoop: Time interval of health check
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of health check
        :type ConnectTimeout: int
        :param _Path: Check path of health check
        :type Path: str
        :param _Method: Health check method: GET/HEAD
        :type Method: str
        :param _StatusCode: Return code indicting normal origin servers. Value range: [100, 200, 300, 400, 500]
        :type StatusCode: list of int non-negative
        :param _Domain: Domain name to be performed health check
You cannot modify this parameter when calling ModifyRuleAttribute API.
        :type Domain: str
        :param _FailedCountInter: Origin server failure check frequency
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FailedCountInter: int
        :param _FailedThreshold: Origin server health check threshold. All requests to the origin server will be blocked once the threshold is exceeded.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FailedThreshold: int
        :param _BlockInter: Duration to block requests targeting the origin server after a failed health check
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BlockInter: int
        """
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._Path = None
        self._Method = None
        self._StatusCode = None
        self._Domain = None
        self._FailedCountInter = None
        self._FailedThreshold = None
        self._BlockInter = None

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

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
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FailedCountInter(self):
        return self._FailedCountInter

    @FailedCountInter.setter
    def FailedCountInter(self, FailedCountInter):
        self._FailedCountInter = FailedCountInter

    @property
    def FailedThreshold(self):
        return self._FailedThreshold

    @FailedThreshold.setter
    def FailedThreshold(self, FailedThreshold):
        self._FailedThreshold = FailedThreshold

    @property
    def BlockInter(self):
        return self._BlockInter

    @BlockInter.setter
    def BlockInter(self, BlockInter):
        self._BlockInter = BlockInter


    def _deserialize(self, params):
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Domain = params.get("Domain")
        self._FailedCountInter = params.get("FailedCountInter")
        self._FailedThreshold = params.get("FailedThreshold")
        self._BlockInter = params.get("BlockInter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """Forwarding rule of layer-7 listeners

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule information
        :type RuleId: str
        :param _ListenerId: Listener information
        :type ListenerId: str
        :param _Domain: Rule domain name
        :type Domain: str
        :param _Path: Rule path
        :type Path: str
        :param _RealServerType: Origin server type
        :type RealServerType: str
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _HealthCheck: Whether health check is enabled. 1: enabled, 0: disabled
        :type HealthCheck: int
        :param _RuleStatus: Rule status. 0: running, 1: creating, 2: terminating, 3: binding/unbinding origin server, 4: updating configuration
        :type RuleStatus: int
        :param _CheckParams: Health check parameters
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _RealServerSet: Bound origin server information
        :type RealServerSet: list of BindRealServer
        :param _BindStatus: Origin server service status. 0: exceptional, 1: normal
If health check is not enabled, this status will always be normal.
As long as one origin server is exceptional, this status will be exceptional. Please view `RealServerSet` for the status of specific origin servers.
        :type BindStatus: int
        :param _ForwardHost: The `host` carried in the request forwarded from the connection to the origin server. `default` indicates directly forwarding the received 'host'.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: Specifies whether to enable Server Name Indication (SNI). Valid values: `ON` (enable) and `OFF` (disable).
Note: This field may return `null`, indicating that no valid value can be obtained.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: Server Name Indication (SNI). This field is required when `ServerNameIndicationSwitch` is `ON`.
Note: This field may return `null`, indicating that no valid value can be obtained.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ServerNameIndication: str
        :param _ForcedRedirect: Forces requests to redirect to HTTPS. When `https:` is passed in, all requests are redirected to HTTPS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForcedRedirect: str
        """
        self._RuleId = None
        self._ListenerId = None
        self._Domain = None
        self._Path = None
        self._RealServerType = None
        self._Scheduler = None
        self._HealthCheck = None
        self._RuleStatus = None
        self._CheckParams = None
        self._RealServerSet = None
        self._BindStatus = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def CheckParams(self):
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ForwardHost(self):
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Path = params.get("Path")
        self._RealServerType = params.get("RealServerType")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindStatus = params.get("BindStatus")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleIn(AbstractModel):
    """Security policy rule (input parameter)

    """

    def __init__(self):
        r"""
        :param _SourceCidr: Source IP or IP range of the request.
        :type SourceCidr: str
        :param _Action: Policy: Allow (ACCEPT) or reject (DROP).
        :type Action: str
        :param _AliasName: Rule alias
        :type AliasName: str
        :param _Protocol: Protocol: TCP or UDP. ALL indicates all protocols.
        :type Protocol: str
        :param _DestPortRange: Target port. Formatting examples:
Single port: 80
Multiple ports: 80, 443
Consecutive ports: 3306-20000
All ports: ALL
        :type DestPortRange: str
        """
        self._SourceCidr = None
        self._Action = None
        self._AliasName = None
        self._Protocol = None
        self._DestPortRange = None

    @property
    def SourceCidr(self):
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DestPortRange(self):
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange


    def _deserialize(self, params):
        self._SourceCidr = params.get("SourceCidr")
        self._Action = params.get("Action")
        self._AliasName = params.get("AliasName")
        self._Protocol = params.get("Protocol")
        self._DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleOut(AbstractModel):
    """Security policy rule (output parameter)

    """

    def __init__(self):
        r"""
        :param _Action: Policy: Allow (ACCEPT) or reject (DROP).
        :type Action: str
        :param _SourceCidr: Source IP or IP range of the request.
        :type SourceCidr: str
        :param _AliasName: Rule alias
        :type AliasName: str
        :param _DestPortRange: Target port range
Note: This field may return null, indicating that no valid values can be obtained.
        :type DestPortRange: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Protocol: Protocol type to be matched (TCP/UDP)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _PolicyId: Security policy ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: str
        """
        self._Action = None
        self._SourceCidr = None
        self._AliasName = None
        self._DestPortRange = None
        self._RuleId = None
        self._Protocol = None
        self._PolicyId = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def SourceCidr(self):
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def DestPortRange(self):
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._SourceCidr = params.get("SourceCidr")
        self._AliasName = params.get("AliasName")
        self._DestPortRange = params.get("DestPortRange")
        self._RuleId = params.get("RuleId")
        self._Protocol = params.get("Protocol")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationRequest(AbstractModel):
    """SetAuthentication request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Domain: The domain name requiring advanced configuration, i.e., the domain name of the listener's forwarding rules.
        :type Domain: str
        :param _BasicAuth: Whether to enable the basic authentication:
0: disable basic authentication;
1: enable basic authentication.
The default value is 0.
        :type BasicAuth: int
        :param _GaapAuth: Whether to enable the connection authentication, which is for the origin server to authenticate GAAP.
0: disable;
1: enable.
The default value is 0.
        :type GaapAuth: int
        :param _RealServerAuth: Whether to enable the origin server authentication, which is for GAAP to authenticate the server.
0: disable;
1: enable.
The default value is 0.
        :type RealServerAuth: int
        :param _BasicAuthConfId: Basic authentication configuration ID, which is obtained from the certificate management page.
        :type BasicAuthConfId: str
        :param _GaapCertificateId: Connection SSL certificate ID, which is obtained from the certificate management page.
        :type GaapCertificateId: str
        :param _RealServerCertificateId: CA certificate ID of the origin server, which is obtained from the certificate management page. When authenticating the origin server, enter this parameter or the `RealServerCertificateIds` parameter.
        :type RealServerCertificateId: str
        :param _RealServerCertificateDomain: This field has been disused. Use ServerNameIndication instead.
        :type RealServerCertificateDomain: str
        :param _PolyRealServerCertificateIds: CA certificate IDs of multiple origin servers, which are obtained from the certificate management page. When authenticating the origin servers, enter this parameter or the `RealServerCertificateId` parameter.
        :type PolyRealServerCertificateIds: list of str
        """
        self._ListenerId = None
        self._Domain = None
        self._BasicAuth = None
        self._GaapAuth = None
        self._RealServerAuth = None
        self._BasicAuthConfId = None
        self._GaapCertificateId = None
        self._RealServerCertificateId = None
        self._RealServerCertificateDomain = None
        self._PolyRealServerCertificateIds = None

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
    def BasicAuth(self):
        return self._BasicAuth

    @BasicAuth.setter
    def BasicAuth(self, BasicAuth):
        self._BasicAuth = BasicAuth

    @property
    def GaapAuth(self):
        return self._GaapAuth

    @GaapAuth.setter
    def GaapAuth(self, GaapAuth):
        self._GaapAuth = GaapAuth

    @property
    def RealServerAuth(self):
        return self._RealServerAuth

    @RealServerAuth.setter
    def RealServerAuth(self, RealServerAuth):
        self._RealServerAuth = RealServerAuth

    @property
    def BasicAuthConfId(self):
        return self._BasicAuthConfId

    @BasicAuthConfId.setter
    def BasicAuthConfId(self, BasicAuthConfId):
        self._BasicAuthConfId = BasicAuthConfId

    @property
    def GaapCertificateId(self):
        return self._GaapCertificateId

    @GaapCertificateId.setter
    def GaapCertificateId(self, GaapCertificateId):
        self._GaapCertificateId = GaapCertificateId

    @property
    def RealServerCertificateId(self):
        return self._RealServerCertificateId

    @RealServerCertificateId.setter
    def RealServerCertificateId(self, RealServerCertificateId):
        self._RealServerCertificateId = RealServerCertificateId

    @property
    def RealServerCertificateDomain(self):
        return self._RealServerCertificateDomain

    @RealServerCertificateDomain.setter
    def RealServerCertificateDomain(self, RealServerCertificateDomain):
        self._RealServerCertificateDomain = RealServerCertificateDomain

    @property
    def PolyRealServerCertificateIds(self):
        return self._PolyRealServerCertificateIds

    @PolyRealServerCertificateIds.setter
    def PolyRealServerCertificateIds(self, PolyRealServerCertificateIds):
        self._PolyRealServerCertificateIds = PolyRealServerCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._BasicAuth = params.get("BasicAuth")
        self._GaapAuth = params.get("GaapAuth")
        self._RealServerAuth = params.get("RealServerAuth")
        self._BasicAuthConfId = params.get("BasicAuthConfId")
        self._GaapCertificateId = params.get("GaapCertificateId")
        self._RealServerCertificateId = params.get("RealServerCertificateId")
        self._RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        self._PolyRealServerCertificateIds = params.get("PolyRealServerCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationResponse(AbstractModel):
    """SetAuthentication response structure.

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


class StatisticsDataInfo(AbstractModel):
    """Statistics information

    """

    def __init__(self):
        r"""
        :param _Time: Corresponding time point
        :type Time: int
        :param _Data: Statistics value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: float
        """
        self._Time = None
        self._Data = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportFeature(AbstractModel):
    """Network support

    """

    def __init__(self):
        r"""
        :param _NetworkType: Supported network types. `normal`: General BGP; `cn2`: Dedicated BGP; `triple`: Non-BGP (provided by the top 3 ISPs in the Chinese mainland); `secure_eip`: Custom security EIPs.
        :type NetworkType: list of str
        """
        self._NetworkType = None

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType


    def _deserialize(self, params):
        self._NetworkType = params.get("NetworkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCPListener(AbstractModel):
    """TCP listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port
        :type Port: int
        :param _RealServerPort: Origin server port, which is only valid for the connections of version 1.0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerPort: int
        :param _RealServerType: Type of the origin server bound to listeners
        :type RealServerType: str
        :param _Protocol: Listener protocol: TCP.
        :type Protocol: str
        :param _ListenerStatus: Listener status:
`0`: Running
`1`: Creating
`2`: Terminating
`3`: Adjusting origin server
`4`: Adjusting configuration
        :type ListenerStatus: int
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds).
        :type ConnectTimeout: int
        :param _DelayLoop: Time interval of origin server health check (unit: seconds).
        :type DelayLoop: int
        :param _HealthCheck: Whether to enable the listener health check:
`0`: Disable
`1`: Enable
        :type HealthCheck: int
        :param _BindStatus: Status of the origin server bound to listeners:
`0`: Abnormal
`1`: Normal
        :type BindStatus: int
        :param _RealServerSet: Information of the origin server bound to listeners
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerSet: list of BindRealServer
        :param _CreateTime: Listener creation time in the format of UNIX timestamp
        :type CreateTime: int
        :param _ClientIPMethod: Describes how the listener obtains client IPs. `0`: TOA; `1`: Proxy Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIPMethod: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 - 10.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode for failover. Values: `1` (enabled); `0` (disabled). It’s not available if the origin type is `DOMAIN`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailoverSwitch: int
        :param _SessionPersist: Specifies whether to enable session persistence. Values: `0` (disable), `1` (enable)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionPersist: int
        :param _ProxyId: Connection ID of the listener. A null value is returned if the listener is associated with the connection group.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyId: str
        :param _GroupId: Connection group ID of the listener. A null value is returned if the listener is associated with a specific connection.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._RealServerPort = None
        self._RealServerType = None
        self._Protocol = None
        self._ListenerStatus = None
        self._Scheduler = None
        self._ConnectTimeout = None
        self._DelayLoop = None
        self._HealthCheck = None
        self._BindStatus = None
        self._RealServerSet = None
        self._CreateTime = None
        self._ClientIPMethod = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._SessionPersist = None
        self._ProxyId = None
        self._GroupId = None

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RealServerPort(self):
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ClientIPMethod(self):
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerType = params.get("RealServerType")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._Scheduler = params.get("Scheduler")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._DelayLoop = params.get("DelayLoop")
        self._HealthCheck = params.get("HealthCheck")
        self._BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._SessionPersist = params.get("SessionPersist")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagPair(AbstractModel):
    """Tag key-value pair

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
        


class TagResourceInfo(AbstractModel):
    """Resource information of the tag

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource types:
`Proxy`: Connection
`ProxyGroup`: Connection group
`RealServer`: Origin server
        :type ResourceType: str
        :param _ResourceId: Instance ID
        :type ResourceId: str
        """
        self._ResourceType = None
        self._ResourceId = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UDPListener(AbstractModel):
    """UDP listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
        :type ListenerId: str
        :param _ListenerName: Listener name
        :type ListenerName: str
        :param _Port: Listener port
        :type Port: int
        :param _RealServerPort: Origin server port, which is only valid for the connections or connection groups of version 1.0.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealServerPort: int
        :param _RealServerType: Type of the origin server bound to listeners
        :type RealServerType: str
        :param _Protocol: Listener protocol: UDP.
        :type Protocol: str
        :param _ListenerStatus: Listener status:
`0`: Running
`1`: Creating
`2`: Terminating
`3`: Adjusting origin server
`4`: Adjusting configuration
        :type ListenerStatus: int
        :param _Scheduler: The strategy used by the listener to access the origin server. Values: `rr` (round-robin), `wrr` (weighted round-robin), `lc` (the least-connections strategy), `lrtt` (the least-response-time strategy).
        :type Scheduler: str
        :param _BindStatus: Origin server binding status of listeners. `0`: Normal; `1`: IP exception; `2`: Domain name resolution exception.
        :type BindStatus: int
        :param _RealServerSet: Information of the origin server bound to listeners
        :type RealServerSet: list of BindRealServer
        :param _CreateTime: Listener creation time in the format of UNIX timestamp
        :type CreateTime: int
        :param _SessionPersist: Specifies whether to enable session persistence. Values: `0` (disable), `1` (enable)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionPersist: int
        :param _DelayLoop: Time interval of origin server health check (unit: seconds). Value range: [5, 300].
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DelayLoop: int
        :param _ConnectTimeout: Response timeout of origin server health check (unit: seconds). Value range: [2, 60]. The timeout value shall be less than the time interval for health check DelayLoop.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ConnectTimeout: int
        :param _HealthyThreshold: Healthy threshold. The number of consecutive successful health checks required before considering an origin server healthy. Value range: 1 - 10.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: Unhealthy threshold. The number of consecutive failed health checks required before considering an origin server unhealthy. Value range: 1 - 10.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: Whether to enable the primary/secondary origin server mode for failover. Values: `1` (enabled); `0` (disabled). It’s not available if the origin type is `DOMAIN`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailoverSwitch: int
        :param _HealthCheck: Whether the health check is enabled for the origin server. Values: `1` (enabled); `0` (disabled).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HealthCheck: int
        :param _CheckType: The health check type. Values: `PORT` (port); `PING` (ping).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CheckType: str
        :param _CheckPort: The health probe port.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CheckPort: int
        :param _ContextType: The UDP message type. Values: `TEXT` (text). This parameter is used only when `CheckType = PORT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ContextType: str
        :param _SendContext: The UDP message sent by the health probe port. This parameter is used only when `CheckType = PORT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SendContext: str
        :param _RecvContext: The UDP message received by the health probe port. This parameter is used only when `CheckType = PORT`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecvContext: str
        :param _ProxyId: Connection ID of the listener. A null value is returned if the listener is associated with the connection group.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param _GroupId: Connection group ID of the listener. A null value is returned if the listener is associated with a specific connection.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._RealServerPort = None
        self._RealServerType = None
        self._Protocol = None
        self._ListenerStatus = None
        self._Scheduler = None
        self._BindStatus = None
        self._RealServerSet = None
        self._CreateTime = None
        self._SessionPersist = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._ProxyId = None
        self._GroupId = None

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
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RealServerPort(self):
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerType(self):
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def RealServerSet(self):
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def DelayLoop(self):
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

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
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerType = params.get("RealServerType")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._Scheduler = params.get("Scheduler")
        self._BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._SessionPersist = params.get("SessionPersist")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        