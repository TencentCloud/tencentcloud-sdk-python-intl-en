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


class AnycastOutPackRelation(AbstractModel):
    """Details of the Anycast package

    """

    def __init__(self):
        r"""
        :param _NormalBandwidth: Application bandwidth (in Mbps).
Note: This field may return null, indicating that no valid values can be obtained.
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: Number of forwarding rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: Auto-renewal flag
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _CurDeadline: Expiration date
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurDeadline: str
        """
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def NormalBandwidth(self):
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressRequest(AbstractModel):
    """AssociateDDoSEipAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID (only Anti-DDoS Advanced). For example, `bgpip-0000011x`.
        :type InstanceId: str
        :param _Eip: EIP of the Anti-DDoS instance ID
        :type Eip: str
        :param _CvmInstanceID: Instance ID to bind. For example, `ins-11112222`. It can be queried in the console or obtained from `InstanceId` returned by `DescribeInstances`.
        :type CvmInstanceID: str
        :param _CvmRegion: Region of the CVM instance. For example, `ap-hongkong`.
        :type CvmRegion: str
        """
        self._InstanceId = None
        self._Eip = None
        self._CvmInstanceID = None
        self._CvmRegion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CvmInstanceID(self):
        return self._CvmInstanceID

    @CvmInstanceID.setter
    def CvmInstanceID(self, CvmInstanceID):
        self._CvmInstanceID = CvmInstanceID

    @property
    def CvmRegion(self):
        return self._CvmRegion

    @CvmRegion.setter
    def CvmRegion(self, CvmRegion):
        self._CvmRegion = CvmRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        self._CvmInstanceID = params.get("CvmInstanceID")
        self._CvmRegion = params.get("CvmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressResponse(AbstractModel):
    """AssociateDDoSEipAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class AssociateDDoSEipLoadBalancerRequest(AbstractModel):
    """AssociateDDoSEipLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID (only Anti-DDoS Advanced). For example, `bgpip-0000011x`.
        :type InstanceId: str
        :param _Eip: EIP of the Anti-DDoS instance ID.
        :type Eip: str
        :param _LoadBalancerID: ID of the CLB to bind, such as `lb-0000002i`. It can be queried in the console or obtained from `LoadBalancerId` returned by the `DescribeLoadBalancers` API.
        :type LoadBalancerID: str
        :param _LoadBalancerRegion: Region of the CLB instance, such as `ap-hongkong`.
        :type LoadBalancerRegion: str
        :param _Vip: CLB private IP
        :type Vip: str
        """
        self._InstanceId = None
        self._Eip = None
        self._LoadBalancerID = None
        self._LoadBalancerRegion = None
        self._Vip = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def LoadBalancerID(self):
        return self._LoadBalancerID

    @LoadBalancerID.setter
    def LoadBalancerID(self, LoadBalancerID):
        self._LoadBalancerID = LoadBalancerID

    @property
    def LoadBalancerRegion(self):
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        self._LoadBalancerID = params.get("LoadBalancerID")
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipLoadBalancerResponse(AbstractModel):
    """AssociateDDoSEipLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class BGPIPInstance(AbstractModel):
    """Anti-DDoS Advanced instance details

    """

    def __init__(self):
        r"""
        :param _InstanceDetail: Anti-DDoS instance details
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param _SpecificationLimit: Anti-DDoS instance specifications
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceSpecification`
        :param _Usage: Anti-DDoS instance usage statistics
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceUsages`
        :param _Region: Region of the Anti-DDoS instance
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param _Status: Status of the Anti-DDoS instance. Valid values:
`idle`: running
`attacking`: under attacks
`blocking`: blocked
`creating`: creating
`deblocking`: unblocking
`isolate`: reprocessed and isolated
        :type Status: str
        :param _ExpiredTime: Purchase time
        :type ExpiredTime: str
        :param _CreatedTime: Expired At
        :type CreatedTime: str
        :param _Name: Name of the Anti-DDoS instance
        :type Name: str
        :param _PackInfo: Package details of the Anti-DDoS instance.
Note: This field is `null` for an Anti-DDoS instance without using a package.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param _StaticPackRelation: Non-BGP package details of the Anti-DDoS instance.
Note: This field is `null` for an Anti-DDoS instance without using a non-BGP package.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StaticPackRelation: :class:`tencentcloud.antiddos.v20200309.models.StaticPackRelation`
        :param _ZoneId: Specifies the ISP. `0`: Chinese mainland ISPs (default); `1`：Radware；`2`: Tencent; `3`: NSFOCUS. Note that `1`, `2` and `3` are used for services outside the Chinese mainland.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _Tgw: Used to differentiate clusters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tgw: int
        :param _EipAddressStatus: EIP states: `CREATING`, `BINDING`, `BIND`, `UNBINDING`, `UNBIND`, `OFFLINING`, and `BIND_ENI`. The EIP must be bound to an Anti-DDoS Advanced instance.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipAddressStatus: str
        :param _EipFlag: Whether it is an Anti-DDoS EIP instance. `1`: Yes; `0`: No.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipFlag: int
        :param _EipAddressPackRelation: EIP package details of the Anti-DDoS Advanced instance.
Note: This field is `null` for an Anti-DDoS Advanced instance without using an EIP package.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipAddressPackRelation: :class:`tencentcloud.antiddos.v20200309.models.EipAddressPackRelation`
        :param _EipAddressInfo: Details of the Anti-DDoS Advanced instance bound to the EIP.
Note: This field is `null` if the EIP is not bound to an Anti-DDoS Advanced instance.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipAddressInfo: :class:`tencentcloud.antiddos.v20200309.models.EipAddressRelation`
        :param _Domain: Recommended domain name for clients to access.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DamDDoSStatus: Whether to enable Sec-MCA. Valid values: `1` (enabled) and `0` (disabled).
        :type DamDDoSStatus: int
        :param _V6Flag: Whether it’s an IPv6 address. `1`: Yes; `0`: No.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type V6Flag: int
        :param _BGPIPChannelFlag: Whether it’s an Anti-DDoS Advanced instance from Tencent Cloud channels. `1`: Yes; `0`: No.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BGPIPChannelFlag: int
        :param _TagInfoList: Tag that the Anti-DDoS Advanced instance is associated with
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TagInfoList: list of TagInfo
        :param _AnycastOutPackRelation: All-out package details of the instance
When an all-out package is not used by the instance, this field is `null`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AnycastOutPackRelation: :class:`tencentcloud.antiddos.v20200309.models.AnycastOutPackRelation`
        :param _InstanceVersion: Edition of the instance
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type InstanceVersion: int
        :param _ConvoyId: Convoy instance ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ConvoyId: str
        :param _ElasticBandwidth: Pay-as-you-go bandwidth
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ElasticBandwidth: int
        :param _EOFlag: Whether it’s the IP broadcasted by EdgeOne. Values: `1` (yes), `0` (no)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EOFlag: int
        """
        self._InstanceDetail = None
        self._SpecificationLimit = None
        self._Usage = None
        self._Region = None
        self._Status = None
        self._ExpiredTime = None
        self._CreatedTime = None
        self._Name = None
        self._PackInfo = None
        self._StaticPackRelation = None
        self._ZoneId = None
        self._Tgw = None
        self._EipAddressStatus = None
        self._EipFlag = None
        self._EipAddressPackRelation = None
        self._EipAddressInfo = None
        self._Domain = None
        self._DamDDoSStatus = None
        self._V6Flag = None
        self._BGPIPChannelFlag = None
        self._TagInfoList = None
        self._AnycastOutPackRelation = None
        self._InstanceVersion = None
        self._ConvoyId = None
        self._ElasticBandwidth = None
        self._EOFlag = None

    @property
    def InstanceDetail(self):
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def SpecificationLimit(self):
        return self._SpecificationLimit

    @SpecificationLimit.setter
    def SpecificationLimit(self, SpecificationLimit):
        self._SpecificationLimit = SpecificationLimit

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PackInfo(self):
        return self._PackInfo

    @PackInfo.setter
    def PackInfo(self, PackInfo):
        self._PackInfo = PackInfo

    @property
    def StaticPackRelation(self):
        return self._StaticPackRelation

    @StaticPackRelation.setter
    def StaticPackRelation(self, StaticPackRelation):
        self._StaticPackRelation = StaticPackRelation

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Tgw(self):
        return self._Tgw

    @Tgw.setter
    def Tgw(self, Tgw):
        self._Tgw = Tgw

    @property
    def EipAddressStatus(self):
        return self._EipAddressStatus

    @EipAddressStatus.setter
    def EipAddressStatus(self, EipAddressStatus):
        self._EipAddressStatus = EipAddressStatus

    @property
    def EipFlag(self):
        return self._EipFlag

    @EipFlag.setter
    def EipFlag(self, EipFlag):
        self._EipFlag = EipFlag

    @property
    def EipAddressPackRelation(self):
        return self._EipAddressPackRelation

    @EipAddressPackRelation.setter
    def EipAddressPackRelation(self, EipAddressPackRelation):
        self._EipAddressPackRelation = EipAddressPackRelation

    @property
    def EipAddressInfo(self):
        return self._EipAddressInfo

    @EipAddressInfo.setter
    def EipAddressInfo(self, EipAddressInfo):
        self._EipAddressInfo = EipAddressInfo

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DamDDoSStatus(self):
        return self._DamDDoSStatus

    @DamDDoSStatus.setter
    def DamDDoSStatus(self, DamDDoSStatus):
        self._DamDDoSStatus = DamDDoSStatus

    @property
    def V6Flag(self):
        return self._V6Flag

    @V6Flag.setter
    def V6Flag(self, V6Flag):
        self._V6Flag = V6Flag

    @property
    def BGPIPChannelFlag(self):
        return self._BGPIPChannelFlag

    @BGPIPChannelFlag.setter
    def BGPIPChannelFlag(self, BGPIPChannelFlag):
        self._BGPIPChannelFlag = BGPIPChannelFlag

    @property
    def TagInfoList(self):
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def AnycastOutPackRelation(self):
        return self._AnycastOutPackRelation

    @AnycastOutPackRelation.setter
    def AnycastOutPackRelation(self, AnycastOutPackRelation):
        self._AnycastOutPackRelation = AnycastOutPackRelation

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def ConvoyId(self):
        return self._ConvoyId

    @ConvoyId.setter
    def ConvoyId(self, ConvoyId):
        self._ConvoyId = ConvoyId

    @property
    def ElasticBandwidth(self):
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth

    @property
    def EOFlag(self):
        return self._EOFlag

    @EOFlag.setter
    def EOFlag(self, EOFlag):
        self._EOFlag = EOFlag


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceRelation()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self._SpecificationLimit = BGPIPInstanceSpecification()
            self._SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self._Usage = BGPIPInstanceUsages()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self._Region = RegionInfo()
            self._Region._deserialize(params.get("Region"))
        self._Status = params.get("Status")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CreatedTime = params.get("CreatedTime")
        self._Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self._PackInfo = PackInfo()
            self._PackInfo._deserialize(params.get("PackInfo"))
        if params.get("StaticPackRelation") is not None:
            self._StaticPackRelation = StaticPackRelation()
            self._StaticPackRelation._deserialize(params.get("StaticPackRelation"))
        self._ZoneId = params.get("ZoneId")
        self._Tgw = params.get("Tgw")
        self._EipAddressStatus = params.get("EipAddressStatus")
        self._EipFlag = params.get("EipFlag")
        if params.get("EipAddressPackRelation") is not None:
            self._EipAddressPackRelation = EipAddressPackRelation()
            self._EipAddressPackRelation._deserialize(params.get("EipAddressPackRelation"))
        if params.get("EipAddressInfo") is not None:
            self._EipAddressInfo = EipAddressRelation()
            self._EipAddressInfo._deserialize(params.get("EipAddressInfo"))
        self._Domain = params.get("Domain")
        self._DamDDoSStatus = params.get("DamDDoSStatus")
        self._V6Flag = params.get("V6Flag")
        self._BGPIPChannelFlag = params.get("BGPIPChannelFlag")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        if params.get("AnycastOutPackRelation") is not None:
            self._AnycastOutPackRelation = AnycastOutPackRelation()
            self._AnycastOutPackRelation._deserialize(params.get("AnycastOutPackRelation"))
        self._InstanceVersion = params.get("InstanceVersion")
        self._ConvoyId = params.get("ConvoyId")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        self._EOFlag = params.get("EOFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceSpecification(AbstractModel):
    """Anti-DDoS Advanced instance specifications

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: Base protection bandwidth (in Mbps)
        :type ProtectBandwidth: int
        :param _ProtectCCQPS: CC protection bandwidth (in QPS)
        :type ProtectCCQPS: int
        :param _NormalBandwidth: Normal application bandwidth (in Mbps)
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: Number of forwarding rules
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: Auto-renewal status. Valid values:
`0`: disabled
`1`: enabled
]
        :type AutoRenewFlag: int
        :param _Line: Anti-DDoS Advanced line. Valid values:
`1`: BGP
`2`: China Telecom
`3`: China Unicom
`4`: China Mobile
`99`: third-party line
]
        :type Line: int
        :param _ElasticBandwidth: Elastic protection bandwidth (in Mbps)
        :type ElasticBandwidth: int
        """
        self._ProtectBandwidth = None
        self._ProtectCCQPS = None
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._Line = None
        self._ElasticBandwidth = None

    @property
    def ProtectBandwidth(self):
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def ProtectCCQPS(self):
        return self._ProtectCCQPS

    @ProtectCCQPS.setter
    def ProtectCCQPS(self, ProtectCCQPS):
        self._ProtectCCQPS = ProtectCCQPS

    @property
    def NormalBandwidth(self):
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def ElasticBandwidth(self):
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._ProtectCCQPS = params.get("ProtectCCQPS")
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Line = params.get("Line")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceUsages(AbstractModel):
    """Anti-DDoS Advanced instance usage statistics

    """

    def __init__(self):
        r"""
        :param _PortRulesUsage: Number of used port rules
        :type PortRulesUsage: int
        :param _DomainRulesUsage: Number of used domain name rules
        :type DomainRulesUsage: int
        :param _Last7DayAttackCount: Number of attack times in the last 7 days
        :type Last7DayAttackCount: int
        """
        self._PortRulesUsage = None
        self._DomainRulesUsage = None
        self._Last7DayAttackCount = None

    @property
    def PortRulesUsage(self):
        return self._PortRulesUsage

    @PortRulesUsage.setter
    def PortRulesUsage(self, PortRulesUsage):
        self._PortRulesUsage = PortRulesUsage

    @property
    def DomainRulesUsage(self):
        return self._DomainRulesUsage

    @DomainRulesUsage.setter
    def DomainRulesUsage(self, DomainRulesUsage):
        self._DomainRulesUsage = DomainRulesUsage

    @property
    def Last7DayAttackCount(self):
        return self._Last7DayAttackCount

    @Last7DayAttackCount.setter
    def Last7DayAttackCount(self, Last7DayAttackCount):
        self._Last7DayAttackCount = Last7DayAttackCount


    def _deserialize(self, params):
        self._PortRulesUsage = params.get("PortRulesUsage")
        self._DomainRulesUsage = params.get("DomainRulesUsage")
        self._Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstance(AbstractModel):
    """Details of the Anti-DDoS Pro instance

    """

    def __init__(self):
        r"""
        :param _InstanceDetail: Details of the Anti-DDoS Pro instance
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param _SpecificationLimit: Specifications of the Anti-DDoS Pro instance
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceSpecification`
        :param _Usage: Usage statistics of the Anti-DDoS Pro instance
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceUsages`
        :param _Region: Region of the Anti-DDoS Pro instance
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param _Status: Status of the Anti-DDoS Pro instance. Valid values:
`idle`: The instance is running normally.
`attacking`: The instance is under attack.
`blocking`: The instance is blocked.
`creating`: The instance is being created.
`deblocking`: Unblocking the instance
`isolate`: The instance is being isolated.
        :type Status: str
        :param _CreatedTime: Purchase time
        :type CreatedTime: str
        :param _ExpiredTime: Expiration time
        :type ExpiredTime: str
        :param _Name: Name of the Anti-DDoS Pro instance
        :type Name: str
        :param _PackInfo: Details of the package to which the Anti-DDoS Pro instance belongs.
When the package provided is not used by the instance, this field is `null`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param _EipProductInfos: Details of the cloud product used by the EIP bound to the Anti-DDoS Pro instance
        :type EipProductInfos: list of EipProductInfo
        :param _BoundStatus: Binding status of the Anti-DDoS Pro instance
`idle`: The instance is bound.
 `bounding`: Binding the instance.
`failed`: Failed to bind
]
        :type BoundStatus: str
        :param _DDoSLevel: Layer-4 protection level
        :type DDoSLevel: str
        :param _CCEnable: Status of CC protection
        :type CCEnable: int
        :param _TagInfoList: Tags associated with the resource
        :type TagInfoList: list of TagInfo
        :param _IpCountNewFlag: New edition of Anti-DDoS Pro
        :type IpCountNewFlag: int
        :param _VitalityVersion: The version of attack defense package
        :type VitalityVersion: int
        :param _Line: Network line
Note: This field may return null, indicating that no valid values can be obtained.
        :type Line: int
        :param _ElasticServiceBandwidth: Whether to enable elastic bandwidth
        :type ElasticServiceBandwidth: int
        :param _GiftServiceBandWidth: Bandwidth quota given away by Tencent Cloud
        :type GiftServiceBandWidth: int
        """
        self._InstanceDetail = None
        self._SpecificationLimit = None
        self._Usage = None
        self._Region = None
        self._Status = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._Name = None
        self._PackInfo = None
        self._EipProductInfos = None
        self._BoundStatus = None
        self._DDoSLevel = None
        self._CCEnable = None
        self._TagInfoList = None
        self._IpCountNewFlag = None
        self._VitalityVersion = None
        self._Line = None
        self._ElasticServiceBandwidth = None
        self._GiftServiceBandWidth = None

    @property
    def InstanceDetail(self):
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def SpecificationLimit(self):
        return self._SpecificationLimit

    @SpecificationLimit.setter
    def SpecificationLimit(self, SpecificationLimit):
        self._SpecificationLimit = SpecificationLimit

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PackInfo(self):
        return self._PackInfo

    @PackInfo.setter
    def PackInfo(self, PackInfo):
        self._PackInfo = PackInfo

    @property
    def EipProductInfos(self):
        return self._EipProductInfos

    @EipProductInfos.setter
    def EipProductInfos(self, EipProductInfos):
        self._EipProductInfos = EipProductInfos

    @property
    def BoundStatus(self):
        return self._BoundStatus

    @BoundStatus.setter
    def BoundStatus(self, BoundStatus):
        self._BoundStatus = BoundStatus

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def TagInfoList(self):
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def IpCountNewFlag(self):
        return self._IpCountNewFlag

    @IpCountNewFlag.setter
    def IpCountNewFlag(self, IpCountNewFlag):
        self._IpCountNewFlag = IpCountNewFlag

    @property
    def VitalityVersion(self):
        return self._VitalityVersion

    @VitalityVersion.setter
    def VitalityVersion(self, VitalityVersion):
        self._VitalityVersion = VitalityVersion

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def ElasticServiceBandwidth(self):
        return self._ElasticServiceBandwidth

    @ElasticServiceBandwidth.setter
    def ElasticServiceBandwidth(self, ElasticServiceBandwidth):
        self._ElasticServiceBandwidth = ElasticServiceBandwidth

    @property
    def GiftServiceBandWidth(self):
        return self._GiftServiceBandWidth

    @GiftServiceBandWidth.setter
    def GiftServiceBandWidth(self, GiftServiceBandWidth):
        self._GiftServiceBandWidth = GiftServiceBandWidth


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceRelation()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self._SpecificationLimit = BGPInstanceSpecification()
            self._SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self._Usage = BGPInstanceUsages()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self._Region = RegionInfo()
            self._Region._deserialize(params.get("Region"))
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self._PackInfo = PackInfo()
            self._PackInfo._deserialize(params.get("PackInfo"))
        if params.get("EipProductInfos") is not None:
            self._EipProductInfos = []
            for item in params.get("EipProductInfos"):
                obj = EipProductInfo()
                obj._deserialize(item)
                self._EipProductInfos.append(obj)
        self._BoundStatus = params.get("BoundStatus")
        self._DDoSLevel = params.get("DDoSLevel")
        self._CCEnable = params.get("CCEnable")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        self._IpCountNewFlag = params.get("IpCountNewFlag")
        self._VitalityVersion = params.get("VitalityVersion")
        self._Line = params.get("Line")
        self._ElasticServiceBandwidth = params.get("ElasticServiceBandwidth")
        self._GiftServiceBandWidth = params.get("GiftServiceBandWidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceSpecification(AbstractModel):
    """Anti-DDoS Pro instance specifications

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: Base protection bandwidth (in Gbps)
        :type ProtectBandwidth: int
        :param _ProtectCountLimit: Number of protection chances
        :type ProtectCountLimit: int
        :param _ProtectIPNumberLimit: Number of protected IPs
        :type ProtectIPNumberLimit: int
        :param _AutoRenewFlag: Auto-renewal status. Values:
`0`: Disabled
`1`: Enabled
]
        :type AutoRenewFlag: int
        :param _UnionPackFlag: Protection type of Anti-DDoS Pro. Valid values: `0` (general protection) and `1` (Lighthouse-based protection).
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnionPackFlag: int
        :param _ServiceBandWidth: Application bandwidth
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceBandWidth: int
        :param _BattleEditionFlag: Whether it’s an Anti-DDoS Pro Premium edition. Values: `0` (General edition); `1` (Premium edition).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BattleEditionFlag: int
        :param _ChannelEditionFlag: Whether it’s an Anti-DDoS Pro Standard edition. Values: `0` (General edition); `1` (Standard edition).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelEditionFlag: int
        :param _EnterpriseFlag: Whether it’s an Anti-DDoS Pro Enterprise edition. Values: `0` (General edition); `1` (Enterprise edition).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseFlag: int
        :param _ElasticLimit: Elastic bandwidth threshold of the Anti-DDoS Pro Enterprise edition.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ElasticLimit: int
        :param _DownGradeProtect: Protection bandwidth after the plan downgrade, in Gbps. 
Note: This field may return `null`, indicating that no valid value was found.
        :type DownGradeProtect: int
        """
        self._ProtectBandwidth = None
        self._ProtectCountLimit = None
        self._ProtectIPNumberLimit = None
        self._AutoRenewFlag = None
        self._UnionPackFlag = None
        self._ServiceBandWidth = None
        self._BattleEditionFlag = None
        self._ChannelEditionFlag = None
        self._EnterpriseFlag = None
        self._ElasticLimit = None
        self._DownGradeProtect = None

    @property
    def ProtectBandwidth(self):
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def ProtectCountLimit(self):
        return self._ProtectCountLimit

    @ProtectCountLimit.setter
    def ProtectCountLimit(self, ProtectCountLimit):
        self._ProtectCountLimit = ProtectCountLimit

    @property
    def ProtectIPNumberLimit(self):
        return self._ProtectIPNumberLimit

    @ProtectIPNumberLimit.setter
    def ProtectIPNumberLimit(self, ProtectIPNumberLimit):
        self._ProtectIPNumberLimit = ProtectIPNumberLimit

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def UnionPackFlag(self):
        return self._UnionPackFlag

    @UnionPackFlag.setter
    def UnionPackFlag(self, UnionPackFlag):
        self._UnionPackFlag = UnionPackFlag

    @property
    def ServiceBandWidth(self):
        return self._ServiceBandWidth

    @ServiceBandWidth.setter
    def ServiceBandWidth(self, ServiceBandWidth):
        self._ServiceBandWidth = ServiceBandWidth

    @property
    def BattleEditionFlag(self):
        return self._BattleEditionFlag

    @BattleEditionFlag.setter
    def BattleEditionFlag(self, BattleEditionFlag):
        self._BattleEditionFlag = BattleEditionFlag

    @property
    def ChannelEditionFlag(self):
        return self._ChannelEditionFlag

    @ChannelEditionFlag.setter
    def ChannelEditionFlag(self, ChannelEditionFlag):
        self._ChannelEditionFlag = ChannelEditionFlag

    @property
    def EnterpriseFlag(self):
        return self._EnterpriseFlag

    @EnterpriseFlag.setter
    def EnterpriseFlag(self, EnterpriseFlag):
        self._EnterpriseFlag = EnterpriseFlag

    @property
    def ElasticLimit(self):
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def DownGradeProtect(self):
        return self._DownGradeProtect

    @DownGradeProtect.setter
    def DownGradeProtect(self, DownGradeProtect):
        self._DownGradeProtect = DownGradeProtect


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._ProtectCountLimit = params.get("ProtectCountLimit")
        self._ProtectIPNumberLimit = params.get("ProtectIPNumberLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._UnionPackFlag = params.get("UnionPackFlag")
        self._ServiceBandWidth = params.get("ServiceBandWidth")
        self._BattleEditionFlag = params.get("BattleEditionFlag")
        self._ChannelEditionFlag = params.get("ChannelEditionFlag")
        self._EnterpriseFlag = params.get("EnterpriseFlag")
        self._ElasticLimit = params.get("ElasticLimit")
        self._DownGradeProtect = params.get("DownGradeProtect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceUsages(AbstractModel):
    """Anti-DDoS Pro instance usage statistics

    """

    def __init__(self):
        r"""
        :param _ProtectCountUsage: Number of used protection chances
        :type ProtectCountUsage: int
        :param _ProtectIPNumberUsage: Number of protected IPs
        :type ProtectIPNumberUsage: int
        :param _Last7DayAttackCount: Number of attack times in the last 7 days
        :type Last7DayAttackCount: int
        """
        self._ProtectCountUsage = None
        self._ProtectIPNumberUsage = None
        self._Last7DayAttackCount = None

    @property
    def ProtectCountUsage(self):
        return self._ProtectCountUsage

    @ProtectCountUsage.setter
    def ProtectCountUsage(self, ProtectCountUsage):
        self._ProtectCountUsage = ProtectCountUsage

    @property
    def ProtectIPNumberUsage(self):
        return self._ProtectIPNumberUsage

    @ProtectIPNumberUsage.setter
    def ProtectIPNumberUsage(self, ProtectIPNumberUsage):
        self._ProtectIPNumberUsage = ProtectIPNumberUsage

    @property
    def Last7DayAttackCount(self):
        return self._Last7DayAttackCount

    @Last7DayAttackCount.setter
    def Last7DayAttackCount(self, Last7DayAttackCount):
        self._Last7DayAttackCount = Last7DayAttackCount


    def _deserialize(self, params):
        self._ProtectCountUsage = params.get("ProtectCountUsage")
        self._ProtectIPNumberUsage = params.get("ProtectIPNumberUsage")
        self._Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlackWhiteIpRelation(AbstractModel):
    """IP blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _Type: IP type. Valid values: `black` (blocklisted IP), `white`(allowlisted IP).
        :type Type: str
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        :param _Mask: IP mask. `0` indicates a 32-bit IP.
        :type Mask: int
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._Ip = None
        self._Type = None
        self._InstanceDetailList = None
        self._Mask = None
        self._ModifyTime = None

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

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Type = params.get("Type")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        self._Mask = params.get("Mask")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """IP bound to the Anti-DDoS Pro instance

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _BizType: Category of product that can be bound. Valid values: `public` (CVM and CLB), `bm` (BM), `eni` (ENI), `vpngw` (VPN gateway), `natgw` (NAT gateway), `waf` (WAF), `fpc` (financial products), `gaap` (GAAP), and `other` (hosted IP). This field is required when you perform binding.
        :type BizType: str
        :param _InstanceId: Anti-DDoS instance ID of the IP. This field is required only when the instance is bound to an IP. For example, this field InstanceId will be `eni-*` if the instance ID is bound to an ENI IP; `none` if there is no instance to bind to a managed IP.
        :type InstanceId: str
        :param _DeviceType: Sub-product category. Valid values: `cvm` (CVM), `lb` (Load balancer), `eni` (ENI), `vpngw` (VPN gateway), `natgw` (NAT gateway), `waf` (WAF), `fpc` (financial products), `gaap` (GAAP), `eip` (BM EIP) and `other` (managed IP). This field is required when you perform binding.
        :type DeviceType: str
        :param _IspCode: ISP. Valid values: `0` (China Telecom), `1` (China Unicom), `2` (China Mobile), and `5` (BGP). This field is required when you perform binding.
        :type IspCode: int
        """
        self._Ip = None
        self._BizType = None
        self._InstanceId = None
        self._DeviceType = None
        self._IspCode = None

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IspCode(self):
        return self._IspCode

    @IspCode.setter
    def IspCode(self, IspCode):
        self._IspCode = IspCode


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._InstanceId = params.get("InstanceId")
        self._DeviceType = params.get("DeviceType")
        self._IspCode = params.get("IspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLevelPolicy(AbstractModel):
    """The level-defining policy of CC attacks

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: Ip
        :type Ip: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Level: Protection level. Values: `default`, `loose` and `strict`.
        :type Level: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Level = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Level = params.get("Level")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPlyRecord(AbstractModel):
    """CC precise protection configuration fields

    """

    def __init__(self):
        r"""
        :param _FieldType: Type of the configuration field. Only `value` is supported.
        :type FieldType: str
        :param _FieldName: Configuration field. Valid values: `cgi`, `ua`, `cookie`, `referer`, `accept`, and `srcip`.
        :type FieldName: str
        :param _Value: Value of the configuration field
        :type Value: str
        :param _ValueOperator: Filters values of configuration fields. `equal`: The value matches the configuration field. `not_equal`: The value does not match the configuration field. `include`: The value is included.
        :type ValueOperator: str
        """
        self._FieldType = None
        self._FieldName = None
        self._Value = None
        self._ValueOperator = None

    @property
    def FieldType(self):
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueOperator(self):
        return self._ValueOperator

    @ValueOperator.setter
    def ValueOperator(self, ValueOperator):
        self._ValueOperator = ValueOperator


    def _deserialize(self, params):
        self._FieldType = params.get("FieldType")
        self._FieldName = params.get("FieldName")
        self._Value = params.get("Value")
        self._ValueOperator = params.get("ValueOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPolicy(AbstractModel):
    """CC precise protection policy information

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Domain: Domain name
        :type Domain: str
        :param _PolicyAction: Action of limiting request frequency. Valid values: `alg` (limit request frequency via verification codes) and `drop`(drop requests).
        :type PolicyAction: str
        :param _PolicyList: List of policies
        :type PolicyList: list of CCPrecisionPlyRecord
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._PolicyAction = None
        self._PolicyList = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def PolicyAction(self):
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCReqLimitPolicyRecord(AbstractModel):
    """Configuration fields of CC frequency limit policies

    """

    def __init__(self):
        r"""
        :param _Period: Sampling interval (in seconds). Valid values: `1`, `10`, `30`, and `60`.
        :type Period: int
        :param _RequestNum: Number of requests. Value range: 1-2000.
        :type RequestNum: int
        :param _Action: Action of limiting request frequency. Valid values: `alg` (limit request frequency via verification codes) and `drop`(drop requests).
        :type Action: str
        :param _ExecuteDuration: Sets an interval of the frequency limit policy. Value range: 1-86400 (in seconds).
        :type ExecuteDuration: int
        :param _Mode: Filters values of configuration fields. `include`: The value is included. `equal`: The value matches the configuration field.
        :type Mode: str
        :param _Uri: URI, which cannot be used together with `User-Agent` and `Cookie`.
        :type Uri: str
        :param _UserAgent: User-Agent, which cannot be used together with `Uri` and `Cookie`.
        :type UserAgent: str
        :param _Cookie: Cookie, which cannot be used together with `Uri` and `User-Agent`.
        :type Cookie: str
        """
        self._Period = None
        self._RequestNum = None
        self._Action = None
        self._ExecuteDuration = None
        self._Mode = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RequestNum(self):
        return self._RequestNum

    @RequestNum.setter
    def RequestNum(self, RequestNum):
        self._RequestNum = RequestNum

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ExecuteDuration(self):
        return self._ExecuteDuration

    @ExecuteDuration.setter
    def ExecuteDuration(self, ExecuteDuration):
        self._ExecuteDuration = ExecuteDuration

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

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
        self._Period = params.get("Period")
        self._RequestNum = params.get("RequestNum")
        self._Action = params.get("Action")
        self._ExecuteDuration = params.get("ExecuteDuration")
        self._Mode = params.get("Mode")
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
        


class CCThresholdPolicy(AbstractModel):
    """CC cleansing threshold policy

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Threshold: Cleansing threshold
        :type Threshold: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Threshold = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Threshold = params.get("Threshold")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcBlackWhiteIpPolicy(AbstractModel):
    """Layer-4 access control list

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Type: IP type. Valid values: `black` (blocklisted IP), `white`(allowlisted IP).
        :type Type: str
        :param _BlackWhiteIp: Blocklist/Allowlist IP address
        :type BlackWhiteIp: str
        :param _Mask: Mask
        :type Mask: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Type = None
        self._BlackWhiteIp = None
        self._Mask = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BlackWhiteIp(self):
        return self._BlackWhiteIp

    @BlackWhiteIp.setter
    def BlackWhiteIp(self, BlackWhiteIp):
        self._BlackWhiteIp = BlackWhiteIp

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Type = params.get("Type")
        self._BlackWhiteIp = params.get("BlackWhiteIp")
        self._Mask = params.get("Mask")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIPBlockConfig(AbstractModel):
    """Anti-DDoS regional blocking configuration

    """

    def __init__(self):
        r"""
        :param _RegionType: Region type. Valid values:
`oversea`: Outside the Chinese mainland.
`china`: The Chinese mainland.
`customized`: User-specified region.
]
        :type RegionType: str
        :param _Action: Blocking action. Valid values:
`drop`: Block the request.
`alg`: Verify the request via CAPTCHA.
]
        :type Action: str
        :param _Id: Configuration ID, which is generated after a configuration is added. This field is only required to modify or delete a configuration.
        :type Id: str
        :param _AreaList: This field is required when RegionType is `customized`; it can be left empty when RegionType is `china` or `oversea`.
        :type AreaList: list of int
        """
        self._RegionType = None
        self._Action = None
        self._Id = None
        self._AreaList = None

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AreaList(self):
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList


    def _deserialize(self, params):
        self._RegionType = params.get("RegionType")
        self._Action = params.get("Action")
        self._Id = params.get("Id")
        self._AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIpPolicyNew(AbstractModel):
    """Information of the policy list

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Domain: 
        :type Domain: str
        :param _Protocol: Protocol. Valid values: `HTTP` and `HTTPS`.
        :type Protocol: str
        :param _Action: Action. Valid values: `drop` and `alg`.
        :type Action: str
        :param _RegionType: Region type. Valid values: `china`, `oversea` and `customized`.
        :type RegionType: str
        :param _AreaList: ID list of regions to be blocked
        :type AreaList: list of int non-negative
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Action = None
        self._RegionType = None
        self._AreaList = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def AreaList(self):
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Action = params.get("Action")
        self._RegionType = params.get("RegionType")
        self._AreaList = params.get("AreaList")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdInsL7Rules(AbstractModel):
    """Set of rules configured for certificates

    """

    def __init__(self):
        r"""
        :param _L7Rules: List of rules configured for certificates
        :type L7Rules: list of InsL7Rules
        :param _CertId: Certificate ID
        :type CertId: str
        """
        self._L7Rules = None
        self._CertId = None

    @property
    def L7Rules(self):
        return self._L7Rules

    @L7Rules.setter
    def L7Rules(self, L7Rules):
        self._L7Rules = L7Rules

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        if params.get("L7Rules") is not None:
            self._L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self._L7Rules.append(obj)
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListRequest(AbstractModel):
    """CreateBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _IpList: List of IPs
        :type IpList: list of str
        :param _Type: IP type. Valid values: `black` (blocklisted IP), `white`(allowlisted IP).
        :type Type: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IpList = params.get("IpList")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListResponse(AbstractModel):
    """CreateBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP)
        :type Business: str
        :param _Id: Anti-DDoS instance ID
        :type Id: str
        :param _BoundDevList: Array of IPs to bind to the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, the array contains only one IP. If there are no IPs to bind, it is empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty.
        :type BoundDevList: list of BoundIpInfo
        :param _UnBoundDevList: Array of IPs to unbind from the Anti-DDoS instance. For Anti-DDoS Pro Single IP instance, the array contains only one IP; if there are no IPs to unbind, it is empty; however, either `BoundDevList` or `UnBoundDevList` must not be empty.
        :type UnBoundDevList: list of BoundIpInfo
        :param _CopyPolicy: Disused
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
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateCCPrecisionPolicyRequest(AbstractModel):
    """CreateCCPrecisionPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Protocol: Protocol. Valid values: `HTTP` and `HTTPS`.
        :type Protocol: str
        :param _Domain: Domain name
        :type Domain: str
        :param _PolicyAction: Action of limiting request frequency. Valid values: `alg` (limit request frequency via verification codes) and `drop`(drop requests).
        :type PolicyAction: str
        :param _PolicyList: Policy records
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._PolicyAction = None
        self._PolicyList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def PolicyAction(self):
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCPrecisionPolicyResponse(AbstractModel):
    """CreateCCPrecisionPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateCCReqLimitPolicyRequest(AbstractModel):
    """CreateCCReqLimitPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address
        :type Ip: str
        :param _Protocol: Protocol. Valid values: `HTTP` and `HTTPS`.
        :type Protocol: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Policy: Configuration field
        :type Policy: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        :param _IsGlobal: Whether it’s a global CC frequency limit
        :type IsGlobal: int
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Policy = None
        self._IsGlobal = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        if params.get("Policy") is not None:
            self._Policy = CCReqLimitPolicyRecord()
            self._Policy._deserialize(params.get("Policy"))
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCReqLimitPolicyResponse(AbstractModel):
    """CreateCCReqLimitPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateCcBlackWhiteIpListRequest(AbstractModel):
    """CreateCcBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IpList: List of IPs
        :type IpList: list of IpSegment
        :param _Type: IP permission. Valid values: `black` (blocked IP), `white` (allowed IP).
        :type Type: str
        :param _Ip: IP address
        :type Ip: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol
        :type Protocol: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcBlackWhiteIpListResponse(AbstractModel):
    """CreateCcBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateCcGeoIPBlockConfigRequest(AbstractModel):
    """CreateCcGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IP: IP address
        :type IP: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol type
        :type Protocol: str
        :param _CcGeoIPBlockConfig: CC regional blocking configuration
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._IP = None
        self._Domain = None
        self._Protocol = None
        self._CcGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CcGeoIPBlockConfig(self):
        return self._CcGeoIPBlockConfig

    @CcGeoIPBlockConfig.setter
    def CcGeoIPBlockConfig(self, CcGeoIPBlockConfig):
        self._CcGeoIPBlockConfig = CcGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IP = params.get("IP")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        if params.get("CcGeoIPBlockConfig") is not None:
            self._CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self._CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcGeoIPBlockConfigResponse(AbstractModel):
    """CreateCcGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateDDoSAIRequest(AbstractModel):
    """CreateDDoSAI request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdList: List of Anti-DDoS instance IDs
        :type InstanceIdList: list of str
        :param _DDoSAI: AI protection switch. Valid values:
`on`: enabled
`off`: disabled
]
        :type DDoSAI: str
        """
        self._InstanceIdList = None
        self._DDoSAI = None

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI


    def _deserialize(self, params):
        self._InstanceIdList = params.get("InstanceIdList")
        self._DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSAIResponse(AbstractModel):
    """CreateDDoSAI response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateDDoSGeoIPBlockConfigRequest(AbstractModel):
    """CreateDDoSGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: Region blocking configuration. The configuration ID should be cleared when you set this parameter.
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSGeoIPBlockConfigResponse(AbstractModel):
    """CreateDDoSGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateDDoSSpeedLimitConfigRequest(AbstractModel):
    """CreateDDoSSpeedLimitConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: Access rate limit configuration. The configuration ID should be cleared when you set this parameter.
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSSpeedLimitConfigResponse(AbstractModel):
    """CreateDDoSSpeedLimitConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateDefaultAlarmThresholdRequest(AbstractModel):
    """CreateDefaultAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _DefaultAlarmConfig: Default alarm threshold configuration
        :type DefaultAlarmConfig: :class:`tencentcloud.antiddos.v20200309.models.DefaultAlarmThreshold`
        :param _InstanceType: Product category. Valid values:
`bgp`: Anti-DDoS Pro
`bgpip`: Anti-DDoS Advanced
]
        :type InstanceType: str
        """
        self._DefaultAlarmConfig = None
        self._InstanceType = None

    @property
    def DefaultAlarmConfig(self):
        return self._DefaultAlarmConfig

    @DefaultAlarmConfig.setter
    def DefaultAlarmConfig(self, DefaultAlarmConfig):
        self._DefaultAlarmConfig = DefaultAlarmConfig

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfig") is not None:
            self._DefaultAlarmConfig = DefaultAlarmThreshold()
            self._DefaultAlarmConfig._deserialize(params.get("DefaultAlarmConfig"))
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultAlarmThresholdResponse(AbstractModel):
    """CreateDefaultAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateIPAlarmThresholdConfigRequest(AbstractModel):
    """CreateIPAlarmThresholdConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IpAlarmThresholdConfigList: List of IP alarm threshold configurations
        :type IpAlarmThresholdConfigList: list of IPAlarmThresholdRelation
        """
        self._IpAlarmThresholdConfigList = None

    @property
    def IpAlarmThresholdConfigList(self):
        return self._IpAlarmThresholdConfigList

    @IpAlarmThresholdConfigList.setter
    def IpAlarmThresholdConfigList(self, IpAlarmThresholdConfigList):
        self._IpAlarmThresholdConfigList = IpAlarmThresholdConfigList


    def _deserialize(self, params):
        if params.get("IpAlarmThresholdConfigList") is not None:
            self._IpAlarmThresholdConfigList = []
            for item in params.get("IpAlarmThresholdConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self._IpAlarmThresholdConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPAlarmThresholdConfigResponse(AbstractModel):
    """CreateIPAlarmThresholdConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateL7RuleCertsRequest(AbstractModel):
    """CreateL7RuleCerts request structure.

    """

    def __init__(self):
        r"""
        :param _CertId: SSL certificate ID
        :type CertId: str
        :param _L7Rules: List of Layer-7 domain name forwarding rules
        :type L7Rules: list of InsL7Rules
        """
        self._CertId = None
        self._L7Rules = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def L7Rules(self):
        return self._L7Rules

    @L7Rules.setter
    def L7Rules(self, L7Rules):
        self._L7Rules = L7Rules


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        if params.get("L7Rules") is not None:
            self._L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self._L7Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertsResponse(AbstractModel):
    """CreateL7RuleCerts response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Rules: List of rules
        :type Rules: list of L7RuleEntry
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _IdList: List of resource IDs
        :type IdList: list of str
        :param _VipList: List of resource IPs
        :type VipList: list of str
        """
        self._Rules = None
        self._Business = None
        self._IdList = None
        self._VipList = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

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


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Success: Success code
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreatePacketFilterConfigRequest(AbstractModel):
    """CreatePacketFilterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _PacketFilterConfig: Feature filtering rules
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePacketFilterConfigResponse(AbstractModel):
    """CreatePacketFilterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateProtocolBlockConfigRequest(AbstractModel):
    """CreateProtocolBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _ProtocolBlockConfig: Protocol blocking configuration
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        """
        self._InstanceId = None
        self._ProtocolBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProtocolBlockConfig(self):
        return self._ProtocolBlockConfig

    @ProtocolBlockConfig.setter
    def ProtocolBlockConfig(self, ProtocolBlockConfig):
        self._ProtocolBlockConfig = ProtocolBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ProtocolBlockConfig") is not None:
            self._ProtocolBlockConfig = ProtocolBlockConfig()
            self._ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtocolBlockConfigResponse(AbstractModel):
    """CreateProtocolBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateSchedulingDomainRequest(AbstractModel):
    """CreateSchedulingDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Indicates whether a hybrid cloud product is used.
`hybrid`: Anti-DDoS Service Platform
For other products, leave this field empty.
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulingDomainResponse(AbstractModel):
    """CreateSchedulingDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Created domain name
        :type Domain: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domain = None
        self._RequestId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class CreateWaterPrintConfigRequest(AbstractModel):
    """CreateWaterPrintConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _WaterPrintConfig: Watermark configuration
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        """
        self._InstanceId = None
        self._WaterPrintConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WaterPrintConfig(self):
        return self._WaterPrintConfig

    @WaterPrintConfig.setter
    def WaterPrintConfig(self, WaterPrintConfig):
        self._WaterPrintConfig = WaterPrintConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WaterPrintConfig") is not None:
            self._WaterPrintConfig = WaterPrintConfig()
            self._WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintConfigResponse(AbstractModel):
    """CreateWaterPrintConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateWaterPrintKeyRequest(AbstractModel):
    """CreateWaterPrintKey request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintKeyResponse(AbstractModel):
    """CreateWaterPrintKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DDoSAIRelation(AbstractModel):
    """Anti-DDoS AI protection switch

    """

    def __init__(self):
        r"""
        :param _DDoSAI: AI protection switch. Valid values:
`on`: enabled
`off`: disabled
]
        :type DDoSAI: str
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._DDoSAI = None
        self._InstanceDetailList = None

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        self._DDoSAI = params.get("DDoSAI")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfig(AbstractModel):
    """Anti-DDoS region blocking configuration

    """

    def __init__(self):
        r"""
        :param _RegionType: Region type. Valid values:
`oversea`: Outside the Chinese mainland
`china`: The Chinese mainland
`customized`: User-specified region
]
        :type RegionType: str
        :param _Action: Blocking action. Valid values:
`drop`: the request is blocked.
`trans`: the request is allowed.
]
        :type Action: str
        :param _Id: Configuration ID, which is generated after a configuration is added. This field is only required to modify or delete a configuration.
        :type Id: str
        :param _AreaList: When `RegionType = customized`, AreaList is required and contains up to 128 areas.
        :type AreaList: list of int
        """
        self._RegionType = None
        self._Action = None
        self._Id = None
        self._AreaList = None

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AreaList(self):
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList


    def _deserialize(self, params):
        self._RegionType = params.get("RegionType")
        self._Action = params.get("Action")
        self._Id = params.get("Id")
        self._AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfigRelation(AbstractModel):
    """Anti-DDoS region blocking configuration details

    """

    def __init__(self):
        r"""
        :param _GeoIPBlockConfig: Anti-DDoS region blocking configuration
        :type GeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._GeoIPBlockConfig = None
        self._InstanceDetailList = None

    @property
    def GeoIPBlockConfig(self):
        return self._GeoIPBlockConfig

    @GeoIPBlockConfig.setter
    def GeoIPBlockConfig(self, GeoIPBlockConfig):
        self._GeoIPBlockConfig = GeoIPBlockConfig

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("GeoIPBlockConfig") is not None:
            self._GeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._GeoIPBlockConfig._deserialize(params.get("GeoIPBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfig(AbstractModel):
    """Anti-DDoS access rate limit configuration

    """

    def __init__(self):
        r"""
        :param _Mode: Rate limit mode. Valid values:
`1`: rate limit based on the real server IP
`2`: rate limit based on the destination port
]
        :type Mode: int
        :param _SpeedValues: Rate limit value. This field contains at least one valid rate limit type. Note that only up to one value of each type is supported.
        :type SpeedValues: list of SpeedValue
        :param _DstPortScopes: This field is replaced with a new field DstPortList.
        :type DstPortScopes: list of PortSegment
        :param _Id: 
        :type Id: str
        :param _ProtocolList: IP protocol number. Valid values:
`ALL`: all protocols
`TCP`: TCP protocol
`UDP`: UDP protocol
`SMP`: SMP protocol
`1;2–100`: user-defined protocol with up to 8 ranges
]
Note: For custom protocol ranges, only protocol number is supported. Multiple ranges are separated by ";". If the value is `ALL`, any other protocol or protocol number should be excluded.
        :type ProtocolList: str
        :param _DstPortList: Port range list, which contains up to 8 ranges. Use ";" to separate multiple ports and "–" to indicate a range of ports, as described in the following formats: `0–65535`, `80;443;1000–2000`.
        :type DstPortList: str
        """
        self._Mode = None
        self._SpeedValues = None
        self._DstPortScopes = None
        self._Id = None
        self._ProtocolList = None
        self._DstPortList = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SpeedValues(self):
        return self._SpeedValues

    @SpeedValues.setter
    def SpeedValues(self, SpeedValues):
        self._SpeedValues = SpeedValues

    @property
    def DstPortScopes(self):
        return self._DstPortScopes

    @DstPortScopes.setter
    def DstPortScopes(self, DstPortScopes):
        self._DstPortScopes = DstPortScopes

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProtocolList(self):
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def DstPortList(self):
        return self._DstPortList

    @DstPortList.setter
    def DstPortList(self, DstPortList):
        self._DstPortList = DstPortList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("SpeedValues") is not None:
            self._SpeedValues = []
            for item in params.get("SpeedValues"):
                obj = SpeedValue()
                obj._deserialize(item)
                self._SpeedValues.append(obj)
        if params.get("DstPortScopes") is not None:
            self._DstPortScopes = []
            for item in params.get("DstPortScopes"):
                obj = PortSegment()
                obj._deserialize(item)
                self._DstPortScopes.append(obj)
        self._Id = params.get("Id")
        self._ProtocolList = params.get("ProtocolList")
        self._DstPortList = params.get("DstPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfigRelation(AbstractModel):
    """DDoS access rate limit configuration details

    """

    def __init__(self):
        r"""
        :param _SpeedLimitConfig: Anti-DDoS access rate limit configuration
        :type SpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._SpeedLimitConfig = None
        self._InstanceDetailList = None

    @property
    def SpeedLimitConfig(self):
        return self._SpeedLimitConfig

    @SpeedLimitConfig.setter
    def SpeedLimitConfig(self, SpeedLimitConfig):
        self._SpeedLimitConfig = SpeedLimitConfig

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("SpeedLimitConfig") is not None:
            self._SpeedLimitConfig = DDoSSpeedLimitConfig()
            self._SpeedLimitConfig._deserialize(params.get("SpeedLimitConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultAlarmThreshold(AbstractModel):
    """Default alarm threshold configuration of an IP

    """

    def __init__(self):
        r"""
        :param _AlarmType: Alarm threshold type. Valid values:
`1`: alarm threshold for inbound traffic
`2`: alarm threshold for cleansing attack traffic
]
        :type AlarmType: int
        :param _AlarmThreshold: Alarm threshold (Mbps). The value should be greater than or equal to 0. Note that the alarm threshold configuration will be removed if you pass the parameter for input and set it to 0.
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
        


class DeleteCCLevelPolicyRequest(AbstractModel):
    """DeleteCCLevelPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: Target IP of the policy
        :type Ip: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Value: `http`
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCLevelPolicyResponse(AbstractModel):
    """DeleteCCLevelPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteCCPrecisionPolicyRequest(AbstractModel):
    """DeleteCCPrecisionPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        """
        self._InstanceId = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCPrecisionPolicyResponse(AbstractModel):
    """DeleteCCPrecisionPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteCCThresholdPolicyRequest(AbstractModel):
    """DeleteCCThresholdPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: Target IP of the policy
        :type Ip: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Value: `http`
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCThresholdPolicyResponse(AbstractModel):
    """DeleteCCThresholdPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteCcBlackWhiteIpListRequest(AbstractModel):
    """DeleteCcBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        """
        self._InstanceId = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcBlackWhiteIpListResponse(AbstractModel):
    """DeleteCcBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteCcGeoIPBlockConfigRequest(AbstractModel):
    """DeleteCcGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _CcGeoIPBlockConfig: Region blocking configuration. The configuration ID cannot be empty when you set this parameter.
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._CcGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CcGeoIPBlockConfig(self):
        return self._CcGeoIPBlockConfig

    @CcGeoIPBlockConfig.setter
    def CcGeoIPBlockConfig(self, CcGeoIPBlockConfig):
        self._CcGeoIPBlockConfig = CcGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("CcGeoIPBlockConfig") is not None:
            self._CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self._CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcGeoIPBlockConfigResponse(AbstractModel):
    """DeleteCcGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: Region blocking configuration. The configuration ID cannot be empty when you set this parameter.
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteDDoSSpeedLimitConfigRequest(AbstractModel):
    """DeleteDDoSSpeedLimitConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: Access rate limit configuration. The configuration ID cannot be empty when you set this parameter.
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSSpeedLimitConfigResponse(AbstractModel):
    """DeleteDDoSSpeedLimitConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeletePacketFilterConfigRequest(AbstractModel):
    """DeletePacketFilterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _PacketFilterConfig: Feature filtering configuration
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePacketFilterConfigResponse(AbstractModel):
    """DeletePacketFilterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteWaterPrintConfigRequest(AbstractModel):
    """DeleteWaterPrintConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintConfigResponse(AbstractModel):
    """DeleteWaterPrintConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteWaterPrintKeyRequest(AbstractModel):
    """DeleteWaterPrintKey request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _KeyId: Watermark key ID
        :type KeyId: str
        """
        self._InstanceId = None
        self._KeyId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintKeyResponse(AbstractModel):
    """DeleteWaterPrintKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeBasicDeviceStatusRequest(AbstractModel):
    """DescribeBasicDeviceStatus request structure.

    """

    def __init__(self):
        r"""
        :param _IpList: List of IP resources
        :type IpList: list of str
        :param _IdList: 
        :type IdList: list of str
        :param _FilterRegion: 
        :type FilterRegion: int
        :param _CnameWafIdList: 
        :type CnameWafIdList: list of str
        """
        self._IpList = None
        self._IdList = None
        self._FilterRegion = None
        self._CnameWafIdList = None

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def FilterRegion(self):
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def CnameWafIdList(self):
        return self._CnameWafIdList

    @CnameWafIdList.setter
    def CnameWafIdList(self, CnameWafIdList):
        self._CnameWafIdList = CnameWafIdList


    def _deserialize(self, params):
        self._IpList = params.get("IpList")
        self._IdList = params.get("IdList")
        self._FilterRegion = params.get("FilterRegion")
        self._CnameWafIdList = params.get("CnameWafIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceStatusResponse(AbstractModel):
    """DescribeBasicDeviceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Status of the specified Anti-DDoS resource. Valid values:
`1`: The IP is blocked.
`2`: The P is normal.
`3`: The IP is being attacked.
        :type Data: list of KeyValue
        :param _CLBData: 
        :type CLBData: list of KeyValue
        :param _CnameWafData: 
        :type CnameWafData: list of KeyValue
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CLBData = None
        self._CnameWafData = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CLBData(self):
        return self._CLBData

    @CLBData.setter
    def CLBData(self, CLBData):
        self._CLBData = CLBData

    @property
    def CnameWafData(self):
        return self._CnameWafData

    @CnameWafData.setter
    def CnameWafData(self, CnameWafData):
        self._CnameWafData = CnameWafData

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
        if params.get("CLBData") is not None:
            self._CLBData = []
            for item in params.get("CLBData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._CLBData.append(obj)
        if params.get("CnameWafData") is not None:
            self._CnameWafData = []
            for item in params.get("CnameWafData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._CnameWafData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBgpBizTrendRequest(AbstractModel):
    """DescribeBgpBizTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service code. `bgp-multip` indicates Anti-DDos Pro.
        :type Business: str
        :param _StartTime: Beginning of the time range for the query, such as `2020-09-22 00:00:00`.
        :type StartTime: str
        :param _EndTime: End of the time range for the query, such as `2020-09-22 00:00:00`.
        :type EndTime: str
        :param _MetricName: Statistical metric. Values: `intraffic`, `outtraffic`, `inpkg`, and `outpkg`.
        :type MetricName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Flag: `0`: Fixed time. `1`: Custom time.
        :type Flag: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._InstanceId = None
        self._Flag = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._InstanceId = params.get("InstanceId")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBgpBizTrendResponse(AbstractModel):
    """DescribeBgpBizTrend response structure.

    """

    def __init__(self):
        r"""
        :param _DataList: Values of the samples
        :type DataList: list of int non-negative
        :param _Total: Number of samples
        :type Total: int
        :param _MetricName: Statistical metric
        :type MetricName: str
        :param _MaxData: Maximum value of the arrays returned
        :type MaxData: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataList = None
        self._Total = None
        self._MetricName = None
        self._MaxData = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MaxData(self):
        return self._MaxData

    @MaxData.setter
    def MaxData(self, MaxData):
        self._MaxData = MaxData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataList = params.get("DataList")
        self._Total = params.get("Total")
        self._MetricName = params.get("MetricName")
        self._MaxData = params.get("MaxData")
        self._RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Statistics: Statistical mode. Value: `sum`.
        :type Statistics: str
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _Period: Statistical period in seconds. Valid values: `60`, `300`, `1800`, `3600`, `21600`, and `86400`.
        :type Period: int
        :param _StartTime: Statistics start time, such as `2020-02-01 12:04:12`
        :type StartTime: str
        :param _EndTime: Statistics end time, such as `2020-02-03 18:03:23`
        :type EndTime: str
        :param _Id: The resource ID.
        :type Id: str
        :param _Domain: Specific domain name query
        :type Domain: str
        :param _ProtoInfo: Protocol and port list, which is valid when the metric is `connum`, `new_conn` or `inactive_conn`. Valid protocols: `TCP`, `UDP`, `HTTP`, `HTTPS`
        :type ProtoInfo: list of ProtocolPort
        """
        self._Statistics = None
        self._Business = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._Domain = None
        self._ProtoInfo = None

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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

    @property
    def ProtoInfo(self):
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo


    def _deserialize(self, params):
        self._Statistics = params.get("Statistics")
        self._Business = params.get("Business")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
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
        :type HttpStatusMap: :class:`tencentcloud.antiddos.v20200309.models.HttpStatusMap`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeBizTrendRequest(AbstractModel):
    """DescribeBizTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Statistics: Statistical method. Valid values: `max`, `min`, `avg`, `sum`. It can only be `max` if the statistical dimension is traffic rate or packet rate.
        :type Statistics: str
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _Period: Sampling interval in seconds. Valid values: `60`, `300`, `1800`, `3600`, `21600`, `86400`
        :type Period: int
        :param _StartTime: Beginning of the time range for the query, such as `2020-09-22 00:00:00`.
        :type StartTime: str
        :param _EndTime: End of the time range for the query, such as `2020-09-22 00:00:00`.
        :type EndTime: str
        :param _Id: Instance ID
        :type Id: str
        :param _MetricName: Metric. Valid values: `connum`, `new_conn`, `inactive_conn`, `intraffic`, `outtraffic`, `inpkg`, `outpkg`, `qps`
        :type MetricName: str
        :param _Domain: You can query data by specifying a domain name when the metric is `qps`.
        :type Domain: str
        :param _ProtoInfo: Protocol and port list, which is valid when the metric is `connum`, `new_conn` or `inactive_conn`. Valid protocols: `TCP`, `UDP`, `HTTP`, `HTTPS`
        :type ProtoInfo: list of ProtocolPort
        """
        self._Statistics = None
        self._Business = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._MetricName = None
        self._Domain = None
        self._ProtoInfo = None

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtoInfo(self):
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo


    def _deserialize(self, params):
        self._Statistics = params.get("Statistics")
        self._Business = params.get("Business")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Domain = params.get("Domain")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizTrendResponse(AbstractModel):
    """DescribeBizTrend response structure.

    """

    def __init__(self):
        r"""
        :param _DataList: Value at a time point on the curve
        :type DataList: list of float
        :param _MetricName: Statistical dimension
        :type MetricName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataList = None
        self._MetricName = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

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
        self._DataList = params.get("DataList")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeBlackWhiteIpListRequest(AbstractModel):
    """DescribeBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlackWhiteIpListResponse(AbstractModel):
    """DescribeBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _BlackIpList: IP blocklist
        :type BlackIpList: list of str
        :param _WhiteIpList: IP allowlist
        :type WhiteIpList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlackIpList = None
        self._WhiteIpList = None
        self._RequestId = None

    @property
    def BlackIpList(self):
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlackIpList = params.get("BlackIpList")
        self._WhiteIpList = params.get("WhiteIpList")
        self._RequestId = params.get("RequestId")


class DescribeCCLevelListRequest(AbstractModel):
    """DescribeCCLevelList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service code. `bgp-multip` indicates Anti-DDos Pro.
        :type Business: str
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of results returned in one page
        :type Limit: int
        :param _InstanceId: ID of the specified instance
        :type InstanceId: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelListResponse(AbstractModel):
    """DescribeCCLevelList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of level-defining policies
        :type Total: int
        :param _LevelList: Total number of level-defining policies
        :type LevelList: list of CCLevelPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._LevelList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def LevelList(self):
        return self._LevelList

    @LevelList.setter
    def LevelList(self, LevelList):
        self._LevelList = LevelList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("LevelList") is not None:
            self._LevelList = []
            for item in params.get("LevelList"):
                obj = CCLevelPolicy()
                obj._deserialize(item)
                self._LevelList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCLevelPolicyRequest(AbstractModel):
    """DescribeCCLevelPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP
        :type Ip: str
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol. Values: `HTTP`，`HTTPS`
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelPolicyResponse(AbstractModel):
    """DescribeCCLevelPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Level: CC protection level. Vaules: `loose`, `strict`, `normal`, `emergency`, `sup_loose` (super loose), `default` (used when the frequency limit is not configured) and `customized`
        :type Level: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Level = None
        self._RequestId = None

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._RequestId = params.get("RequestId")


class DescribeCCPrecisionPlyListRequest(AbstractModel):
    """DescribeCCPrecisionPlyList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. Valid values: `bgpip-multip` (Anti-DDoS Pro) and `bgpip` (Anti-DDoS Advanced).
        :type Business: str
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of results returned in one page
        :type Limit: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address, which is required when an Anti-DDoS Advanced instance is used.
        :type Ip: str
        :param _Domain: Domain name, which is required when an Anti-DDoS Advanced instance is used.
        :type Domain: str
        :param _Protocol: Protocol, which is required when an Anti-DDoS Advanced instance is used.
        :type Protocol: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCPrecisionPlyListResponse(AbstractModel):
    """DescribeCCPrecisionPlyList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of policy lists
        :type Total: int
        :param _PrecisionPolicyList: Information of the policy list
        :type PrecisionPolicyList: list of CCPrecisionPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._PrecisionPolicyList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PrecisionPolicyList(self):
        return self._PrecisionPolicyList

    @PrecisionPolicyList.setter
    def PrecisionPolicyList(self, PrecisionPolicyList):
        self._PrecisionPolicyList = PrecisionPolicyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("PrecisionPolicyList") is not None:
            self._PrecisionPolicyList = []
            for item in params.get("PrecisionPolicyList"):
                obj = CCPrecisionPolicy()
                obj._deserialize(item)
                self._PrecisionPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCThresholdListRequest(AbstractModel):
    """DescribeCCThresholdList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service code. `bgp-multip` indicates Anti-DDos Pro.
        :type Business: str
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of results returned in one page
        :type Limit: int
        :param _InstanceId: ID of the specified instance
        :type InstanceId: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCThresholdListResponse(AbstractModel):
    """DescribeCCThresholdList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of cleansing threshold policies
        :type Total: int
        :param _ThresholdList: Details of cleansing threshold policies
        :type ThresholdList: list of CCThresholdPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ThresholdList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ThresholdList(self):
        return self._ThresholdList

    @ThresholdList.setter
    def ThresholdList(self, ThresholdList):
        self._ThresholdList = ThresholdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ThresholdList") is not None:
            self._ThresholdList = []
            for item in params.get("ThresholdList"):
                obj = CCThresholdPolicy()
                obj._deserialize(item)
                self._ThresholdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Instance IP
        :type Ip: str
        :param _Period: Sampling period. Valid values: `300` (5 minutes), `3600` (one hour), `86400` (one day)
        :type Period: int
        :param _StartTime: Beginning of the time range for the query
        :type StartTime: str
        :param _EndTime: End of the time range for the query
        :type EndTime: str
        :param _MetricName: Metric. Valid values: `inqps` (total QPS peaks), `dropqps` (attack QPS peaks), `incount` (total number of requests), and `dropcount` (number of attack requests).
        :type MetricName: str
        :param _Domain: (Optional) Domain name
        :type Domain: str
        :param _Id: Instance ID. Leave this field empty when `Business` is `basic`, as basic protection does not require an instance.
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Domain = None
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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
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
        :param _Count: Number of values returned
        :type Count: int
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Instance IP
        :type Ip: str
        :param _Period: Sampling period. Valid values: `300` (5 minutes), `3600` (one hour), `86400` (one day)
        :type Period: int
        :param _StartTime: Beginning of the time range for the query
        :type StartTime: str
        :param _EndTime: End of the time range for the query
        :type EndTime: str
        :param _Data: Value array
        :type Data: list of int non-negative
        :param _Id: Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Id: str
        :param _MetricName: Metric. Valid values: `inqps` (total QPS peaks), `dropqps` (attack QPS peaks), `incount` (total number of requests), and `dropcount` (number of attack requests).
        :type MetricName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Id = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeCcBlackWhiteIpListRequest(AbstractModel):
    """DescribeCcBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. Valid values: `bgpip-multip` (Anti-DDoS Pro) and `bgpip` (Anti-DDoS Advanced).
        :type Business: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of results returned in one page
        :type Limit: int
        :param _Ip: IP address, which is required when an Anti-DDoS Advanced instance is used.
        :type Ip: str
        :param _Domain: Domain name, which is required when an Anti-DDoS Advanced instance is used.
        :type Domain: str
        :param _Protocol: Protocol, which is required when an Anti-DDoS Advanced instance is used.
        :type Protocol: str
        :param _FilterIp: Specifies a blocklist/allowlist IP.
        :type FilterIp: str
        :param _FilterType: Specifies whether is an IP blocklist or IP allowlist.
        :type FilterType: str
        """
        self._Business = None
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._FilterIp = None
        self._FilterType = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._FilterIp = params.get("FilterIp")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcBlackWhiteIpListResponse(AbstractModel):
    """DescribeCcBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of policy lists
        :type Total: int
        :param _CcBlackWhiteIpList: Information of the policy list
        :type CcBlackWhiteIpList: list of CcBlackWhiteIpPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._CcBlackWhiteIpList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CcBlackWhiteIpList(self):
        return self._CcBlackWhiteIpList

    @CcBlackWhiteIpList.setter
    def CcBlackWhiteIpList(self, CcBlackWhiteIpList):
        self._CcBlackWhiteIpList = CcBlackWhiteIpList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CcBlackWhiteIpList") is not None:
            self._CcBlackWhiteIpList = []
            for item in params.get("CcBlackWhiteIpList"):
                obj = CcBlackWhiteIpPolicy()
                obj._deserialize(item)
                self._CcBlackWhiteIpList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCcGeoIPBlockConfigListRequest(AbstractModel):
    """DescribeCcGeoIPBlockConfigList request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. Valid values: `bgpip-multip` (Anti-DDoS Pro) and `bgpip` (Anti-DDoS Advanced).
        :type Business: str
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of results returned in one page
        :type Limit: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ip: IP address, which is required when an Anti-DDoS Advanced instance is used.
        :type Ip: str
        :param _Domain: Domain name, which is required when an Anti-DDoS Advanced instance is used.
        :type Domain: str
        :param _Protocol: Protocol, which is required when an Anti-DDoS Advanced instance is used.
        :type Protocol: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcGeoIPBlockConfigListResponse(AbstractModel):
    """DescribeCcGeoIPBlockConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of policy lists
        :type Total: int
        :param _CcGeoIpPolicyList: Information of the policy list
        :type CcGeoIpPolicyList: list of CcGeoIpPolicyNew
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._CcGeoIpPolicyList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CcGeoIpPolicyList(self):
        return self._CcGeoIpPolicyList

    @CcGeoIpPolicyList.setter
    def CcGeoIpPolicyList(self, CcGeoIpPolicyList):
        self._CcGeoIpPolicyList = CcGeoIpPolicyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CcGeoIpPolicyList") is not None:
            self._CcGeoIpPolicyList = []
            for item in params.get("CcGeoIpPolicyList"):
                obj = CcGeoIpPolicyNew()
                obj._deserialize(item)
                self._CcGeoIpPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Instance IP
        :type Ip: str
        :param _Period: Sampling period. Valid values: `300` (5 minutes), `3600` (one hour), `86400` (one day)
        :type Period: int
        :param _StartTime: Beginning of the time range for the query
        :type StartTime: str
        :param _EndTime: End of the time range for the query
        :type EndTime: str
        :param _MetricName: Metric. Valid values: `bps`: attack traffic bandwidth; `pps`: attack packet rate
        :type MetricName: str
        :param _Id: Instance ID. Leave this field empty when `Business` is `basic`, as basic protection does not require an instance.
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
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
        :param _Count: Number of values returned
        :type Count: int
        :param _Business: Anti-DDoS service type. `bgpip`: Anti-DDoS Advanced; `bgp`: Anti-DDoS Pro (Single IP); `bgp-multip`: Anti-DDoS Pro (Multi-IP); `net`: Anti-DDoS Ultimate; `basic`: Anti-DDoS Basic
        :type Business: str
        :param _Ip: Instance IP
        :type Ip: str
        :param _Period: Sampling period. Valid values: `300` (5 minutes), `3600` (one hour), `86400` (one day)
        :type Period: int
        :param _StartTime: Beginning of the time range for the query
        :type StartTime: str
        :param _EndTime: End of the time range for the query
        :type EndTime: str
        :param _Data: Value array. The unit for attack traffic bandwidth is Mbps, and that for the packet rate is pps.
        :type Data: list of int non-negative
        :param _Id: Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Id: str
        :param _MetricName: Metric. Valid values: `bps`: attack traffic bandwidth; `pps`: attack packet rate
        :type MetricName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Id = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeDefaultAlarmThresholdRequest(AbstractModel):
    """DescribeDefaultAlarmThreshold request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Product category. Valid values:
`bgp`: Anti-DDoS Pro
`bgpip`: Anti-DDoS Advanced
]
        :type InstanceType: str
        :param _FilterAlarmType: Alarm threshold type filter. Valid values:
`1`: alarm threshold for inbound traffic
`2`: alarm threshold for cleansing attack traffic
]
        :type FilterAlarmType: int
        """
        self._InstanceType = None
        self._FilterAlarmType = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def FilterAlarmType(self):
        return self._FilterAlarmType

    @FilterAlarmType.setter
    def FilterAlarmType(self, FilterAlarmType):
        self._FilterAlarmType = FilterAlarmType


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._FilterAlarmType = params.get("FilterAlarmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultAlarmThresholdResponse(AbstractModel):
    """DescribeDefaultAlarmThreshold response structure.

    """

    def __init__(self):
        r"""
        :param _DefaultAlarmConfigList: Default alarm threshold configuration
        :type DefaultAlarmConfigList: list of DefaultAlarmThreshold
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DefaultAlarmConfigList = None
        self._RequestId = None

    @property
    def DefaultAlarmConfigList(self):
        return self._DefaultAlarmConfigList

    @DefaultAlarmConfigList.setter
    def DefaultAlarmConfigList(self, DefaultAlarmConfigList):
        self._DefaultAlarmConfigList = DefaultAlarmConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfigList") is not None:
            self._DefaultAlarmConfigList = []
            for item in params.get("DefaultAlarmConfigList"):
                obj = DefaultAlarmThreshold()
                obj._deserialize(item)
                self._DefaultAlarmConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList request structure.

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList response structure.

    """

    def __init__(self):
        r"""
        :param _List: IP block list
        :type List: list of IpBlockData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeL7RulesBySSLCertIdRequest(AbstractModel):
    """DescribeL7RulesBySSLCertId request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Domain name status. Valid values: `bindable`, `binded`, `opened`, `closed`, `all` (all states).
        :type Status: str
        :param _CertIds: List of certificate IDs
        :type CertIds: list of str
        """
        self._Status = None
        self._CertIds = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertIds(self):
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7RulesBySSLCertIdResponse(AbstractModel):
    """DescribeL7RulesBySSLCertId response structure.

    """

    def __init__(self):
        r"""
        :param _CertSet: Certificate rule set
        :type CertSet: list of CertIdInsL7Rules
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = CertIdInsL7Rules()
                obj._deserialize(item)
                self._CertSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBGPIPInstancesRequest(AbstractModel):
    """DescribeListBGPIPInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterIp: IP filter
        :type FilterIp: str
        :param _FilterInstanceId: Anti-DDoS instance ID filter. For example, you can filter the Anti-DDoS Advanced instance ID by `bgpip-00000001`.
        :type FilterInstanceId: str
        :param _FilterLine: Anti-DDoS Advanced line filter. Valid values:
`1`: BGP line
`2`: China Telecom
`3`: China Unicom
`4`: China Mobile
`99`: third-party line
]
        :type FilterLine: int
        :param _FilterRegion: Region filter. For example, `ap-guangzhou`.
        :type FilterRegion: str
        :param _FilterName: Name filter
        :type FilterName: str
        :param _FilterEipType: Whether to obtain only Anti-DDoS EIP instances. `1`: Yes; `0`: No.
        :type FilterEipType: int
        :param _FilterEipEipAddressStatus: Anti-DDoS Advanced instance binding status filter. Valid values: `BINDING`, `BIND`, `UNBINDING`, `UNBIND`. This filter is only valid when `FilterEipType = 1`.
        :type FilterEipEipAddressStatus: list of str
        :param _FilterDamDDoSStatus: Whether to obtain only Anti-DDoS instances with Sec-MCA enabled. Valid values: `1` (only obtain Anti-DDoS instances with Sec-MCA enabled) and `0` (obtain other Anti-DDoS instances).
        :type FilterDamDDoSStatus: int
        :param _FilterStatus: Filters by the status of bound resources. Values: `idle` (normal), `attacking` (being attacked), `blocking` (being blocked), `trial` (in trial)
        :type FilterStatus: str
        :param _FilterCname: Filters by the instance CNAME
        :type FilterCname: str
        :param _FilterInstanceIdList: Filters by the instance ID
        :type FilterInstanceIdList: list of str
        :param _FilterTag: Searches by tag
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        :param _FilterPackType: Filters by package type.
        :type FilterPackType: list of str
        :param _FilterConvoy: Filters out Convoy instances
        :type FilterConvoy: int
        """
        self._Offset = None
        self._Limit = None
        self._FilterIp = None
        self._FilterInstanceId = None
        self._FilterLine = None
        self._FilterRegion = None
        self._FilterName = None
        self._FilterEipType = None
        self._FilterEipEipAddressStatus = None
        self._FilterDamDDoSStatus = None
        self._FilterStatus = None
        self._FilterCname = None
        self._FilterInstanceIdList = None
        self._FilterTag = None
        self._FilterPackType = None
        self._FilterConvoy = None

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
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterLine(self):
        return self._FilterLine

    @FilterLine.setter
    def FilterLine(self, FilterLine):
        self._FilterLine = FilterLine

    @property
    def FilterRegion(self):
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def FilterName(self):
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterEipType(self):
        return self._FilterEipType

    @FilterEipType.setter
    def FilterEipType(self, FilterEipType):
        self._FilterEipType = FilterEipType

    @property
    def FilterEipEipAddressStatus(self):
        return self._FilterEipEipAddressStatus

    @FilterEipEipAddressStatus.setter
    def FilterEipEipAddressStatus(self, FilterEipEipAddressStatus):
        self._FilterEipEipAddressStatus = FilterEipEipAddressStatus

    @property
    def FilterDamDDoSStatus(self):
        return self._FilterDamDDoSStatus

    @FilterDamDDoSStatus.setter
    def FilterDamDDoSStatus(self, FilterDamDDoSStatus):
        self._FilterDamDDoSStatus = FilterDamDDoSStatus

    @property
    def FilterStatus(self):
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def FilterCname(self):
        return self._FilterCname

    @FilterCname.setter
    def FilterCname(self, FilterCname):
        self._FilterCname = FilterCname

    @property
    def FilterInstanceIdList(self):
        return self._FilterInstanceIdList

    @FilterInstanceIdList.setter
    def FilterInstanceIdList(self, FilterInstanceIdList):
        self._FilterInstanceIdList = FilterInstanceIdList

    @property
    def FilterTag(self):
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def FilterPackType(self):
        return self._FilterPackType

    @FilterPackType.setter
    def FilterPackType(self, FilterPackType):
        self._FilterPackType = FilterPackType

    @property
    def FilterConvoy(self):
        return self._FilterConvoy

    @FilterConvoy.setter
    def FilterConvoy(self, FilterConvoy):
        self._FilterConvoy = FilterConvoy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterIp = params.get("FilterIp")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterLine = params.get("FilterLine")
        self._FilterRegion = params.get("FilterRegion")
        self._FilterName = params.get("FilterName")
        self._FilterEipType = params.get("FilterEipType")
        self._FilterEipEipAddressStatus = params.get("FilterEipEipAddressStatus")
        self._FilterDamDDoSStatus = params.get("FilterDamDDoSStatus")
        self._FilterStatus = params.get("FilterStatus")
        self._FilterCname = params.get("FilterCname")
        self._FilterInstanceIdList = params.get("FilterInstanceIdList")
        if params.get("FilterTag") is not None:
            self._FilterTag = TagFilter()
            self._FilterTag._deserialize(params.get("FilterTag"))
        self._FilterPackType = params.get("FilterPackType")
        self._FilterConvoy = params.get("FilterConvoy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPIPInstancesResponse(AbstractModel):
    """DescribeListBGPIPInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _InstanceList: List of Anti-DDoS Advanced instances
        :type InstanceList: list of BGPIPInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPIPInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBGPInstancesRequest(AbstractModel):
    """DescribeListBGPInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterIp: Filters by IP.
        :type FilterIp: str
        :param _FilterInstanceId: Anti-DDoS instance ID filter. For example, `bgp-00000001`.
        :type FilterInstanceId: str
        :param _FilterRegion: Filters by region. For example, `ap-guangzhou`.
        :type FilterRegion: str
        :param _FilterName: Filters by name.
        :type FilterName: str
        :param _FilterLine: Line filter. Valid values: 1: BGP; 2: Non-BGP.
        :type FilterLine: int
        :param _FilterStatus: Filters by instance status. `idle`: Running; `attacking`: Being attacked; `blocking`: Being blocked.
        :type FilterStatus: str
        :param _FilterBoundStatus: Filters by binding status. `bounding`: The instance is bound; `failed`: The binding failed.
        :type FilterBoundStatus: str
        :param _FilterInstanceIdList: Array of instance IDs
        :type FilterInstanceIdList: list of str
        :param _FilterEnterpriseFlag: Enterprise edition. Values: `1` (the Convoy package included), `2` (the Convoy package not included)
        :type FilterEnterpriseFlag: int
        :param _FilterLightFlag: Whether it’s a Lighthouse edition
        :type FilterLightFlag: int
        :param _FilterChannelFlag: Whether it’s a Channel edition
        :type FilterChannelFlag: int
        :param _FilterTag: Filters by tag
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        :param _FilterTrialFlag: Filters out trial instances. Values: `1` (emergency protection instances), `2` (PLG instances)
        :type FilterTrialFlag: int
        :param _FilterConvoy: Filters out Convoy instances
        :type FilterConvoy: int
        :param _ExcludeAdvancedInfo: Whether to exclude the advanced information (such as `InstanceList[0].Usage`). Values: `true` (exclude), `false` (do not exclude). The default value is `false`.
        :type ExcludeAdvancedInfo: bool
        """
        self._Offset = None
        self._Limit = None
        self._FilterIp = None
        self._FilterInstanceId = None
        self._FilterRegion = None
        self._FilterName = None
        self._FilterLine = None
        self._FilterStatus = None
        self._FilterBoundStatus = None
        self._FilterInstanceIdList = None
        self._FilterEnterpriseFlag = None
        self._FilterLightFlag = None
        self._FilterChannelFlag = None
        self._FilterTag = None
        self._FilterTrialFlag = None
        self._FilterConvoy = None
        self._ExcludeAdvancedInfo = None

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
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterRegion(self):
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def FilterName(self):
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterLine(self):
        return self._FilterLine

    @FilterLine.setter
    def FilterLine(self, FilterLine):
        self._FilterLine = FilterLine

    @property
    def FilterStatus(self):
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def FilterBoundStatus(self):
        return self._FilterBoundStatus

    @FilterBoundStatus.setter
    def FilterBoundStatus(self, FilterBoundStatus):
        self._FilterBoundStatus = FilterBoundStatus

    @property
    def FilterInstanceIdList(self):
        return self._FilterInstanceIdList

    @FilterInstanceIdList.setter
    def FilterInstanceIdList(self, FilterInstanceIdList):
        self._FilterInstanceIdList = FilterInstanceIdList

    @property
    def FilterEnterpriseFlag(self):
        return self._FilterEnterpriseFlag

    @FilterEnterpriseFlag.setter
    def FilterEnterpriseFlag(self, FilterEnterpriseFlag):
        self._FilterEnterpriseFlag = FilterEnterpriseFlag

    @property
    def FilterLightFlag(self):
        return self._FilterLightFlag

    @FilterLightFlag.setter
    def FilterLightFlag(self, FilterLightFlag):
        self._FilterLightFlag = FilterLightFlag

    @property
    def FilterChannelFlag(self):
        return self._FilterChannelFlag

    @FilterChannelFlag.setter
    def FilterChannelFlag(self, FilterChannelFlag):
        self._FilterChannelFlag = FilterChannelFlag

    @property
    def FilterTag(self):
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def FilterTrialFlag(self):
        return self._FilterTrialFlag

    @FilterTrialFlag.setter
    def FilterTrialFlag(self, FilterTrialFlag):
        self._FilterTrialFlag = FilterTrialFlag

    @property
    def FilterConvoy(self):
        return self._FilterConvoy

    @FilterConvoy.setter
    def FilterConvoy(self, FilterConvoy):
        self._FilterConvoy = FilterConvoy

    @property
    def ExcludeAdvancedInfo(self):
        return self._ExcludeAdvancedInfo

    @ExcludeAdvancedInfo.setter
    def ExcludeAdvancedInfo(self, ExcludeAdvancedInfo):
        self._ExcludeAdvancedInfo = ExcludeAdvancedInfo


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterIp = params.get("FilterIp")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterRegion = params.get("FilterRegion")
        self._FilterName = params.get("FilterName")
        self._FilterLine = params.get("FilterLine")
        self._FilterStatus = params.get("FilterStatus")
        self._FilterBoundStatus = params.get("FilterBoundStatus")
        self._FilterInstanceIdList = params.get("FilterInstanceIdList")
        self._FilterEnterpriseFlag = params.get("FilterEnterpriseFlag")
        self._FilterLightFlag = params.get("FilterLightFlag")
        self._FilterChannelFlag = params.get("FilterChannelFlag")
        if params.get("FilterTag") is not None:
            self._FilterTag = TagFilter()
            self._FilterTag._deserialize(params.get("FilterTag"))
        self._FilterTrialFlag = params.get("FilterTrialFlag")
        self._FilterConvoy = params.get("FilterConvoy")
        self._ExcludeAdvancedInfo = params.get("ExcludeAdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPInstancesResponse(AbstractModel):
    """DescribeListBGPInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of Anti-DDoS Pro instances
        :type Total: int
        :param _InstanceList: List of Anti-DDoS Pro instances
        :type InstanceList: list of BGPInstance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBlackWhiteIpListRequest(AbstractModel):
    """DescribeListBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBlackWhiteIpListResponse(AbstractModel):
    """DescribeListBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _IpList: IP blocklist/allowlist
        :type IpList: list of BlackWhiteIpRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._IpList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = BlackWhiteIpRelation()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSAIRequest(AbstractModel):
    """DescribeListDDoSAI request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSAIResponse(AbstractModel):
    """DescribeListDDoSAI response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of AI protection switches
        :type ConfigList: list of DDoSAIRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSAIRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of Anti-DDoS region blocking configurations
        :type ConfigList: list of DDoSGeoIPBlockConfigRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSGeoIPBlockConfigRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSSpeedLimitConfigRequest(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSSpeedLimitConfigResponse(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of access rate limit configurations
        :type ConfigList: list of DDoSSpeedLimitConfigRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSSpeedLimitConfigRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListIPAlarmConfigRequest(AbstractModel):
    """DescribeListIPAlarmConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterAlarmType: Alarm threshold type filter. Valid values:
`1`: alarm threshold for inbound traffic
`2`: alarm threshold for cleansing attack traffic
]
        :type FilterAlarmType: int
        :param _FilterIp: IP filter
        :type FilterIp: str
        :param _FilterCname: CNAME of the Anti-DDoS Advanced instance
        :type FilterCname: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterAlarmType = None
        self._FilterIp = None
        self._FilterCname = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterAlarmType(self):
        return self._FilterAlarmType

    @FilterAlarmType.setter
    def FilterAlarmType(self, FilterAlarmType):
        self._FilterAlarmType = FilterAlarmType

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterCname(self):
        return self._FilterCname

    @FilterCname.setter
    def FilterCname(self, FilterCname):
        self._FilterCname = FilterCname


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterAlarmType = params.get("FilterAlarmType")
        self._FilterIp = params.get("FilterIp")
        self._FilterCname = params.get("FilterCname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListIPAlarmConfigResponse(AbstractModel):
    """DescribeListIPAlarmConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of IP alarm threshold configurations
        :type ConfigList: list of IPAlarmThresholdRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListListenerRequest(AbstractModel):
    """DescribeListListener request structure.

    """


class DescribeListListenerResponse(AbstractModel):
    """DescribeListListener response structure.

    """

    def __init__(self):
        r"""
        :param _Layer4Listeners: List of layer-4 forwarding listeners
        :type Layer4Listeners: list of Layer4Rule
        :param _Layer7Listeners: List of layer-7 forwarding listeners
        :type Layer7Listeners: list of Layer7Rule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Layer4Listeners = None
        self._Layer7Listeners = None
        self._RequestId = None

    @property
    def Layer4Listeners(self):
        return self._Layer4Listeners

    @Layer4Listeners.setter
    def Layer4Listeners(self, Layer4Listeners):
        self._Layer4Listeners = Layer4Listeners

    @property
    def Layer7Listeners(self):
        return self._Layer7Listeners

    @Layer7Listeners.setter
    def Layer7Listeners(self, Layer7Listeners):
        self._Layer7Listeners = Layer7Listeners

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Layer4Listeners") is not None:
            self._Layer4Listeners = []
            for item in params.get("Layer4Listeners"):
                obj = Layer4Rule()
                obj._deserialize(item)
                self._Layer4Listeners.append(obj)
        if params.get("Layer7Listeners") is not None:
            self._Layer7Listeners = []
            for item in params.get("Layer7Listeners"):
                obj = Layer7Rule()
                obj._deserialize(item)
                self._Layer7Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListPacketFilterConfigRequest(AbstractModel):
    """DescribeListPacketFilterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when Limit = 0. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListPacketFilterConfigResponse(AbstractModel):
    """DescribeListPacketFilterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: Feature filtering configuration
        :type ConfigList: list of PacketFilterRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = PacketFilterRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListProtectThresholdConfigRequest(AbstractModel):
    """DescribeListProtectThresholdConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        :param _FilterDomain: Domain name filter for querying CC protection thresholds of domain names and protocols
        :type FilterDomain: str
        :param _FilterProtocol: Protocol filter for querying CC protection thresholds of domain names and protocols
        :type FilterProtocol: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None
        self._FilterDomain = None
        self._FilterProtocol = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterDomain(self):
        return self._FilterDomain

    @FilterDomain.setter
    def FilterDomain(self, FilterDomain):
        self._FilterDomain = FilterDomain

    @property
    def FilterProtocol(self):
        return self._FilterProtocol

    @FilterProtocol.setter
    def FilterProtocol(self, FilterProtocol):
        self._FilterProtocol = FilterProtocol


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        self._FilterDomain = params.get("FilterDomain")
        self._FilterProtocol = params.get("FilterProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListProtectThresholdConfigResponse(AbstractModel):
    """DescribeListProtectThresholdConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of protection threshold configurations
        :type ConfigList: list of ProtectThresholdRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProtectThresholdRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListProtocolBlockConfigRequest(AbstractModel):
    """DescribeListProtocolBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListProtocolBlockConfigResponse(AbstractModel):
    """DescribeListProtocolBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: Protocol blocking configuration
        :type ConfigList: list of ProtocolBlockRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProtocolBlockRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListSchedulingDomainRequest(AbstractModel):
    """DescribeListSchedulingDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterDomain: Scheduling domain name filter
        :type FilterDomain: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterDomain = None

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
    def FilterDomain(self):
        return self._FilterDomain

    @FilterDomain.setter
    def FilterDomain(self, FilterDomain):
        self._FilterDomain = FilterDomain


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterDomain = params.get("FilterDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListSchedulingDomainResponse(AbstractModel):
    """DescribeListSchedulingDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _DomainList: List of scheduling domain names
        :type DomainList: list of SchedulingDomainInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = SchedulingDomainInfo()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListWaterPrintConfigRequest(AbstractModel):
    """DescribeListWaterPrintConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _Limit: Number of items per page. The default value is 20 when `Limit = 0`. The maximum value is 100.
        :type Limit: int
        :param _FilterInstanceId: Anti-DDoS instance ID filter. Anti-DDoS instance prefix wildcard search is supported. For example, you can filter Anti-DDoS Pro instances by `bgp-*`.
        :type FilterInstanceId: str
        :param _FilterIp: IP filter
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

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
    def FilterInstanceId(self):
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListWaterPrintConfigResponse(AbstractModel):
    """DescribeListWaterPrintConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists
        :type Total: int
        :param _ConfigList: List of watermark configurations
        :type ConfigList: list of WaterPrintRelation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = WaterPrintRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _RuleIdList: List of rule IDs
        :type RuleIdList: list of str
        """
        self._Business = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth response structure.

    """

    def __init__(self):
        r"""
        :param _ErrHealths: List of rules with exceptions. `Key`: Rule ID, `Value`: Exception IPs and error message. 
        :type ErrHealths: list of KeyValue
        :param _Total: Total number of rules with exceptions
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrHealths = None
        self._Total = None
        self._RequestId = None

    @property
    def ErrHealths(self):
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

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
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNewL7RulesRequest(AbstractModel):
    """DescribeNewL7Rules request structure.

    """

    def __init__(self):
        r"""
        :param _Business: Anti-DDoS service type (`bgpip`: Anti-DDoS Advanced)
        :type Business: str
        :param _StatusList: (Optional) Searches by rule status. Valid values: `0` (Successfully configured), `1` (Being configured), `2` (Configuration failed), `3` (Being deleted), `5` (Deletion failed), `6` (awaiting configuration), `7` (awaiting deletion), and `8` (awaiting certificate configuration).
        :type StatusList: list of int non-negative
        :param _Domain: (Optional) Searches by domain name.
        :type Domain: str
        :param _Ip: (Optional) Searches by IP.
        :type Ip: str
        :param _Limit: Number of items in a page. Returned results are not paged if you enter “0”.
        :type Limit: int
        :param _Offset: Starting offset of the page. Value: (number of pages – 1) * items per page.
        :type Offset: int
        :param _ProtocolList: (Optional) Searches by forwarding protocol. Values: [http, https, http/https]
        :type ProtocolList: list of str
        :param _Cname: CNAME of the Anti-DDoS Advanced instance
        :type Cname: str
        """
        self._Business = None
        self._StatusList = None
        self._Domain = None
        self._Ip = None
        self._Limit = None
        self._Offset = None
        self._ProtocolList = None
        self._Cname = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def ProtocolList(self):
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StatusList = params.get("StatusList")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProtocolList = params.get("ProtocolList")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesResponse(AbstractModel):
    """DescribeNewL7Rules response structure.

    """

    def __init__(self):
        r"""
        :param _Rules: List of forwarding rules
        :type Rules: list of NewL7RuleEntry
        :param _Healths: List of health check settings
        :type Healths: list of L7RuleHealth
        :param _Total: Total number of rules
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rules = None
        self._Healths = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

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
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOverviewDDoSEventListRequest(AbstractModel):
    """DescribeOverviewDDoSEventList request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _AttackStatus: Filters by the attack status. `start`: The attack is ongoing; `end`: The attack ends.
        :type AttackStatus: str
        :param _Offset: The offset value
        :type Offset: int
        :param _Limit: Total number of records
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._AttackStatus = None
        self._Offset = None
        self._Limit = None

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
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AttackStatus = params.get("AttackStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewDDoSEventListResponse(AbstractModel):
    """DescribeOverviewDDoSEventList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of records
        :type Total: int
        :param _EventList: Event list
        :type EventList: list of OverviewDDoSEvent
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._EventList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = OverviewDDoSEvent()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePendingRiskInfoRequest(AbstractModel):
    """DescribePendingRiskInfo request structure.

    """


class DescribePendingRiskInfoResponse(AbstractModel):
    """DescribePendingRiskInfo response structure.

    """

    def __init__(self):
        r"""
        :param _IsPaidUsr: Whether the user is a paid user. Values: `true`, `false`.
        :type IsPaidUsr: bool
        :param _AttackingCount: Number of resources being attacked
        :type AttackingCount: int
        :param _BlockingCount: Number of resource blocked
        :type BlockingCount: int
        :param _ExpiredCount: Number of expired resources
        :type ExpiredCount: int
        :param _Total: Total pending risk events
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsPaidUsr = None
        self._AttackingCount = None
        self._BlockingCount = None
        self._ExpiredCount = None
        self._Total = None
        self._RequestId = None

    @property
    def IsPaidUsr(self):
        return self._IsPaidUsr

    @IsPaidUsr.setter
    def IsPaidUsr(self, IsPaidUsr):
        self._IsPaidUsr = IsPaidUsr

    @property
    def AttackingCount(self):
        return self._AttackingCount

    @AttackingCount.setter
    def AttackingCount(self, AttackingCount):
        self._AttackingCount = AttackingCount

    @property
    def BlockingCount(self):
        return self._BlockingCount

    @BlockingCount.setter
    def BlockingCount(self, BlockingCount):
        self._BlockingCount = BlockingCount

    @property
    def ExpiredCount(self):
        return self._ExpiredCount

    @ExpiredCount.setter
    def ExpiredCount(self, ExpiredCount):
        self._ExpiredCount = ExpiredCount

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
        self._IsPaidUsr = params.get("IsPaidUsr")
        self._AttackingCount = params.get("AttackingCount")
        self._BlockingCount = params.get("BlockingCount")
        self._ExpiredCount = params.get("ExpiredCount")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DisassociateDDoSEipAddressRequest(AbstractModel):
    """DisassociateDDoSEipAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID (only Anti-DDoS Advanced). For example, `bgpip-0000011x`.
        :type InstanceId: str
        :param _Eip: EIP of the Anti-DDoS instance ID
        :type Eip: str
        """
        self._InstanceId = None
        self._Eip = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDDoSEipAddressResponse(AbstractModel):
    """DisassociateDDoSEipAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class EipAddressPackRelation(AbstractModel):
    """Details of the Anycast package

    """

    def __init__(self):
        r"""
        :param _IpCount: Number of package IPs
        :type IpCount: int
        :param _AutoRenewFlag: Auto-renewal flag
        :type AutoRenewFlag: int
        :param _CurDeadline: Current expiration time
        :type CurDeadline: str
        """
        self._IpCount = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def IpCount(self):
        return self._IpCount

    @IpCount.setter
    def IpCount(self, IpCount):
        self._IpCount = IpCount

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._IpCount = params.get("IpCount")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAddressRelation(AbstractModel):
    """EIP association details

    """

    def __init__(self):
        r"""
        :param _EipAddressRegion: Region of the Anti-DDoS instance bound to the EIP. For example, hk indicates Hong Kong.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipAddressRegion: str
        :param _EipBoundRscIns: ID of the bound resource. For example, an ID may be bound to an CVM instance.
Note: This is field may return `null`, indicating that no valid value can be obtained.
        :type EipBoundRscIns: str
        :param _EipBoundRscEni: ID of the bound ENI
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipBoundRscEni: str
        :param _EipBoundRscVip: Private IP of the bound resource
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EipBoundRscVip: str
        :param _ModifyTime: Modification time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ModifyTime: str
        """
        self._EipAddressRegion = None
        self._EipBoundRscIns = None
        self._EipBoundRscEni = None
        self._EipBoundRscVip = None
        self._ModifyTime = None

    @property
    def EipAddressRegion(self):
        return self._EipAddressRegion

    @EipAddressRegion.setter
    def EipAddressRegion(self, EipAddressRegion):
        self._EipAddressRegion = EipAddressRegion

    @property
    def EipBoundRscIns(self):
        return self._EipBoundRscIns

    @EipBoundRscIns.setter
    def EipBoundRscIns(self, EipBoundRscIns):
        self._EipBoundRscIns = EipBoundRscIns

    @property
    def EipBoundRscEni(self):
        return self._EipBoundRscEni

    @EipBoundRscEni.setter
    def EipBoundRscEni(self, EipBoundRscEni):
        self._EipBoundRscEni = EipBoundRscEni

    @property
    def EipBoundRscVip(self):
        return self._EipBoundRscVip

    @EipBoundRscVip.setter
    def EipBoundRscVip(self, EipBoundRscVip):
        self._EipBoundRscVip = EipBoundRscVip

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._EipAddressRegion = params.get("EipAddressRegion")
        self._EipBoundRscIns = params.get("EipBoundRscIns")
        self._EipBoundRscEni = params.get("EipBoundRscEni")
        self._EipBoundRscVip = params.get("EipBoundRscVip")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipProductInfo(AbstractModel):
    """Details of the cloud product used by the EIP

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _BizType: Cloud product category. Valid values:
`public`: CVM
`bm`: BM
`eni`: ENI
`vpngw`: VPN gateway
 `natgw`: NAT gateway
`waf`: WAF
`fpc`: financial products
`gaap`: GAAP 
`other`: hosted IP
]
        :type BizType: str
        :param _DeviceType: Cloud sub-product category. Valid values: `cvm` (CVM), `lb` (Load balancer), `eni` (ENI), `vpngw` (VPN gateway), `natgw` (NAT gateway), `waf` (WAF), `fpc` (financial products), `gaap` (GAAP), `eip` (BM EIP) and `other` (hosted IP).
        :type DeviceType: str
        :param _InstanceId: Cloud instance ID of the IP. This field InstanceId will be `eni-*` if the instance ID is bound to an ENI IP; `none` if there is no instance ID to bind to a hosted IP.
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
        


class ForwardListener(AbstractModel):
    """Forwarding listener

    """

    def __init__(self):
        r"""
        :param _FrontendPort: The starting port for listener forwarding. Value range: 1 to 65535.
        :type FrontendPort: int
        :param _ForwardProtocol: Forwarding protocol. Valid values:
`TCP`
`UDP`
]
        :type ForwardProtocol: str
        :param _FrontendPortEnd: The ending port for listener forwarding. Value range: 1 to 65535.
        :type FrontendPortEnd: int
        """
        self._FrontendPort = None
        self._ForwardProtocol = None
        self._FrontendPortEnd = None

    @property
    def FrontendPort(self):
        return self._FrontendPort

    @FrontendPort.setter
    def FrontendPort(self, FrontendPort):
        self._FrontendPort = FrontendPort

    @property
    def ForwardProtocol(self):
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def FrontendPortEnd(self):
        return self._FrontendPortEnd

    @FrontendPortEnd.setter
    def FrontendPortEnd(self, FrontendPortEnd):
        self._FrontendPortEnd = FrontendPortEnd


    def _deserialize(self, params):
        self._FrontendPort = params.get("FrontendPort")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._FrontendPortEnd = params.get("FrontendPortEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusMap(AbstractModel):
    """Aggregated data on the HTTP status codes of business traffic

    """

    def __init__(self):
        r"""
        :param _SourceHttp2xx: HTTP 2xx Forwarding status code
        :type SourceHttp2xx: list of float
        :param _Http5xx: HTTP 5xx Status code
        :type Http5xx: list of float
        :param _SourceHttp5xx: HTTP 5xx Forwarding status code
        :type SourceHttp5xx: list of float
        :param _SourceHttp404: HTTP 404 Forwarding status code
        :type SourceHttp404: list of float
        :param _Http4xx: HTTP 4xx Status code
        :type Http4xx: list of float
        :param _SourceHttp4xx: HTTP 4xx Forwarding status code
        :type SourceHttp4xx: list of float
        :param _Http2xx: HTTP 2xx Status code
        :type Http2xx: list of float
        :param _Http404: HTTP 404 Status code
        :type Http404: list of float
        :param _SourceHttp3xx: HTTP 3xx Forwarding status code
        :type SourceHttp3xx: list of float
        :param _Http3xx: HTTP 3xx Status code
        :type Http3xx: list of float
        """
        self._SourceHttp2xx = None
        self._Http5xx = None
        self._SourceHttp5xx = None
        self._SourceHttp404 = None
        self._Http4xx = None
        self._SourceHttp4xx = None
        self._Http2xx = None
        self._Http404 = None
        self._SourceHttp3xx = None
        self._Http3xx = None

    @property
    def SourceHttp2xx(self):
        return self._SourceHttp2xx

    @SourceHttp2xx.setter
    def SourceHttp2xx(self, SourceHttp2xx):
        self._SourceHttp2xx = SourceHttp2xx

    @property
    def Http5xx(self):
        return self._Http5xx

    @Http5xx.setter
    def Http5xx(self, Http5xx):
        self._Http5xx = Http5xx

    @property
    def SourceHttp5xx(self):
        return self._SourceHttp5xx

    @SourceHttp5xx.setter
    def SourceHttp5xx(self, SourceHttp5xx):
        self._SourceHttp5xx = SourceHttp5xx

    @property
    def SourceHttp404(self):
        return self._SourceHttp404

    @SourceHttp404.setter
    def SourceHttp404(self, SourceHttp404):
        self._SourceHttp404 = SourceHttp404

    @property
    def Http4xx(self):
        return self._Http4xx

    @Http4xx.setter
    def Http4xx(self, Http4xx):
        self._Http4xx = Http4xx

    @property
    def SourceHttp4xx(self):
        return self._SourceHttp4xx

    @SourceHttp4xx.setter
    def SourceHttp4xx(self, SourceHttp4xx):
        self._SourceHttp4xx = SourceHttp4xx

    @property
    def Http2xx(self):
        return self._Http2xx

    @Http2xx.setter
    def Http2xx(self, Http2xx):
        self._Http2xx = Http2xx

    @property
    def Http404(self):
        return self._Http404

    @Http404.setter
    def Http404(self, Http404):
        self._Http404 = Http404

    @property
    def SourceHttp3xx(self):
        return self._SourceHttp3xx

    @SourceHttp3xx.setter
    def SourceHttp3xx(self, SourceHttp3xx):
        self._SourceHttp3xx = SourceHttp3xx

    @property
    def Http3xx(self):
        return self._Http3xx

    @Http3xx.setter
    def Http3xx(self, Http3xx):
        self._Http3xx = Http3xx


    def _deserialize(self, params):
        self._SourceHttp2xx = params.get("SourceHttp2xx")
        self._Http5xx = params.get("Http5xx")
        self._SourceHttp5xx = params.get("SourceHttp5xx")
        self._SourceHttp404 = params.get("SourceHttp404")
        self._Http4xx = params.get("Http4xx")
        self._SourceHttp4xx = params.get("SourceHttp4xx")
        self._Http2xx = params.get("Http2xx")
        self._Http404 = params.get("Http404")
        self._SourceHttp3xx = params.get("SourceHttp3xx")
        self._Http3xx = params.get("Http3xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAlarmThresholdRelation(AbstractModel):
    """Single IP alarm threshold configuration

    """

    def __init__(self):
        r"""
        :param _AlarmType: Alarm threshold type. Valid values:
`1`: alarm threshold for inbound traffic
`2`: alarm threshold for cleansing attack traffic
]
        :type AlarmType: int
        :param _AlarmThreshold: Alarm threshold (Mbps). The value should be greater than or equal to 0. Note that the alarm threshold configuration will be removed if you pass the parameter for input and set it to 0.
        :type AlarmThreshold: int
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._AlarmType = None
        self._AlarmThreshold = None
        self._InstanceDetailList = None

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
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLineInfo(AbstractModel):
    """IP line information

    """

    def __init__(self):
        r"""
        :param _Type: IP line type. Valid values:
`bgp`: BGP IP
`ctcc`: CTCC IP
`cucc`: CUCC IP
`cmcc`: CMCC IP
`abroad`: IP outside the Chinese mainland
]
        :type Type: str
        :param _Eip: 
        :type Eip: str
        :param _Cname: CNAME of the instance
        :type Cname: str
        :param _ResourceFlag: Flag of the instance. `0`: Anti-DDoS Pro instance; `1`: Anti-DDoS Advanced instance; `2`: Non-Anti-DDoS Advanced instance.
        :type ResourceFlag: int
        """
        self._Type = None
        self._Eip = None
        self._Cname = None
        self._ResourceFlag = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def ResourceFlag(self):
        return self._ResourceFlag

    @ResourceFlag.setter
    def ResourceFlag(self, ResourceFlag):
        self._ResourceFlag = ResourceFlag


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Eip = params.get("Eip")
        self._Cname = params.get("Cname")
        self._ResourceFlag = params.get("ResourceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsL7Rules(AbstractModel):
    """Layer-7 instance rules

    """

    def __init__(self):
        r"""
        :param _Status: Rules can only be modified when the status is `0`, `2`, or `8`.
Rule status. Values: `0` (Normal), `1` (Being configured), `2` (Configuration failed), `3` (Being deleted), `5` (Failed to be deleted), `6` (Pending add), `7` (Pending delete), `8` (Pending certificate upload), `9` (Associated resource not exist), `10` (Pending modify), `11` (Being modified).
        :type Status: int
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _InsId: Instance ID
        :type InsId: str
        :param _AppId: User App ID
        :type AppId: str
        :param _VirtualPort: High-defense port
        :type VirtualPort: str
        :param _SSLId: Certificate ID
        :type SSLId: str
        """
        self._Status = None
        self._Domain = None
        self._Protocol = None
        self._InsId = None
        self._AppId = None
        self._VirtualPort = None
        self._SSLId = None

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
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InsId(self):
        return self._InsId

    @InsId.setter
    def InsId(self, InsId):
        self._InsId = InsId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._InsId = params.get("InsId")
        self._AppId = params.get("AppId")
        self._VirtualPort = params.get("VirtualPort")
        self._SSLId = params.get("SSLId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRelation(AbstractModel):
    """Instance IP information

    """

    def __init__(self):
        r"""
        :param _EipList: Instance IP
        :type EipList: list of str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._EipList = None
        self._InstanceId = None

    @property
    def EipList(self):
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipList = params.get("EipList")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Status: 
        :type Status: str
        :param _Ip: 
        :type Ip: str
        :param _BlockTime: 
        :type BlockTime: str
        :param _UnBlockTime: 
        :type UnBlockTime: str
        :param _ActionType: 
        :type ActionType: str
        :param _ProtectFlag: 
        :type ProtectFlag: int
        """
        self._Status = None
        self._Ip = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None
        self._ProtectFlag = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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

    @property
    def ProtectFlag(self):
        return self._ProtectFlag

    @ProtectFlag.setter
    def ProtectFlag(self, ProtectFlag):
        self._ProtectFlag = ProtectFlag


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Ip = params.get("Ip")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        self._ProtectFlag = params.get("ProtectFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpSegment(AbstractModel):
    """Structure of IP range

    """

    def __init__(self):
        r"""
        :param _Ip: IP address
        :type Ip: str
        :param _Mask: IP mask. For a 32-bit IP address, enter `0`.
        :type Mask: int
        """
        self._Ip = None
        self._Mask = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """Status of the IP

    """

    def __init__(self):
        r"""
        :param _Key: IP
        :type Key: str
        :param _Value: Status of the IP. Values: `1` (blocked); `2` (normal); `3` (being attacked)
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
        


class L4RuleSource(AbstractModel):
    """List of layer-4 forwarding rules

    """

    def __init__(self):
        r"""
        :param _Source: IP or domain name for forwarding.
        :type Source: str
        :param _Weight: Weight. Value range: [0,100].
        :type Weight: int
        :param _Port: 8000
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param _Backup: Secondary origin server. `1`: secondary origin server; `0`: general origin server.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Backup: int
        """
        self._Source = None
        self._Weight = None
        self._Port = None
        self._Backup = None

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

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        self._Backup = params.get("Backup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """Layer-7 forwarding rule.

    """

    def __init__(self):
        r"""
        :param _KeepTime: Session persistence duration, in seconds.
        :type KeepTime: int
        :param _Domain: Forwarding domain name.
        :type Domain: str
        :param _Protocol: Forwarding protocol. Valid values: `http` and `https`.
        :type Protocol: str
        :param _SourceType: Forwarding method. Valid values: `1` (by domain name); `2` (by IP).
        :type SourceType: int
        :param _LbType: Load balancing method. Valid value: `1` (weighed polling).
        :type LbType: int
        :param _SourceList: List of origins
        :type SourceList: list of L4RuleSource
        :param _KeepEnable: Whether session persistence is enabled. Valid values: `0` (disabled) and `1` (enabled).
        :type KeepEnable: int
        :param _Status: Rule status. Valid values: `0` (the rule was successfully configured), `1` (configuring the rule), `2` (rule configuration failed), `3` (deleting the rule), `5` (failed to delete rule), `6` (rule awaiting configuration), `7` (rule awaiting deletion), and `8` (rule awaiting certificate configuration).
        :type Status: int
        :param _RuleId: Rule ID. This field is not required for adding a rule, but is required for modifying or deleting a rule.
        :type RuleId: str
        :param _CCThreshold: CC protection threshold based on HTTPS.
        :type CCThreshold: int
        :param _PrivateKey: [Disused] When the certificate is an external certificate, the certificate key should be provided here. 
        :type PrivateKey: str
        :param _CCEnable: CC protection status based on HTTPS. Valid values: `0` (disabled) and `1` (enabled).
        :type CCEnable: int
        :param _HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disable) and `1` (enable). It defaults to `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpsToHttpEnable: int
        :param _CertType: Certificate source. When the forwarding protocol is HTTPS, this field must be set to `2` (Tencent Cloud managed certificate), and for HTTP protocol, it can be set to `0`.
        :type CertType: int
        :param _Cert: [Disused] When the certificate is an external certificate, the certificate content should be provided here. 
        :type Cert: str
        :param _CCLevel: CC protection level based on HTTPS.
        :type CCLevel: str
        :param _RuleName: Rule description.
        :type RuleName: str
        :param _CCStatus: CC protection status. Valid values: `0` (disabled) and `1` (enabled).
        :type CCStatus: int
        :param _VirtualPort: Access port number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VirtualPort: int
        :param _SSLId: When the certificate is managed by Tencent Cloud, this field must be set to the ID of the managed certificate.
        :type SSLId: str
        :param _Id: ID of the rule
        :type Id: str
        :param _CCAIEnable: Intelligent CC protection status. Valid values: `0` (disabled) and `1` (enabled).
        :type CCAIEnable: int
        """
        self._KeepTime = None
        self._Domain = None
        self._Protocol = None
        self._SourceType = None
        self._LbType = None
        self._SourceList = None
        self._KeepEnable = None
        self._Status = None
        self._RuleId = None
        self._CCThreshold = None
        self._PrivateKey = None
        self._CCEnable = None
        self._HttpsToHttpEnable = None
        self._CertType = None
        self._Cert = None
        self._CCLevel = None
        self._RuleName = None
        self._CCStatus = None
        self._VirtualPort = None
        self._SSLId = None
        self._Id = None
        self._CCAIEnable = None

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def HttpsToHttpEnable(self):
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CCLevel(self):
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CCStatus(self):
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CCAIEnable(self):
        return self._CCAIEnable

    @CCAIEnable.setter
    def CCAIEnable(self, CCAIEnable):
        self._CCAIEnable = CCAIEnable


    def _deserialize(self, params):
        self._KeepTime = params.get("KeepTime")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._SourceType = params.get("SourceType")
        self._LbType = params.get("LbType")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._KeepEnable = params.get("KeepEnable")
        self._Status = params.get("Status")
        self._RuleId = params.get("RuleId")
        self._CCThreshold = params.get("CCThreshold")
        self._PrivateKey = params.get("PrivateKey")
        self._CCEnable = params.get("CCEnable")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._CertType = params.get("CertType")
        self._Cert = params.get("Cert")
        self._CCLevel = params.get("CCLevel")
        self._RuleName = params.get("RuleName")
        self._CCStatus = params.get("CCStatus")
        self._VirtualPort = params.get("VirtualPort")
        self._SSLId = params.get("SSLId")
        self._Id = params.get("Id")
        self._CCAIEnable = params.get("CCAIEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """Health check parameters of layer-7 forwarding rules

    """

    def __init__(self):
        r"""
        :param _Status: Configuration status. Values: `0` (normal), `1` (configuration in progress) and `2` (configuration failed).
        :type Status: int
        :param _Enable: Switch. Values: `1`: Enable; `0`: Disable.
        :type Enable: int
        :param _RuleId: ID of the rule
        :type RuleId: str
        :param _Url: HTTP request path. The default value is /.
        :type Url: str
        :param _Interval: Health check interval. Unit: second.
        :type Interval: int
        :param _AliveNum: Healthy threshold, which specifies the number of consecutive successful health checks.
        :type AliveNum: int
        :param _KickNum: Unhealthy threshold, which specifies the number of consecutive failed health checks.
        :type KickNum: int
        :param _Method: HTTP request method. Values: `HEAD` and `GET`.
        :type Method: str
        :param _StatusCode: Status code that signifies a normal state. Values: `1` (1xx), `2` (2xx), `4` (3xx), `8` (4xx), and `16` (5xx).
        :type StatusCode: int
        :param _ProtocolFlag: Whether to deploy both HTTP and HTTPS health check rules
        :type ProtocolFlag: int
        :param _PassiveEnable: Enables passive detection. Values: `1` (enable) and `0` (disable).
        :type PassiveEnable: int
        :param _BlockInter: Blocking period in the passive detection configuration
        :type BlockInter: int
        :param _FailedCountInter: Time interval between passive detections
        :type FailedCountInter: int
        :param _FailedThreshold: Unhealthy threshold in the passive detection configuration
        :type FailedThreshold: int
        :param _PassiveStatusCode: Status code that signals that the passive detection considers the status normal. Values: `1` (1xx), `2` (2xx), `4` (3xx), `8` (4xx), and `16` (5xx).
        :type PassiveStatusCode: int
        :param _PassiveStatus: Configuration status of the passive health check. Values: `0` (Normal), `1` (configuration in progress) and `2` (configuration failed).
        :type PassiveStatus: int
        """
        self._Status = None
        self._Enable = None
        self._RuleId = None
        self._Url = None
        self._Interval = None
        self._AliveNum = None
        self._KickNum = None
        self._Method = None
        self._StatusCode = None
        self._ProtocolFlag = None
        self._PassiveEnable = None
        self._BlockInter = None
        self._FailedCountInter = None
        self._FailedThreshold = None
        self._PassiveStatusCode = None
        self._PassiveStatus = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

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
    def ProtocolFlag(self):
        return self._ProtocolFlag

    @ProtocolFlag.setter
    def ProtocolFlag(self, ProtocolFlag):
        self._ProtocolFlag = ProtocolFlag

    @property
    def PassiveEnable(self):
        return self._PassiveEnable

    @PassiveEnable.setter
    def PassiveEnable(self, PassiveEnable):
        self._PassiveEnable = PassiveEnable

    @property
    def BlockInter(self):
        return self._BlockInter

    @BlockInter.setter
    def BlockInter(self, BlockInter):
        self._BlockInter = BlockInter

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
    def PassiveStatusCode(self):
        return self._PassiveStatusCode

    @PassiveStatusCode.setter
    def PassiveStatusCode(self, PassiveStatusCode):
        self._PassiveStatusCode = PassiveStatusCode

    @property
    def PassiveStatus(self):
        return self._PassiveStatus

    @PassiveStatus.setter
    def PassiveStatus(self, PassiveStatus):
        self._PassiveStatus = PassiveStatus


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._RuleId = params.get("RuleId")
        self._Url = params.get("Url")
        self._Interval = params.get("Interval")
        self._AliveNum = params.get("AliveNum")
        self._KickNum = params.get("KickNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._ProtocolFlag = params.get("ProtocolFlag")
        self._PassiveEnable = params.get("PassiveEnable")
        self._BlockInter = params.get("BlockInter")
        self._FailedCountInter = params.get("FailedCountInter")
        self._FailedThreshold = params.get("FailedThreshold")
        self._PassiveStatusCode = params.get("PassiveStatusCode")
        self._PassiveStatus = params.get("PassiveStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer4Rule(AbstractModel):
    """Layer-4 forwarding rule

    """

    def __init__(self):
        r"""
        :param _BackendPort: Real server port. Value range: 1–65535.
        :type BackendPort: int
        :param _FrontendPort: Forwarding port. Value range: 1–65535.
        :type FrontendPort: int
        :param _Protocol: Forwarding rule. Valid values:
TCP
UDP
]
        :type Protocol: str
        :param _RealServers: List of real servers
        :type RealServers: list of SourceServer
        :param _InstanceDetails: Information of the Anti-DDoS instance
        :type InstanceDetails: list of InstanceRelation
        :param _InstanceDetailRule: Information of the Anti-DDoS instance configured
        :type InstanceDetailRule: list of RuleInstanceRelation
        """
        self._BackendPort = None
        self._FrontendPort = None
        self._Protocol = None
        self._RealServers = None
        self._InstanceDetails = None
        self._InstanceDetailRule = None

    @property
    def BackendPort(self):
        return self._BackendPort

    @BackendPort.setter
    def BackendPort(self, BackendPort):
        self._BackendPort = BackendPort

    @property
    def FrontendPort(self):
        return self._FrontendPort

    @FrontendPort.setter
    def FrontendPort(self, FrontendPort):
        self._FrontendPort = FrontendPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RealServers(self):
        return self._RealServers

    @RealServers.setter
    def RealServers(self, RealServers):
        self._RealServers = RealServers

    @property
    def InstanceDetails(self):
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def InstanceDetailRule(self):
        return self._InstanceDetailRule

    @InstanceDetailRule.setter
    def InstanceDetailRule(self, InstanceDetailRule):
        self._InstanceDetailRule = InstanceDetailRule


    def _deserialize(self, params):
        self._BackendPort = params.get("BackendPort")
        self._FrontendPort = params.get("FrontendPort")
        self._Protocol = params.get("Protocol")
        if params.get("RealServers") is not None:
            self._RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self._RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self._InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer7Rule(AbstractModel):
    """Layer-7 forwarding rule

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _ProxyTypeList: List of forwarding types
        :type ProxyTypeList: list of ProxyTypeInfo
        :param _RealServers: List of real servers
        :type RealServers: list of SourceServer
        :param _InstanceDetails: Information of the Anti-DDoS instance
        :type InstanceDetails: list of InstanceRelation
        :param _InstanceDetailRule: Information of the Anti-DDoS instance configured
        :type InstanceDetailRule: list of RuleInstanceRelation
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Vport: Port number
        :type Vport: int
        """
        self._Domain = None
        self._ProxyTypeList = None
        self._RealServers = None
        self._InstanceDetails = None
        self._InstanceDetailRule = None
        self._Protocol = None
        self._Vport = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProxyTypeList(self):
        return self._ProxyTypeList

    @ProxyTypeList.setter
    def ProxyTypeList(self, ProxyTypeList):
        self._ProxyTypeList = ProxyTypeList

    @property
    def RealServers(self):
        return self._RealServers

    @RealServers.setter
    def RealServers(self, RealServers):
        self._RealServers = RealServers

    @property
    def InstanceDetails(self):
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def InstanceDetailRule(self):
        return self._InstanceDetailRule

    @InstanceDetailRule.setter
    def InstanceDetailRule(self, InstanceDetailRule):
        self._InstanceDetailRule = InstanceDetailRule

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


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("ProxyTypeList") is not None:
            self._ProxyTypeList = []
            for item in params.get("ProxyTypeList"):
                obj = ProxyTypeInfo()
                obj._deserialize(item)
                self._ProxyTypeList.append(obj)
        if params.get("RealServers") is not None:
            self._RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self._RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self._InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailRule.append(obj)
        self._Protocol = params.get("Protocol")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerCcThreholdConfig(AbstractModel):
    """CC protection thresholds of the domain name and protocol

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _Protocol: Protocol. Value: `https`.
        :type Protocol: str
        :param _CCEnable: Status. Valid values: `0` (disabled), `1` (enabled).
        :type CCEnable: int
        :param _CCThreshold: CC protection threshold
        :type CCThreshold: int
        """
        self._Domain = None
        self._Protocol = None
        self._CCEnable = None
        self._CCThreshold = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

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


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPrecisionPolicyRequest(AbstractModel):
    """ModifyCCPrecisionPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        :param _PolicyAction: Specifies the action. `alg`: Verify the access request via CAPTCHA; `drop`: Drop the access request.
        :type PolicyAction: str
        :param _PolicyList: Policy records
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self._InstanceId = None
        self._PolicyId = None
        self._PolicyAction = None
        self._PolicyList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyAction(self):
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPrecisionPolicyResponse(AbstractModel):
    """ModifyCCPrecisionPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyCcBlackWhiteIpListRequest(AbstractModel):
    """ModifyCcBlackWhiteIpList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IpList: List of IPs
        :type IpList: list of IpSegment
        :param _Type: IP type. Valid values: `black` (blocklisted IP), `white`(allowlisted IP).
        :type Type: str
        :param _PolicyId: Policy ID
        :type PolicyId: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcBlackWhiteIpListResponse(AbstractModel):
    """ModifyCcBlackWhiteIpList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyDDoSGeoIPBlockConfigRequest(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: Region blocking configuration. The configuration ID cannot be empty when you set this parameter.
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSGeoIPBlockConfigResponse(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyDDoSSpeedLimitConfigRequest(AbstractModel):
    """ModifyDDoSSpeedLimitConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: Access rate limit configuration. The configuration ID cannot be empty when you set this parameter.
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSpeedLimitConfigResponse(AbstractModel):
    """ModifyDDoSSpeedLimitConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyDomainUsrNameRequest(AbstractModel):
    """ModifyDomainUsrName request structure.

    """

    def __init__(self):
        r"""
        :param _DomainName: User CNAME
        :type DomainName: str
        :param _DomainUserName: Domain name
        :type DomainUserName: str
        """
        self._DomainName = None
        self._DomainUserName = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainUserName(self):
        return self._DomainUserName

    @DomainUserName.setter
    def DomainUserName(self, DomainUserName):
        self._DomainUserName = DomainUserName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._DomainUserName = params.get("DomainUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUsrNameResponse(AbstractModel):
    """ModifyDomainUsrName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :type Rule: :class:`tencentcloud.antiddos.v20200309.models.NewL7RuleEntry`
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
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyPacketFilterConfigRequest(AbstractModel):
    """ModifyPacketFilterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _PacketFilterConfig: Feature filtering configuration
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPacketFilterConfigResponse(AbstractModel):
    """ModifyPacketFilterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class NewL7RuleEntry(AbstractModel):
    """Layer-7 rule.

    """

    def __init__(self):
        r"""
        :param _Protocol: Forwarding protocol. Valid values: `http` and `https`.
        :type Protocol: str
        :param _Domain: Forwarding domain name.
        :type Domain: str
        :param _LbType: Load balancing method. Valid value: `1` (weighed polling).
        :type LbType: int
        :param _KeepEnable: Whether session persistence is enabled. Valid values: `0` (disabled) and `1` (enabled).
        :type KeepEnable: int
        :param _KeepTime: Session persistence duration, in seconds.
        :type KeepTime: int
        :param _SourceType: Forwarding method. Valid values: `1` (by domain name); `2` (by IP).
        :type SourceType: int
        :param _SourceList: List of origins
        :type SourceList: list of L4RuleSource
        :param _Region: Region code.
        :type Region: int
        :param _Id: Resource ID.
        :type Id: str
        :param _Ip: Anti-DDoS instance IP address.
        :type Ip: str
        :param _RuleId: Rule ID. This field is not required for adding a rule, but is required for modifying or deleting a rule.
        :type RuleId: str
        :param _RuleName: Rule description.
        :type RuleName: str
        :param _CertType: Certificate source. When the forwarding protocol is HTTPS, this field must be set to `2` (Tencent Cloud managed certificate), and for HTTP protocol, it can be set to `0`.
        :type CertType: int
        :param _SSLId: When the certificate is managed by Tencent Cloud, this field must be set to the ID of the managed certificate.
        :type SSLId: str
        :param _Cert: [Disused] When the certificate is an external certificate, the certificate content should be provided here. 
        :type Cert: str
        :param _PrivateKey: [Disused] When the certificate is an external certificate, the certificate key should be provided here. 
        :type PrivateKey: str
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
        :param _ModifyTime: Modification time.
        :type ModifyTime: str
        :param _HttpsToHttpEnable: Whether to enable **Forward HTTPS requests via HTTP**. Valid values: `0` (disabled) and `1` (enabled). It defaults to `0`.
        :type HttpsToHttpEnable: int
        :param _VirtualPort: Access port number.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VirtualPort: int
        :param _RewriteHttps: Specifies whether to forcibly redirect HTTP to HTTPS. `1`: Enable. `0`: Disable.
        :type RewriteHttps: int
        :param _ErrCode: Returns an error code when the rule configuration fails (only valid when `Status=2`). `1001`: The certificate does not exist. `1002`: Failed to obtain the certificate. `1003`: Failed to upload the certificate. `1004`: The certificate has expired.
        :type ErrCode: int
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: int
        """
        self._Protocol = None
        self._Domain = None
        self._LbType = None
        self._KeepEnable = None
        self._KeepTime = None
        self._SourceType = None
        self._SourceList = None
        self._Region = None
        self._Id = None
        self._Ip = None
        self._RuleId = None
        self._RuleName = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._ModifyTime = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None
        self._RewriteHttps = None
        self._ErrCode = None
        self._Version = None

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
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

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

    @property
    def RewriteHttps(self):
        return self._RewriteHttps

    @RewriteHttps.setter
    def RewriteHttps(self, RewriteHttps):
        self._RewriteHttps = RewriteHttps

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._KeepTime = params.get("KeepTime")
        self._SourceType = params.get("SourceType")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._ModifyTime = params.get("ModifyTime")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        self._RewriteHttps = params.get("RewriteHttps")
        self._ErrCode = params.get("ErrCode")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewDDoSEvent(AbstractModel):
    """DDoS events recorded

    """

    def __init__(self):
        r"""
        :param _Id: Event ID
        :type Id: str
        :param _Vip: IP
        :type Vip: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _AttackType: Attack type
        :type AttackType: str
        :param _AttackStatus: Attack status. `0`: The attack is ongoing; `1`: The attack ends.
        :type AttackStatus: int
        :param _Mbps: Attack traffic, in Mbps
        :type Mbps: int
        :param _Pps: Attack packets, in PPS
        :type Pps: int
        :param _Business: Anti-DDoS service type. `bgp-multip`: Anti-DDoS Pro; `bgpip`: Anti-DDoS Advanced; `basic`: Anti-DDoS Basic.
        :type Business: str
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _InstanceName: Anti-DDoS instance name
        :type InstanceName: str
        """
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._AttackType = None
        self._AttackStatus = None
        self._Mbps = None
        self._Pps = None
        self._Business = None
        self._InstanceId = None
        self._InstanceName = None

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
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

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
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AttackType = params.get("AttackType")
        self._AttackStatus = params.get("AttackStatus")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._Business = params.get("Business")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackInfo(AbstractModel):
    """Package information

    """

    def __init__(self):
        r"""
        :param _PackType: Package type. Valid values:
`staticpack`: non-BGP package
`insurance`: guarantee package
]
        :type PackType: str
        :param _PackId: Package ID
        :type PackId: str
        """
        self._PackType = None
        self._PackId = None

    @property
    def PackType(self):
        return self._PackType

    @PackType.setter
    def PackType(self, PackType):
        self._PackType = PackType

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId


    def _deserialize(self, params):
        self._PackType = params.get("PackType")
        self._PackId = params.get("PackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterConfig(AbstractModel):
    """Feature filtering configuration

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol. Valid values: `tcp`, `udp`, `icmp`, `all`.
        :type Protocol: str
        :param _SportStart: Start source port. Value range: 0–65535.
        :type SportStart: int
        :param _SportEnd: End source port. Value range: 0–65535. The value also should be greater than or equal to that of the start source port.
        :type SportEnd: int
        :param _DportStart: Start destination port
        :type DportStart: int
        :param _DportEnd: End destination port. Value range: 1–65535. The value also should be greater than or equal to that of the start source port.
        :type DportEnd: int
        :param _PktlenMin: Minimum message length. Value range: 1–1500.
        :type PktlenMin: int
        :param _PktlenMax: Maximum message length. Value range: 1–1500. The value also should be greater than or equal to that of the minimum message length.
        :type PktlenMax: int
        :param _Action: Action. Valid values:
`drop`: discards the request.
`transmit`: allows the request.
`drop_black`: discards the request and adds the IP to blocklist.
`drop_rst`: blocks the request.
`drop_black_rst`: blocks the request and adds the IP to blocklist.
`forward`: continues protection.
]
        :type Action: str
        :param _MatchBegin: Detection location:
`begin_l3`: IP header
`begin_l4`: TCP/UDP header
`begin_l5`: T load
`no_match`: no match
]
        :type MatchBegin: str
        :param _MatchType: Detection type:
`sunday`: keyword
`pcre`: regular expression
]
        :type MatchType: str
        :param _Str: Detection value. Should be in key string or regular expression. 
When the `MatchType` is `sunday`, enter a string or a string in hexadecimal byte code representation. For example, a string "123" corresponds to the hexadecimal byte code "\x313233".
When the `MatchType` is `pcre`, enter a regular expression.
]
        :type Str: str
        :param _Depth: Detection depth starting from the detection position. Value range: [0, 1500].
        :type Depth: int
        :param _Offset: Offset starting from the detection position. Value range: [0, Depth].
        :type Offset: int
        :param _IsNot: Whether the detection value is included:
`0`: included
`1`: excluded
]
        :type IsNot: int
        :param _MatchLogic: Relationship between the first and second detection conditions:
`and`: under both the first and second detection conditions
`none`: under only the first detection condition
]
        :type MatchLogic: str
        :param _MatchBegin2: The second detection position:
`begin_l5`: load
`no_match`: no match
]
        :type MatchBegin2: str
        :param _MatchType2: The second detection type:
`sunday`: keyword
`pcre`: regular expression
]
        :type MatchType2: str
        :param _Str2: The second detection value. Should be in key string or regular expression.
When the `MatchType` is `sunday`, enter a string or a string in hexadecimal byte code representation. For example, a string "123" corresponds to the hexadecimal byte code "\x313233".
When the `MatchType` is `pcre`, enter a regular expression.
]
        :type Str2: str
        :param _Depth2: Detection depth starting from the second detection position. Value range: [0, 1500].
        :type Depth2: int
        :param _Offset2: Offset starting from the second detection position. Value range: [0, Depth2].
        :type Offset2: int
        :param _IsNot2: Whether the second detection value is included:
`0`: included
`1`: excluded
]
        :type IsNot2: int
        :param _Id: A rule ID is generated after a feature filtering configuration is added successfully. Leave this field empty when adding a new feature filtering configuration.
        :type Id: str
        :param _PktLenGT: Byte threshold of the packet. Packets larger than the specified size are not returned. It must be an integer larger than 1.
        :type PktLenGT: int
        """
        self._Protocol = None
        self._SportStart = None
        self._SportEnd = None
        self._DportStart = None
        self._DportEnd = None
        self._PktlenMin = None
        self._PktlenMax = None
        self._Action = None
        self._MatchBegin = None
        self._MatchType = None
        self._Str = None
        self._Depth = None
        self._Offset = None
        self._IsNot = None
        self._MatchLogic = None
        self._MatchBegin2 = None
        self._MatchType2 = None
        self._Str2 = None
        self._Depth2 = None
        self._Offset2 = None
        self._IsNot2 = None
        self._Id = None
        self._PktLenGT = None

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
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

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
    def MatchLogic(self):
        return self._MatchLogic

    @MatchLogic.setter
    def MatchLogic(self, MatchLogic):
        self._MatchLogic = MatchLogic

    @property
    def MatchBegin2(self):
        return self._MatchBegin2

    @MatchBegin2.setter
    def MatchBegin2(self, MatchBegin2):
        self._MatchBegin2 = MatchBegin2

    @property
    def MatchType2(self):
        return self._MatchType2

    @MatchType2.setter
    def MatchType2(self, MatchType2):
        self._MatchType2 = MatchType2

    @property
    def Str2(self):
        return self._Str2

    @Str2.setter
    def Str2(self, Str2):
        self._Str2 = Str2

    @property
    def Depth2(self):
        return self._Depth2

    @Depth2.setter
    def Depth2(self, Depth2):
        self._Depth2 = Depth2

    @property
    def Offset2(self):
        return self._Offset2

    @Offset2.setter
    def Offset2(self, Offset2):
        self._Offset2 = Offset2

    @property
    def IsNot2(self):
        return self._IsNot2

    @IsNot2.setter
    def IsNot2(self, IsNot2):
        self._IsNot2 = IsNot2

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PktLenGT(self):
        return self._PktLenGT

    @PktLenGT.setter
    def PktLenGT(self, PktLenGT):
        self._PktLenGT = PktLenGT


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._SportStart = params.get("SportStart")
        self._SportEnd = params.get("SportEnd")
        self._DportStart = params.get("DportStart")
        self._DportEnd = params.get("DportEnd")
        self._PktlenMin = params.get("PktlenMin")
        self._PktlenMax = params.get("PktlenMax")
        self._Action = params.get("Action")
        self._MatchBegin = params.get("MatchBegin")
        self._MatchType = params.get("MatchType")
        self._Str = params.get("Str")
        self._Depth = params.get("Depth")
        self._Offset = params.get("Offset")
        self._IsNot = params.get("IsNot")
        self._MatchLogic = params.get("MatchLogic")
        self._MatchBegin2 = params.get("MatchBegin2")
        self._MatchType2 = params.get("MatchType2")
        self._Str2 = params.get("Str2")
        self._Depth2 = params.get("Depth2")
        self._Offset2 = params.get("Offset2")
        self._IsNot2 = params.get("IsNot2")
        self._Id = params.get("Id")
        self._PktLenGT = params.get("PktLenGT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterRelation(AbstractModel):
    """Feature filtering information

    """

    def __init__(self):
        r"""
        :param _PacketFilterConfig: Feature filtering configuration
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._PacketFilterConfig = None
        self._InstanceDetailList = None
        self._ModifyTime = None

    @property
    def PacketFilterConfig(self):
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortSegment(AbstractModel):
    """Port range information

    """

    def __init__(self):
        r"""
        :param _BeginPort: Start port. Value range: 1–65535.
        :type BeginPort: int
        :param _EndPort: End port. The value should be in the range 1–65535 and cannot be less than that of the start port.
        :type EndPort: int
        """
        self._BeginPort = None
        self._EndPort = None

    @property
    def BeginPort(self):
        return self._BeginPort

    @BeginPort.setter
    def BeginPort(self, BeginPort):
        self._BeginPort = BeginPort

    @property
    def EndPort(self):
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._BeginPort = params.get("BeginPort")
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectThresholdRelation(AbstractModel):
    """Protection threshold configuration information

    """

    def __init__(self):
        r"""
        :param _DDoSLevel: DDoS protection level:
`low`: loose protection
`middle`: medium protection
`high`: strict protection
]
        :type DDoSLevel: str
        :param _DDoSThreshold: DDoS cleansing threshold (in Mbps)
        :type DDoSThreshold: int
        :param _DDoSAI: DDoS AI protection switch:
`on`: enabled
`off`: disabled
]
        :type DDoSAI: str
        :param _CCEnable: CC cleansing switch
`0`: disabled
`1`: enabled
]
        :type CCEnable: int
        :param _CCThreshold: CC cleansing threshold (in QPS)
        :type CCThreshold: int
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        :param _ListenerCcThresholdList: Domain name and protocol protection thresholds
        :type ListenerCcThresholdList: list of ListenerCcThreholdConfig
        :param _SynFloodThreshold: SYN traffic threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type SynFloodThreshold: int
        :param _SynFloodPktThreshold: SYN packet threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type SynFloodPktThreshold: int
        :param _UdpFloodThreshold: UDP traffic threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type UdpFloodThreshold: int
        :param _UdpFloodPktThreshold: UDP packet threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type UdpFloodPktThreshold: int
        :param _AckFloodThreshold: ACK traffic threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type AckFloodThreshold: int
        :param _AckFloodPktThreshold: ACK packet threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type AckFloodPktThreshold: int
        :param _SynAckFloodThreshold: SYNACK traffic threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type SynAckFloodThreshold: int
        :param _SynAckFloodPktThreshold: SYNACK packet threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type SynAckFloodPktThreshold: int
        :param _RstFloodThreshold: RST traffic threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type RstFloodThreshold: int
        :param _RstFloodPktThreshold: RST packet threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type RstFloodPktThreshold: int
        """
        self._DDoSLevel = None
        self._DDoSThreshold = None
        self._DDoSAI = None
        self._CCEnable = None
        self._CCThreshold = None
        self._InstanceDetailList = None
        self._ListenerCcThresholdList = None
        self._SynFloodThreshold = None
        self._SynFloodPktThreshold = None
        self._UdpFloodThreshold = None
        self._UdpFloodPktThreshold = None
        self._AckFloodThreshold = None
        self._AckFloodPktThreshold = None
        self._SynAckFloodThreshold = None
        self._SynAckFloodPktThreshold = None
        self._RstFloodThreshold = None
        self._RstFloodPktThreshold = None

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def DDoSThreshold(self):
        return self._DDoSThreshold

    @DDoSThreshold.setter
    def DDoSThreshold(self, DDoSThreshold):
        self._DDoSThreshold = DDoSThreshold

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI

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
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList

    @property
    def ListenerCcThresholdList(self):
        return self._ListenerCcThresholdList

    @ListenerCcThresholdList.setter
    def ListenerCcThresholdList(self, ListenerCcThresholdList):
        self._ListenerCcThresholdList = ListenerCcThresholdList

    @property
    def SynFloodThreshold(self):
        return self._SynFloodThreshold

    @SynFloodThreshold.setter
    def SynFloodThreshold(self, SynFloodThreshold):
        self._SynFloodThreshold = SynFloodThreshold

    @property
    def SynFloodPktThreshold(self):
        return self._SynFloodPktThreshold

    @SynFloodPktThreshold.setter
    def SynFloodPktThreshold(self, SynFloodPktThreshold):
        self._SynFloodPktThreshold = SynFloodPktThreshold

    @property
    def UdpFloodThreshold(self):
        return self._UdpFloodThreshold

    @UdpFloodThreshold.setter
    def UdpFloodThreshold(self, UdpFloodThreshold):
        self._UdpFloodThreshold = UdpFloodThreshold

    @property
    def UdpFloodPktThreshold(self):
        return self._UdpFloodPktThreshold

    @UdpFloodPktThreshold.setter
    def UdpFloodPktThreshold(self, UdpFloodPktThreshold):
        self._UdpFloodPktThreshold = UdpFloodPktThreshold

    @property
    def AckFloodThreshold(self):
        return self._AckFloodThreshold

    @AckFloodThreshold.setter
    def AckFloodThreshold(self, AckFloodThreshold):
        self._AckFloodThreshold = AckFloodThreshold

    @property
    def AckFloodPktThreshold(self):
        return self._AckFloodPktThreshold

    @AckFloodPktThreshold.setter
    def AckFloodPktThreshold(self, AckFloodPktThreshold):
        self._AckFloodPktThreshold = AckFloodPktThreshold

    @property
    def SynAckFloodThreshold(self):
        return self._SynAckFloodThreshold

    @SynAckFloodThreshold.setter
    def SynAckFloodThreshold(self, SynAckFloodThreshold):
        self._SynAckFloodThreshold = SynAckFloodThreshold

    @property
    def SynAckFloodPktThreshold(self):
        return self._SynAckFloodPktThreshold

    @SynAckFloodPktThreshold.setter
    def SynAckFloodPktThreshold(self, SynAckFloodPktThreshold):
        self._SynAckFloodPktThreshold = SynAckFloodPktThreshold

    @property
    def RstFloodThreshold(self):
        return self._RstFloodThreshold

    @RstFloodThreshold.setter
    def RstFloodThreshold(self, RstFloodThreshold):
        self._RstFloodThreshold = RstFloodThreshold

    @property
    def RstFloodPktThreshold(self):
        return self._RstFloodPktThreshold

    @RstFloodPktThreshold.setter
    def RstFloodPktThreshold(self, RstFloodPktThreshold):
        self._RstFloodPktThreshold = RstFloodPktThreshold


    def _deserialize(self, params):
        self._DDoSLevel = params.get("DDoSLevel")
        self._DDoSThreshold = params.get("DDoSThreshold")
        self._DDoSAI = params.get("DDoSAI")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        if params.get("ListenerCcThresholdList") is not None:
            self._ListenerCcThresholdList = []
            for item in params.get("ListenerCcThresholdList"):
                obj = ListenerCcThreholdConfig()
                obj._deserialize(item)
                self._ListenerCcThresholdList.append(obj)
        self._SynFloodThreshold = params.get("SynFloodThreshold")
        self._SynFloodPktThreshold = params.get("SynFloodPktThreshold")
        self._UdpFloodThreshold = params.get("UdpFloodThreshold")
        self._UdpFloodPktThreshold = params.get("UdpFloodPktThreshold")
        self._AckFloodThreshold = params.get("AckFloodThreshold")
        self._AckFloodPktThreshold = params.get("AckFloodPktThreshold")
        self._SynAckFloodThreshold = params.get("SynAckFloodThreshold")
        self._SynAckFloodPktThreshold = params.get("SynAckFloodPktThreshold")
        self._RstFloodThreshold = params.get("RstFloodThreshold")
        self._RstFloodPktThreshold = params.get("RstFloodPktThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockConfig(AbstractModel):
    """Protocol blocking configuration

    """

    def __init__(self):
        r"""
        :param _DropTcp: TCP blocking. Valid values: `0` (disabled), `1`(enabled).
        :type DropTcp: int
        :param _DropUdp: UDP blocking. Valid values: `0` (disabled), `1`(enabled).
        :type DropUdp: int
        :param _DropIcmp: ICMP blocking. Valid values: `0` (disabled), `1`(enabled).
        :type DropIcmp: int
        :param _DropOther: Other protocol blocking. Valid values: `0` (disabled), `1`(enabled).
        :type DropOther: int
        :param _CheckExceptNullConnect: Null connection protection. Valid values: `0` (disabled), `1` (enabled).
        :type CheckExceptNullConnect: int
        :param _PingOfDeath: PoD protection. Values: `0` (disable), `1` (enable).
        :type PingOfDeath: int
        :param _TearDrop: Teardrop protection. Values: `0` (disable), `1` (enable).
        :type TearDrop: int
        """
        self._DropTcp = None
        self._DropUdp = None
        self._DropIcmp = None
        self._DropOther = None
        self._CheckExceptNullConnect = None
        self._PingOfDeath = None
        self._TearDrop = None

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
    def CheckExceptNullConnect(self):
        return self._CheckExceptNullConnect

    @CheckExceptNullConnect.setter
    def CheckExceptNullConnect(self, CheckExceptNullConnect):
        self._CheckExceptNullConnect = CheckExceptNullConnect

    @property
    def PingOfDeath(self):
        return self._PingOfDeath

    @PingOfDeath.setter
    def PingOfDeath(self, PingOfDeath):
        self._PingOfDeath = PingOfDeath

    @property
    def TearDrop(self):
        return self._TearDrop

    @TearDrop.setter
    def TearDrop(self, TearDrop):
        self._TearDrop = TearDrop


    def _deserialize(self, params):
        self._DropTcp = params.get("DropTcp")
        self._DropUdp = params.get("DropUdp")
        self._DropIcmp = params.get("DropIcmp")
        self._DropOther = params.get("DropOther")
        self._CheckExceptNullConnect = params.get("CheckExceptNullConnect")
        self._PingOfDeath = params.get("PingOfDeath")
        self._TearDrop = params.get("TearDrop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockRelation(AbstractModel):
    """Protocol blocking information

    """

    def __init__(self):
        r"""
        :param _ProtocolBlockConfig: Protocol blocking configuration
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._ProtocolBlockConfig = None
        self._InstanceDetailList = None

    @property
    def ProtocolBlockConfig(self):
        return self._ProtocolBlockConfig

    @ProtocolBlockConfig.setter
    def ProtocolBlockConfig(self, ProtocolBlockConfig):
        self._ProtocolBlockConfig = ProtocolBlockConfig

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("ProtocolBlockConfig") is not None:
            self._ProtocolBlockConfig = ProtocolBlockConfig()
            self._ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """"Protocol" and "Port" parameters

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol. Valid values: `tcp`, `udp`
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
        


class ProxyTypeInfo(AbstractModel):
    """Forwarding type

    """

    def __init__(self):
        r"""
        :param _ProxyPorts: List of forwarding listening ports. Value range: 1–65535.
        :type ProxyPorts: list of int
        :param _ProxyType: Forwarding protocol:
`http`: HTTP protocol
`https`: HTTPS protocol
]
        :type ProxyType: str
        """
        self._ProxyPorts = None
        self._ProxyType = None

    @property
    def ProxyPorts(self):
        return self._ProxyPorts

    @ProxyPorts.setter
    def ProxyPorts(self, ProxyPorts):
        self._ProxyPorts = ProxyPorts

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType


    def _deserialize(self, params):
        self._ProxyPorts = params.get("ProxyPorts")
        self._ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """Region information.

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`
        :type Region: str
        """
        self._Region = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInstanceRelation(AbstractModel):
    """Information of the Anti-DDoS instance using layer-4/7 forwarding rules

    """

    def __init__(self):
        r"""
        :param _EipList: Instance IP
        :type EipList: list of str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Cname: Instance CNAME
        :type Cname: str
        """
        self._EipList = None
        self._InstanceId = None
        self._Cname = None

    @property
    def EipList(self):
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._EipList = params.get("EipList")
        self._InstanceId = params.get("InstanceId")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomainInfo(AbstractModel):
    """Scheduling domain name details

    """

    def __init__(self):
        r"""
        :param _Domain: Scheduling domain name
        :type Domain: str
        :param _LineIPList: List of line IPs
        :type LineIPList: list of IPLineInfo
        :param _Method: Scheduling mode. Valid value: `priority` (priority scheduling).
        :type Method: str
        :param _TTL: TTL value recorded from the scheduling domain name resolution
        :type TTL: int
        :param _Status: Running status. Valid values:
`0`: not running
`1`: running
`2`: abnormal
]
        :type Status: int
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        :param _ModifyTime: Last modification time
        :type ModifyTime: str
        :param _UsrDomainName: Domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UsrDomainName: str
        """
        self._Domain = None
        self._LineIPList = None
        self._Method = None
        self._TTL = None
        self._Status = None
        self._CreatedTime = None
        self._ModifyTime = None
        self._UsrDomainName = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LineIPList(self):
        return self._LineIPList

    @LineIPList.setter
    def LineIPList(self, LineIPList):
        self._LineIPList = LineIPList

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

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
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def UsrDomainName(self):
        return self._UsrDomainName

    @UsrDomainName.setter
    def UsrDomainName(self, UsrDomainName):
        self._UsrDomainName = UsrDomainName


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("LineIPList") is not None:
            self._LineIPList = []
            for item in params.get("LineIPList"):
                obj = IPLineInfo()
                obj._deserialize(item)
                self._LineIPList.append(obj)
        self._Method = params.get("Method")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifyTime = params.get("ModifyTime")
        self._UsrDomainName = params.get("UsrDomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceServer(AbstractModel):
    """Real server details

    """

    def __init__(self):
        r"""
        :param _RealServer: Types of the real server address, such as IP or domain name.
        :type RealServer: str
        :param _RsType: Types of the real server address:
`1`: domain name
`2`: IP
]
        :type RsType: int
        :param _Weight: Forward weight of the real server. Value range: 1–100.
        :type Weight: int
        :param _Port: Port number. Value range: 0-65535.
        :type Port: int
        """
        self._RealServer = None
        self._RsType = None
        self._Weight = None
        self._Port = None

    @property
    def RealServer(self):
        return self._RealServer

    @RealServer.setter
    def RealServer(self, RealServer):
        self._RealServer = RealServer

    @property
    def RsType(self):
        return self._RsType

    @RsType.setter
    def RsType(self, RsType):
        self._RsType = RsType

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._RealServer = params.get("RealServer")
        self._RsType = params.get("RsType")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedValue(AbstractModel):
    """Rate limit value types, such as pps and bps.

    """

    def __init__(self):
        r"""
        :param _Type: Rate limit value types:
`1`: packets per second (pps)
`2`: bits per second (bps)
]
        :type Type: int
        :param _Value: Value
        :type Value: int
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticPackRelation(AbstractModel):
    """Non-BGP package details

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: Base protection bandwidth
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProtectBandwidth: int
        :param _NormalBandwidth: Application bandwidth
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: Forwarding rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: Auto-renewal flag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AutoRenewFlag: int
        :param _CurDeadline: Expiration time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CurDeadline: str
        """
        self._ProtectBandwidth = None
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def ProtectBandwidth(self):
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def NormalBandwidth(self):
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """Return code, only used to report success.

    """

    def __init__(self):
        r"""
        :param _Message: Description
        :type Message: str
        :param _Code: Success/Error code
        :type Code: str
        """
        self._Message = None
        self._Code = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigRequest(AbstractModel):
    """SwitchWaterPrintConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Anti-DDoS instance ID
        :type InstanceId: str
        :param _OpenStatus: Watermark status. `1`: enabled; `0`: disabled.
        :type OpenStatus: int
        :param _CloudSdkProxy: Whether to enable proxy. Values: `1` (Enable proxy and ignore IP+port verification), `0` (Do not enable proxy and IP+port verification is required)
        :type CloudSdkProxy: int
        """
        self._InstanceId = None
        self._OpenStatus = None
        self._CloudSdkProxy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def CloudSdkProxy(self):
        return self._CloudSdkProxy

    @CloudSdkProxy.setter
    def CloudSdkProxy(self, CloudSdkProxy):
        self._CloudSdkProxy = CloudSdkProxy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OpenStatus = params.get("OpenStatus")
        self._CloudSdkProxy = params.get("CloudSdkProxy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigResponse(AbstractModel):
    """SwitchWaterPrintConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class TagFilter(AbstractModel):
    """Tag type

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: list of str
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
        


class TagInfo(AbstractModel):
    """Tag information, which is used to return the tag of the associated instance

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
        


class WaterPrintConfig(AbstractModel):
    """Watermark configuration

    """

    def __init__(self):
        r"""
        :param _Offset: Watermark offset. Value range: [0, 100).
        :type Offset: int
        :param _OpenStatus: Start status. Valid values:
`0`: manual start
`1`: instant start
]
        :type OpenStatus: int
        :param _Listeners: List of forwarding listeners configured
        :type Listeners: list of ForwardListener
        :param _Keys: A list of watermark keys is generated after a watermark is added successfully. Each watermark can have up to 2 keys. When there is only one valid key, it cannot be deleted.
        :type Keys: list of WaterPrintKey
        :param _Verify: Watermark checking mode, which can be:
`checkall`: normal mode
`shortfpcheckall`: compact mode
]
        :type Verify: str
        :param _CloudSdkProxy: Whether to enable proxy. Values: `1` (Enable proxy and ignore IP+port verification), `0` (Do not enable proxy and IP+port verification is required)
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloudSdkProxy: int
        """
        self._Offset = None
        self._OpenStatus = None
        self._Listeners = None
        self._Keys = None
        self._Verify = None
        self._CloudSdkProxy = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Verify(self):
        return self._Verify

    @Verify.setter
    def Verify(self, Verify):
        self._Verify = Verify

    @property
    def CloudSdkProxy(self):
        return self._CloudSdkProxy

    @CloudSdkProxy.setter
    def CloudSdkProxy(self, CloudSdkProxy):
        self._CloudSdkProxy = CloudSdkProxy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._OpenStatus = params.get("OpenStatus")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ForwardListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._Verify = params.get("Verify")
        self._CloudSdkProxy = params.get("CloudSdkProxy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """Created watermark key

    """

    def __init__(self):
        r"""
        :param _KeyVersion: Key version
        :type KeyVersion: str
        :param _KeyContent: Key content
        :type KeyContent: str
        :param _KeyId: Key ID
        :type KeyId: str
        :param _KeyOpenStatus: Key status. Valid value: `1` (enabled).
        :type KeyOpenStatus: int
        :param _CreateTime: Key creation time
        :type CreateTime: str
        """
        self._KeyVersion = None
        self._KeyContent = None
        self._KeyId = None
        self._KeyOpenStatus = None
        self._CreateTime = None

    @property
    def KeyVersion(self):
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def KeyContent(self):
        return self._KeyContent

    @KeyContent.setter
    def KeyContent(self, KeyContent):
        self._KeyContent = KeyContent

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyOpenStatus(self):
        return self._KeyOpenStatus

    @KeyOpenStatus.setter
    def KeyOpenStatus(self, KeyOpenStatus):
        self._KeyOpenStatus = KeyOpenStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._KeyVersion = params.get("KeyVersion")
        self._KeyContent = params.get("KeyContent")
        self._KeyId = params.get("KeyId")
        self._KeyOpenStatus = params.get("KeyOpenStatus")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintRelation(AbstractModel):
    """Watermark configuration details

    """

    def __init__(self):
        r"""
        :param _WaterPrintConfig: Watermark configuration
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        :param _InstanceDetailList: Anti-DDoS instance configured
        :type InstanceDetailList: list of InstanceRelation
        """
        self._WaterPrintConfig = None
        self._InstanceDetailList = None

    @property
    def WaterPrintConfig(self):
        return self._WaterPrintConfig

    @WaterPrintConfig.setter
    def WaterPrintConfig(self, WaterPrintConfig):
        self._WaterPrintConfig = WaterPrintConfig

    @property
    def InstanceDetailList(self):
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("WaterPrintConfig") is not None:
            self._WaterPrintConfig = WaterPrintConfig()
            self._WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        