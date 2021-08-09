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
        """
        :param DirectConnectTunnelId: The connection owner accepts an application for sharing the dedicated tunnel\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccessPoint(AbstractModel):
    """Access point information.

    """

    def __init__(self):
        """
        :param AccessPointName: Access point name.\n        :type AccessPointName: str\n        :param AccessPointId: Unique access point ID.\n        :type AccessPointId: str\n        :param State: Access point status. Valid values: available, unavailable.\n        :type State: str\n        :param Location: Access point location.\n        :type Location: str\n        :param LineOperator: List of ISPs supported by access point.\n        :type LineOperator: list of str\n        :param RegionId: ID of the region that manages the access point.\n        :type RegionId: str\n        :param AvailablePortType: Available port type at the access point. Valid values: 1000BASE-T: gigabit electrical port; 1000BASE-LX: 10 km gigabit single-mode optical port; 1000BASE-ZX: 80 km gigabit single-mode optical port; 10GBASE-LR: 10 km 10-gigabit single-mode optical port; 10GBASE-ZR: 80 km 10-gigabit single-mode optical port; 10GBASE-LH: 40 km 10-gigabit single-mode optical port; 100GBASE-LR4: 10 km 100-gigabit single-mode optical portfiber optic port.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AvailablePortType: list of str\n        :param Coordinate: Latitude and longitude of the access point
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Coordinate: :class:`tencentcloud.dc.v20180410.models.Coordinate`\n        :param City: City where the access point is located
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type City: str\n        :param Area: Access point region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Area: str\n        """
        self.AccessPointName = None
        self.AccessPointId = None
        self.State = None
        self.Location = None
        self.LineOperator = None
        self.RegionId = None
        self.AvailablePortType = None
        self.Coordinate = None
        self.City = None
        self.Area = None


    def _deserialize(self, params):
        self.AccessPointName = params.get("AccessPointName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.Location = params.get("Location")
        self.LineOperator = params.get("LineOperator")
        self.RegionId = params.get("RegionId")
        self.AvailablePortType = params.get("AvailablePortType")
        if params.get("Coordinate") is not None:
            self.Coordinate = Coordinate()
            self.Coordinate._deserialize(params.get("Coordinate"))
        self.City = params.get("City")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressRequest(AbstractModel):
    """ApplyInternetAddress request structure.

    """

    def __init__(self):
        """
        :param MaskLen: Mask length of a CIDR block\n        :type MaskLen: int\n        :param AddrType: Address type. Valid values: 0: BGP
