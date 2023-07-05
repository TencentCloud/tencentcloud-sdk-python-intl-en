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


class AcceptDirectConnectTunnelRequest(AbstractModel):
    """AcceptDirectConnectTunnel request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: The connection owner accepts an application for sharing the dedicated tunnel
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel response structure.

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


class AccessPoint(AbstractModel):
    """Access point information.

    """

    def __init__(self):
        r"""
        :param _AccessPointName: Access point name.
        :type AccessPointName: str
        :param _AccessPointId: Unique access point ID.
        :type AccessPointId: str
        :param _State: Access point status. Valid values: available, unavailable.
        :type State: str
        :param _Location: Access point location.
        :type Location: str
        :param _LineOperator: List of ISPs supported by access point.
        :type LineOperator: list of str
        :param _RegionId: ID of the region that manages the access point.
        :type RegionId: str
        :param _AvailablePortType: Available port type at the access point. Valid values: 1000BASE-T: gigabit electrical port; 1000BASE-LX: 10 km gigabit single-mode optical port; 1000BASE-ZX: 80 km gigabit single-mode optical port; 10GBASE-LR: 10 km 10-gigabit single-mode optical port; 10GBASE-ZR: 80 km 10-gigabit single-mode optical port; 10GBASE-LH: 40 km 10-gigabit single-mode optical port; 100GBASE-LR4: 10 km 100-gigabit single-mode optical portfiber optic port.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AvailablePortType: list of str
        :param _Coordinate: Latitude and longitude of the access point
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Coordinate: :class:`tencentcloud.dc.v20180410.models.Coordinate`
        :param _City: City where the access point is located
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type City: str
        :param _Area: Access point region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Area: str
        :param _AccessPointType: Access point type. Valid values: `VXLAN`, `QCPL`, and `QCAR`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AccessPointType: str
        """
        self._AccessPointName = None
        self._AccessPointId = None
        self._State = None
        self._Location = None
        self._LineOperator = None
        self._RegionId = None
        self._AvailablePortType = None
        self._Coordinate = None
        self._City = None
        self._Area = None
        self._AccessPointType = None

    @property
    def AccessPointName(self):
        return self._AccessPointName

    @AccessPointName.setter
    def AccessPointName(self, AccessPointName):
        self._AccessPointName = AccessPointName

    @property
    def AccessPointId(self):
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def LineOperator(self):
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def AvailablePortType(self):
        return self._AvailablePortType

    @AvailablePortType.setter
    def AvailablePortType(self, AvailablePortType):
        self._AvailablePortType = AvailablePortType

    @property
    def Coordinate(self):
        return self._Coordinate

    @Coordinate.setter
    def Coordinate(self, Coordinate):
        self._Coordinate = Coordinate

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AccessPointType(self):
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType


    def _deserialize(self, params):
        self._AccessPointName = params.get("AccessPointName")
        self._AccessPointId = params.get("AccessPointId")
        self._State = params.get("State")
        self._Location = params.get("Location")
        self._LineOperator = params.get("LineOperator")
        self._RegionId = params.get("RegionId")
        self._AvailablePortType = params.get("AvailablePortType")
        if params.get("Coordinate") is not None:
            self._Coordinate = Coordinate()
            self._Coordinate._deserialize(params.get("Coordinate"))
        self._City = params.get("City")
        self._Area = params.get("Area")
        self._AccessPointType = params.get("AccessPointType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressRequest(AbstractModel):
    """ApplyInternetAddress request structure.

    """

    def __init__(self):
        r"""
        :param _MaskLen: Mask length of a CIDR block
        :type MaskLen: int
        :param _AddrType: Address type. Valid values: 0: BGP
1: China Telecom
2: China Mobile
3: China Unicom
        :type AddrType: int
        :param _AddrProto: Address protocol. Valid values: 0: IPv4
1: IPv6
        :type AddrProto: int
        """
        self._MaskLen = None
        self._AddrType = None
        self._AddrProto = None

    @property
    def MaskLen(self):
        return self._MaskLen

    @MaskLen.setter
    def MaskLen(self, MaskLen):
        self._MaskLen = MaskLen

    @property
    def AddrType(self):
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def AddrProto(self):
        return self._AddrProto

    @AddrProto.setter
    def AddrProto(self, AddrProto):
        self._AddrProto = AddrProto


    def _deserialize(self, params):
        self._MaskLen = params.get("MaskLen")
        self._AddrType = params.get("AddrType")
        self._AddrProto = params.get("AddrProto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressResponse(AbstractModel):
    """ApplyInternetAddress response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the internet tunnel’s public IP address
Note: this field may return `null`, indicating that no valid values can be obtained.
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


