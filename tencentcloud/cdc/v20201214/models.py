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


class CbsInfo(AbstractModel):
    """Information about purchased CBS

    """

    def __init__(self):
        r"""
        :param _Size: CBS storage size, in TB
        :type Size: int
        :param _Type: CBS storage type, SSD by default
        :type Type: str
        """
        self._Size = None
        self._Type = None

    @property
    def Size(self):
        """CBS storage size, in TB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        """CBS storage type, SSD by default
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosCapacity(AbstractModel):
    """Capacity of COS in CDC

    """

    def __init__(self):
        r"""
        :param _TotalCapacity: Total capacity, in GB
        :type TotalCapacity: float
        :param _TotalFreeCapacity: Available capacity, in GB
        :type TotalFreeCapacity: float
        :param _TotalUsedCapacity: Used capacity, in GB
        :type TotalUsedCapacity: float
        """
        self._TotalCapacity = None
        self._TotalFreeCapacity = None
        self._TotalUsedCapacity = None

    @property
    def TotalCapacity(self):
        """Total capacity, in GB
        :rtype: float
        """
        return self._TotalCapacity

    @TotalCapacity.setter
    def TotalCapacity(self, TotalCapacity):
        self._TotalCapacity = TotalCapacity

    @property
    def TotalFreeCapacity(self):
        """Available capacity, in GB
        :rtype: float
        """
        return self._TotalFreeCapacity

    @TotalFreeCapacity.setter
    def TotalFreeCapacity(self, TotalFreeCapacity):
        self._TotalFreeCapacity = TotalFreeCapacity

    @property
    def TotalUsedCapacity(self):
        """Used capacity, in GB
        :rtype: float
        """
        return self._TotalUsedCapacity

    @TotalUsedCapacity.setter
    def TotalUsedCapacity(self, TotalUsedCapacity):
        self._TotalUsedCapacity = TotalUsedCapacity


    def _deserialize(self, params):
        self._TotalCapacity = params.get("TotalCapacity")
        self._TotalFreeCapacity = params.get("TotalFreeCapacity")
        self._TotalUsedCapacity = params.get("TotalUsedCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInfo(AbstractModel):
    """Used to add COS information on the purchase page.

    """

    def __init__(self):
        r"""
        :param _Size: COS size, in TB
        :type Size: int
        :param _Type: COS type, COS by default
        :type Type: str
        """
        self._Size = None
        self._Type = None

    @property
    def Size(self):
        """COS size, in TB
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        """COS type, COS by default
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterOrderRequest(AbstractModel):
    """CreateDedicatedClusterOrder request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: CDC id
        :type DedicatedClusterId: str
        :param _DedicatedClusterTypes: Array of order-related CDC types
        :type DedicatedClusterTypes: list of DedicatedClusterTypeInfo
        :param _CosInfo: Order-related COS storage information
        :type CosInfo: :class:`tencentcloud.cdc.v20201214.models.CosInfo`
        :param _CbsInfo: Order-related CBS storage information
        :type CbsInfo: :class:`tencentcloud.cdc.v20201214.models.CbsInfo`
        :param _PurchaseSource: Purchase source, cloudApi by default
        :type PurchaseSource: str
        :param _DedicatedClusterOrderId: DedicatedClusterOrderId needs to be submitted when API is invoked to submit an order.
        :type DedicatedClusterOrderId: str
        """
        self._DedicatedClusterId = None
        self._DedicatedClusterTypes = None
        self._CosInfo = None
        self._CbsInfo = None
        self._PurchaseSource = None
        self._DedicatedClusterOrderId = None

    @property
    def DedicatedClusterId(self):
        """CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DedicatedClusterTypes(self):
        """Array of order-related CDC types
        :rtype: list of DedicatedClusterTypeInfo
        """
        return self._DedicatedClusterTypes

    @DedicatedClusterTypes.setter
    def DedicatedClusterTypes(self, DedicatedClusterTypes):
        self._DedicatedClusterTypes = DedicatedClusterTypes

    @property
    def CosInfo(self):
        """Order-related COS storage information
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CosInfo`
        """
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo

    @property
    def CbsInfo(self):
        """Order-related CBS storage information
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CbsInfo`
        """
        return self._CbsInfo

    @CbsInfo.setter
    def CbsInfo(self, CbsInfo):
        self._CbsInfo = CbsInfo

    @property
    def PurchaseSource(self):
        """Purchase source, cloudApi by default
        :rtype: str
        """
        return self._PurchaseSource

    @PurchaseSource.setter
    def PurchaseSource(self, PurchaseSource):
        self._PurchaseSource = PurchaseSource

    @property
    def DedicatedClusterOrderId(self):
        """DedicatedClusterOrderId needs to be submitted when API is invoked to submit an order.
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("DedicatedClusterTypes") is not None:
            self._DedicatedClusterTypes = []
            for item in params.get("DedicatedClusterTypes"):
                obj = DedicatedClusterTypeInfo()
                obj._deserialize(item)
                self._DedicatedClusterTypes.append(obj)
        if params.get("CosInfo") is not None:
            self._CosInfo = CosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        if params.get("CbsInfo") is not None:
            self._CbsInfo = CbsInfo()
            self._CbsInfo._deserialize(params.get("CbsInfo"))
        self._PurchaseSource = params.get("PurchaseSource")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterOrderResponse(AbstractModel):
    """CreateDedicatedClusterOrder response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterOrderId: CDC order id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type DedicatedClusterOrderId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterOrderId = None
        self._RequestId = None

    @property
    def DedicatedClusterOrderId(self):
        """CDC order id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._RequestId = params.get("RequestId")


class CreateDedicatedClusterRequest(AbstractModel):
    """CreateDedicatedCluster request structure.

    """

    def __init__(self):
        r"""
        :param _SiteId: SiteId to which the CDC belongs
        :type SiteId: str
        :param _Name: CDC name
        :type Name: str
        :param _Zone: AZ to which the CDC belongs
        :type Zone: str
        :param _Description: CDC description
        :type Description: str
        """
        self._SiteId = None
        self._Name = None
        self._Zone = None
        self._Description = None

    @property
    def SiteId(self):
        """SiteId to which the CDC belongs
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Name(self):
        """CDC name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        """AZ to which the CDC belongs
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """CDC description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterResponse(AbstractModel):
    """CreateDedicatedCluster response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Created CDC id
        :type DedicatedClusterId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterId = None
        self._RequestId = None

    @property
    def DedicatedClusterId(self):
        """Created CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._RequestId = params.get("RequestId")


class CreateSiteRequest(AbstractModel):
    """CreateSite request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _Country: Country where the site is located
        :type Country: str
        :param _Province: Province where the site is located
        :type Province: str
        :param _City: City where the site is located
        :type City: str
        :param _AddressLine: Detailed address of the site
        :type AddressLine: str
        :param _Description: Site description
        :type Description: str
        :param _Note: Note
        :type Note: str
        :param _FiberType: You are using optical fiber type to connect the CDC device to the network Single-mode or multi-mode fibers are available.
        :type FiberType: str
        :param _OpticalStandard: Optical standard used to connect the CDC device to the network This field depends on the uplink speed, optical fiber type, and distance to upstream equipment.
        :type OpticalStandard: str
        :param _PowerConnectors: Type of power connector
        :type PowerConnectors: str
        :param _PowerFeedDrop: Whether power is supplied from above or below the rack
        :type PowerFeedDrop: str
        :param _MaxWeight: Maximum weight capacity (KG)
        :type MaxWeight: int
        :param _PowerDrawKva: Power consumption (KW)
        :type PowerDrawKva: int
        :param _UplinkSpeedGbps: Uplink speed from the network to Tencent Cloud Region
        :type UplinkSpeedGbps: int
        :param _UplinkCount: Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :type UplinkCount: int
        :param _ConditionRequirement: Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :type ConditionRequirement: bool
        :param _DimensionRequirement: Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :type DimensionRequirement: bool
        :param _RedundantNetworking: Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :type RedundantNetworking: bool
        :param _PostalCode: Postal code of the site area
        :type PostalCode: int
        :param _OptionalAddressLine: Detailed address of the site area (to be added)
        :type OptionalAddressLine: str
        :param _NeedHelp: Whether you need help from Tencent Cloud for rack installation?
        :type NeedHelp: bool
        :param _RedundantPower: Whether there is power redundancy?
        :type RedundantPower: bool
        :param _BreakerRequirement: Whether there is an upstream circuit breaker?
        :type BreakerRequirement: bool
        """
        self._Name = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._Description = None
        self._Note = None
        self._FiberType = None
        self._OpticalStandard = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._MaxWeight = None
        self._PowerDrawKva = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._RedundantNetworking = None
        self._PostalCode = None
        self._OptionalAddressLine = None
        self._NeedHelp = None
        self._RedundantPower = None
        self._BreakerRequirement = None

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
    def Country(self):
        """Country where the site is located
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province where the site is located
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City where the site is located
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """Detailed address of the site
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def Description(self):
        """Site description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Note(self):
        """Note
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def FiberType(self):
        """You are using optical fiber type to connect the CDC device to the network Single-mode or multi-mode fibers are available.
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def OpticalStandard(self):
        """Optical standard used to connect the CDC device to the network This field depends on the uplink speed, optical fiber type, and distance to upstream equipment.
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def PowerConnectors(self):
        """Type of power connector
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """Whether power is supplied from above or below the rack
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def MaxWeight(self):
        """Maximum weight capacity (KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def PowerDrawKva(self):
        """Power consumption (KW)
        :rtype: int
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def UplinkSpeedGbps(self):
        """Uplink speed from the network to Tencent Cloud Region
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def ConditionRequirement(self):
        """Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def RedundantNetworking(self):
        """Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def PostalCode(self):
        """Postal code of the site area
        :rtype: int
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def OptionalAddressLine(self):
        """Detailed address of the site area (to be added)
        :rtype: str
        """
        return self._OptionalAddressLine

    @OptionalAddressLine.setter
    def OptionalAddressLine(self, OptionalAddressLine):
        self._OptionalAddressLine = OptionalAddressLine

    @property
    def NeedHelp(self):
        """Whether you need help from Tencent Cloud for rack installation?
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def RedundantPower(self):
        """Whether there is power redundancy?
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def BreakerRequirement(self):
        """Whether there is an upstream circuit breaker?
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._Description = params.get("Description")
        self._Note = params.get("Note")
        self._FiberType = params.get("FiberType")
        self._OpticalStandard = params.get("OpticalStandard")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._MaxWeight = params.get("MaxWeight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._PostalCode = params.get("PostalCode")
        self._OptionalAddressLine = params.get("OptionalAddressLine")
        self._NeedHelp = params.get("NeedHelp")
        self._RedundantPower = params.get("RedundantPower")
        self._BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSiteResponse(AbstractModel):
    """CreateSite response structure.

    """

    def __init__(self):
        r"""
        :param _SiteId: Created Site id
        :type SiteId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SiteId = None
        self._RequestId = None

    @property
    def SiteId(self):
        """Created Site id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._RequestId = params.get("RequestId")


class DedicatedCluster(AbstractModel):
    """CDC list

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: CDC id, e.g., cluster-xxxxx.
        :type DedicatedClusterId: str
        :param _Zone: Name of AZ to which the CDC belongs
        :type Zone: str
        :param _Description: CDC description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Description: str
        :param _Name: CDC name
        :type Name: str
        :param _LifecycleStatus: Life cycle of the CDC, e.g., PENDING.
        :type LifecycleStatus: str
        :param _CreateTime: Creation time of the CDC
        :type CreateTime: str
        :param _SiteId: Site id to which the CDC belongs
        :type SiteId: str
        """
        self._DedicatedClusterId = None
        self._Zone = None
        self._Description = None
        self._Name = None
        self._LifecycleStatus = None
        self._CreateTime = None
        self._SiteId = None

    @property
    def DedicatedClusterId(self):
        """CDC id, e.g., cluster-xxxxx.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Zone(self):
        """Name of AZ to which the CDC belongs
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """CDC description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """CDC name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LifecycleStatus(self):
        """Life cycle of the CDC, e.g., PENDING.
        :rtype: str
        """
        return self._LifecycleStatus

    @LifecycleStatus.setter
    def LifecycleStatus(self, LifecycleStatus):
        self._LifecycleStatus = LifecycleStatus

    @property
    def CreateTime(self):
        """Creation time of the CDC
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SiteId(self):
        """Site id to which the CDC belongs
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._LifecycleStatus = params.get("LifecycleStatus")
        self._CreateTime = params.get("CreateTime")
        self._SiteId = params.get("SiteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterInstanceType(AbstractModel):
    """List of instance specifications supported by the CDC host

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _InstanceType: Type name
        :type InstanceType: str
        :param _NetworkCard: NIC type, e.g., 25 represents a 25 GB NIC.
        :type NetworkCard: int
        :param _Cpu: Number of CPU cores of instance, in cores
        :type Cpu: int
        :param _Memory: Memory capacity of instance, in GB
        :type Memory: int
        :param _InstanceFamily: Instance family
        :type InstanceFamily: str
        :param _TypeName: Type name
        :type TypeName: str
        :param _StorageBlockAmount: Local storage block count
        :type StorageBlockAmount: int
        :param _InstanceBandwidth: LAN bandwidth, in GB/s
        :type InstanceBandwidth: float
        :param _InstancePps: Network packet receiving/sending capacity, in 10,000 PPS
        :type InstancePps: int
        :param _CpuType: Processor type
        :type CpuType: str
        :param _Gpu: Number of GPUs of instance
        :type Gpu: int
        :param _Fpga: Number of FPGAs of instance.
        :type Fpga: int
        :param _Remark: Type description
        :type Remark: str
        :param _Status: Whether the instance is for sale? Value values: <br><li>SELL: Indicates that the instance is for sale. <br><li>SOLD_OUT: Indicates that the instance has been sold out.
        :type Status: str
        """
        self._Zone = None
        self._InstanceType = None
        self._NetworkCard = None
        self._Cpu = None
        self._Memory = None
        self._InstanceFamily = None
        self._TypeName = None
        self._StorageBlockAmount = None
        self._InstanceBandwidth = None
        self._InstancePps = None
        self._CpuType = None
        self._Gpu = None
        self._Fpga = None
        self._Remark = None
        self._Status = None

    @property
    def Zone(self):
        """AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """Type name
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def NetworkCard(self):
        """NIC type, e.g., 25 represents a 25 GB NIC.
        :rtype: int
        """
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Cpu(self):
        """Number of CPU cores of instance, in cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory capacity of instance, in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceFamily(self):
        """Instance family
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        """Type name
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StorageBlockAmount(self):
        """Local storage block count
        :rtype: int
        """
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def InstanceBandwidth(self):
        """LAN bandwidth, in GB/s
        :rtype: float
        """
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        """Network packet receiving/sending capacity, in 10,000 PPS
        :rtype: int
        """
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def CpuType(self):
        """Processor type
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        """Number of GPUs of instance
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        """Number of FPGAs of instance.
        :rtype: int
        """
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        """Type description
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        """Whether the instance is for sale? Value values: <br><li>SELL: Indicates that the instance is for sale. <br><li>SOLD_OUT: Indicates that the instance has been sold out.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._NetworkCard = params.get("NetworkCard")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceFamily = params.get("InstanceFamily")
        self._TypeName = params.get("TypeName")
        self._StorageBlockAmount = params.get("StorageBlockAmount")
        self._InstanceBandwidth = params.get("InstanceBandwidth")
        self._InstancePps = params.get("InstancePps")
        self._CpuType = params.get("CpuType")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrder(AbstractModel):
    """CDC order

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: CDC id
        :type DedicatedClusterId: str
        :param _DedicatedClusterTypeId: CDC type id (moved to the next level, obsolete and will be deleted later)
        :type DedicatedClusterTypeId: str
        :param _SupportedStorageType: List of supported storage types (moved to the next level, obsolete and will be deleted later)
        :type SupportedStorageType: list of str
        :param _SupportedUplinkSpeed: Supported uplink switch transmission rate (GiB) (moved to the next level, obsolete and will be deleted later)
        :type SupportedUplinkSpeed: list of int
        :param _SupportedInstanceFamily: List of supported instance families (moved to the next level, obsolete and will be deleted later)
        :type SupportedInstanceFamily: list of str
        :param _Weight: Floor weight capacity (KG)
        :type Weight: int
        :param _PowerDraw: Power requirements (KW)
        :type PowerDraw: float
        :param _OrderStatus: Order status
        :type OrderStatus: str
        :param _CreateTime: Order creation time
        :type CreateTime: str
        :param _DedicatedClusterOrderId: Large order ID
        :type DedicatedClusterOrderId: str
        :param _Action: Order type, CREATE or EXTEND
        :type Action: str
        :param _DedicatedClusterOrderItems: List of sub-order details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type DedicatedClusterOrderItems: list of DedicatedClusterOrderItem
        :param _Cpu: CPU value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Cpu: int
        :param _Mem: MEM value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Mem: int
        :param _Gpu: GPU value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Gpu: int
        :param _PayStatus: 0 for unpaid, 1 for paid 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type PayStatus: int
        :param _PayType: Payment method: lump-sum, monthly, and annually 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type PayType: str
        :param _TimeUnit: Unit of purchased period 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type TimeUnit: str
        :param _TimeSpan: Purchased period 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type TimeSpan: int
        :param _OrderType: Order type 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type OrderType: str
        :param _CheckStatus: 
        :type CheckStatus: str
        :param _DeliverExpectTime: 
        :type DeliverExpectTime: str
        :param _DeliverFinishTime: 
        :type DeliverFinishTime: str
        :param _CheckExpectTime: 
        :type CheckExpectTime: str
        :param _CheckFinishTime: 
        :type CheckFinishTime: str
        :param _OrderSLA: 
        :type OrderSLA: str
        :param _OrderPayPlan: 
        :type OrderPayPlan: str
        """
        self._DedicatedClusterId = None
        self._DedicatedClusterTypeId = None
        self._SupportedStorageType = None
        self._SupportedUplinkSpeed = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDraw = None
        self._OrderStatus = None
        self._CreateTime = None
        self._DedicatedClusterOrderId = None
        self._Action = None
        self._DedicatedClusterOrderItems = None
        self._Cpu = None
        self._Mem = None
        self._Gpu = None
        self._PayStatus = None
        self._PayType = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._OrderType = None
        self._CheckStatus = None
        self._DeliverExpectTime = None
        self._DeliverFinishTime = None
        self._CheckExpectTime = None
        self._CheckFinishTime = None
        self._OrderSLA = None
        self._OrderPayPlan = None

    @property
    def DedicatedClusterId(self):
        """CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def DedicatedClusterTypeId(self):
        """CDC type id (moved to the next level, obsolete and will be deleted later)
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def SupportedStorageType(self):
        """List of supported storage types (moved to the next level, obsolete and will be deleted later)
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkSpeed(self):
        """Supported uplink switch transmission rate (GiB) (moved to the next level, obsolete and will be deleted later)
        :rtype: list of int
        """
        return self._SupportedUplinkSpeed

    @SupportedUplinkSpeed.setter
    def SupportedUplinkSpeed(self, SupportedUplinkSpeed):
        self._SupportedUplinkSpeed = SupportedUplinkSpeed

    @property
    def SupportedInstanceFamily(self):
        """List of supported instance families (moved to the next level, obsolete and will be deleted later)
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """Floor weight capacity (KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDraw(self):
        """Power requirements (KW)
        :rtype: float
        """
        return self._PowerDraw

    @PowerDraw.setter
    def PowerDraw(self, PowerDraw):
        self._PowerDraw = PowerDraw

    @property
    def OrderStatus(self):
        """Order status
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def CreateTime(self):
        """Order creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DedicatedClusterOrderId(self):
        """Large order ID
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

    @property
    def Action(self):
        """Order type, CREATE or EXTEND
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def DedicatedClusterOrderItems(self):
        """List of sub-order details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of DedicatedClusterOrderItem
        """
        return self._DedicatedClusterOrderItems

    @DedicatedClusterOrderItems.setter
    def DedicatedClusterOrderItems(self, DedicatedClusterOrderItems):
        self._DedicatedClusterOrderItems = DedicatedClusterOrderItems

    @property
    def Cpu(self):
        """CPU value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """MEM value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Gpu(self):
        """GPU value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def PayStatus(self):
        """0 for unpaid, 1 for paid 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._PayStatus

    @PayStatus.setter
    def PayStatus(self, PayStatus):
        self._PayStatus = PayStatus

    @property
    def PayType(self):
        """Payment method: lump-sum, monthly, and annually 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def TimeUnit(self):
        """Unit of purchased period 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Purchased period 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def OrderType(self):
        """Order type 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def CheckStatus(self):
        """
        :rtype: str
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def DeliverExpectTime(self):
        """
        :rtype: str
        """
        return self._DeliverExpectTime

    @DeliverExpectTime.setter
    def DeliverExpectTime(self, DeliverExpectTime):
        self._DeliverExpectTime = DeliverExpectTime

    @property
    def DeliverFinishTime(self):
        """
        :rtype: str
        """
        return self._DeliverFinishTime

    @DeliverFinishTime.setter
    def DeliverFinishTime(self, DeliverFinishTime):
        self._DeliverFinishTime = DeliverFinishTime

    @property
    def CheckExpectTime(self):
        """
        :rtype: str
        """
        return self._CheckExpectTime

    @CheckExpectTime.setter
    def CheckExpectTime(self, CheckExpectTime):
        self._CheckExpectTime = CheckExpectTime

    @property
    def CheckFinishTime(self):
        """
        :rtype: str
        """
        return self._CheckFinishTime

    @CheckFinishTime.setter
    def CheckFinishTime(self, CheckFinishTime):
        self._CheckFinishTime = CheckFinishTime

    @property
    def OrderSLA(self):
        """
        :rtype: str
        """
        return self._OrderSLA

    @OrderSLA.setter
    def OrderSLA(self, OrderSLA):
        self._OrderSLA = OrderSLA

    @property
    def OrderPayPlan(self):
        """
        :rtype: str
        """
        return self._OrderPayPlan

    @OrderPayPlan.setter
    def OrderPayPlan(self, OrderPayPlan):
        self._OrderPayPlan = OrderPayPlan


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDraw = params.get("PowerDraw")
        self._OrderStatus = params.get("OrderStatus")
        self._CreateTime = params.get("CreateTime")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._Action = params.get("Action")
        if params.get("DedicatedClusterOrderItems") is not None:
            self._DedicatedClusterOrderItems = []
            for item in params.get("DedicatedClusterOrderItems"):
                obj = DedicatedClusterOrderItem()
                obj._deserialize(item)
                self._DedicatedClusterOrderItems.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Gpu = params.get("Gpu")
        self._PayStatus = params.get("PayStatus")
        self._PayType = params.get("PayType")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._OrderType = params.get("OrderType")
        self._CheckStatus = params.get("CheckStatus")
        self._DeliverExpectTime = params.get("DeliverExpectTime")
        self._DeliverFinishTime = params.get("DeliverFinishTime")
        self._CheckExpectTime = params.get("CheckExpectTime")
        self._CheckFinishTime = params.get("CheckFinishTime")
        self._OrderSLA = params.get("OrderSLA")
        self._OrderPayPlan = params.get("OrderPayPlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterOrderItem(AbstractModel):
    """CDC sub-order

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeId: CDC type id
        :type DedicatedClusterTypeId: str
        :param _SupportedStorageType: List of supported storage types
        :type SupportedStorageType: list of str
        :param _SupportedUplinkSpeed: Supported uplink switch transmission rate (GiB)
        :type SupportedUplinkSpeed: list of int
        :param _SupportedInstanceFamily: List of supported instance families
        :type SupportedInstanceFamily: list of str
        :param _Weight: Floor weight capacity (KG)
        :type Weight: int
        :param _PowerDraw: Power requirements (KW)
        :type PowerDraw: float
        :param _SubOrderStatus: Order status
        :type SubOrderStatus: str
        :param _CreateTime: Order creation time
        :type CreateTime: str
        :param _SubOrderId: Sub-order ID
        :type SubOrderId: str
        :param _Count: Number of linked cluster types
        :type Count: int
        :param _Name: Brief description of type
        :type Name: str
        :param _Description: Detailed description of type
        :type Description: str
        :param _TotalCpu: Number of CPUs
        :type TotalCpu: int
        :param _TotalMem: Number of memories
        :type TotalMem: int
        :param _TotalGpu: Total GPUs
        :type TotalGpu: int
        :param _TypeName: English type name
        :type TypeName: str
        :param _ComputeFormat: Type display 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type ComputeFormat: str
        :param _TypeFamily: Type family 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type TypeFamily: str
        :param _SubOrderPayStatus: 0 for unpaid, 1 for paid 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type SubOrderPayStatus: int
        """
        self._DedicatedClusterTypeId = None
        self._SupportedStorageType = None
        self._SupportedUplinkSpeed = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDraw = None
        self._SubOrderStatus = None
        self._CreateTime = None
        self._SubOrderId = None
        self._Count = None
        self._Name = None
        self._Description = None
        self._TotalCpu = None
        self._TotalMem = None
        self._TotalGpu = None
        self._TypeName = None
        self._ComputeFormat = None
        self._TypeFamily = None
        self._SubOrderPayStatus = None

    @property
    def DedicatedClusterTypeId(self):
        """CDC type id
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def SupportedStorageType(self):
        """List of supported storage types
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkSpeed(self):
        """Supported uplink switch transmission rate (GiB)
        :rtype: list of int
        """
        return self._SupportedUplinkSpeed

    @SupportedUplinkSpeed.setter
    def SupportedUplinkSpeed(self, SupportedUplinkSpeed):
        self._SupportedUplinkSpeed = SupportedUplinkSpeed

    @property
    def SupportedInstanceFamily(self):
        """List of supported instance families
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """Floor weight capacity (KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDraw(self):
        """Power requirements (KW)
        :rtype: float
        """
        return self._PowerDraw

    @PowerDraw.setter
    def PowerDraw(self, PowerDraw):
        self._PowerDraw = PowerDraw

    @property
    def SubOrderStatus(self):
        """Order status
        :rtype: str
        """
        return self._SubOrderStatus

    @SubOrderStatus.setter
    def SubOrderStatus(self, SubOrderStatus):
        self._SubOrderStatus = SubOrderStatus

    @property
    def CreateTime(self):
        """Order creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SubOrderId(self):
        """Sub-order ID
        :rtype: str
        """
        return self._SubOrderId

    @SubOrderId.setter
    def SubOrderId(self, SubOrderId):
        self._SubOrderId = SubOrderId

    @property
    def Count(self):
        """Number of linked cluster types
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Name(self):
        """Brief description of type
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Detailed description of type
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TotalCpu(self):
        """Number of CPUs
        :rtype: int
        """
        return self._TotalCpu

    @TotalCpu.setter
    def TotalCpu(self, TotalCpu):
        self._TotalCpu = TotalCpu

    @property
    def TotalMem(self):
        """Number of memories
        :rtype: int
        """
        return self._TotalMem

    @TotalMem.setter
    def TotalMem(self, TotalMem):
        self._TotalMem = TotalMem

    @property
    def TotalGpu(self):
        """Total GPUs
        :rtype: int
        """
        return self._TotalGpu

    @TotalGpu.setter
    def TotalGpu(self, TotalGpu):
        self._TotalGpu = TotalGpu

    @property
    def TypeName(self):
        """English type name
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def ComputeFormat(self):
        """Type display 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._ComputeFormat

    @ComputeFormat.setter
    def ComputeFormat(self, ComputeFormat):
        self._ComputeFormat = ComputeFormat

    @property
    def TypeFamily(self):
        """Type family 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._TypeFamily

    @TypeFamily.setter
    def TypeFamily(self, TypeFamily):
        self._TypeFamily = TypeFamily

    @property
    def SubOrderPayStatus(self):
        """0 for unpaid, 1 for paid 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: int
        """
        return self._SubOrderPayStatus

    @SubOrderPayStatus.setter
    def SubOrderPayStatus(self, SubOrderPayStatus):
        self._SubOrderPayStatus = SubOrderPayStatus


    def _deserialize(self, params):
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkSpeed = params.get("SupportedUplinkSpeed")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDraw = params.get("PowerDraw")
        self._SubOrderStatus = params.get("SubOrderStatus")
        self._CreateTime = params.get("CreateTime")
        self._SubOrderId = params.get("SubOrderId")
        self._Count = params.get("Count")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._TotalCpu = params.get("TotalCpu")
        self._TotalMem = params.get("TotalMem")
        self._TotalGpu = params.get("TotalGpu")
        self._TypeName = params.get("TypeName")
        self._ComputeFormat = params.get("ComputeFormat")
        self._TypeFamily = params.get("TypeFamily")
        self._SubOrderPayStatus = params.get("SubOrderPayStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterType(AbstractModel):
    """CDC configurations

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeId: Configuration id
        :type DedicatedClusterTypeId: str
        :param _Description: Configuration description, corresponding to description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Description: str
        :param _Name: Configuration name, corresponding to computing resource type
        :type Name: str
        :param _CreateTime: Configuration creation time
        :type CreateTime: str
        :param _SupportedStorageType: List of supported storage types
        :type SupportedStorageType: list of str
        :param _SupportedUplinkGiB: Supported uplink switch transmission rate
        :type SupportedUplinkGiB: list of int
        :param _SupportedInstanceFamily: List of supported instance families
        :type SupportedInstanceFamily: list of str
        :param _Weight: Floor weight capacity (KG)
        :type Weight: int
        :param _PowerDrawKva: Power requirements (KW)
        :type PowerDrawKva: float
        :param _ComputeFormatDesc: Displays the details of computing resource types, and does not display resources such as storage; corresponding to type
        :type ComputeFormatDesc: str
        """
        self._DedicatedClusterTypeId = None
        self._Description = None
        self._Name = None
        self._CreateTime = None
        self._SupportedStorageType = None
        self._SupportedUplinkGiB = None
        self._SupportedInstanceFamily = None
        self._Weight = None
        self._PowerDrawKva = None
        self._ComputeFormatDesc = None

    @property
    def DedicatedClusterTypeId(self):
        """Configuration id
        :rtype: str
        """
        return self._DedicatedClusterTypeId

    @DedicatedClusterTypeId.setter
    def DedicatedClusterTypeId(self, DedicatedClusterTypeId):
        self._DedicatedClusterTypeId = DedicatedClusterTypeId

    @property
    def Description(self):
        """Configuration description, corresponding to description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """Configuration name, corresponding to computing resource type
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        """Configuration creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SupportedStorageType(self):
        """List of supported storage types
        :rtype: list of str
        """
        return self._SupportedStorageType

    @SupportedStorageType.setter
    def SupportedStorageType(self, SupportedStorageType):
        self._SupportedStorageType = SupportedStorageType

    @property
    def SupportedUplinkGiB(self):
        """Supported uplink switch transmission rate
        :rtype: list of int
        """
        return self._SupportedUplinkGiB

    @SupportedUplinkGiB.setter
    def SupportedUplinkGiB(self, SupportedUplinkGiB):
        self._SupportedUplinkGiB = SupportedUplinkGiB

    @property
    def SupportedInstanceFamily(self):
        """List of supported instance families
        :rtype: list of str
        """
        return self._SupportedInstanceFamily

    @SupportedInstanceFamily.setter
    def SupportedInstanceFamily(self, SupportedInstanceFamily):
        self._SupportedInstanceFamily = SupportedInstanceFamily

    @property
    def Weight(self):
        """Floor weight capacity (KG)
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PowerDrawKva(self):
        """Power requirements (KW)
        :rtype: float
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def ComputeFormatDesc(self):
        """Displays the details of computing resource types, and does not display resources such as storage; corresponding to type
        :rtype: str
        """
        return self._ComputeFormatDesc

    @ComputeFormatDesc.setter
    def ComputeFormatDesc(self, ComputeFormatDesc):
        self._ComputeFormatDesc = ComputeFormatDesc


    def _deserialize(self, params):
        self._DedicatedClusterTypeId = params.get("DedicatedClusterTypeId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._SupportedStorageType = params.get("SupportedStorageType")
        self._SupportedUplinkGiB = params.get("SupportedUplinkGiB")
        self._SupportedInstanceFamily = params.get("SupportedInstanceFamily")
        self._Weight = params.get("Weight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._ComputeFormatDesc = params.get("ComputeFormatDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DedicatedClusterTypeInfo(AbstractModel):
    """DedicatedClusterType => (Id, Count)

    """

    def __init__(self):
        r"""
        :param _Id: Cluster type id
        :type Id: str
        :param _Count: Cluster type count
        :type Count: int
        """
        self._Id = None
        self._Count = None

    @property
    def Id(self):
        """Cluster type id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Count(self):
        """Cluster type count
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClustersRequest(AbstractModel):
    """DeleteDedicatedClusters request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: CDC id to be deleted
        :type DedicatedClusterIds: list of str
        """
        self._DedicatedClusterIds = None

    @property
    def DedicatedClusterIds(self):
        """CDC id to be deleted
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDedicatedClustersResponse(AbstractModel):
    """DeleteDedicatedClusters response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSitesRequest(AbstractModel):
    """DeleteSites request structure.

    """

    def __init__(self):
        r"""
        :param _SiteIds: List of site ids to be deleted
        :type SiteIds: list of str
        """
        self._SiteIds = None

    @property
    def SiteIds(self):
        """List of site ids to be deleted
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSitesResponse(AbstractModel):
    """DeleteSites response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterCosCapacityRequest(AbstractModel):
    """DescribeDedicatedClusterCosCapacity request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Queried CDC id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """Queried CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterCosCapacityResponse(AbstractModel):
    """DescribeDedicatedClusterCosCapacity response structure.

    """

    def __init__(self):
        r"""
        :param _CosCapacity: Cluster COS capacity, in GB
        :type CosCapacity: :class:`tencentcloud.cdc.v20201214.models.CosCapacity`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosCapacity = None
        self._RequestId = None

    @property
    def CosCapacity(self):
        """Cluster COS capacity, in GB
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CosCapacity`
        """
        return self._CosCapacity

    @CosCapacity.setter
    def CosCapacity(self, CosCapacity):
        self._CosCapacity = CosCapacity

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CosCapacity") is not None:
            self._CosCapacity = CosCapacity()
            self._CosCapacity._deserialize(params.get("CosCapacity"))
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostStatisticsRequest(AbstractModel):
    """DescribeDedicatedClusterHostStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Queried CDC id
        :type DedicatedClusterId: str
        :param _HostId: Host id
        :type HostId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Period: Time range accuracy, 1 min/5 min
        :type Period: str
        """
        self._DedicatedClusterId = None
        self._HostId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def DedicatedClusterId(self):
        """Queried CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def HostId(self):
        """Host id
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

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
    def Period(self):
        """Time range accuracy, 1 min/5 min
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._HostId = params.get("HostId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostStatisticsResponse(AbstractModel):
    """DescribeDedicatedClusterHostStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _HostStatisticSet: List of statistic information of the cluster host
        :type HostStatisticSet: list of HostStatistic
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HostStatisticSet = None
        self._RequestId = None

    @property
    def HostStatisticSet(self):
        """List of statistic information of the cluster host
        :rtype: list of HostStatistic
        """
        return self._HostStatisticSet

    @HostStatisticSet.setter
    def HostStatisticSet(self, HostStatisticSet):
        self._HostStatisticSet = HostStatisticSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HostStatisticSet") is not None:
            self._HostStatisticSet = []
            for item in params.get("HostStatisticSet"):
                obj = HostStatistic()
                obj._deserialize(item)
                self._HostStatisticSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterHostsRequest(AbstractModel):
    """DescribeDedicatedClusterHosts request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Cluster id
        :type DedicatedClusterId: str
        :param _Offset: Offset, 0 by default
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default
        :type Limit: int
        """
        self._DedicatedClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def DedicatedClusterId(self):
        """Cluster id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Offset(self):
        """Offset, 0 by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterHostsResponse(AbstractModel):
    """DescribeDedicatedClusterHosts response structure.

    """

    def __init__(self):
        r"""
        :param _HostInfoSet: Host information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type HostInfoSet: list of HostInfo
        :param _TotalCount: Total number of hosts
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HostInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HostInfoSet(self):
        """Host information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of HostInfo
        """
        return self._HostInfoSet

    @HostInfoSet.setter
    def HostInfoSet(self, HostInfoSet):
        self._HostInfoSet = HostInfoSet

    @property
    def TotalCount(self):
        """Total number of hosts
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HostInfoSet") is not None:
            self._HostInfoSet = []
            for item in params.get("HostInfoSet"):
                obj = HostInfo()
                obj._deserialize(item)
                self._HostInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterInstanceTypesRequest(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Queried CDC id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """Queried CDC id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterInstanceTypesResponse(AbstractModel):
    """DescribeDedicatedClusterInstanceTypes response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterInstanceTypeSet: List of supported instance types
        :type DedicatedClusterInstanceTypeSet: list of DedicatedClusterInstanceType
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterInstanceTypeSet = None
        self._RequestId = None

    @property
    def DedicatedClusterInstanceTypeSet(self):
        """List of supported instance types
        :rtype: list of DedicatedClusterInstanceType
        """
        return self._DedicatedClusterInstanceTypeSet

    @DedicatedClusterInstanceTypeSet.setter
    def DedicatedClusterInstanceTypeSet(self, DedicatedClusterInstanceTypeSet):
        self._DedicatedClusterInstanceTypeSet = DedicatedClusterInstanceTypeSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DedicatedClusterInstanceTypeSet") is not None:
            self._DedicatedClusterInstanceTypeSet = []
            for item in params.get("DedicatedClusterInstanceTypeSet"):
                obj = DedicatedClusterInstanceType()
                obj._deserialize(item)
                self._DedicatedClusterInstanceTypeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterOrdersRequest(AbstractModel):
    """DescribeDedicatedClusterOrders request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: Filter by CDC id.
        :type DedicatedClusterIds: list of str
        :param _DedicatedClusterOrderIds: Filter by CDC order id.
        :type DedicatedClusterOrderIds: str
        :param _Offset: Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Status: The order status is the filter condition: PENDING INCONSTRUCTION DELIVERING DELIVERED EXPIRED CANCELLED OFFLINE
        :type Status: str
        :param _ActionType: The order type is the filter condition: CREATE EXTEND
        :type ActionType: str
        :param _OrderTypes: 
        :type OrderTypes: list of str
        """
        self._DedicatedClusterIds = None
        self._DedicatedClusterOrderIds = None
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ActionType = None
        self._OrderTypes = None

    @property
    def DedicatedClusterIds(self):
        """Filter by CDC id.
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds

    @property
    def DedicatedClusterOrderIds(self):
        """Filter by CDC order id.
        :rtype: str
        """
        return self._DedicatedClusterOrderIds

    @DedicatedClusterOrderIds.setter
    def DedicatedClusterOrderIds(self, DedicatedClusterOrderIds):
        self._DedicatedClusterOrderIds = DedicatedClusterOrderIds

    @property
    def Offset(self):
        """Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """The order status is the filter condition: PENDING INCONSTRUCTION DELIVERING DELIVERED EXPIRED CANCELLED OFFLINE
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActionType(self):
        """The order type is the filter condition: CREATE EXTEND
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def OrderTypes(self):
        """
        :rtype: list of str
        """
        return self._OrderTypes

    @OrderTypes.setter
    def OrderTypes(self, OrderTypes):
        self._OrderTypes = OrderTypes


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        self._DedicatedClusterOrderIds = params.get("DedicatedClusterOrderIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ActionType = params.get("ActionType")
        self._OrderTypes = params.get("OrderTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOrdersResponse(AbstractModel):
    """DescribeDedicatedClusterOrders response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterOrderSet: List of CDC orders
        :type DedicatedClusterOrderSet: list of DedicatedClusterOrder
        :param _TotalCount: Total number of CDC orders that meet the conditions
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterOrderSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterOrderSet(self):
        """List of CDC orders
        :rtype: list of DedicatedClusterOrder
        """
        return self._DedicatedClusterOrderSet

    @DedicatedClusterOrderSet.setter
    def DedicatedClusterOrderSet(self, DedicatedClusterOrderSet):
        self._DedicatedClusterOrderSet = DedicatedClusterOrderSet

    @property
    def TotalCount(self):
        """Total number of CDC orders that meet the conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DedicatedClusterOrderSet") is not None:
            self._DedicatedClusterOrderSet = []
            for item in params.get("DedicatedClusterOrderSet"):
                obj = DedicatedClusterOrder()
                obj._deserialize(item)
                self._DedicatedClusterOrderSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterOverviewRequest(AbstractModel):
    """DescribeDedicatedClusterOverview request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: Cluster id
        :type DedicatedClusterId: str
        """
        self._DedicatedClusterId = None

    @property
    def DedicatedClusterId(self):
        """Cluster id
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterOverviewResponse(AbstractModel):
    """DescribeDedicatedClusterOverview response structure.

    """

    def __init__(self):
        r"""
        :param _CvmCount: Number of CVMs
        :type CvmCount: int
        :param _HostCount: Number of hosts
        :type HostCount: int
        :param _VpnConnectionState: VPN channel status 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type VpnConnectionState: str
        :param _VpngwBandwidthData: VPN gateway monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type VpngwBandwidthData: :class:`tencentcloud.cdc.v20201214.models.VpngwBandwidthData`
        :param _LocalNetInfo: Local gateway information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type LocalNetInfo: :class:`tencentcloud.cdc.v20201214.models.LocalNetInfo`
        :param _VpnConnectionBandwidthData: VPN gateway channel monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type VpnConnectionBandwidthData: list of VpngwBandwidthData
        :param _HostDetailInfo: 
        :type HostDetailInfo: list of HostDetailInfo
        :param _HostStandbyCount: 
        :type HostStandbyCount: int
        :param _HostNormalCount: 
        :type HostNormalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CvmCount = None
        self._HostCount = None
        self._VpnConnectionState = None
        self._VpngwBandwidthData = None
        self._LocalNetInfo = None
        self._VpnConnectionBandwidthData = None
        self._HostDetailInfo = None
        self._HostStandbyCount = None
        self._HostNormalCount = None
        self._RequestId = None

    @property
    def CvmCount(self):
        """Number of CVMs
        :rtype: int
        """
        return self._CvmCount

    @CvmCount.setter
    def CvmCount(self, CvmCount):
        self._CvmCount = CvmCount

    @property
    def HostCount(self):
        """Number of hosts
        :rtype: int
        """
        return self._HostCount

    @HostCount.setter
    def HostCount(self, HostCount):
        self._HostCount = HostCount

    @property
    def VpnConnectionState(self):
        """VPN channel status 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._VpnConnectionState

    @VpnConnectionState.setter
    def VpnConnectionState(self, VpnConnectionState):
        self._VpnConnectionState = VpnConnectionState

    @property
    def VpngwBandwidthData(self):
        """VPN gateway monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.VpngwBandwidthData`
        """
        return self._VpngwBandwidthData

    @VpngwBandwidthData.setter
    def VpngwBandwidthData(self, VpngwBandwidthData):
        self._VpngwBandwidthData = VpngwBandwidthData

    @property
    def LocalNetInfo(self):
        """Local gateway information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.LocalNetInfo`
        """
        return self._LocalNetInfo

    @LocalNetInfo.setter
    def LocalNetInfo(self, LocalNetInfo):
        self._LocalNetInfo = LocalNetInfo

    @property
    def VpnConnectionBandwidthData(self):
        """VPN gateway channel monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of VpngwBandwidthData
        """
        return self._VpnConnectionBandwidthData

    @VpnConnectionBandwidthData.setter
    def VpnConnectionBandwidthData(self, VpnConnectionBandwidthData):
        self._VpnConnectionBandwidthData = VpnConnectionBandwidthData

    @property
    def HostDetailInfo(self):
        """
        :rtype: list of HostDetailInfo
        """
        return self._HostDetailInfo

    @HostDetailInfo.setter
    def HostDetailInfo(self, HostDetailInfo):
        self._HostDetailInfo = HostDetailInfo

    @property
    def HostStandbyCount(self):
        """
        :rtype: int
        """
        return self._HostStandbyCount

    @HostStandbyCount.setter
    def HostStandbyCount(self, HostStandbyCount):
        self._HostStandbyCount = HostStandbyCount

    @property
    def HostNormalCount(self):
        """
        :rtype: int
        """
        return self._HostNormalCount

    @HostNormalCount.setter
    def HostNormalCount(self, HostNormalCount):
        self._HostNormalCount = HostNormalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CvmCount = params.get("CvmCount")
        self._HostCount = params.get("HostCount")
        self._VpnConnectionState = params.get("VpnConnectionState")
        if params.get("VpngwBandwidthData") is not None:
            self._VpngwBandwidthData = VpngwBandwidthData()
            self._VpngwBandwidthData._deserialize(params.get("VpngwBandwidthData"))
        if params.get("LocalNetInfo") is not None:
            self._LocalNetInfo = LocalNetInfo()
            self._LocalNetInfo._deserialize(params.get("LocalNetInfo"))
        if params.get("VpnConnectionBandwidthData") is not None:
            self._VpnConnectionBandwidthData = []
            for item in params.get("VpnConnectionBandwidthData"):
                obj = VpngwBandwidthData()
                obj._deserialize(item)
                self._VpnConnectionBandwidthData.append(obj)
        if params.get("HostDetailInfo") is not None:
            self._HostDetailInfo = []
            for item in params.get("HostDetailInfo"):
                obj = HostDetailInfo()
                obj._deserialize(item)
                self._HostDetailInfo.append(obj)
        self._HostStandbyCount = params.get("HostStandbyCount")
        self._HostNormalCount = params.get("HostNormalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClusterTypesRequest(AbstractModel):
    """DescribeDedicatedClusterTypes request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name of fuzzy matching CDC configuration
        :type Name: str
        :param _DedicatedClusterTypeIds: List of CDC configuration ids to be queried
        :type DedicatedClusterTypeIds: list of str
        :param _Offset: Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _IsCompute: Whether to query only the computing type?
        :type IsCompute: bool
        """
        self._Name = None
        self._DedicatedClusterTypeIds = None
        self._Offset = None
        self._Limit = None
        self._IsCompute = None

    @property
    def Name(self):
        """Name of fuzzy matching CDC configuration
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DedicatedClusterTypeIds(self):
        """List of CDC configuration ids to be queried
        :rtype: list of str
        """
        return self._DedicatedClusterTypeIds

    @DedicatedClusterTypeIds.setter
    def DedicatedClusterTypeIds(self, DedicatedClusterTypeIds):
        self._DedicatedClusterTypeIds = DedicatedClusterTypeIds

    @property
    def Offset(self):
        """Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IsCompute(self):
        """Whether to query only the computing type?
        :rtype: bool
        """
        return self._IsCompute

    @IsCompute.setter
    def IsCompute(self, IsCompute):
        self._IsCompute = IsCompute


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DedicatedClusterTypeIds = params.get("DedicatedClusterTypeIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IsCompute = params.get("IsCompute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClusterTypesResponse(AbstractModel):
    """DescribeDedicatedClusterTypes response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterTypeSet: List of CDC configurations
        :type DedicatedClusterTypeSet: list of DedicatedClusterType
        :param _TotalCount: Number of records that meet the conditions
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterTypeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterTypeSet(self):
        """List of CDC configurations
        :rtype: list of DedicatedClusterType
        """
        return self._DedicatedClusterTypeSet

    @DedicatedClusterTypeSet.setter
    def DedicatedClusterTypeSet(self, DedicatedClusterTypeSet):
        self._DedicatedClusterTypeSet = DedicatedClusterTypeSet

    @property
    def TotalCount(self):
        """Number of records that meet the conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DedicatedClusterTypeSet") is not None:
            self._DedicatedClusterTypeSet = []
            for item in params.get("DedicatedClusterTypeSet"):
                obj = DedicatedClusterType()
                obj._deserialize(item)
                self._DedicatedClusterTypeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedClustersRequest(AbstractModel):
    """DescribeDedicatedClusters request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterIds: Query by one or more instance IDs. Example of instance ID: cluster-xxxxxxxx
        :type DedicatedClusterIds: list of str
        :param _Zones: Filter by AZ name.
        :type Zones: list of str
        :param _SiteIds: Filter by site id.
        :type SiteIds: list of str
        :param _LifecycleStatuses: Filter by CDC life cycle.
        :type LifecycleStatuses: list of str
        :param _Name: Name of fuzzy matching CDC
        :type Name: str
        :param _Offset: Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._DedicatedClusterIds = None
        self._Zones = None
        self._SiteIds = None
        self._LifecycleStatuses = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def DedicatedClusterIds(self):
        """Query by one or more instance IDs. Example of instance ID: cluster-xxxxxxxx
        :rtype: list of str
        """
        return self._DedicatedClusterIds

    @DedicatedClusterIds.setter
    def DedicatedClusterIds(self, DedicatedClusterIds):
        self._DedicatedClusterIds = DedicatedClusterIds

    @property
    def Zones(self):
        """Filter by AZ name.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SiteIds(self):
        """Filter by site id.
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def LifecycleStatuses(self):
        """Filter by CDC life cycle.
        :rtype: list of str
        """
        return self._LifecycleStatuses

    @LifecycleStatuses.setter
    def LifecycleStatuses(self, LifecycleStatuses):
        self._LifecycleStatuses = LifecycleStatuses

    @property
    def Name(self):
        """Name of fuzzy matching CDC
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DedicatedClusterIds = params.get("DedicatedClusterIds")
        self._Zones = params.get("Zones")
        self._SiteIds = params.get("SiteIds")
        self._LifecycleStatuses = params.get("LifecycleStatuses")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedClustersResponse(AbstractModel):
    """DescribeDedicatedClusters response structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterSet: List of CDCs that meet the conditions
        :type DedicatedClusterSet: list of DedicatedCluster
        :param _TotalCount: Total number of CDCs that meet the conditions
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DedicatedClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DedicatedClusterSet(self):
        """List of CDCs that meet the conditions
        :rtype: list of DedicatedCluster
        """
        return self._DedicatedClusterSet

    @DedicatedClusterSet.setter
    def DedicatedClusterSet(self, DedicatedClusterSet):
        self._DedicatedClusterSet = DedicatedClusterSet

    @property
    def TotalCount(self):
        """Total number of CDCs that meet the conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DedicatedClusterSet") is not None:
            self._DedicatedClusterSet = []
            for item in params.get("DedicatedClusterSet"):
                obj = DedicatedCluster()
                obj._deserialize(item)
                self._DedicatedClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDedicatedSupportedZonesRequest(AbstractModel):
    """DescribeDedicatedSupportedZones request structure.

    """

    def __init__(self):
        r"""
        :param _Regions: List of input regions
        :type Regions: list of int
        """
        self._Regions = None

    @property
    def Regions(self):
        """List of input regions
        :rtype: list of int
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDedicatedSupportedZonesResponse(AbstractModel):
    """DescribeDedicatedSupportedZones response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneSet: List of supported AZs
        :type ZoneSet: list of RegionZoneInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneSet = None
        self._RequestId = None

    @property
    def ZoneSet(self):
        """List of supported AZs
        :rtype: list of RegionZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = RegionZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSitesDetailRequest(AbstractModel):
    """DescribeSitesDetail request structure.

    """

    def __init__(self):
        r"""
        :param _SiteIds: Filter by site id.
        :type SiteIds: list of str
        :param _Offset: Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Name: Fuzzy match by site name.
        :type Name: str
        """
        self._SiteIds = None
        self._Offset = None
        self._Limit = None
        self._Name = None

    @property
    def SiteIds(self):
        """Filter by site id.
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def Offset(self):
        """Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        """Fuzzy match by site name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesDetailResponse(AbstractModel):
    """DescribeSitesDetail response structure.

    """

    def __init__(self):
        r"""
        :param _SiteDetailSet: Site details
        :type SiteDetailSet: list of SiteDetail
        :param _TotalCount: Total number of sites that meet the conditions
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SiteDetailSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SiteDetailSet(self):
        """Site details
        :rtype: list of SiteDetail
        """
        return self._SiteDetailSet

    @SiteDetailSet.setter
    def SiteDetailSet(self, SiteDetailSet):
        self._SiteDetailSet = SiteDetailSet

    @property
    def TotalCount(self):
        """Total number of sites that meet the conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SiteDetailSet") is not None:
            self._SiteDetailSet = []
            for item in params.get("SiteDetailSet"):
                obj = SiteDetail()
                obj._deserialize(item)
                self._SiteDetailSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites request structure.

    """

    def __init__(self):
        r"""
        :param _SiteIds: Filter by site id.
        :type SiteIds: list of str
        :param _Name: Name of fuzzy matching site
        :type Name: str
        :param _Offset: Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._SiteIds = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def SiteIds(self):
        """Filter by site id.
        :rtype: list of str
        """
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def Name(self):
        """Name of fuzzy matching site
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """Offset, 0 by default For further information on Offset, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned pieces, 20 by default and can be up to 100. For further information on Limit, please refer to relevant sections in API [Overview] (https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesResponse(AbstractModel):
    """DescribeSites response structure.

    """

    def __init__(self):
        r"""
        :param _SiteSet: List of sites that meet the query conditions
        :type SiteSet: list of Site
        :param _TotalCount: Number of sites that meet the conditions
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SiteSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SiteSet(self):
        """List of sites that meet the query conditions
        :rtype: list of Site
        """
        return self._SiteSet

    @SiteSet.setter
    def SiteSet(self, SiteSet):
        self._SiteSet = SiteSet

    @property
    def TotalCount(self):
        """Number of sites that meet the conditions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SiteSet") is not None:
            self._SiteSet = []
            for item in params.get("SiteSet"):
                obj = Site()
                obj._deserialize(item)
                self._SiteSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetailData(AbstractModel):
    """Time-stamped detailed data

    """

    def __init__(self):
        r"""
        :param _Timestamps: Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Timestamps: list of float
        :param _Values: Corresponding value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """Corresponding value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostDetailInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _HostTypeFamily: 
        :type HostTypeFamily: str
        :param _CpuTotal: 
        :type CpuTotal: float
        :param _CpuAvailable: 
        :type CpuAvailable: float
        :param _MemTotal: 
        :type MemTotal: float
        :param _MemAvailable: 
        :type MemAvailable: float
        """
        self._HostTypeFamily = None
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None

    @property
    def HostTypeFamily(self):
        """
        :rtype: str
        """
        return self._HostTypeFamily

    @HostTypeFamily.setter
    def HostTypeFamily(self, HostTypeFamily):
        self._HostTypeFamily = HostTypeFamily

    @property
    def CpuTotal(self):
        """
        :rtype: float
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        """
        :rtype: float
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        """
        :rtype: float
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        """
        :rtype: float
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable


    def _deserialize(self, params):
        self._HostTypeFamily = params.get("HostTypeFamily")
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostInfo(AbstractModel):
    """CDC host details

    """

    def __init__(self):
        r"""
        :param _HostIp: Host IP
        :type HostIp: str
        :param _ServiceType: Cloud service type
        :type ServiceType: str
        :param _HostStatus: Host running status
        :type HostStatus: str
        :param _HostType: Host type
        :type HostType: str
        :param _CpuAvailable: Number of available CPUs
        :type CpuAvailable: int
        :param _CpuTotal: Total CPUs
        :type CpuTotal: int
        :param _MemAvailable: Available memories
        :type MemAvailable: int
        :param _MemTotal: Total memories
        :type MemTotal: int
        :param _RunTime: Running time
        :type RunTime: str
        :param _ExpireTime: Expiration time
        :type ExpireTime: str
        :param _HostId: Host id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type HostId: str
        """
        self._HostIp = None
        self._ServiceType = None
        self._HostStatus = None
        self._HostType = None
        self._CpuAvailable = None
        self._CpuTotal = None
        self._MemAvailable = None
        self._MemTotal = None
        self._RunTime = None
        self._ExpireTime = None
        self._HostId = None

    @property
    def HostIp(self):
        """Host IP
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def ServiceType(self):
        """Cloud service type
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def HostStatus(self):
        """Host running status
        :rtype: str
        """
        return self._HostStatus

    @HostStatus.setter
    def HostStatus(self, HostStatus):
        self._HostStatus = HostStatus

    @property
    def HostType(self):
        """Host type
        :rtype: str
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def CpuAvailable(self):
        """Number of available CPUs
        :rtype: int
        """
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def CpuTotal(self):
        """Total CPUs
        :rtype: int
        """
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def MemAvailable(self):
        """Available memories
        :rtype: int
        """
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def MemTotal(self):
        """Total memories
        :rtype: int
        """
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def RunTime(self):
        """Running time
        :rtype: str
        """
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

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
    def HostId(self):
        """Host id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._HostIp = params.get("HostIp")
        self._ServiceType = params.get("ServiceType")
        self._HostStatus = params.get("HostStatus")
        self._HostType = params.get("HostType")
        self._CpuAvailable = params.get("CpuAvailable")
        self._CpuTotal = params.get("CpuTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._MemTotal = params.get("MemTotal")
        self._RunTime = params.get("RunTime")
        self._ExpireTime = params.get("ExpireTime")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostStatistic(AbstractModel):
    """Statistic information of hosts in the CDC

    """

    def __init__(self):
        r"""
        :param _HostType: Host type
        :type HostType: str
        :param _HostFamily: Host model family
        :type HostFamily: str
        :param _Cpu: Number of CPU cores of host, in cores
        :type Cpu: int
        :param _Memory: Host memory, in GB
        :type Memory: int
        :param _Count: Number of hosts of this type
        :type Count: int
        :param _CpuAverage: Average CPU load percentage 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type CpuAverage: float
        :param _MemAverage: Average memory usage percentage 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type MemAverage: float
        :param _NetAverage: Average network traffic 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type NetAverage: float
        :param _CpuDetailData: Detailed CPU monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type CpuDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _MemDetailData: Memory details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type MemDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _NetRateDetailData: Network rate details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type NetRateDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        :param _NetPacketDetailData: Network packet details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type NetPacketDetailData: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        self._HostType = None
        self._HostFamily = None
        self._Cpu = None
        self._Memory = None
        self._Count = None
        self._CpuAverage = None
        self._MemAverage = None
        self._NetAverage = None
        self._CpuDetailData = None
        self._MemDetailData = None
        self._NetRateDetailData = None
        self._NetPacketDetailData = None

    @property
    def HostType(self):
        """Host type
        :rtype: str
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostFamily(self):
        """Host model family
        :rtype: str
        """
        return self._HostFamily

    @HostFamily.setter
    def HostFamily(self, HostFamily):
        self._HostFamily = HostFamily

    @property
    def Cpu(self):
        """Number of CPU cores of host, in cores
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Host memory, in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Count(self):
        """Number of hosts of this type
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CpuAverage(self):
        """Average CPU load percentage 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._CpuAverage

    @CpuAverage.setter
    def CpuAverage(self, CpuAverage):
        self._CpuAverage = CpuAverage

    @property
    def MemAverage(self):
        """Average memory usage percentage 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._MemAverage

    @MemAverage.setter
    def MemAverage(self, MemAverage):
        self._MemAverage = MemAverage

    @property
    def NetAverage(self):
        """Average network traffic 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._NetAverage

    @NetAverage.setter
    def NetAverage(self, NetAverage):
        self._NetAverage = NetAverage

    @property
    def CpuDetailData(self):
        """Detailed CPU monitoring data 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._CpuDetailData

    @CpuDetailData.setter
    def CpuDetailData(self, CpuDetailData):
        self._CpuDetailData = CpuDetailData

    @property
    def MemDetailData(self):
        """Memory details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._MemDetailData

    @MemDetailData.setter
    def MemDetailData(self, MemDetailData):
        self._MemDetailData = MemDetailData

    @property
    def NetRateDetailData(self):
        """Network rate details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._NetRateDetailData

    @NetRateDetailData.setter
    def NetRateDetailData(self, NetRateDetailData):
        self._NetRateDetailData = NetRateDetailData

    @property
    def NetPacketDetailData(self):
        """Network packet details 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DetailData`
        """
        return self._NetPacketDetailData

    @NetPacketDetailData.setter
    def NetPacketDetailData(self, NetPacketDetailData):
        self._NetPacketDetailData = NetPacketDetailData


    def _deserialize(self, params):
        self._HostType = params.get("HostType")
        self._HostFamily = params.get("HostFamily")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Count = params.get("Count")
        self._CpuAverage = params.get("CpuAverage")
        self._MemAverage = params.get("MemAverage")
        self._NetAverage = params.get("NetAverage")
        if params.get("CpuDetailData") is not None:
            self._CpuDetailData = DetailData()
            self._CpuDetailData._deserialize(params.get("CpuDetailData"))
        if params.get("MemDetailData") is not None:
            self._MemDetailData = DetailData()
            self._MemDetailData._deserialize(params.get("MemDetailData"))
        if params.get("NetRateDetailData") is not None:
            self._NetRateDetailData = DetailData()
            self._NetRateDetailData._deserialize(params.get("NetRateDetailData"))
        if params.get("NetPacketDetailData") is not None:
            self._NetPacketDetailData = DetailData()
            self._NetPacketDetailData._deserialize(params.get("NetPacketDetailData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InBandwidth(AbstractModel):
    """Inbound bandwidth data

    """

    def __init__(self):
        r"""
        :param _Timestamps: Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Timestamps: list of float
        :param _Values: Time-specific value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """Time-specific value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalNetInfo(AbstractModel):
    """Local network information

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Protocol: str
        :param _VpcId: Network id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type VpcId: str
        :param _BGPRoute: Routing information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type BGPRoute: str
        :param _LocalIp: Local IP 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type LocalIp: str
        """
        self._Protocol = None
        self._VpcId = None
        self._BGPRoute = None
        self._LocalIp = None

    @property
    def Protocol(self):
        """Protocol 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VpcId(self):
        """Network id 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def BGPRoute(self):
        """Routing information 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._BGPRoute

    @BGPRoute.setter
    def BGPRoute(self, BGPRoute):
        self._BGPRoute = BGPRoute

    @property
    def LocalIp(self):
        """Local IP 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._LocalIp

    @LocalIp.setter
    def LocalIp(self, LocalIp):
        self._LocalIp = LocalIp


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VpcId = params.get("VpcId")
        self._BGPRoute = params.get("BGPRoute")
        self._LocalIp = params.get("LocalIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoRequest(AbstractModel):
    """ModifyDedicatedClusterInfo request structure.

    """

    def __init__(self):
        r"""
        :param _DedicatedClusterId: CDC ID
        :type DedicatedClusterId: str
        :param _Name: New cluster name
        :type Name: str
        :param _Zone: New cluster AZ
        :type Zone: str
        :param _Description: New cluster description
        :type Description: str
        :param _SiteId: Site where the cluster resides
        :type SiteId: str
        """
        self._DedicatedClusterId = None
        self._Name = None
        self._Zone = None
        self._Description = None
        self._SiteId = None

    @property
    def DedicatedClusterId(self):
        """CDC ID
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def Name(self):
        """New cluster name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        """New cluster AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Description(self):
        """New cluster description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SiteId(self):
        """Site where the cluster resides
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId


    def _deserialize(self, params):
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._Description = params.get("Description")
        self._SiteId = params.get("SiteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDedicatedClusterInfoResponse(AbstractModel):
    """ModifyDedicatedClusterInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyOrderStatusRequest(AbstractModel):
    """ModifyOrderStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status to be updated
        :type Status: str
        :param _DedicatedClusterOrderId: Large order ID
        :type DedicatedClusterOrderId: str
        :param _SubOrderIds: Small order ID
        :type SubOrderIds: list of str
        """
        self._Status = None
        self._DedicatedClusterOrderId = None
        self._SubOrderIds = None

    @property
    def Status(self):
        """Status to be updated
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DedicatedClusterOrderId(self):
        """Large order ID
        :rtype: str
        """
        return self._DedicatedClusterOrderId

    @DedicatedClusterOrderId.setter
    def DedicatedClusterOrderId(self, DedicatedClusterOrderId):
        self._DedicatedClusterOrderId = DedicatedClusterOrderId

    @property
    def SubOrderIds(self):
        """Small order ID
        :rtype: list of str
        """
        return self._SubOrderIds

    @SubOrderIds.setter
    def SubOrderIds(self, SubOrderIds):
        self._SubOrderIds = SubOrderIds


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DedicatedClusterOrderId = params.get("DedicatedClusterOrderId")
        self._SubOrderIds = params.get("SubOrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrderStatusResponse(AbstractModel):
    """ModifyOrderStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySiteDeviceInfoRequest(AbstractModel):
    """ModifySiteDeviceInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SiteId: Equipment room ID
        :type SiteId: str
        :param _FiberType: You are using optical fiber type to connect the CDC device to the network Single-mode or multi-mode fibers are available.
        :type FiberType: str
        :param _OpticalStandard: Optical standard used to connect the CDC device to the network This field depends on the uplink speed, optical fiber type, and distance to upstream equipment.
        :type OpticalStandard: str
        :param _PowerConnectors: Type of power connector
        :type PowerConnectors: str
        :param _PowerFeedDrop: Whether power is supplied from above or below the rack
        :type PowerFeedDrop: str
        :param _MaxWeight: Maximum weight capacity (KG)
        :type MaxWeight: int
        :param _PowerDrawKva: Power consumption (KW)
        :type PowerDrawKva: int
        :param _UplinkSpeedGbps: Uplink speed from the network to Tencent Cloud Region
        :type UplinkSpeedGbps: int
        :param _UplinkCount: Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :type UplinkCount: int
        :param _ConditionRequirement: Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :type ConditionRequirement: bool
        :param _DimensionRequirement: Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :type DimensionRequirement: bool
        :param _RedundantNetworking: Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :type RedundantNetworking: bool
        :param _NeedHelp: Whether you need help from Tencent Cloud for rack installation?
        :type NeedHelp: bool
        :param _RedundantPower: Whether there is power redundancy?
        :type RedundantPower: bool
        :param _BreakerRequirement: Whether there is an upstream circuit breaker?
        :type BreakerRequirement: bool
        """
        self._SiteId = None
        self._FiberType = None
        self._OpticalStandard = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._MaxWeight = None
        self._PowerDrawKva = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._RedundantNetworking = None
        self._NeedHelp = None
        self._RedundantPower = None
        self._BreakerRequirement = None

    @property
    def SiteId(self):
        """Equipment room ID
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def FiberType(self):
        """You are using optical fiber type to connect the CDC device to the network Single-mode or multi-mode fibers are available.
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def OpticalStandard(self):
        """Optical standard used to connect the CDC device to the network This field depends on the uplink speed, optical fiber type, and distance to upstream equipment.
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def PowerConnectors(self):
        """Type of power connector
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """Whether power is supplied from above or below the rack
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def MaxWeight(self):
        """Maximum weight capacity (KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def PowerDrawKva(self):
        """Power consumption (KW)
        :rtype: int
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def UplinkSpeedGbps(self):
        """Uplink speed from the network to Tencent Cloud Region
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def ConditionRequirement(self):
        """Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def RedundantNetworking(self):
        """Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def NeedHelp(self):
        """Whether you need help from Tencent Cloud for rack installation?
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def RedundantPower(self):
        """Whether there is power redundancy?
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def BreakerRequirement(self):
        """Whether there is an upstream circuit breaker?
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._FiberType = params.get("FiberType")
        self._OpticalStandard = params.get("OpticalStandard")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._MaxWeight = params.get("MaxWeight")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._NeedHelp = params.get("NeedHelp")
        self._RedundantPower = params.get("RedundantPower")
        self._BreakerRequirement = params.get("BreakerRequirement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteDeviceInfoResponse(AbstractModel):
    """ModifySiteDeviceInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySiteInfoRequest(AbstractModel):
    """ModifySiteInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SiteId: Equipment room ID
        :type SiteId: str
        :param _Name: Site name
        :type Name: str
        :param _Description: Site description
        :type Description: str
        :param _Note: Note
        :type Note: str
        :param _Country: Country where the site is located
        :type Country: str
        :param _Province: Province where the site is located
        :type Province: str
        :param _City: City where the site is located
        :type City: str
        :param _PostalCode: Postal code of the site area
        :type PostalCode: str
        :param _AddressLine: Detailed address of the site
        :type AddressLine: str
        """
        self._SiteId = None
        self._Name = None
        self._Description = None
        self._Note = None
        self._Country = None
        self._Province = None
        self._City = None
        self._PostalCode = None
        self._AddressLine = None

    @property
    def SiteId(self):
        """Equipment room ID
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

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
    def Description(self):
        """Site description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Note(self):
        """Note
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Country(self):
        """Country where the site is located
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province where the site is located
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City where the site is located
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def PostalCode(self):
        """Postal code of the site area
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def AddressLine(self):
        """Detailed address of the site
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Note = params.get("Note")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PostalCode = params.get("PostalCode")
        self._AddressLine = params.get("AddressLine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteInfoResponse(AbstractModel):
    """ModifySiteInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OutBandwidth(AbstractModel):
    """Outbound bandwidth data

    """

    def __init__(self):
        r"""
        :param _Timestamps: Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Timestamps: list of float
        :param _Values: Time-specific value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """Timestamp 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """Time-specific value 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionZoneInfo(AbstractModel):
    """Information of RegionZoneInfo

    """

    def __init__(self):
        r"""
        :param _RegionId: Region id
        :type RegionId: int
        :param _Zones: ZoneInfo array
        :type Zones: list of ZoneInfo
        """
        self._RegionId = None
        self._Zones = None

    @property
    def RegionId(self):
        """Region id
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zones(self):
        """ZoneInfo array
        :rtype: list of ZoneInfo
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._Zones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Site(AbstractModel):
    """Customer site information

    """

    def __init__(self):
        r"""
        :param _Name: Site name
        :type Name: str
        :param _SiteId: Site id
        :type SiteId: str
        :param _Description: Site description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type Description: str
        :param _CreateTime: Site creation time
        :type CreateTime: str
        """
        self._Name = None
        self._SiteId = None
        self._Description = None
        self._CreateTime = None

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
    def SiteId(self):
        """Site id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Description(self):
        """Site description 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """Site creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SiteId = params.get("SiteId")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SiteDetail(AbstractModel):
    """Site details

    """

    def __init__(self):
        r"""
        :param _SiteId: Site id
        :type SiteId: str
        :param _Name: Site name
        :type Name: str
        :param _Description: Site description
        :type Description: str
        :param _CreateTime: Site creation time
        :type CreateTime: str
        :param _FiberType: Optical fiber type
        :type FiberType: str
        :param _UplinkSpeedGbps: Uplink speed from the network to Tencent Cloud Region
        :type UplinkSpeedGbps: int
        :param _UplinkCount: Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :type UplinkCount: int
        :param _OpticalStandard: Optical standard used to connect the CDC device to the network
        :type OpticalStandard: str
        :param _RedundantNetworking: Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :type RedundantNetworking: bool
        :param _PowerConnectors: Type of power connector
        :type PowerConnectors: str
        :param _PowerFeedDrop: Whether power is supplied from above or below the rack
        :type PowerFeedDrop: str
        :param _PowerDrawKva: Power consumption (KW)
        :type PowerDrawKva: float
        :param _ConditionRequirement: Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :type ConditionRequirement: bool
        :param _DimensionRequirement: Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :type DimensionRequirement: bool
        :param _MaxWeight: Maximum weight capacity (KG)
        :type MaxWeight: int
        :param _AddressLine: Site address
        :type AddressLine: str
        :param _OptionalAddressLine: Detailed address of the site area (to be added)
        :type OptionalAddressLine: str
        :param _NeedHelp: Whether you need help from Tencent Cloud for rack installation?
        :type NeedHelp: bool
        :param _BreakerRequirement: Whether there is an upstream circuit breaker?
        :type BreakerRequirement: bool
        :param _RedundantPower: Whether there is power redundancy?
        :type RedundantPower: bool
        :param _Country: Country where the site is located
        :type Country: str
        :param _Province: Province where the site is located
        :type Province: str
        :param _City: City where the site is located
        :type City: str
        :param _PostalCode: Postal code of the site area
        :type PostalCode: int
        """
        self._SiteId = None
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._FiberType = None
        self._UplinkSpeedGbps = None
        self._UplinkCount = None
        self._OpticalStandard = None
        self._RedundantNetworking = None
        self._PowerConnectors = None
        self._PowerFeedDrop = None
        self._PowerDrawKva = None
        self._ConditionRequirement = None
        self._DimensionRequirement = None
        self._MaxWeight = None
        self._AddressLine = None
        self._OptionalAddressLine = None
        self._NeedHelp = None
        self._BreakerRequirement = None
        self._RedundantPower = None
        self._Country = None
        self._Province = None
        self._City = None
        self._PostalCode = None

    @property
    def SiteId(self):
        """Site id
        :rtype: str
        """
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

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
    def Description(self):
        """Site description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """Site creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FiberType(self):
        """Optical fiber type
        :rtype: str
        """
        return self._FiberType

    @FiberType.setter
    def FiberType(self, FiberType):
        self._FiberType = FiberType

    @property
    def UplinkSpeedGbps(self):
        """Uplink speed from the network to Tencent Cloud Region
        :rtype: int
        """
        return self._UplinkSpeedGbps

    @UplinkSpeedGbps.setter
    def UplinkSpeedGbps(self, UplinkSpeedGbps):
        self._UplinkSpeedGbps = UplinkSpeedGbps

    @property
    def UplinkCount(self):
        """Number of uplinks used by each CDC device (2 devices per rack) when connected to the network
        :rtype: int
        """
        return self._UplinkCount

    @UplinkCount.setter
    def UplinkCount(self, UplinkCount):
        self._UplinkCount = UplinkCount

    @property
    def OpticalStandard(self):
        """Optical standard used to connect the CDC device to the network
        :rtype: str
        """
        return self._OpticalStandard

    @OpticalStandard.setter
    def OpticalStandard(self, OpticalStandard):
        self._OpticalStandard = OpticalStandard

    @property
    def RedundantNetworking(self):
        """Whether redundant upstream equipment (switch or router) is provided so that both network devices can be connected to the network.
        :rtype: bool
        """
        return self._RedundantNetworking

    @RedundantNetworking.setter
    def RedundantNetworking(self, RedundantNetworking):
        self._RedundantNetworking = RedundantNetworking

    @property
    def PowerConnectors(self):
        """Type of power connector
        :rtype: str
        """
        return self._PowerConnectors

    @PowerConnectors.setter
    def PowerConnectors(self, PowerConnectors):
        self._PowerConnectors = PowerConnectors

    @property
    def PowerFeedDrop(self):
        """Whether power is supplied from above or below the rack
        :rtype: str
        """
        return self._PowerFeedDrop

    @PowerFeedDrop.setter
    def PowerFeedDrop(self, PowerFeedDrop):
        self._PowerFeedDrop = PowerFeedDrop

    @property
    def PowerDrawKva(self):
        """Power consumption (KW)
        :rtype: float
        """
        return self._PowerDrawKva

    @PowerDrawKva.setter
    def PowerDrawKva(self, PowerDrawKva):
        self._PowerDrawKva = PowerDrawKva

    @property
    def ConditionRequirement(self):
        """Whether the following environmental conditions are met: 
1. There are no material requirements or the acceptance standard on site that will affect the delivery and installation of the CDC device. 
2. The following conditions are met for finalized rack positions: 
Temperature ranges from 41 to 104°F (5 to 40°C). 
Humidity ranges from 10°F (-12°C) to 70°F (21°C) and relative humidity ranges from 8% RH to 80% RH. 
Air flows from front to back at the rack position and there is sufficient air in CFM (cubic feet per minute). The air quantity in CFM must be 145.8 times the power consumption (in KVA) of CDC.
        :rtype: bool
        """
        return self._ConditionRequirement

    @ConditionRequirement.setter
    def ConditionRequirement(self, ConditionRequirement):
        self._ConditionRequirement = ConditionRequirement

    @property
    def DimensionRequirement(self):
        """Whether the following dimension conditions are met: 
Your loading dock can accommodate one rack container (H x W x D = 94" x 54" x 48"). 
You can provide a clear route from the delivery point of your rack (H x W x D = 80" x 24" x 48") to its final installation location. You should consider platforms, corridors, doors, turns, ramps, freight elevators as well as other access restrictions when measuring the depth. 
There shall be a 48" or greater front clearance and a 24" or greater rear clearance where the CDC is finally installed.
        :rtype: bool
        """
        return self._DimensionRequirement

    @DimensionRequirement.setter
    def DimensionRequirement(self, DimensionRequirement):
        self._DimensionRequirement = DimensionRequirement

    @property
    def MaxWeight(self):
        """Maximum weight capacity (KG)
        :rtype: int
        """
        return self._MaxWeight

    @MaxWeight.setter
    def MaxWeight(self, MaxWeight):
        self._MaxWeight = MaxWeight

    @property
    def AddressLine(self):
        """Site address
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def OptionalAddressLine(self):
        """Detailed address of the site area (to be added)
        :rtype: str
        """
        return self._OptionalAddressLine

    @OptionalAddressLine.setter
    def OptionalAddressLine(self, OptionalAddressLine):
        self._OptionalAddressLine = OptionalAddressLine

    @property
    def NeedHelp(self):
        """Whether you need help from Tencent Cloud for rack installation?
        :rtype: bool
        """
        return self._NeedHelp

    @NeedHelp.setter
    def NeedHelp(self, NeedHelp):
        self._NeedHelp = NeedHelp

    @property
    def BreakerRequirement(self):
        """Whether there is an upstream circuit breaker?
        :rtype: bool
        """
        return self._BreakerRequirement

    @BreakerRequirement.setter
    def BreakerRequirement(self, BreakerRequirement):
        self._BreakerRequirement = BreakerRequirement

    @property
    def RedundantPower(self):
        """Whether there is power redundancy?
        :rtype: bool
        """
        return self._RedundantPower

    @RedundantPower.setter
    def RedundantPower(self, RedundantPower):
        self._RedundantPower = RedundantPower

    @property
    def Country(self):
        """Country where the site is located
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province where the site is located
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City where the site is located
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def PostalCode(self):
        """Postal code of the site area
        :rtype: int
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._FiberType = params.get("FiberType")
        self._UplinkSpeedGbps = params.get("UplinkSpeedGbps")
        self._UplinkCount = params.get("UplinkCount")
        self._OpticalStandard = params.get("OpticalStandard")
        self._RedundantNetworking = params.get("RedundantNetworking")
        self._PowerConnectors = params.get("PowerConnectors")
        self._PowerFeedDrop = params.get("PowerFeedDrop")
        self._PowerDrawKva = params.get("PowerDrawKva")
        self._ConditionRequirement = params.get("ConditionRequirement")
        self._DimensionRequirement = params.get("DimensionRequirement")
        self._MaxWeight = params.get("MaxWeight")
        self._AddressLine = params.get("AddressLine")
        self._OptionalAddressLine = params.get("OptionalAddressLine")
        self._NeedHelp = params.get("NeedHelp")
        self._BreakerRequirement = params.get("BreakerRequirement")
        self._RedundantPower = params.get("RedundantPower")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PostalCode = params.get("PostalCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpngwBandwidthData(AbstractModel):
    """VPN gateway traffic monitoring data

    """

    def __init__(self):
        r"""
        :param _OutBandwidth: Outbound bandwidth traffic 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :type OutBandwidth: :class:`tencentcloud.cdc.v20201214.models.OutBandwidth`
        :param _InBandwidth: Inbound bandwidth traffic
        :type InBandwidth: :class:`tencentcloud.cdc.v20201214.models.InBandwidth`
        """
        self._OutBandwidth = None
        self._InBandwidth = None

    @property
    def OutBandwidth(self):
        """Outbound bandwidth traffic 
Note: The returned value of this field may be null, indicating that no valid value is obtained.
        :rtype: :class:`tencentcloud.cdc.v20201214.models.OutBandwidth`
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InBandwidth(self):
        """Inbound bandwidth traffic
        :rtype: :class:`tencentcloud.cdc.v20201214.models.InBandwidth`
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth


    def _deserialize(self, params):
        if params.get("OutBandwidth") is not None:
            self._OutBandwidth = OutBandwidth()
            self._OutBandwidth._deserialize(params.get("OutBandwidth"))
        if params.get("InBandwidth") is not None:
            self._InBandwidth = InBandwidth()
            self._InBandwidth._deserialize(params.get("InBandwidth"))
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
        :param _Zone: AZ name
        :type Zone: str
        :param _ZoneName: AZ description
        :type ZoneName: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneState: AZ status: AVAILABLE or UNAVAILABLE AVAILABLE means the AZ is available while UNAVAILABLE means the AZ is unavailable.
        :type ZoneState: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None

    @property
    def Zone(self):
        """AZ name
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        """AZ description
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        """AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        """AZ status: AVAILABLE or UNAVAILABLE AVAILABLE means the AZ is available while UNAVAILABLE means the AZ is unavailable.
        :rtype: str
        """
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        