1: China Telecom
2: China Mobile
3: China Unicom\n        :type AddrType: int\n        :param AddrProto: Address protocol. Valid values: 0: IPv4
1: IPv6\n        :type AddrProto: int\n        """
        self.MaskLen = None
        self.AddrType = None
        self.AddrProto = None


    def _deserialize(self, params):
        self.MaskLen = params.get("MaskLen")
        self.AddrType = params.get("AddrType")
        self.AddrProto = params.get("AddrProto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressResponse(AbstractModel):
    """ApplyInternetAddress response structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the internet tunnel’s public IP address
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class BgpPeer(AbstractModel):
    """BGP parameter, including Asn and AuthKey.

    """

    def __init__(self):
        """
        :param Asn: User-side BGP Asn.\n        :type Asn: int\n        :param AuthKey: User-side BGP key.\n        :type AuthKey: str\n        """
        self.Asn = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.Asn = params.get("Asn")
        self.AuthKey = params.get("AuthKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """Coordinate describing the longitude and latitude.

    """

    def __init__(self):
        """
        :param Lat: Latitude\n        :type Lat: float\n        :param Lng: Longitude\n        :type Lng: float\n        """
        self.Lat = None
        self.Lng = None


    def _deserialize(self, params):
        self.Lat = params.get("Lat")
        self.Lng = params.get("Lng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect request structure.

    """

    def __init__(self):
        """
        :param DirectConnectName: Connection name.\n        :type DirectConnectName: str\n        :param AccessPointId: Access point of connection.
You can call `DescribeAccessPoints` to get the region ID. The selected access point must exist and be available.\n        :type AccessPointId: str\n        :param LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).\n        :type LineOperator: str\n        :param PortType: Port type of connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface), 1000Base-LX (1-Gigabit single-module optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-module optical Ethernet interface; 10 KM). Default value: 1000Base-LX.\n        :type PortType: str\n        :param CircuitCode: Circuit code of a connection, which is provided by the ISP or connection provider.\n        :type CircuitCode: str\n        :param Location: Local IDC location.\n        :type Location: str\n        :param Bandwidth: Connection port bandwidth in Mbps. Value range: [2,10240]. Default value: 1000.\n        :type Bandwidth: int\n        :param RedundantDirectConnectId: ID of redundant connection.\n        :type RedundantDirectConnectId: str\n        :param Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.\n        :type Vlan: int\n        :param TencentAddress: Tencent-side IP address for connection debugging, which is automatically assigned by default.\n        :type TencentAddress: str\n        :param CustomerAddress: User-side IP address for connection debugging, which is automatically assigned by default.\n        :type CustomerAddress: str\n        :param CustomerName: Name of connection applicant, which is obtained from the account system by default.\n        :type CustomerName: str\n        :param CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.\n        :type CustomerContactNumber: str\n        :param FaultReportContactPerson: Fault reporting contact person.\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: Fault reporting contact number.\n        :type FaultReportContactNumber: str\n        :param SignLaw: Whether the connection applicant has signed the service agreement. Default value: true.\n        :type SignLaw: bool\n        """
        self.DirectConnectName = None
        self.AccessPointId = None
        self.LineOperator = None
        self.PortType = None
        self.CircuitCode = None
        self.Location = None
        self.Bandwidth = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.SignLaw = None


    def _deserialize(self, params):
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.LineOperator = params.get("LineOperator")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.Location = params.get("Location")
        self.Bandwidth = params.get("Bandwidth")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        self.SignLaw = params.get("SignLaw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect response structure.

    """

    def __init__(self):
        """
        :param DirectConnectIdSet: Connection ID.\n        :type DirectConnectIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DirectConnectIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectIdSet = params.get("DirectConnectIdSet")
        self.RequestId = params.get("RequestId")


class CreateDirectConnectTunnelRequest(AbstractModel):
    """CreateDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectId: Direct Connect ID, such as `dc-kd7d06of`.\n        :type DirectConnectId: str\n        :param DirectConnectTunnelName: Dedicated tunnel name.\n        :type DirectConnectTunnelName: str\n        :param DirectConnectOwnerAccount: Connection owner, who is the current customer by default.
The developer account ID should be entered for shared connections.\n        :type DirectConnectOwnerAccount: str\n        :param NetworkType: Network type. Valid values: VPC, BMVPC, CCN. Default value: VPC.
VPC: Virtual Private Cloud.
BMVPC: BM VPC.
CCN: Cloud Connect Network.\n        :type NetworkType: str\n        :param NetworkRegion: Network region.\n        :type NetworkRegion: str\n        :param VpcId: Unified VPC ID or BMVPC ID.\n        :type VpcId: str\n        :param DirectConnectGatewayId: Direct connect gateway ID, such as `dcg-d545ddf`.\n        :type DirectConnectGatewayId: str\n        :param Bandwidth: Direct Connect bandwidth in Mbps.
Default value: connection bandwidth value.\n        :type Bandwidth: int\n        :param RouteType: BGP: BGP routing.
STATIC: Static routing.
Default value: BGP routing.\n        :type RouteType: str\n        :param BgpPeer: BgpPeer, which is BGP information on the user side and includes Asn and AuthKey.\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: Static routing, i.e., IP range of the user's IDC.\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param Vlan: VLAN. Value range: 0-3,000.
0: sub-interface not enabled.
Default value: Non-zero.\n        :type Vlan: int\n        :param TencentAddress: TencentAddress: Tencent-side IP address.\n        :type TencentAddress: str\n        :param CustomerAddress: CustomerAddress: User-side IP address.\n        :type CustomerAddress: str\n        :param TencentBackupAddress: TencentBackupAddress, i.e., Tencent-side standby IP address\n        :type TencentBackupAddress: str\n        :param CloudAttachId: Cloud Attached Connection Service ID\n        :type CloudAttachId: str\n        """
        self.DirectConnectId = None
        self.DirectConnectTunnelName = None
        self.DirectConnectOwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.Bandwidth = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.TencentBackupAddress = None
        self.CloudAttachId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.CloudAttachId = params.get("CloudAttachId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelIdSet: Dedicated tunnel ID.\n        :type DirectConnectTunnelIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DirectConnectTunnelIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelIdSet = params.get("DirectConnectTunnelIdSet")
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectRequest(AbstractModel):
    """DeleteDirectConnect request structure.

    """

    def __init__(self):
        """
        :param DirectConnectId: Connection ID.\n        :type DirectConnectId: str\n        """
        self.DirectConnectId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints request structure.

    """

    def __init__(self):
        """
        :param RegionId: Access point region, which can be queried through `DescribeRegions`.

You can call `DescribeRegions` to get the region ID.\n        :type RegionId: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.RegionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints response structure.

    """

    def __init__(self):
        """
        :param AccessPointSet: Access point information.\n        :type AccessPointSet: list of AccessPoint\n        :param TotalCount: Number of eligible access points.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AccessPointSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessPointSet") is not None:
            self.AccessPointSet = []
            for item in params.get("AccessPointSet"):
                obj = AccessPoint()
                obj._deserialize(item)
                self.AccessPointSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelsRequest(AbstractModel):
    """DescribeDirectConnectTunnels request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions:
This parameter does not support specifying `DirectConnectTunnelIds` and `Filters` at the same time.
<li> direct-connect-tunnel-name: Dedicated tunnel name.</li>
<li> direct-connect-tunnel-id: Dedicated tunnel instance ID, such as `dcx-abcdefgh`.</li>
<li>direct-connect-id: Connection instance ID, such as `dc-abcdefgh`.</li>\n        :type Filters: list of Filter\n        :param DirectConnectTunnelIds: Array of dedicated tunnel IDs.\n        :type DirectConnectTunnelIds: list of str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.Filters = None
        self.DirectConnectTunnelIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectTunnelIds = params.get("DirectConnectTunnelIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels response structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelSet: List of dedicated tunnels.\n        :type DirectConnectTunnelSet: list of DirectConnectTunnel\n        :param TotalCount: Number of eligible dedicated tunnels.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DirectConnectTunnelSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectTunnelSet") is not None:
            self.DirectConnectTunnelSet = []
            for item in params.get("DirectConnectTunnelSet"):
                obj = DirectConnectTunnel()
                obj._deserialize(item)
                self.DirectConnectTunnelSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions:\n        :type Filters: list of Filter\n        :param DirectConnectIds: Array of connection IDs.\n        :type DirectConnectIds: list of str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.Filters = None
        self.DirectConnectIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectIds = params.get("DirectConnectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects response structure.

    """

    def __init__(self):
        """
        :param DirectConnectSet: List of connections.\n        :type DirectConnectSet: list of DirectConnect\n        :param TotalCount: Number of eligible connection lists.\n        :type TotalCount: int\n        :param AllSignLaw: Whether all connections under the account have the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AllSignLaw: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DirectConnectSet = None
        self.TotalCount = None
        self.AllSignLaw = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self.DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self.DirectConnectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.AllSignLaw = params.get("AllSignLaw")
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressQuotaRequest(AbstractModel):
    """DescribeInternetAddressQuota request structure.

    """


class DescribeInternetAddressQuotaResponse(AbstractModel):
    """DescribeInternetAddressQuota response structure.

    """

    def __init__(self):
        """
        :param Ipv6PrefixLen: Minimum prefix length allowed for a public IPv6 address
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Ipv6PrefixLen: int\n        :param Ipv4BgpQuota: Quota of BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Ipv4BgpQuota: int\n        :param Ipv4OtherQuota: Quota of non-BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Ipv4OtherQuota: int\n        :param Ipv4BgpNum: Used number of BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Ipv4BgpNum: int\n        :param Ipv4OtherNum: Used number of non-BGP IPv4 addresses
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Ipv4OtherNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Ipv6PrefixLen = None
        self.Ipv4BgpQuota = None
        self.Ipv4OtherQuota = None
        self.Ipv4BgpNum = None
        self.Ipv4OtherNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ipv6PrefixLen = params.get("Ipv6PrefixLen")
        self.Ipv4BgpQuota = params.get("Ipv4BgpQuota")
        self.Ipv4OtherQuota = params.get("Ipv4OtherQuota")
        self.Ipv4BgpNum = params.get("Ipv4BgpNum")
        self.Ipv4OtherNum = params.get("Ipv4OtherNum")
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressRequest(AbstractModel):
    """DescribeInternetAddress request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param Filters: Filter conditions:
<li>AddrType, address type. Valid values: 0: BGP; 1: China Telecom; 2: China Mobile; 3: China Unicom</li>
<li>AddrProto, address protocol. Valid values: 0: IPv4; 1: IPv6</li>
<li>Status, address status. Valid values: 0: in use; 1: disabled; 2: returned</li>
<li>Subnet, public IP address array</li>
<InstanceIds>Public IP address ID array</li>\n        :type Filters: list of Filter\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeInternetAddressResponse(AbstractModel):
    """DescribeInternetAddress response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of public IP addresses for internet tunnels\n        :type TotalCount: int\n        :param Subnets: List of the public IP addresses for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Subnets: list of InternetAddressDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Subnets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = InternetAddressDetail()
                obj._deserialize(item)
                self.Subnets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressStatisticsRequest(AbstractModel):
    """DescribeInternetAddressStatistics request structure.

    """


class DescribeInternetAddressStatisticsResponse(AbstractModel):
    """DescribeInternetAddressStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of public IP address statistics for internet tunnels\n        :type TotalCount: int\n        :param InternetAddressStatistics: List of the public IP address statistics for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InternetAddressStatistics: list of InternetAddressStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InternetAddressStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InternetAddressStatistics") is not None:
            self.InternetAddressStatistics = []
            for item in params.get("InternetAddressStatistics"):
                obj = InternetAddressStatistics()
                obj._deserialize(item)
                self.InternetAddressStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DirectConnect(AbstractModel):
    """Connection information list.

    """

    def __init__(self):
        """
        :param DirectConnectId: Connection ID.\n        :type DirectConnectId: str\n        :param DirectConnectName: Connection name.\n        :type DirectConnectName: str\n        :param AccessPointId: Access point ID of a connection.\n        :type AccessPointId: str\n        :param State: Connection status.
PENDING: Applying. 
REJECTED: Application rejected.   
TOPAY: Payment pending. 
PAID: Paid. 
ALLOCATED: Constructing.   
AVAILABLE: Available.  
DELETING: Deleting.
DELETED: Deleted.\n        :type State: str\n        :param CreatedTime: Connection creation time.\n        :type CreatedTime: str\n        :param EnabledTime: Connection activation time.\n        :type EnabledTime: str\n        :param LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).\n        :type LineOperator: str\n        :param Location: Location of a local IDC.\n        :type Location: str\n        :param Bandwidth: Connection port bandwidth in Mbps.\n        :type Bandwidth: int\n        :param PortType: User-side port type of a connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface; it is the default value), 1000Base-LX (1-Gigabit single-mode optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-mode optical Ethernet interface; 10 KM).\n        :type PortType: str\n        :param CircuitCode: Circuit code of a connection, which is provided by the ISP or service provider.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CircuitCode: str\n        :param RedundantDirectConnectId: ID of a redundant connection.\n        :type RedundantDirectConnectId: str\n        :param Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Vlan: int\n        :param TencentAddress: Tencent-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TencentAddress: str\n        :param CustomerAddress: User-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CustomerAddress: str\n        :param CustomerName: Name of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CustomerName: str\n        :param CustomerContactMail: Email address of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: Contact number of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CustomerContactNumber: str\n        :param ExpiredTime: Connection expiration time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpiredTime: str\n        :param ChargeType: Connection billing mode. NON_RECURRING_CHARGE: One-time charge for accessing service
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeType: str\n        :param FaultReportContactPerson: Fault reporting contact person.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: Fault reporting contact number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FaultReportContactNumber: str\n        :param TagSet: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagSet: list of Tag\n        :param AccessPointType: Access point type of a connection.\n        :type AccessPointType: str\n        :param IdcCity: IDC city.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IdcCity: str\n        :param ChargeState: Billing status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeState: str\n        :param StartTime: Connection activation time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTime: str\n        :param SignLaw: Whether the connection has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type SignLaw: bool\n        :param LocalZone: Whether the connection is an edge zone.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LocalZone: bool\n        :param VlanZeroDirectConnectTunnelCount: Number of dedicated tunnels with disabled VLAN in the connection
Note: this field may return `null`, indicating that no valid value can be found.\n        :type VlanZeroDirectConnectTunnelCount: int\n        :param OtherVlanDirectConnectTunnelCount: Number of dedicated tunnels with enabled VLAN in the connection
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type OtherVlanDirectConnectTunnelCount: int\n        :param MinBandwidth: Minimum bandwidth of the connection
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MinBandwidth: int\n        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.AccessPointId = None
        self.State = None
        self.CreatedTime = None
        self.EnabledTime = None
        self.LineOperator = None
        self.Location = None
        self.Bandwidth = None
        self.PortType = None
        self.CircuitCode = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.ExpiredTime = None
        self.ChargeType = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.TagSet = None
        self.AccessPointType = None
        self.IdcCity = None
        self.ChargeState = None
        self.StartTime = None
        self.SignLaw = None
        self.LocalZone = None
        self.VlanZeroDirectConnectTunnelCount = None
        self.OtherVlanDirectConnectTunnelCount = None
        self.MinBandwidth = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.EnabledTime = params.get("EnabledTime")
        self.LineOperator = params.get("LineOperator")
        self.Location = params.get("Location")
        self.Bandwidth = params.get("Bandwidth")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.ExpiredTime = params.get("ExpiredTime")
        self.ChargeType = params.get("ChargeType")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.AccessPointType = params.get("AccessPointType")
        self.IdcCity = params.get("IdcCity")
        self.ChargeState = params.get("ChargeState")
        self.StartTime = params.get("StartTime")
        self.SignLaw = params.get("SignLaw")
        self.LocalZone = params.get("LocalZone")
        self.VlanZeroDirectConnectTunnelCount = params.get("VlanZeroDirectConnectTunnelCount")
        self.OtherVlanDirectConnectTunnelCount = params.get("OtherVlanDirectConnectTunnelCount")
        self.MinBandwidth = params.get("MinBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnel(AbstractModel):
    """Dedicated tunnel information list.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.\n        :type DirectConnectTunnelId: str\n        :param DirectConnectId: Connection ID.\n        :type DirectConnectId: str\n        :param State: Dedicated tunnel status.
AVAILABLE: Ready or connected.
PENDING: Applying.
ALLOCATING: Configuring.
ALLOCATED: Configured.
ALTERING: Modifying.
DELETING: Deleting.
DELETED: Deleted.
COMFIRMING: To be accepted.
REJECTED: Rejected.\n        :type State: str\n        :param DirectConnectOwnerAccount: Connection owner, i.e., developer account ID.\n        :type DirectConnectOwnerAccount: str\n        :param OwnerAccount: Dedicated tunnel owner, i.e., developer account ID.\n        :type OwnerAccount: str\n        :param NetworkType: Network type. Valid values: VPC, BMVPC, CCN.
 VPC: Virtual Private Cloud; BMVPC: BM VPC; CCN: Cloud Connect Network.\n        :type NetworkType: str\n        :param NetworkRegion: Network of the VPC region, such as `ap-guangzhou`.\n        :type NetworkRegion: str\n        :param VpcId: Unified VPC ID or BMVPC ID.\n        :type VpcId: str\n        :param DirectConnectGatewayId: Direct connect gateway ID.\n        :type DirectConnectGatewayId: str\n        :param RouteType: BGP: BGP routing; STATIC: Static routing. Default value: BGP routing.\n        :type RouteType: str\n        :param BgpPeer: User-side BGP, including Asn and AuthKey.\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: User-side IP range.\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param Vlan: VLAN of a dedicated tunnel.\n        :type Vlan: int\n        :param TencentAddress: TencentAddress: Tencent-side IP address.\n        :type TencentAddress: str\n        :param CustomerAddress: CustomerAddress: User-side IP address.\n        :type CustomerAddress: str\n        :param DirectConnectTunnelName: Dedicated tunnel name.\n        :type DirectConnectTunnelName: str\n        :param CreatedTime: Creation time of a dedicated tunnel.\n        :type CreatedTime: str\n        :param Bandwidth: Bandwidth value of a dedicated tunnel.\n        :type Bandwidth: int\n        :param TagSet: Tag value of a dedicated tunnel.\n        :type TagSet: list of Tag\n        :param NetDetectId: Associated custom network probe ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NetDetectId: str\n        :param EnableBGPCommunity: BGP community switch
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnableBGPCommunity: bool\n        :param NatType: Whether it is a NAT tunnel
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NatType: int\n        :param VpcRegion: VPC region abbreviation, such as `gz`, `cd`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VpcRegion: str\n        :param BfdEnable: Whether to enable BFD
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BfdEnable: int\n        :param AccessPointType: Access point type of a dedicated tunnel.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AccessPointType: str\n        :param DirectConnectGatewayName: Direct connect gateway name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DirectConnectGatewayName: str\n        :param VpcName: VPC name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VpcName: str\n        :param TencentBackupAddress: Backup IP address on the Tencent side.\n        :type TencentBackupAddress: str\n        :param SignLaw: Whether the connection associated with the dedicated tunnel has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type SignLaw: bool\n        :param CloudAttachId: Cloud Attached Connection Service ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CloudAttachId: str\n        """
        self.DirectConnectTunnelId = None
        self.DirectConnectId = None
        self.State = None
        self.DirectConnectOwnerAccount = None
        self.OwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.DirectConnectTunnelName = None
        self.CreatedTime = None
        self.Bandwidth = None
        self.TagSet = None
        self.NetDetectId = None
        self.EnableBGPCommunity = None
        self.NatType = None
        self.VpcRegion = None
        self.BfdEnable = None
        self.AccessPointType = None
        self.DirectConnectGatewayName = None
        self.VpcName = None
        self.TencentBackupAddress = None
        self.SignLaw = None
        self.CloudAttachId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectId = params.get("DirectConnectId")
        self.State = params.get("State")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.OwnerAccount = params.get("OwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.CreatedTime = params.get("CreatedTime")
        self.Bandwidth = params.get("Bandwidth")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.NetDetectId = params.get("NetDetectId")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatType = params.get("NatType")
        self.VpcRegion = params.get("VpcRegion")
        self.BfdEnable = params.get("BfdEnable")
        self.AccessPointType = params.get("AccessPointType")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcName = params.get("VpcName")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.SignLaw = params.get("SignLaw")
        self.CloudAttachId = params.get("CloudAttachId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressRequest(AbstractModel):
    """DisableInternetAddress request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the internet tunnel’s public IP address\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressResponse(AbstractModel):
    """DisableInternetAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableInternetAddressRequest(AbstractModel):
    """EnableInternetAddress request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the internet tunnel’s public IP address\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableInternetAddressResponse(AbstractModel):
    """EnableInternetAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Used for conditional filtering queries.

    """

    def __init__(self):
        """
        :param Name: Fields to be filtered.\n        :type Name: str\n        :param Values: Filter values of the field.\n        :type Values: list of str\n        """
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
        


class InternetAddressDetail(AbstractModel):
    """Internet tunnel’s IP address details

    """

    def __init__(self):
        """
        :param InstanceId: Internet tunnel’s IP address ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param Subnet: Internet tunnel’s network address
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Subnet: str\n        :param MaskLen: Mask length of a network address
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MaskLen: int\n        :param AddrType: Address type. Valid values: 0: BGP
1: China Telecom
2: China Mobile
3: China Unicom
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AddrType: int\n        :param Status: Address status. Valid values: 0: in use
1: disabled
2: returned\n        :type Status: int\n        :param ApplyTime: Applied at
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ApplyTime: str\n        :param StopTime: Disabled at
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type StopTime: str\n        :param ReleaseTime: Returned at
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ReleaseTime: str\n        :param Region: Region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Region: str\n        :param AppId: User ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AppId: int\n        :param AddrProto: Address protocol. Valid values: 0: IPv4; 1: IPv6
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AddrProto: int\n        :param ReserveTime: Retention period of a released IP address, in days
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ReserveTime: int\n        """
        self.InstanceId = None
        self.Subnet = None
        self.MaskLen = None
        self.AddrType = None
        self.Status = None
        self.ApplyTime = None
        self.StopTime = None
        self.ReleaseTime = None
        self.Region = None
        self.AppId = None
        self.AddrProto = None
        self.ReserveTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Subnet = params.get("Subnet")
        self.MaskLen = params.get("MaskLen")
        self.AddrType = params.get("AddrType")
        self.Status = params.get("Status")
        self.ApplyTime = params.get("ApplyTime")
        self.StopTime = params.get("StopTime")
        self.ReleaseTime = params.get("ReleaseTime")
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.AddrProto = params.get("AddrProto")
        self.ReserveTime = params.get("ReserveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAddressStatistics(AbstractModel):
    """Public IP address statistics of internet tunnels

    """

    def __init__(self):
        """
        :param Region: Region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Region: str\n        :param SubnetNum: Number of public IP addresses for internet tunnels
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SubnetNum: int\n        """
        self.Region = None
        self.SubnetNum = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.SubnetNum = params.get("SubnetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectId: Connection ID.\n        :type DirectConnectId: str\n        :param DirectConnectName: Connection name.\n        :type DirectConnectName: str\n        :param CircuitCode: Circuit code of a connection, which is provided by the ISP or connection provider.\n        :type CircuitCode: str\n        :param Vlan: VLAN for connection debugging.\n        :type Vlan: int\n        :param TencentAddress: Tencent-side IP address for connection debugging.\n        :type TencentAddress: str\n        :param CustomerAddress: User-side IP address for connection debugging.\n        :type CustomerAddress: str\n        :param CustomerName: Name of connection applicant, which is obtained from the account system by default.\n        :type CustomerName: str\n        :param CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.\n        :type CustomerContactNumber: str\n        :param FaultReportContactPerson: Fault reporting contact person.\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: Fault reporting contact number.\n        :type FaultReportContactNumber: str\n        :param SignLaw: Whether the connection applicant has signed the service agreement.\n        :type SignLaw: bool\n        :param Bandwidth: Connection’s bandwidth\n        :type Bandwidth: int\n        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.CircuitCode = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.SignLaw = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.CircuitCode = params.get("CircuitCode")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        self.SignLaw = params.get("SignLaw")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.\n        :type DirectConnectTunnelId: str\n        :param DirectConnectTunnelName: Dedicated tunnel name.\n        :type DirectConnectTunnelName: str\n        :param BgpPeer: User-side BGP, including Asn and AuthKey.\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: User-side IP range.\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param TencentAddress: Tencent-side IP address.\n        :type TencentAddress: str\n        :param CustomerAddress: User-side IP address.\n        :type CustomerAddress: str\n        :param Bandwidth: Bandwidth value of a dedicated tunnel in Mbps.\n        :type Bandwidth: int\n        :param TencentBackupAddress: Tencent-side standby IP address\n        :type TencentBackupAddress: str\n        """
        self.DirectConnectTunnelId = None
        self.DirectConnectTunnelName = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.Bandwidth = None
        self.TencentBackupAddress = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: None.\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseInternetAddressRequest(AbstractModel):
    """ReleaseInternetAddress request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of the internet tunnel’s public IP address\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseInternetAddressResponse(AbstractModel):
    """ReleaseInternetAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteFilterPrefix(AbstractModel):
    """User-side IP range.

    """

    def __init__(self):
        """
        :param Cidr: User-side IP range.\n        :type Cidr: str\n        """
        self.Cidr = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        """
        :param Key: Tag key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Key: str\n        :param Value: Tag value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Value: str\n        """
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
        