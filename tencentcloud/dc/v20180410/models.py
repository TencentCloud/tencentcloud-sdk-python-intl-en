# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AcceptDirectConnectTunnelRequest(AbstractModel):
    """AcceptDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: The connection owner accepts an application for sharing the dedicated tunnel
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccessPoint(AbstractModel):
    """

    """

    def __init__(self):
        """
        :param AccessPointName: 
        :type AccessPointName: str
        :param AccessPointId: 
        :type AccessPointId: str
        :param State: 
        :type State: str
        :param Location: 
        :type Location: str
        :param LineOperator: 
        :type LineOperator: list of str
        :param RegionId: 
        :type RegionId: str
        :param AvailablePortType: Available port type at the access point. Valid values: 1000BASE-T: gigabit electrical port; 1000BASE-LX: 10 km gigabit single-mode optical port; 1000BASE-ZX: 80 km gigabit single-mode optical port; 10GBASE-LR: 10 km 10-gigabit single-mode optical port; 10GBASE-ZR: 80 km 10-gigabit single-mode optical port; 10GBASE-LH: 40 km 10-gigabit single-mode optical port; 100GBASE-LR4: 10 km 100-gigabit single-mode optical portfiber optic port.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AvailablePortType: list of str
        """
        self.AccessPointName = None
        self.AccessPointId = None
        self.State = None
        self.Location = None
        self.LineOperator = None
        self.RegionId = None
        self.AvailablePortType = None


    def _deserialize(self, params):
        self.AccessPointName = params.get("AccessPointName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.Location = params.get("Location")
        self.LineOperator = params.get("LineOperator")
        self.RegionId = params.get("RegionId")
        self.AvailablePortType = params.get("AvailablePortType")


class BgpPeer(AbstractModel):
    """BGP parameter, including Asn and AuthKey.

    """

    def __init__(self):
        """
        :param Asn: User-side BGP Asn.
        :type Asn: int
        :param AuthKey: User-side BGP key.
        :type AuthKey: str
        """
        self.Asn = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.Asn = params.get("Asn")
        self.AuthKey = params.get("AuthKey")


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect request structure.

    """

    def __init__(self):
        """
        :param DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param AccessPointId: Access point of connection.
You can call `DescribeAccessPoints` to get the region ID. The selected access point must exist and be available.
        :type AccessPointId: str
        :param LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).
        :type LineOperator: str
        :param PortType: Port type of connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface), 1000Base-LX (1-Gigabit single-module optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-module optical Ethernet interface; 10 KM). Default value: 1000Base-LX.
        :type PortType: str
        :param CircuitCode: Circuit code of connection, which is provided by the ISP or connection provider.
        :type CircuitCode: str
        :param Location: Local IDC location.
        :type Location: str
        :param Bandwidth: Connection port bandwidth in Mbps. Value range: [2,10240]. Default value: 1000.
        :type Bandwidth: int
        :param RedundantDirectConnectId: ID of redundant connection.
        :type RedundantDirectConnectId: str
        :param Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.
        :type Vlan: int
        :param TencentAddress: Tencent-side IP address for connection debugging, which is automatically assigned by default.
        :type TencentAddress: str
        :param CustomerAddress: User-side IP address for connection debugging, which is automatically assigned by default.
        :type CustomerAddress: str
        :param CustomerName: Name of connection applicant, which is obtained from the account system by default.
        :type CustomerName: str
        :param CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.
        :type CustomerContactMail: str
        :param CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: Fault reporting contact person.
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: Fault reporting contact number.
        :type FaultReportContactNumber: str
        :param SignLaw: Whether the connection applicant has signed the service agreement. Default value: true.
        :type SignLaw: bool
        """
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


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect response structure.

    """

    def __init__(self):
        """
        :param DirectConnectIdSet: Connection ID.
        :type DirectConnectIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DirectConnectId: Direct Connect ID, such as `dc-kd7d06of`.
        :type DirectConnectId: str
        :param DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param DirectConnectOwnerAccount: Connection owner, who is the current customer by default.
The developer account ID should be entered for shared connections.
        :type DirectConnectOwnerAccount: str
        :param NetworkType: Network type. Valid values: VPC, BMVPC, CCN. Default value: VPC.
VPC: Virtual Private Cloud.
BMVPC: BM VPC.
CCN: Cloud Connect Network.
        :type NetworkType: str
        :param NetworkRegion: Network region.
        :type NetworkRegion: str
        :param VpcId: Unified VPC ID or BMVPC ID.
        :type VpcId: str
        :param DirectConnectGatewayId: Direct connect gateway ID, such as `dcg-d545ddf`.
        :type DirectConnectGatewayId: str
        :param Bandwidth: Direct Connect bandwidth in Mbps.
Default value: connection bandwidth value.
        :type Bandwidth: int
        :param RouteType: BGP: BGP routing.