class BFDInfo(AbstractModel):
    """BFD configuration information

    """

    def __init__(self):
        r"""
        :param _ProbeFailedTimes: Number of health checks
        :type ProbeFailedTimes: int
        :param _Interval: Health check interval
        :type Interval: int
        """
        self._ProbeFailedTimes = None
        self._Interval = None

    @property
    def ProbeFailedTimes(self):
        return self._ProbeFailedTimes

    @ProbeFailedTimes.setter
    def ProbeFailedTimes(self, ProbeFailedTimes):
        self._ProbeFailedTimes = ProbeFailedTimes

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._ProbeFailedTimes = params.get("ProbeFailedTimes")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BgpPeer(AbstractModel):
    """BGP parameter, including Asn and AuthKey.

    """

    def __init__(self):
        r"""
        :param _Asn: User-side BGP Asn.
        :type Asn: int
        :param _AuthKey: User-side BGP key.
        :type AuthKey: str
        """
        self._Asn = None
        self._AuthKey = None

    @property
    def Asn(self):
        return self._Asn

    @Asn.setter
    def Asn(self, Asn):
        self._Asn = Asn

    @property
    def AuthKey(self):
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey


    def _deserialize(self, params):
        self._Asn = params.get("Asn")
        self._AuthKey = params.get("AuthKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """Coordinate describing the longitude and latitude.

    """

    def __init__(self):
        r"""
        :param _Lat: Latitude
        :type Lat: float
        :param _Lng: Longitude
        :type Lng: float
        """
        self._Lat = None
        self._Lng = None

    @property
    def Lat(self):
        return self._Lat

    @Lat.setter
    def Lat(self, Lat):
        self._Lat = Lat

    @property
    def Lng(self):
        return self._Lng

    @Lng.setter
    def Lng(self, Lng):
        self._Lng = Lng


    def _deserialize(self, params):
        self._Lat = params.get("Lat")
        self._Lng = params.get("Lng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param _AccessPointId: Access point of connection.
You can call `DescribeAccessPoints` to get the region ID. The selected access point must exist and be available.
        :type AccessPointId: str
        :param _LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).
        :type LineOperator: str
        :param _PortType: Port type of connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface), 1000Base-LX (1-Gigabit single-module optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-module optical Ethernet interface; 10 KM). Default value: 1000Base-LX.
        :type PortType: str
        :param _CircuitCode: Circuit code of a connection, which is provided by the ISP or connection provider.
        :type CircuitCode: str
        :param _Location: Local IDC location.
        :type Location: str
        :param _Bandwidth: Connection port bandwidth in Mbps. Value range: [2,10240]. Default value: 1000.
        :type Bandwidth: int
        :param _RedundantDirectConnectId: ID of redundant connection.
        :type RedundantDirectConnectId: str
        :param _Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.
        :type Vlan: int
        :param _TencentAddress: Tencent-side IP address for connection debugging, which is automatically assigned by default.
        :type TencentAddress: str
        :param _CustomerAddress: User-side IP address for connection debugging, which is automatically assigned by default.
        :type CustomerAddress: str
        :param _CustomerName: Name of connection applicant, which is obtained from the account system by default.
        :type CustomerName: str
        :param _CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.
        :type CustomerContactMail: str
        :param _CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.
        :type CustomerContactNumber: str
        :param _FaultReportContactPerson: Fault reporting contact person.
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: Fault reporting contact number.
        :type FaultReportContactNumber: str
        :param _SignLaw: Whether the connection applicant has signed the service agreement. Default value: true.
        :type SignLaw: bool
        """
        self._DirectConnectName = None
        self._AccessPointId = None
        self._LineOperator = None
        self._PortType = None
        self._CircuitCode = None
        self._Location = None
        self._Bandwidth = None
        self._RedundantDirectConnectId = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._SignLaw = None

    @property
    def DirectConnectName(self):
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def AccessPointId(self):
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def LineOperator(self):
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def PortType(self):
        return self._PortType

    @PortType.setter
    def PortType(self, PortType):
        self._PortType = PortType

    @property
    def CircuitCode(self):
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def RedundantDirectConnectId(self):
        return self._RedundantDirectConnectId

    @RedundantDirectConnectId.setter
    def RedundantDirectConnectId(self, RedundantDirectConnectId):
        self._RedundantDirectConnectId = RedundantDirectConnectId

    @property
    def Vlan(self):
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def FaultReportContactPerson(self):
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def SignLaw(self):
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw


    def _deserialize(self, params):
        self._DirectConnectName = params.get("DirectConnectName")
        self._AccessPointId = params.get("AccessPointId")
        self._LineOperator = params.get("LineOperator")
        self._PortType = params.get("PortType")
        self._CircuitCode = params.get("CircuitCode")
        self._Location = params.get("Location")
        self._Bandwidth = params.get("Bandwidth")
        self._RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        self._SignLaw = params.get("SignLaw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect response structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectIdSet: Connection ID.
        :type DirectConnectIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DirectConnectIdSet = None
        self._RequestId = None

    @property
    def DirectConnectIdSet(self):
        return self._DirectConnectIdSet

    @DirectConnectIdSet.setter
    def DirectConnectIdSet(self, DirectConnectIdSet):
        self._DirectConnectIdSet = DirectConnectIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DirectConnectIdSet = params.get("DirectConnectIdSet")
        self._RequestId = params.get("RequestId")


class CreateDirectConnectTunnelRequest(AbstractModel):
    """CreateDirectConnectTunnel request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: Direct Connect ID, such as `dc-kd7d06of`.
        :type DirectConnectId: str
        :param _DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param _DirectConnectOwnerAccount: Connection owner, who is the current customer by default.
The developer account ID should be entered for shared connections.
        :type DirectConnectOwnerAccount: str
        :param _NetworkType: Network type. Valid values: VPC, BMVPC, CCN. Default value: VPC.
VPC: Virtual Private Cloud.
BMVPC: BM VPC.
CCN: Cloud Connect Network.
        :type NetworkType: str
        :param _NetworkRegion: Network region.
        :type NetworkRegion: str
        :param _VpcId: Unified VPC ID or BMVPC ID.
        :type VpcId: str
        :param _DirectConnectGatewayId: Direct connect gateway ID, such as `dcg-d545ddf`.
        :type DirectConnectGatewayId: str
        :param _Bandwidth: Direct Connect bandwidth in Mbps.
Default value: connection bandwidth value.
        :type Bandwidth: int
        :param _RouteType: BGP: BGP routing.
STATIC: Static routing.
Default value: BGP routing.
        :type RouteType: str
        :param _BgpPeer: BgpPeer, which is BGP information on the user side and includes Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: Static routing, i.e., IP range of the user's IDC.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _Vlan: VLAN. Value range: 0-3,000.
0: sub-interface not enabled.
Default value: Non-zero.
        :type Vlan: int
        :param _TencentAddress: TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param _CustomerAddress: CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param _TencentBackupAddress: TencentBackupAddress, i.e., Tencent-side standby IP address
        :type TencentBackupAddress: str
        :param _CloudAttachId: Cloud Attached Connection Service ID
        :type CloudAttachId: str
        :param _BfdEnable: Whether to enable BFD
        :type BfdEnable: int
        :param _NqaEnable: Whether to enable NQA
        :type NqaEnable: int
        :param _BfdInfo: BFD configuration information
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param _NqaInfo: NQA configuration information
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        """
        self._DirectConnectId = None
        self._DirectConnectTunnelName = None
        self._DirectConnectOwnerAccount = None
        self._NetworkType = None
        self._NetworkRegion = None
        self._VpcId = None
        self._DirectConnectGatewayId = None
        self._Bandwidth = None
        self._RouteType = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._TencentBackupAddress = None
        self._CloudAttachId = None
        self._BfdEnable = None
        self._NqaEnable = None
        self._BfdInfo = None
        self._NqaInfo = None

    @property
    def DirectConnectId(self):
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectTunnelName(self):
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def DirectConnectOwnerAccount(self):
        return self._DirectConnectOwnerAccount

    @DirectConnectOwnerAccount.setter
    def DirectConnectOwnerAccount(self, DirectConnectOwnerAccount):
        self._DirectConnectOwnerAccount = DirectConnectOwnerAccount

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def NetworkRegion(self):
        return self._NetworkRegion

    @NetworkRegion.setter
    def NetworkRegion(self, NetworkRegion):
        self._NetworkRegion = NetworkRegion

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DirectConnectGatewayId(self):
        return self._DirectConnectGatewayId

    @DirectConnectGatewayId.setter
    def DirectConnectGatewayId(self, DirectConnectGatewayId):
        self._DirectConnectGatewayId = DirectConnectGatewayId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def RouteType(self):
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def BgpPeer(self):
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def Vlan(self):
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def TencentBackupAddress(self):
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def CloudAttachId(self):
        return self._CloudAttachId

    @CloudAttachId.setter
    def CloudAttachId(self, CloudAttachId):
        self._CloudAttachId = CloudAttachId

    @property
    def BfdEnable(self):
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def NqaEnable(self):
        return self._NqaEnable

    @NqaEnable.setter
    def NqaEnable(self, NqaEnable):
        self._NqaEnable = NqaEnable

    @property
    def BfdInfo(self):
        return self._BfdInfo

    @BfdInfo.setter
    def BfdInfo(self, BfdInfo):
        self._BfdInfo = BfdInfo

    @property
    def NqaInfo(self):
        return self._NqaInfo

    @NqaInfo.setter
    def NqaInfo(self, NqaInfo):
        self._NqaInfo = NqaInfo


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self._DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self._NetworkType = params.get("NetworkType")
        self._NetworkRegion = params.get("NetworkRegion")
        self._VpcId = params.get("VpcId")
        self._DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self._Bandwidth = params.get("Bandwidth")
        self._RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._CloudAttachId = params.get("CloudAttachId")
        self._BfdEnable = params.get("BfdEnable")
        self._NqaEnable = params.get("NqaEnable")
        if params.get("BfdInfo") is not None:
            self._BfdInfo = BFDInfo()
            self._BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self._NqaInfo = NQAInfo()
            self._NqaInfo._deserialize(params.get("NqaInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel response structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelIdSet: Dedicated tunnel ID.
        :type DirectConnectTunnelIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DirectConnectTunnelIdSet = None
        self._RequestId = None

    @property
    def DirectConnectTunnelIdSet(self):
        return self._DirectConnectTunnelIdSet

    @DirectConnectTunnelIdSet.setter
    def DirectConnectTunnelIdSet(self, DirectConnectTunnelIdSet):
        self._DirectConnectTunnelIdSet = DirectConnectTunnelIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DirectConnectTunnelIdSet = params.get("DirectConnectTunnelIdSet")
        self._RequestId = params.get("RequestId")


class DeleteDirectConnectRequest(AbstractModel):
    """DeleteDirectConnect request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: Connection ID.
        :type DirectConnectId: str
        """
        self._DirectConnectId = None

    @property
    def DirectConnectId(self):
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect response structure.

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


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel response structure.

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


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints request structure.

    """

    def __init__(self):
        r"""
        :param _RegionId: Access point region, which can be queried through `DescribeRegions`.

You can call `DescribeRegions` to get the region ID.
        :type RegionId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._RegionId = None
        self._Offset = None
        self._Limit = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

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
        self._RegionId = params.get("RegionId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints response structure.

    """

    def __init__(self):
        r"""
        :param _AccessPointSet: Access point information.
        :type AccessPointSet: list of AccessPoint
        :param _TotalCount: Number of eligible access points.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessPointSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccessPointSet(self):
        return self._AccessPointSet

    @AccessPointSet.setter
    def AccessPointSet(self, AccessPointSet):
        self._AccessPointSet = AccessPointSet

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
        if params.get("AccessPointSet") is not None:
            self._AccessPointSet = []
            for item in params.get("AccessPointSet"):
                obj = AccessPoint()
                obj._deserialize(item)
                self._AccessPointSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelsRequest(AbstractModel):
    """DescribeDirectConnectTunnels request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions:
This parameter does not support specifying `DirectConnectTunnelIds` and `Filters` at the same time.
<li> direct-connect-tunnel-name: Dedicated tunnel name.</li>
<li> direct-connect-tunnel-id: Dedicated tunnel instance ID, such as `dcx-abcdefgh`.</li>
<li>direct-connect-id: Connection instance ID, such as `dc-abcdefgh`.</li>
        :type Filters: list of Filter
        :param _DirectConnectTunnelIds: Array of dedicated tunnel IDs.
        :type DirectConnectTunnelIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._Filters = None
        self._DirectConnectTunnelIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DirectConnectTunnelIds(self):
        return self._DirectConnectTunnelIds

    @DirectConnectTunnelIds.setter
    def DirectConnectTunnelIds(self, DirectConnectTunnelIds):
        self._DirectConnectTunnelIds = DirectConnectTunnelIds

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DirectConnectTunnelIds = params.get("DirectConnectTunnelIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels response structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelSet: List of dedicated tunnels.
        :type DirectConnectTunnelSet: list of DirectConnectTunnel
        :param _TotalCount: Number of eligible dedicated tunnels.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DirectConnectTunnelSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DirectConnectTunnelSet(self):
        return self._DirectConnectTunnelSet

    @DirectConnectTunnelSet.setter
    def DirectConnectTunnelSet(self, DirectConnectTunnelSet):
        self._DirectConnectTunnelSet = DirectConnectTunnelSet

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
        if params.get("DirectConnectTunnelSet") is not None:
            self._DirectConnectTunnelSet = []
            for item in params.get("DirectConnectTunnelSet"):
                obj = DirectConnectTunnel()
                obj._deserialize(item)
                self._DirectConnectTunnelSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions:
        :type Filters: list of Filter
        :param _DirectConnectIds: Array of connection IDs.
        :type DirectConnectIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._Filters = None
        self._DirectConnectIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DirectConnectIds(self):
        return self._DirectConnectIds

    @DirectConnectIds.setter
    def DirectConnectIds(self, DirectConnectIds):
        self._DirectConnectIds = DirectConnectIds

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DirectConnectIds = params.get("DirectConnectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects response structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectSet: List of connections.
        :type DirectConnectSet: list of DirectConnect
        :param _TotalCount: Number of eligible connection lists.
        :type TotalCount: int
        :param _AllSignLaw: Whether all connections under the account have the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AllSignLaw: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DirectConnectSet = None
        self._TotalCount = None
        self._AllSignLaw = None
        self._RequestId = None

    @property
    def DirectConnectSet(self):
        return self._DirectConnectSet

    @DirectConnectSet.setter
    def DirectConnectSet(self, DirectConnectSet):
        self._DirectConnectSet = DirectConnectSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AllSignLaw(self):
        return self._AllSignLaw

    @AllSignLaw.setter
    def AllSignLaw(self, AllSignLaw):
        self._AllSignLaw = AllSignLaw

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self._DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self._DirectConnectSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AllSignLaw = params.get("AllSignLaw")
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressQuotaRequest(AbstractModel):
    """DescribeInternetAddressQuota request structure.

    """


class DescribeInternetAddressQuotaResponse(AbstractModel):
    """DescribeInternetAddressQuota response structure.

    """

    def __init__(self):
        r"""
        :param _Ipv6PrefixLen: Minimum prefix length allowed for a public IPv6 address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv6PrefixLen: int
        :param _Ipv4BgpQuota: Quota of BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv4BgpQuota: int
        :param _Ipv4OtherQuota: Quota of non-BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv4OtherQuota: int
        :param _Ipv4BgpNum: Used number of BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv4BgpNum: int
        :param _Ipv4OtherNum: Used number of non-BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv4OtherNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ipv6PrefixLen = None
        self._Ipv4BgpQuota = None
        self._Ipv4OtherQuota = None
        self._Ipv4BgpNum = None
        self._Ipv4OtherNum = None
        self._RequestId = None

    @property
    def Ipv6PrefixLen(self):
        return self._Ipv6PrefixLen

    @Ipv6PrefixLen.setter
    def Ipv6PrefixLen(self, Ipv6PrefixLen):
        self._Ipv6PrefixLen = Ipv6PrefixLen

    @property
    def Ipv4BgpQuota(self):
        return self._Ipv4BgpQuota

    @Ipv4BgpQuota.setter
    def Ipv4BgpQuota(self, Ipv4BgpQuota):
        self._Ipv4BgpQuota = Ipv4BgpQuota

    @property
    def Ipv4OtherQuota(self):
        return self._Ipv4OtherQuota

    @Ipv4OtherQuota.setter
    def Ipv4OtherQuota(self, Ipv4OtherQuota):
        self._Ipv4OtherQuota = Ipv4OtherQuota

    @property
    def Ipv4BgpNum(self):
        return self._Ipv4BgpNum

    @Ipv4BgpNum.setter
    def Ipv4BgpNum(self, Ipv4BgpNum):
        self._Ipv4BgpNum = Ipv4BgpNum

    @property
    def Ipv4OtherNum(self):
        return self._Ipv4OtherNum

    @Ipv4OtherNum.setter
    def Ipv4OtherNum(self, Ipv4OtherNum):
        self._Ipv4OtherNum = Ipv4OtherNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ipv6PrefixLen = params.get("Ipv6PrefixLen")
        self._Ipv4BgpQuota = params.get("Ipv4BgpQuota")
        self._Ipv4OtherQuota = params.get("Ipv4OtherQuota")
        self._Ipv4BgpNum = params.get("Ipv4BgpNum")
        self._Ipv4OtherNum = params.get("Ipv4OtherNum")
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressRequest(AbstractModel):
    """DescribeInternetAddress request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filter conditions:
<li>AddrType, address type. Valid values: 0: BGP; 1: China Telecom; 2: China Mobile; 3: China Unicom</li>
<li>AddrProto, address protocol. Valid values: 0: IPv4; 1: IPv6</li>
<li>Status, address status. Valid values: 0: in use; 1: disabled; 2: returned</li>
<li>Subnet, public IP address array</li>
<InstanceIds>Public IP address ID array</li>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeInternetAddressResponse(AbstractModel):
    """DescribeInternetAddress response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of public IP addresses for internet tunnels
        :type TotalCount: int
        :param _Subnets: List of the public IP addresses for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Subnets: list of InternetAddressDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Subnets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Subnets(self):
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Subnets") is not None:
            self._Subnets = []
            for item in params.get("Subnets"):
                obj = InternetAddressDetail()
                obj._deserialize(item)
                self._Subnets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressStatisticsRequest(AbstractModel):
    """DescribeInternetAddressStatistics request structure.

    """


class DescribeInternetAddressStatisticsResponse(AbstractModel):
    """DescribeInternetAddressStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of public IP address statistics for internet tunnels
        :type TotalCount: int
        :param _InternetAddressStatistics: List of the public IP address statistics for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InternetAddressStatistics: list of InternetAddressStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InternetAddressStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InternetAddressStatistics(self):
        return self._InternetAddressStatistics

    @InternetAddressStatistics.setter
    def InternetAddressStatistics(self, InternetAddressStatistics):
        self._InternetAddressStatistics = InternetAddressStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InternetAddressStatistics") is not None:
            self._InternetAddressStatistics = []
            for item in params.get("InternetAddressStatistics"):
                obj = InternetAddressStatistics()
                obj._deserialize(item)
                self._InternetAddressStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DirectConnect(AbstractModel):
    """Connection information list.

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param _DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param _AccessPointId: Access point ID of a connection.
        :type AccessPointId: str
        :param _State: Connection status.
PENDING: Applying. 
REJECTED: Application rejected.   
TOPAY: Payment pending. 
PAID: Paid. 
ALLOCATED: Constructing.   
AVAILABLE: Available.  
DELETING: Deleting.
DELETED: Deleted.
        :type State: str
        :param _CreatedTime: Connection creation time.
        :type CreatedTime: str
        :param _EnabledTime: Connection activation time.
        :type EnabledTime: str
        :param _LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).
        :type LineOperator: str
        :param _Location: Location of a local IDC.
        :type Location: str
        :param _Bandwidth: Connection port bandwidth in Mbps.
        :type Bandwidth: int
        :param _PortType: User-side port type of a connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface; it is the default value), 1000Base-LX (1-Gigabit single-mode optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-mode optical Ethernet interface; 10 KM).
        :type PortType: str
        :param _CircuitCode: Circuit code of a connection, which is provided by the ISP or service provider.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CircuitCode: str
        :param _RedundantDirectConnectId: ID of a redundant connection.
        :type RedundantDirectConnectId: str
        :param _Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vlan: int
        :param _TencentAddress: Tencent-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TencentAddress: str
        :param _CustomerAddress: User-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerAddress: str
        :param _CustomerName: Name of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerName: str
        :param _CustomerContactMail: Email address of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerContactMail: str
        :param _CustomerContactNumber: Contact number of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerContactNumber: str
        :param _ExpiredTime: Connection expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _ChargeType: Connection billing mode. NON_RECURRING_CHARGE: One-time charge for accessing service
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _FaultReportContactPerson: Fault reporting contact person.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: Fault reporting contact number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaultReportContactNumber: str
        :param _TagSet: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _AccessPointType: Access point type of a connection.
        :type AccessPointType: str
        :param _IdcCity: IDC city.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdcCity: str
        :param _ChargeState: Billing status
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeState: str
        :param _StartTime: Connection activation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _SignLaw: Whether the connection has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SignLaw: bool
        :param _LocalZone: Whether the connection is an edge zone.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LocalZone: bool
        :param _VlanZeroDirectConnectTunnelCount: Number of dedicated tunnels with disabled VLAN in the connection
Note: this field may return `null`, indicating that no valid value can be found.
        :type VlanZeroDirectConnectTunnelCount: int
        :param _OtherVlanDirectConnectTunnelCount: Number of dedicated tunnels with enabled VLAN in the connection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OtherVlanDirectConnectTunnelCount: int
        :param _MinBandwidth: Minimum bandwidth of the connection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MinBandwidth: int
        """
        self._DirectConnectId = None
        self._DirectConnectName = None
        self._AccessPointId = None
        self._State = None
        self._CreatedTime = None
        self._EnabledTime = None
        self._LineOperator = None
        self._Location = None
        self._Bandwidth = None
        self._PortType = None
        self._CircuitCode = None
        self._RedundantDirectConnectId = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._ExpiredTime = None
        self._ChargeType = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._TagSet = None
        self._AccessPointType = None
        self._IdcCity = None
        self._ChargeState = None
        self._StartTime = None
        self._SignLaw = None
        self._LocalZone = None
        self._VlanZeroDirectConnectTunnelCount = None
        self._OtherVlanDirectConnectTunnelCount = None
        self._MinBandwidth = None

    @property
    def DirectConnectId(self):
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectName(self):
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def AccessPointId(self):
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EnabledTime(self):
        return self._EnabledTime

    @EnabledTime.setter
    def EnabledTime(self, EnabledTime):
        self._EnabledTime = EnabledTime

    @property
    def LineOperator(self):
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PortType(self):
        return self._PortType

    @PortType.setter
    def PortType(self, PortType):
        self._PortType = PortType

    @property
    def CircuitCode(self):
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def RedundantDirectConnectId(self):
        return self._RedundantDirectConnectId

    @RedundantDirectConnectId.setter
    def RedundantDirectConnectId(self, RedundantDirectConnectId):
        self._RedundantDirectConnectId = RedundantDirectConnectId

    @property
    def Vlan(self):
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def FaultReportContactPerson(self):
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AccessPointType(self):
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def IdcCity(self):
        return self._IdcCity

    @IdcCity.setter
    def IdcCity(self, IdcCity):
        self._IdcCity = IdcCity

    @property
    def ChargeState(self):
        return self._ChargeState

    @ChargeState.setter
    def ChargeState(self, ChargeState):
        self._ChargeState = ChargeState

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SignLaw(self):
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def LocalZone(self):
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def VlanZeroDirectConnectTunnelCount(self):
        return self._VlanZeroDirectConnectTunnelCount

    @VlanZeroDirectConnectTunnelCount.setter
    def VlanZeroDirectConnectTunnelCount(self, VlanZeroDirectConnectTunnelCount):
        self._VlanZeroDirectConnectTunnelCount = VlanZeroDirectConnectTunnelCount

    @property
    def OtherVlanDirectConnectTunnelCount(self):
        return self._OtherVlanDirectConnectTunnelCount

    @OtherVlanDirectConnectTunnelCount.setter
    def OtherVlanDirectConnectTunnelCount(self, OtherVlanDirectConnectTunnelCount):
        self._OtherVlanDirectConnectTunnelCount = OtherVlanDirectConnectTunnelCount

    @property
    def MinBandwidth(self):
        return self._MinBandwidth

    @MinBandwidth.setter
    def MinBandwidth(self, MinBandwidth):
        self._MinBandwidth = MinBandwidth


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectName = params.get("DirectConnectName")
        self._AccessPointId = params.get("AccessPointId")
        self._State = params.get("State")
        self._CreatedTime = params.get("CreatedTime")
        self._EnabledTime = params.get("EnabledTime")
        self._LineOperator = params.get("LineOperator")
        self._Location = params.get("Location")
        self._Bandwidth = params.get("Bandwidth")
        self._PortType = params.get("PortType")
        self._CircuitCode = params.get("CircuitCode")
        self._RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._ExpiredTime = params.get("ExpiredTime")
        self._ChargeType = params.get("ChargeType")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._AccessPointType = params.get("AccessPointType")
        self._IdcCity = params.get("IdcCity")
        self._ChargeState = params.get("ChargeState")
        self._StartTime = params.get("StartTime")
        self._SignLaw = params.get("SignLaw")
        self._LocalZone = params.get("LocalZone")
        self._VlanZeroDirectConnectTunnelCount = params.get("VlanZeroDirectConnectTunnelCount")
        self._OtherVlanDirectConnectTunnelCount = params.get("OtherVlanDirectConnectTunnelCount")
        self._MinBandwidth = params.get("MinBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnel(AbstractModel):
    """Dedicated tunnel information list.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        :param _DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param _State: Dedicated tunnel status.
AVAILABLE: Ready or connected.
PENDING: Applying.
ALLOCATING: Configuring.
ALLOCATED: Configured.
ALTERING: Modifying.
DELETING: Deleting.
DELETED: Deleted.
COMFIRMING: To be accepted.
REJECTED: Rejected.
        :type State: str
        :param _DirectConnectOwnerAccount: Connection owner, i.e., developer account ID.
        :type DirectConnectOwnerAccount: str
        :param _OwnerAccount: Dedicated tunnel owner, i.e., developer account ID.
        :type OwnerAccount: str
        :param _NetworkType: Network type. Valid values: VPC, BMVPC, CCN.
 VPC: Virtual Private Cloud; BMVPC: BM VPC; CCN: Cloud Connect Network.
        :type NetworkType: str
        :param _NetworkRegion: Network of the VPC region, such as `ap-guangzhou`.
        :type NetworkRegion: str
        :param _VpcId: Unified VPC ID or BMVPC ID.
        :type VpcId: str
        :param _DirectConnectGatewayId: Direct connect gateway ID.
        :type DirectConnectGatewayId: str
        :param _RouteType: BGP: BGP routing; STATIC: Static routing. Default value: BGP routing.
        :type RouteType: str
        :param _BgpPeer: User-side BGP, including Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: User-side IP range.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _Vlan: VLAN of a dedicated tunnel.
        :type Vlan: int
        :param _TencentAddress: TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param _CustomerAddress: CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param _DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param _CreatedTime: Creation time of a dedicated tunnel.
        :type CreatedTime: str
        :param _Bandwidth: Bandwidth value of a dedicated tunnel.
        :type Bandwidth: int
        :param _TagSet: Tag value of a dedicated tunnel.
        :type TagSet: list of Tag
        :param _NetDetectId: Associated custom network probe ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetDetectId: str
        :param _EnableBGPCommunity: BGP community switch
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableBGPCommunity: bool
        :param _NatType: Whether it is a NAT tunnel
Note: this field may return null, indicating that no valid values can be obtained.
        :type NatType: int
        :param _VpcRegion: VPC region abbreviation, such as `gz`, `cd`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcRegion: str
        :param _BfdEnable: Whether to enable BFD
Note: this field may return null, indicating that no valid values can be obtained.
        :type BfdEnable: int
        :param _AccessPointType: Access point type of a dedicated tunnel.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessPointType: str
        :param _DirectConnectGatewayName: Direct connect gateway name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DirectConnectGatewayName: str
        :param _VpcName: VPC name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param _TencentBackupAddress: Backup IP address on the Tencent side.
        :type TencentBackupAddress: str
        :param _SignLaw: Whether the connection associated with the dedicated tunnel has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SignLaw: bool
        :param _CloudAttachId: Cloud Attached Connection Service ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CloudAttachId: str
        """
        self._DirectConnectTunnelId = None
        self._DirectConnectId = None
        self._State = None
        self._DirectConnectOwnerAccount = None
        self._OwnerAccount = None
        self._NetworkType = None
        self._NetworkRegion = None
        self._VpcId = None
        self._DirectConnectGatewayId = None
        self._RouteType = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._DirectConnectTunnelName = None
        self._CreatedTime = None
        self._Bandwidth = None
        self._TagSet = None
        self._NetDetectId = None
        self._EnableBGPCommunity = None
        self._NatType = None
        self._VpcRegion = None
        self._BfdEnable = None
        self._AccessPointType = None
        self._DirectConnectGatewayName = None
        self._VpcName = None
        self._TencentBackupAddress = None
        self._SignLaw = None
        self._CloudAttachId = None

    @property
    def DirectConnectTunnelId(self):
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def DirectConnectId(self):
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DirectConnectOwnerAccount(self):
        return self._DirectConnectOwnerAccount

    @DirectConnectOwnerAccount.setter
    def DirectConnectOwnerAccount(self, DirectConnectOwnerAccount):
        self._DirectConnectOwnerAccount = DirectConnectOwnerAccount

    @property
    def OwnerAccount(self):
        return self._OwnerAccount

    @OwnerAccount.setter
    def OwnerAccount(self, OwnerAccount):
        self._OwnerAccount = OwnerAccount

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def NetworkRegion(self):
        return self._NetworkRegion

    @NetworkRegion.setter
    def NetworkRegion(self, NetworkRegion):
        self._NetworkRegion = NetworkRegion

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DirectConnectGatewayId(self):
        return self._DirectConnectGatewayId

    @DirectConnectGatewayId.setter
    def DirectConnectGatewayId(self, DirectConnectGatewayId):
        self._DirectConnectGatewayId = DirectConnectGatewayId

    @property
    def RouteType(self):
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def BgpPeer(self):
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def Vlan(self):
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def DirectConnectTunnelName(self):
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def NetDetectId(self):
        return self._NetDetectId

    @NetDetectId.setter
    def NetDetectId(self, NetDetectId):
        self._NetDetectId = NetDetectId

    @property
    def EnableBGPCommunity(self):
        return self._EnableBGPCommunity

    @EnableBGPCommunity.setter
    def EnableBGPCommunity(self, EnableBGPCommunity):
        self._EnableBGPCommunity = EnableBGPCommunity

    @property
    def NatType(self):
        return self._NatType

    @NatType.setter
    def NatType(self, NatType):
        self._NatType = NatType

    @property
    def VpcRegion(self):
        return self._VpcRegion

    @VpcRegion.setter
    def VpcRegion(self, VpcRegion):
        self._VpcRegion = VpcRegion

    @property
    def BfdEnable(self):
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def AccessPointType(self):
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def DirectConnectGatewayName(self):
        return self._DirectConnectGatewayName

    @DirectConnectGatewayName.setter
    def DirectConnectGatewayName(self, DirectConnectGatewayName):
        self._DirectConnectGatewayName = DirectConnectGatewayName

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def TencentBackupAddress(self):
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def SignLaw(self):
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def CloudAttachId(self):
        return self._CloudAttachId

    @CloudAttachId.setter
    def CloudAttachId(self, CloudAttachId):
        self._CloudAttachId = CloudAttachId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._DirectConnectId = params.get("DirectConnectId")
        self._State = params.get("State")
        self._DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self._OwnerAccount = params.get("OwnerAccount")
        self._NetworkType = params.get("NetworkType")
        self._NetworkRegion = params.get("NetworkRegion")
        self._VpcId = params.get("VpcId")
        self._DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self._RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self._CreatedTime = params.get("CreatedTime")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._NetDetectId = params.get("NetDetectId")
        self._EnableBGPCommunity = params.get("EnableBGPCommunity")
        self._NatType = params.get("NatType")
        self._VpcRegion = params.get("VpcRegion")
        self._BfdEnable = params.get("BfdEnable")
        self._AccessPointType = params.get("AccessPointType")
        self._DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self._VpcName = params.get("VpcName")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._SignLaw = params.get("SignLaw")
        self._CloudAttachId = params.get("CloudAttachId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressRequest(AbstractModel):
    """DisableInternetAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the internet tunnel’s public IP address
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
        


class DisableInternetAddressResponse(AbstractModel):
    """DisableInternetAddress response structure.

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


class EnableInternetAddressRequest(AbstractModel):
    """EnableInternetAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the internet tunnel’s public IP address
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
        


class EnableInternetAddressResponse(AbstractModel):
    """EnableInternetAddress response structure.

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


class Filter(AbstractModel):
    """Used for conditional filtering queries.

    """

    def __init__(self):
        r"""
        :param _Name: Fields to be filtered.
        :type Name: str
        :param _Values: Filter values of the field.
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
        


class InternetAddressDetail(AbstractModel):
    """Internet tunnel’s IP address details

    """

    def __init__(self):
        r"""
        :param _InstanceId: Internet tunnel’s IP address ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Subnet: Internet tunnel’s network address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Subnet: str
        :param _MaskLen: Mask length of a network address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaskLen: int
        :param _AddrType: Address type. Valid values: 0: BGP
1: China Telecom
2: China Mobile
3: China Unicom
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AddrType: int
        :param _Status: Address status. Valid values: 0: in use
1: disabled
2: returned
        :type Status: int
        :param _ApplyTime: Applied at
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ApplyTime: str
        :param _StopTime: Disabled at
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StopTime: str
        :param _ReleaseTime: Returned at
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReleaseTime: str
        :param _Region: Region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param _AppId: User ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AppId: int
        :param _AddrProto: Address protocol. Valid values: 0: IPv4; 1: IPv6
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AddrProto: int
        :param _ReserveTime: Retention period of a released IP address, in days
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReserveTime: int
        """
        self._InstanceId = None
        self._Subnet = None
        self._MaskLen = None
        self._AddrType = None
        self._Status = None
        self._ApplyTime = None
        self._StopTime = None
        self._ReleaseTime = None
        self._Region = None
        self._AppId = None
        self._AddrProto = None
        self._ReserveTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Subnet(self):
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def MaskLen(self):
        return self._MaskLen

    @MaskLen.setter
    def MaskLen(self, MaskLen):
        self._MaskLen = MaskLen

    @property
    def AddrType(self):
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def StopTime(self):
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AddrProto(self):
        return self._AddrProto

    @AddrProto.setter
    def AddrProto(self, AddrProto):
        self._AddrProto = AddrProto

    @property
    def ReserveTime(self):
        return self._ReserveTime

    @ReserveTime.setter
    def ReserveTime(self, ReserveTime):
        self._ReserveTime = ReserveTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Subnet = params.get("Subnet")
        self._MaskLen = params.get("MaskLen")
        self._AddrType = params.get("AddrType")
        self._Status = params.get("Status")
        self._ApplyTime = params.get("ApplyTime")
        self._StopTime = params.get("StopTime")
        self._ReleaseTime = params.get("ReleaseTime")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._AddrProto = params.get("AddrProto")
        self._ReserveTime = params.get("ReserveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAddressStatistics(AbstractModel):
    """Public IP address statistics of internet tunnels

    """

    def __init__(self):
        r"""
        :param _Region: Region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param _SubnetNum: Number of public IP addresses for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubnetNum: int
        """
        self._Region = None
        self._SubnetNum = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SubnetNum(self):
        return self._SubnetNum

    @SubnetNum.setter
    def SubnetNum(self, SubnetNum):
        self._SubnetNum = SubnetNum


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._SubnetNum = params.get("SubnetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param _DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param _CircuitCode: Circuit code of a connection, which is provided by the ISP or connection provider.
        :type CircuitCode: str
        :param _Vlan: VLAN for connection debugging.
        :type Vlan: int
        :param _TencentAddress: Tencent-side IP address for connection debugging.
        :type TencentAddress: str
        :param _CustomerAddress: User-side IP address for connection debugging.
        :type CustomerAddress: str
        :param _CustomerName: Name of connection applicant, which is obtained from the account system by default.
        :type CustomerName: str
        :param _CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.
        :type CustomerContactMail: str
        :param _CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.
        :type CustomerContactNumber: str
        :param _FaultReportContactPerson: Fault reporting contact person.
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: Fault reporting contact number.
        :type FaultReportContactNumber: str
        :param _SignLaw: Whether the connection applicant has signed the service agreement.
        :type SignLaw: bool
        :param _Bandwidth: Connection’s bandwidth
        :type Bandwidth: int
        """
        self._DirectConnectId = None
        self._DirectConnectName = None
        self._CircuitCode = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._SignLaw = None
        self._Bandwidth = None

    @property
    def DirectConnectId(self):
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectName(self):
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def CircuitCode(self):
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def Vlan(self):
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def FaultReportContactPerson(self):
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def SignLaw(self):
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectName = params.get("DirectConnectName")
        self._CircuitCode = params.get("CircuitCode")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        self._SignLaw = params.get("SignLaw")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute response structure.

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


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        :param _DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param _BgpPeer: User-side BGP, including Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: User-side IP range.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param _CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param _Bandwidth: Bandwidth value of a dedicated tunnel in Mbps.
        :type Bandwidth: int
        :param _TencentBackupAddress: Tencent-side standby IP address
        :type TencentBackupAddress: str
        """
        self._DirectConnectTunnelId = None
        self._DirectConnectTunnelName = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._Bandwidth = None
        self._TencentBackupAddress = None

    @property
    def DirectConnectTunnelId(self):
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def DirectConnectTunnelName(self):
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def BgpPeer(self):
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def TencentAddress(self):
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TencentBackupAddress(self):
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._Bandwidth = params.get("Bandwidth")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute response structure.

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


class NQAInfo(AbstractModel):
    """NQA configuration information

    """

    def __init__(self):
        r"""
        :param _ProbeFailedTimes: Number of health checks
        :type ProbeFailedTimes: int
        :param _Interval: Health check interval
        :type Interval: int
        :param _DestinationIp: IP address for the health check
        :type DestinationIp: str
        """
        self._ProbeFailedTimes = None
        self._Interval = None
        self._DestinationIp = None

    @property
    def ProbeFailedTimes(self):
        return self._ProbeFailedTimes

    @ProbeFailedTimes.setter
    def ProbeFailedTimes(self, ProbeFailedTimes):
        self._ProbeFailedTimes = ProbeFailedTimes

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def DestinationIp(self):
        return self._DestinationIp

    @DestinationIp.setter
    def DestinationIp(self, DestinationIp):
        self._DestinationIp = DestinationIp


    def _deserialize(self, params):
        self._ProbeFailedTimes = params.get("ProbeFailedTimes")
        self._Interval = params.get("Interval")
        self._DestinationIp = params.get("DestinationIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel request structure.

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: None.
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel response structure.

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


class ReleaseInternetAddressRequest(AbstractModel):
    """ReleaseInternetAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the internet tunnel’s public IP address
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
        


class ReleaseInternetAddressResponse(AbstractModel):
    """ReleaseInternetAddress response structure.

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


class RouteFilterPrefix(AbstractModel):
    """User-side IP range.

    """

    def __init__(self):
        r"""
        :param _Cidr: User-side IP range.
        :type Cidr: str
        """
        self._Cidr = None

    @property
    def Cidr(self):
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr


    def _deserialize(self, params):
        self._Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
Note: this field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Tag value
Note: this field may return null, indicating that no valid values can be obtained.
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
        