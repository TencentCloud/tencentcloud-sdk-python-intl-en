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


class AcceptAttachCcnInstancesRequest(AbstractModel):
    """AcceptAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param Instances: List of associated instances.
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class AcceptAttachCcnInstancesResponse(AbstractModel):
    """AcceptAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccountAttribute(AbstractModel):
    """Account attribute object

    """

    def __init__(self):
        """
        :param AttributeName: Attribute name
        :type AttributeName: str
        :param AttributeValues: Attribute values
        :type AttributeValues: list of str
        """
        self.AttributeName = None
        self.AttributeValues = None


    def _deserialize(self, params):
        self.AttributeName = params.get("AttributeName")
        self.AttributeValues = params.get("AttributeValues")


class AddBandwidthPackageResourcesRequest(AbstractModel):
    """AddBandwidthPackageResources request structure.

    """

    def __init__(self):
        """
        :param ResourceIds: The unique ID of the source, such as 'eip-xxxx' and 'lb-xxxx'. EIP and LB resources are currently supported.
        :type ResourceIds: list of str
        :param BandwidthPackageId: The unique ID of the bandwidth package, such as 'bwp-xxxx'.
        :type BandwidthPackageId: str
        :param NetworkType: The network type of the bandwidth package. Valid value: `BGP`, indicating that the internal resource is a BGP IP.
        :type NetworkType: str
        :param ResourceType: The resource type, including `Address` and `LoadBalance`.
        :type ResourceType: str
        :param Protocol: The protocol type of the bandwidth package. Valid values: `ipv4` and `ipv6`.
        :type Protocol: str
        """
        self.ResourceIds = None
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ResourceType = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ResourceType = params.get("ResourceType")
        self.Protocol = params.get("Protocol")


class AddBandwidthPackageResourcesResponse(AbstractModel):
    """AddBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Address(AbstractModel):
    """Detailed EIP information

    """

    def __init__(self):
        """
        :param AddressId: `EIP` `ID`, the unique ID of the `EIP`.
        :type AddressId: str
        :param AddressName: The `EIP` name.
        :type AddressName: str
        :param AddressStatus: Possible `EIP` states are 'CREATING', 'BINDING', 'BIND', 'UNBINDING', 'UNBIND', 'OFFLINING', and 'BIND_ENI'.
        :type AddressStatus: str
        :param AddressIp: The public IP address
        :type AddressIp: str
        :param InstanceId: The ID of the bound resource instance. This can be a `CVM` or `NAT`.
        :type InstanceId: str
        :param CreatedTime: The creation time, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param NetworkInterfaceId: The ID of the bound ENI
        :type NetworkInterfaceId: str
        :param PrivateAddressIp: The private IP of the bound resources
        :type PrivateAddressIp: str
        :param IsArrears: The isolation status of the resource. `True` indicates the EIP is isolated. `False` indicates that the resource is not isolated.
        :type IsArrears: bool
        :param IsBlocked: The block status of the resource. `True` indicates the EIP is blocked. `False` indicates that the EIP is not blocked.
        :type IsBlocked: bool
        :param IsEipDirectConnection: Whether the EIP supports direct connection mode. `True` indicates the EIP supports direct connection. `False` indicates that the resource does not support direct connection.
        :type IsEipDirectConnection: bool
        :param AddressType: The resource type of the EIP. This includes `CalcIP`, `WanIP`, `EIP`, and `AnycastEIP`. Among these, `CalcIP` indicates the device IP, `WanIP` indicates the common public IP, `EIP` indicates Elastic IP, and `AnycastEip` indicates accelerated EIP.
        :type AddressType: str
        :param CascadeRelease: Whether the EIP is automatically released after being unbound. `True` indicates the EIP will be automatically released after being unbound. `False` indicates the EIP will not be automatically released after being unbound.
        :type CascadeRelease: bool
        :param EipAlgType: Type of the protocol used in EIP ALG
        :type EipAlgType: :class:`tencentcloud.vpc.v20170312.models.AlgType`
        :param InternetServiceProvider: The ISP of an EIP/Elastic IP, with possible return values currently including "CMCC", "CTCC", "CUCC" and "BGP"
        :type InternetServiceProvider: str
        :param LocalBgp: Whether the EIP is in a local BGP.
        :type LocalBgp: bool
        :param Bandwidth: Bandwidth value of EIP. The EIP for the bill-by-CVM account will return `null`.
Note: this field may return `null`, indicating that no valid value was found.
        :type Bandwidth: int
        :param InternetChargeType: Network billing mode of EIP. The EIP for the bill-by-CVM account will return `null`.