STATIC: Static routing.
Default value: BGP routing.
        :type RouteType: str
        :param BgpPeer: BgpPeer, which is BGP information on the user side and includes Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: Static routing, i.e., IP range of the user's IDC.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: VLAN. Value range: 0-3,000.
0: sub-interface not enabled.
Default value: Non-zero.
        :type Vlan: int
        :param TencentAddress: TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param TencentBackupAddress: TencentBackupAddress, i.e., Tencent-side standby IP address
        :type TencentBackupAddress: str
        """
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


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelIdSet: Dedicated tunnel ID.
        :type DirectConnectTunnelIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DirectConnectId: Connection ID.
        :type DirectConnectId: str
        """
        self.DirectConnectId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints request structure.

    """

    def __init__(self):
        """
        :param RegionId: Access point region, which can be queried through `DescribeRegions`.

You can call `DescribeRegions` to get the region ID.
        :type RegionId: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.RegionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints response structure.

    """

    def __init__(self):
        """
        :param AccessPointSet: Access point information.
        :type AccessPointSet: list of AccessPoint
        :param TotalCount: Number of eligible access points.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>direct-connect-id: Connection instance ID, such as `dc-abcdefgh`.</li>
        :type Filters: list of Filter
        :param DirectConnectTunnelIds: Array of dedicated tunnel IDs.
        :type DirectConnectTunnelIds: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
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


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels response structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelSet: List of dedicated tunnels.
        :type DirectConnectTunnelSet: list of DirectConnectTunnel
        :param TotalCount: Number of eligible dedicated tunnels.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Filters: Filter conditions:
        :type Filters: list of Filter
        :param DirectConnectIds: Array of connection IDs.
        :type DirectConnectIds: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
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


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects response structure.

    """

    def __init__(self):
        """
        :param DirectConnectSet: List of connections.
        :type DirectConnectSet: list of DirectConnect
        :param TotalCount: Number of eligible connection lists.
        :type TotalCount: int
        :param AllSignLaw: Whether all connections under the account have the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AllSignLaw: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DirectConnect(AbstractModel):
    """Connection information list.

    """

    def __init__(self):
        """
        :param DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param AccessPointId: Access point ID of a connection.
        :type AccessPointId: str
        :param State: Connection status.
PENDING: Applying. 
REJECTED: Application rejected.   
TOPAY: Payment pending. 
PAID: Paid. 
ALLOCATED: Constructing.   
AVAILABLE: Available.  
DELETING: Deleting.
DELETED: Deleted.
        :type State: str
        :param CreatedTime: Connection creation time.
        :type CreatedTime: str
        :param EnabledTime: Connection activation time.
        :type EnabledTime: str
        :param LineOperator: ISP that provides connections. Valid values: ChinaTelecom (China Telecom), ChinaMobile (China Mobile), ChinaUnicom (China Unicom), In-houseWiring (in-house wiring), ChinaOther (other Chinese ISPs), InternationalOperator (international ISPs).
        :type LineOperator: str
        :param Location: Location of a local IDC.
        :type Location: str
        :param Bandwidth: Connection port bandwidth in Mbps.
        :type Bandwidth: int
        :param PortType: User-side port type of a connection. Valid values: 100Base-T (100-Megabit electrical Ethernet interface), 1000Base-T (1-Gigabit electrical Ethernet interface; it is the default value), 1000Base-LX (1-Gigabit single-mode optical Ethernet interface; 10 KM), 10GBase-T (10-Gigabit electrical Ethernet interface), 10GBase-LR (10-Gigabit single-mode optical Ethernet interface; 10 KM).
        :type PortType: str
        :param CircuitCode: Circuit code of a connection, which is provided by the ISP or service provider.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CircuitCode: str
        :param RedundantDirectConnectId: ID of a redundant connection.
        :type RedundantDirectConnectId: str
        :param Vlan: VLAN for connection debugging, which is enabled and automatically assigned by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vlan: int
        :param TencentAddress: Tencent-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TencentAddress: str
        :param CustomerAddress: User-side IP address for connection debugging.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerAddress: str
        :param CustomerName: Name of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerName: str
        :param CustomerContactMail: Email address of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerContactMail: str
        :param CustomerContactNumber: Contact number of the connection applicant, which is obtained from the account system by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomerContactNumber: str
        :param ExpiredTime: Connection expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param ChargeType: Connection billing mode. NON_RECURRING_CHARGE: One-time charge for accessing service
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param FaultReportContactPerson: Fault reporting contact person.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: Fault reporting contact number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaultReportContactNumber: str
        :param TagSet: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param AccessPointType: Access point type of a connection.
        :type AccessPointType: str
        :param IdcCity: IDC city.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdcCity: str
        :param ChargeState: Billing status
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeState: str
        :param StartTime: 
        :type StartTime: str
        :param SignLaw: Whether the connection has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SignLaw: bool
        """
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


class DirectConnectTunnel(AbstractModel):
    """Dedicated tunnel information list.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        :param DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param State: Dedicated tunnel status.
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
        :param DirectConnectOwnerAccount: Connection owner, i.e., developer account ID.
        :type DirectConnectOwnerAccount: str
        :param OwnerAccount: Dedicated tunnel owner, i.e., developer account ID.
        :type OwnerAccount: str
        :param NetworkType: Network type. Valid values: VPC, BMVPC, CCN.
 VPC: Virtual Private Cloud; BMVPC: BM VPC; CCN: Cloud Connect Network.
        :type NetworkType: str
        :param NetworkRegion: Network of the VPC region, such as `ap-guangzhou`.
        :type NetworkRegion: str
        :param VpcId: Unified VPC ID or BMVPC ID.
        :type VpcId: str
        :param DirectConnectGatewayId: Direct connect gateway ID.
        :type DirectConnectGatewayId: str
        :param RouteType: BGP: BGP routing; STATIC: Static routing. Default value: BGP routing.
        :type RouteType: str
        :param BgpPeer: User-side BGP, including Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: User-side IP range.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: VLAN of a dedicated tunnel.
        :type Vlan: int
        :param TencentAddress: TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param CreatedTime: Creation time of a dedicated tunnel.
        :type CreatedTime: str
        :param Bandwidth: Bandwidth value of a dedicated tunnel.
        :type Bandwidth: int
        :param TagSet: Tag value of a dedicated tunnel.
        :type TagSet: list of Tag
        :param NetDetectId: Associated custom network probe ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetDetectId: str
        :param EnableBGPCommunity: BGP community switch
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableBGPCommunity: bool
        :param NatType: Whether it is a NAT tunnel
Note: this field may return null, indicating that no valid values can be obtained.
        :type NatType: int
        :param VpcRegion: VPC region abbreviation, such as `gz`, `cd`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcRegion: str
        :param BfdEnable: Whether to enable BFD
Note: this field may return null, indicating that no valid values can be obtained.
        :type BfdEnable: int
        :param AccessPointType: Access point type of a dedicated tunnel.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessPointType: str
        :param DirectConnectGatewayName: Direct connect gateway name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DirectConnectGatewayName: str
        :param VpcName: VPC name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param TencentBackupAddress: 
        :type TencentBackupAddress: str
        :param SignLaw: Whether the connection associated with the dedicated tunnel has the service agreement signed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SignLaw: bool
        """
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


class Filter(AbstractModel):
    """Used for conditional filtering queries.

    """

    def __init__(self):
        """
        :param Name: Fields to be filtered.
        :type Name: str
        :param Values: Filter values of the field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectId: Connection ID.
        :type DirectConnectId: str
        :param DirectConnectName: Connection name.
        :type DirectConnectName: str
        :param CircuitCode: Circuit code of connection, which is provided by the ISP or connection provider.
        :type CircuitCode: str
        :param Vlan: VLAN for connection debugging.
        :type Vlan: int
        :param TencentAddress: Tencent-side IP address for connection debugging.
        :type TencentAddress: str
        :param CustomerAddress: User-side IP address for connection debugging.
        :type CustomerAddress: str
        :param CustomerName: Name of connection applicant, which is obtained from the account system by default.
        :type CustomerName: str
        :param CustomerContactMail: Email address of connection applicant, which is obtained from the account system by default.
        :type CustomerContactMail: str
        :param CustomerContactNumber: Contact number of connection applicant, which is obtained from the account system by default.
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: Fault reporting contact person.
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: Fault reporting contact number.
        :type FaultReportContactNumber: str
        :param SignLaw: Whether the connection applicant has signed the service agreement.
        :type SignLaw: bool
        """
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


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: Dedicated tunnel ID.
        :type DirectConnectTunnelId: str
        :param DirectConnectTunnelName: Dedicated tunnel name.
        :type DirectConnectTunnelName: str
        :param BgpPeer: User-side BGP, including Asn and AuthKey.
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: User-side IP range.
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param TencentAddress: Tencent-side IP address.
        :type TencentAddress: str
        :param CustomerAddress: User-side IP address.
        :type CustomerAddress: str
        :param Bandwidth: Bandwidth value of a dedicated tunnel in Mbps.
        :type Bandwidth: int
        :param TencentBackupAddress: Tencent-side standby IP address
        :type TencentBackupAddress: str
        """
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


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel request structure.

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: None.
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteFilterPrefix(AbstractModel):
    """User-side IP range.

    """

    def __init__(self):
        """
        :param Cidr: User-side IP range.
        :type Cidr: str
        """
        self.Cidr = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        """
        :param Key: Tag key
Note: this field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Tag value
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")