Note: this field may return `null`, indicating that no valid value was found.
        :type InternetChargeType: str
        """
        self.AddressId = None
        self.AddressName = None
        self.AddressStatus = None
        self.AddressIp = None
        self.InstanceId = None
        self.CreatedTime = None
        self.NetworkInterfaceId = None
        self.PrivateAddressIp = None
        self.IsArrears = None
        self.IsBlocked = None
        self.IsEipDirectConnection = None
        self.AddressType = None
        self.CascadeRelease = None
        self.EipAlgType = None
        self.InternetServiceProvider = None
        self.LocalBgp = None
        self.Bandwidth = None
        self.InternetChargeType = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.AddressStatus = params.get("AddressStatus")
        self.AddressIp = params.get("AddressIp")
        self.InstanceId = params.get("InstanceId")
        self.CreatedTime = params.get("CreatedTime")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateAddressIp = params.get("PrivateAddressIp")
        self.IsArrears = params.get("IsArrears")
        self.IsBlocked = params.get("IsBlocked")
        self.IsEipDirectConnection = params.get("IsEipDirectConnection")
        self.AddressType = params.get("AddressType")
        self.CascadeRelease = params.get("CascadeRelease")
        if params.get("EipAlgType") is not None:
            self.EipAlgType = AlgType()
            self.EipAlgType._deserialize(params.get("EipAlgType"))
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.LocalBgp = params.get("LocalBgp")
        self.Bandwidth = params.get("Bandwidth")
        self.InternetChargeType = params.get("InternetChargeType")


class AddressChargePrepaid(AbstractModel):
    """EIP cost object

    """

    def __init__(self):
        """
        :param Period: Purchased usage period, in month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36
        :type Period: int
        :param AutoRenewFlag: Setting of renewal. Valid values: 0: manual renewal; 1: auto-renewal; 2: no renewal after expiration. Default value: 0
        :type AutoRenewFlag: int
        """
        self.Period = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class AddressTemplate(AbstractModel):
    """IP address template

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP address template name.
        :type AddressTemplateName: str
        :param AddressTemplateId: The unique ID of the IP address template instance.
        :type AddressTemplateId: str
        :param AddressSet: IP address information.
        :type AddressSet: list of str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        """
        self.AddressTemplateName = None
        self.AddressTemplateId = None
        self.AddressSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressSet = params.get("AddressSet")
        self.CreatedTime = params.get("CreatedTime")


class AddressTemplateGroup(AbstractModel):
    """IP address template group

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP address template group name.
        :type AddressTemplateGroupName: str
        :param AddressTemplateGroupId: IP address template group instance ID, such as `ipmg-dih8xdbq`.
        :type AddressTemplateGroupId: str
        :param AddressTemplateIdSet: IP address template ID.
        :type AddressTemplateIdSet: list of str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param AddressTemplateSet: IP address template instance
        :type AddressTemplateSet: list of AddressTemplateItem
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateGroupId = None
        self.AddressTemplateIdSet = None
        self.CreatedTime = None
        self.AddressTemplateSet = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateIdSet = params.get("AddressTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplateItem()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)


class AddressTemplateItem(AbstractModel):
    """Address information

    """

    def __init__(self):
        """
        :param From: Start address
        :type From: str
        :param To: End address
        :type To: str
        """
        self.From = None
        self.To = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")


class AddressTemplateSpecification(AbstractModel):
    """IP address template.

    """

    def __init__(self):
        """
        :param AddressId: The ID of the IP address, such as `ipm-2uw6ujo6`.
        :type AddressId: str
        :param AddressGroupId: The ID of the IP address group, such as `ipmg-2uw6ujo6`.
        :type AddressGroupId: str
        """
        self.AddressId = None
        self.AddressGroupId = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressGroupId = params.get("AddressGroupId")


class AlgType(AbstractModel):
    """ALG protocol type

    """

    def __init__(self):
        """
        :param Ftp: Whether FTP ALG is enabled
        :type Ftp: bool
        :param Sip: Whether SIP ALG is enabled
        :type Sip: bool
        """
        self.Ftp = None
        self.Sip = None


    def _deserialize(self, params):
        self.Ftp = params.get("Ftp")
        self.Sip = params.get("Sip")


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses request structure.

    """

    def __init__(self):
        """
        :param AddressCount: The number of EIPs. Default: 1.
        :type AddressCount: int
        :param InternetServiceProvider: The EIP line type. Default: BGP.
<ul style="margin:0"><li>For a user who has activated the static single-line IP allowlist, possible values are:<ul><li>CMCC: China Mobile</li>
<li>CTCC: China Telecom</li>
<li>CUCC: China Unicom</li></ul>Note: Only certain regions support static single-line IP addresses.</li></ul>
        :type InternetServiceProvider: str
        :param InternetChargeType: The EIP billing method.
<ul style="margin:0"><li>For bill-by-IP account beta users, valid values: <ul><li>BANDWIDTH_PACKAGE: paid by the [bandwidth package](https://intl.cloud.tencent.com/document/product/684/15255?from_cn_redirect=1)(who must also be bandwidth package beta users)</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR: billed by hourly bandwidth on a pay-as-you-go basis</li>
<li>BANDWIDTH_PREPAID_BY_MONTH: monthly bandwidth subscription</li>
<li>TRAFFIC_POSTPAID_BY_HOUR: billed by hourly traffic on a pay-as-you-go basis</li></ul>Default value: TRAFFIC_POSTPAID_BY_HOUR</li>
<li>If you are not a bill-by-IP account beta user, the EIP billing is the same as that for the instance bound to the EIP. Therefore, you do not need to pass in this parameter.</li></ul>
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: The EIP outbound bandwidth cap, in Mbps.
<ul style="margin:0"><li>For bill-by-IP account beta users, valid values:<ul><li>BANDWIDTH_PACKAGE: 1 Mbps to 1000 Mbps</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li>
<li>BANDWIDTH_PREPAID_BY_MONTH: 1 Mbps to 200 Mbps</li>
<li>TRAFFIC_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li></ul>Default value: 1 Mbps</li>
<li>If you are not a bill-by-IP account beta user, the EIP outbound bandwidth cap is subject to that of the instance bound to the EIP. Therefore, you do not need to pass in this parameter.</li></ul>
        :type InternetMaxBandwidthOut: int
        :param AddressChargePrepaid: A required billing parameter for an EIP billed by monthly bandwidth subscription. For EIPs using other billing modes, it can be ignored.
        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`
        :param AddressType: The EIP type. Default: EIP.
<ul style="margin:0"><li>For a user who has activated the AIA allowlist, possible values are:<ul><li>AnycastEIP: an Anycast EIP address. For more information, see [Anycast Internet Acceleration](https://intl.cloud.tencent.com/document/product/644?from_cn_redirect=1).</li></ul>Note: Only certain regions support Anycast EIPs.</li></ul>
        :type AddressType: str
        :param AnycastZone: Anycast publishing region
<ul style="margin:0"><li>Valid for users who have activated AIA. Values:<ul><li>ANYCAST_ZONE_GLOBAL: global publishing region </li><li>ANYCAST_ZONE_OVERSEAS: overseas publishing region</li><li><b>**[Disused]**</b> ANYCAST_ZONE_A: publishing region A (updated to ANYCAST_ZONE_GLOBAL)</li><li><b>**[Disused]**</b> ANYCAST_ZONE_B: publishing region B (updated to ANYCAST_ZONE_GLOBAL)</li></ul>Default: ANYCAST_ZONE_OVERSEAS.</li></ul>
        :type AnycastZone: str
        :param ApplicableForCLB: <b>**[Disused]**</b>
Whether the Anycast EIP can be bound to CLB instances.
<ul style="margin:0"><li>Valid for users who have activated the AIA. Values:<ul><li>TRUE: the Anycast EIP can be bound to CLB instances.</li>
<li>FALSE: the Anycast EIP can be bound to CVMs, NAT gateways, and HAVIPs.</li></ul>Default: FALSE.</li></ul>
        :type ApplicableForCLB: bool
        :param Tags: List of tags to be bound.
        :type Tags: list of Tag
        :param BandwidthPackageId: The unique ID of a BGP bandwidth package. If you configure this parameter and set InternetChargeType as BANDWIDTH_PACKAGE, the new EIP is added to this package and billed by the bandwidth package mode.
        :type BandwidthPackageId: str
        """
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressChargePrepaid = None
        self.AddressType = None
        self.AnycastZone = None
        self.ApplicableForCLB = None
        self.Tags = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))
        self.AddressType = params.get("AddressType")
        self.AnycastZone = params.get("AnycastZone")
        self.ApplicableForCLB = params.get("ApplicableForCLB")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses response structure.

    """

    def __init__(self):
        """
        :param AddressSet: List of the unique IDs of the requested EIPs.
        :type AddressSet: list of str
        :param TaskId: The Async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: A list of `IPv6` addresses. You can specify a maximum of 10 at one time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one.
        :type Ipv6Addresses: list of Ipv6Address
        :param Ipv6AddressCount: The number of automatically assigned `IPv6` addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one.
        :type Ipv6AddressCount: int
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: The list of `IPv6` addresses assigned to ENIs.
        :type Ipv6AddressSet: list of Ipv6Address
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ipv6AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignIpv6CidrBlockRequest(AbstractModel):
    """AssignIpv6CidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class AssignIpv6CidrBlockResponse(AbstractModel):
    """AssignIpv6CidrBlock response structure.

    """

    def __init__(self):
        """
        :param Ipv6CidrBlock: The assigned `IPv6` IP range, such as `3402:4e00:20:1000::/56`
        :type Ipv6CidrBlock: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ipv6CidrBlock = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.RequestId = params.get("RequestId")


class AssignIpv6SubnetCidrBlockRequest(AbstractModel):
    """AssignIpv6SubnetCidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param Ipv6SubnetCidrBlocks: The assigned `IPv6` subnet IP range list.
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)


class AssignIpv6SubnetCidrBlockResponse(AbstractModel):
    """AssignIpv6SubnetCidrBlock response structure.

    """

    def __init__(self):
        """
        :param Ipv6SubnetCidrBlockSet: The assigned `IPv6` subnet IP range list.
        :type Ipv6SubnetCidrBlockSet: list of Ipv6SubnetCidrBlock
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ipv6SubnetCidrBlockSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6SubnetCidrBlockSet") is not None:
            self.Ipv6SubnetCidrBlockSet = []
            for item in params.get("Ipv6SubnetCidrBlockSet"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlockSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: The information on private IP addresses, of which you can specify a maximum of 10 at a time. You should provide either this parameter or SecondaryPrivateIpAddressCount, or both.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: The number of newly-applied private IP addresses. You should provide either this parameter or PrivateIpAddresses, or both. The total number of private IP addresses cannot exceed the quota. For more information, see<a href="/document/product/576/18527">ENI Use Limits</a>.
        :type SecondaryPrivateIpAddressCount: int
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param PrivateIpAddressSet: The detailed information of the Private IP.
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssistantCidr(AbstractModel):
    """Information about the secondary CIDR of the VPC.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of a `VPC` instance, such as `vpc-6v2ht8q5`.
        :type VpcId: str
        :param CidrBlock: The secondary CIDR, such as `172.16.0.0/16`.
        :type CidrBlock: str
        :param AssistantType: The secondary CIDR block type. 0: common secondary CIDR block. 1: container secondary CIDR block. Default: 0.
        :type AssistantType: int
        :param SubnetSet: Subnets divided by the secondary CIDR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetSet: list of Subnet
        """
        self.VpcId = None
        self.CidrBlock = None
        self.AssistantType = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.AssistantType = params.get("AssistantType")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.
        :type AddressId: str
        :param InstanceId: The ID of the instance to be bound, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API.
        :type InstanceId: str
        :param NetworkInterfaceId: The ID of the ENI to be bonud, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. You can query the ENI ID by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `networkInterfaceId` field in the returned result of [DescribeNetworkInterfaces](https://intl.cloud.tencent.com/document/api/215/15817?from_cn_redirect=1) API.
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: The private IP to be bound. If you specify `NetworkInterfaceId`, then you must also specify `PrivateIpAddress`, indicating the EIP is bound to the specified private IP of the specified ENI. At the same time, you must ensure the specified `PrivateIpAddress` is a private IP on the `NetworkInterfaceId`. You can query the private IP of the specified ENI by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `privateIpAddress` field in the returned result of [DescribeNetworkInterfaces](https://intl.cloud.tencent.com/document/api/215/15817?from_cn_redirect=1) API.
        :type PrivateIpAddress: str
        """
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssociateDirectConnectGatewayNatGatewayRequest(AbstractModel):
    """AssociateDirectConnectGatewayNatGateway request structure.

    """

    def __init__(self):
        """
        :param VpcId: The direct connect gateway ID.
        :type VpcId: str
        :param NatGatewayId: The NAT Gateway ID.
        :type NatGatewayId: str
        :param DirectConnectGatewayId: The ID of the VPC instance, which can be obtained from the `VpcId` field in response of the `DescribeVpcs` API.
        :type DirectConnectGatewayId: str
        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class AssociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """AssociateDirectConnectGatewayNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNatGatewayAddressRequest(AbstractModel):
    """AssociateNatGatewayAddress request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param AddressCount: The number of EIPs you want to apply for. The system will create the same number of EIPs as you require. Either `AddressCount` or `PublicAddresses` must be passed in.
        :type AddressCount: int
        :param PublicIpAddresses: Array of the EIPs bound to the NAT gateway. Either `AddressCount` or `PublicAddresses` must be passed in.
        :type PublicIpAddresses: list of str
        :param Zone: The availability zone of the EIP, which is passed in when the EIP is automatically assigned.
        :type Zone: str
        """
        self.NatGatewayId = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")


class AssociateNatGatewayAddressResponse(AbstractModel):
    """AssociateNatGatewayAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkAclSubnetsRequest(AbstractModel):
    """AssociateNetworkAclSubnets request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.
        :type NetworkAclId: str
        :param SubnetIds: Array of subnet instance IDs. Example: [subnet-12345678]
        :type SubnetIds: list of str
        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")


class AssociateNetworkAclSubnetsResponse(AbstractModel):
    """AssociateNetworkAclSubnets response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request.
        :type NetworkInterfaceIds: list of str
        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request.
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class AssociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param Instances: List of associated network instances
        :type Instances: list of CcnInstance
        :param CcnUin: The UIN (root account) of the CCN. By default, the current account belongs to the UIN
        :type CcnUin: str
        """
        self.CcnId = None
        self.Instances = None
        self.CcnUin = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.CcnUin = params.get("CcnUin")


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachClassicLinkVpcRequest(AbstractModel):
    """AttachClassicLinkVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID
        :type VpcId: str
        :param InstanceIds: CVM Instance ID
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class AttachClassicLinkVpcResponse(AbstractModel):
    """AttachClassicLinkVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param InstanceId: The ID of the CVM instance, such as `ins-r8hr2upy`.
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditCrossBorderComplianceRequest(AbstractModel):
    """AuditCrossBorderCompliance request structure.

    """

    def __init__(self):
        """
        :param ServiceProvider: Service provider. Valid values: `UNICOM`.
        :type ServiceProvider: str
        :param ComplianceId: Unique ID of compliance review request.
        :type ComplianceId: int
        :param AuditBehavior: Audit behavior. Valid values: `APPROVED` and `DENY`.
        :type AuditBehavior: str
        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.AuditBehavior = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.AuditBehavior = params.get("AuditBehavior")


class AuditCrossBorderComplianceResponse(AbstractModel):
    """AuditCrossBorderCompliance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPackage(AbstractModel):
    """The structure of information of the bandwidth package.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package.
        :type BandwidthPackageId: str
        :param NetworkType: The bandwidth package type. Valid values: 'BGP', 'SINGLEISP', and 'ANYCAST'
        :type NetworkType: str
        :param ChargeType: The bandwidth package billing mode. Valid values: 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'
        :type ChargeType: str
        :param BandwidthPackageName: The name of the bandwidth package.
        :type BandwidthPackageName: str
        :param CreatedTime: The creation time of the bandwidth package, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param Status: The status of the bandwidth package. Valid values: 'CREATING', 'CREATED', 'DELETING', and 'DELETED'.
        :type Status: str
        :param ResourceSet: The resource information of the bandwidth package.
        :type ResourceSet: list of Resource
        :param Bandwidth: The limit of the bandwidth package in Mbps. The value '-1' indicates there is no limit.
        :type Bandwidth: int
        """
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.CreatedTime = None
        self.Status = None
        self.ResourceSet = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.CreatedTime = params.get("CreatedTime")
        self.Status = params.get("Status")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.Bandwidth = params.get("Bandwidth")


class BandwidthPackageBillBandwidth(AbstractModel):
    """Current billable usage of a pay-as-you-go bandwidth package

    """

    def __init__(self):
        """
        :param BandwidthUsage: Current billable usage, in Mbps
        :type BandwidthUsage: int
        """
        self.BandwidthUsage = None


    def _deserialize(self, params):
        self.BandwidthUsage = params.get("BandwidthUsage")


class CCN(AbstractModel):
    """The CCN object

    """

    def __init__(self):
        """
        :param CcnId: The unique ID of the CCN
        :type CcnId: str
        :param CcnName: The name of the CCN
        :type CcnName: str
        :param CcnDescription: The detailed information of the CCN
        :type CcnDescription: str
        :param InstanceCount: The number of associated instances
        :type InstanceCount: int
        :param CreateTime: The creation time
        :type CreateTime: str
        :param State: The instance status. 'ISOLATED': Being isolated (instance is in arrears and service is suspended). 'AVAILABLE': Operating.
        :type State: str
        :param QosLevel: The instance service quality. ’PT’: Platinum , 'AU': Gold, 'AG': Silver.
        :type QosLevel: str
        :param InstanceChargeType: The billing method. POSTPAID indicates postpaid.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceChargeType: str
        :param BandwidthLimitType: The limit type. INTER_REGION_LIMIT is the limit between regions. OUTER_REGION_LIMIT is a region egress limit.
Note: This field may return null, indicating no valid value.
        :type BandwidthLimitType: str
        :param TagSet: Tag key-value pairs.
        :type TagSet: list of Tag
        :param RoutePriorityFlag: Whether the CCN route priority feature is supported. Valid values: False: do not support; True: support.
        :type RoutePriorityFlag: bool
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None
        self.InstanceCount = None
        self.CreateTime = None
        self.State = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.TagSet = None
        self.RoutePriorityFlag = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.InstanceCount = params.get("InstanceCount")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.RoutePriorityFlag = params.get("RoutePriorityFlag")


class CcnAttachedInstance(AbstractModel):
    """The instance object associated with a CCN

    """

    def __init__(self):
        """
        :param CcnId: The ID of a CCN instance.
        :type CcnId: str
        :param InstanceType: The type of associated instances:
<li>`VPC`: VPC</li>
<li>`DIRECTCONNECT`: Direct Connect</li>
<li>`BMVPC`: BM VPC</li>
        :type InstanceType: str
        :param InstanceId: The ID of the associated instance.
        :type InstanceId: str
        :param InstanceName: The name of the associated instance.
        :type InstanceName: str
        :param InstanceRegion: The region to which the associated instance belongs, such as `ap-guangzhou`.
        :type InstanceRegion: str
        :param InstanceUin: The UIN (root account) to which the associated instance belongs.
        :type InstanceUin: str
        :param CidrBlock: The CIDR of the associated instance.
        :type CidrBlock: list of str
        :param State: The status of the associated instance:
<li>`PENDING`: In application</li>
<li>`ACTIVE`: Connected</li>
<li>`EXPIRED`: Expired</li>
<li>`REJECTED`: Rejected</li>
<li>`DELETED`: Deleted</li>
<li>`FAILED`: Failed (it will be asynchronously unbound after 2 hours)</li>
<li>`ATTACHING`: binding</li>
<li>`DETACHING`: Unbinding</li>
<li>`DETACHFAILED`: The unbinding failed (it will be asynchronously unbound after 2 hours)</li>
        :type State: str
        :param AttachedTime: Association Time.
        :type AttachedTime: str
        :param CcnUin: The UIN (root account) to which the CCN belongs.
        :type CcnUin: str
        :param InstanceArea: General location of the associated instance, such as CHINA_MAINLAND.
        :type InstanceArea: str
        """
        self.CcnId = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.InstanceUin = None
        self.CidrBlock = None
        self.State = None
        self.AttachedTime = None
        self.CcnUin = None
        self.InstanceArea = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceUin = params.get("InstanceUin")
        self.CidrBlock = params.get("CidrBlock")
        self.State = params.get("State")
        self.AttachedTime = params.get("AttachedTime")
        self.CcnUin = params.get("CcnUin")
        self.InstanceArea = params.get("InstanceArea")


class CcnBandwidthInfo(AbstractModel):
    """The information of the cross-region bandwidth limit for CCN instances.

    """

    def __init__(self):
        """
        :param CcnId: The CCN ID that the bandwidth belongs to.
Note: this field may return null, indicating that no valid value was found.
        :type CcnId: str
        :param CreatedTime: The creation time of the instance.
Note: this field may return null, indicating that no valid value was found.
        :type CreatedTime: str
        :param ExpiredTime: The expiration time of the instance.
Note: this field may return null, indicating that no valid value was found.
        :type ExpiredTime: str
        :param RegionFlowControlId: The unique ID of the bandwidth instance.
Note: this field may return null, indicating that no valid value was found.
        :type RegionFlowControlId: str
        :param RenewFlag: The billing flag.
Note: this field may return null, indicating that no valid value was found.
        :type RenewFlag: str
        :param CcnRegionBandwidthLimit: The information of the bandwidth regions and bandwidth caps. The parameter is only returned for the cross-region limit mode, but not for egress limit.
Note: this field may return null, indicating that no valid value was found.
        :type CcnRegionBandwidthLimit: :class:`tencentcloud.vpc.v20170312.models.CcnRegionBandwidthLimit`
        """
        self.CcnId = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.RegionFlowControlId = None
        self.RenewFlag = None
        self.CcnRegionBandwidthLimit = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RegionFlowControlId = params.get("RegionFlowControlId")
        self.RenewFlag = params.get("RenewFlag")
        if params.get("CcnRegionBandwidthLimit") is not None:
            self.CcnRegionBandwidthLimit = CcnRegionBandwidthLimit()
            self.CcnRegionBandwidthLimit._deserialize(params.get("CcnRegionBandwidthLimit"))


class CcnInstance(AbstractModel):
    """The instance object associated with a CCN.

    """

    def __init__(self):
        """
        :param InstanceId: The ID of the associated instance.
        :type InstanceId: str
        :param InstanceRegion: The region to which the associated instance ID belongs, such as `ap-guangzhou`.
        :type InstanceRegion: str
        :param InstanceType: The type of the associated instance. Available values are:
<li>`VPC`: VPC</li>
<li>`DIRECTCONNECT`: Direct Connect</li>
<li>`BMVPC`: BM VPC</li>
        :type InstanceType: str
        """
        self.InstanceId = None
        self.InstanceRegion = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceType = params.get("InstanceType")


class CcnRegionBandwidthLimit(AbstractModel):
    """The outbound bandwidth cap of the CCN region

    """

    def __init__(self):
        """
        :param Region: Region, such as `ap-guangzhou`
        :type Region: str
        :param BandwidthLimit: The outbound bandwidth cap. Units: Mbps
        :type BandwidthLimit: int
        :param IsBm: Whether it is a BM region. The default is `false`.
        :type IsBm: bool
        :param DstRegion: The target region, such as `ap-shanghai`
Note: This field may return null, indicating no valid value.
        :type DstRegion: str
        :param DstIsBm: Whether the target region is a BM region. The default is `false`.
        :type DstIsBm: bool
        """
        self.Region = None
        self.BandwidthLimit = None
        self.IsBm = None
        self.DstRegion = None
        self.DstIsBm = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.BandwidthLimit = params.get("BandwidthLimit")
        self.IsBm = params.get("IsBm")
        self.DstRegion = params.get("DstRegion")
        self.DstIsBm = params.get("DstIsBm")


class CcnRoute(AbstractModel):
    """The CCN routing policy object

    """

    def __init__(self):
        """
        :param RouteId: The ID of the routing policy
        :type RouteId: str
        :param DestinationCidrBlock: Destination
        :type DestinationCidrBlock: str
        :param InstanceType: The type of the next hop (associated instance type). Available types: VPC, DIRECTCONNECT
        :type InstanceType: str
        :param InstanceId: The next hop (associated instance)
        :type InstanceId: str
        :param InstanceName: The name of the next hop (associated instance name)
        :type InstanceName: str
        :param InstanceRegion: The region of the next hop (the region of the associated instance)
        :type InstanceRegion: str
        :param UpdateTime: Update Time
        :type UpdateTime: str
        :param Enabled: Whether the route is enabled
        :type Enabled: bool
        :param InstanceUin: The UIN (root account) to which the associated instance belongs
        :type InstanceUin: str
        :param ExtraState: Additional status of the route
        :type ExtraState: str
        :param IsBgp: Whether it is a dynamic route
        :type IsBgp: bool
        :param RoutePriority: Route priority
        :type RoutePriority: int
        :param InstanceExtraName: Next hop port name (associated instance’s port name)
        :type InstanceExtraName: str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.UpdateTime = None
        self.Enabled = None
        self.InstanceUin = None
        self.ExtraState = None
        self.IsBgp = None
        self.RoutePriority = None
        self.InstanceExtraName = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.UpdateTime = params.get("UpdateTime")
        self.Enabled = params.get("Enabled")
        self.InstanceUin = params.get("InstanceUin")
        self.ExtraState = params.get("ExtraState")
        self.IsBgp = params.get("IsBgp")
        self.RoutePriority = params.get("RoutePriority")
        self.InstanceExtraName = params.get("InstanceExtraName")


class CheckAssistantCidrRequest(AbstractModel):
    """CheckAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.
        :type VpcId: str
        :param NewCidrBlocks: Load CIDR blocks to add. CIDR block set; format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type NewCidrBlocks: list of str
        :param OldCidrBlocks: Load CIDR blocks to delete. CIDR block set; Format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type OldCidrBlocks: list of str
        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")


class CheckAssistantCidrResponse(AbstractModel):
    """CheckAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param ConflictSourceSet: Array of conflict resources.
        :type ConflictSourceSet: list of ConflictSource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConflictSourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConflictSourceSet") is not None:
            self.ConflictSourceSet = []
            for item in params.get("ConflictSourceSet"):
                obj = ConflictSource()
                obj._deserialize(item)
                self.ConflictSourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class CheckNetDetectStateRequest(AbstractModel):
    """CheckNetDetectState request structure.

    """

    def __init__(self):
        """
        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.
        :type DetectDestinationIp: list of str
        :param NextHopType: The type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.
        :type NextHopType: str
        :param NextHopDestination: The next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.
        :type NextHopDestination: str
        :param NetDetectId: ID of a network inspector instance, e.g. netd-12345678. Enter at least one of this parameter, VpcId, SubnetId, and NetDetectName. Use NetDetectId if it is present.
        :type NetDetectId: str
        :param VpcId: ID of a `VPC` instance, e.g. `vpc-12345678`, which is used together with SubnetId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.
        :type VpcId: str
        :param SubnetId: ID of a subnet instance, e.g. `subnet-12345678`, which is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.
        :type SubnetId: str
        :param NetDetectName: The name of a network inspector, up to 60 bytes in length. It is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.
        :type NetDetectName: str
        """
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectId = None
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectId = params.get("NetDetectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")


class CheckNetDetectStateResponse(AbstractModel):
    """CheckNetDetectState response structure.

    """

    def __init__(self):
        """
        :param NetDetectIpStateSet: The array of network detection verification results.
        :type NetDetectIpStateSet: list of NetDetectIpState
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetDetectIpStateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)
        self.RequestId = params.get("RequestId")


class ClassicLinkInstance(AbstractModel):
    """Classiclink instance

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID
        :type VpcId: str
        :param InstanceId: The unique ID of the CVM instance
        :type InstanceId: str
        """
        self.VpcId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceId = params.get("InstanceId")


class ConflictItem(AbstractModel):
    """Conflict resource items.

    """

    def __init__(self):
        """
        :param ConfilctId: Conflict resource ID
        :type ConfilctId: str
        :param DestinationItem: Conflict destination resource
        :type DestinationItem: str
        """
        self.ConfilctId = None
        self.DestinationItem = None


    def _deserialize(self, params):
        self.ConfilctId = params.get("ConfilctId")
        self.DestinationItem = params.get("DestinationItem")


class ConflictSource(AbstractModel):
    """Conflict resource.

    """

    def __init__(self):
        """
        :param ConflictSourceId: Conflict resource ID
        :type ConflictSourceId: str
        :param SourceItem: Conflict resource
        :type SourceItem: str
        :param ConflictItemSet: Conflict resource items
        :type ConflictItemSet: list of ConflictItem
        """
        self.ConflictSourceId = None
        self.SourceItem = None
        self.ConflictItemSet = None


    def _deserialize(self, params):
        self.ConflictSourceId = params.get("ConflictSourceId")
        self.SourceItem = params.get("SourceItem")
        if params.get("ConflictItemSet") is not None:
            self.ConflictItemSet = []
            for item in params.get("ConflictItemSet"):
                obj = ConflictItem()
                obj._deserialize(item)
                self.ConflictItemSet.append(obj)


class CreateAddressTemplateGroupRequest(AbstractModel):
    """CreateAddressTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: The name of the IP address template group.
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: The instance ID of the IP address template, such as `ipm-mdunqeb6`.
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class CreateAddressTemplateGroupResponse(AbstractModel):
    """CreateAddressTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroup: Group object of the IP address template.
        :type AddressTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddressTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplateGroup") is not None:
            self.AddressTemplateGroup = AddressTemplateGroup()
            self.AddressTemplateGroup._deserialize(params.get("AddressTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateAddressTemplateRequest(AbstractModel):
    """CreateAddressTemplate request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateName: The name of the IP address template
        :type AddressTemplateName: str
        :param Addresses: Address information, including IP, CIDR and IP address range.
        :type Addresses: list of str
        """
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate response structure.

    """

    def __init__(self):
        """
        :param AddressTemplate: The template object of the IP address.
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplate`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddressTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplate()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.RequestId = params.get("RequestId")


class CreateAndAttachNetworkInterfaceRequest(AbstractModel):
    """CreateAndAttachNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the `VpcId` field in the returned result of the `DescribeVpcs` API.
        :type VpcId: str
        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 bytes.
        :type NetworkInterfaceName: str
        :param SubnetId: The subnet instance ID of the ENI, such as 'subnet-0ap8nwca'.
        :type SubnetId: str
        :param InstanceId: CVM instance ID.
        :type InstanceId: str
        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 IPs each time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: The number of private IP addresses you can apply for. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: The security group to be bound with, such as ['sg-1dd51d'].
        :type SecurityGroupIds: list of str
        :param NetworkInterfaceDescription: The ENI description. You can enter any information within 60 characters.
        :type NetworkInterfaceDescription: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.InstanceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.NetworkInterfaceDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateAndAttachNetworkInterfaceResponse(AbstractModel):
    """CreateAndAttachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param NetworkInterface: The ENI instance.
        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateAssistantCidrRequest(AbstractModel):
    """CreateAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.
        :type VpcId: str
        :param CidrBlocks: CIDR set, e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type CidrBlocks: list of str
        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")


class CreateAssistantCidrResponse(AbstractModel):
    """CreateAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of secondary CIDR blocks.
Note: This field may return null, indicating that no valid value was found.
        :type AssistantCidrSet: list of AssistantCidr
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateBandwidthPackageRequest(AbstractModel):
    """CreateBandwidthPackage request structure.

    """

    def __init__(self):
        """
        :param NetworkType: The bandwidth package type. Valid values: 'BGP', 'SINGLEISP', and 'ANYCAST'.
        :type NetworkType: str
        :param ChargeType: The bandwidth package billing mode. Valid values: 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'.
        :type ChargeType: str
        :param BandwidthPackageName: The name of the bandwidth package.
        :type BandwidthPackageName: str
        :param BandwidthPackageCount: The number of bandwidth packages (It can only be “1” for bill-by-CVM accounts)
        :type BandwidthPackageCount: int
        :param InternetMaxBandwidth: The limit of the bandwidth package in Mbps. The value '-1' indicates there is no limit.
        :type InternetMaxBandwidth: int
        :param Tags: The list of tags to be bound.
        :type Tags: list of Tag
        :param Protocol: The protocol type of the bandwidth package. Valid values: 'ipv4' and 'ipv6'. Default value: 'ipv4'.
        :type Protocol: str
        """
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.BandwidthPackageCount = None
        self.InternetMaxBandwidth = None
        self.Tags = None
        self.Protocol = None


    def _deserialize(self, params):
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.BandwidthPackageCount = params.get("BandwidthPackageCount")
        self.InternetMaxBandwidth = params.get("InternetMaxBandwidth")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Protocol = params.get("Protocol")


class CreateBandwidthPackageResponse(AbstractModel):
    """CreateBandwidthPackage response structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package.
        :type BandwidthPackageId: str
        :param BandwidthPackageIds: The unique ID list of the bandwidth package (effective only when you apply for more than 1 bandwidth packages).
        :type BandwidthPackageIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        self.RequestId = params.get("RequestId")


class CreateCcnRequest(AbstractModel):
    """CreateCcn request structure.

    """

    def __init__(self):
        """
        :param CcnName: The name of the CCN. The maximum length is 60 characters.
        :type CcnName: str
        :param CcnDescription: The description of the CCN. The maximum length is 100 characters.
        :type CcnDescription: str
        :param QosLevel: CCN service quality, 'PT': Platinum, 'AU': Gold, 'AG': Silver. The default is 'AU'.
        :type QosLevel: str
        :param InstanceChargeType: The billing method. POSTPAID: postpaid by traffic. Default: POSTPAID.
        :type InstanceChargeType: str
        :param BandwidthLimitType: The bandwidth limit type. Valid values: OUTER_REGION_LIMIT: region outbound bandwidth limit; INTER_REGION_LIMIT: inter-region bandwidth limit. Default value: OUTER_REGION_LIMIT. Monthly-subscribed CCN instances only support inter-region bandwidth limit, while pay-as-you-go CCN instances support the both bandwidth limit types.
        :type BandwidthLimitType: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.CcnName = None
        self.CcnDescription = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.Tags = None


    def _deserialize(self, params):
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateCcnResponse(AbstractModel):
    """CreateCcn response structure.

    """

    def __init__(self):
        """
        :param Ccn: The CCN object.
        :type Ccn: :class:`tencentcloud.vpc.v20170312.models.CCN`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ccn = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ccn") is not None:
            self.Ccn = CCN()
            self.Ccn._deserialize(params.get("Ccn"))
        self.RequestId = params.get("RequestId")


class CreateCustomerGatewayRequest(AbstractModel):
    """CreateCustomerGateway request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayName: Customer gateway can be named freely, but the maximum length is 60 characters.
        :type CustomerGatewayName: str
        :param IpAddress: Customer gateway public IP.
        :type IpAddress: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.Tags = None


    def _deserialize(self, params):
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway response structure.

    """

    def __init__(self):
        """
        :param CustomerGateway: Customer gateway object
        :type CustomerGateway: :class:`tencentcloud.vpc.v20170312.models.CustomerGateway`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CustomerGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGateway") is not None:
            self.CustomerGateway = CustomerGateway()
            self.CustomerGateway._deserialize(params.get("CustomerGateway"))
        self.RequestId = params.get("RequestId")


class CreateDefaultVpcRequest(AbstractModel):
    """CreateDefaultVpc request structure.

    """

    def __init__(self):
        """
        :param Zone: The ID of the availability zone in which the subnet resides. The availability zone will be randomly selected if not specified.
        :type Zone: str
        :param Force: Whether to forcibly return a default VPC
        :type Force: bool
        """
        self.Zone = None
        self.Force = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Force = params.get("Force")


class CreateDefaultVpcResponse(AbstractModel):
    """CreateDefaultVpc response structure.

    """

    def __init__(self):
        """
        :param Vpc: Default VPC and subnet IDs
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.DefaultVpcSubnet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = DefaultVpcSubnet()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`
        :type DirectConnectGatewayId: str
        :param Routes: The list of IDC IP range that must be connected
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class CreateDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayName: The name of the direct connect gateway.
        :type DirectConnectGatewayName: str
        :param NetworkType: The type of the associated network. Valid values:
<li>VPC</li>
<li>CCN</li>
        :type NetworkType: str
        :param NetworkInstanceId: <li>When the NetworkType is VPC, this value is the VPC instance ID</li>
<li>When the NetworkType is CCN, this value is the CCN instance ID</li>
        :type NetworkInstanceId: str
        :param GatewayType: The type of the gateway. Valid values:
<li>NORMAL - (Default) Standard type. Note: CCN only supports the standard type</li>
<li>NAT - NAT type</li>NAT gateway supports network address translation. The specified type cannot be modified. A VPC can create one NAT direct connect gateway and one non-NAT direct connect gateway
        :type GatewayType: str
        :param ModeType: CCN route publishing method. Valid values: `standard` and `exquisite`. This parameter is only valid for the CCN direct connect gateway.
        :type ModeType: str
        """
        self.DirectConnectGatewayName = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.ModeType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.ModeType = params.get("ModeType")


class CreateDirectConnectGatewayResponse(AbstractModel):
    """CreateDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param DirectConnectGateway: The object of the direct connect gateway.
        :type DirectConnectGateway: :class:`tencentcloud.vpc.v20170312.models.DirectConnectGateway`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DirectConnectGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectGateway") is not None:
            self.DirectConnectGateway = DirectConnectGateway()
            self.DirectConnectGateway._deserialize(params.get("DirectConnectGateway"))
        self.RequestId = params.get("RequestId")


class CreateFlowLogRequest(AbstractModel):
    """CreateFlowLog request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogName: The name of the flow log instance.
        :type FlowLogName: str
        :param ResourceType: The type of resources to which the flow log belongs. Valid values: 'VPC', 'SUBNET' and 'NETWORKINTERFACE'.
        :type ResourceType: str
        :param ResourceId: The unique ID of the resource.
        :type ResourceId: str
        :param TrafficType: Type of the flow logs to be collected. Valid values: `ACCEPT`, `REJECT` and `ALL`.
        :type TrafficType: str
        :param CloudLogId: The storage ID of the flow log.
        :type CloudLogId: str
        :param FlowLogDescription: The description of the flow log instance
        :type FlowLogDescription: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.FlowLogDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.FlowLogDescription = params.get("FlowLogDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateFlowLogResponse(AbstractModel):
    """CreateFlowLog response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The information of the flow log created.
        :type FlowLog: list of FlowLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the VPC to which the `HAVIP` belongs.
        :type VpcId: str
        :param SubnetId: The `ID` of the subnet to which the `HAVIP` belongs.
        :type SubnetId: str
        :param HaVipName: The name of the `HAVIP`.
        :type HaVipName: str
        :param Vip: The specified virtual IP address, which must be within the IP range of the `VPC` and not in use. It will be automatically assigned if not specified.
        :type Vip: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.HaVipName = None
        self.Vip = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip response structure.

    """

    def __init__(self):
        """
        :param HaVip: `HAVIP` object.
        :type HaVip: :class:`tencentcloud.vpc.v20170312.models.HaVip`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HaVip = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self.HaVip = HaVip()
            self.HaVip._deserialize(params.get("HaVip"))
        self.RequestId = params.get("RequestId")


class CreateNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param DestinationIpPortTranslationNatRules: The port forwarding rules of the NAT gateway.
        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule
        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)


class CreateNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway request structure.

    """

    def __init__(self):
        """
        :param NatGatewayName: NAT gateway name
        :type NatGatewayName: str
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the NAT gateway (unit: Mbps). Supported parameter values: `20, 50, 100, 200, 500, 1000, 2000, 5000`. Default: `100Mbps`.
        :type InternetMaxBandwidthOut: int
        :param MaxConcurrentConnection: The concurrent connection cap of the NAT gateway. Supported parameter values: `1000000, 3000000, 10000000`. The default value is `100000`.
        :type MaxConcurrentConnection: int
        :param AddressCount: The number of EIPs that needs to be applied for. The system will create N number of EIPs according to your requirements. Either AddressCount or PublicAddresses must be passed in.
        :type AddressCount: int
        :param PublicIpAddresses: The EIP array bound to the NAT gateway. Either AddressCount or PublicAddresses must be passed in.
        :type PublicIpAddresses: list of str
        :param Zone: The availability zone, such as `ap-guangzhou-1`.
        :type Zone: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        :param SubnetId: Subnet of the NAT gateway
        :type SubnetId: str
        """
        self.NatGatewayName = None
        self.VpcId = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None
        self.Tags = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.NatGatewayName = params.get("NatGatewayName")
        self.VpcId = params.get("VpcId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SubnetId = params.get("SubnetId")


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway response structure.

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT gateway object array.
        :type NatGatewaySet: list of NatGateway
        :param TotalCount: The number of NAT gateway objects meeting the conditions.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateNetDetectRequest(AbstractModel):
    """CreateNetDetect request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of a `VPC` instance, such as `vpc-12345678`.
        :type VpcId: str
        :param SubnetId: The ID of a subnet instance, such as subnet-12345678.
        :type SubnetId: str
        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.
        :type NetDetectName: str
        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.
        :type DetectDestinationIp: list of str
        :param NextHopType: The type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.
        :type NextHopType: str
        :param NextHopDestination: The next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.
        :type NextHopDestination: str
        :param NetDetectDescription: Network detection description.
        :type NetDetectDescription: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")


class CreateNetDetectResponse(AbstractModel):
    """CreateNetDetect response structure.

    """

    def __init__(self):
        """
        :param NetDetect: The network detection (NetDetect) object.
        :type NetDetect: :class:`tencentcloud.vpc.v20170312.models.NetDetect`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetDetect = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetect") is not None:
            self.NetDetect = NetDetect()
            self.NetDetect._deserialize(params.get("NetDetect"))
        self.RequestId = params.get("RequestId")


class CreateNetworkAclRequest(AbstractModel):
    """CreateNetworkAcl request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of the DescribeVpcs API.
        :type VpcId: str
        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.
        :type NetworkAclName: str
        """
        self.VpcId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclName = params.get("NetworkAclName")


class CreateNetworkAclResponse(AbstractModel):
    """CreateNetworkAcl response structure.

    """

    def __init__(self):
        """
        :param NetworkAcl: Network ACL instance
        :type NetworkAcl: :class:`tencentcloud.vpc.v20170312.models.NetworkAcl`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkAcl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAcl") is not None:
            self.NetworkAcl = NetworkAcl()
            self.NetworkAcl._deserialize(params.get("NetworkAcl"))
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 characters.
        :type NetworkInterfaceName: str
        :param SubnetId: The subnet instance ID of the ENI, such as `subnet-0ap8nwca`.
        :type SubnetId: str
        :param NetworkInterfaceDescription: ENI description can be named freely, but the maximum length is 60 characters.
        :type NetworkInterfaceDescription: str
        :param SecondaryPrivateIpAddressCount: The number of private IP addresses that is newly applied for. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: Specifies the security group to be bound with, such as ['sg-1dd51d'].
        :type SecurityGroupIds: list of str
        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 each time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param NetworkInterface: ENI instance.
        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateRouteTableRequest(AbstractModel):
    """CreateRouteTable request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param RouteTableName: The route table name. The maximum length is 60 characters.
        :type RouteTableName: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.RouteTableName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable response structure.

    """

    def __init__(self):
        """
        :param RouteTable: Route table object.
        :type RouteTable: :class:`tencentcloud.vpc.v20170312.models.RouteTable`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RouteTable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteTable") is not None:
            self.RouteTable = RouteTable()
            self.RouteTable._deserialize(params.get("RouteTable"))
        self.RequestId = params.get("RequestId")


class CreateRoutesRequest(AbstractModel):
    """CreateRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: Route table instance ID.
        :type RouteTableId: str
        :param Routes: Routing policy object.
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of newly added instances.
        :type TotalCount: int
        :param RouteTableSet: Route table object.
        :type RouteTableSet: list of RouteTable
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.
        :type GroupName: str
        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.
        :type GroupDescription: str
        :param ProjectId: Project ID. The default is 0. You can query it on the project management page of the Qcloud console.
        :type ProjectId: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group object.
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupWithPoliciesRequest(AbstractModel):
    """CreateSecurityGroupWithPolicies request structure.

    """

    def __init__(self):
        """
        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.
        :type GroupName: str
        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.
        :type GroupDescription: str
        :param ProjectId: The project id is 0 by default. You can query this in the project management page of the Qcloud console.
        :type ProjectId: str
        :param SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class CreateSecurityGroupWithPoliciesResponse(AbstractModel):
    """CreateSecurityGroupWithPolicies response structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group object.
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateGroupRequest(AbstractModel):
    """CreateServiceTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupName: Group name of the protocol port template.
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: Instance ID of the protocol port template, such as `ppm-4dw6agho`.
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class CreateServiceTemplateGroupResponse(AbstractModel):
    """CreateServiceTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroup: Group object of the protocol port template.
        :type ServiceTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplateGroup") is not None:
            self.ServiceTemplateGroup = ServiceTemplateGroup()
            self.ServiceTemplateGroup._deserialize(params.get("ServiceTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateRequest(AbstractModel):
    """CreateServiceTemplate request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateName: Template name of the protocol port
        :type ServiceTemplateName: str
        :param Services: It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE.
        :type Services: list of str
        """
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class CreateServiceTemplateResponse(AbstractModel):
    """CreateServiceTemplate response structure.

    """

    def __init__(self):
        """
        :param ServiceTemplate: Protocol port template object.
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplate`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplate()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param SubnetName: The subnet name. The maximum length is 60 bytes.
        :type SubnetName: str
        :param CidrBlock: The subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC.
        :type CidrBlock: str
        :param Zone: The ID of the availability zone in which the subnet resides. You can set up disaster recovery across availability zones by choosing different availability zones for different subnets.
        :type Zone: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet response structure.

    """

    def __init__(self):
        """
        :param Subnet: Subnet object.
        :type Subnet: :class:`tencentcloud.vpc.v20170312.models.Subnet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Subnet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self.Subnet = Subnet()
            self.Subnet._deserialize(params.get("Subnet"))
        self.RequestId = params.get("RequestId")


class CreateSubnetsRequest(AbstractModel):
    """CreateSubnets request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC` instance, such as `vpc-6v2ht8q5`.
        :type VpcId: str
        :param Subnets: The subnet object list.
        :type Subnets: list of SubnetInput
        :param Tags: Bound tags. Note that the collection of tags here is shared by all subnet objects in the list. You cannot specify tags for each subnet. Example: [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.Subnets = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = SubnetInput()
                obj._deserialize(item)
                self.Subnets.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSubnetsResponse(AbstractModel):
    """CreateSubnets response structure.

    """

    def __init__(self):
        """
        :param SubnetSet: The list of newly created subnets.
        :type SubnetSet: list of Subnet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc request structure.

    """

    def __init__(self):
        """
        :param VpcName: The VPC name. The maximum length is 60 bytes.
        :type VpcName: str
        :param CidrBlock: VPC CIDR, which must fall within the following private network IP ranges: 10.0.0.0/16, 172.16.0.0/16, and 192.168.0.0/16.
        :type CidrBlock: str
        :param EnableMulticast: Whether multicast is enabled. `true`: Enabled. `false`: Not enabled.
        :type EnableMulticast: str
        :param DnsServers: The DNS address. A maximum of 4 addresses is supported.
        :type DnsServers: list of str
        :param DomainName: Domain name
        :type DomainName: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcName = None
        self.CidrBlock = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateVpcResponse(AbstractModel):
    """CreateVpc response structure.

    """

    def __init__(self):
        """
        :param Vpc: The VPC object.
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.Vpc`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = Vpc()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateVpnConnectionRequest(AbstractModel):
    """CreateVpnConnection request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.
        :type CustomerGatewayId: str
        :param VpnConnectionName: Gateway can be named freely, but the maximum length is 60 characters.
        :type VpnConnectionName: str
        :param PreShareKey: The pre-shared key.
        :type PreShareKey: str
        :param SecurityPolicyDatabases: The SPD policy group, for example: {"10.0.0.5/24":["172.123.10.5/16"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC.
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user.
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self.SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateVpnConnectionResponse(AbstractModel):
    """CreateVpnConnection response structure.

    """

    def __init__(self):
        """
        :param VpnConnection: Tunnel instance object.
        :type VpnConnection: :class:`tencentcloud.vpc.v20170312.models.VpnConnection`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VpnConnection = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnConnection") is not None:
            self.VpnConnection = VpnConnection()
            self.VpnConnection._deserialize(params.get("VpnConnection"))
        self.RequestId = params.get("RequestId")


class CreateVpnGatewayRequest(AbstractModel):
    """CreateVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param VpnGatewayName: The VPN gateway name. The maximum length is 60 bytes.
        :type VpnGatewayName: str
        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        :param Zone: The availability zone, such as `ap-guangzhou-2`.
        :type Zone: str
        :param Type: VPN gateway type. Value: `CCN`, indicates CCN-type VPN gateway
        :type Type: str
        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.VpnGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Zone = None
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateVpnGatewayResponse(AbstractModel):
    """CreateVpnGateway response structure.

    """

    def __init__(self):
        """
        :param VpnGateway: VPN gateway object.
        :type VpnGateway: :class:`tencentcloud.vpc.v20170312.models.VpnGateway`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VpnGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnGateway") is not None:
            self.VpnGateway = VpnGateway()
            self.VpnGateway._deserialize(params.get("VpnGateway"))
        self.RequestId = params.get("RequestId")


class CrossBorderCompliance(AbstractModel):
    """Compliance review request

    """

    def __init__(self):
        """
        :param ServiceProvider: Service provider. Valid values: `UNICOM`.
        :type ServiceProvider: str
        :param ComplianceId: ID of compliance review request.
        :type ComplianceId: int
        :param Company: Full company name.
        :type Company: str
        :param UniformSocialCreditCode: Unified Social Credit Code.
        :type UniformSocialCreditCode: str
        :param LegalPerson: Legal person.
        :type LegalPerson: str
        :param IssuingAuthority: Issuing authority.
        :type IssuingAuthority: str
        :param BusinessLicense: Business license.
        :type BusinessLicense: str
        :param BusinessAddress: Business address.
        :type BusinessAddress: str
        :param PostCode: Zip code.
        :type PostCode: int
        :param Manager: Operator.
        :type Manager: str
        :param ManagerId: Operator ID card number.
        :type ManagerId: str
        :param ManagerIdCard: Operator ID card.
        :type ManagerIdCard: str
        :param ManagerAddress: Operator address.
        :type ManagerAddress: str
        :param ManagerTelephone: Operator phone number.
        :type ManagerTelephone: str
        :param Email: Email.
        :type Email: str
        :param ServiceHandlingForm: Service handling form.
        :type ServiceHandlingForm: str
        :param AuthorizationLetter: Authorization letter.
        :type AuthorizationLetter: str
        :param SafetyCommitment: Information security commitment.
        :type SafetyCommitment: str
        :param ServiceStartDate: Service start date.
        :type ServiceStartDate: str
        :param ServiceEndDate: Service end date.
        :type ServiceEndDate: str
        :param State: Status. Valid values: `PENDING`, `APPROVED`, and `DENY`.
        :type State: str
        :param CreatedTime: Creation time of the review form.
        :type CreatedTime: str
        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.Company = None
        self.UniformSocialCreditCode = None
        self.LegalPerson = None
        self.IssuingAuthority = None
        self.BusinessLicense = None
        self.BusinessAddress = None
        self.PostCode = None
        self.Manager = None
        self.ManagerId = None
        self.ManagerIdCard = None
        self.ManagerAddress = None
        self.ManagerTelephone = None
        self.Email = None
        self.ServiceHandlingForm = None
        self.AuthorizationLetter = None
        self.SafetyCommitment = None
        self.ServiceStartDate = None
        self.ServiceEndDate = None
        self.State = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.Company = params.get("Company")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.LegalPerson = params.get("LegalPerson")
        self.IssuingAuthority = params.get("IssuingAuthority")
        self.BusinessLicense = params.get("BusinessLicense")
        self.BusinessAddress = params.get("BusinessAddress")
        self.PostCode = params.get("PostCode")
        self.Manager = params.get("Manager")
        self.ManagerId = params.get("ManagerId")
        self.ManagerIdCard = params.get("ManagerIdCard")
        self.ManagerAddress = params.get("ManagerAddress")
        self.ManagerTelephone = params.get("ManagerTelephone")
        self.Email = params.get("Email")
        self.ServiceHandlingForm = params.get("ServiceHandlingForm")
        self.AuthorizationLetter = params.get("AuthorizationLetter")
        self.SafetyCommitment = params.get("SafetyCommitment")
        self.ServiceStartDate = params.get("ServiceStartDate")
        self.ServiceEndDate = params.get("ServiceEndDate")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")


class CustomerGateway(AbstractModel):
    """Customer Gateway

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The unique ID of the customer gateway
        :type CustomerGatewayId: str
        :param CustomerGatewayName: Gateway Name
        :type CustomerGatewayName: str
        :param IpAddress: Public network address
        :type IpAddress: str
        :param CreatedTime: The creation time.
        :type CreatedTime: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreatedTime = params.get("CreatedTime")


class CustomerGatewayVendor(AbstractModel):
    """Customer gateway vendor information object.

    """

    def __init__(self):
        """
        :param Platform: Platform.
        :type Platform: str
        :param SoftwareVersion: Software version.
        :type SoftwareVersion: str
        :param VendorName: Vendor name.
        :type VendorName: str
        """
        self.Platform = None
        self.SoftwareVersion = None
        self.VendorName = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.SoftwareVersion = params.get("SoftwareVersion")
        self.VendorName = params.get("VendorName")


class CvmInstance(AbstractModel):
    """A CVM instance.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param SubnetId: Subnet instance ID.
        :type SubnetId: str
        :param InstanceId: CVM instance ID.
        :type InstanceId: str
        :param InstanceName: CVM Name
        :type InstanceName: str
        :param InstanceState: CVM status.
        :type InstanceState: str
        :param CPU: Number of CPU cores in an instance (in core).
        :type CPU: int
        :param Memory: Instance’s memory capacity. Unit: GB.
        :type Memory: int
        :param CreatedTime: The creation time.
        :type CreatedTime: str
        :param InstanceType: Instance type.
        :type InstanceType: str
        :param EniLimit: Instance ENI quota (including primary ENIs).
        :type EniLimit: int
        :param EniIpLimit: Private IP quoata for instance ENIs (including primary ENIs).
        :type EniIpLimit: int
        :param InstanceEniCount: The number of ENIs (including primary ENIs) bound to a instance.
        :type InstanceEniCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.CPU = None
        self.Memory = None
        self.CreatedTime = None
        self.InstanceType = None
        self.EniLimit = None
        self.EniIpLimit = None
        self.InstanceEniCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceType = params.get("InstanceType")
        self.EniLimit = params.get("EniLimit")
        self.EniIpLimit = params.get("EniIpLimit")
        self.InstanceEniCount = params.get("InstanceEniCount")


class DefaultVpcSubnet(AbstractModel):
    """Default VPC and subnet

    """

    def __init__(self):
        """
        :param VpcId: Default VpcId
        :type VpcId: str
        :param SubnetId: Default SubnetId
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteAddressTemplateGroupRequest(AbstractModel):
    """DeleteAddressTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: The IP address template group instance ID, such as `ipmg-90cex8mq`.
        :type AddressTemplateGroupId: str
        """
        self.AddressTemplateGroupId = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")


class DeleteAddressTemplateGroupResponse(AbstractModel):
    """DeleteAddressTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateId: The IP address template instance ID, such as `ipm-09o5m8kc`.
        :type AddressTemplateId: str
        """
        self.AddressTemplateId = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAssistantCidrRequest(AbstractModel):
    """DeleteAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.
        :type VpcId: str
        :param CidrBlocks: CIDR set, e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type CidrBlocks: list of str
        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")


class DeleteAssistantCidrResponse(AbstractModel):
    """DeleteAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBandwidthPackageRequest(AbstractModel):
    """DeleteBandwidthPackage request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package to be deleted.
        :type BandwidthPackageId: str
        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class DeleteBandwidthPackageResponse(AbstractModel):
    """DeleteBandwidthPackage response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcnRequest(AbstractModel):
    """DeleteCcn request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")


class DeleteCcnResponse(AbstractModel):
    """DeleteCcn response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.
        :type CustomerGatewayId: str
        """
        self.CustomerGatewayId = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`
        :type DirectConnectGatewayId: str
        :param RouteIds: The route ID, such as `ccnr-f49l6u0z`.
        :type RouteIds: list of str
        """
        self.DirectConnectGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteIds = params.get("RouteIds")


class DeleteDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The unique `ID` of the direct connect gateway, such as `dcg-9o233uri`.
        :type DirectConnectGatewayId: str
        """
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class DeleteDirectConnectGatewayResponse(AbstractModel):
    """DeleteDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFlowLogRequest(AbstractModel):
    """DeleteFlowLog request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogId: The unique ID of the flow log.
        :type FlowLogId: str
        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")


class DeleteFlowLogResponse(AbstractModel):
    """DeleteFlowLog response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param DestinationIpPortTranslationNatRules: The port forwarding rules of the NAT gateway.
        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule
        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)


class DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        """
        self.NatGatewayId = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetDetectRequest(AbstractModel):
    """DeleteNetDetect request structure.

    """

    def __init__(self):
        """
        :param NetDetectId: The `ID` of a network detection instance, such as `netd-12345678`.
        :type NetDetectId: str
        """
        self.NetDetectId = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")


class DeleteNetDetectResponse(AbstractModel):
    """DeleteNetDetect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkAclRequest(AbstractModel):
    """DeleteNetworkAcl request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.
        :type NetworkAclId: str
        """
        self.NetworkAclId = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")


class DeleteNetworkAclResponse(AbstractModel):
    """DeleteNetworkAcl response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        """
        self.NetworkInterfaceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        """
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: Route table instance ID.
        :type RouteTableId: str
        :param Routes: Routing policy object.
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: The policy set of the security group. One request can only delete one or more policies in one direction. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. Each request can use only one matching method.
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateGroupRequest(AbstractModel):
    """DeleteServiceTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: The protocol port template group instance ID, such as `ppmg-n17uxvve`.
        :type ServiceTemplateGroupId: str
        """
        self.ServiceTemplateGroupId = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")


class DeleteServiceTemplateGroupResponse(AbstractModel):
    """DeleteServiceTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateRequest(AbstractModel):
    """DeleteServiceTemplate request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port template instance ID, such as `ppm-e6dy460g`.
        :type ServiceTemplateId: str
        """
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")


class DeleteServiceTemplateResponse(AbstractModel):
    """DeleteServiceTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet request structure.

    """

    def __init__(self):
        """
        :param SubnetId: The ID of the subnet instance. You can obtain the parameter value from the SubnetId field in the returned result of DescribeSubnets API.
        :type SubnetId: str
        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        """
        self.VpnGatewayId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountAttributesRequest(AbstractModel):
    """DescribeAccountAttributes request structure.

    """


class DescribeAccountAttributesResponse(AbstractModel):
    """DescribeAccountAttributes response structure.

    """

    def __init__(self):
        """
        :param AccountAttributeSet: User account attribute object
        :type AccountAttributeSet: list of AccountAttribute
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountAttributeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountAttributeSet") is not None:
            self.AccountAttributeSet = []
            for item in params.get("AccountAttributeSet"):
                obj = AccountAttribute()
                obj._deserialize(item)
                self.AccountAttributeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota request structure.

    """


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota response structure.

    """

    def __init__(self):
        """
        :param QuotaSet: The quota information of EIPs in an account.
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


class DescribeAddressTemplateGroupsRequest(AbstractModel):
    """DescribeAddressTemplateGroups request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions.
<li>address-template-group-name - String - (Filter condition) IP address template group name.</li>
<li>address-template-group-id - String - (Filter condition) IP address template group instance ID, such as `ipmg-mdunqeb6`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: str
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressTemplateGroupsResponse(AbstractModel):
    """DescribeAddressTemplateGroups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param AddressTemplateGroupSet: IP address template.
        :type AddressTemplateGroupSet: list of AddressTemplateGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateGroupSet") is not None:
            self.AddressTemplateGroupSet = []
            for item in params.get("AddressTemplateGroupSet"):
                obj = AddressTemplateGroup()
                obj._deserialize(item)
                self.AddressTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressTemplatesRequest(AbstractModel):
    """DescribeAddressTemplates request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions.
<li>address-template-name - String - (Filter condition) IP address template name.</li>
<li>address-template-id - String - (Filter condition) IP address template instance ID, such as `ipm-mdunqeb6`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: str
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressTemplatesResponse(AbstractModel):
    """DescribeAddressTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param AddressTemplateSet: IP address template.
        :type AddressTemplateSet: list of AddressTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplate()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses request structure.

    """

    def __init__(self):
        """
        :param AddressIds: The list of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time.
        :type AddressIds: list of str
        :param Filters: The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. Detailed filter conditions are as follows:
<li> address-id - String - Required: no - (Filter condition) The unique EIP ID, such as `eip-11112222`.</li>
<li> address-name - String - Required: no - (Filter condition) The EIP name. Fuzzy filtering is not supported.</li>
<li> address-ip - String - Required: no - (Filter condition) Filters by EIP.</li>
<li> address-status - String - Required: no - (Filter condition) The EIP state. Possible EIP states are: 'CREATING', 'BINDING', 'BIND', 'UNBINDING', 'UNBIND', 'OFFLINING', and 'BIND_ENI'.</li>
<li> instance-id - String - Required: no - (Filter condition) The ID of the instance bound to the EIP, such as `ins-11112222`.</li>
<li> private-ip-address - String - Required: no - (Filter condition) The private IP address bound to the EIP.</li>
<li> network-interface-id - String - Required: no - (Filter condition) The ID of the ENI bound to the EIP, such as `eni-11112222`.</li>
<li> is-arrears - String - Required: no - (Filter condition) Whether the EIP is in arrears. (TRUE: the EIP is in arrears | FALSE: the billing status of the EIP is normal)</li>
        :type Filters: list of Filter
        :param Offset: The Offset. The default value is 0. For more information on `Offset`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646).
        :type Offset: int
        :param Limit: Number of returned results. The default value is 20. The maximum is 100. For more information on `Limit`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646).
        :type Limit: int
        """
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of EIPs meeting the condition.
        :type TotalCount: int
        :param AddressSet: List of EIPs details.
        :type AddressSet: list of Address
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressSet") is not None:
            self.AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self.AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssistantCidrRequest(AbstractModel):
    """DescribeAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcIds: The ID of a VPC instance set, such as `vpc-6v2ht8q5`.
        :type VpcIds: list of str
        :param Filters: Filter condition. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAssistantCidrResponse(AbstractModel):
    """DescribeAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of eligible secondary CIDR blocks
Note: This field may return null, indicating that no valid value was found.
        :type AssistantCidrSet: list of AssistantCidr
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackageBillUsageRequest(AbstractModel):
    """DescribeBandwidthPackageBillUsage request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: Unique ID of the pay-as-you-go bandwidth package.
        :type BandwidthPackageId: str
        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class DescribeBandwidthPackageBillUsageResponse(AbstractModel):
    """DescribeBandwidthPackageBillUsage response structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageBillBandwidthSet: Current billable usage.
        :type BandwidthPackageBillBandwidthSet: list of BandwidthPackageBillBandwidth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BandwidthPackageBillBandwidthSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BandwidthPackageBillBandwidthSet") is not None:
            self.BandwidthPackageBillBandwidthSet = []
            for item in params.get("BandwidthPackageBillBandwidthSet"):
                obj = BandwidthPackageBillBandwidth()
                obj._deserialize(item)
                self.BandwidthPackageBillBandwidthSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackageQuotaRequest(AbstractModel):
    """DescribeBandwidthPackageQuota request structure.

    """


class DescribeBandwidthPackageQuotaResponse(AbstractModel):
    """DescribeBandwidthPackageQuota response structure.

    """

    def __init__(self):
        """
        :param QuotaSet: The quota of the bandwidth package.
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


class DescribeBandwidthPackageResourcesRequest(AbstractModel):
    """DescribeBandwidthPackageResources request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: Unique ID of the bandwidth package in the form of `bwp-11112222`.
        :type BandwidthPackageId: str
        :param Filters: Each request can have up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:
<li>resource-id - String - Required: no -  (Filter condition) Filters by the unique ID of resources in a bandwidth package, such as `eip-11112222`.</li>
<li>resource-type - String - Required: no - (Filter condition) Filters by the type of resources in a bandwidth package. It now supports only EIP (`Address`) and load balancer (`LoadBalance`).</li>
        :type Filters: list of Filter
        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).
        :type Limit: int
        """
        self.BandwidthPackageId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBandwidthPackageResourcesResponse(AbstractModel):
    """DescribeBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible resources in the bandwidth package.
        :type TotalCount: int
        :param ResourceSet: The list of resources in the bandwidth package.
        :type ResourceSet: list of Resource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackagesRequest(AbstractModel):
    """DescribeBandwidthPackages request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageIds: The unique ID list of bandwidth packages.
        :type BandwidthPackageIds: list of str
        :param Filters: Each request can have up to 10 `Filters`. `BandwidthPackageIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:
<li> bandwidth-package_id - String - Required: No - (Filter condition) Filter by the unique ID of the bandwidth package.</li>
<li> bandwidth-package-name - String - Required: No - (Filter condition) Filter by the bandwidth package name. Fuzzy filtering is not supported.</li>
<li> network-type - String - Required: No - (Filter condition) Filter by the bandwidth package type. Types include 'BGP', 'SINGLEISP', and 'ANYCAST'.</li>
<li> charge-type - String - Required: No - (Filter condition) Filter by the bandwidth package billing mode. Billing modes include 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'.</li>
<li> resource.resource-type - String - Required: No - (Filter condition) Filter by the bandwidth package resource type. Resource types include 'Address' and 'LoadBalance'.</li>
<li> resource.resource-id - String - Required: No - (Filter condition) Filter by the bandwidth package resource ID, such as 'eip-xxxx' and 'lb-xxxx'.</li>
<li> resource.address-ip - String - Required: No - (Filter condition) Filter by the bandwidth package resource IP.</li>
        :type Filters: list of Filter
        :param Offset: Offset of the query results
        :type Offset: int
        :param Limit: Max number of the bandwidth packages to be returned.
        :type Limit: int
        """
        self.BandwidthPackageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBandwidthPackagesResponse(AbstractModel):
    """DescribeBandwidthPackages response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible bandwidth packages.
        :type TotalCount: int
        :param BandwidthPackageSet: Detail information of the bandwidth package.
        :type BandwidthPackageSet: list of BandwidthPackage
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.BandwidthPackageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BandwidthPackageSet") is not None:
            self.BandwidthPackageSet = []
            for item in params.get("BandwidthPackageSet"):
                obj = BandwidthPackage()
                obj._deserialize(item)
                self.BandwidthPackageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    """DescribeCcnAttachedInstances request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset
        :type Offset: int
        :param Limit: The returned quantity
        :type Limit: int
        :param Filters: Filter conditions:
<li>ccn-id - String - (Filter condition) The CCN instance ID.</li>
<li>instance-type - String - (Filter condition) The associated instance type.</li>
<li>instance-region - String - (Filter condition) The associated instance region.</li>
<li>instance-type - String - (Filter condition) The instance ID of the associated instance.</li>
        :type Filters: list of Filter
        :param CcnId: The ID of the CCN instance
        :type CcnId: str
        :param OrderField: The order field supports `CcnId`, `InstanceType`, `InstanceId`, `InstanceName`, `InstanceRegion`, `AttachedTime`, and `State`.
        :type OrderField: str
        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.
        :type OrderDirection: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.CcnId = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.CcnId = params.get("CcnId")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param InstanceSet: The list of associated instances.
        :type InstanceSet: list of CcnAttachedInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRoutesRequest(AbstractModel):
    """DescribeCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-gree226l`.
        :type CcnId: str
        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.
        :type RouteIds: list of str
        :param Filters: Filter condition. `RouteIds` and `Filters` cannot be specified at the same time.
<li>route-id - String - (Filter condition) Routing policy ID.</li>
<li>cidr-block - String - (Filter condition) Destination port.</li>
<li>instance-type - String - (Filter condition) The next hop type.</li>
<li>instance-region - String - (Filter condition) The next hop region.</li>
<li>instance-type - String - (Filter condition) The instance ID of the next hop.</li>
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: The returned quantity
        :type Limit: int
        """
        self.CcnId = None
        self.RouteIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCcnRoutesResponse(AbstractModel):
    """DescribeCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param RouteSet: The CCN routing policy object.
        :type RouteSet: list of CcnRoute
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = CcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnsRequest(AbstractModel):
    """DescribeCcns request structure.

    """

    def __init__(self):
        """
        :param CcnIds: The CCN instance ID, such as `ccn-f49l6u0z`. Each request can have a maximum of 100 instances. `CcnIds` and `Filters` cannot be specified at the same time
        :type CcnIds: list of str
        :param Filters: Filter conditions. `CcnIds` and `Filters` cannot be specified at the same time.
<li>ccn-id - String - (Filter condition) The unique ID of the CCN, such as `vpc-f49l6u0z`.</li>
<li>ccn-name - String - (Filter condition) The CCN name.</li>
<li>ccn-description - String - (Filter condition) CCN description.</li>
<li>state - String - (Filter condition) The instance status. 'ISOLATED': Isolated (the account is in arrears and the service is suspended.) 'AVAILABLE': Running.</li>
<li>tag-key - String - Required: no - (Filter condition) Filters by tag key.</li>
<li>`tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see this example: **Querying the list of CCNs bound to tags**.</li>
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: The returned quantity
        :type Limit: int
        :param OrderField: Order fields support `CcnId`, `CcnName`, `CreateTime`, `State`, and `QosLevel`
        :type OrderField: str
        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.
        :type OrderDirection: str
        """
        self.CcnIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.CcnIds = params.get("CcnIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeCcnsResponse(AbstractModel):
    """DescribeCcns response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param CcnSet: CCN object.
        :type CcnSet: list of CCN
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.CcnSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CcnSet") is not None:
            self.CcnSet = []
            for item in params.get("CcnSet"):
                obj = CCN()
                obj._deserialize(item)
                self.CcnSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicLinkInstancesRequest(AbstractModel):
    """DescribeClassicLinkInstances request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions.
<li>vpc-id - String - (Filter condition) The VPC instance ID.</li>
<li>vm-ip - String - (Filter condition) The IP address of the CVM on the basic network.</li>
        :type Filters: list of FilterObject
        :param Offset: Offset
        :type Offset: str
        :param Limit: The returned quantity
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClassicLinkInstancesResponse(AbstractModel):
    """DescribeClassicLinkInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param ClassicLinkInstanceSet: Classiclink instance.
        :type ClassicLinkInstanceSet: list of ClassicLinkInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClassicLinkInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClassicLinkInstanceSet") is not None:
            self.ClassicLinkInstanceSet = []
            for item in params.get("ClassicLinkInstanceSet"):
                obj = ClassicLinkInstance()
                obj._deserialize(item)
                self.ClassicLinkInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCrossBorderComplianceRequest(AbstractModel):
    """DescribeCrossBorderCompliance request structure.

    """

    def __init__(self):
        """
        :param ServiceProvider: (Exact match) Service provider. Valid values: `UNICOM`.
        :type ServiceProvider: str
        :param ComplianceId: (Exact match) ID of compliance review request.
        :type ComplianceId: int
        :param Company: (Fuzzy match) Company name.
        :type Company: str
        :param UniformSocialCreditCode: (Fuzzy match) Unified Social Credit Code.
        :type UniformSocialCreditCode: str
        :param LegalPerson: (Fuzzy match) Legal person.
        :type LegalPerson: str
        :param IssuingAuthority: (Fuzzy match) Issuing authority.
        :type IssuingAuthority: str
        :param BusinessAddress: (Fuzzy match) Business address.
        :type BusinessAddress: str
        :param PostCode: (Exact match) Zip code.
        :type PostCode: int
        :param Manager: (Fuzzy match) Operator.
        :type Manager: str
        :param ManagerId: (Exact match) Operator ID card number.
        :type ManagerId: str
        :param ManagerAddress: (Fuzzy match) Operator address.
        :type ManagerAddress: str
        :param ManagerTelephone: (Exact match) Operator phone number.
        :type ManagerTelephone: str
        :param Email: (Exact match) Email.
        :type Email: str
        :param ServiceStartDate: (Exact match) Service start date, such as `2020-07-28`.
        :type ServiceStartDate: str
        :param ServiceEndDate: (Exact match) Service end date, such as `2020-07-28`.
        :type ServiceEndDate: str
        :param State: (Exact match) Status. Valid values: `PENDING`, `APPROVED`, and `DENY`.
        :type State: str
        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.Company = None
        self.UniformSocialCreditCode = None
        self.LegalPerson = None
        self.IssuingAuthority = None
        self.BusinessAddress = None
        self.PostCode = None
        self.Manager = None
        self.ManagerId = None
        self.ManagerAddress = None
        self.ManagerTelephone = None
        self.Email = None
        self.ServiceStartDate = None
        self.ServiceEndDate = None
        self.State = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.Company = params.get("Company")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.LegalPerson = params.get("LegalPerson")
        self.IssuingAuthority = params.get("IssuingAuthority")
        self.BusinessAddress = params.get("BusinessAddress")
        self.PostCode = params.get("PostCode")
        self.Manager = params.get("Manager")
        self.ManagerId = params.get("ManagerId")
        self.ManagerAddress = params.get("ManagerAddress")
        self.ManagerTelephone = params.get("ManagerTelephone")
        self.Email = params.get("Email")
        self.ServiceStartDate = params.get("ServiceStartDate")
        self.ServiceEndDate = params.get("ServiceEndDate")
        self.State = params.get("State")


class DescribeCrossBorderComplianceResponse(AbstractModel):
    """DescribeCrossBorderCompliance response structure.

    """

    def __init__(self):
        """
        :param CrossBorderComplianceSet: List of compliance review requests.
        :type CrossBorderComplianceSet: list of CrossBorderCompliance
        :param TotalCount: Total number of compliance review requests.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CrossBorderComplianceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CrossBorderComplianceSet") is not None:
            self.CrossBorderComplianceSet = []
            for item in params.get("CrossBorderComplianceSet"):
                obj = CrossBorderCompliance()
                obj._deserialize(item)
                self.CrossBorderComplianceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewayVendorsRequest(AbstractModel):
    """DescribeCustomerGatewayVendors request structure.

    """


class DescribeCustomerGatewayVendorsResponse(AbstractModel):
    """DescribeCustomerGatewayVendors response structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayVendorSet: Customer gateway vendor information object.
        :type CustomerGatewayVendorSet: list of CustomerGatewayVendor
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CustomerGatewayVendorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewayVendorSet") is not None:
            self.CustomerGatewayVendorSet = []
            for item in params.get("CustomerGatewayVendorSet"):
                obj = CustomerGatewayVendor()
                obj._deserialize(item)
                self.CustomerGatewayVendorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayIds: Customer gateway ID, such as `cgw-2wqq41m9`. Each request can have a maximum of 100 instances. `CustomerGatewayIds` and `Filters` cannot be specified at the same time.
        :type CustomerGatewayIds: list of str
        :param Filters: The filter condition. For details, see the Instance Filter Conditions Table. The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `CustomerGatewayIds` and `Filters` cannot be specified at the same time.
<li>customer-gateway-id - String - (Filter condition) The unique ID of the user gateway, such as `cgw-mgp33pll`.</li>
<li>customer-gateway-name - String - (Filter condition) The name of the user gateway, such as `test-cgw`.</li>
<li>ip-address - String - (Filter condition) The public IP address, such as `58.211.1.12`.</li>
        :type Filters: list of Filter
        :param Offset: The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.CustomerGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CustomerGatewayIds = params.get("CustomerGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways response structure.

    """

    def __init__(self):
        """
        :param CustomerGatewaySet: Customer gateway object list
        :type CustomerGatewaySet: list of CustomerGateway
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CustomerGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewaySet") is not None:
            self.CustomerGatewaySet = []
            for item in params.get("CustomerGatewaySet"):
                obj = CustomerGateway()
                obj._deserialize(item)
                self.CustomerGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`.
        :type DirectConnectGatewayId: str
        :param CcnRouteType: The route learning type of the CCN. Available values:
<li>`BGP` - Automatic learning.</li>
<li>`STATIC` - Static means user-configured. This is the default value.</li>
        :type CcnRouteType: str
        :param Offset: Offset.
        :type Offset: int
        :param Limit: The returned quantity.
        :type Limit: int
        """
        self.DirectConnectGatewayId = None
        self.CcnRouteType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param RouteSet: The CCN route (IDC IP range) list.
        :type RouteSet: list of DirectConnectGatewayCcnRoute
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewaysRequest(AbstractModel):
    """DescribeDirectConnectGateways request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayIds: The unique ID of the direct connect gateway, such as `dcg-9o233uri`.
        :type DirectConnectGatewayIds: list of str
        :param Filters: Filter condition. `DirectConnectGatewayIds` and `Filters` cannot be specified at the same time.
<li>direct-connect-gateway-id - String - The unique ID of the direct connect gateway, such as `dcg-9o233uri`.</li>
<li>direct-connect-gateway-name - String - The name of the direct connect gateway. The default is fuzzy query.</li>
<li>direct-connect-gateway-ip - String - The IP of the direct connect gateway.</li>
<li>gateway-type - String - The gateway type. Valid values: `NORMAL` (Standard type), `NAT` (NAT type).</li>
<li>network-type- String - The network type. Valid values: `VPC` (VPC type), `CCN` (CCN type).</li>
<li>ccn-id - String - The ID of the CCN where the direct connect gateway resides.</li>
<li>vpc-id - String - The ID of the VPC where the direct connect gateway resides.</li>
        :type Filters: list of Filter
        :param Offset: The offset.
        :type Offset: int
        :param Limit: Max number of results returned
        :type Limit: int
        """
        self.DirectConnectGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayIds = params.get("DirectConnectGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewaysResponse(AbstractModel):
    """DescribeDirectConnectGateways response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible objects.
        :type TotalCount: int
        :param DirectConnectGatewaySet: The object array of the direct connect gateway.
        :type DirectConnectGatewaySet: list of DirectConnectGateway
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DirectConnectGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DirectConnectGatewaySet") is not None:
            self.DirectConnectGatewaySet = []
            for item in params.get("DirectConnectGatewaySet"):
                obj = DirectConnectGateway()
                obj._deserialize(item)
                self.DirectConnectGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowLogRequest(AbstractModel):
    """DescribeFlowLog request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogId: The unique ID of the flow log.
        :type FlowLogId: str
        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")


class DescribeFlowLogResponse(AbstractModel):
    """DescribeFlowLog response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The flow log information.
        :type FlowLog: list of FlowLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowLogsRequest(AbstractModel):
    """DescribeFlowLogs request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogId: The unique ID of the flow log.
        :type FlowLogId: str
        :param FlowLogName: The name of the flow log instance.
        :type FlowLogName: str
        :param ResourceType: The resource type of the flow log. Valid values: 'VPC', 'SUBNET', and 'NETWORKINTERFACE'.
        :type ResourceType: str
        :param ResourceId: The unique ID of the resource.
        :type ResourceId: str
        :param TrafficType: Type of flow logs to be collected. Valid values: 'ACCEPT', 'REJECT' and 'ALL'.
        :type TrafficType: str
        :param CloudLogId: The storage ID of the flow log.
        :type CloudLogId: str
        :param CloudLogState: The storage ID status of the flow log.
        :type CloudLogState: str
        :param OrderField: Order by field. Valid values: 'flowLogName' and 'createTime'. Default value: 'createTime'.
        :type OrderField: str
        :param OrderDirection: In ascending (`asc`) or descending (`desc`) order. Default value: 'desc'.
        :type OrderDirection: str
        :param Offset: The offset. Default value: 0.
        :type Offset: int
        :param Limit: The number of rows per page. Default value: 10.
        :type Limit: int
        :param Filters: Filter condition. `FlowLogIds` and `Filters` cannot be specified at the same time.
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key.</li>
        :type Filters: :class:`tencentcloud.vpc.v20170312.models.Filter`
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.OrderField = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))


class DescribeFlowLogsResponse(AbstractModel):
    """DescribeFlowLogs response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The instance set of flow logs.
        :type FlowLog: list of FlowLog
        :param TotalNum: The total number of flow logs.
        :type TotalNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowLog = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowMonitorDetailRequest(AbstractModel):
    """DescribeGatewayFlowMonitorDetail request structure.

    """

    def __init__(self):
        """
        :param TimePoint: The point in time. This indicates details of this minute will be queried. For example, in `2019-02-28 18:15:20`, details at `18:15` will be queried.
        :type TimePoint: str
        :param VpnId: The instance ID of the VPN gateway, such as `vpn-ltjahce6`.
        :type VpnId: str
        :param DirectConnectGatewayId: The instance ID of the Direct Connect gateway, such as `dcg-ltjahce6`.
        :type DirectConnectGatewayId: str
        :param PeeringConnectionId: The instance ID of the peering connection, such as `pcx-ltjahce6`.
        :type PeeringConnectionId: str
        :param NatId: The instance ID of the NAT gateway, such as `nat-ltjahce6`.
        :type NatId: str
        :param Offset: Offset.
        :type Offset: int
        :param Limit: The returned quantity.
        :type Limit: int
        :param OrderField: The order field supports `InPkg`, `OutPkg`, `InTraffic`, and `OutTraffic`.
        :type OrderField: str
        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.
        :type OrderDirection: str
        """
        self.TimePoint = None
        self.VpnId = None
        self.DirectConnectGatewayId = None
        self.PeeringConnectionId = None
        self.NatId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.TimePoint = params.get("TimePoint")
        self.VpnId = params.get("VpnId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.PeeringConnectionId = params.get("PeeringConnectionId")
        self.NatId = params.get("NatId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeGatewayFlowMonitorDetailResponse(AbstractModel):
    """DescribeGatewayFlowMonitorDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param GatewayFlowMonitorDetailSet: The gateway traffic monitoring details.
        :type GatewayFlowMonitorDetailSet: list of GatewayFlowMonitorDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.GatewayFlowMonitorDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GatewayFlowMonitorDetailSet") is not None:
            self.GatewayFlowMonitorDetailSet = []
            for item in params.get("GatewayFlowMonitorDetailSet"):
                obj = GatewayFlowMonitorDetail()
                obj._deserialize(item)
                self.GatewayFlowMonitorDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowQosRequest(AbstractModel):
    """DescribeGatewayFlowQos request structure.

    """

    def __init__(self):
        """
        :param GatewayId: Gateway instance ID, which currently supports these types:
ID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;
ID of NAT gateway instance, e.g. `nat-ltjahce6`;
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.
        :type GatewayId: str
        :param IpAddresses: CVM private IP addresses with limited bandwidth.
        :type IpAddresses: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.GatewayId = None
        self.IpAddresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.IpAddresses = params.get("IpAddresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGatewayFlowQosResponse(AbstractModel):
    """DescribeGatewayFlowQos response structure.

    """

    def __init__(self):
        """
        :param GatewayQosSet: List of instance details.
        :type GatewayQosSet: list of GatewayQos
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GatewayQosSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GatewayQosSet") is not None:
            self.GatewayQosSet = []
            for item in params.get("GatewayQosSet"):
                obj = GatewayQos()
                obj._deserialize(item)
                self.GatewayQosSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips request structure.

    """

    def __init__(self):
        """
        :param HaVipIds: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.
        :type HaVipIds: list of str
        :param Filters: Filter condition. `HaVipIds` and `Filters` cannot be specified at the same time.
li>havip-id - String - The unique ID of the HAVIP, such as `havip-9o233uri`.</li>
<li>havip-name - String - HAVIP name.</li>
<li>vpc-id - String - VPC ID of the HAVIP.</li>
<li>subnet-id - String - Subnet ID of the HAVIP.</li>
<li>vip - String - Virtual IP address of the HAVIP.</li>
<li>address-ip - String - Bound EIP.</li>
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: The returned quantity
        :type Limit: int
        """
        self.HaVipIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.HaVipIds = params.get("HaVipIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param HaVipSet: `HAVIP` object array.
        :type HaVipSet: list of HaVip
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.HaVipSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HaVipSet") is not None:
            self.HaVipSet = []
            for item in params.get("HaVipSet"):
                obj = HaVip()
                obj._deserialize(item)
                self.HaVipSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpGeolocationDatabaseUrlRequest(AbstractModel):
    """DescribeIpGeolocationDatabaseUrl request structure.

    """

    def __init__(self):
        """
        :param Type: Protocol type of the IP location database. Valid values: `ipv4` and `ipv6`.
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")


class DescribeIpGeolocationDatabaseUrlResponse(AbstractModel):
    """DescribeIpGeolocationDatabaseUrl response structure.

    """

    def __init__(self):
        """
        :param DownLoadUrl: Download link of the IP location database.
        :type DownLoadUrl: str
        :param ExpiredAt: Link expiration time in UTC format following the ISO8601 standard.
        :type ExpiredAt: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownLoadUrl = None
        self.ExpiredAt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownLoadUrl = params.get("DownLoadUrl")
        self.ExpiredAt = params.get("ExpiredAt")
        self.RequestId = params.get("RequestId")


class DescribeIpGeolocationInfosRequest(AbstractModel):
    """DescribeIpGeolocationInfos request structure.

    """

    def __init__(self):
        """
        :param AddressIps: IP addresses to be queried. Both IPv4 and IPv6 addresses are supported.
        :type AddressIps: list of str
        :param Fields: Fields of the IP addresses to be queried, including `Country`, `Province`, `City`, `Region`, `Isp`, `AsName` and `AsId`
        :type Fields: :class:`tencentcloud.vpc.v20170312.models.IpField`
        """
        self.AddressIps = None
        self.Fields = None


    def _deserialize(self, params):
        self.AddressIps = params.get("AddressIps")
        if params.get("Fields") is not None:
            self.Fields = IpField()
            self.Fields._deserialize(params.get("Fields"))


class DescribeIpGeolocationInfosResponse(AbstractModel):
    """DescribeIpGeolocationInfos response structure.

    """

    def __init__(self):
        """
        :param AddressInfo: IP address details
        :type AddressInfo: list of IpGeolocationInfo
        :param Total: Number of IP addresses
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddressInfo = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressInfo") is not None:
            self.AddressInfo = []
            for item in params.get("AddressInfo"):
                obj = IpGeolocationInfo()
                obj._deserialize(item)
                self.AddressInfo.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules request structure.

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT gateway ID.
        :type NatGatewayIds: list of str
        :param Filters: Filter conditions:
`NatGatewayIds` and `Filters` cannot be specified at the same time.
<li> nat-gateway-id, the NAT gateway ID, such as `nat-0yi4hekt`.</li>
<li> vpc-id, the VPC ID, such as `vpc-0yi4hekt`.</li>
<li> public-ip-address, the EIP, such as `139.199.232.238`.</li>
<li>public-port, the public network port.</li>
<li>private-ip-address, the private IP, such as `10.0.0.1`.</li>
<li>private-port, the private network port.</li>
<li>description, the rule description.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: int
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: int
        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules response structure.

    """

    def __init__(self):
        """
        :param NatGatewayDestinationIpPortTranslationNatRuleSet: The object array of port forwarding rules for the NAT gateway.
        :type NatGatewayDestinationIpPortTranslationNatRuleSet: list of NatGatewayDestinationIpPortTranslationNatRule
        :param TotalCount: The number of object arrays of NAT port forwarding rules meeting the conditions.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatGatewayDestinationIpPortTranslationNatRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewayDestinationIpPortTranslationNatRuleSet") is not None:
            self.NatGatewayDestinationIpPortTranslationNatRuleSet = []
            for item in params.get("NatGatewayDestinationIpPortTranslationNatRuleSet"):
                obj = NatGatewayDestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.NatGatewayDestinationIpPortTranslationNatRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways request structure.

    """

    def __init__(self):
        """
        :param NatGatewayIds: The unified ID of the NAT gateways, such as `nat-123xx454`.
        :type NatGatewayIds: list of str
        :param Filters: Filter condition. `NatGatewayIds` and `Filters` cannot be specified at the same time.
<li>nat-gateway-id - String - (Filter condition) The ID of the protocol port template instance, such as `nat-123xx454`.</li>
<li>vpc-id - String - (Filter condition) The unique ID of the VPC, such as `vpc-123xx454`.</li>
<li>nat-gateway-name - String - (Filter condition) The name of the protocol port template instance, such as `test_nat`.</li>
<li>tag-key - String - (Filter condition) The tag key, such as `test-key`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: int
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: int
        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways response structure.

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT gateway object array.
        :type NatGatewaySet: list of NatGateway
        :param TotalCount: The number of NAT gateway object sets meeting the conditions.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectStatesRequest(AbstractModel):
    """DescribeNetDetectStates request structure.

    """

    def __init__(self):
        """
        :param NetDetectIds: The array of network detection instance `IDs`, such as [`netd-12345678`].
        :type NetDetectIds: list of str
        :param Filters: Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.
<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>
        :type Filters: list of Filter
        :param Offset: The offset. Default: 0.
        :type Offset: int
        :param Limit: The number of returned values. Default: 20. Maximum: 100.
        :type Limit: int
        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetDetectStatesResponse(AbstractModel):
    """DescribeNetDetectStates response structure.

    """

    def __init__(self):
        """
        :param NetDetectStateSet: The array of network detection verification results that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetDetectStateSet: list of NetDetectState
        :param TotalCount: The number of network detection verification results that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetDetectStateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectStateSet") is not None:
            self.NetDetectStateSet = []
            for item in params.get("NetDetectStateSet"):
                obj = NetDetectState()
                obj._deserialize(item)
                self.NetDetectStateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectsRequest(AbstractModel):
    """DescribeNetDetects request structure.

    """

    def __init__(self):
        """
        :param NetDetectIds: The array of network detection instance `IDs`, such as [`netd-12345678`].
        :type NetDetectIds: list of str
        :param Filters: Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) The VPC instance ID, such as vpc-12345678.</li>
<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>
<li>subnet-id - String - (Filter condition) The subnet instance ID, such as subnet-12345678.</li>
<li>net-detect-name - String - (Filter condition) The network detection name.</li>
        :type Filters: list of Filter
        :param Offset: The offset. Default: 0.
        :type Offset: int
        :param Limit: The number of returned values. Default: 20. Maximum: 100.
        :type Limit: int
        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetDetectsResponse(AbstractModel):
    """DescribeNetDetects response structure.

    """

    def __init__(self):
        """
        :param NetDetectSet: The array of network detection objects that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetDetectSet: list of NetDetect
        :param TotalCount: The number of network detection objects that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetDetectSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectSet") is not None:
            self.NetDetectSet = []
            for item in params.get("NetDetectSet"):
                obj = NetDetect()
                obj._deserialize(item)
                self.NetDetectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkAclsRequest(AbstractModel):
    """DescribeNetworkAcls request structure.

    """

    def __init__(self):
        """
        :param NetworkAclIds: Array of network ACL instance IDs, such as [acl-12345678]. Up to 100 instances are allowed for each request. This parameter does not support specifying `NetworkAclIds` and `Filters` at the same time.
        :type NetworkAclIds: list of str
        :param Filters: Filter condition. `NetworkAclIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as vpc-12345678.</li>
<li>network-acl-id - String - (Filter condition) Network ACL instance ID, such as acl-12345678.</li>
<li>network-acl-name - String - (Filter condition) Network ACL instance name.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default: 0.
        :type Offset: int
        :param Limit: Returned quantity. Default: 20. Value range: 1-100.
        :type Limit: int
        """
        self.NetworkAclIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetworkAclIds = params.get("NetworkAclIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetworkAclsResponse(AbstractModel):
    """DescribeNetworkAcls response structure.

    """

    def __init__(self):
        """
        :param NetworkAclSet: List of instance details.
        :type NetworkAclSet: list of NetworkAcl
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkAclSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAclSet") is not None:
            self.NetworkAclSet = []
            for item in params.get("NetworkAclSet"):
                obj = NetworkAcl()
                obj._deserialize(item)
                self.NetworkAclSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfaceLimitRequest(AbstractModel):
    """DescribeNetworkInterfaceLimit request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of a CVM instance or ENI to query
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeNetworkInterfaceLimitResponse(AbstractModel):
    """DescribeNetworkInterfaceLimit response structure.

    """

    def __init__(self):
        """
        :param EniQuantity: ENI quota
        :type EniQuantity: int
        :param EniPrivateIpAddressQuantity: Quota of IP addresses that can be allocated to each ENI.
        :type EniPrivateIpAddressQuantity: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EniQuantity = None
        self.EniPrivateIpAddressQuantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EniQuantity = params.get("EniQuantity")
        self.EniPrivateIpAddressQuantity = params.get("EniPrivateIpAddressQuantity")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request can have a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
        :type NetworkInterfaceIds: list of str
        :param Filters: Filter condition. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>subnet-id - String - (Filter condition) Subnet instance ID, such as `subnet-f49l6u0z`.</li>
<li>network-interface-id - String - (Filter condition) ENI instance ID, such as `eni-5k56k7k7`.</li>
<li>attachment.instance-id - String - (Filter condition) CVM instance ID, such as `ins-3nqpdn3i`.</li>
<li>groups.security-group-id - String - (Filter condition) Instance ID of the security group, such as `sg-f9ekbxeq`.</li>
<li>network-interface-name - String - (Filter condition) ENI instance name.</li>
<li>network-interface-description - String - (Filter condition) ENI instance description.</li>
<li>address-ip - String - (Filter condition) Private IPv4 address.</li>
<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>
<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>
<li>is-primary - Boolean - Required: no - (Filter condition) Filters based on whether it is a primary ENI. If the value is ‘true’, filter only the primary ENI. If the value is ‘false’, filter only the secondary ENI. If the secondary filter parameter is provided, filter the both.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces response structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceSet: List of instance details.
        :type NetworkInterfaceSet: list of NetworkInterface
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkInterfaceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables request structure.

    """

    def __init__(self):
        """
        :param RouteTableIds: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableIds: list of str
        :param Filters: Filter condition. `RouteTableIds` and `Filters` cannot be speified at the same time.
<li>route-table-id - String - (Filter condition) Route table instance ID.</li>
<li>route-table-name - String - (Filter condition) Route table name.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>association.main - String - (Filter condition) Whether it is the main route table.</li>
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>
        :type Filters: list of Filter
        :param Offset: Offset.
        :type Offset: str
        :param Limit: The number of request objects.
        :type Limit: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RouteTableSet: Route table object.
        :type RouteTableSet: list of RouteTable
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupIds: The Security instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups.
        :type SecurityGroupIds: list of str
        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupAssociationStatisticsSet: Statistics on the instances associated with a security group.
        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroupAssociationStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupAssociationStatisticsSet") is not None:
            self.SecurityGroupAssociationStatisticsSet = []
            for item in params.get("SecurityGroupAssociationStatisticsSet"):
                obj = SecurityGroupAssociationStatistics()
                obj._deserialize(item)
                self.SecurityGroupAssociationStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroupPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupReferencesRequest(AbstractModel):
    """DescribeSecurityGroupReferences request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupIds: A set of security group instance IDs, e.g. ['sg-12345678']
        :type SecurityGroupIds: list of str
        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupReferencesResponse(AbstractModel):
    """DescribeSecurityGroupReferences response structure.

    """

    def __init__(self):
        """
        :param ReferredSecurityGroupSet: Referred security groups.
        :type ReferredSecurityGroupSet: list of ReferredSecurityGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReferredSecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReferredSecurityGroupSet") is not None:
            self.ReferredSecurityGroupSet = []
            for item in params.get("ReferredSecurityGroupSet"):
                obj = ReferredSecurityGroup()
                obj._deserialize(item)
                self.ReferredSecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through `DescribeSecurityGroups`. Each request can have a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
        :type SecurityGroupIds: list of str
        :param Filters: Filter conditions. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
<li>security-group-id - String - (Filter condition) The security group ID.</li>
<li>project-id - Integer - (Filter condition) The project ID.</li>
<li>security-group-name - String - (Filter condition) The security group name.</li>
<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>
<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: str
        """
        self.SecurityGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupSet: Security group object.
        :type SecurityGroupSet: list of SecurityGroup
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplateGroupsRequest(AbstractModel):
    """DescribeServiceTemplateGroups request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions.
<li>service-template-group-name - String - (Filter condition) Protocol port template group name.</li>
<li>service-template-group-id - String - (Filter condition) Protocol port template group instance ID, such as `ppmg-e6dy460g`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: str
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeServiceTemplateGroupsResponse(AbstractModel):
    """DescribeServiceTemplateGroups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param ServiceTemplateGroupSet: Protocol port template group.
        :type ServiceTemplateGroupSet: list of ServiceTemplateGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateGroupSet") is not None:
            self.ServiceTemplateGroupSet = []
            for item in params.get("ServiceTemplateGroupSet"):
                obj = ServiceTemplateGroup()
                obj._deserialize(item)
                self.ServiceTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplatesRequest(AbstractModel):
    """DescribeServiceTemplates request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter conditions.
<li>service-template-name - String - (Filter condition) Protocol port template name.</li>
<li>service-template-id - String - (Filter condition) Protocol port template instance ID, such as `ppm-e6dy460g`.</li>
        :type Filters: list of Filter
        :param Offset: Offset. The default value is 0.
        :type Offset: str
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeServiceTemplatesResponse(AbstractModel):
    """DescribeServiceTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param ServiceTemplateSet: Protocol port template object.
        :type ServiceTemplateSet: list of ServiceTemplate
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets request structure.

    """

    def __init__(self):
        """
        :param SubnetIds: Queries the ID of the subnet instance, such as `subnet-pxir56ns`. Each request can have a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time.
        :type SubnetIds: list of str
        :param Filters: Filter condition. `SubnetIds` and `Filters` cannot be specified at the same time.
<li>subnet-id - String - (Filter condition) Subnet instance name.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>cidr-block - String - (Filter condition) The subnet IP range, such as 192.168.1.0.</li>
<li>is-default - Boolean - (Filter condition) Whether it is the default subnet.</li>
<li>is-remote-vpc-snat - Boolean - (Filter condition) Whether it is a VPC SNAT address pool subnet.</li>
<li>subnet-name - String - (Filter condition) Subnet name.</li>
<li>zone - String - (Filter condition) Availability zone.</li>
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: str
        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param SubnetSet: Subnet object.
        :type SubnetSet: list of Subnet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult request structure.

    """

    def __init__(self):
        """
        :param TaskId: Async task ID. Either TaskId or DealName must be entered.
        :type TaskId: int
        :param DealName: Billing order No. Either TaskId or DealName must be entered.
        :type DealName: str
        """
        self.TaskId = None
        self.DealName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DealName = params.get("DealName")


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult response structure.

    """

    def __init__(self):
        """
        :param TaskId: Job ID
        :type TaskId: int
        :param Result: The execution results, including `SUCCESS`, `FAILED`, and `RUNNING`
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeVpcInstancesRequest(AbstractModel):
    """DescribeVpcInstances request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter condition. `RouteTableIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>instance-type - String - (Filter condition) CVM instance ID.</li>
<li>instance-name - String - (Filter condition) CVM name.</li>
        :type Filters: list of Filter
        :param Offset: Offset.
        :type Offset: int
        :param Limit: The number of requested objects.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcInstancesResponse(AbstractModel):
    """DescribeVpcInstances response structure.

    """

    def __init__(self):
        """
        :param InstanceSet: List of CVM instances.
        :type InstanceSet: list of CvmInstance
        :param TotalCount: The number of eligible CVM instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CvmInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcIpv6AddressesRequest(AbstractModel):
    """DescribeVpcIpv6Addresses request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param Ipv6Addresses: The `IP` address list. Each request supports a maximum of `10` batch querying.
        :type Ipv6Addresses: list of str
        :param Offset: Offset.
        :type Offset: int
        :param Limit: The returned quantity.
        :type Limit: int
        """
        self.VpcId = None
        self.Ipv6Addresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6Addresses = params.get("Ipv6Addresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcIpv6AddressesResponse(AbstractModel):
    """DescribeVpcIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: The `IPv6` address list.
        :type Ipv6AddressSet: list of VpcIpv6Address
        :param TotalCount: The total number of `IPv6` addresses.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ipv6AddressSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = VpcIpv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcPrivateIpAddressesRequest(AbstractModel):
    """DescribeVpcPrivateIpAddresses request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param PrivateIpAddresses: The private `IP` address list. Each request supports a maximum of `10` batch querying.
        :type PrivateIpAddresses: list of str
        """
        self.VpcId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")


class DescribeVpcPrivateIpAddressesResponse(AbstractModel):
    """DescribeVpcPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param VpcPrivateIpAddressSet: The list of private `IP` address information.
        :type VpcPrivateIpAddressSet: list of VpcPrivateIpAddress
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VpcPrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcPrivateIpAddressSet") is not None:
            self.VpcPrivateIpAddressSet = []
            for item in params.get("VpcPrivateIpAddressSet"):
                obj = VpcPrivateIpAddress()
                obj._deserialize(item)
                self.VpcPrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcResourceDashboardRequest(AbstractModel):
    """DescribeVpcResourceDashboard request structure.

    """

    def __init__(self):
        """
        :param VpcIds: Vpc instance ID, e.g. vpc-f1xjkw1b.
        :type VpcIds: list of str
        """
        self.VpcIds = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")


class DescribeVpcResourceDashboardResponse(AbstractModel):
    """DescribeVpcResourceDashboard response structure.

    """

    def __init__(self):
        """
        :param ResourceDashboardSet: List of resource objects.
        :type ResourceDashboardSet: list of ResourceDashboard
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResourceDashboardSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceDashboardSet") is not None:
            self.ResourceDashboardSet = []
            for item in params.get("ResourceDashboardSet"):
                obj = ResourceDashboard()
                obj._deserialize(item)
                self.ResourceDashboardSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs request structure.

    """

    def __init__(self):
        """
        :param VpcIds: The VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time.
        :type VpcIds: list of str
        :param Filters: Filter condition. `VpcIds` and `Filters` cannot be specified at the same time.
<li>vpc-name - String - (Filter condition) VPC instance name.</li>
<li>is-default - String - (Filter condition) Indicates whether it is the default VPC.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>cidr-block - String - (Filter condition) VPC CIDR.</li>
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: str
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.
        :type TotalCount: int
        :param VpcSet: The VPC object.
        :type VpcSet: list of Vpc
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = Vpc()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnConnectionsRequest(AbstractModel):
    """DescribeVpnConnections request structure.

    """

    def __init__(self):
        """
        :param VpnConnectionIds: The instance ID of the VPN tunnel, such as `vpnx-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnConnectionIds` and `Filters` cannot be specified at the same time.
        :type VpnConnectionIds: list of str
        :param Filters: Filter condition. In each request, the upper limit for `Filters` is 10 and 5 for `Filter.Values`. `VpnConnectionIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - VPC instance ID, such as `vpc-0a36uwkr`.</li>
<li>vpn-gateway-id - String - VPN gateway instance ID, such as `vpngw-p4lmqawn`.</li>
<li>customer-gateway-id - String - Customer gateway instance ID, such as `cgw-l4rblw63`.</li>
<li>vpn-connection-name - String - Connection name, such as `test-vpn`.</li>
<li>vpn-connection-id - String - Connection instance ID, such as `vpnx-5p7vkch8"`.</li>
        :type Filters: list of Filter
        :param Offset: The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction.
        :type Offset: int
        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.
        :type Limit: int
        """
        self.VpnConnectionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnConnectionIds = params.get("VpnConnectionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param VpnConnectionSet: VPN tunnel instance.
        :type VpnConnectionSet: list of VpnConnection
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnConnectionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnConnectionSet") is not None:
            self.VpnConnectionSet = []
            for item in params.get("VpnConnectionSet"):
                obj = VpnConnection()
                obj._deserialize(item)
                self.VpnConnectionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewayCcnRoutesRequest(AbstractModel):
    """DescribeVpnGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param Offset: Offset.
        :type Offset: int
        :param Limit: The returned quantity
        :type Limit: int
        """
        self.VpnGatewayId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnGatewayCcnRoutesResponse(AbstractModel):
    """DescribeVpnGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RouteSet: The CCN route (IDC IP range) list.
        :type RouteSet: list of VpngwCcnRoutes
        :param TotalCount: Number of objects that meet the condition.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RouteSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayIds: The VPN gateway instance ID, such as `vpngw-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnGatewayIds` and `Filters` cannot be specified at the same time.
        :type VpnGatewayIds: list of str
        :param Filters: Filter condition. `VpnGatewayIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>vpn-gateway-id - String - (Filter condition) VPN instance ID, such as `vpngw-5aluhh9t`.</li>
<li>vpn-gateway-name - String - (Filter condition) VPN instance name.</li>
<li>type - String - (Filter condition) VPN gateway type: 'IPSEC', 'SSL'.</li>
<li>public-ip-address- String - (Filter condition) Public IP.</li>
<li>renew-flag - String - (Filter condition) Gateway renewal type. Manual renewal: `NOTIFY_AND_MANUAL_RENEW`, Automatic renewal: `NOTIFY_AND_AUTO_RENEW`.</li>
<li>zone - String - (Filter condition) The availability zone where the VPN is located, such as `ap-guangzhou-2`.</li>
        :type Filters: list of FilterObject
        :param Offset: Offset
        :type Offset: int
        :param Limit: The number of request objects.
        :type Limit: int
        """
        self.VpnGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayIds = params.get("VpnGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.
        :type TotalCount: int
        :param VpnGatewaySet: The list of details of VPN gateway instances.
        :type VpnGatewaySet: list of VpnGateway
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnGatewaySet") is not None:
            self.VpnGatewaySet = []
            for item in params.get("VpnGatewaySet"):
                obj = VpnGateway()
                obj._deserialize(item)
                self.VpnGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DestinationIpPortTranslationNatRule(AbstractModel):
    """The port forwarding rules of the NAT gateway

    """

    def __init__(self):
        """
        :param IpProtocol: Network protocol. Available choices: `TCP`, `UDP`.
        :type IpProtocol: str
        :param PublicIpAddress: EIP.
        :type PublicIpAddress: str
        :param PublicPort: Public port.
        :type PublicPort: int
        :param PrivateIpAddress: Private network address.
        :type PrivateIpAddress: str
        :param PrivatePort: Private network port.
        :type PrivatePort: int
        :param Description: NAT gateway forwarding rule description.
        :type Description: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param Instances: The list of network instances to be unbound
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachClassicLinkVpcRequest(AbstractModel):
    """DetachClassicLinkVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.
        :type VpcId: str
        :param InstanceIds: Queries the ID of the CVM instance, such as `ins-r8hr2upy`.
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class DetachClassicLinkVpcResponse(AbstractModel):
    """DetachClassicLinkVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param InstanceId: The ID of the CVM instance, such as `ins-r8hr2upy`.
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DirectConnectGateway(AbstractModel):
    """Direct Connect gateway object.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: Direct Connect `ID`.
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: Direct Connect gateway name.
        :type DirectConnectGatewayName: str
        :param VpcId: The `ID` of the `VPC` instance associated with the Direct Connect gateway.
        :type VpcId: str
        :param NetworkType: The associated network type:
<li>`VPC` - VPC</li>
<li>`CCN` - CCN</li>
        :type NetworkType: str
        :param NetworkInstanceId: The `ID` of the associated network instance:
<li>When the NetworkType is `VPC`, this value is the VPC instance `ID`</li>
<li>When the NetworkType is `CCN`, this value is the CCN instance `ID`</li>
        :type NetworkInstanceId: str
        :param GatewayType: Gateway type:
<li>NORMAL - Standard type. Note: CCN only supports the standard type</li>
<li>NAT - NAT type</li>
NAT type supports network address switch configuration. After the type is confirmed, it cannot be modified. A VPC can create one NAT-type Direct Connect gateway and one non-NAT-type Direct Connect gateway
        :type GatewayType: str
        :param CreateTime: Creation Time.
        :type CreateTime: str
        :param DirectConnectGatewayIp: Direct Connect gateway IP.
        :type DirectConnectGatewayIp: str
        :param CcnId: The `ID` of the `CCN` instance associated with the Direct Connect gateway.
        :type CcnId: str
        :param CcnRouteType: The route-learning type of the CCN:
<li>`BGP` - Automatic learning.</li>
<li>`STATIC` - Static, that is, user-configured.</li>
        :type CcnRouteType: str
        :param EnableBGP: Whether BGP is enabled.
        :type EnableBGP: bool
        :param EnableBGPCommunity: Whether to enable BGP's `community` attribute. Valid values: enable, disable
        :type EnableBGPCommunity: bool
        :param NatGatewayId: ID of the NAT gateway bound.
Note: this field may return `null`, indicating that no valid value was found.
        :type NatGatewayId: str
        :param VXLANSupport: Whether the direct connect gateway supports the VXLAN architecture.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VXLANSupport: list of bool
        :param ModeType: CCN route publishing mode. Valid values: `standard` and `exquisite`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ModeType: str
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.VpcId = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.CreateTime = None
        self.DirectConnectGatewayIp = None
        self.CcnId = None
        self.CcnRouteType = None
        self.EnableBGP = None
        self.EnableBGPCommunity = None
        self.NatGatewayId = None
        self.VXLANSupport = None
        self.ModeType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcId = params.get("VpcId")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.CreateTime = params.get("CreateTime")
        self.DirectConnectGatewayIp = params.get("DirectConnectGatewayIp")
        self.CcnId = params.get("CcnId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.EnableBGP = params.get("EnableBGP")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VXLANSupport = params.get("VXLANSupport")
        self.ModeType = params.get("ModeType")


class DirectConnectGatewayCcnRoute(AbstractModel):
    """The object of the CCN route (IDC IP range) of the Direct Connect gateway

    """

    def __init__(self):
        """
        :param RouteId: Route ID.
        :type RouteId: str
        :param DestinationCidrBlock: IDC IP range.
        :type DestinationCidrBlock: str
        :param ASPath: The `AS-Path` attribute of `BGP`.
        :type ASPath: list of str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.ASPath = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.ASPath = params.get("ASPath")


class DisableCcnRoutesRequest(AbstractModel):
    """DisableCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class DisableCcnRoutesResponse(AbstractModel):
    """DisableCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableGatewayFlowMonitorRequest(AbstractModel):
    """DisableGatewayFlowMonitor request structure.

    """

    def __init__(self):
        """
        :param GatewayId: Gateway instance ID, which currently supports these types:
ID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;
ID of NAT gateway instance, e.g. `nat-ltjahce6`;
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")


class DisableGatewayFlowMonitorResponse(AbstractModel):
    """DisableGatewayFlowMonitor response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.
        :type AddressId: str
        :param ReallocateNormalPublicIp: Whether a common public IP is assigned after the EIP is unbound. Value range:<br><li>TRUE: Indicates that after the EIP is unbound, a common public IP is assigned.<br><li>FALSE: Indicates that after the EIP is unbound, a common public IP is not assigned.<br>Default value: FALSE.<br><br>The parameter can be specified only under the following conditions:<br><li>It can only be specified when you unbind an EIP from the primary private IP of the primary ENI.<br><li>After an EIP is unbound, you can assign public IPs to an account up to 10 times per day. For more information, use the [DescribeAddressQuota] (https://intl.cloud.tencent.com/document/api/213/1378?from_cn_redirect=1) API.
        :type ReallocateNormalPublicIp: bool
        """
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisassociateDirectConnectGatewayNatGatewayRequest(AbstractModel):
    """DisassociateDirectConnectGatewayNatGateway request structure.

    """

    def __init__(self):
        """
        :param VpcId: The direct connect gateway ID.
        :type VpcId: str
        :param NatGatewayId: The NAT Gateway ID.
        :type NatGatewayId: str
        :param DirectConnectGatewayId: The ID of the VPC instance, which can be obtained from the `VpcId` field in response of the `DescribeVpcs` API.
        :type DirectConnectGatewayId: str
        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class DisassociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """DisassociateDirectConnectGatewayNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNatGatewayAddressRequest(AbstractModel):
    """DisassociateNatGatewayAddress request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param PublicIpAddresses: Array of the EIPs to be unbound from the NAT gateway.
        :type PublicIpAddresses: list of str
        """
        self.NatGatewayId = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")


class DisassociateNatGatewayAddressResponse(AbstractModel):
    """DisassociateNatGatewayAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkAclSubnetsRequest(AbstractModel):
    """DisassociateNetworkAclSubnets request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.
        :type NetworkAclId: str
        :param SubnetIds: Array of subnet instance IDs. Example: [subnet-12345678].
        :type SubnetIds: list of str
        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")


class DisassociateNetworkAclSubnetsResponse(AbstractModel):
    """DisassociateNetworkAclSubnets response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request.
        :type NetworkInterfaceIds: list of str
        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request.
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DisassociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.
        :type VpnConnectionId: str
        :param CustomerGatewayVendor: Customer gateway vendor information object, which can be obtained through DescribeCustomerGatewayVendors.
        :type CustomerGatewayVendor: :class:`tencentcloud.vpc.v20170312.models.CustomerGatewayVendor`
        :param InterfaceName: Name of the physical API for tunnel access device.
        :type InterfaceName: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None
        self.CustomerGatewayVendor = None
        self.InterfaceName = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        if params.get("CustomerGatewayVendor") is not None:
            self.CustomerGatewayVendor = CustomerGatewayVendor()
            self.CustomerGatewayVendor._deserialize(params.get("CustomerGatewayVendor"))
        self.InterfaceName = params.get("InterfaceName")


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration response structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: Configuration information in XML format.
        :type CustomerGatewayConfiguration: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CustomerGatewayConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
        self.RequestId = params.get("RequestId")


class EnableCcnRoutesRequest(AbstractModel):
    """EnableCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class EnableCcnRoutesResponse(AbstractModel):
    """EnableCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableGatewayFlowMonitorRequest(AbstractModel):
    """EnableGatewayFlowMonitor request structure.

    """

    def __init__(self):
        """
        :param GatewayId: Gateway instance ID, which currently supports these types:
ID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;
ID of NAT gateway instance, e.g. `nat-ltjahce6`;
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")


class EnableGatewayFlowMonitorResponse(AbstractModel):
    """EnableGatewayFlowMonitor response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        """
        :param Name: The attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :type Name: str
        :param Values: The attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is `OR`.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class FilterObject(AbstractModel):
    """Filter key-value pair

    """

    def __init__(self):
        """
        :param Name: The attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :type Name: str
        :param Values: The attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is `OR`.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class FlowLog(AbstractModel):
    """Flow Log

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogId: The unique ID of the flow log.
        :type FlowLogId: str
        :param FlowLogName: The name of the flow log instance.
        :type FlowLogName: str
        :param ResourceType: The resource type of the flow log. Valid values: 'VPC', 'SUBNET', and 'NETWORKINTERFACE'.
        :type ResourceType: str
        :param ResourceId: The unique ID of the resource.
        :type ResourceId: str
        :param TrafficType: Type of flow logs to be collected. Valid values: `ACCEPT`, `REJECT` and `ALL`.
        :type TrafficType: str
        :param CloudLogId: The storage ID of the flow log.
        :type CloudLogId: str
        :param CloudLogState: The storage ID status of the flow log.
        :type CloudLogState: str
        :param FlowLogDescription: The flow log description.
        :type FlowLogDescription: str
        :param CreatedTime: The creation time of the flow log.
        :type CreatedTime: str
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.FlowLogDescription = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.FlowLogDescription = params.get("FlowLogDescription")
        self.CreatedTime = params.get("CreatedTime")


class GatewayFlowMonitorDetail(AbstractModel):
    """The gateway traffic monitoring details

    """

    def __init__(self):
        """
        :param PrivateIpAddress: Origin `IP`.
        :type PrivateIpAddress: str
        :param InPkg: Inbound packets.
        :type InPkg: int
        :param OutPkg: Outbound packets.
        :type OutPkg: int
        :param InTraffic: Inbound traffic, in Byte.
        :type InTraffic: int
        :param OutTraffic: Outbound traffic, in Byte.
        :type OutTraffic: int
        """
        self.PrivateIpAddress = None
        self.InPkg = None
        self.OutPkg = None
        self.InTraffic = None
        self.OutTraffic = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.InPkg = params.get("InPkg")
        self.OutPkg = params.get("OutPkg")
        self.InTraffic = params.get("InTraffic")
        self.OutTraffic = params.get("OutTraffic")


class GatewayQos(AbstractModel):
    """Gateway bandwidth limit information

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param IpAddress: CVM Private IP.
        :type IpAddress: str
        :param Bandwidth: Bandwidth limit value.
        :type Bandwidth: int
        :param CreateTime: The creation time.
        :type CreateTime: str
        """
        self.VpcId = None
        self.IpAddress = None
        self.Bandwidth = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpAddress = params.get("IpAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.CreateTime = params.get("CreateTime")


class GetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """GetCcnRegionBandwidthLimits request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param Filters: The filter condition.
<li>sregion - String - (Filter condition) Filter by the source region, such as 'ap-guangzhou'.</li>
<li>dregion - String - (Filter condition) Filter by the destination region, such as 'ap-shanghai-bm'.</li>
        :type Filters: list of Filter
        :param SortedBy: The sorting condition. Valid values: `BandwidthLimit` and `ExpireTime`.
        :type SortedBy: str
        :param Offset: The offset.
        :type Offset: int
        :param Limit: The returned quantity.
        :type Limit: int
        :param OrderBy: In ascending or descending order. Valid values: 'ASC' and 'DESC'.
        :type OrderBy: str
        """
        self.CcnId = None
        self.Filters = None
        self.SortedBy = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortedBy = params.get("SortedBy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")


class GetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """GetCcnRegionBandwidthLimits response structure.

    """

    def __init__(self):
        """
        :param CcnBandwidthSet: The outbound bandwidth limits of regions in a CCN instance.
Note: this field may return null, indicating that no valid value was found.
        :type CcnBandwidthSet: list of CcnBandwidthInfo
        :param TotalCount: The number of eligible objects.
Note: this field may return null, indicating that no valid value was found.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CcnBandwidthSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnBandwidthSet") is not None:
            self.CcnBandwidthSet = []
            for item in params.get("CcnBandwidthSet"):
                obj = CcnBandwidthInfo()
                obj._deserialize(item)
                self.CcnBandwidthSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class HaVip(AbstractModel):
    """HAVIP description information

    """

    def __init__(self):
        """
        :param HaVipId: The `ID` of the `HAVIP`. This is the unique identifier of the `HAVIP`.
        :type HaVipId: str
        :param HaVipName: The name of the `HAVIP`.
        :type HaVipName: str
        :param Vip: The virtual IP address.
        :type Vip: str
        :param VpcId: The `ID` of the VPC to which the `HAVIP` belongs.
        :type VpcId: str
        :param SubnetId: The `ID` of the subnet to which the `HAVIP` belongs.
        :type SubnetId: str
        :param NetworkInterfaceId: The `ID` of the ENI associated with the `HAVIP`.
        :type NetworkInterfaceId: str
        :param InstanceId: The `ID` of the bound instance.
        :type InstanceId: str
        :param AddressIp: Bound `EIP`.
        :type AddressIp: str
        :param State: Status:
<li>`AVAILABLE`: Operating</li>
<li>`UNBIND`: Not bound</li>
        :type State: str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param Business: Identifier for businesses that use HAVIP.
        :type Business: str
        """
        self.HaVipId = None
        self.HaVipName = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.AddressIp = None
        self.State = None
        self.CreatedTime = None
        self.Business = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.AddressIp = params.get("AddressIp")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.Business = params.get("Business")


class HaVipAssociateAddressIpRequest(AbstractModel):
    """HaVipAssociateAddressIp request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be a `HAVIP` that has not been bound to an `EIP`
        :type HaVipId: str
        :param AddressIp: The Elastic `IP`. This must be an `EIP` that has not been bound to a `HAVIP`
        :type AddressIp: str
        """
        self.HaVipId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.AddressIp = params.get("AddressIp")


class HaVipAssociateAddressIpResponse(AbstractModel):
    """HaVipAssociateAddressIp response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class HaVipDisassociateAddressIpRequest(AbstractModel):
    """HaVipDisassociateAddressIp request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be an `HAVIP` that has been bound to an `EIP`.
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class HaVipDisassociateAddressIpResponse(AbstractModel):
    """HaVipDisassociateAddressIp response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IKEOptionsSpecification(AbstractModel):
    """Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user.

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: Encryption algorithm. Available values: '3DES-CBC', 'AES-CBC-128', 'AES-CBS-192', 'AES-CBC-256', and 'DES-CBC'. Default is 3DES-CBC.
        :type PropoEncryAlgorithm: str
        :param PropoAuthenAlgorithm: Verification algorithm. Available value: 'MD5' and 'SHA1'. Default is MD5.
        :type PropoAuthenAlgorithm: str
        :param ExchangeMode: Negotiation mode. Available values: 'AGGRESSIVE' and 'MAIN'. Default is MAIN.
        :type ExchangeMode: str
        :param LocalIdentity: Type of local identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS.
        :type LocalIdentity: str
        :param RemoteIdentity: Type of remote identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS.
        :type RemoteIdentity: str
        :param LocalAddress: Local identity. When ADDRESS is selected for LocalIdentity, LocalAddress is required. The default LocalAddress is the public IP of the VPN gateway.
        :type LocalAddress: str
        :param RemoteAddress: Remote identity. When ADDRESS is selected for RemoteIdentity, RemoteAddress is required.
        :type RemoteAddress: str
        :param LocalFqdnName: Local identity. When FQDN is selected for LocalIdentity, LocalFqdnName is required.
        :type LocalFqdnName: str
        :param RemoteFqdnName: Remote identity. When FQDN is selected for RemoteIdentity, RemoteFqdnName is required.
        :type RemoteFqdnName: str
        :param DhGroupName: DH group. Specify the DH group used for exchanging the key via IKE. Available values: 'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', and 'GROUP24'.
        :type DhGroupName: str
        :param IKESaLifetimeSeconds: IKE SA lifetime (in sec). Value range: 60-604800
        :type IKESaLifetimeSeconds: int
        :param IKEVersion: IKE version
        :type IKEVersion: str
        """
        self.PropoEncryAlgorithm = None
        self.PropoAuthenAlgorithm = None
        self.ExchangeMode = None
        self.LocalIdentity = None
        self.RemoteIdentity = None
        self.LocalAddress = None
        self.RemoteAddress = None
        self.LocalFqdnName = None
        self.RemoteFqdnName = None
        self.DhGroupName = None
        self.IKESaLifetimeSeconds = None
        self.IKEVersion = None


    def _deserialize(self, params):
        self.PropoEncryAlgorithm = params.get("PropoEncryAlgorithm")
        self.PropoAuthenAlgorithm = params.get("PropoAuthenAlgorithm")
        self.ExchangeMode = params.get("ExchangeMode")
        self.LocalIdentity = params.get("LocalIdentity")
        self.RemoteIdentity = params.get("RemoteIdentity")
        self.LocalAddress = params.get("LocalAddress")
        self.RemoteAddress = params.get("RemoteAddress")
        self.LocalFqdnName = params.get("LocalFqdnName")
        self.RemoteFqdnName = params.get("RemoteFqdnName")
        self.DhGroupName = params.get("DhGroupName")
        self.IKESaLifetimeSeconds = params.get("IKESaLifetimeSeconds")
        self.IKEVersion = params.get("IKEVersion")


class IPSECOptionsSpecification(AbstractModel):
    """IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.

    """

    def __init__(self):
        """
        :param EncryptAlgorithm: Encryption algorithm. Available values: '3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', and 'NULL'. Default is AES-CBC-128.
        :type EncryptAlgorithm: str
        :param IntegrityAlgorith: Verification algorithm. Available value: 'MD5' and 'SHA1'. Default is:
        :type IntegrityAlgorith: str
        :param IPSECSaLifetimeSeconds: IPsec SA lifetime (in sec). Value range: 180-604800
        :type IPSECSaLifetimeSeconds: int
        :param PfsDhGroup: PFS. Available value: 'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', and 'DH-GROUP24'. Default is NULL.
        :type PfsDhGroup: str
        :param IPSECSaLifetimeTraffic: IPsec SA lifetime (in KB). Value range: 2560-604800
        :type IPSECSaLifetimeTraffic: int
        """
        self.EncryptAlgorithm = None
        self.IntegrityAlgorith = None
        self.IPSECSaLifetimeSeconds = None
        self.PfsDhGroup = None
        self.IPSECSaLifetimeTraffic = None


    def _deserialize(self, params):
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.IntegrityAlgorith = params.get("IntegrityAlgorith")
        self.IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self.PfsDhGroup = params.get("PfsDhGroup")
        self.IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")


class InquirePriceCreateDirectConnectGatewayRequest(AbstractModel):
    """InquirePriceCreateDirectConnectGateway request structure.

    """


class InquirePriceCreateDirectConnectGatewayResponse(AbstractModel):
    """InquirePriceCreateDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param TotalCost: Standard access fee for a direct connect gateway
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCost: int
        :param RealTotalCost: Actual access fee for a direct connect gateway
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RealTotalCost: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCost = None
        self.RealTotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateVpnGatewayRequest(AbstractModel):
    """InquiryPriceCreateVpnGateway request structure.

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceCreateVpnGatewayResponse(AbstractModel):
    """InquiryPriceCreateVpnGateway response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewVpnGatewayRequest(AbstractModel):
    """InquiryPriceRenewVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: Specifies the purchased validity period, whether to enable auto-renewal. This parameter is required for monthly-subscription instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceRenewVpnGatewayResponse(AbstractModel):
    """InquiryPriceRenewVpnGateway response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """Prepaid (monthly subscription) billing object.

    """

    def __init__(self):
        """
        :param Period: Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36].
        :type Period: int
        :param RenewFlag: Auto-renewal ID. Value range: NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically, NOTIFY_AND_MANUAL_RENEW: notify expiry but do not renew automatically. The default is NOTIFY_AND_MANUAL_RENEW
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceStatistic(AbstractModel):
    """Statistics used to describe the instance

    """

    def __init__(self):
        """
        :param InstanceType: Type of instance
        :type InstanceType: str
        :param InstanceCount: Number of instances
        :type InstanceCount: int
        """
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")


class IpField(AbstractModel):
    """IP information to be queried

    """

    def __init__(self):
        """
        :param Country: Country/region of the IP
        :type Country: bool
        :param Province: Province/municipality/state of the IP
        :type Province: bool
        :param City: City of the IP
        :type City: bool
        :param Region: City district of the IP
        :type Region: bool
        :param Isp: Access ISP field
        :type Isp: bool
        :param AsName: ISP backbone network’s AS field
        :type AsName: bool
        :param AsId: Backbone AS ID
        :type AsId: bool
        :param Comment: Comment
        :type Comment: bool
        """
        self.Country = None
        self.Province = None
        self.City = None
        self.Region = None
        self.Isp = None
        self.AsName = None
        self.AsId = None
        self.Comment = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Region = params.get("Region")
        self.Isp = params.get("Isp")
        self.AsName = params.get("AsName")
        self.AsId = params.get("AsId")
        self.Comment = params.get("Comment")


class IpGeolocationInfo(AbstractModel):
    """IP location

    """

    def __init__(self):
        """
        :param Country: Country/region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Country: str
        :param Province: Province- or municipality-level administrative region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Province: str
        :param City: Municipal administrative region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type City: str
        :param Region: Urban area
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param Isp: Access ISP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Isp: str
        :param AsName: ISP backbone network’s AS name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AsName: str
        :param AsId: ISP backbone network’s AS ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AsId: str
        :param Comment: Comment. The APN value of mobile users is entered currently. If there is no APN attribute, this is `null`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Comment: str
        :param AddressIp: IP address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AddressIp: str
        """
        self.Country = None
        self.Province = None
        self.City = None
        self.Region = None
        self.Isp = None
        self.AsName = None
        self.AsId = None
        self.Comment = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Region = params.get("Region")
        self.Isp = params.get("Isp")
        self.AsName = params.get("AsName")
        self.AsId = params.get("AsId")
        self.Comment = params.get("Comment")
        self.AddressIp = params.get("AddressIp")


class Ipv6Address(AbstractModel):
    """`IPv6` address information.

    """

    def __init__(self):
        """
        :param Address: `IPv6` address, such as `3402:4e00:20:100:0:8cd9:2a67:71f3`
        :type Address: str
        :param Primary: Whether it is a primary `IP`.
        :type Primary: bool
        :param AddressId: The `ID` of the `EIP` instance, such as `eip-hxlqja90`.
        :type AddressId: str
        :param Description: Message description
        :type Description: str
        :param IsWanIpBlocked: Whether the public IP is blocked.
        :type IsWanIpBlocked: bool
        :param State: `IPv6` address status:
<li>`PENDING`: Creating</li>
<li>`MIGRATING`: Migrating</li>
<li>`DELETING`: Deleting</li>
<li>`AVAILABLE`: Available</li>
        :type State: str
        """
        self.Address = None
        self.Primary = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Primary = params.get("Primary")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")


class Ipv6SubnetCidrBlock(AbstractModel):
    """IPv6 subnet IP range object.

    """

    def __init__(self):
        """
        :param SubnetId: The `ID` of the subnet instance, such as `subnet-pxir56ns`.
        :type SubnetId: str
        :param Ipv6CidrBlock: The `IPv6` subnet IP range, such as `3402:4e00:20:1001::/64`
        :type Ipv6CidrBlock: str
        """
        self.SubnetId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")


class ItemPrice(AbstractModel):
    """The pricing information of a single billing item

    """

    def __init__(self):
        """
        :param UnitPrice: The pay-as-you-go billing method. Unit: CNY.
        :type UnitPrice: float
        :param ChargeUnit: Pay-as-you-go billing method. Value Range: HOUR: Indicates billing by the hour. Scenarios using this hourly billing unit include: Instances postpaid on an hourly basis (POSTPAID_BY_HOUR), and bandwidth postpaid on an hourly basis (BANDWIDTH_POSTPAID_BY_HOUR). GB: Indicates billing on a per-GB basis. Scenarios using this billing unit include: Traffic postpaid on an hourly basis (TRAFFIC_POSTPAID_BY_HOUR).
        :type ChargeUnit: str
        :param OriginalPrice: Original price of the prepaid product. Unit: CNY.
        :type OriginalPrice: float
        :param DiscountPrice: Discount price of the prepaid product. Unit: CNY.
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param SourceInstanceId: The ID of the CVM bound to the ENI, such as `ins-r8hr2upy`.
        :type SourceInstanceId: str
        :param DestinationInstanceId: ID of the destination CVM instance to be migrated.
        :type DestinationInstanceId: str
        """
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress request structure.

    """

    def __init__(self):
        """
        :param SourceNetworkInterfaceId: ID of the ENI instance bound with the private IP, such as `eni-m6dyj72l`.
        :type SourceNetworkInterfaceId: str
        :param DestinationNetworkInterfaceId: ID of the destination ENI instance to be migrated.
        :type DestinationNetworkInterfaceId: str
        :param PrivateIpAddress: The private IP to be migrated, such as 10.0.0.6.
        :type PrivateIpAddress: str
        """
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self.DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.
        :type AddressId: str
        :param AddressName: The EIP name after modification. The maximum length is 20 characters.
        :type AddressName: str
        :param EipDirectConnection: Whether the set EIP is a direct connection EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct connection function.
        :type EipDirectConnection: str
        """
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.EipDirectConnection = params.get("EipDirectConnection")


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressInternetChargeTypeRequest(AbstractModel):
    """ModifyAddressInternetChargeType request structure.

    """

    def __init__(self):
        """
        :param AddressId: Unique EIP ID, such as "eip-xxxx"
        :type AddressId: str
        :param InternetChargeType: The target billing method. It can be `BANDWIDTH_PREPAID_BY_MONTH` or `TRAFFIC_POSTPAID_BY_HOUR`
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: The target bandwidth value
        :type InternetMaxBandwidthOut: int
        :param AddressChargePrepaid: Billing details of monthly-subscribed network bandwidth. This parameter is required if the target billing method is `BANDWIDTH_PREPAID_BY_MONTH`.
        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`
        """
        self.AddressId = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressChargePrepaid = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))


class ModifyAddressInternetChargeTypeResponse(AbstractModel):
    """ModifyAddressInternetChargeType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateAttributeRequest(AbstractModel):
    """ModifyAddressTemplateAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP address template instance ID, such as `ipm-mdunqeb6`.
        :type AddressTemplateId: str
        :param AddressTemplateName: IP address template name.
        :type AddressTemplateName: str
        :param Addresses: Address information, including IP, CIDR and IP address range.
        :type Addresses: list of str
        """
        self.AddressTemplateId = None
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class ModifyAddressTemplateAttributeResponse(AbstractModel):
    """ModifyAddressTemplateAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateGroupAttributeRequest(AbstractModel):
    """ModifyAddressTemplateGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP address template group instance ID, such as `ipmg-2uw6ujo6`.
        :type AddressTemplateGroupId: str
        :param AddressTemplateGroupName: IP address template group name.
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: IP address template instance ID, such as `ipm-mdunqeb6`.
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupId = None
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class ModifyAddressTemplateGroupAttributeResponse(AbstractModel):
    """ModifyAddressTemplateGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth request structure.

    """

    def __init__(self):
        """
        :param AddressIds: List of EIP IDs, such as “eip-xxxx”.
        :type AddressIds: list of str
        :param InternetMaxBandwidthOut: Target bandwidth value adjustment
        :type InternetMaxBandwidthOut: int
        :param StartTime: (Disused) The start time of the monthly bandwidth subscription
        :type StartTime: str
        :param EndTime: (Disused) The end time of the monthly bandwidth subscription
        :type EndTime: str
        """
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAssistantCidrRequest(AbstractModel):
    """ModifyAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.
        :type VpcId: str
        :param NewCidrBlocks: Load CIDR blocks to add. CIDR block set; format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type NewCidrBlocks: list of str
        :param OldCidrBlocks: Load CIDR blocks to delete. CIDR block set; Format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]
        :type OldCidrBlocks: list of str
        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")


class ModifyAssistantCidrResponse(AbstractModel):
    """ModifyAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of secondary CIDR blocks.
Note: This field may return null, indicating that no valid value was found.
        :type AssistantCidrSet: list of AssistantCidr
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyBandwidthPackageAttributeRequest(AbstractModel):
    """ModifyBandwidthPackageAttribute request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package.
        :type BandwidthPackageId: str
        :param BandwidthPackageName: The name of the bandwidth package.
        :type BandwidthPackageName: str
        :param ChargeType: The billing mode of the bandwidth package.
        :type ChargeType: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageName = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.ChargeType = params.get("ChargeType")


class ModifyBandwidthPackageAttributeResponse(AbstractModel):
    """ModifyBandwidthPackageAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttributeRequest(AbstractModel):
    """ModifyCcnAttribute request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param CcnName: The name of the CCN. The maximum length is 60 characters.
        :type CcnName: str
        :param CcnDescription: The description of the CCN. The maximum length is 100 characters.
        :type CcnDescription: str
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")


class ModifyCcnAttributeResponse(AbstractModel):
    """ModifyCcnAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnRegionBandwidthLimitsTypeRequest(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType request structure.

    """

    def __init__(self):
        """
        :param CcnId: CCN instance ID.
        :type CcnId: str
        :param BandwidthLimitType: CCN bandwidth limit type. INTER_REGION_LIMIT: limit between regions. OUTER_REGION_LIMIT: region egress limit.
        :type BandwidthLimitType: str
        """
        self.CcnId = None
        self.BandwidthLimitType = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.BandwidthLimitType = params.get("BandwidthLimitType")


class ModifyCcnRegionBandwidthLimitsTypeResponse(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.
        :type CustomerGatewayId: str
        :param CustomerGatewayName: Customer gateway can be named freely, but the maximum length is 60 characters.
        :type CustomerGatewayName: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectGatewayAttributeRequest(AbstractModel):
    """ModifyDirectConnectGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The unique ID of the direct connect gateway, such as `dcg-9o233uri`.
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: The direct connect gateway name. You can enter any name within 60 characters.
        :type DirectConnectGatewayName: str
        :param CcnRouteType: The CCN route-learning type. Valid values: `BGP` (Automatic learning), `STATIC` (Static, that is, user-configured). You can only modify `CcnRouteType` for a CCN direct connect gateway with BGP enabled.
        :type CcnRouteType: str
        :param ModeType: CCN route publishing method. Valid values: `standard` and `exquisite`. You can only modify `ModeType` for a CCN direct connect gateway.
        :type ModeType: str
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.CcnRouteType = None
        self.ModeType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.CcnRouteType = params.get("CcnRouteType")
        self.ModeType = params.get("ModeType")


class ModifyDirectConnectGatewayAttributeResponse(AbstractModel):
    """ModifyDirectConnectGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFlowLogAttributeRequest(AbstractModel):
    """ModifyFlowLogAttribute request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance
        :type VpcId: str
        :param FlowLogId: The unique ID of the flow log.
        :type FlowLogId: str
        :param FlowLogName: The name of the flow log.
        :type FlowLogName: str
        :param FlowLogDescription: The description of the flow log.
        :type FlowLogDescription: str
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.FlowLogDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.FlowLogDescription = params.get("FlowLogDescription")


class ModifyFlowLogAttributeResponse(AbstractModel):
    """ModifyFlowLogAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGatewayFlowQosRequest(AbstractModel):
    """ModifyGatewayFlowQos request structure.

    """

    def __init__(self):
        """
        :param GatewayId: Gateway instance ID, which currently supports these types:
ID of Direct Connect gateway instance, e.g. `dcg-ltjahce6`;
ID of NAT gateway instance, e.g. `nat-ltjahce6`;
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.
        :type GatewayId: str
        :param Bandwidth: Bandwidth limit value.
        :type Bandwidth: int
        :param IpAddresses: CVM private IP addresses with limited bandwidth.
        :type IpAddresses: list of str
        """
        self.GatewayId = None
        self.Bandwidth = None
        self.IpAddresses = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.IpAddresses = params.get("IpAddresses")


class ModifyGatewayFlowQosResponse(AbstractModel):
    """ModifyGatewayFlowQos response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.
        :type HaVipId: str
        :param HaVipName: `HAVIP` can be named freely, but the maximum length is 60 characters.
        :type HaVipName: str
        """
        self.HaVipId = None
        self.HaVipName = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: The information of the specified private `IPv6` addresses.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayAttributeRequest(AbstractModel):
    """ModifyNatGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param NatGatewayName: The NAT gateway name, such as `test_nat`.
        :type NatGatewayName: str
        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the NAT gateway. Unit: Mbps.
        :type InternetMaxBandwidthOut: int
        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ModifyNatGatewayAttributeResponse(AbstractModel):
    """ModifyNatGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.
        :type NatGatewayId: str
        :param SourceNatRule: The port forwarding rule of the source NAT gateway.
        :type SourceNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`
        :param DestinationNatRule: The port forwarding rule of the destination NAT gateway.
        :type DestinationNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`
        """
        self.NatGatewayId = None
        self.SourceNatRule = None
        self.DestinationNatRule = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceNatRule") is not None:
            self.SourceNatRule = DestinationIpPortTranslationNatRule()
            self.SourceNatRule._deserialize(params.get("SourceNatRule"))
        if params.get("DestinationNatRule") is not None:
            self.DestinationNatRule = DestinationIpPortTranslationNatRule()
            self.DestinationNatRule._deserialize(params.get("DestinationNatRule"))


class ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetDetectRequest(AbstractModel):
    """ModifyNetDetect request structure.

    """

    def __init__(self):
        """
        :param NetDetectId: The ID of a network detection instance, such as `netd-12345678`.
        :type NetDetectId: str
        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.
        :type NetDetectName: str
        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.
        :type DetectDestinationIp: list of str
        :param NextHopType: The type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.
        :type NextHopType: str
        :param NextHopDestination: The next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.
        :type NextHopDestination: str
        :param NetDetectDescription: Network detection description.
        :type NetDetectDescription: str
        """
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")


class ModifyNetDetectResponse(AbstractModel):
    """ModifyNetDetect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclAttributeRequest(AbstractModel):
    """ModifyNetworkAclAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.
        :type NetworkAclId: str
        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.
        :type NetworkAclName: str
        """
        self.NetworkAclId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")


class ModifyNetworkAclAttributeResponse(AbstractModel):
    """ModifyNetworkAclAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclEntriesRequest(AbstractModel):
    """ModifyNetworkAclEntries request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.
        :type NetworkAclId: str
        :param NetworkAclEntrySet: Network ACL rule set.
        :type NetworkAclEntrySet: :class:`tencentcloud.vpc.v20170312.models.NetworkAclEntrySet`
        """
        self.NetworkAclId = None
        self.NetworkAclEntrySet = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclEntrySet") is not None:
            self.NetworkAclEntrySet = NetworkAclEntrySet()
            self.NetworkAclEntrySet._deserialize(params.get("NetworkAclEntrySet"))


class ModifyNetworkAclEntriesResponse(AbstractModel):
    """ModifyNetworkAclEntries response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-pxir56ns`.
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 characters.
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: ENI description can be named freely, but the maximum length is 60 characters.
        :type NetworkInterfaceDescription: str
        :param SecurityGroupIds: The specified security groups to be bound with, such as ['sg-1dd51d'].
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    """ModifyNetworkInterfaceAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: The specified private IP information.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.
        :type GroupName: str
        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.
        :type GroupDescription: str
        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: The security group policy set. SecurityGroupPolicySet object must specify new egress and ingress policies at the same time. SecurityGroupPolicy object does not support custom index (PolicyIndex).
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param SortPolicys: Whether security group sorting is supported. True indicates that security group sorting is supported. If SortPolicys does not exist or is set to False, the security group policy can be modified.
        :type SortPolicys: bool
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.SortPolicys = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.SortPolicys = params.get("SortPolicys")


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateAttributeRequest(AbstractModel):
    """ModifyServiceTemplateAttribute request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port template instance ID, such as `ppm-529nwwj8`.
        :type ServiceTemplateId: str
        :param ServiceTemplateName: Protocol port template name.
        :type ServiceTemplateName: str
        :param Services: It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE.
        :type Services: list of str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class ModifyServiceTemplateAttributeResponse(AbstractModel):
    """ModifyServiceTemplateAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateGroupAttributeRequest(AbstractModel):
    """ModifyServiceTemplateGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: The protocol port template group instance ID, such as `ppmg-ei8hfd9a`.
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: Protocol port template group name.
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: Instance ID of the protocol port template, such as `ppm-4dw6agho`.
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class ModifyServiceTemplateGroupAttributeResponse(AbstractModel):
    """ModifyServiceTemplateGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute request structure.

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID, such as `subnet-pxir56ns`.
        :type SubnetId: str
        :param SubnetName: The subnet name. The maximum length is 60 bytes.
        :type SubnetName: str
        :param EnableBroadcast: Whether the subnet has broadcast enabled.
        :type EnableBroadcast: str
        """
        self.SubnetId = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute request structure.

    """

    def __init__(self):
        """
        :param VpcId: Security group can be named freely, but cannot exceed 60 characters.
        :type VpcId: str
        :param VpcName: VPC can be named freely, but the maximum length is 60 characters.
        :type VpcName: str
        :param EnableMulticast: Whether multicast is enabled. `true`: Enabled. `false`: Off.
        :type EnableMulticast: str
        :param DnsServers: DNS address. A maximum of 4 addresses is supported. The first one is primary server by default, and the rest are secondary servers.
        :type DnsServers: list of str
        :param DomainName: Domain name
        :type DomainName: str
        """
        self.VpcId = None
        self.VpcName = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute request structure.

    """

    def __init__(self):
        """
        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.
        :type VpnConnectionId: str
        :param VpnConnectionName: VPN tunnel can be named freely, but the maximum length is 60 characters.
        :type VpnConnectionName: str
        :param PreShareKey: The pre-shared key.
        :type PreShareKey: str
        :param SecurityPolicyDatabases: The SPD policy group, for example: {"10.0.0.5/24":["172.123.10.5/16"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC.
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE (Internet Key Exchange) configuration. IKE comes with a self-protection mechanism. The network security protocol is configured by the user.
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self.SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param VpnGatewayName: The VPN gateway name. The maximum length is 60 bytes.
        :type VpnGatewayName: str
        :param InstanceChargeType: VPN gateway billing mode. Currently, only the conversion of prepaid (monthly subscription) to postpaid (that is, pay-as-you-go) is supported. That is, the parameters only supports POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InstanceChargeType = params.get("InstanceChargeType")


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayCcnRoutesRequest(AbstractModel):
    """ModifyVpnGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param Routes: The CCN route (IDC IP range) list.
        :type Routes: list of VpngwCcnRoutes
        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.Routes.append(obj)


class ModifyVpnGatewayCcnRoutesResponse(AbstractModel):
    """ModifyVpnGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NatGateway(AbstractModel):
    """NAT gateway object.

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT gateway ID.
        :type NatGatewayId: str
        :param NatGatewayName: NAT gateway name.
        :type NatGatewayName: str
        :param CreatedTime: NAT gateway creation time.
        :type CreatedTime: str
        :param State: The status of the NAT gateway.
 'PENDING': Creating, 'DELETING': Deleting, 'AVAILABLE': Operating, 'UPDATING': Upgrading,
‘FAILED’: Failed.
        :type State: str
        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the gateway. Unit: Mbps.
        :type InternetMaxBandwidthOut: int
        :param MaxConcurrentConnection: The concurrent connections cap of the gateway.
        :type MaxConcurrentConnection: int
        :param PublicIpAddressSet: The public IP object array of the bound NAT gateway.
        :type PublicIpAddressSet: list of NatGatewayAddress
        :param NetworkState: The NAT gateway status. `AVAILABLE`: Operating, `UNAVAILABLE`: Unavailable, `INSUFFICIENT`: Account is in arrears and the service is suspended.
        :type NetworkState: str
        :param DestinationIpPortTranslationNatRuleSet: The port forwarding rules of the NAT gateway.
        :type DestinationIpPortTranslationNatRuleSet: list of DestinationIpPortTranslationNatRule
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param Zone: The availability zone in which the NAT gateway is located.
        :type Zone: str
        :param DirectConnectGatewayIds: IDs of direct connect gateway associated.
        :type DirectConnectGatewayIds: list of str
        :param SubnetId: Subnet ID.
        :type SubnetId: str
        :param TagSet: Tag key-value pair.
        :type TagSet: list of Tag
        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.CreatedTime = None
        self.State = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.PublicIpAddressSet = None
        self.NetworkState = None
        self.DestinationIpPortTranslationNatRuleSet = None
        self.VpcId = None
        self.Zone = None
        self.DirectConnectGatewayIds = None
        self.SubnetId = None
        self.TagSet = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        if params.get("PublicIpAddressSet") is not None:
            self.PublicIpAddressSet = []
            for item in params.get("PublicIpAddressSet"):
                obj = NatGatewayAddress()
                obj._deserialize(item)
                self.PublicIpAddressSet.append(obj)
        self.NetworkState = params.get("NetworkState")
        if params.get("DestinationIpPortTranslationNatRuleSet") is not None:
            self.DestinationIpPortTranslationNatRuleSet = []
            for item in params.get("DestinationIpPortTranslationNatRuleSet"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRuleSet.append(obj)
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")
        self.DirectConnectGatewayIds = params.get("DirectConnectGatewayIds")
        self.SubnetId = params.get("SubnetId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class NatGatewayAddress(AbstractModel):
    """The EIP bound to the NAT gateway

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the Elastic IP (EIP), such as `eip-11112222`.
        :type AddressId: str
        :param PublicIpAddress: The public IP address, such as `123.121.34.33`.
        :type PublicIpAddress: str
        :param IsBlocked: The block status of the resource. `true` indicates the EIP is blocked. `false` indicates that the EIP is not blocked.
        :type IsBlocked: bool
        """
        self.AddressId = None
        self.PublicIpAddress = None
        self.IsBlocked = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.IsBlocked = params.get("IsBlocked")


class NatGatewayDestinationIpPortTranslationNatRule(AbstractModel):
    """The port forwarding rules of the NAT gateway

    """

    def __init__(self):
        """
        :param IpProtocol: Network protocol. Available choices: `TCP`, `UDP`.
        :type IpProtocol: str
        :param PublicIpAddress: EIP.
        :type PublicIpAddress: str
        :param PublicPort: Public port.
        :type PublicPort: int
        :param PrivateIpAddress: Private network address.
        :type PrivateIpAddress: str
        :param PrivatePort: Private network port.
        :type PrivatePort: int
        :param Description: NAT gateway forwarding rule description.
        :type Description: str
        :param NatGatewayId: NAT gateway ID.
Note: This field may return null, indicating no valid value.
        :type NatGatewayId: str
        :param VpcId: VPC ID.
Note: This field may return null, indicating no valid value.
        :type VpcId: str
        :param CreatedTime: The creation time of the NAT gateway forwarding rule.
Note: This field may return null, indicating no valid value.
        :type CreatedTime: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None
        self.NatGatewayId = None
        self.VpcId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")


class NetDetect(AbstractModel):
    """The network detection object.

    """

    def __init__(self):
        """
        :param VpcId: The ID of a VPC instance, such as `vpc-12345678`.
        :type VpcId: str
        :param VpcName: The name of a VPC instance.
        :type VpcName: str
        :param SubnetId: The ID of a subnet instance, such as subnet-12345678.
        :type SubnetId: str
        :param SubnetName: The name of a subnet instance.
        :type SubnetName: str
        :param NetDetectId: The ID of a network detection instance, such as netd-12345678.
        :type NetDetectId: str
        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.
        :type NetDetectName: str
        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.
        :type DetectDestinationIp: list of str
        :param DetectSourceIp: The array of detection source IPv4 addresses automatically allocated by the system. The length is 2.
        :type DetectSourceIp: list of str
        :param NextHopType: Type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.
        :type NextHopType: str
        :param NextHopDestination: Next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.
        :type NextHopDestination: str
        :param NextHopName: The name of the next-hop gateway.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NextHopName: str
        :param NetDetectDescription: Network detection description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetDetectDescription: str
        :param CreateTime: The creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        """
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.DetectSourceIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NextHopName = None
        self.NetDetectDescription = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.DetectSourceIp = params.get("DetectSourceIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NextHopName = params.get("NextHopName")
        self.NetDetectDescription = params.get("NetDetectDescription")
        self.CreateTime = params.get("CreateTime")


class NetDetectIpState(AbstractModel):
    """The verification result of the network detection destination IP address.

    """

    def __init__(self):
        """
        :param DetectDestinationIp: The destination IPv4 address of network detection.
        :type DetectDestinationIp: str
        :param State: The detection result.
0: successful;
-1: no packet loss occurred during routing;
-2: packet loss occurred when outbound traffic is blocked by the ACL;
-3: packet loss occurred when inbound traffic is blocked by the ACL;
-4: other errors.
        :type State: int
        :param Delay: The latency. Unit: ms.
        :type Delay: int
        :param PacketLossRate: The packet loss rate.
        :type PacketLossRate: int
        """
        self.DetectDestinationIp = None
        self.State = None
        self.Delay = None
        self.PacketLossRate = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.State = params.get("State")
        self.Delay = params.get("Delay")
        self.PacketLossRate = params.get("PacketLossRate")


class NetDetectState(AbstractModel):
    """The network detection verification result.

    """

    def __init__(self):
        """
        :param NetDetectId: The ID of a network detection instance, such as netd-12345678.
        :type NetDetectId: str
        :param NetDetectIpStateSet: The array of network detection destination IP verification results.
        :type NetDetectIpStateSet: list of NetDetectIpState
        """
        self.NetDetectId = None
        self.NetDetectIpStateSet = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)


class NetworkAcl(AbstractModel):
    """Network ACL

    """

    def __init__(self):
        """
        :param VpcId: `ID` of the `VPC` instance.
        :type VpcId: str
        :param NetworkAclId: `ID` of the network ACL instance.
        :type NetworkAclId: str
        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.
        :type NetworkAclName: str
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param SubnetSet: Array of subnets associated with the network ACL.
        :type SubnetSet: list of Subnet
        :param IngressEntries: Inbound rules of the network ACL.
        :type IngressEntries: list of NetworkAclEntry
        :param EgressEntries: Outbound rules of the network ACL.
        :type EgressEntries: list of NetworkAclEntry
        """
        self.VpcId = None
        self.NetworkAclId = None
        self.NetworkAclName = None
        self.CreatedTime = None
        self.SubnetSet = None
        self.IngressEntries = None
        self.EgressEntries = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        if params.get("IngressEntries") is not None:
            self.IngressEntries = []
            for item in params.get("IngressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.IngressEntries.append(obj)
        if params.get("EgressEntries") is not None:
            self.EgressEntries = []
            for item in params.get("EgressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.EgressEntries.append(obj)


class NetworkAclEntry(AbstractModel):
    """Network ACL rules.

    """

    def __init__(self):
        """
        :param ModifyTime: Modification time.
        :type ModifyTime: str
        :param Protocol: Protocol. Valid values: TCP, UDP, ICMP, ALL.
        :type Protocol: str
        :param Port: Port. Valid values: all, single port, range. When Protocol takes the value `ALL` or `ICMP`, Port cannot be specified.
        :type Port: str
        :param CidrBlock: IP range or IP address (mutually exclusive).
        :type CidrBlock: str
        :param Ipv6CidrBlock: CIDR block or IPv6 address (mutually exclusive).
        :type Ipv6CidrBlock: str
        :param Action: ACCEPT or DROP.
        :type Action: str
        :param Description: Rule description, which is up to 100 bytes.
        :type Description: str
        """
        self.ModifyTime = None
        self.Protocol = None
        self.Port = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.Action = None
        self.Description = None


    def _deserialize(self, params):
        self.ModifyTime = params.get("ModifyTime")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.Action = params.get("Action")
        self.Description = params.get("Description")


class NetworkAclEntrySet(AbstractModel):
    """Network ACL rule set

    """

    def __init__(self):
        """
        :param Ingress: Inbound rules.
        :type Ingress: list of NetworkAclEntry
        :param Egress: Outbound rules.
        :type Egress: list of NetworkAclEntry
        """
        self.Ingress = None
        self.Egress = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Ingress.append(obj)
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Egress.append(obj)


class NetworkInterface(AbstractModel):
    """ENI

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-f1xjkw1b`.
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: ENI Name
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: ENI description.
        :type NetworkInterfaceDescription: str
        :param SubnetId: Subnet instance ID.
        :type SubnetId: str
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param GroupSet: Bound security group.
        :type GroupSet: list of str
        :param Primary: Whether it is the primary ENI.
        :type Primary: bool
        :param MacAddress: MAC address
        :type MacAddress: str
        :param State: ENI status:
<li>`PENDING`: Creating</li>
<li>`AVAILABLE`: Available</li>
<li>`ATTACHING`: Binding</li>
<li>`DETACHING`: Unbinding</li>
<li>`DELETING`: Deleting</li>
        :type State: str
        :param PrivateIpAddressSet: Private IP information.
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param Attachment: Bound CVM object.
Note: This field may return null, indicating no valid value.
        :type Attachment: :class:`tencentcloud.vpc.v20170312.models.NetworkInterfaceAttachment`
        :param Zone: Availability Zone.
        :type Zone: str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param Ipv6AddressSet: The `IPv6` address list.
        :type Ipv6AddressSet: list of Ipv6Address
        :param TagSet: Tag key-value pair.
        :type TagSet: list of Tag
        :param EniType: The ENI type. 0: ENI. 1: EVM ENI.
        :type EniType: int
        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SubnetId = None
        self.VpcId = None
        self.GroupSet = None
        self.Primary = None
        self.MacAddress = None
        self.State = None
        self.PrivateIpAddressSet = None
        self.Attachment = None
        self.Zone = None
        self.CreatedTime = None
        self.Ipv6AddressSet = None
        self.TagSet = None
        self.EniType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.GroupSet = params.get("GroupSet")
        self.Primary = params.get("Primary")
        self.MacAddress = params.get("MacAddress")
        self.State = params.get("State")
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        if params.get("Attachment") is not None:
            self.Attachment = NetworkInterfaceAttachment()
            self.Attachment._deserialize(params.get("Attachment"))
        self.Zone = params.get("Zone")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.EniType = params.get("EniType")


class NetworkInterfaceAttachment(AbstractModel):
    """Binding relationship of the ENI

    """

    def __init__(self):
        """
        :param InstanceId: CVM instance ID.
        :type InstanceId: str
        :param DeviceIndex: The serial number of ENI in the CVM instance.
        :type DeviceIndex: int
        :param InstanceAccountId: The account information of the CVM owner.
        :type InstanceAccountId: str
        :param AttachTime: Binding time
        :type AttachTime: str
        """
        self.InstanceId = None
        self.DeviceIndex = None
        self.InstanceAccountId = None
        self.AttachTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceIndex = params.get("DeviceIndex")
        self.InstanceAccountId = params.get("InstanceAccountId")
        self.AttachTime = params.get("AttachTime")


class Price(AbstractModel):
    """Price

    """

    def __init__(self):
        """
        :param InstancePrice: Instance price.
        :type InstancePrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        :param BandwidthPrice: Network price.
        :type BandwidthPrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))


class PrivateIpAddressSpecification(AbstractModel):
    """Private IP information

    """

    def __init__(self):
        """
        :param PrivateIpAddress: Private IP address.
        :type PrivateIpAddress: str
        :param Primary: Whether it is a primary IP.
        :type Primary: bool
        :param PublicIpAddress: Public IP address.
        :type PublicIpAddress: str
        :param AddressId: EIP instance ID, such as `eip-11112222`.
        :type AddressId: str
        :param Description: Private IP description.
        :type Description: str
        :param IsWanIpBlocked: Whether the public IP is blocked.
        :type IsWanIpBlocked: bool
        :param State: IP status:
PENDING: Creating
MIGRATING: Migrating
DELETING: Deleting
AVAILABLE: Available
        :type State: str
        """
        self.PrivateIpAddress = None
        self.Primary = None
        self.PublicIpAddress = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.Primary = params.get("Primary")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")


class Quota(AbstractModel):
    """Quota description information

    """

    def __init__(self):
        """
        :param QuotaId: Quota name. Value range:<br><li>`TOTAL_EIP_QUOTA`:EIP quota under the user's current region<br><li>`DAILY_EIP_APPLY`: Number of EIP applications submitted daily under the user's current region<br><li>`DAILY_PUBLIC_IP_ASSIGN`: Number of public IP reassignments under the user's current region.
        :type QuotaId: str
        :param QuotaCurrent: Current count
        :type QuotaCurrent: int
        :param QuotaLimit: Quota
        :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")


class ReferredSecurityGroup(AbstractModel):
    """Referred security groups

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group instance ID.
        :type SecurityGroupId: str
        :param ReferredSecurityGroupIds: IDs of all referred security group instances.
        :type ReferredSecurityGroupIds: list of str
        """
        self.SecurityGroupId = None
        self.ReferredSecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ReferredSecurityGroupIds = params.get("ReferredSecurityGroupIds")


class RejectAttachCcnInstancesRequest(AbstractModel):
    """RejectAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param Instances: The list of instances whose association is rejected.
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class RejectAttachCcnInstancesResponse(AbstractModel):
    """RejectAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses request structure.

    """

    def __init__(self):
        """
        :param AddressIds: The unique ID list of the EIP. The unique ID of an EIP is as follows: `eip-11112222`.
        :type AddressIds: list of str
        """
        self.AddressIds = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemoveBandwidthPackageResourcesRequest(AbstractModel):
    """RemoveBandwidthPackageResources request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package, such as `bwp-xxxx`.
        :type BandwidthPackageId: str
        :param ResourceType: The resource type. Valid values: `Address` and `LoadBalance`.
        :type ResourceType: str
        :param ResourceIds: The resource IP, such as `eip-xxxx` and `lb-xxxx`.
        :type ResourceIds: list of str
        """
        self.BandwidthPackageId = None
        self.ResourceType = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceIds = params.get("ResourceIds")


class RemoveBandwidthPackageResourcesResponse(AbstractModel):
    """RemoveBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewVpnGatewayRequest(AbstractModel):
    """RenewVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: Billing Methods
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class RenewVpnGatewayResponse(AbstractModel):
    """RenewVpnGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`
        :type DirectConnectGatewayId: str
        :param Routes: The list of IDC IP range that must be connected
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class ReplaceDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation request structure.

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID, such as `subnet-3x5lf5q0`. This can be queried using the DescribeSubnets API.
        :type SubnetId: str
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param Routes: Routing policy object. The routing policy ID (RouteId) must be specified.
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set object.
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param OriginalSecurityGroupPolicySet: (Optional) The old policy set of the security group, which is used for log records.
        :type OriginalSecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.OriginalSecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        if params.get("OriginalSecurityGroupPolicySet") is not None:
            self.OriginalSecurityGroupPolicySet = SecurityGroupPolicySet()
            self.OriginalSecurityGroupPolicySet._deserialize(params.get("OriginalSecurityGroupPolicySet"))


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAttachCcnInstancesRequest(AbstractModel):
    """ResetAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param CcnUin: The UIN (root account) to which the CCN belongs.
        :type CcnUin: str
        :param Instances: The list of network instances that re-apply for association.
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.CcnUin = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnUin = params.get("CcnUin")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class ResetAttachCcnInstancesResponse(AbstractModel):
    """ResetAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetNatGatewayConnectionRequest(AbstractModel):
    """ResetNatGatewayConnection request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT gateway ID.
        :type NatGatewayId: str
        :param MaxConcurrentConnection: Concurrent connections cap of the NAT gateway, such as 1000000, 3000000, 10000000.
        :type MaxConcurrentConnection: int
        """
        self.NatGatewayId = None
        self.MaxConcurrentConnection = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")


class ResetNatGatewayConnectionResponse(AbstractModel):
    """ResetNatGatewayConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param RouteTableName: The route table name. The maximum length is 60 characters.
        :type RouteTableName: str
        :param Routes: Routing policy.
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.RouteTableName = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """The structure of information of the bandwidth package.

    """

    def __init__(self):
        """
        :param ResourceType: The bandwidth package resource type, including `Address`, and `LoadBalance`
        :type ResourceType: str
        :param ResourceId: The bandwidth package ID, such as `eip-xxxx` and `lb-xxxx`.
        :type ResourceId: str
        :param AddressIp: The bandwidth package resource IP.
        :type AddressIp: str
        """
        self.ResourceType = None
        self.ResourceId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.AddressIp = params.get("AddressIp")


class ResourceDashboard(AbstractModel):
    """VPC resource dashboard (all resource counts)

    """

    def __init__(self):
        """
        :param VpcId: Vpc instance ID, e.g. vpc-f1xjkw1b.
        :type VpcId: str
        :param SubnetId: Subnet instance ID, such as subnet-bthucmmy.
        :type SubnetId: str
        :param Classiclink: Classiclink.
        :type Classiclink: int
        :param Dcg: Direct Connect gateway.
        :type Dcg: int
        :param Pcx: Peering connection.
        :type Pcx: int
        :param Ip: The total number of used IP addresses.
        :type Ip: int
        :param Nat: NAT gateway.
        :type Nat: int
        :param Vpngw: VPN gateway.
        :type Vpngw: int
        :param FlowLog: Flow log.
        :type FlowLog: int
        :param NetworkDetect: Network probing.
        :type NetworkDetect: int
        :param NetworkACL: Network ACL.
        :type NetworkACL: int
        :param CVM: Cloud Virtual Machine.
        :type CVM: int
        :param LB: Load balancer.
        :type LB: int
        :param CDB: Relational database.
        :type CDB: int
        :param Cmem: TencentDB for Memcached.
        :type Cmem: int
        :param CTSDB: Cloud time series database.
        :type CTSDB: int
        :param MariaDB: TencentDB for MariaDB (TDSQL).
        :type MariaDB: int
        :param SQLServer: TencentDB for SQL Server.
        :type SQLServer: int
        :param Postgres: TencentDB for PostgreSQL.
        :type Postgres: int
        :param NAS: Network attached storage.
        :type NAS: int
        :param Greenplumn: Snova data warehouse.
        :type Greenplumn: int
        :param Ckafka: Cloud Kafka (CKafka).
        :type Ckafka: int
        :param Grocery: Grocery.
        :type Grocery: int
        :param HSM: Data encryption service.
        :type HSM: int
        :param Tcaplus: Game storage - Tcaplus.
        :type Tcaplus: int
        :param Cnas: Cnas.
        :type Cnas: int
        :param TiDB: HTAP database - TiDB.
        :type TiDB: int
        :param Emr: EMR cluster.
        :type Emr: int
        :param SEAL: SEAL.
        :type SEAL: int
        :param CFS: Cloud file storage - CFS.
        :type CFS: int
        :param Oracle: Oracle.
        :type Oracle: int
        :param ElasticSearch: ElasticSearch Service.
        :type ElasticSearch: int
        :param TBaaS: Blockchain service.
        :type TBaaS: int
        :param Itop: Itop.
        :type Itop: int
        :param DBAudit: Cloud database audit.
        :type DBAudit: int
        :param CynosDBPostgres: Enterprise TencentDB - CynosDB for Postgres.
        :type CynosDBPostgres: int
        :param Redis: TencentDB for Redis.
        :type Redis: int
        :param MongoDB: TencentDB for MongoDB.
        :type MongoDB: int
        :param DCDB: A distributed cloud database - TencentDB for TDSQL.
        :type DCDB: int
        :param CynosDBMySQL: An enterprise-grade TencentDB - CynosDB for MySQL.
        :type CynosDBMySQL: int
        :param Subnet: Subnets.
        :type Subnet: int
        :param RouteTable: Route table.
        :type RouteTable: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.Classiclink = None
        self.Dcg = None
        self.Pcx = None
        self.Ip = None
        self.Nat = None
        self.Vpngw = None
        self.FlowLog = None
        self.NetworkDetect = None
        self.NetworkACL = None
        self.CVM = None
        self.LB = None
        self.CDB = None
        self.Cmem = None
        self.CTSDB = None
        self.MariaDB = None
        self.SQLServer = None
        self.Postgres = None
        self.NAS = None
        self.Greenplumn = None
        self.Ckafka = None
        self.Grocery = None
        self.HSM = None
        self.Tcaplus = None
        self.Cnas = None
        self.TiDB = None
        self.Emr = None
        self.SEAL = None
        self.CFS = None
        self.Oracle = None
        self.ElasticSearch = None
        self.TBaaS = None
        self.Itop = None
        self.DBAudit = None
        self.CynosDBPostgres = None
        self.Redis = None
        self.MongoDB = None
        self.DCDB = None
        self.CynosDBMySQL = None
        self.Subnet = None
        self.RouteTable = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Classiclink = params.get("Classiclink")
        self.Dcg = params.get("Dcg")
        self.Pcx = params.get("Pcx")
        self.Ip = params.get("Ip")
        self.Nat = params.get("Nat")
        self.Vpngw = params.get("Vpngw")
        self.FlowLog = params.get("FlowLog")
        self.NetworkDetect = params.get("NetworkDetect")
        self.NetworkACL = params.get("NetworkACL")
        self.CVM = params.get("CVM")
        self.LB = params.get("LB")
        self.CDB = params.get("CDB")
        self.Cmem = params.get("Cmem")
        self.CTSDB = params.get("CTSDB")
        self.MariaDB = params.get("MariaDB")
        self.SQLServer = params.get("SQLServer")
        self.Postgres = params.get("Postgres")
        self.NAS = params.get("NAS")
        self.Greenplumn = params.get("Greenplumn")
        self.Ckafka = params.get("Ckafka")
        self.Grocery = params.get("Grocery")
        self.HSM = params.get("HSM")
        self.Tcaplus = params.get("Tcaplus")
        self.Cnas = params.get("Cnas")
        self.TiDB = params.get("TiDB")
        self.Emr = params.get("Emr")
        self.SEAL = params.get("SEAL")
        self.CFS = params.get("CFS")
        self.Oracle = params.get("Oracle")
        self.ElasticSearch = params.get("ElasticSearch")
        self.TBaaS = params.get("TBaaS")
        self.Itop = params.get("Itop")
        self.DBAudit = params.get("DBAudit")
        self.CynosDBPostgres = params.get("CynosDBPostgres")
        self.Redis = params.get("Redis")
        self.MongoDB = params.get("MongoDB")
        self.DCDB = params.get("DCDB")
        self.CynosDBMySQL = params.get("CynosDBMySQL")
        self.Subnet = params.get("Subnet")
        self.RouteTable = params.get("RouteTable")


class Route(AbstractModel):
    """Routing policy object

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: Destination IP range, such as 112.20.51.0/24. Values cannot be in the VPC IP range.
        :type DestinationCidrBlock: str
        :param GatewayType: Type of the next hop. Currently supported types are:
CVM: CVM of the public gateway type;
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
SSLVPN: sslvpn gateway;
NAT: NAT gateway; 
NORMAL_CVM: normal CVM;
EIP: public IP address of the CVM;
CCN: Cloud Connect Network.
        :type GatewayType: str
        :param GatewayId: Next hop address. You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address.
Important note: When the GatewayType is EIP, the GatewayId has a fixed value `0`
        :type GatewayId: str
        :param RouteId: Routing policy ID. The IPv4 routing policy will have a meaningful value, while the IPv6 routing policy is always 0. We recommend using the unique ID `RouteItemId` for the routing policy.
        :type RouteId: int
        :param RouteDescription: The description of the routing policy.
        :type RouteDescription: str
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param RouteType: The route type. Currently, the following types are supported:
USER: User route;
NETD: Network probe route. When creating a network probe route, the system delivers by default. It cannot be edited or deleted;
CCN: CCN route. The system delivers by default. It cannot be edited or deleted.
Users can only add and operate USER-type routes.
        :type RouteType: str
        :param RouteTableId: Route table instance ID, such as rtb-azd4dt1c.
        :type RouteTableId: str
        :param DestinationIpv6CidrBlock: Destination IPv6 IP range, which cannot be included in VPC IP range, such as 2402:4e00:1000:810b::/64.
        :type DestinationIpv6CidrBlock: str
        :param RouteItemId: Unique routing policy ID.
        :type RouteItemId: str
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None
        self.RouteTableId = None
        self.DestinationIpv6CidrBlock = None
        self.RouteItemId = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteId = params.get("RouteId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationIpv6CidrBlock = params.get("DestinationIpv6CidrBlock")
        self.RouteItemId = params.get("RouteItemId")


class RouteTable(AbstractModel):
    """Route table object

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        :param AssociationSet: The association relationships of the route table.
        :type AssociationSet: list of RouteTableAssociation
        :param RouteSet: IPv4 routing policy set.
        :type RouteSet: list of Route
        :param Main: Whether it is the default route table.
        :type Main: bool
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param TagSet: Tag key-value pairs.
        :type TagSet: list of Tag
        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("AssociationSet") is not None:
            self.AssociationSet = []
            for item in params.get("AssociationSet"):
                obj = RouteTableAssociation()
                obj._deserialize(item)
                self.AssociationSet.append(obj)
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.Main = params.get("Main")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class RouteTableAssociation(AbstractModel):
    """The association relationships of the route table

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID.
        :type SubnetId: str
        :param RouteTableId: Route table instance ID.
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class SecurityGroup(AbstractModel):
    """Security group object

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-ohuuioma`.
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group can be named freely, but cannot exceed 60 characters.
        :type SecurityGroupName: str
        :param SecurityGroupDesc: The remarks for the security group. The maximum length is 100 characters.
        :type SecurityGroupDesc: str
        :param ProjectId: The project id is 0 by default. You can query this in the project management page of the Qcloud console.
        :type ProjectId: str
        :param IsDefault: Whether it is the default security group (which cannot be deleted).
        :type IsDefault: bool
        :param CreatedTime: Security group creation time.
        :type CreatedTime: str
        :param TagSet: Tag key-value pairs.
        :type TagSet: list of Tag
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDesc = None
        self.ProjectId = None
        self.IsDefault = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class SecurityGroupAssociationStatistics(AbstractModel):
    """Statistics on the instances associated with the security group

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group instance ID.
        :type SecurityGroupId: str
        :param CVM: Number of CVM instances.
        :type CVM: int
        :param CDB: Number of database instances.
        :type CDB: int
        :param ENI: Number of ENI instances.
        :type ENI: int
        :param SG: Number of times a security group is referenced by other security groups
        :type SG: int
        :param CLB: Number of load balancer instances.
        :type CLB: int
        :param InstanceStatistics: The binding statistics for all instances.
        :type InstanceStatistics: list of InstanceStatistic
        :param TotalCount: Total count of all resources (excluding resources referenced by security groups).
        :type TotalCount: int
        """
        self.SecurityGroupId = None
        self.CVM = None
        self.CDB = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.CVM = params.get("CVM")
        self.CDB = params.get("CDB")
        self.ENI = params.get("ENI")
        self.SG = params.get("SG")
        self.CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self.InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self.InstanceStatistics.append(obj)
        self.TotalCount = params.get("TotalCount")


class SecurityGroupPolicy(AbstractModel):
    """Security group policy object

    """

    def __init__(self):
        """
        :param PolicyIndex: The index number of security group rules, which dynamically changes with the rules. This parameter can be obtained via the `DescribeSecurityGroupPolicies` API and used with the `Version` field in the returned value of the API.
        :type PolicyIndex: int
        :param Protocol: Protocol. Valid values: TCP, UDP, ICMP, ICMPv6, ALL.
        :type Protocol: str
        :param Port: Port (all, discrete port, range).
        :type Port: str
        :param ServiceTemplate: Protocol port ID or protocol port group ID. ServiceTemplate and Protocol+Port are mutually exclusive.
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateSpecification`
        :param CidrBlock: IP range or IP (mutually exclusive).
        :type CidrBlock: str
        :param Ipv6CidrBlock: The CIDR block or IPv6 (mutually exclusive).
        :type Ipv6CidrBlock: str
        :param SecurityGroupId: The security group instance ID, such as `sg-ohuuioma`.
        :type SecurityGroupId: str
        :param AddressTemplate: IP address ID or IP address group ID.
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateSpecification`
        :param Action: ACCEPT or DROP.
        :type Action: str
        :param PolicyDescription: Security group policy description.
        :type PolicyDescription: str
        :param ModifyTime: The last modification time of the security group.
        :type ModifyTime: str
        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplateSpecification()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplateSpecification()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.Action = params.get("Action")
        self.PolicyDescription = params.get("PolicyDescription")
        self.ModifyTime = params.get("ModifyTime")


class SecurityGroupPolicySet(AbstractModel):
    """Security group policy set

    """

    def __init__(self):
        """
        :param Version: The version of the security group policy. The version number is automatically increased by one each time users update the security policy, to prevent the expiration of updated routing policies. Conflict is ignored if it is left empty.
        :type Version: str
        :param Egress: Outbound policy.
        :type Egress: list of SecurityGroupPolicy
        :param Ingress: Inbound policy.
        :type Ingress: list of SecurityGroupPolicy
        """
        self.Version = None
        self.Egress = None
        self.Ingress = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Egress.append(obj)
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Ingress.append(obj)


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase policy

    """

    def __init__(self):
        """
        :param LocalCidrBlock: Local IP range
        :type LocalCidrBlock: str
        :param RemoteCidrBlock: Opposite IP range
        :type RemoteCidrBlock: list of str
        """
        self.LocalCidrBlock = None
        self.RemoteCidrBlock = None


    def _deserialize(self, params):
        self.LocalCidrBlock = params.get("LocalCidrBlock")
        self.RemoteCidrBlock = params.get("RemoteCidrBlock")


class ServiceTemplate(AbstractModel):
    """Protocol port template

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port instance ID, such as `ppm-f5n1f8da`.
        :type ServiceTemplateId: str
        :param ServiceTemplateName: Template name.
        :type ServiceTemplateName: str
        :param ServiceSet: Protocol port information.
        :type ServiceSet: list of str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.ServiceSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.ServiceSet = params.get("ServiceSet")
        self.CreatedTime = params.get("CreatedTime")


class ServiceTemplateGroup(AbstractModel):
    """Protocol port template group

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: Protocol port template group instance ID, such as `ppmg-2klmrefu`.
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: Protocol port template group name.
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIdSet: Protocol port template instance ID.
        :type ServiceTemplateIdSet: list of str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param ServiceTemplateSet: Protocol port template instance information.
        :type ServiceTemplateSet: list of ServiceTemplate
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIdSet = None
        self.CreatedTime = None
        self.ServiceTemplateSet = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIdSet = params.get("ServiceTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)


class ServiceTemplateSpecification(AbstractModel):
    """Protocol port template

    """

    def __init__(self):
        """
        :param ServiceId: Protocol port ID, such as `ppm-f5n1f8da`.
        :type ServiceId: str
        :param ServiceGroupId: Protocol port group ID, such as `ppmg-f5n1f8da`.
        :type ServiceGroupId: str
        """
        self.ServiceId = None
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupId = params.get("ServiceGroupId")


class SetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """SetCcnRegionBandwidthLimits request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.
        :type CcnId: str
        :param CcnRegionBandwidthLimits: The outbound bandwidth cap of each CCN region.
        :type CcnRegionBandwidthLimits: list of CcnRegionBandwidthLimit
        """
        self.CcnId = None
        self.CcnRegionBandwidthLimits = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("CcnRegionBandwidthLimits") is not None:
            self.CcnRegionBandwidthLimits = []
            for item in params.get("CcnRegionBandwidthLimits"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimits.append(obj)


class SetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """SetCcnRegionBandwidthLimits response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subnet(AbstractModel):
    """Subnet object

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC` instance.
        :type VpcId: str
        :param SubnetId: Subnet instance `ID`, such as `subnet-bthucmmy`.
        :type SubnetId: str
        :param SubnetName: Subnet name.
        :type SubnetName: str
        :param CidrBlock: The `IPv4` `CIDR` of the subnet.
        :type CidrBlock: str
        :param IsDefault: Whether it is the default subnet.
        :type IsDefault: bool
        :param EnableBroadcast: Whether to enable broadcast.
        :type EnableBroadcast: bool
        :param Zone: Availability Zone.
        :type Zone: str
        :param RouteTableId: The route table instance ID, such as `rtb-l2h8d7c2`.
        :type RouteTableId: str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param AvailableIpAddressCount: The number of available IPv4 addresses
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: The `IPv6` `CIDR` of the subnet.
        :type Ipv6CidrBlock: str
        :param NetworkAclId: The associated `ACL`ID
        :type NetworkAclId: str
        :param IsRemoteVpcSnat: Whether it is a `SNAT` address pool subnet.
        :type IsRemoteVpcSnat: bool
        :param TotalIpAddressCount: The total number of IPv4 addresses in the subnet.
        :type TotalIpAddressCount: int
        :param TagSet: Tag key-value pairs
        :type TagSet: list of Tag
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.Zone = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TotalIpAddressCount = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        self.TotalIpAddressCount = params.get("TotalIpAddressCount")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class SubnetInput(AbstractModel):
    """Subnet object

    """

    def __init__(self):
        """
        :param CidrBlock: The `CIDR` of the subnet.
        :type CidrBlock: str
        :param SubnetName: Subnet name.
        :type SubnetName: str
        :param Zone: The availability zone, such as `ap-guangzhou-2`.
        :type Zone: str
        :param RouteTableId: The specified associated route table, such as `rtb-3ryrwzuu`.
        :type RouteTableId: str
        """
        self.CidrBlock = None
        self.SubnetName = None
        self.Zone = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        """
        :param Key: Tag key
Note: This field may return null, indicating no valid value.
        :type Key: str
        :param Value: Tag value
Note: This field may return null, indicating no valid value.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TransformAddressRequest(AbstractModel):
    """TransformAddress request structure.

    """

    def __init__(self):
        """
        :param InstanceId: The ID of the instance with a common public IP to be operated on, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/9389?from_cn_redirect=1) API.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TransformAddressResponse(AbstractModel):
    """TransformAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6AddressesRequest(AbstractModel):
    """UnassignIpv6Addresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: The list of specified `IPv6` addresses. A maximum of 10 can be specified each time.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)


class UnassignIpv6AddressesResponse(AbstractModel):
    """UnassignIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6CidrBlockRequest(AbstractModel):
    """UnassignIpv6CidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param Ipv6CidrBlock: The `IPv6` IP range, such as `3402:4e00:20:1000::/56`
        :type Ipv6CidrBlock: str
        """
        self.VpcId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")


class UnassignIpv6CidrBlockResponse(AbstractModel):
    """UnassignIpv6CidrBlock response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6SubnetCidrBlockRequest(AbstractModel):
    """UnassignIpv6SubnetCidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param Ipv6SubnetCidrBlocks: The `IPv6` subnet IP range list.
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)


class UnassignIpv6SubnetCidrBlockResponse(AbstractModel):
    """UnassignIpv6SubnetCidrBlock response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignPrivateIpAddressesRequest(AbstractModel):
    """UnassignPrivateIpAddresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 each time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class UnassignPrivateIpAddressesResponse(AbstractModel):
    """UnassignPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Vpc(AbstractModel):
    """Virtual Private Cloud (VPC) object.

    """

    def __init__(self):
        """
        :param VpcName: `VPC` name.
        :type VpcName: str
        :param VpcId: `VPC` instance `ID`, such as `vpc-azd4dt1c`.
        :type VpcId: str
        :param CidrBlock: The `IPv4` `CIDR` of the `VPC`.
        :type CidrBlock: str
        :param IsDefault: Whether it is the default `VPC`.
        :type IsDefault: bool
        :param EnableMulticast: Whether multicast is enabled.
        :type EnableMulticast: bool
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param DnsServerSet: `DNS` list.
        :type DnsServerSet: list of str
        :param DomainName: DHCP domain name option value.
        :type DomainName: str
        :param DhcpOptionsId: `DHCP` option set `ID`.
        :type DhcpOptionsId: str
        :param EnableDhcp: Whether `DHCP` is enabled.
        :type EnableDhcp: bool
        :param Ipv6CidrBlock: The `IPv6` `CIDR` of the `VPC`.
        :type Ipv6CidrBlock: str
        :param TagSet: Tag key-value pair
        :type TagSet: list of Tag
        :param AssistantCidrSet: The secondary CIDR block.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssistantCidrSet: list of AssistantCidr
        """
        self.VpcName = None
        self.VpcId = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableMulticast = None
        self.CreatedTime = None
        self.DnsServerSet = None
        self.DomainName = None
        self.DhcpOptionsId = None
        self.EnableDhcp = None
        self.Ipv6CidrBlock = None
        self.TagSet = None
        self.AssistantCidrSet = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableMulticast = params.get("EnableMulticast")
        self.CreatedTime = params.get("CreatedTime")
        self.DnsServerSet = params.get("DnsServerSet")
        self.DomainName = params.get("DomainName")
        self.DhcpOptionsId = params.get("DhcpOptionsId")
        self.EnableDhcp = params.get("EnableDhcp")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)


class VpcIpv6Address(AbstractModel):
    """VPC private IPv6 object.

    """

    def __init__(self):
        """
        :param Ipv6Address: `VPC` private `IPv6` address
        :type Ipv6Address: str
        :param CidrBlock: The `IPv6` `CIDR` belonging to the subnet.
        :type CidrBlock: str
        :param Ipv6AddressType: `IPv6` type.
        :type Ipv6AddressType: str
        :param CreatedTime: `IPv6` application time.
        :type CreatedTime: str
        """
        self.Ipv6Address = None
        self.CidrBlock = None
        self.Ipv6AddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ipv6Address = params.get("Ipv6Address")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6AddressType = params.get("Ipv6AddressType")
        self.CreatedTime = params.get("CreatedTime")


class VpcPrivateIpAddress(AbstractModel):
    """VPC private IP object.

    """

    def __init__(self):
        """
        :param PrivateIpAddress: `VPC` private `IP`.
        :type PrivateIpAddress: str
        :param CidrBlock: The `CIDR` belonging to the subnet.
        :type CidrBlock: str
        :param PrivateIpAddressType: Private `IP` type.
        :type PrivateIpAddressType: str
        :param CreatedTime: `IP` application time.
        :type CreatedTime: str
        """
        self.PrivateIpAddress = None
        self.CidrBlock = None
        self.PrivateIpAddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.CidrBlock = params.get("CidrBlock")
        self.PrivateIpAddressType = params.get("PrivateIpAddressType")
        self.CreatedTime = params.get("CreatedTime")


class VpnConnection(AbstractModel):
    """VPN tunnel object.

    """

    def __init__(self):
        """
        :param VpnConnectionId: Tunnel instance ID.
        :type VpnConnectionId: str
        :param VpnConnectionName: Tunnel name.
        :type VpnConnectionName: str
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param VpnGatewayId: The ID of the VPN gateway instance.
        :type VpnGatewayId: str
        :param CustomerGatewayId: Customer gateway instance ID.
        :type CustomerGatewayId: str
        :param PreShareKey: The pre-shared key.
        :type PreShareKey: str
        :param VpnProto: Tunnel transmission protocol.
        :type VpnProto: str
        :param EncryptProto: Tunnel encryption protocol.
        :type EncryptProto: str
        :param RouteType: Route Type.
        :type RouteType: str
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param State: Production status of the tunnel. PENDING: Creating; AVAILABLE: Running; DELETING: Deleting.
        :type State: str
        :param NetStatus: Connection status of the tunnel. AVAILABLE: Connected.
        :type NetStatus: str
        :param SecurityPolicyDatabaseSet: SPD.
        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE options.
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSEC options.
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.PreShareKey = None
        self.VpnProto = None
        self.EncryptProto = None
        self.RouteType = None
        self.CreatedTime = None
        self.State = None
        self.NetStatus = None
        self.SecurityPolicyDatabaseSet = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.PreShareKey = params.get("PreShareKey")
        self.VpnProto = params.get("VpnProto")
        self.EncryptProto = params.get("EncryptProto")
        self.RouteType = params.get("RouteType")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.NetStatus = params.get("NetStatus")
        if params.get("SecurityPolicyDatabaseSet") is not None:
            self.SecurityPolicyDatabaseSet = []
            for item in params.get("SecurityPolicyDatabaseSet"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabaseSet.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class VpnGateway(AbstractModel):
    """VPN gateway object.

    """

    def __init__(self):
        """
        :param VpnGatewayId: Gateway instance ID.
        :type VpnGatewayId: str
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param VpnGatewayName: Gateway instance name.
        :type VpnGatewayName: str
        :param Type: Gateway instance type. Valid values: 'IPSEC', 'SSL', and 'CCN'.
        :type Type: str
        :param State: Gateway instance status. 'PENDING': Creating; 'DELETING': Deleting; 'AVAILABLE': Running.
        :type State: str
        :param PublicIpAddress: Gateway public IP.
        :type PublicIpAddress: str
        :param RenewFlag: Gateway renewal type: 'NOTIFY_AND_MANUAL_RENEW': Manual renewal. 'NOTIFY_AND_AUTO_RENEW': Automatic renewal. 'NOT_NOTIFY_AND_NOT_RENEW': No renewal after expiration.
        :type RenewFlag: str
        :param InstanceChargeType: Gateway billing type: POSTPAID_BY_HOUR: Postpaid by hour; PREPAID: Prepaid.
        :type InstanceChargeType: str
        :param InternetMaxBandwidthOut: Outbound bandwidth of gateway.
        :type InternetMaxBandwidthOut: int
        :param CreatedTime: Creation Time.
        :type CreatedTime: str
        :param ExpiredTime: Expiration time of the prepaid gateway.
        :type ExpiredTime: str
        :param IsAddressBlocked: Whether the public IP is blocked.
        :type IsAddressBlocked: bool
        :param NewPurchasePlan: Change of billing method. PREPAID_TO_POSTPAID: Monthly subscription prepaid to postpaid by hour.
        :type NewPurchasePlan: str
        :param RestrictState: Gateway billing status. PROTECTIVELY_ISOLATED: Instance is isolated; NORMAL: Normal.
        :type RestrictState: str
        :param Zone: The availability zone, such as `ap-guangzhou-2`
        :type Zone: str
        :param VpnGatewayQuotaSet: Gateway bandwidth quota information.
        :type VpnGatewayQuotaSet: list of VpnGatewayQuota
        :param Version: Gateway instance version.
        :type Version: str
        :param NetworkInstanceId: CCN instance ID when the value of Type is CCN.
        :type NetworkInstanceId: str
        """
        self.VpnGatewayId = None
        self.VpcId = None
        self.VpnGatewayName = None
        self.Type = None
        self.State = None
        self.PublicIpAddress = None
        self.RenewFlag = None
        self.InstanceChargeType = None
        self.InternetMaxBandwidthOut = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.IsAddressBlocked = None
        self.NewPurchasePlan = None
        self.RestrictState = None
        self.Zone = None
        self.VpnGatewayQuotaSet = None
        self.Version = None
        self.NetworkInstanceId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.Type = params.get("Type")
        self.State = params.get("State")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.RenewFlag = params.get("RenewFlag")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.IsAddressBlocked = params.get("IsAddressBlocked")
        self.NewPurchasePlan = params.get("NewPurchasePlan")
        self.RestrictState = params.get("RestrictState")
        self.Zone = params.get("Zone")
        if params.get("VpnGatewayQuotaSet") is not None:
            self.VpnGatewayQuotaSet = []
            for item in params.get("VpnGatewayQuotaSet"):
                obj = VpnGatewayQuota()
                obj._deserialize(item)
                self.VpnGatewayQuotaSet.append(obj)
        self.Version = params.get("Version")
        self.NetworkInstanceId = params.get("NetworkInstanceId")


class VpnGatewayQuota(AbstractModel):
    """VPN gateway quota object

    """

    def __init__(self):
        """
        :param Bandwidth: The bandwidth quota.
        :type Bandwidth: int
        :param Cname: The bandwidth quota name in Chinese.
        :type Cname: str
        :param Name: The bandwidth quota name in English.
        :type Name: str
        """
        self.Bandwidth = None
        self.Cname = None
        self.Name = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Cname = params.get("Cname")
        self.Name = params.get("Name")


class VpngwCcnRoutes(AbstractModel):
    """Information on VPN gateway-based CCN routes.

    """

    def __init__(self):
        """
        :param RouteId: Route ID
        :type RouteId: str
        :param Status: Enable the route or not
ENABLE: enable the route
DISABLE: do not enable the route
        :type Status: str
        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")